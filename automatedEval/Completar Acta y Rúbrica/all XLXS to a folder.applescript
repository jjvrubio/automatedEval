-- Ask user to choose the root folder
-- Ask user to choose the root folder
set rootFolder to choose folder with prompt "Select the root folder to search for Excel files"

-- Convert to POSIX path and build destination folder (keep it inside the selected root)
set rootPath to POSIX path of rootFolder
set AppleScript's text item delimiters to "/"
set folderName to last text item of text items of rootPath
set destFolder to rootPath & folderName & " XLSXs/"

-- Create destination folder
do shell script "mkdir -p " & quoted form of destFolder

-- Find and copy all Excel files: use a simpler -iname pattern to avoid shell escaping issues in AppleScript
set findCmd to "find " & quoted form of rootPath & " -type f -iname '*.xls*' -not -name '~$*' -print0"
set copyCmd to findCmd & " | while IFS= read -r -d '' file; do base=$(basename \"$file\"); dest=\"" & destFolder & "\"$base; if [ -e \"$dest\" ]; then dest=\"" & destFolder & "\"$(date +%s)_$base; fi; cp \"$file\" \"$dest\"; done"

do shell script copyCmd

display dialog "All Excel files have been copied to: " & destFolder buttons {"OK"} default button "OK"
