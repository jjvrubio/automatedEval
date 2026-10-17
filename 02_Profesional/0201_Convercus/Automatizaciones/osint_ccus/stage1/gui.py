"""Native macOS CSV picker with a Tk fallback."""

from __future__ import annotations

from pathlib import Path


def choose_csv() -> Path | None:
    try:
        from AppKit import NSApplication, NSModalResponseOK, NSOpenPanel

        NSApplication.sharedApplication()
        panel = NSOpenPanel.openPanel()
        panel.setTitle_("Selecciona el CSV de compañías")
        panel.setPrompt_("Seleccionar")
        panel.setCanChooseFiles_(True)
        panel.setCanChooseDirectories_(False)
        panel.setAllowsMultipleSelection_(False)
        panel.setAllowedFileTypes_(["csv"])
        if panel.runModal() == NSModalResponseOK:
            urls = panel.URLs()
            if urls:
                return Path(str(urls[0].path()))
        return None
    except (ImportError, AttributeError):
        return _choose_with_tk()


def confirm_run(
    company_count: int, estimated_api_calls: int, stage: str = "1a"
) -> bool:
    message = (
        f"Se investigarán {company_count} compañías.\n\n"
        f"Se prevén hasta {estimated_api_calls} llamadas de investigación "
        "a la API.\n\n"
        "La ejecución consumirá créditos. ¿Quieres continuar?"
    )
    try:
        from AppKit import NSAlert, NSAlertFirstButtonReturn

        alert = NSAlert.alloc().init()
        alert.setMessageText_(f"Confirmar Etapa {stage.upper()}")
        alert.setInformativeText_(message)
        alert.addButtonWithTitle_("Iniciar")
        alert.addButtonWithTitle_("Cancelar")
        return alert.runModal() == NSAlertFirstButtonReturn
    except (ImportError, AttributeError):
        return _confirm_with_tk(message)


def _choose_with_tk() -> Path | None:
    try:
        from tkinter import Tk, filedialog
    except ImportError:
        return None

    root = Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(
        title="Selecciona el CSV de compañías",
        filetypes=[("Archivos CSV", "*.csv")],
    )
    root.destroy()
    return Path(filename) if filename else None


def _confirm_with_tk(message: str) -> bool:
    try:
        from tkinter import Tk, messagebox
    except ImportError:
        return False
    root = Tk()
    root.withdraw()
    confirmed = messagebox.askyesno("Confirmar Etapa 1", message)
    root.destroy()
    return bool(confirmed)
