-- Diagnóstico de Mail para encontrar correos de Streak
use AppleScript version "2.8"
use scripting additions

on run
	set diagnosticInfo to {}
	
	tell application "Mail"
		-- Listar todas las cuentas
		set end of diagnosticInfo to "=== CUENTAS DISPONIBLES ==="
		repeat with eachAccount in every account
			set accountName to name of eachAccount
			set end of diagnosticInfo to "Cuenta: " & accountName
			
			-- Listar mailboxes de cada cuenta (incluyendo anidados)
			set end of diagnosticInfo to "  Mailboxes:"
			repeat with eachMailbox in mailboxes of eachAccount
				set mailboxName to name of eachMailbox
				set msgCount to count of messages of eachMailbox
				set end of diagnosticInfo to "    - " & mailboxName & " (" & msgCount & " mensajes)"
				
				-- Mostrar submailboxes
				try
					repeat with subMailbox in mailboxes of eachMailbox
						set subMailboxName to name of subMailbox
						set subMsgCount to count of messages of subMailbox
						set end of diagnosticInfo to "      ?? " & subMailboxName & " (" & subMsgCount & " mensajes)"
					end repeat
				end try
			end repeat
			
			set end of diagnosticInfo to ""
		end repeat
		
		-- Buscar específicamente en cuenta que contenga "pleasepoint"
		set end of diagnosticInfo to "=== BUSCANDO EN CUENTA CON 'pleasepoint' ==="
		repeat with eachAccount in every account
			set accountName to name of eachAccount
			if accountName contains "pleasepoint" then
				set end of diagnosticInfo to "Cuenta encontrada: " & accountName
				
				-- Buscar en TODOS los mailboxes (primer nivel y anidados)
				set allMailboxes to {}
				repeat with eachMailbox in mailboxes of eachAccount
					set end of allMailboxes to eachMailbox
					try
						repeat with subMailbox in mailboxes of eachMailbox
							set end of allMailboxes to subMailbox
						end repeat
					end try
				end repeat
				
				set end of diagnosticInfo to "Total de mailboxes (incluyendo anidados): " & (count of allMailboxes)
				set end of diagnosticInfo to ""
				
				-- Buscar en cada mailbox
				repeat with targetMailbox in allMailboxes
					set mailboxName to name of targetMailbox
					set msgCount to count of messages of targetMailbox
					
					if msgCount > 0 then
						set end of diagnosticInfo to "--- Mailbox: " & mailboxName & " (" & msgCount & " mensajes) ---"
						
						-- Mostrar primeros 5 senders
						set end of diagnosticInfo to "Primeros 5 senders:"
						set sampleCount to 0
						repeat with msg in messages of targetMailbox
							if sampleCount < 5 then
								set senderText to sender of msg
								set end of diagnosticInfo to "  " & senderText
								set sampleCount to sampleCount + 1
							else
								exit repeat
							end if
						end repeat
						
						-- Probar búsqueda de Streak
						try
							set streakMatches to (every message of targetMailbox whose sender contains "Streak")
							if (count of streakMatches) > 0 then
								set end of diagnosticInfo to "  ? Encontrados " & (count of streakMatches) & " mensajes con 'Streak'"
								-- Mostrar un ejemplo
								set exampleSender to sender of item 1 of streakMatches
								set end of diagnosticInfo to "  Ejemplo: " & exampleSender
							end if
						end try
						
						set end of diagnosticInfo to ""
					end if
				end repeat
				
				exit repeat
			end if
		end repeat
	end tell
	
	-- Mostrar resultados
	set AppleScript's text item delimiters to return
	set diagnosticText to diagnosticInfo as text
	set AppleScript's text item delimiters to ""
	
	display dialog diagnosticText buttons {"OK"} default button "OK" with title "Diagnóstico Mail"
	
	-- También guardar en archivo
	set desktopPath to (path to desktop as text) & "diagnostico_mail.txt"
	set fileRef to open for access file desktopPath with write permission
	try
		set eof of fileRef to 0
		write diagnosticText to fileRef
		close access fileRef
	on error
		try
			close access fileRef
		end try
	end try
	
	display dialog "Diagnóstico guardado en el Escritorio: diagnostico_mail.txt" buttons {"OK"} default button "OK"
end run
