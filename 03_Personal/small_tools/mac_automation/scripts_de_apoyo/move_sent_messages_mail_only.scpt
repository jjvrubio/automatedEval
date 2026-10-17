on findMailboxByName(theAccount, targetName)
    tell application "Mail"
        repeat with mb in every mailbox of theAccount
            if name of mb as text is targetName then return mb
        end repeat
    end tell
    error "La carpeta '" & targetName & "' no existe en la cuenta '" & (name of theAccount) & "'."
end findMailboxByName

on promptForText(promptText, defaultText)
    set dialogResult to display dialog promptText default answer defaultText buttons {"Cancelar", "Continuar"} default button "Continuar" cancel button "Cancelar"
    set enteredText to text returned of dialogResult
    if enteredText is "" then error "Este campo no puede estar vacío."
    return enteredText
end promptForText

on writeProgress(logPath, messageText)
    set timestamp to do shell script "date '+%Y-%m-%d %H:%M:%S'"
    set logLine to timestamp & " | " & messageText
    do shell script "printf '%s\\n' " & quoted form of logLine & " >> " & quoted form of logPath
    log logLine
end writeProgress

on matchingMessages(sourceMailbox, subjectText, progressLogPath)
    tell application "Mail"
        set matchedMessages to {}
        set scannedCount to 0
        repeat with msg in every message of sourceMailbox
            set scannedCount to scannedCount + 1
            try
                set messageSubject to subject of msg as text
                ignoring case
                    if messageSubject contains subjectText then set end of matchedMessages to contents of msg
                end ignoring
            on error errMsg number errNum
                my writeProgress(progressLogPath, "No se pudo leer un asunto: " & errMsg & " (" & errNum & ").")
            end try
            if (scannedCount mod 100) is 0 then my writeProgress(progressLogPath, "Analizados " & scannedCount & " mensajes; coincidencias: " & (count of matchedMessages) & ".")
        end repeat
        my writeProgress(progressLogPath, "Análisis completado. Mensajes analizados: " & scannedCount & ".")
        return matchedMessages
    end tell
end matchingMessages

on run argv
    set progressLogPath to "/tmp/move_sent_messages_mail_only.log"
    do shell script "printf '' > " & quoted form of progressLogPath

    if (count of argv) is 0 then
        set accountName to my promptForText("Cuenta de Mail:", "convercus")
        set sourceName to my promptForText("Carpeta de origen:", "Elementos enviados")
        set destinationName to my promptForText("Carpeta de destino:", "Por Apollo")
        set subjectText to my promptForText("El asunto debe contener:", "Convercus e o seu")
        set dryRun to false
    else if (count of argv) is 5 then
        set accountName to item 1 of argv
        set sourceName to item 2 of argv
        set destinationName to item 3 of argv
        set subjectText to item 4 of argv
        set dryRun to (item 5 of argv as text) is "true"
    else
        error "Se requieren 5 argumentos: <cuenta> <origen> <destino> <texto_en_asunto> <dryRun(true|false)>"
    end if

    my writeProgress(progressLogPath, "Inicio. Cuenta=" & accountName & "; origen=" & sourceName & "; destino=" & destinationName & "; dry-run=" & dryRun)

    tell application "Mail"
        set theAccount to first account whose name is accountName
        my writeProgress(progressLogPath, "Cuenta localizada.")
        set sourceMailbox to my findMailboxByName(theAccount, sourceName)
        set destinationMailbox to my findMailboxByName(theAccount, destinationName)
        my writeProgress(progressLogPath, "Carpetas localizadas. Buscando coincidencias...")
        set messageList to my matchingMessages(sourceMailbox, subjectText, progressLogPath)
        set matchingCount to count of messageList
        my writeProgress(progressLogPath, "Coincidencias encontradas: " & matchingCount)

        if dryRun then
            my writeProgress(progressLogPath, "Dry-run finalizado. No se movió ningún mensaje.")
            return matchingCount as string
        end if

        set confirmationText to "Se moverán " & matchingCount & " mensajes desde '" & sourceName & "' a '" & destinationName & "'."
        display dialog confirmationText buttons {"Cancelar", "Mover mensajes"} default button "Mover mensajes" cancel button "Cancelar" with icon caution

        set movedCount to 0
        set failedCount to 0

        repeat with msg in messageList
            try
                move msg to destinationMailbox
                set movedCount to movedCount + 1
                if (movedCount mod 25) is 0 then my writeProgress(progressLogPath, "Movidos " & movedCount & " de " & matchingCount & ".")
            on error errMsg number errNum
                set failedCount to failedCount + 1
                my writeProgress(progressLogPath, "Error al mover un mensaje: " & errMsg & " (" & errNum & ").")
            end try
        end repeat
        my writeProgress(progressLogPath, "Finalizado. Movidos=" & movedCount & "; fallidos=" & failedCount & "; total=" & matchingCount & ".")
    end tell

    display dialog "Mensajes movidos: " & movedCount & ". Errores: " & failedCount & "." buttons {"Aceptar"} default button "Aceptar"
    return "Movidos: " & movedCount & "; errores: " & failedCount & "; registro: " & progressLogPath
end run
