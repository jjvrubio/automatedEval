#!/usr/bin/env python3
"""Obsidian Bridge Vault Manager 1.0: catalog administration only; no vault writes."""
import argparse
import datetime
import json
import os
import re
import shutil
import socket
import sys
import tempfile
from pathlib import Path

VALID_ID = re.compile(r'^[a-z][a-z0-9-]*$')
SUPPORTED_SCHEMA_VERSIONS = {'1.0-draft', '1.0', '1.0.1'}
SUPPORTED_STATUSES = {'inventory_only_not_enforced', 'NOT_ENFORCED'}
SUPPORTED_ACCESS = {'R0', 'R1_candidate', 'R1', 'R2', 'R3', 'R4'}
POLICY_KEYS = {'access', 'writes_enabled', 'symlinks', 'nested_vaults', 'private_config'}
VAULT_KEYS = {'id', 'relative_path', 'connection', 'access'}
CONNECTION_KEYS = {'host', 'https_port', 'credential_ref'}


def schema_errors(data):
    errors = []
    if not isinstance(data, dict):
        return ['catalog must be a JSON object']
    if data.get('schema_version') not in SUPPORTED_SCHEMA_VERSIONS:
        errors.append('schema_version is unsupported or missing')
    if data.get('status') not in SUPPORTED_STATUSES:
        errors.append('status must indicate an unenforced inventory')
    if not isinstance(data.get('root'), str) or not data['root'].strip():
        errors.append('root must be a non-empty string')
    policy = data.get('default_policy')
    if not isinstance(policy, dict):
        errors.append('default_policy must be an object')
    else:
        missing = POLICY_KEYS - policy.keys()
        if missing:
            errors.append('default_policy missing: ' + ', '.join(sorted(missing)))
        if policy.get('access') not in SUPPORTED_ACCESS:
            errors.append('default_policy.access is invalid')
        if type(policy.get('writes_enabled')) is not bool:
            errors.append('default_policy.writes_enabled must be boolean')
        if policy.get('symlinks') != 'deny':
            errors.append('default_policy.symlinks must be deny')
        if policy.get('nested_vaults') != 'exclude':
            errors.append('default_policy.nested_vaults must be exclude')
        if policy.get('private_config') != 'deny':
            errors.append('default_policy.private_config must be deny')
    vaults = data.get('vaults')
    if not isinstance(vaults, list):
        errors.append('vaults must be an array')
        return errors
    for i, vault in enumerate(vaults):
        prefix = f'vault[{i}]'
        if not isinstance(vault, dict):
            errors.append(f'{prefix} must be an object')
            continue
        if not isinstance(vault.get('id'), str) or not VALID_ID.fullmatch(vault['id']):
            errors.append(f'{prefix}: invalid id')
        if not isinstance(vault.get('relative_path'), str) or not vault['relative_path']:
            errors.append(f'{prefix}: relative_path must be a non-empty string')
        if vault.get('id') == 'documents-root':
            if vault.get('relative_path') != '.':
                errors.append('documents-root must use relative_path "."')
            if 'connection' in vault:
                errors.append('documents-root is organizational and cannot have a connection')
        if vault.get('access') not in SUPPORTED_ACCESS:
            errors.append(f'{prefix}: access is invalid')
        connection = vault.get('connection')
        if connection is not None:
            if not isinstance(connection, dict):
                errors.append(f'{prefix}: connection must be an object')
                continue
            missing = CONNECTION_KEYS - connection.keys()
            if missing:
                errors.append(f'{prefix}: connection missing: ' + ', '.join(sorted(missing)))
            if connection.get('host') != '127.0.0.1':
                errors.append(f'{prefix}: connection.host must be 127.0.0.1')
            port = connection.get('https_port')
            if type(port) is not int or not (1024 <= port <= 65535):
                errors.append(f'{prefix}: connection.https_port is invalid')
            if not isinstance(connection.get('credential_ref'), str) or not connection['credential_ref'].strip():
                errors.append(f'{prefix}: connection.credential_ref is required')
    return errors

def load_catalog(path):
    with path.open(encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, dict) or not isinstance(data.get('vaults'), list):
        raise ValueError('Expected JSON object with a vaults array')
    return data

def within(path, root):
    return path == root or root in path.parents


def has_symlink_component(root, relative_path):
    current = root
    for component in relative_path.parts:
        current /= component
        if current.is_symlink():
            return True
    return False


def display_scope(vault_id, access, nested):
    if vault_id == 'documents-root':
        return 'ORGANIZATIONAL'
    if nested:
        return 'NOT_OPERATIONAL_NESTED'
    return access


