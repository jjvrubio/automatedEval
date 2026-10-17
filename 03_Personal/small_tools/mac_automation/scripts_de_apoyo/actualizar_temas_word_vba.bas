Attribute VB_Name = "ActualizarTemasBatch"
Option Explicit

Private Const RAIZ_CLOUDSTORAGE As String = "/Users/juanjo/Library/CloudStorage"

' Macro reiniciada desde cero para macOS.
' Empareja SOLO nombres exactos:
'   TEMA 1.docx  <-> tema_1_rev.docx
'   TEMA 2.docx  <-> tema_2_rev.docx
'   ...
'
' Seguridad:
' - Nunca sobrescribe originales.
' - Guarda salidas con prefijo de ejecucion en la misma carpeta TEMAS.

' Prueba minima y hardcoded: solo TEMA 1 + tema_1_rev.
' Uso recomendado:
' 1) Abre en Word el archivo TEMA 1.docx desde la carpeta TEMAS.
' 2) Ejecuta ProbarPrimerParHardcoded.
Public Sub ProbarPrimerParHardcoded()
    Dim etapa As String
    Dim carpetaTemas As String
    Dim origPath As String
    Dim revPath As String
    Dim outPath As String
    Dim docOrig As Document
    Dim docRev As Document
    Dim docCmp As Document

    On Error GoTo Fallo

    etapa = "validar_documento_activo"
    If Application.Documents.Count = 0 Then
        MsgBox "Abre primero TEMA 1.docx y vuelve a ejecutar la prueba.", vbExclamation
        Exit Sub
    End If

    carpetaTemas = NormalizarRutaMac(Application.ActiveDocument.Path)

    ' Si Word abre desde SharePoint/OneDrive web, Path llega como URL.
    ' En ese caso usamos la carpeta local sincronizada en CloudStorage.
    If LCase$(Left$(carpetaTemas, 4)) = "http" Then
        carpetaTemas = ResolverRutaTemasAutomatica()
    End If

    If Len(carpetaTemas) = 0 Then
        MsgBox "No se pudo resolver la carpeta local TEMAS.", vbCritical
        Exit Sub
    End If

    etapa = "construir_rutas"
    origPath = PathCombinar(carpetaTemas, "TEMA 1.docx")
    revPath = PathCombinar(carpetaTemas, "tema_1_rev.docx")
    outPath = PathCombinar(carpetaTemas, "TEMA 1_ACTUALIZADO_TEST.docx")

    etapa = "validar_archivos"
    If Not ExisteArchivo(origPath) Then
        MsgBox "No existe: " & origPath, vbCritical
        Exit Sub
    End If
    If Not ExisteArchivo(revPath) Then
        MsgBox "No existe: " & revPath, vbCritical
        Exit Sub
    End If

    Application.ScreenUpdating = False
    Application.DisplayAlerts = wdAlertsNone

    etapa = "abrir_original"
    Set docOrig = Application.Documents.Open(FileName:=origPath, ReadOnly:=True, AddToRecentFiles:=False, Visible:=False)

    etapa = "abrir_revisado"
    Set docRev = Application.Documents.Open(FileName:=revPath, ReadOnly:=True, AddToRecentFiles:=False, Visible:=False)

    etapa = "comparar"
    Set docCmp = Application.CompareDocuments(OriginalDocument:=docOrig, _
                                              RevisedDocument:=docRev, _
                                              Destination:=wdCompareDestinationNew, _
                                              Granularity:=wdGranularityWordLevel)

    etapa = "aceptar_revisiones"
    docCmp.AcceptAllRevisions

    etapa = "actualizar_campos"
    docCmp.Fields.Update

    etapa = "guardar"
    docCmp.SaveAs2 FileName:=outPath, FileFormat:=wdFormatXMLDocument

    etapa = "cerrar"
    docCmp.Close SaveChanges:=wdDoNotSaveChanges
    docRev.Close SaveChanges:=wdDoNotSaveChanges
    docOrig.Close SaveChanges:=wdDoNotSaveChanges

    Application.DisplayAlerts = wdAlertsAll
    Application.ScreenUpdating = True

    MsgBox "Prueba OK. Salida generada en:" & vbCrLf & outPath, vbInformation
    Exit Sub

