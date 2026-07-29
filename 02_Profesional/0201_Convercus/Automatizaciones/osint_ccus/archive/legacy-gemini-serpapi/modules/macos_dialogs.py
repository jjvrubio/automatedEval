#!/usr/bin/env python3
"""
Módulo de utilidades para diálogos nativos de macOS.
Usa AppKit/Cocoa para consistencia con el resto del repositorio.
"""

from AppKit import (
    NSAlert,
    NSAlertFirstButtonReturn,
    NSTextField,
    NSView,
    NSMakeRect,
    NSPopUpButton
)
from typing import Optional, Tuple


class MacOSDialogs:
    """Diálogos nativos de macOS usando AppKit."""
    
    @staticmethod
    def input_text(
        title: str,
        message: str,
        default_value: str = "",
        button_ok: str = "OK",
        button_cancel: str = "Cancelar"
    ) -> Optional[str]:
        """
        Muestra un diálogo de entrada de texto nativo de macOS.
        
        Args:
            title: Título del diálogo
            message: Mensaje descriptivo
            default_value: Valor por defecto del campo
            button_ok: Texto del botón de confirmación
            button_cancel: Texto del botón de cancelación
        
        Returns:
            Texto ingresado por el usuario, o None si canceló
        """
        alert = NSAlert.alloc().init()
        alert.setMessageText_(title)
        alert.setInformativeText_(message)
        alert.addButtonWithTitle_(button_ok)
        alert.addButtonWithTitle_(button_cancel)
        
        # Crear campo de texto
        input_field = NSTextField.alloc().initWithFrame_(NSMakeRect(0, 0, 300, 24))
        input_field.setStringValue_(default_value)
        
        alert.setAccessoryView_(input_field)
        
        # Mostrar diálogo
        response = alert.runModal()
        
        if response == NSAlertFirstButtonReturn:
            return input_field.stringValue()
        else:
            return None
    
    @staticmethod
    def input_two_fields(
        title: str,
        message: str,
        label1: str,
        label2: str,
        default1: str = "",
        default2: str = "",
        button_ok: str = "OK",
        button_cancel: str = "Cancelar"
    ) -> Optional[Tuple[str, str]]:
        """
        Muestra un diálogo con dos campos de entrada.
        
        Args:
            title: Título del diálogo
            message: Mensaje descriptivo
            label1: Etiqueta del primer campo
            label2: Etiqueta del segundo campo
            default1: Valor por defecto del primer campo
            default2: Valor por defecto del segundo campo
            button_ok: Texto del botón de confirmación
            button_cancel: Texto del botón de cancelación
        
        Returns:
            Tupla (campo1, campo2) o None si canceló
        """
        alert = NSAlert.alloc().init()
        alert.setMessageText_(title)
        alert.setInformativeText_(message)
        alert.addButtonWithTitle_(button_ok)
        alert.addButtonWithTitle_(button_cancel)
        
        # Crear vista contenedora
        view = NSView.alloc().initWithFrame_(NSMakeRect(0, 0, 300, 80))
        
        # Primer campo con etiqueta
        label1_field = NSTextField.alloc().initWithFrame_(NSMakeRect(0, 56, 300, 20))
        label1_field.setStringValue_(label1)
        label1_field.setBezeled_(False)
        label1_field.setDrawsBackground_(False)
        label1_field.setEditable_(False)
        label1_field.setSelectable_(False)
        
        input1 = NSTextField.alloc().initWithFrame_(NSMakeRect(0, 32, 300, 24))
        input1.setStringValue_(default1)
        
        # Segundo campo con etiqueta
        label2_field = NSTextField.alloc().initWithFrame_(NSMakeRect(0, 8, 300, 20))
        label2_field.setStringValue_(label2)
        label2_field.setBezeled_(False)
        label2_field.setDrawsBackground_(False)
        label2_field.setEditable_(False)
        label2_field.setSelectable_(False)
        
        input2 = NSTextField.alloc().initWithFrame_(NSMakeRect(0, -16, 300, 24))
        input2.setStringValue_(default2)
        
        # Agregar campos a la vista
        view.addSubview_(label1_field)
        view.addSubview_(input1)
        view.addSubview_(label2_field)
        view.addSubview_(input2)
        
        alert.setAccessoryView_(view)
        
        # Mostrar diálogo
        response = alert.runModal()
        
        if response == NSAlertFirstButtonReturn:
            return (input1.stringValue(), input2.stringValue())
        else:
            return None
    
    @staticmethod
    def show_info(
        title: str,
        message: str,
        button_text: str = "OK"
    ):
        """
        Muestra un diálogo informativo simple.
        
        Args:
            title: Título del diálogo
            message: Mensaje a mostrar
            button_text: Texto del botón
        """
        alert = NSAlert.alloc().init()
        alert.setMessageText_(title)
        alert.setInformativeText_(message)
        alert.addButtonWithTitle_(button_text)
        alert.runModal()

    @staticmethod
    def choose_option(
        title: str,
        message: str,
        options: list[str],
        button_ok: str = "Seleccionar",
        button_cancel: str = "Cancelar"
    ) -> Optional[int]:
        """
        Muestra un selector desplegable con opciones y devuelve el índice seleccionado o None si canceló.
        """
        alert = NSAlert.alloc().init()
        alert.setMessageText_(title)
        alert.setInformativeText_(message)
        alert.addButtonWithTitle_(button_ok)
        alert.addButtonWithTitle_(button_cancel)

        popup = NSPopUpButton.alloc().initWithFrame_(NSMakeRect(0, 0, 300, 26))
        for opt in options:
            popup.addItemWithTitle_(opt)

        alert.setAccessoryView_(popup)
        response = alert.runModal()

        if response == NSAlertFirstButtonReturn:
            # Obtener índice seleccionado
            selected_title = popup.titleOfSelectedItem()
            try:
                return options.index(selected_title)
            except ValueError:
                return 0
        return None
    
    @staticmethod
    def confirm(
        title: str,
        message: str,
        button_yes: str = "Sí",
        button_no: str = "No"
    ) -> bool:
        """
        Muestra un diálogo de confirmación.
        
        Args:
            title: Título del diálogo
            message: Mensaje de confirmación
            button_yes: Texto del botón afirmativo
            button_no: Texto del botón negativo
        
        Returns:
            True si el usuario confirmó, False si no
        """
        alert = NSAlert.alloc().init()
        alert.setMessageText_(title)
        alert.setInformativeText_(message)
        alert.addButtonWithTitle_(button_yes)
        alert.addButtonWithTitle_(button_no)
        
        response = alert.runModal()
        return response == NSAlertFirstButtonReturn


