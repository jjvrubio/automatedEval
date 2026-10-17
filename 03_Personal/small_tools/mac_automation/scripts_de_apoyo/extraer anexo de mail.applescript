tell application "Mail"
	-- Get the currently selected messages
	set selectedMessages to selection
	
	-- Create a variable to store the save location
	set saveFolder to (choose folder with prompt "Select folder to save attachments:")
	
	-- Counter for processed attachments
	set attachmentCount to 0
	
	-- Process each selected message
	repeat with theMessage in selectedMessages
		-- Get all attachments from the message
		set theAttachments to mail attachments of theMessage
		
		-- Process each attachment in the message
		repeat with theAttachment in theAttachments
			-- Get the attachment name
			set attachmentName to name of theAttachment
			
			-- Save the attachment to the chosen folder
			try
				save theAttachment in (saveFolder as string) & attachmentName
				set attachmentCount to attachmentCount + 1
			on error errMsg
				display dialog "Error saving " & attachmentName & ": " & errMsg
			end try
		end repeat
	end repeat
	
	-- Show completion message
	display dialog "Extracted " & attachmentCount & " attachments" buttons {"OK"} default button "OK"
end tell