Fallo:
    On Error Resume Next
    If Not docCmp Is Nothing Then docCmp.Close SaveChanges:=wdDoNotSaveChanges
    If Not docRev Is Nothing Then docRev.Close SaveChanges:=wdDoNotSaveChanges
    If Not docOrig Is Nothing Then docOrig.Close SaveChanges:=wdDoNotSaveChanges
    Application.DisplayAlerts = wdAlertsAll
    Application.ScreenUpdating = True
    On Error GoTo 0

    MsgBox "Fallo en etapa '" & etapa & "': " & Err.Number & " - " & Err.Description, vbCritical
End Sub

' Prueba ultra simple, sin selector ni log:
' Resuelve TEMAS desde UNIR y procesa SOLO TEMA 1.
Public Sub ProbarPrimerParDirecto()
    Dim etapa As String
    Dim pTemas As String
    Dim origPath As String
    Dim revPath As String
    Dim outPath As String
    Dim docOrig As Document
    Dim docRev As Document
    Dim docCmp As Document

    On Error GoTo Fallo

    etapa = "resolver_temas_por_archivos"
    pTemas = ResolverRutaTemasPorArchivos()
    If Len(pTemas) = 0 Then
        MsgBox "No se pudo resolver la carpeta TEMAS por busqueda de archivos.", vbCritical
        Exit Sub
    End If

    etapa = "rutas_archivos"
    origPath = PathCombinar(pTemas, "TEMA 1.docx")
    revPath = PathCombinar(pTemas, "tema_1_rev.docx")
    outPath = PathCombinar(pTemas, "TEMA 1_ACTUALIZADO_TEST.docx")

    If Not ExisteArchivo(origPath) Then
        MsgBox "No existe: " & origPath, vbCritical
        Exit Sub
    End If
    If Not ExisteArchivo(revPath) Then
        MsgBox "No existe: " & revPath, vbCritical
        Exit Sub
    End If

    Application.ScreenUpdating = False
    Application.DisplayAlerts = wdAlertsNone

    etapa = "abrir_original"
    Set docOrig = Application.Documents.Open(FileName:=origPath, ReadOnly:=True, AddToRecentFiles:=False, Visible:=False)

    etapa = "abrir_revisado"
    Set docRev = Application.Documents.Open(FileName:=revPath, ReadOnly:=True, AddToRecentFiles:=False, Visible:=False)

    etapa = "comparar"
    Set docCmp = Application.CompareDocuments(OriginalDocument:=docOrig, _
                                              RevisedDocument:=docRev, _
                                              Destination:=wdCompareDestinationNew, _
                                              Granularity:=wdGranularityWordLevel)

    etapa = "aceptar_revisiones"
    docCmp.AcceptAllRevisions

    etapa = "actualizar_campos"
    docCmp.Fields.Update

    etapa = "guardar"
    docCmp.SaveAs2 FileName:=outPath, FileFormat:=wdFormatXMLDocument

    etapa = "cerrar"
    docCmp.Close SaveChanges:=wdDoNotSaveChanges
    docRev.Close SaveChanges:=wdDoNotSaveChanges
    docOrig.Close SaveChanges:=wdDoNotSaveChanges

    Application.DisplayAlerts = wdAlertsAll
    Application.ScreenUpdating = True

    MsgBox "Prueba directa OK. Salida: " & outPath, vbInformation
    Exit Sub

Fallo:
    On Error Resume Next
    If Not docCmp Is Nothing Then docCmp.Close SaveChanges:=wdDoNotSaveChanges
    If Not docRev Is Nothing Then docRev.Close SaveChanges:=wdDoNotSaveChanges
    If Not docOrig Is Nothing Then docOrig.Close SaveChanges:=wdDoNotSaveChanges
    Application.DisplayAlerts = wdAlertsAll
    Application.ScreenUpdating = True
    On Error GoTo 0

    MsgBox "Fallo en etapa '" & etapa & "': " & Err.Number & " - " & Err.Description, vbCritical
End Sub