def report(data, inspect_fs=True):
    problems=[]; warnings=[]; rows=[]
    problems.extend(schema_errors(data))
    if problems:
        return rows, problems, warnings
    base=Path(os.path.expanduser(data['root']))
    if not base.is_absolute(): problems.append('root must be an absolute directory (or start with ~)')
    root=base.resolve(strict=False)
    if inspect_fs and not root.is_dir(): warnings.append(f'root not available on this computer: {root}')
    ids=set(); paths={}; ports={}; creds={}
    for i,v in enumerate(data['vaults']):
        if not isinstance(v,dict): problems.append(f'vault[{i}] not an object');continue
        vid=v.get('id'); rel=v.get('relative_path')
        if not isinstance(vid,str) or not VALID_ID.fullmatch(vid): problems.append(f'vault[{i}]: invalid id'); continue
        if vid in ids: problems.append(f'duplicate id: {vid}')
        ids.add(vid)
        if not isinstance(rel,str): problems.append(f'{vid}: missing relative_path');continue
        p=Path(rel)
        if p.is_absolute() or '..' in p.parts: problems.append(f'{vid}: unsafe relative_path');continue
        target=(root/p).resolve(strict=False)
        if not within(target,root): problems.append(f'{vid}: path escapes root');continue
        if target in paths: problems.append(f'{vid}: duplicate path shared with {paths[target]}')
        paths[target]=vid
        if inspect_fs:
            if not target.is_dir(): warnings.append(f'{vid}: directory not found: {target}')
            elif not (target/'.obsidian').is_dir(): warnings.append(f'{vid}: .obsidian not found')
        if has_symlink_component(root, p):
            problems.append(f'{vid}: vault path contains a symlink')
        conn=v.get('connection')
        if conn is not None:
            if not isinstance(conn,dict): problems.append(f'{vid}: connection must be object')
            else:
                host=conn.get('host'); port=conn.get('https_port'); cred=conn.get('credential_ref')
                if host!='127.0.0.1': problems.append(f'{vid}: host must be 127.0.0.1')
                if type(port) is not int or not (1024 <= port <= 65535): problems.append(f'{vid}: invalid https_port')
                elif port in ports: problems.append(f'{vid}: port {port} also used by {ports[port]}')
                else: ports[port]=vid
                if not isinstance(cred,str) or not cred.strip(): problems.append(f'{vid}: missing credential_ref')
                elif cred in creds: problems.append(f'{vid}: credential_ref shared with {creds[cred]}')
                else: creds[cred]=vid
        rows.append((vid,rel,conn.get('https_port') if isinstance(conn,dict) else None,v.get('access','undefined')))
    nested_ids = set()
    for p,vid in paths.items():
        parents=[(q,pid) for q,pid in paths.items() if q!=p and q in p.parents]
        operational_parents = [pid for q,pid in parents if pid != 'documents-root']
        if operational_parents:
            nested_ids.add(vid)
    pol=data['default_policy']
    if pol.get('writes_enabled') is not False: problems.append('default_policy.writes_enabled must remain false')
    if pol.get('access')!='R0': warnings.append('default access is not R0')
    display_rows = [(vid, rel, port, display_scope(vid, access, vid in nested_ids))
                    for vid, rel, port, access in rows]
    return display_rows,problems,warnings

def save_atomic(path,data):
    stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup=path.with_name(path.name+'.bak-'+stamp)
    suffix = 1
    while backup.exists():
        backup = path.with_name(path.name + f'.bak-{stamp}-{suffix}')
        suffix += 1
    shutil.copy2(path,backup)
    fd,tmp=tempfile.mkstemp(dir=str(path.parent),prefix='.vault-manager-',suffix='.tmp')
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
        os.chmod(tmp,0o600)
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)
    return backup

def check_port(port):
    try:
        with socket.create_connection(('127.0.0.1',port),timeout=0.7): return 'LISTENING (TCP only; vault identity not verified)'
    except OSError: return 'NOT_LISTENING'

def main():
    ap=argparse.ArgumentParser(description='Manage Obsidian Bridge catalog; does not edit vault contents')
    ap.add_argument('--catalog',type=Path,default=Path(__file__).with_name('catalog.json'))
    sub=ap.add_subparsers(dest='action',required=True)
    sub.add_parser('validate');sub.add_parser('list');sub.add_parser('status')
    add=sub.add_parser('set-connection',help='Modify only catalog with backup; not Codex')
    add.add_argument('vault_id');add.add_argument('--port',required=True,type=int)
    add.add_argument('--credential-ref',required=True)
    add.add_argument('--host',default='127.0.0.1')
    args=ap.parse_args()
    try:
        data=load_catalog(args.catalog)
        if args.action=='set-connection':
            found=[v for v in data['vaults'] if v.get('id')==args.vault_id]
            if len(found)!=1: raise ValueError('vault ID must exist exactly once')
            found[0]['connection']={'host':args.host,'https_port':args.port,'credential_ref':args.credential_ref}
            rows,errors,warnings=report(data,inspect_fs=False)
            if errors: raise ValueError('Refusing update: '+'; '.join(errors))
            backup=save_atomic(args.catalog,data)
            print(f'UPDATED CATALOG: {args.catalog}\nBACKUP: {backup}\nNo vault files or Codex settings modified.')
            return 0
        rows,errors,warnings=report(data)
        if args.action=='list':
            print('VAULT ID                        PORT    POLICY        RELATIVE PATH')
            for vid,rel,port,access in rows: print(f'{vid:31} {str(port or "-"):7} {str(access):13} {rel}')
        elif args.action=='status':
            print('Configured endpoints (TCP check only; no authentication or vault content read):')
            for vid,rel,port,access in rows:
                if port: print(f'{vid}: 127.0.0.1:{port} — {check_port(port)}')
        print(f'Catalog records: {len(rows)} | Errors: {len(errors)} | Warnings: {len(warnings)}')
        for x in errors: print('ERROR:',x)
        for x in warnings: print('WARNING:',x)
        print('POLICIES ARE DECLARATIVE — NOT ENFORCED BY THIS TOOL')
        return 2 if errors else 0
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print('ERROR:',exc,file=sys.stderr);return 2
if __name__=='__main__': raise SystemExit(main())
