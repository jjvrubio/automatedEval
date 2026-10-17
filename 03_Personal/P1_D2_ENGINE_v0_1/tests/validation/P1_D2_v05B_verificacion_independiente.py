#!/usr/bin/env python3
"""Verificador independiente de los artefactos P1.D2 v0.5B frente a v0.5A.
No consulta SEC, no ejecuta el motor, no modifica originales.
"""
from __future__ import annotations
import csv, hashlib, re
from collections import Counter,defaultdict
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def baseline(name):
    return name if (ROOT/name).exists() else name.replace('.csv','(1).csv')

FILES = {'resA':baseline('D2_results_v05A.csv'),'resB':'D2_results_v05B.csv',
         'uniA':baseline('P1_universe_v05A.csv'),'uniB':'P1_universe_v05B.csv',
         'provA':baseline('D2_provenance_v05A.csv'),'provB':'D2_provenance_v05B.csv',
         'audit':'D2_flag_consistency_audit_v05B.csv','diag':'D2_diagnostics_v05B.md',
         'report':'CODEX_TASK_05B_REPORT.md'}

def rows(name):
    with (ROOT / FILES[name]).open(encoding='utf-8-sig',newline='') as fh:
        r=csv.DictReader(fh)
        return list(r),list(r.fieldnames or [])

def scalar(x):return Decimal(x)
def boo(x):
    assert x in ('True','False','true','false'),f'booleano inválido {x!r}'
    return x.lower()=='true'
def approx(x,y):
    a,b=scalar(x),scalar(y)
    return abs(a-b) <= Decimal('0.00000001')*max(Decimal(1),abs(a),abs(b))

def unique_index(data):
    ix={x['ticker']:x for x in data}
    assert len(ix)==len(data),'Ticker duplicado'
    return ix