Public Sub ActualizarTemasLote()
    Dim carpetaTemas As String
    Dim runTag As String
    Dim logPath As String
    Dim logText As String
    Dim i As Long
    Dim okCount As Long
    Dim totalPares As Long
    Dim logHabilitado As Boolean

    carpetaTemas = SeleccionarCarpetaTemas()
    If Len(carpetaTemas) = 0 Then Exit Sub

    carpetaTemas = NormalizarRutaMac(carpetaTemas)
    If EsRutaAliasFinder(carpetaTemas) Then
        MsgBox "Has seleccionado un alias de Finder. Selecciona la carpeta real TEMAS (no el alias).", vbExclamation
        Exit Sub
    End If

    If Not EsCarpetaLegible(carpetaTemas) Then
        MsgBox "La carpeta seleccionada no existe o no es legible:" & vbCrLf & carpetaTemas, vbCritical
        Exit Sub
    End If

    runTag = Format(Now, "yyyymmdd_hhnnss")

    logPath = PathCombinar(carpetaTemas, "proceso_actualizacion_" & runTag & ".log")
    logHabilitado = GuardarTexto(logPath, "")
    If Not logHabilitado Then
        logPath = ""
        MsgBox "No se pudo crear la bitacora. La ejecucion continuara sin log.", vbExclamation
    End If

    logText = "Inicio: " & Now & vbCrLf
    logText = logText & "Entrada: " & carpetaTemas & vbCrLf
    logText = logText & "Salida (misma carpeta): " & carpetaTemas & vbCrLf
    logText = logText & "Etiqueta de ejecucion: " & runTag & vbCrLf
    If logHabilitado Then Call GuardarTexto(logPath, logText)

    Application.ScreenUpdating = False
    Application.DisplayAlerts = wdAlertsNone

    On Error GoTo FatalError

    For i = 1 To 200
        Dim origPath As String
        Dim revPath As String
        Dim outPath As String

        origPath = PathCombinar(carpetaTemas, "TEMA " & CStr(i) & ".docx")
        revPath = PathCombinar(carpetaTemas, "tema_" & CStr(i) & "_rev.docx")
        outPath = PathCombinar(carpetaTemas, "TEMA " & CStr(i) & "_ACTUALIZADO_" & runTag & ".docx")

        If ExisteArchivo(origPath) Or ExisteArchivo(revPath) Then
            If ExisteArchivo(origPath) And ExisteArchivo(revPath) Then
                totalPares = totalPares + 1
                If logHabilitado Then Call AnexarTexto(logPath, "INICIO TEMA " & CStr(i) & ": " & NombreArchivo(origPath) & " + " & NombreArchivo(revPath) & vbCrLf)
                DoEvents

                If ProcesarPar(origPath, revPath, outPath, logText, logPath, logHabilitado) Then
                    okCount = okCount + 1
                End If
            Else
                logText = logText & "SKIP TEMA " & CStr(i) & ": falta uno de los dos archivos" & vbCrLf
                If logHabilitado Then Call AnexarTexto(logPath, "SKIP TEMA " & CStr(i) & ": falta uno de los dos archivos" & vbCrLf)
            End If
        End If
    Next i

    If totalPares = 0 Then
        logText = logText & "No se encontraron pares exactos TEMA n.docx + tema_n_rev.docx" & vbCrLf
    End If

    logText = logText & "Procesados OK: " & CStr(okCount) & "/" & CStr(totalPares) & vbCrLf
    logText = logText & "Fin: " & Now & vbCrLf
    If logHabilitado And Not GuardarTexto(logPath, logText) Then
        MsgBox "No se pudo escribir la bitacora en:" & vbCrLf & logPath, vbExclamation
    End If

    Application.DisplayAlerts = wdAlertsAll
    Application.ScreenUpdating = True

    MsgBox "Completado: " & CStr(okCount) & "/" & CStr(totalPares) & vbCrLf & _
            "Salida: " & carpetaTemas & vbCrLf & _
           "Bitacora: " & IIf(logHabilitado, logPath, "(deshabilitada)"), vbInformation
    Exit Sub

FatalError:
    Application.DisplayAlerts = wdAlertsAll
    Application.ScreenUpdating = True
    If logHabilitado Then Call GuardarTexto(logPath, logText & "ERROR FATAL: " & Err.Number & " - " & Err.Description & vbCrLf)
    MsgBox "Error: " & Err.Number & " - " & Err.Description & vbCrLf & "Bitacora: " & IIf(logHabilitado, logPath, "(deshabilitada)"), vbCritical
