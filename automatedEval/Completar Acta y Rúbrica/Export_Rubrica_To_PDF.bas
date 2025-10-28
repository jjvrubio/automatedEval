
Option Explicit

' Set to False to disable all logging (no export_log.txt will be created or written)
Const ENABLE_LOG As Boolean = False

' Export_Rubrica_To_PDF.bas
' Macro para Excel (Office 365 Mac) — exporta la hoja llamada "rúbrica" (varias variantes) a PDF
' - Selecciona carpeta con FileDialog (carpeta que contiene los libros .xls/.xlsx/.xlsm)
' - Para cada libro en la carpeta, abre el libro, busca la hoja cuyo nombre contiene "rubrica"
'   (insensible a mayúsculas y a acentos: rúbrica, RUBRICA, Rúbrica, etc.)
' - Si encuentra la hoja, la exporta como PDF en la misma carpeta con nombre <workbook>_RUBRICA.pdf
' - Evita sobrescribir archivos existentes añadiendo timestamp si hace falta
' - Intenta escribir un log `export_log.txt` en la carpeta; si no puede, muestra advertencia pero continúa

Sub ExportRubricaToPDF()
    Dim fd As Object
    Dim folderPath As String
    Dim fileName As String
    Dim logFile As String
    Dim ff As Integer
    Dim anyProcessed As Boolean
    ' Try native FileDialog; on Mac it may be unavailable, so guard and fallback to AppleScript or InputBox
    On Error Resume Next
    Set fd = Application.FileDialog(msoFileDialogFolderPicker)
    If Err.Number = 0 And Not fd Is Nothing Then
        On Error GoTo 0
        fd.Title = "Selecciona la carpeta que contiene los libros de Excel"
        fd.AllowMultiSelect = False
        If fd.Show <> -1 Then
            MsgBox "Operación cancelada.", vbInformation
            Exit Sub
        End If
        folderPath = fd.SelectedItems(1)
    Else
        Err.Clear
        On Error GoTo 0
        ' Try AppleScript folder chooser (returns POSIX path). If MacScript missing, fall back to InputBox
        On Error Resume Next
        Dim folderPOSIX As String
        folderPOSIX = MacScript("return POSIX path of (choose folder with prompt " & Chr(34) & "Selecciona la carpeta que contiene los libros de Excel" & Chr(34) & ")")
        If Err.Number = 0 And folderPOSIX <> "" Then
            folderPath = folderPOSIX
        Else
            Err.Clear
            folderPath = InputBox("Introduce la ruta completa de la carpeta (por ejemplo /Users/juanjo/Desktop/TFM):", "Ruta de la carpeta")
            If folderPath = "" Then
                MsgBox "Operación cancelada.", vbInformation
                Exit Sub
            End If
        End If
        On Error GoTo 0
    End If

    ' Ensure trailing separator (accept POSIX or HFS) — keep as provided because modern Excel for Mac acepta POSIX
    If Right(folderPath, 1) <> "/" And Right(folderPath, 1) <> ":" Then
        folderPath = folderPath & "/"
    End If

    logFile = folderPath & "export_log.txt"
    If ENABLE_LOG Then
        On Error Resume Next
        ff = FreeFile
        Open logFile For Append As #ff
        If Err.Number <> 0 Then
            Dim initErr As Long
            Dim initErrDesc As String
            initErr = Err.Number
            initErrDesc = Err.Description
            Err.Clear
            ' Preguntar si usar el Escritorio como fallback para el log
            Dim useDesktop As VbMsgBoxResult
            useDesktop = MsgBox("Advertencia: no he podido crear/abrir el log en:" & vbCrLf & folderPath & "export_log.txt" & vbCrLf & _
                                 "Err: " & initErr & " - " & initErrDesc & vbCrLf & "¿Crear el log en el Escritorio en su lugar?", vbYesNo + vbExclamation, "Log no disponible")
            If useDesktop = vbYes Then
                Dim desktopPOSIX As String
                On Error Resume Next
                desktopPOSIX = MacScript("return POSIX path of (path to desktop folder)")
                On Error GoTo 0
                If desktopPOSIX = "" Then
                    desktopPOSIX = Environ("HOME") & "/Desktop/"
                Else
                    If Right(desktopPOSIX, 1) <> "/" Then desktopPOSIX = desktopPOSIX & "/"
                End If
                logFile = desktopPOSIX & "export_log.txt"
                On Error Resume Next
                ff = FreeFile
                Open logFile For Append As #ff
                If Err.Number <> 0 Then
                    MsgBox "Aún no puedo crear el log en el Escritorio. Se continuará sin fichero de log. Err: " & Err.Number & " - " & Err.Description, vbExclamation, "Log no disponible"
                    Err.Clear
                Else
                    Print #ff, "Export started: " & Now & " (log en Escritorio)"
                    Close #ff
                End If
                On Error GoTo 0
            Else
                MsgBox "Se continuará sin fichero de log.", vbExclamation, "Log no disponible"
            End If
        Else
            Print #ff, "Export started: " & Now
            Close #ff
        End If
        On Error GoTo 0
    End If

    anyProcessed = False
    ' Build a stable list of files first (Dir's state can be clobbered by Workbooks.Open).
    Dim files As Collection
    Set files = New Collection

    On Error Resume Next
    Dim tmpName As String
    ' gather .xlsx
    tmpName = Dir(folderPath & "*.xlsx")
    Do While tmpName <> ""
        If Left(tmpName, 2) <> "~$" Then files.Add tmpName
        tmpName = Dir
    Loop
    ' gather .xlsm
    tmpName = Dir(folderPath & "*.xlsm")
    Do While tmpName <> ""
        If Left(tmpName, 2) <> "~$" Then files.Add tmpName
        tmpName = Dir
    Loop
    ' gather .xls
    tmpName = Dir(folderPath & "*.xls")
    Do While tmpName <> ""
        If Left(tmpName, 2) <> "~$" Then files.Add tmpName
        tmpName = Dir
    Loop
    On Error GoTo 0

    ' If no files found via Dir (may happen on OneDrive placeholders), fall back to shell listing via MacScript
    If files.Count = 0 Then
        Dim listOutput As String
        Dim items As Variant
        Dim i As Long
        On Error Resume Next
        listOutput = MacScript("do shell script " & Chr(34) & "/bin/ls -1 " & folderPath & " 2>/dev/null" & Chr(34))
        If Err.Number = 0 And listOutput <> "" Then
            items = Split(listOutput, vbLf)
            For i = LBound(items) To UBound(items)
                Dim fname As String
                fname = items(i)
                If fname <> "" Then
                    If LCase(Right(fname, 5)) = ".xlsx" Or LCase(Right(fname, 5)) = ".xlsm" Or LCase(Right(fname, 4)) = ".xls" Then
                        If Left(fname, 2) <> "~$" Then files.Add fname
                    End If
                End If
            Next i
        Else
            MsgBox "No he podido enumerar los archivos en la carpeta seleccionada. Si la carpeta está en OneDrive/iCloud, asegúrate de que está sincronizada localmente o copia los archivos a una carpeta local y vuelve a intentarlo.", vbExclamation, "Error de acceso a carpeta"
        End If
        On Error GoTo 0
    End If

    ' Process collected files (stable iteration)
    Dim idx As Long
    For idx = 1 To files.Count
        Call ProcessWorkbookForRubrica(folderPath, files(idx), logFile)
        anyProcessed = True
    Next idx

    If anyProcessed Then
        If ENABLE_LOG Then
            MsgBox "Procesamiento completo. Revisa " & logFile & " para más detalles (si disponible).", vbInformation, "Export terminado"
        Else
            MsgBox "Procesamiento completo.", vbInformation, "Export terminado"
        End If
    Else
        MsgBox "No se encontraron libros Excel en la carpeta seleccionada.", vbInformation, "Nada que hacer"
    End If
