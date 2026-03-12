#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analiza el JSON generado para identificar:
- Redundancias
- Contenido duplicado
- Estructura suboptima
- Proponer mejoras
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import json
import re
from collections import defaultdict
from pathlib import Path

JSON_PATH = Path(r"D:\Users\cra\Desktop\Sec+\secplus_fusionado_completo.json")

def cargar_json():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def analizar_estructura(datos):
    """Analiza la estructura general del JSON"""
    print("="*70)
    print("ANALISIS DE ESTRUCTURA DEL JSON")
    print("="*70)

    print(f"\n1. METADATA:")
    print(f"   - Titulo: {datos['metadata']['titulo']}")
    print(f"   - Total paginas: {datos['metadata']['total_paginas_pdf']}")
    print(f"   - Total bloques: {len(datos['bloques'])}")

    print(f"\n2. BLOQUES:")
    total_chars = 0
    total_pages = 0
    for bloque in datos['bloques']:
        total_chars += bloque['total_caracteres']
        total_pages += bloque['total_paginas_bloque']

    print(f"   - Bloques procesados: {len(datos['bloques'])}")
    print(f"   - Paginas totales: {total_pages}")
    print(f"   - Caracteres totales: {total_chars:,}")
    print(f"   - Promedio chars/pagina: {total_chars//total_pages:,}")

def detectar_patrones(datos):
    """Detecta patrones y estructuras en el contenido"""
    print("\n" + "="*70)
    print("DETECCION DE PATRONES Y ESTRUCTURAS")
    print("="*70)

    # Buscar secciones recurrentes
    patrones = {
        'dominios': 0,
        'objetivos': 0,
        'preguntas_topic': 0,
        'preguntas_practice': 0,
        'preguntas_acronyms': 0,
        'preguntas_nuevas': 0,
        'flashcards': 0,
        'teoria_messer': 0,
        'teoria_examcompass': 0,
        'mapa_prioridades': 0,
        'tabla_contenidos': 0
    }

    for bloque in datos['bloques']:
        for pagina in bloque['paginas']:
            texto = pagina['texto'].lower()

            if 'dominio' in texto and re.search(r'dominio\s+\d+', texto):
                patrones['dominios'] += 1
            if 'objetivo' in texto and re.search(r'\d+\.\d+', texto):
                patrones['objetivos'] += 1
            if 'preguntas topic' in texto or 'topic:' in texto:
                patrones['preguntas_topic'] += 1
            if 'practice test' in texto:
                patrones['preguntas_practice'] += 1
            if 'acronyms quiz' in texto:
                patrones['preguntas_acronyms'] += 1
            if 'preguntas adicionales' in texto or 'preguntas nuevas' in texto:
                patrones['preguntas_nuevas'] += 1
            if 'flashcard' in texto:
                patrones['flashcards'] += 1
            if 'professor messer' in texto or 'conceptos clave' in texto:
                patrones['teoria_messer'] += 1
            if 'examcompass' in texto or 'teoria complementaria' in texto:
                patrones['teoria_examcompass'] += 1
            if 'alta prioridad' in texto or 'media prioridad' in texto:
                patrones['mapa_prioridades'] += 1
            if 'tabla de contenidos' in texto:
                patrones['tabla_contenidos'] += 1

    print("\nSecciones detectadas (menciones):")
    for seccion, count in sorted(patrones.items(), key=lambda x: -x[1]):
        if count > 0:
            print(f"   - {seccion:25s}: {count:3d} veces")

def identificar_redundancias(datos):
    """Identifica contenido redundante o duplicado"""
    print("\n" + "="*70)
    print("IDENTIFICACION DE REDUNDANCIAS")
    print("="*70)

    # Buscar textos repetidos (headers, footers, etc)
    textos_frecuentes = defaultdict(int)
    lineas_cortas = []

    for bloque in datos['bloques']:
        for pagina in bloque['paginas']:
            lineas = pagina['texto'].split('\n')
            for linea in lineas:
                linea = linea.strip()
                if 10 < len(linea) < 100:  # Lineas sospechosas de ser headers/footers
                    textos_frecuentes[linea] += 1

    print("\nTextos repetidos mas de 10 veces (probables headers/footers):")
    repetidos = [(texto, count) for texto, count in textos_frecuentes.items() if count > 10]
    repetidos.sort(key=lambda x: -x[1])

    for texto, count in repetidos[:15]:
        texto_limpio = texto[:80].encode('ascii', 'replace').decode('ascii')
        print(f"   [{count:3d}x] {texto_limpio}")

def extraer_estructura_contenido(datos):
    """Extrae y organiza la estructura real del contenido"""
    print("\n" + "="*70)
    print("EXTRACCION DE ESTRUCTURA DE CONTENIDO")
    print("="*70)

    estructura = {
        'portada': [],
        'tabla_contenidos': [],
        'mapa_prioridades': [],
        'dominios': defaultdict(lambda: {'objetivos': defaultdict(dict)}),
        'practice_tests': [],
        'acronyms': []
    }

    dominio_actual = None
    objetivo_actual = None

    for bloque in datos['bloques']:
        for pagina in bloque['paginas']:
            texto = pagina['texto']

            # Detectar dominio
            match_dominio = re.search(r'DOMINIO\s+(\d+)\s+(.+?)\((\d+)%', texto)
            if match_dominio:
                dominio_num = int(match_dominio.group(1))
                dominio_nombre = match_dominio.group(2).strip()
                dominio_porcentaje = int(match_dominio.group(3))
                dominio_actual = dominio_num
                estructura['dominios'][dominio_num]['nombre'] = dominio_nombre
                estructura['dominios'][dominio_num]['porcentaje'] = dominio_porcentaje
                print(f"\n   [DOMINIO {dominio_num}] {dominio_nombre} ({dominio_porcentaje}%)")

            # Detectar objetivo
            match_objetivo = re.search(r'^(\d+\.\d+)\s+(.+)', texto, re.MULTILINE)
            if match_objetivo and dominio_actual:
                obj_id = match_objetivo.group(1)
                obj_titulo = match_objetivo.group(2).strip()
                if obj_id.startswith(str(dominio_actual)):
                    objetivo_actual = obj_id
                    if 'titulo' not in estructura['dominios'][dominio_actual]['objetivos'][obj_id]:
                        estructura['dominios'][dominio_actual]['objetivos'][obj_id]['titulo'] = obj_titulo
                        print(f"      └─ {obj_id} {obj_titulo[:50]}")

    return estructura

