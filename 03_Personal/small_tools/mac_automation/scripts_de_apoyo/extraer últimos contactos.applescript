(*
  Exporta contactos creados desde una fecha (inclusive) a CSV.
  Fecha de entrada: YYYY-MM-DD (ej: 2026-05-01)
*)

set respuesta to display dialog "Fecha desde la que quieres exportar (YYYY-MM-DD):" default answer "2026-05-01" buttons {"Cancelar", "Continuar"} default button "Continuar"
set fechaTexto to text returned of respuesta
set fechaCorte to my fechaISOaDate(fechaTexto)

set filas to {}
tell application "Contacts"
    set todasPersonas to every person
    
    repeat with p in todasPersonas
        try
            set fCreacion to creation date of p
            if fCreacion ≥ fechaCorte then
                set nombreCompleto to ""
                try
                    set nombreCompleto to name of p
                end try
                
                set emailTxt to ""
                try
                    set emailsPersona to value of emails of p
                    if (count of emailsPersona) > 0 then set emailTxt to item 1 of emailsPersona
                end try
                
                set telTxt to ""
                try
                    set telsPersona to value of phones of p
                    if (count of telsPersona) > 0 then set telTxt to item 1 of telsPersona
                end try
                
                set fechaCreacionISO to my dateToISO(fCreacion)
                set end of filas to {nombreCompleto, emailTxt, telTxt, fechaCreacionISO}
            end if
        end try
    end repeat
end tell

set csvText to "Nombre,Email,Telefono,FechaCreacion" & linefeed
repeat with f in filas
    set csvText to csvText & my csvField(item 1 of f) & "," & my csvField(item 2 of f) & "," & my csvField(item 3 of f) & "," & my csvField(item 4 of f) & linefeed
end repeat

set nombreFichero to "contactos_nuevos_desde_" & fechaTexto & ".csv"
set destinoArchivo to choose file name with prompt "Guardar CSV como..." default name nombreFichero default location (path to desktop folder)

set fileRef to open for access destinoArchivo with write permission
try
    set eof fileRef to 0
    write csvText to fileRef as «class utf8»
    close access fileRef
on error errMsg number errNum
    try
        close access fileRef
    end try
    error errMsg number errNum
end try

display dialog "Exportación completada." & return & "Contactos exportados: " & (count of filas) buttons {"OK"} default button "OK"


on fechaISOaDate(isoText)
    if (length of isoText) is not 10 then error "Formato inválido. Usa YYYY-MM-DD."
    if (character 5 of isoText) is not "-" or (character 8 of isoText) is not "-" then error "Formato inválido. Usa YYYY-MM-DD."
    
    try
        set y to (text 1 thru 4 of isoText) as integer
        set m to (text 6 thru 7 of isoText) as integer
        set d to (text 9 thru 10 of isoText) as integer
    on error
        error "La fecha contiene valores no válidos."
    end try
    
    set dt to current date
    set year of dt to y
    set month of dt to m
    set day of dt to d
    set time of dt to 0
    return dt
end fechaISOaDate

on dateToISO(d)
    set y to (year of d) as integer
    set m to my pad2((month of d) as integer)
    set dd to my pad2(day of d)
    return (y as text) & "-" & m & "-" & dd
end dateToISO

on pad2(n)
    if n < 10 then
        return "0" & (n as text)
    else
        return n as text
    end if
end pad2

on csvField(v)
    set s to v as text
    set q to quote
    set s to my replaceText(q, q & q, s)
    return q & s & q
end csvField

on replaceText(findText, replaceText, sourceText)
    set oldTIDs to AppleScript's text item delimiters
    set AppleScript's text item delimiters to findText
    set parts to text items of sourceText
    set AppleScript's text item delimiters to replaceText
    set outText to parts as text
    set AppleScript's text item delimiters to oldTIDs
    return outText
end replaceText