End Sub

Private Sub ProcessWorkbookForRubrica(folderPath As String, fileName As String, logFile As String)
    Dim wb As Workbook
    Dim sh As Worksheet
    Dim targetSh As Worksheet
    Dim fpath As String
    Dim pdfName As String
    Dim pdfPath As String
    Dim ff As Integer

    On Error GoTo ErrHandler

    fpath = folderPath & fileName
    Set wb = Workbooks.Open(fpath)

    Set targetSh = Nothing
    For Each sh In wb.Worksheets
        If InStr(NormalizeString(sh.Name), "rubrica") > 0 Then
            Set targetSh = sh
            Exit For
        End If
    Next sh

    If Not targetSh Is Nothing Then
        ' Build PDF path: <workbookname>_RUBRICA.pdf
        pdfName = Left(fileName, InStrRev(fileName, ".") - 1) & "_RUBRICA.pdf"
        pdfPath = folderPath & pdfName
        ' If exists, add timestamp
        If Dir(pdfPath) <> "" Then
            pdfPath = folderPath & Left(fileName, InStrRev(fileName, ".") - 1) & "_RUBRICA_" & Format(Now, "yyyymmdd_HHNNSS") & ".pdf"
        End If
        ' Export only the worksheet
        targetSh.ExportAsFixedFormat Type:=xlTypePDF, fileName:=pdfPath, Quality:=xlQualityStandard

        ' Log success if possible
        If ENABLE_LOG Then
            On Error Resume Next
            ff = FreeFile
            Open logFile For Append As #ff
            If Err.Number = 0 Then
                Print #ff, Now & " - OK - " & fileName & " -> " & pdfPath
                Close #ff
            Else
                Err.Clear
            End If
            On Error GoTo ErrHandler
        End If
    Else
        ' Log not found
        If ENABLE_LOG Then
            On Error Resume Next
            ff = FreeFile
            Open logFile For Append As #ff
            If Err.Number = 0 Then
                Print #ff, Now & " - SKIP - " & fileName & " - sheet 'rubrica' not found"
                Close #ff
            Else
                Err.Clear
            End If
            On Error GoTo ErrHandler
        End If
    End If

    wb.Close SaveChanges:=False
    Exit Sub