def request_empresa_escenario() -> Optional[Tuple[str, str]]:
    """
    Solicita al usuario la empresa y el escenario usando diálogo nativo.
    
    Returns:
        Tupla (empresa, escenario) o None si el usuario canceló
    """
    result = MacOSDialogs.input_two_fields(
        title="Configuración de Análisis OSINT",
        message="Ingresa los datos para el análisis:",
        label1="Empresa Target:",
        label2="Escenario de Análisis:",
        default1="",
        default2="Due Diligence Comercial",
        button_ok="Continuar",
        button_cancel="Cancelar"
    )
    
    if result:
        empresa, escenario = result
        # Validar que no estén vacíos
        if empresa.strip() and escenario.strip():
            return (empresa.strip(), escenario.strip())
        else:
            MacOSDialogs.show_info(
                title="Error de Validación",
                message="La empresa y el escenario no pueden estar vacíos."
            )
            return None
    
    return None


def request_scenario_option(scenarios_dict: dict) -> Optional[Tuple[str, str, str]]:
    """
    Solicita selección de escenario desde las opciones disponibles.
    """
    # Construir lista de opciones ordenadas
    keys = sorted(scenarios_dict.keys())
    options: list[str] = []
    for key in keys:
        scenario = scenarios_dict[key]
        options.append(f"OPCIÓN {key}: {scenario['title']}")

    # Mostrar selector
    selected_index = MacOSDialogs.choose_option(
        title="Selecciona Escenario de Análisis",
        message="Elige el contexto estratégico para el análisis:",
        options=options,
        button_ok="Seleccionar",
        button_cancel="Cancelar"
    )

    if selected_index is not None:
        selected_key = keys[selected_index]
        scenario = scenarios_dict[selected_key]
        return (selected_key, scenario['title'], scenario['content'])

    return None


def request_empresa_escenario() -> Optional[Tuple[str, str]]:
    """
    Solicita al usuario la empresa y el escenario usando diálogo nativo.

    Returns:
        Tupla (empresa, escenario_custom) o None si el usuario canceló
    """
    result = MacOSDialogs.input_two_fields(
        title="Configuración de Análisis OSINT",
        message="Ingresa los datos para el análisis:",
        label1="Empresa Target:",
        label2="Contexto adicional (opcional):",
        default1="",
        default2="",
        button_ok="Continuar",
        button_cancel="Cancelar"
    )

    if result:
        empresa, contexto = result
        # Validar que empresa no esté vacía
        if empresa.strip():
            return (empresa.strip(), contexto.strip())
        else:
            MacOSDialogs.show_info(
                title="Error de Validación",
                message="El nombre de la empresa no puede estar vacío."
            )
            return None

    return None


if __name__ == "__main__":
    # Test de los diálogos
    print("🧪 Testeando diálogos nativos de macOS...\n")
    
    # Test 1: Diálogo simple
    nombre = MacOSDialogs.input_text(
        title="Test Simple",
        message="Ingresa tu nombre:",
        default_value="Usuario"
    )
    if nombre:
        print(f"✅ Nombre ingresado: {nombre}")
    
    # Test 2: Diálogo doble campo
    result = request_empresa_escenario()
    if result:
        empresa, escenario = result
        print(f"✅ Empresa: {empresa}")
        print(f"✅ Escenario: {escenario}")
    else:
        print("❌ Usuario canceló")
