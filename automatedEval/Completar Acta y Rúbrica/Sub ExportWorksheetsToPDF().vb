Sub ExportWorksheetsToPDF()
    Dim folderPath As String
    Dim fileName As String
    Dim wb As Workbook
    Dim ws As Worksheet
    Dim pdfPath As String

    ' Prompt user to select folder: try native FileDialog first (guarded), fall back to AppleScript if unavailable
    Dim fd As Object
    Dim folderHFS As String
    Dim useFD As Boolean
    useFD = False

    On Error Resume Next
    Set fd = Application.FileDialog(msoFileDialogFolderPicker)
    If Not fd Is Nothing Then
        fd.AllowMultiSelect = False
        If Err.Number = 0 Then
            useFD = True
        Else
            useFD = False
        End If
    End If
    On Error GoTo 0

    If useFD Then
        If fd.Show = -1 Then
            folderHFS = fd.SelectedItems(1)
        Else
            Exit Sub
        End If
    Else
        ' Fallback to AppleScript folder chooser (returns POSIX path) and convert to HFS
        Dim folderPOSIX As String
        folderPOSIX = MacScript("return POSIX path of (choose folder with prompt " & Chr(34) & "Select the folder containing Excel files" & Chr(34) & ")")
        If folderPOSIX = "" Then Exit Sub
        folderHFS = MacScript("return (POSIX file " & Chr(34) & folderPOSIX & Chr(34) & ") as text")
    End If

    ' Normalize folderHFS: ensure trailing separator (HFS style uses ':' but some Excel versions return POSIX with '/')
    If Right(folderHFS, 1) <> ":" And Right(folderHFS, 1) <> "/" Then
        If InStr(folderHFS, ":") > 0 Then
            folderHFS = folderHFS & ":"
        Else
            folderHFS = folderHFS & "/"
        End If
    End If

    ' Prepare log file path (HFS expected for VBA Open)
    Dim logFile As String
    logFile = folderHFS & "export_log.txt"

    ' Validate folder exists and that we can create/write the log file. Fail fast with a helpful message if not.
    If Dir(folderHFS, vbDirectory) = "" Then
        MsgBox "Selected folder not found or not accessible: " & folderHFS, vbCritical, "Folder not found"
        Exit Sub
    End If

    ' Ensure the log file exists (create if necessary) and that we have write permission
    On Error Resume Next
    Dim ffCreate As Integer
    ffCreate = FreeFile
    Open logFile For Append As #ffCreate
    If Err.Number <> 0 Then
        MsgBox "Cannot open or create log file: " & logFile & vbCrLf & "Err " & Err.Number & ": " & Err.Description, vbCritical, "Log file error"
        On Error GoTo 0
        Exit Sub
    End If
    Close #ffCreate
    On Error GoTo 0

    Dim fnum As Integer
    ' Loop over common Excel extensions (*.xlsx, *.xlsm, *.xls)
    fileName = Dir(folderHFS & "*.xlsx")
    Do While fileName <> ""
        Call ProcessFile(folderHFS, fileName, logFile)
        fileName = Dir
    Loop
    fileName = Dir(folderHFS & "*.xlsm")
    Do While fileName <> ""
        Call ProcessFile(folderHFS, fileName, logFile)
        fileName = Dir
    Loop
    fileName = Dir(folderHFS & "*.xls")
    Do While fileName <> ""
        ' ignore Excel temporary files that start with ~$
        If Left(fileName, 2) <> "~$" Then
            Call ProcessFile(folderHFS, fileName, logFile)
        End If
        fileName = Dir
    Loop

    MsgBox "PDF export complete! See log: " & logFile

End Sub

' Normaliza cadenas para comparación: minusculas, trim y sustitución de acentos comunes
Private Function NormalizeString(s As String) As String
    Dim t As String
    t = LCase(Trim(s))
    t = Replace(t, "á", "a")
    t = Replace(t, "é", "e")
    t = Replace(t, "í", "i")
    t = Replace(t, "ó", "o")
    t = Replace(t, "ú", "u")
    t = Replace(t, "à", "a")
    t = Replace(t, "è", "e")
    t = Replace(t, "ì", "i")
    t = Replace(t, "ò", "o")
    t = Replace(t, "ù", "u")
    t = Replace(t, "ä", "a")
    t = Replace(t, "ë", "e")
    t = Replace(t, "ï", "i")
    t = Replace(t, "ö", "o")
    t = Replace(t, "ü", "u")
    t = Replace(t, "ñ", "n")
    t = Replace(t, "ç", "c")
    ' Remove double spaces
    Do While InStr(t, "  ") > 0
        t = Replace(t, "  ", " ")
    Loop
    NormalizeString = t
End Function

Private Sub ProcessFile(folderPath As String, fileName As String, logFile As String)
    Dim wb As Workbook
    Dim ws As Worksheet
    Dim pdfPath As String
    Dim ff As Integer
    On Error GoTo ErrHandler

    ' Open workbook using HFS path (folderPath is passed as HFS folder)
    Dim fileHFS As String
    fileHFS = folderPath & fileName
    Set wb = Workbooks.Open(fileHFS)

    ' Prefer sheet named like "Rubrica" (accent-insensitive, case-insensitive), otherwise use first sheet
    Dim targetName As String
    targetName = NormalizeString("Rubrica")
    Set ws = Nothing
    Dim sh As Worksheet
    For Each sh In wb.Sheets
        ' Match if normalized sheet name contains the target (substring match)
        If InStr(NormalizeString(sh.Name), targetName) > 0 Then
            Set ws = sh
            Exit For
        End If
    Next sh
    If ws Is Nothing Then
        Set ws = wb.Sheets(1)
    End If

    If Not ws Is Nothing Then
        ws.Select
        With ws.PageSetup
            .Zoom = False
            .FitToPagesWide = 1
            .FitToPagesTall = 1
            .Orientation = xlPortrait
            .PaperSize = xlPaperA4
        End With

            Dim pdfPathHFS As String
            pdfPathHFS = folderPath & Replace(fileName, ".xlsx", ".pdf")
            pdfPathHFS = Replace(pdfPathHFS, ".xlsm", ".pdf")
            pdfPathHFS = Replace(pdfPathHFS, ".xls", ".pdf")

        ' If file exists, add timestamp to avoid overwrite
        If Dir(pdfPathHFS) <> "" Then
            pdfPathHFS = folderPath & Format(Now, "yyyymmdd_HHNNSS") & "_" & Replace(fileName, ".", "_") & ".pdf"
        End If

        ws.ExportAsFixedFormat Type:=xlTypePDF, fileName:=pdfPathHFS, Quality:=xlQualityStandard
        ' Log success
        ff = FreeFile
        Open logFile For Append As #ff
    Print #ff, Now & " - OK - " & fileName & " -> " & pdfPathHFS
        Close #ff
    End If

    wb.Close SaveChanges:=False
    Exit Sub

ErrHandler:
    ff = FreeFile
    Open logFile For Append As #ff
    Print #ff, Now & " - ERROR - " & fileName & " - " & Err.Description
    Close #ff
    On Error Resume Next
    If Not wb Is Nothing Then wb.Close SaveChanges:=False
End Sub

