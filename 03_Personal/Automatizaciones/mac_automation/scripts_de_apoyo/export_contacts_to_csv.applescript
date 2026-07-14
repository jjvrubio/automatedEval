-- Export Apple Contacts to CSV with common fields and labeled values
property csvDelimiter : ","
property multiValueSeparator : " | "
property labeledValueSeparator : ": "

on run
	try
		set exportAlias to my askForDestination()
		set exportResult to my assembleCSV()
		my writeText(exportResult's csvText, exportAlias)
		my showSuccess(exportAlias, exportResult's contactCount)
	on error errMsg number errNum
		if errNum is -128 then return -- user cancelled
		display dialog "No se pudo exportar los contactos: " & errMsg buttons {"OK"} default button "OK"
	end try
end run

on askForDestination()
	set timestamp to do shell script "date +%Y%m%d-%H%M%S"
	set defaultName to "Contactos-" & timestamp & ".csv"
	return choose file name with prompt "Selecciona la ubicacion del CSV de contactos" default name defaultName
end askForDestination

on assembleCSV()
	set headerRow to {"Full Name", "First Name", "Last Name", "Company", "Job Title", "Emails", "Phones", "Addresses", "Websites", "Notes", "Birthday", "Created", "Modified", "Contact ID"}
	set rows to {my buildRow(headerRow)}
	set exportedCount to 0
	tell application "Contacts"
		set contactList to every person
		repeat with personRecord in contactList
			-- Extract emails
			set emailsList to {}
			repeat with eachEmail in emails of personRecord
				try
					set emailLabel to label of eachEmail
					set emailValue to value of eachEmail
					set end of emailsList to {emailLabel, emailValue}
				end try
			end repeat
			
			-- Extract phones
			set phonesList to {}
			repeat with eachPhone in phones of personRecord
				try
					set phoneLabel to label of eachPhone
					set phoneValue to value of eachPhone
					set end of phonesList to {phoneLabel, phoneValue}
				end try
			end repeat
			
			-- Extract addresses
			set addressesList to {}
			repeat with eachAddr in addresses of personRecord
				try
					set addrLabel to label of eachAddr
					set addrStreet to street of eachAddr
					set addrCity to city of eachAddr
					set addrState to state of eachAddr
					set addrZip to zip of eachAddr
					set addrCountry to country of eachAddr
					set end of addressesList to {addrLabel, addrStreet, addrCity, addrState, addrZip, addrCountry}
				end try
			end repeat
			
			-- Extract URLs
			set urlsList to {}
			repeat with eachURL in urls of personRecord
				try
					set urlLabel to label of eachURL
					set urlValue to value of eachURL
					set end of urlsList to {urlLabel, urlValue}
				end try
			end repeat
			
			set rowData to {my cleanText(name of personRecord), my cleanText(first name of personRecord), my cleanText(last name of personRecord), my cleanText(company of personRecord), my cleanText(job title of personRecord), my formatExtractedLabeledValues(emailsList), my formatExtractedLabeledValues(phonesList), my formatExtractedAddresses(addressesList), my formatExtractedLabeledValues(urlsList), my cleanText(note of personRecord), my formatDateOnly(birth date of personRecord), my formatDateTime(creation date of personRecord), my formatDateTime(modification date of personRecord), my cleanText(id of personRecord)}
			set end of rows to my buildRow(rowData)
			set exportedCount to exportedCount + 1
		end repeat
	end tell
	set AppleScript's text item delimiters to linefeed
	set csvText to rows as text
	set AppleScript's text item delimiters to ""
	return {csvText:csvText, contactCount:exportedCount}
end assembleCSV

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

on formatExtractedLabeledValues(extractedList)
	if extractedList is missing value or extractedList = {} then return ""
	set formattedItems to {}
	repeat with eachItem in extractedList
		try
			set labelText to my cleanText(item 1 of eachItem)
			set valueText to my cleanText(item 2 of eachItem)
			if valueText is not "" then
				if labelText is "" then
					set end of formattedItems to valueText
				else
					set end of formattedItems to labelText & labeledValueSeparator & valueText
				end if
			end if
		end try
	end repeat
	return my joinList(formattedItems, multiValueSeparator)
end formatExtractedLabeledValues

on formatExtractedAddresses(extractedList)
	if extractedList is missing value or extractedList = {} then return ""
	set formatted to {}
	repeat with eachAddr in extractedList
		try
			set parts to {}
			set streetText to my cleanText(item 2 of eachAddr)
			if streetText is not "" then set end of parts to streetText
			set cityText to my cleanText(item 3 of eachAddr)
			if cityText is not "" then set end of parts to cityText
			set stateText to my cleanText(item 4 of eachAddr)
			if stateText is not "" then set end of parts to stateText
			set zipText to my cleanText(item 5 of eachAddr)
			if zipText is not "" then set end of parts to zipText
			set countryText to my cleanText(item 6 of eachAddr)
			if countryText is not "" then set end of parts to countryText
			set addressText to my joinList(parts, ", ")
			set labelText to my cleanText(item 1 of eachAddr)
			if labelText is not "" and addressText is not "" then
				set end of formatted to labelText & labeledValueSeparator & addressText
			else if addressText is not "" then
				set end of formatted to addressText
			end if
		end try
	end repeat
	return my joinList(formatted, multiValueSeparator)
end formatExtractedAddresses

on joinList(valueList, delimiterText)
	if valueList is missing value or valueList = {} then return ""
	set AppleScript's text item delimiters to delimiterText
	set joinedText to valueList as text
	set AppleScript's text item delimiters to ""
	return joinedText
end joinList

on formatDateOnly(aDate)
	if aDate is missing value then return ""
	set y to year of aDate as text
	set m to my pad2(month of aDate as integer)
	set d to my pad2(day of aDate)
	return y & "-" & m & "-" & d
end formatDateOnly

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
	set fileRef to open for access targetAlias with write permission
	try
		set eof of fileRef to 0
		write csvText to fileRef as Çclass utf8È
	on error errMsg number errNum
		try
			close access fileRef
		end try
		error errMsg number errNum
	end try
	close access fileRef
end writeText

on showSuccess(targetAlias, countExported)
	set targetPath to POSIX path of targetAlias
	display dialog "Se exportaron " & countExported & " contactos a:" & return & targetPath buttons {"OK"} default button "OK"
end showSuccess