End Sub

Private Function SeleccionarCarpetaTemas() As String
    ' 1) Via mas robusta en macOS sandbox: usar carpeta del documento activo.
    SeleccionarCarpetaTemas = CarpetaDesdeDocumentoActivo()
    If Len(SeleccionarCarpetaTemas) > 0 Then
        MsgBox "Se usara la carpeta del documento activo:" & vbCrLf & SeleccionarCarpetaTemas, vbInformation
        Exit Function
    End If

    ' 2) Intento por selector nativo de Word.
    On Error GoTo FallbackAuto

    With Application.FileDialog(4) ' msoFileDialogFolderPicker
        .Title = "Selecciona la carpeta TEMAS"
        .AllowMultiSelect = False
        If .Show = -1 Then
            SeleccionarCarpetaTemas = .SelectedItems(1)
            Exit Function
        End If
    End With

FallbackAuto:
    Err.Clear
    SeleccionarCarpetaTemas = ResolverRutaTemasAutomatica()
    If Len(SeleccionarCarpetaTemas) > 0 Then
        MsgBox "No se mostro el selector. Se usara la carpeta TEMAS detectada automaticamente:" & vbCrLf & SeleccionarCarpetaTemas, vbInformation
        Exit Function
    End If

    ' 3) Ultimo fallback robusto: localizar por nombre de archivo en CloudStorage.
    SeleccionarCarpetaTemas = ResolverRutaTemasPorArchivos()
    If Len(SeleccionarCarpetaTemas) > 0 Then
        MsgBox "Se encontro la carpeta TEMAS por busqueda de archivos:" & vbCrLf & SeleccionarCarpetaTemas, vbInformation
        Exit Function
    End If

    MsgBox "No se pudo abrir el selector ni detectar la carpeta TEMAS automaticamente.", vbExclamation
    Exit Function
End Function

Private Function ResolverRutaTemasPorArchivos() As String
    Dim tema1 As String
    Dim rev1 As String
    Dim d1 As String
    Dim d2 As String

    tema1 = BuscarArchivoPorNombre(RAIZ_CLOUDSTORAGE, "TEMA 1.docx", 9)
    rev1 = BuscarArchivoPorNombre(RAIZ_CLOUDSTORAGE, "tema_1_rev.docx", 9)

    If Len(tema1) = 0 Or Len(rev1) = 0 Then
        ResolverRutaTemasPorArchivos = ""
        Exit Function
    End If

    d1 = CarpetaPadre(tema1)
    d2 = CarpetaPadre(rev1)

    If Len(d1) > 0 And LCase$(d1) = LCase$(d2) Then
        ResolverRutaTemasPorArchivos = d1
    Else
        ResolverRutaTemasPorArchivos = ""
    End If
End Function

Private Function BuscarArchivoPorNombre(ByVal baseDir As String, ByVal nombreObjetivo As String, ByVal maxDepth As Long) As String
    On Error GoTo Fallo

    Dim dirs() As String
    Dim depths() As Long
    Dim head As Long
    Dim tail As Long

    Dim dirActual As String
    Dim depthActual As Long
    Dim nombre As String
    Dim fullPath As String
    Dim attrs As Long

    ReDim dirs(0 To 0)
    ReDim depths(0 To 0)
    dirs(0) = baseDir
    depths(0) = 0
    head = 0
    tail = 0

    Do While head <= tail
        dirActual = dirs(head)
        depthActual = depths(head)
        head = head + 1

        nombre = Dir(PathCombinar(dirActual, "*"))
        Do While Len(nombre) > 0
            If nombre <> "." And nombre <> ".." Then
                fullPath = PathCombinar(dirActual, nombre)

                On Error Resume Next
                attrs = GetAttr(fullPath)
                If Err.Number = 0 Then
                    If (attrs And vbDirectory) = vbDirectory Then
                        If depthActual < maxDepth Then
                            tail = tail + 1
                            ReDim Preserve dirs(0 To tail)
                            ReDim Preserve depths(0 To tail)
                            dirs(tail) = fullPath
                            depths(tail) = depthActual + 1
                        End If
                    Else
                        If LCase$(nombre) = LCase$(nombreObjetivo) Then
                            BuscarArchivoPorNombre = fullPath
                            Exit Function
                        End If
                    End If
                End If
                Err.Clear
                On Error GoTo Fallo
            End If
            nombre = Dir()
        Loop
    Loop

    BuscarArchivoPorNombre = ""
    Exit Function

