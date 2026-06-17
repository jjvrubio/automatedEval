-- Export Mail messages whose sender contains " (via Streak)" to CSV
use AppleScript version "2.8"
use framework "Foundation"
use scripting additions

property csvDelimiter : ","
property streakMarker : " (via Streak)"

on run
	try
		set exportAlias to my askForDestination()
		set exportResult to my collectRows()
		my writeText(exportResult's csvText, exportAlias)
		my showSuccess(exportAlias, exportResult's matchCount)
	on error errMsg number errNum
		if errNum is -128 then return -- user cancelled
		try
			-- Escape error message to avoid dialog issues
			set cleanErrMsg to my cleanText(errMsg)
			if length of cleanErrMsg > 200 then
				set cleanErrMsg to (text 1 thru 200 of cleanErrMsg) & "..."
			end if
			display dialog "No se pudieron exportar los correos:" & return & return & "Error " & errNum & ": " & cleanErrMsg buttons {"OK"} default button "OK" with icon stop
		on error
			-- If even showing the error fails, show generic message
			display dialog "Error inesperado durante la exportaci—n. Revisa la consola para m‡s detalles." buttons {"OK"} default button "OK" with icon stop
		end try
		error number errNum
	end try
end run

on askForDestination()
	set timestamp to do shell script "date +%Y%m%d-%H%M%S"
	set defaultName to "Streak-mails-" & timestamp & ".csv"
	return choose file name with prompt "Selecciona la ubicaci—n del CSV" default name defaultName
end askForDestination

on collectRows()
	set headerRow to {"Account", "Mailbox", "Sender", "Subject", "Date Sent", "Message ID"}
	set rows to {my buildRow(headerRow)}
	set matchCount to 0
	
	-- Optimized: search only in specific account
	set targetAccountName to "pleasepoint"
	
	tell application "Mail"
		with timeout of 300 seconds
			try
				-- Find the account containing the target email
				set targetAccount to missing value
				repeat with eachAccount in accounts
					try
						set accountName to name of eachAccount
					if accountName contains targetAccountName then
						set targetAccount to eachAccount
						exit repeat
					end if
				end try
				end repeat
				
				if targetAccount is missing value then
					error "No se encontr— una cuenta que contenga: " & targetAccountName
				end if
				
				set accountName to my cleanText(name of targetAccount)
				log "Procesando cuenta: " & accountName
				
				-- Process all mailboxes in this account
				repeat with eachMailbox in mailboxes of targetAccount
					try
						set mailboxName to my cleanText(name of eachMailbox)
						set matchedMessages to (every message of eachMailbox whose sender contains streakMarker)
						repeat with msg in matchedMessages
							try
								set rowData to {accountName, mailboxName, my cleanText(sender of msg), my cleanText(subject of msg), my formatDateTime(date sent of msg), my cleanText(message id of msg)}
								set end of rows to my buildRow(rowData)
								set matchCount to matchCount + 1
							end try
						end repeat
						
						-- Process submailboxes recursively
						set subResult to my processSubMailboxes(eachMailbox, accountName)
						set rows to rows & (item 1 of subResult)
						set matchCount to matchCount + (item 2 of subResult)
					on error errMsg
						log "Error processing mailbox " & mailboxName & ": " & errMsg
					end try
				end repeat
				
			on error errMsg
				error "Error al buscar mensajes: " & errMsg
			end try
		end timeout
	end tell
	
	set AppleScript's text item delimiters to linefeed
	set csvText to rows as text
	set AppleScript's text item delimiters to ""
	return {csvText:csvText, matchCount:matchCount}
end collectRows

on processSubMailboxes(parentMailbox, accountName)
	set subRows to {}
	set subCount to 0
	
	tell application "Mail"
		try
			repeat with eachSubMailbox in mailboxes of parentMailbox
				try
					set mailboxName to my cleanText(name of eachSubMailbox)
					set matchedMessages to (every message of eachSubMailbox whose sender contains streakMarker)
					repeat with msg in matchedMessages
						try
							set rowData to {accountName, mailboxName, my cleanText(sender of msg), my cleanText(subject of msg), my formatDateTime(date sent of msg), my cleanText(message id of msg)}
							set end of subRows to my buildRow(rowData)
							set subCount to subCount + 1
						end try
					end repeat
					
					-- Recursively process nested mailboxes
					set nestedResult to my processSubMailboxes(eachSubMailbox, accountName)
					set subRows to subRows & (item 1 of nestedResult)
					set subCount to subCount + (item 2 of nestedResult)
				end try
			end repeat
		end try
	end tell
	
	return {subRows, subCount}
end processSubMailboxes

on buildRow(valueList)
	set escapedCells to {}
	repeat with eachValue in valueList
		set end of escapedCells to my escapeCell(eachValue)
	end repeat
	set AppleScript's text item delimiters to csvDelimiter
	set rowText to escapedCells as text
	set AppleScript's text item delimiters to ""
	return rowText
end buildRow

on escapeCell(rawValue)
	set cleanedValue to my cleanText(rawValue)
	if cleanedValue is "" then return ""
	set needsQuotes to false
	if cleanedValue contains csvDelimiter then set needsQuotes to true
	if cleanedValue contains return then set needsQuotes to true
	if cleanedValue contains linefeed then set needsQuotes to true
	if cleanedValue contains "\"" then set needsQuotes to true
	if needsQuotes then
		set escapedValue to my replaceText(cleanedValue, "\"", "\"\"")
		return "\"" & escapedValue & "\""
	else
		return cleanedValue
	end if
end escapeCell

on cleanText(rawValue)
	if rawValue is missing value then return ""
	set theText to rawValue as text
	set theText to my replaceText(theText, return, " ")
	set theText to my replaceText(theText, linefeed, " ")
	return theText
end cleanText

on replaceText(theText, searchString, replacementString)
	if searchString is "" then return theText
	set AppleScript's text item delimiters to searchString
	set textItems to text items of theText
	set AppleScript's text item delimiters to replacementString
	set newText to textItems as text
	set AppleScript's text item delimiters to ""
	return newText
end replaceText

on formatDateTime(aDate)
	if aDate is missing value then return ""
	set y to year of aDate as text
	set m to my pad2(month of aDate as integer)
	set d to my pad2(day of aDate)
	set h to my pad2(hours of aDate)
	set min to my pad2(minutes of aDate)
	set s to my pad2(seconds of aDate)
	return y & "-" & m & "-" & d & "T" & h & ":" & min & ":" & s
end formatDateTime

on pad2(n)
	if n < 10 then
		return "0" & (n as text)
	else
		return n as text
	end if
end pad2

on writeText(csvText, targetAlias)
	set filePath to POSIX path of targetAlias
	set nsString to current application's nsString's stringWithString:csvText
	set nsData to nsString's dataUsingEncoding:(current application's NSUTF8StringEncoding)
	nsData's writeToFile:filePath atomically:true
end writeText

on showSuccess(targetAlias, matchCount)
	set targetPath to POSIX path of targetAlias
	display dialog "Se exportaron " & matchCount & " correos con \"" & streakMarker & "\" a:" & return & targetPath buttons {"OK"} default button "OK"
end showSuccess
