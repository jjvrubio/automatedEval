#!/bin/bash
# ===============================================
# Script de Instalación del Sistema de Referencias
# ===============================================

echo "🚀 INSTALANDO SISTEMA DE VALIDACIÓN DE REFERENCIAS"
echo "=================================================="

# Verificar que estamos en el directorio correcto
if [[ ! -f "referencias_validator.py" ]]; then
    echo "❌ Error: Ejecutar desde el directorio 'APA Report'"
    echo "   cd 'automatedEval/APA Report'"
    exit 1
fi

echo "📍 Directorio verificado: $(pwd)"

# Verificar Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    exit 1
fi

echo "✅ Python 3 encontrado: $(python3 --version)"

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip3 install -r requirements_referencias.txt

if [[ $? -eq 0 ]]; then
    echo "✅ Dependencias instaladas correctamente"
else
    echo "❌ Error instalando dependencias"
    exit 1
fi

# Verificar instalación
echo "🔍 Verificando instalación..."
python3 -c "import pdfplumber, lxml; print('✅ Dependencias verificadas')"

if [[ $? -eq 0 ]]; then
    echo "✅ Sistema listo para usar"
else
    echo "❌ Error en la verificación"
    exit 1
fi

# Mostrar ayuda
echo ""
echo "🎉 INSTALACIÓN COMPLETADA"
echo "========================="
echo ""
echo "📚 Comandos disponibles:"
echo "   python3 referencias_validator.py --help"
echo "   python3 ejemplos_uso.py"
echo ""
echo "💡 Ejemplo de uso:"
echo "   python3 referencias_validator.py --archivo documento.pdf --estilo apa"
echo ""
echo "📖 Documentación completa:"
echo "   README_REFERENCIAS.md"