Fallo:
    BuscarArchivoPorNombre = ""
End Function

Private Function CarpetaPadre(ByVal ruta As String) As String
    Dim p As Long
    p = InStrRev(ruta, "/")
    If p <= 1 Then
        CarpetaPadre = ""
    Else
        CarpetaPadre = Left$(ruta, p - 1)
    End If
End Function

Private Function CarpetaDesdeDocumentoActivo() As String
    On Error GoTo Fallo

    If Application.Documents.Count = 0 Then
        CarpetaDesdeDocumentoActivo = ""
        Exit Function
    End If

    Dim p As String
    p = Application.ActiveDocument.Path
    p = NormalizarRutaMac(p)

    If Len(p) = 0 Then
        CarpetaDesdeDocumentoActivo = ""
        Exit Function
    End If

    If EsCarpetaLegible(p) Then
        CarpetaDesdeDocumentoActivo = p
    Else
        CarpetaDesdeDocumentoActivo = ""
    End If
    Exit Function

Fallo:
    CarpetaDesdeDocumentoActivo = ""
End Function

Private Function ResolverRutaTemasAutomatica() As String
    Dim p1 As String
    Dim p2 As String
    Dim p3 As String
    Dim p4 As String

    p1 = "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/UNIR"
    If Not EsCarpetaLegible(p1) Then
        ResolverRutaTemasAutomatica = ""
        Exit Function
    End If

    p2 = PrimerSubcarpeta(p1, "*Contenidos*")
    If Len(p2) = 0 Then
        ResolverRutaTemasAutomatica = ""
        Exit Function
    End If

    p3 = PrimerSubcarpeta(p2, "Ecosistema Digital*Disruptivas")
    If Len(p3) = 0 Then
        ResolverRutaTemasAutomatica = ""
        Exit Function
    End If

    p4 = PrimerSubcarpeta(p3, "Curso 2026")
    If Len(p4) = 0 Then
        ResolverRutaTemasAutomatica = ""
        Exit Function
    End If

    ResolverRutaTemasAutomatica = PrimerSubcarpeta(p4, "TEMAS")
End Function

Private Function PrimerSubcarpeta(ByVal baseDir As String, ByVal patron As String) As String
    On Error GoTo Fallo

    Dim nombre As String
    Dim candidato As String
    Dim attrs As Long

    nombre = Dir(PathCombinar(baseDir, patron), vbDirectory)
    Do While Len(nombre) > 0
        If nombre <> "." And nombre <> ".." Then
            candidato = PathCombinar(baseDir, nombre)
            On Error Resume Next
            attrs = GetAttr(candidato)
            If Err.Number = 0 Then
                If (attrs And vbDirectory) = vbDirectory Then
                    On Error GoTo 0
                    PrimerSubcarpeta = candidato
                    Exit Function
                End If
            End If
            Err.Clear
            On Error GoTo Fallo
        End If
        nombre = Dir()
    Loop

Fallo:
    PrimerSubcarpeta = ""
End Function

Private Function NormalizarRutaMac(ByVal ruta As String) As String
    Dim p As String

    p = Trim$(ruta)

    ' Finder suele copiar rutas entre comillas simples; eliminamos comillas externas.
    p = QuitarComillasExternas(p)

    If Len(p) >= 2 Then
        If Left$(p, 1) = Chr$(34) And Right$(p, 1) = Chr$(34) Then
            p = Mid$(p, 2, Len(p) - 2)
        End If
    End If

    ' En macOS Word puede devolver rutas POSIX o HFS; no forzamos conversiones.
    If Len(p) > 0 Then
        If Right$(p, 1) = "/" Or Right$(p, 1) = ":" Then
            p = Left$(p, Len(p) - 1)
        End If
    End If
    NormalizarRutaMac = p
End Function

