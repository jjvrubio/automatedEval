Option Explicit

Private Function NormalizarTexto(ByVal entrada As String) As String
    Dim tmp As String

    tmp = Trim$(entrada)
    tmp = Replace(tmp, "á", "a")
    tmp = Replace(tmp, "é", "e")
    tmp = Replace(tmp, "í", "i")
    tmp = Replace(tmp, "ó", "o")
    tmp = Replace(tmp, "ú", "u")
    tmp = Replace(tmp, "ü", "u")
    tmp = Replace(tmp, "ñ", "n")

    tmp = UCase$(tmp)
    tmp = Replace(tmp, "Á", "A")
    tmp = Replace(tmp, "É", "E")
    tmp = Replace(tmp, "Í", "I")
    tmp = Replace(tmp, "Ó", "O")
    tmp = Replace(tmp, "Ú", "U")
    tmp = Replace(tmp, "Ü", "U")
    tmp = Replace(tmp, "Ñ", "N")

    NormalizarTexto = tmp
End Function

Private Function BuscarHojaPorNombre(ByVal wb As Workbook, ByVal nombreObjetivo As String) As Worksheet
    Dim hoja As Worksheet
    Dim nombreNormalizado As String

    nombreNormalizado = NormalizarTexto(nombreObjetivo)

    For Each hoja In wb.Worksheets
        If NormalizarTexto(hoja.Name) = nombreNormalizado Then
            Set BuscarHojaPorNombre = hoja
            Exit Function
        End If
    Next hoja

    Set BuscarHojaPorNombre = Nothing
End Function

Private Function ObtenerBaseSinExtension(ByVal nombreArchivo As String) As String
    Dim pos As Long

    pos = InStrRev(nombreArchivo, ".")
    If pos > 0 Then
        ObtenerBaseSinExtension = Left$(nombreArchivo, pos - 1)
    Else
        ObtenerBaseSinExtension = nombreArchivo
    End If
End Function

Sub ExportWorksheetsToPDF()
    Dim folderPath As String
    Dim fileName As String
    Dim wb As Workbook
    Dim ws As Worksheet
    Dim pdfPath As String

    ' Solicita al usuario seleccionar una carpeta (compatible con macOS)
    On Error Resume Next
    folderPath = MacScript("return POSIX path of (choose folder with prompt ""Selecciona la carpeta que contiene los archivos Excel"")")
    On Error GoTo 0

    If folderPath = "" Then
        MsgBox "No se seleccionó ninguna carpeta.", vbExclamation
        Exit Sub
    End If

    ' Asegura que la ruta termine con "/"
    If Right(folderPath, 1) <> "/" Then folderPath = folderPath & "/"

    ' Busca archivos .xlsx/.xlsm en la carpeta sin importar mayúsculas
    fileName = Dir(folderPath & "*.xls*")

    If fileName = "" Then
        MsgBox "No se encontraron archivos .xlsx en la carpeta seleccionada.", vbInformation
        Exit Sub
    End If

    ' Procesa cada archivo
    Do While fileName <> ""
        Set wb = Workbooks.Open(folderPath & fileName)
        Set ws = Nothing ' Limpia la variable antes de buscar la hoja

        Set ws = BuscarHojaPorNombre(wb, "Rubrica") ' Localiza variaciones con acentos y mayúsculas

        If Not ws Is Nothing Then
            ' Configura la hoja para impresión
            With ws.PageSetup
                .Zoom = False
                .FitToPagesWide = 1
                .FitToPagesTall = 1
                .Orientation = xlPortrait
                .PaperSize = xlPaperA4
            End With

            ' Exporta como PDF
            pdfPath = folderPath & ObtenerBaseSinExtension(fileName) & ".pdf"
            ws.ExportAsFixedFormat Type:=xlTypePDF, fileName:=pdfPath, Quality:=xlQualityStandard
        Else
            MsgBox "La hoja 'Rubrica' no se encontró en: " & fileName, vbExclamation
        End If

        wb.Close SaveChanges:=False
        fileName = Dir ' Siguiente archivo
    Loop

    MsgBox "¡Exportación a PDF completada!", vbInformation
End Sub
