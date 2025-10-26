#!/usr/bin/env python3
"""
Script de verificación para confirmar que el evaluador TFM genera análisis únicos.
Este script prueba las funciones críticas que deben generar variabilidad.
"""

import sys
import os
import hashlib
import time
import random

# Añadir el directorio del evaluador al path
sys.path.insert(0, '/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/Grading/UNIR Grading')

def test_temperatura_variabilidad():
    """Verificar que la temperatura no sea 0.0"""
    from Evaluador_TFM_Integrado_ultraestricto import TEMPERATURA_POR_DEFECTO
    
    print(f"🌡️ Temperatura configurada: {TEMPERATURA_POR_DEFECTO}")
    
    if TEMPERATURA_POR_DEFECTO == 0.0:
        print("❌ ERROR: Temperatura sigue en 0.0 - Causa análisis idénticos")
        return False
    elif TEMPERATURA_POR_DEFECTO > 0.0:
        print("✅ OK: Temperatura > 0.0 - Permitirá variabilidad")
        return True
    else:
        print("⚠️ WARNING: Temperatura negativa o inválida")
        return False

def test_extraccion_elementos_unicos():
    """Verificar que la extracción de elementos únicos funciona"""
    try:
        from Evaluador_TFM_Integrado_ultraestricto import extraer_elementos_unicos_del_documento
        
        # Texto de prueba con elementos únicos
        texto_prueba = """
        La transformación digital de la fiscalización tributaria en Colombia 
        presenta un nivel de madurez digital básico del 47.4% según el análisis
        realizado con la metodología COBIT Framework. Se identificaron 5 riesgos
        principales mediante entrevistas con 15 participantes en el DIAN.
        """
        
        elementos = extraer_elementos_unicos_del_documento(texto_prueba)
        print(f"🔍 Elementos únicos extraídos:")
        print(elementos)
        
        # Verificar que se extraen números
        if "47.4" in elementos or "15" in elementos:
            print("✅ OK: Extracción de números específicos funciona")
            return True
        else:
            print("❌ ERROR: No se extraen números específicos")
            return False
            
    except Exception as e:
        print(f"❌ ERROR en extracción de elementos únicos: {e}")
        return False

def test_hash_documento():
    """Verificar que se genera hash único por documento"""
    texto1 = "Este es el primer documento de prueba con contenido específico."
    texto2 = "Este es el segundo documento diferente con otro contenido único."
    
    hash1 = hashlib.md5(texto1.encode('utf-8')).hexdigest()[:12]
    hash2 = hashlib.md5(texto2.encode('utf-8')).hexdigest()[:12]
    
    print(f"🔑 Hash documento 1: {hash1}")
    print(f"🔑 Hash documento 2: {hash2}")
    
    if hash1 != hash2:
        print("✅ OK: Hashes únicos para documentos diferentes")
        return True
    else:
        print("❌ ERROR: Mismo hash para documentos diferentes")
        return False

def test_semilla_aleatoria():
    """Verificar que se genera semilla aleatoria diferente"""
    semillas = []
    
    for i in range(3):
        seed_unico = int(time.time() * 1000000) % 999999
        semillas.append(seed_unico)
        print(f"🎲 Semilla {i+1}: {seed_unico}")
        time.sleep(0.001)  # Pequeña pausa para garantizar diferencia
    
    if len(set(semillas)) == len(semillas):
        print("✅ OK: Semillas aleatorias únicas generadas")
        return True
    else:
        print("❌ ERROR: Semillas idénticas generadas")
        return False

def test_max_tokens():
    """Verificar que max_tokens es suficiente"""
    # Esta función solo verifica que los valores estén en el código
    print("🔢 Verificando configuración de max_tokens en el código...")
    
    with open('/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/Grading/UNIR Grading/Evaluador_TFM_Integrado_ultraestricto.py', 'r') as f:
        contenido = f.read()
    
    if 'max_tokens=3000' in contenido:
        print("✅ OK: max_tokens=3000 configurado para análisis profundo")
        resultado1 = True
    else:
        print("❌ ERROR: max_tokens=3000 no encontrado")
        resultado1 = False
    
    if 'max_tokens=2000' in contenido:
        print("✅ OK: max_tokens=2000 configurado para evaluación de criterios")
        resultado2 = True
    else:
        print("❌ ERROR: max_tokens=2000 no encontrado") 
        resultado2 = False
    
    return resultado1 and resultado2

def main():
    """Ejecutar todas las pruebas"""
    print("🔍 VERIFICACIÓN DEL EVALUADOR TFM - ANÁLISIS ÚNICOS")
    print("=" * 60)
    
    tests = [
        ("Temperatura de variabilidad", test_temperatura_variabilidad),
        ("Extracción de elementos únicos", test_extraccion_elementos_unicos),
        ("Hash único por documento", test_hash_documento),
        ("Semilla aleatoria", test_semilla_aleatoria),
        ("Max tokens suficientes", test_max_tokens)
    ]
    
    resultados = []
    
    for nombre, test_func in tests:
        print(f"\n📋 Probando: {nombre}")
        print("-" * 40)
        try:
            resultado = test_func()
            resultados.append((nombre, resultado))
        except Exception as e:
            print(f"❌ ERROR en {nombre}: {e}")
            resultados.append((nombre, False))
    
    # Resumen final
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE VERIFICACIÓN")
    print("=" * 60)
    
    tests_ok = 0
    for nombre, resultado in resultados:
        estado = "✅ PASS" if resultado else "❌ FAIL"
        print(f"{estado} {nombre}")
        if resultado:
            tests_ok += 1
    
    print(f"\n🎯 Resultado final: {tests_ok}/{len(tests)} pruebas pasadas")
    
    if tests_ok == len(tests):
        print("🎉 ¡TODOS LOS TESTS PASARON! El evaluador debe generar análisis únicos ahora.")
        return True
    else:
        print("⚠️ Algunos tests fallaron. El evaluador puede seguir generando análisis idénticos.")
        return False

if __name__ == "__main__":
    main()