Private Function QuitarComillasExternas(ByVal txt As String) As String
    Dim s As String
    s = Trim$(txt)

    If Len(s) >= 2 Then
        If Left$(s, 1) = "'" And Right$(s, 1) = "'" Then
            s = Mid$(s, 2, Len(s) - 2)
        End If
    End If

    If Len(s) >= 2 Then
        If Left$(s, 1) = Chr$(34) And Right$(s, 1) = Chr$(34) Then
            s = Mid$(s, 2, Len(s) - 2)
        End If
    End If

    QuitarComillasExternas = Trim$(s)
End Function

Private Function SeparadorRuta(ByVal base As String) As String
    If InStr(1, base, ":", vbBinaryCompare) > 0 And InStr(1, base, "/", vbBinaryCompare) = 0 Then
        SeparadorRuta = ":"
    Else
        SeparadorRuta = "/"
    End If
End Function

Private Function PathCombinar(ByVal base As String, ByVal nombre As String) As String
    Dim sep As String
    sep = SeparadorRuta(base)

    If Right$(base, 1) = sep Then
        PathCombinar = base & nombre
    Else
        PathCombinar = base & sep & nombre
    End If
End Function

Private Function EsRutaAliasFinder(ByVal ruta As String) As Boolean
    Dim r As String
    r = LCase$(ruta)

    If Right$(r, 6) = ".alias" Then
        EsRutaAliasFinder = True
        Exit Function
    End If

    If InStr(1, r, ".alias/", vbTextCompare) > 0 Or InStr(1, r, ".alias:", vbTextCompare) > 0 Then
        EsRutaAliasFinder = True
    Else
        EsRutaAliasFinder = False
    End If
End Function

Private Function EsCarpetaLegible(ByVal ruta As String) As Boolean
    On Error Resume Next
    Dim t As String
    Dim rutaHfs As String

    t = Dir(PathCombinar(ruta, "*"))
    If Err.Number = 0 Then
        EsCarpetaLegible = True
        Exit Function
    End If

    Err.Clear
    rutaHfs = PosixAHfs(ruta)
    If Len(rutaHfs) > 0 Then
        t = Dir(PathCombinar(rutaHfs, "*"))
        EsCarpetaLegible = (Err.Number = 0)
    Else
        EsCarpetaLegible = False
    End If

    Err.Clear
    On Error GoTo 0
End Function

Private Function ExisteArchivo(ByVal ruta As String) As Boolean
    On Error Resume Next
    Dim rutaHfs As String

    ExisteArchivo = (Len(Dir(ruta)) > 0)
    If ExisteArchivo Then Exit Function

    Err.Clear
    rutaHfs = PosixAHfs(ruta)
    If Len(rutaHfs) > 0 Then
        ExisteArchivo = (Len(Dir(rutaHfs)) > 0)
    Else
        ExisteArchivo = False
    End If

    Err.Clear
    On Error GoTo 0
End Function