def proponer_reorganizacion(datos, estructura):
    """Propone una estructura JSON optimizada"""
    print("\n" + "="*70)
    print("PROPUESTA DE REORGANIZACION")
    print("="*70)

    print("\nESTRUCTURA ACTUAL:")
    print("  secplus_fusionado_completo.json (0.46 MB)")
    print("  └─ metadata")
    print("  └─ bloques[21]")
    print("      └─ paginas[10]")
    print("          └─ texto (string plano)")
    print("\nPROBLEMAS DETECTADOS:")
    print("  1. Texto plano sin estructura semantica")
    print("  2. Headers/footers repetidos en cada pagina")
    print("  3. No separacion clara entre teoria y preguntas")
    print("  4. Dificil extraer solo contenido de prioridad ALTA/MEDIA")
    print("  5. Redundancia: 'Pagina X | Messer + ExamCompass' repetido 209 veces")

    print("\nESTRUCTURA PROPUESTA:")
    print("  secplus_estructurado.json")
    print("  └─ metadata (igual)")
    print("  └─ contenido")
    print("      └─ portada")
    print("      └─ tabla_contenidos")
    print("      └─ mapa_prioridades_global")
    print("      └─ dominios[5]")
    print("          └─ info: {numero, nombre, porcentaje}")
    print("          └─ prioridades: {alta[], media[], baja[]}")
    print("          └─ objetivos[]")
    print("              └─ id: '1.1'")
    print("              └─ titulo: '...'")
    print("              └─ teoria_messer: {puntos_clave[], conceptos[]}")
    print("              └─ teoria_examcompass: []")
    print("              └─ preguntas_topic[]")
    print("              └─ preguntas_nuevas[]")
    print("              └─ flashcards[]")
    print("      └─ practice_tests[]")
    print("      └─ acronyms_quizzes[]")

    print("\nBENEFICIOS:")
    print("  + Estructura semantica clara")
    print("  + Facil filtrar por prioridad (ALTA/MEDIA)")
    print("  + Elimina redundancias (headers/footers)")
    print("  + Acceso directo a dominios/objetivos")
    print("  + Reduccion estimada de tamaño: 20-30%")

def calcular_estadisticas_prioridades(datos):
    """Calcula cuanto contenido es ALTA vs MEDIA vs BAJA prioridad"""
    print("\n" + "="*70)
    print("ESTADISTICAS DE PRIORIDADES")
    print("="*70)

    contenido_por_prioridad = {
        'ALTA': 0,
        'MEDIA': 0,
        'COMPLEMENTARIO': 0,
        'SIN_CLASIFICAR': 0
    }

    for bloque in datos['bloques']:
        for pagina in bloque['paginas']:
            texto = pagina['texto']

            if 'ALTA PRIORIDAD' in texto or 'alta prioridad' in texto.lower():
                contenido_por_prioridad['ALTA'] += len(texto)
            elif 'MEDIA PRIORIDAD' in texto or 'media prioridad' in texto.lower():
                contenido_por_prioridad['MEDIA'] += len(texto)
            elif 'COMPLEMENTARIO' in texto or 'complementario' in texto.lower():
                contenido_por_prioridad['COMPLEMENTARIO'] += len(texto)
            else:
                contenido_por_prioridad['SIN_CLASIFICAR'] += len(texto)

    total = sum(contenido_por_prioridad.values())

    print("\nDistribucion aproximada de contenido:")
    for nivel, chars in sorted(contenido_por_prioridad.items(), key=lambda x: -x[1]):
        porcentaje = (chars / total * 100) if total > 0 else 0
        print(f"   - {nivel:20s}: {chars:8,} chars ({porcentaje:5.1f}%)")

    print(f"\nSi creas PDF solo con ALTA + MEDIA:")
    alta_media = contenido_por_prioridad['ALTA'] + contenido_por_prioridad['MEDIA']
    reduccion = (1 - alta_media / total) * 100 if total > 0 else 0
    print(f"   - Reduccion estimada: {reduccion:.1f}%")
    print(f"   - Caracteres restantes: {alta_media:,}")

def main():
    print("\n" + "="*70)
    print(" ANALISIS COMPLETO DEL JSON - CompTIA Security+ SY0-701")
    print("="*70 + "\n")

    datos = cargar_json()

    analizar_estructura(datos)
    detectar_patrones(datos)
    identificar_redundancias(datos)
    estructura = extraer_estructura_contenido(datos)
    proponer_reorganizacion(datos, estructura)
    calcular_estadisticas_prioridades(datos)

    print("\n" + "="*70)
    print(" FIN DEL ANALISIS")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
