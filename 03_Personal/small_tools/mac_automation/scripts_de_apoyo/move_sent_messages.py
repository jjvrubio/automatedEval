#!/usr/bin/env python3
"""
Mueve mensajes desde la carpeta de enviados a otra carpeta en Mail.app o Outlook (macOS).

Criterios soportados:
- Aparición de una cadena en el asunto (--subject-contains)
- Antigüedad en días (--older-than-days)
- Todos los mensajes (--all)
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


MAIL_SCRIPT = r'''
on _normalizePath(pathText)
    set oldTIDs to AppleScript's text item delimiters
    set AppleScript's text item delimiters to "/"
    set rawItems to text items of pathText
    set AppleScript's text item delimiters to oldTIDs

    set cleanedItems to {}
    repeat with i in rawItems
        set oneItem to (contents of i) as text
        if oneItem is not "" then set end of cleanedItems to oneItem
    end repeat

    if (count of cleanedItems) is 0 then return ""

    set AppleScript's text item delimiters to "/"
    set cleanedPath to cleanedItems as text
    set AppleScript's text item delimiters to oldTIDs
    return cleanedPath
end _normalizePath

on _splitPath(pathText)
    set cleanedPath to my _normalizePath(pathText)
    if cleanedPath is "" then error "Ruta de carpeta vacía."

    set oldTIDs to AppleScript's text item delimiters
    set AppleScript's text item delimiters to "/"
    set pathItems to text items of cleanedPath
    set AppleScript's text item delimiters to oldTIDs
    return pathItems
end _splitPath

on _mailboxByName(theAccount, targetName)
    set matchList to every mailbox of theAccount whose name is targetName
    if (count of matchList) is 0 then
        error "La carpeta '" & targetName & "' no existe en la cuenta '" & (name of theAccount) & "'."
    end if
    return item 1 of matchList
end _mailboxByName
on run argv
    set accountName to item 1 of argv
    set sourceName to item 2 of argv
    set destinationName to item 3 of argv
    set olderThanDays to (item 4 of argv) as integer
    set subjectContains to item 5 of argv
    set dryRun to (item 6 of argv) is "true"
    set moveAll to (item 7 of argv) is "true"

    if olderThanDays < -1 then error "olderThanDays no puede ser menor a -1."

    set movedCount to 0
    set useDateFilter to olderThanDays is greater than or equal to 0
    set sourcePath to my _normalizePath(sourceName)
    set destinationPath to my _normalizePath(destinationName)
    if sourcePath is "" then error "Carpeta origen inválida."
    if destinationPath is "" then error "Carpeta destino inválida."
    if useDateFilter then
        set cutoffDate to (current date) - (olderThanDays * days)
    end if

    tell application "Mail"
        set theAccount to first account whose name is accountName
        set sourceMailbox to my _mailboxByName(theAccount, sourcePath)
        set destinationMailbox to my _mailboxByName(theAccount, destinationPath)
        set messageList to messages of sourceMailbox

        repeat with m in messageList
            try
                set matchesDate to true
                if useDateFilter then
                    set matchesDate to (date sent of m) is less than or equal to cutoffDate
                end if

                set matchesSubject to true
                if subjectContains is not "" then
                    set messageSubject to subject of m as text
                    ignoring case
                        set matchesSubject to (messageSubject contains subjectContains)
                    end ignoring
                end if

                if moveAll or (matchesDate and matchesSubject) then
                    if dryRun then
                        set movedCount to movedCount + 1
                    else
                        move m to destinationMailbox
                        set movedCount to movedCount + 1
                    end if
                end if
            end try
        end repeat
    end tell

    return movedCount as string
end run
'''


OUTLOOK_SCRIPT = r'''
on _normalizePath(pathText)
    set oldTIDs to AppleScript's text item delimiters
    set AppleScript's text item delimiters to "/"
    set rawItems to text items of pathText
    set AppleScript's text item delimiters to oldTIDs

    set cleanedItems to {}
    repeat with i in rawItems
        set oneItem to (contents of i) as text
        if oneItem is not "" then set end of cleanedItems to oneItem
    end repeat

    if (count of cleanedItems) is 0 then return ""

    set AppleScript's text item delimiters to "/"
    set cleanedPath to cleanedItems as text
    set AppleScript's text item delimiters to oldTIDs
    return cleanedPath
end _normalizePath

on _splitPath(pathText)
    set cleanedPath to my _normalizePath(pathText)
    if cleanedPath is "" then error "Ruta de carpeta vacía."

    set oldTIDs to AppleScript's text item delimiters
    set AppleScript's text item delimiters to "/"
    set pathItems to text items of cleanedPath
    set AppleScript's text item delimiters to oldTIDs
    return pathItems
end _splitPath

on _folderByName(theAccount, targetName)
    set matchList to every folder of theAccount whose name is targetName
    if (count of matchList) is 0 then
        error "La carpeta '" & targetName & "' no existe en la cuenta '" & (name of theAccount) & "'."
    end if
    return item 1 of matchList
end _folderByName
on run argv
    set accountName to item 1 of argv
    set sourceName to item 2 of argv
    set destinationName to item 3 of argv
    set olderThanDays to (item 4 of argv) as integer
    set subjectContains to item 5 of argv
    set dryRun to (item 6 of argv) is "true"
    set moveAll to (item 7 of argv) is "true"

    if olderThanDays < -1 then error "olderThanDays no puede ser menor a -1."

    set movedCount to 0
    set useDateFilter to olderThanDays is greater than or equal to 0
    set sourcePath to my _normalizePath(sourceName)
    set destinationPath to my _normalizePath(destinationName)
    if sourcePath is "" then error "Carpeta origen inválida."
    if destinationPath is "" then error "Carpeta destino inválida."
    if useDateFilter then
        set cutoffDate to (current date) - (olderThanDays * days)
    end if

    tell application "Microsoft Outlook"
        set theAccount to first account whose name is accountName
        set sourceFolder to my _folderByName(theAccount, sourcePath)
        set destinationFolder to my _folderByName(theAccount, destinationPath)
        set messageList to messages of sourceFolder

        repeat with m in messageList
            try
                set matchesDate to true
                if useDateFilter then
                    try
                        set sentDate to time sent of m
                        set matchesDate to sentDate is less than or equal to cutoffDate
                    on error
                        set recvDate to time received of m
                        set matchesDate to recvDate is less than or equal to cutoffDate
                    end try
                end if

                set matchesSubject to true
                if subjectContains is not "" then
                    set messageSubject to subject of m as text
                    ignoring case
                        set matchesSubject to (messageSubject contains subjectContains)
                    end ignoring
                end if

                if moveAll or (matchesDate and matchesSubject) then
                    if dryRun then
                        set movedCount to movedCount + 1
                    else
                        move m to destinationFolder
                        set movedCount to movedCount + 1
                    end if
                end if
            end try
        end repeat
    end tell

    return movedCount as string
end run
'''


def run_applescript(script: str, argv: list[str]) -> str:
    with tempfile.NamedTemporaryFile("w", suffix=".applescript", delete=False) as f:
        f.write(script)
        script_path = Path(f.name)

    try:
        result = subprocess.run(
            ["osascript", str(script_path), *argv],
            capture_output=True,
            text=True,
        )
    finally:
        script_path.unlink(missing_ok=True)

    if result.returncode != 0:
        err = (result.stderr or result.stdout).strip()
        raise RuntimeError(err or "Error ejecutando AppleScript.")
    return result.stdout.strip()

def normalize_folder_path(path_text: str) -> str:
    parts = [part.strip() for part in (path_text or "").split("/") if part.strip()]
    return "/".join(parts)


def validate_move_request(args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
    args.account = (getattr(args, "account", "") or "").strip()
    args.source = normalize_folder_path(getattr(args, "source", ""))
    args.dest = normalize_folder_path(getattr(args, "dest", ""))
    args.subject_contains = (getattr(args, "subject_contains", "") or "").strip()

    if not args.account:
        parser.error("--account no puede estar vacío.")

    using_date = args.older_than_days is not None
    using_subject = bool(args.subject_contains)

    if args.source == args.dest:
        parser.error("--source y --dest no pueden ser la misma carpeta.")
    if args.all and (using_date or using_subject):
        parser.error("--all no se puede combinar con --older-than-days ni --subject-contains.")
    if not args.all and not using_date and not using_subject:
        parser.error("Debes indicar al menos un criterio: --subject-contains, --older-than-days o --all.")
    if using_date and args.older_than_days < 0:
        parser.error("--older-than-days debe ser >= 0.")
    if not args.source:
        parser.error("--source no puede estar vacío.")
    if not args.dest:
        parser.error("--dest no puede estar vacío.")
    if "/" in args.source or "/" in args.dest:
        parser.error("En Mail/Outlook esta versión solo admite nombres exactos de carpeta, sin jerarquías con '/'. Usa una carpeta real y exacta del cliente de correo.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Mover correos de Enviados a otra carpeta (Mail.app / Outlook en macOS)."
    )
    parser.add_argument(
        "--app",
        choices=["mail", "outlook"],
        required=True,
        help="Cliente de correo.",
    )
    parser.add_argument(
        "--account",
        required=True,
        help="Nombre exacto de la cuenta en la app.",
    )
    parser.add_argument(
        "--source",
        required=True,
        help="Carpeta origen. Soporta subcarpetas con '/', ej: Enviado/Subcarpeta.",
    )
    parser.add_argument(
        "--dest",
        required=True,
        help="Carpeta destino. Soporta subcarpetas con '/', ej: Enviado/Archivo.",
    )
    parser.add_argument(
        "--older-than-days",
        type=int,
        default=None,
        help="Mover mensajes con al menos N días de antigüedad.",
    )
    parser.add_argument(
        "--subject-contains",
        default=None,
        help="Mover mensajes cuyo asunto contenga esta cadena (sin distinguir mayúsculas/minúsculas).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Mover todos los mensajes (sin filtros).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Solo cuenta mensajes, no mueve.",
    )

    args = parser.parse_args()
    validate_move_request(args, parser)
    return args


def main() -> int:
    args = parse_args()

    script = MAIL_SCRIPT if args.app == "mail" else OUTLOOK_SCRIPT
    older_than = str(args.older_than_days) if args.older_than_days is not None else "-1"
    subject_contains = args.subject_contains or ""
    dry = "true" if args.dry_run else "false"
    move_all = "true" if args.all else "false"

    try:
        moved = run_applescript(
            script,
            [
                args.account,
                args.source,
                args.dest,
                older_than,
                subject_contains,
                dry,
                move_all,
            ],
        )
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    label = "Candidatos a mover" if args.dry_run else "Mensajes movidos"
    print(f"{label}: {moved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
