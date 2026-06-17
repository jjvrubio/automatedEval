# Rubrica PDF Export Macro

This Visual Basic for Applications (VBA) macro batch-exports the worksheet named "Rubrica" from every Excel workbook in a chosen folder to individual PDF files. It is designed for evaluators who need to generate standardized rubric reports without opening each workbook manually.

## Key Features
- Detects the worksheet even if its name mixes upper/lower case or includes Spanish accented characters (for example "Rubrica", "RUBRICA", or "Rubrica" escrito con tilde).
- Supports files with the ``.xlsx`` and ``.xlsm`` extensions.
- Keeps each PDF in the same folder as its source workbook, reusing the workbook name as the PDF base name.
- Configures the page setup automatically for A4 portrait output scaled to one page.

## Usage
1. Open the VBA editor in Excel (``ALT`` + ``F11``) and import ``macro_code.bas`` into a module, or paste its contents into an existing module.
2. Ensure macros are enabled for the workbook that will host the macro.
3. Run ``ExportWorksheetsToPDF``.
4. When prompted, select the folder that contains the Excel files to process.
5. Wait for the confirmation dialog indicating that each matching worksheet has been exported.

## Requirements and Notes
- The macro uses ``MacScript`` to display the folder picker on macOS. On Windows, replace the folder-selection block with ``Application.FileDialog`` if needed.
- The workbook containing the macro should remain open during execution.
- PDF files with the same name will be overwritten without confirmation. Move or rename existing PDFs beforehand if you need to keep older versions.
- To support additional worksheet names, update the call to ``BuscarHojaPorNombre`` in ``macro_code.bas`` with the desired target name.