Private Function ProcesarPar(ByVal origPath As String, _
                             ByVal revPath As String, _
                             ByVal outPath As String, _
                             ByRef logText As String, _
                             ByVal logPath As String, _
                             ByVal logHabilitado As Boolean) As Boolean
    On Error GoTo HandleError

    Dim docOrig As Document
    Dim docRev As Document
    Dim docCmp As Document
    Dim etapaLocal As String

    etapaLocal = "abrir_original"
    If logHabilitado Then Call AnexarTexto(logPath, "  etapa: abrir_original" & vbCrLf)

    Set docOrig = Application.Documents.Open(FileName:=origPath, ReadOnly:=True, AddToRecentFiles:=False, Visible:=False)
    etapaLocal = "abrir_revisado"
    If logHabilitado Then Call AnexarTexto(logPath, "  etapa: abrir_revisado" & vbCrLf)
    Set docRev = Application.Documents.Open(FileName:=revPath, ReadOnly:=True, AddToRecentFiles:=False, Visible:=False)

    etapaLocal = "comparar_documentos"
    If logHabilitado Then Call AnexarTexto(logPath, "  etapa: comparar_documentos" & vbCrLf)
    Set docCmp = Application.CompareDocuments(OriginalDocument:=docOrig, _
                                              RevisedDocument:=docRev, _
                                              Destination:=wdCompareDestinationNew, _
                                              Granularity:=wdGranularityWordLevel)

    etapaLocal = "aceptar_revisiones"
    If logHabilitado Then Call AnexarTexto(logPath, "  etapa: aceptar_revisiones" & vbCrLf)
    docCmp.AcceptAllRevisions

    etapaLocal = "actualizar_campos"
    If logHabilitado Then Call AnexarTexto(logPath, "  etapa: actualizar_campos" & vbCrLf)
    docCmp.Fields.Update

    On Error Resume Next
    Dim i As Long
    For i = 1 To docCmp.TablesOfContents.Count
        docCmp.TablesOfContents(i).Update
    Next i
    For i = 1 To docCmp.TablesOfFigures.Count
        docCmp.TablesOfFigures(i).Update
    Next i
    On Error GoTo HandleError

    etapaLocal = "guardar_salida"
    If logHabilitado Then Call AnexarTexto(logPath, "  etapa: guardar_salida" & vbCrLf)
    docCmp.SaveAs2 FileName:=outPath, FileFormat:=wdFormatXMLDocument

    docCmp.Close SaveChanges:=wdDoNotSaveChanges
    docRev.Close SaveChanges:=wdDoNotSaveChanges
    docOrig.Close SaveChanges:=wdDoNotSaveChanges

    logText = logText & "OK: " & NombreArchivo(origPath) & " + " & NombreArchivo(revPath) & " -> " & NombreArchivo(outPath) & vbCrLf
    If logHabilitado Then Call AnexarTexto(logPath, "OK TEMA: " & NombreArchivo(outPath) & vbCrLf)
    ProcesarPar = True
    Exit Function

HandleError:
    On Error Resume Next
    If Not docCmp Is Nothing Then docCmp.Close SaveChanges:=wdDoNotSaveChanges
    If Not docRev Is Nothing Then docRev.Close SaveChanges:=wdDoNotSaveChanges
    If Not docOrig Is Nothing Then docOrig.Close SaveChanges:=wdDoNotSaveChanges
    On Error GoTo 0

    logText = logText & "ERROR (" & etapaLocal & "): " & NombreArchivo(origPath) & " + " & NombreArchivo(revPath) & " :: " & Err.Number & " - " & Err.Description & vbCrLf
    If logHabilitado Then Call AnexarTexto(logPath, "ERROR (" & etapaLocal & "): " & Err.Number & " - " & Err.Description & vbCrLf)
    ProcesarPar = False
End Function

Private Sub AnexarTexto(ByVal ruta As String, ByVal contenido As String)
    On Error Resume Next
    Dim fn As Integer
    fn = FreeFile
    Open ruta For Append As #fn
    Print #fn, contenido;
    Close #fn
    On Error GoTo 0
End Sub

Private Function GuardarTexto(ByVal ruta As String, ByVal contenido As String) As Boolean
    On Error GoTo IntentoHfs
    Dim fn As Integer
    Dim rutaHfs As String

    fn = FreeFile
    Open ruta For Output As #fn
    Print #fn, contenido;
    Close #fn
    GuardarTexto = True
    Exit Function

IntentoHfs:
    Err.Clear
    rutaHfs = PosixAHfs(ruta)
    If Len(rutaHfs) > 0 Then
        On Error GoTo Fallo
        fn = FreeFile
        Open rutaHfs For Output As #fn
        Print #fn, contenido;
        Close #fn
        GuardarTexto = True
        Exit Function
    End If

Fallo:
    GuardarTexto = False
End Function

Private Function PosixAHfs(ByVal rutaPosix As String) As String
    On Error GoTo Fallo

    ' Conversion opcional desactivada para evitar errores de compilacion
    ' por secuencias de escape en VBA para Mac.
    PosixAHfs = ""
    Exit Function

Fallo:
    PosixAHfs = ""
End Function

Private Function NombreArchivo(ByVal rutaCompleta As String) As String
    Dim p As Long
    p = InStrRev(rutaCompleta, "/")
    If p = 0 Then
        NombreArchivo = rutaCompleta
    Else
        NombreArchivo = Mid$(rutaCompleta, p + 1)
    End If
End Function