def run():
    checks=[]
    def ok(label,fn):
        try:fn();checks.append((label,'PASS',''))
        except Exception as exc: checks.append((label,'FAIL',str(exc)))

    rsA,cA=rows('resA');rsB,cB=rows('resB')
    unA,uA=rows('uniA');unB,uB=rows('uniB')
    pvA,pA=rows('provA');pvB,pB=rows('provB')
    au,ac=rows('audit')
    old=unique_index(rsA);new=unique_index(rsB)
    old_u=unique_index(unA);new_u=unique_index(unB)
    audits=unique_index(au)
    diag=(ROOT/FILES['diag']).read_text(encoding='utf8')
    report=(ROOT/FILES['report']).read_text(encoding='utf8')

    def check_hashes():
        entries=re.findall(r'^([0-9a-f]{64})\s+output/([^\s]+)$',report,re.M)
        assert len(entries)==5,f'reporte lista {len(entries)} hashes en lugar de cinco'
        for exp,filename in entries:
            assert (ROOT/filename).is_file(),f'archivo no existe: {filename}'
            got=hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()
            assert got==exp,f'SHA diferente: {filename}'
    ok('SHA256 de cinco outputs',check_hashes)

    def preserve_universe():
        assert len(new_u)==len(old_u)==50
        assert set(new_u)==set(old_u)
        assert uA==uB
        for k,r in old_u.items():
            for col in uA:
                if col not in ('engine_version','task'):
                    assert r[col]==new_u[k][col],f'Universo modificado {k}.{col}'
        assert all(r['engine_version']=='0.5B' and r['task']=='CODEX_TASK_05B' for r in new_u.values())
    ok('Universo intacto y metadatos v0.5B',preserve_universe)

    changed=[]
    def preserve_results():
        assert set(old)==set(new) and len(new)==50
        assert set(cA).issubset(cB)
        assert set(cB)-set(cA)=={'d2_evaluation_status','d2_evaluation_reason'}
        for k,r in old.items():
            for col in cA:
                if r[col]!=new[k][col]:
                    changed.append((k,col,r[col],new[k][col]))
                    assert col in ('engine_version','task','raw_d2_signal','eligible_d2_signal'),f'Cambio no autorizado: {k}.{col}'
            assert new[k]['engine_version']=='0.5B' and new[k]['task']=='CODEX_TASK_05B'
            assert new[k]['d2_engine_version']=='0.3'
        assert [(k,col,before,after) for k,col,before,after in changed if col in ('raw_d2_signal','eligible_d2_signal')]==[
            ('AAON','raw_d2_signal','False','True'),('AAON','eligible_d2_signal','False','True')],f'Cambiaron otros flags: {changed}'
    ok('Resultados económicos inmóviles; sólo AAON cambia dos indicadores',preserve_results)

    def provenance_same():
        assert set(pA).issubset(pB)
        assert set(pB)-set(pA)=={'engine_version','d2_engine_version','task'}
        assert Counter(tuple(r[col] for col in pA) for r in pvA)==Counter(tuple(r[col] for col in pA) for r in pvB),'Procedencia SEC modificada'
        assert all(r['engine_version']=='0.5B' and r['d2_engine_version']=='0.3' and r['task']=='CODEX_TASK_05B' for r in pvB)
    ok('189 registros de procedencia originales conservados',provenance_same)

    def verify_flags():
        assert set(new)==set(audits)
        for k,r in new.items():
            c,s,raw,elig=map(boo,[r[x] for x in ['candidate_d2','d2_signal','raw_d2_signal','eligible_d2_signal']])
            assert c==s==raw, f'{k}: candidate/d2/raw no equivalentes'
            assert elig==(s and r['universe_eligible']=='True' and r['freshness_status']=='fresh'),f'{k}: eligible_d2 incorrecto'
            ar=audits[k]
            assert ar['consistency_status']=='consistent' and not ar['consistency_reason'], f'{k}: audit no consistente'
            for fld in ('candidate_d2','d2_signal','raw_d2_signal','eligible_d2_signal','universe_eligible','freshness_status','latest_fy_resolution_status','status'):
                assert r[fld]==ar[fld], f'{k}: auditoría discrepante en {fld}'
            assert r['universe_eligible']==new_u[k]['universe_eligible']
            assert r['revenue_eligibility']==new_u[k]['revenue_eligibility']
            evaluated=r['d2_evaluation_status']=='evaluated'
            assert evaluated==(r['freshness_status']=='fresh'),f'{k}: estado evaluación/frescura inconsistente'
            assert (not r['d2_evaluation_reason']) if evaluated else bool(r['d2_evaluation_reason']),f'{k}: razón de evaluación inconsistente'
    ok('50 invariantes de señal y audit CSV',verify_flags)

    def calculations():
        prov=defaultdict(list)
        for row in pvB:
            if row['provenance_role'].lower()=='d2_calculation':
                prov[(row['ticker'],row['metric'],row['end'])].append(row)
        nfresh=0
        for k,r in new.items():
            if r['freshness_status']!='fresh':
                assert not boo(r['d2_signal']) and not boo(r['raw_d2_signal']) and not boo(r['eligible_d2_signal'])
                continue
            nfresh+=1
            assert r['latest_fy_resolution_status']=='resolved' and r['universe_eligible']=='True'
            R,R0,O,O0=[scalar(r[z]) for z in ('revenue_fy_t','revenue_fy_t_minus_1','operating_income_fy_t','operating_income_fy_t_minus_1')]
            assert R>0 and R0>0
            growth=R/R0-1; om=O/R; om0=O0/R0; delta=100*(om-om0)
            for field,val in [('revenue_growth_fy_yoy',growth),('operating_margin_fy_t',om),('operating_margin_fy_t_minus_1',om0),('om_delta_pp',delta)]:
                assert approx(r[field],val),f'{k}: {field} no reconcilia'
            assert boo(r['d2_signal'])==(growth>=Decimal('0.10') and delta<=Decimal('-2')),f'{k}: umbral incorrecto'
            for metric,end,value in [('revenue',r['fy_t_end'],R),('revenue',r['fy_t_minus_1_end'],R0),('operating_income',r['fy_t_end'],O),('operating_income',r['fy_t_minus_1_end'],O0)]:
                facts=prov[(k,metric,end)]
                assert len(facts)==1 and approx(facts[0]['value'],value),f'{k}: procedencia {metric} {end}'
        assert nfresh==38
    ok('38 cálculos D2 contra 152 registros de procedencia',calculations)

    def metrics():
        nt=sum(x['universe_eligible']=='True' for x in unB)
        nf=sum(x['universe_eligible']=='False' for x in unB)
        nu=sum(x['universe_eligible']=='unknown' for x in unB)
        nfr=sum(x['freshness_status']=='fresh' for x in rsB)
        nraw=sum(boo(x['raw_d2_signal']) for x in rsB)
        nelig=sum(boo(x['eligible_d2_signal']) for x in rsB)
        assert (nt,nf,nu,nfr,nraw,nelig)==(40,7,3,38,3,3)
        for key,value in [('N_input',50),('N_universe_eligible',40),('N_universe_ineligible',7),('N_universe_unknown',3),('N_fresh_eligible_processable',38),('N_raw_D2_signals',3),('N_eligible_D2_signals',3),('N_flag_inconsistencies',0)]:
            m=re.search(r'^'+re.escape(key)+r':\s*(\d+)\s*$',diag,re.M)
            assert m and int(m.group(1))==value,key
        for key,value in [('UniverseResolutionRate','94.0'),('EligibleFreshCoverage','95.0')]:
            m=re.search(r'^'+re.escape(key)+r':\s*([0-9.]+)%\s*$',diag,re.M)
            assert m and m.group(1)==value,key
        assert sorted(x['ticker'] for x in rsB if boo(x['eligible_d2_signal']))==['AAON','CXT','FUN']
    ok('Diagnóstico v0.5B y tres señales',metrics)

    def categorical():
        assert Counter(r['consistency_status'] for r in au)=={'consistent':50}
        assert Counter(r['d2_evaluation_status'] for r in rsB)=={'evaluated':38,'not_evaluated':12}
        assert {r['ticker'] for r in rsB if r['status']=='missing_operating_income'}=={'CNX'}
        assert {r['ticker'] for r in rsB if r['status']=='latest_fy_unresolved'}=={'IP'}
        assert {r['ticker'] for r in rsB if r['universe_eligible']=='unknown'}=={'EMAT','PXED','RRC'}
    ok('CNX, IP y tres desconocidos correctamente no evaluados',categorical)

    nfail=sum(c[1]=='FAIL' for c in checks)
    print('AUDITOR INDEPENDIENTE P1.D2 v0.5B')
    for name,result,err in checks:print(f'{result}: {name}'+(f' :: {err}' if err else ''))
    print(f'CHECKS: {len(checks)} | FAILURES: {nfail} | READY_FOR_SIGNAL_TRIAGE: {"PASS" if nfail==0 else "BLOCKED"}')
    print('CAVEAT: pruebas pytest reportadas por Codex, no ejecutadas contra el código fuente en esta sesión.')
    print('CAVEAT: la v0.5B omite algunas métricas narrativas de diagnóstico v0.5A; no afecta consistencia técnica del CSV.')
    return 0 if nfail==0 else 1
if __name__=='__main__':raise SystemExit(run())
