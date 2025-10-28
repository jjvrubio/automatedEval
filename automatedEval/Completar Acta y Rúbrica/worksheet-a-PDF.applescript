-- Ask user to select folder
set folderPath to choose folder with prompt "Select the folder containing Excel files"

-- Convert folderPath to POSIX for logging and file checks
set posixFolderPath to POSIX path of folderPath
set logPath to posixFolderPath & "conversion_log.txt"

-- Get all Excel files in the folder (xlsx, xlsm, xls)
tell application "Finder"
    set excelFiles to files of folder folderPath whose name extension is in {"xlsx", "xlsm", "xls"}
end tell

-- Loop through each Excel file
repeat with f in excelFiles
    set filePathAlias to (f as alias)
    set fileName to name of f
    try
        tell application "Microsoft Excel"
            -- Open the Excel file
            open filePathAlias
            set wb to active workbook

            -- Prefer worksheet named "Rubrica" if present, otherwise use the first worksheet
            try
                set ws to worksheet "Rubrica" of wb
            on error
                set ws to item 1 of worksheets of wb
            end try
            activate object ws

            -- Set page setup to fit to 1 A4 page
            -- Use explicit property assignments to avoid AppleScript record key parsing issues
            tell ws
                set orientation of page setup to portrait
                set zoom of page setup to false
                set fit to pages wide of page setup to 1
                set fit to pages tall of page setup to 1
                -- paper size setting removed because AppleScript constants vary by Excel version
                -- If you need to force A4, we can set a numeric constant or use Excel VBA macro instead
            end tell

            -- Build pdf path and avoid overwriting existing PDFs (append timestamp if needed)
            set pdfName to (name of wb) & ".pdf"
            set pdfPathPosix to posixFolderPath & pdfName
            -- If file exists, append timestamp
            try
                do shell script "test -e " & quoted form of pdfPathPosix
                set pdfPathPosix to posixFolderPath & (do shell script "date +%s") & "_" & pdfName
            on error
                -- file does not exist, keep original name
            end try

            -- Use Excel's ExportAsFixedFormat via AppleScript
            set pdfPathHFS to POSIX file pdfPathPosix as text
            tell wb to save as filename pdfPathHFS file format PDF file format

            -- Close the workbook without saving changes
            close wb saving no
        end tell

        -- Log success
        do shell script "echo \"$(date '+%Y-%m-%d %H:%M:%S') - OK - " & quoted form of fileName & " -> " & quoted form of pdfPathPosix & "\" >> " & quoted form of logPath
    on error errMsg
        -- Log error and show a minimal dialog
        do shell script "echo \"$(date '+%Y-%m-%d %H:%M:%S') - ERROR - " & quoted form of fileName & " - " & quoted form of (errMsg as string) & "\" >> " & quoted form of logPath
        try
            display dialog "Error processing file: " & fileName & return & "Error: " & errMsg buttons {"OK"} default button "OK"
        end try
    end try
end repeat

-- Notify user of completion and log location
display dialog "All Excel files have been processed and saved as PDF. Log: " & logPath buttons {"OK"} default button "OK"