ErrHandler:
    On Error Resume Next
    If ENABLE_LOG Then
        ff = FreeFile
        Open logFile For Append As #ff
        Print #ff, Now & " - ERROR - " & fileName & " - " & Err.Number & " : " & Err.Description
        Close #ff
    End If
    On Error Resume Next
    If Not wb Is Nothing Then wb.Close SaveChanges:=False
    Err.Clear
End Sub

Private Function NormalizeString(s As String) As String
    Dim t As String
    t = LCase(Trim(s))
    ' Replace common accented characters with plain equivalents
    t = Replace(t, "á", "a")
    t = Replace(t, "à", "a")
    t = Replace(t, "ä", "a")
    t = Replace(t, "â", "a")
    t = Replace(t, "é", "e")
    t = Replace(t, "è", "e")
    t = Replace(t, "ë", "e")
    t = Replace(t, "ê", "e")
    t = Replace(t, "í", "i")
    t = Replace(t, "ì", "i")
    t = Replace(t, "ï", "i")
    t = Replace(t, "î", "i")
    t = Replace(t, "ó", "o")
    t = Replace(t, "ò", "o")
    t = Replace(t, "ö", "o")
    t = Replace(t, "ô", "o")
    t = Replace(t, "ú", "u")
    t = Replace(t, "ù", "u")
    t = Replace(t, "ü", "u")
    t = Replace(t, "û", "u")
    t = Replace(t, "ñ", "n")
    t = Replace(t, "ç", "c")
    NormalizeString = t
End Function


' GetLastFolderName: devuelve el nombre de la última carpeta en una ruta POSIX/HFS
Private Function GetLastFolderName(folderPath As String) As String
    Dim p As String
    p = folderPath
    If p = "" Then
        GetLastFolderName = ""
        Exit Function
    End If
    ' Remove trailing separator(s)
    Do While Right(p, 1) = "/" Or Right(p, 1) = ":"
        p = Left(p, Len(p) - 1)
    Loop
    If InStrRev(p, "/") > 0 Then
        GetLastFolderName = Mid(p, InStrRev(p, "/") + 1)
    ElseIf InStrRev(p, ":") > 0 Then
        GetLastFolderName = Mid(p, InStrRev(p, ":") + 1)
    Else
        GetLastFolderName = p
    End If
End Function

' AppendLogLine: intenta escribir una línea en el fichero de log.
'  - primero intenta el método VBA normal (Open For Append)
'  - si falla, intenta forzar la creación con `touch` vía MacScript y reintentar
'  - devuelve True si la línea se escribió correctamente, False en caso contrario
Private Function AppendLogLine(logFile As String, textLine As String) As Boolean
    Dim ff As Integer
    On Error Resume Next
    ff = FreeFile
    Open logFile For Append As #ff
    If Err.Number = 0 Then
        Print #ff, textLine
        Close #ff
        AppendLogLine = True
        Exit Function
    End If
    Err.Clear

    ' Try to create/touch the file via shell (may trigger OneDrive to download)
    On Error Resume Next
    ' Build AppleScript that runs: do shell script "/usr/bin/touch " & quoted form of "<path>"
    MacScript "do shell script " & Chr(34) & "/usr/bin/touch " & Chr(34) & " & quoted form of " & Chr(34) & logFile & Chr(34)
    Err.Clear

    ' Small wait for filesystem to settle
    On Error Resume Next
    Application.Wait (Now + TimeValue("0:00:01"))
    Err.Clear

    ' Try again
    ff = FreeFile
    On Error Resume Next
    Open logFile For Append As #ff
    If Err.Number = 0 Then
        Print #ff, textLine
        Close #ff
        AppendLogLine = True
        Exit Function
    End If
    Err.Clear

    ' Last resort: fail and return False
    AppendLogLine = False
End Function
