#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Identifica las preguntas de ALTA y MEDIA prioridad en el PDF original
Genera una guia de que paginas marcar en el PDF impreso
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import json
import re
from pathlib import Path
from collections import defaultdict

JSON_COMPLETO = Path(r"D:\Users\cra\Desktop\Sec+\secplus_fusionado_completo.json")
JSON_ESTRUCTURADO = Path(r"D:\Users\cra\Desktop\Sec+\secplus_estructurado.json")
OUTPUT_TXT = Path(r"D:\Users\cra\Desktop\Sec+\GUIA_PREGUNTAS_PRIORITARIAS.txt")

def cargar_jsons():
    with open(JSON_COMPLETO, 'r', encoding='utf-8') as f:
        completo = json.load(f)
    with open(JSON_ESTRUCTURADO, 'r', encoding='utf-8') as f:
        estructurado = json.load(f)
    return completo, estructurado

def extraer_conceptos_prioritarios(estructurado):
    """Extrae todos los conceptos de ALTA y MEDIA prioridad"""
    conceptos = {
        'alta': set(),
        'media': set()
    }

    for dom_num, dominio in estructurado['dominios'].items():
        for concepto in dominio['prioridades']['alta']:
            # Extraer palabras clave del concepto
            palabras = concepto.lower().split('/')
            for palabra in palabras:
                palabra = palabra.strip()
                if len(palabra) > 3:
                    conceptos['alta'].add(palabra)

        for concepto in dominio['prioridades']['media']:
            palabras = concepto.lower().split('/')
            for palabra in palabras:
                palabra = palabra.strip()
                if len(palabra) > 3:
                    conceptos['media'].add(palabra)

    return conceptos

def analizar_preguntas(completo, conceptos_prioritarios):
    """Analiza cada pregunta y determina si es de ALTA/MEDIA prioridad"""

    preguntas_alta = []
    preguntas_media = []
    preguntas_otras = []

    pregunta_num = 0

    for bloque in completo['bloques']:
        bloque_num = bloque['bloque_numero']

        for pag_rel, pagina in enumerate(bloque['paginas'], 1):
            pag_absoluta = bloque['rango_paginas_original']['inicio'] + pag_rel - 1
            texto = pagina['texto']
            lineas = texto.split('\n')

            pregunta_actual = None
            texto_pregunta = ""
            opciones = []

            for i, linea in enumerate(lineas):
                linea = linea.strip()

                # Detectar inicio de pregunta (numero seguido de punto)
                match_pregunta = re.match(r'^(\d+)\.\s+(.+)', linea)
                if match_pregunta and len(match_pregunta.group(2)) > 20:
                    # Guardar pregunta anterior si existe
                    if pregunta_actual:
                        pregunta_num += 1
                        clasificar_y_guardar(
                            pregunta_num, pregunta_actual, texto_pregunta, opciones,
                            pag_absoluta, conceptos_prioritarios,
                            preguntas_alta, preguntas_media, preguntas_otras
                        )

                    # Nueva pregunta
                    pregunta_actual = {
                        'numero_local': match_pregunta.group(1),
                        'pagina': pag_absoluta,
                        'bloque': bloque_num
                    }
                    texto_pregunta = match_pregunta.group(2)
                    opciones = []

                # Detectar opciones
                elif pregunta_actual and re.match(r'^[✓\s]*[A-J]\)', linea):
                    opciones.append(linea)

                # Acumular texto de pregunta multilínea
                elif pregunta_actual and not linea.startswith('Fuente:') and texto_pregunta and len(linea) > 10:
                    if not re.match(r'^[A-J]\)', linea):
                        texto_pregunta += " " + linea

            # Guardar ultima pregunta de la pagina
            if pregunta_actual:
                pregunta_num += 1
                clasificar_y_guardar(
                    pregunta_num, pregunta_actual, texto_pregunta, opciones,
                    pag_absoluta, conceptos_prioritarios,
                    preguntas_alta, preguntas_media, preguntas_otras
                )

    return preguntas_alta, preguntas_media, preguntas_otras

def clasificar_y_guardar(num, pregunta, texto, opciones, pagina, conceptos, alta, media, otras):
    """Clasifica una pregunta segun conceptos prioritarios"""

    texto_completo = (texto + " " + " ".join(opciones)).lower()

    # Buscar coincidencias con conceptos ALTA
    matches_alta = []
    for concepto in conceptos['alta']:
        if concepto in texto_completo:
            matches_alta.append(concepto)

    # Buscar coincidencias con conceptos MEDIA
    matches_media = []
    for concepto in conceptos['media']:
        if concepto in texto_completo:
            matches_media.append(concepto)

    info = {
        'numero_global': num,
        'numero_local': pregunta['numero_local'],
        'pagina': pagina,
        'bloque': pregunta['bloque'],
        'pregunta': texto[:100] + "..." if len(texto) > 100 else texto,
        'matches_alta': matches_alta,
        'matches_media': matches_media
    }

    # Clasificar
    if len(matches_alta) >= 2:  # Al menos 2 conceptos ALTA
        alta.append(info)
    elif len(matches_alta) >= 1 or len(matches_media) >= 2:  # 1 ALTA o 2+ MEDIA
        media.append(info)
    else:
        otras.append(info)

def generar_guia(preguntas_alta, preguntas_media, preguntas_otras):
    """Genera la guia en formato texto"""

    output = []
    output.append("="*80)
    output.append(" GUIA DE PREGUNTAS PRIORITARIAS - CompTIA Security+ SY0-701")
    output.append("="*80)
    output.append("")
    output.append("Esta guia te indica que preguntas marcar en tu PDF impreso")
    output.append("segun la prioridad de los conceptos que cubren.")
    output.append("")
    output.append(f"Total preguntas analizadas: {len(preguntas_alta) + len(preguntas_media) + len(preguntas_otras)}")
    output.append(f"  • ALTA prioridad:  {len(preguntas_alta)} preguntas")
    output.append(f"  • MEDIA prioridad: {len(preguntas_media)} preguntas")
    output.append(f"  • Otras:           {len(preguntas_otras)} preguntas")
    output.append("")
    output.append("="*80)
    output.append("")

    # ALTA PRIORIDAD
    output.append("╔" + "="*78 + "╗")
    output.append("║" + " PREGUNTAS DE ALTA PRIORIDAD (marcar con ROJO) ".center(78) + "║")
    output.append("╚" + "="*78 + "╝")
    output.append("")
    output.append(f"Total: {len(preguntas_alta)} preguntas")
    output.append("")

    # Agrupar por pagina
    por_pagina = defaultdict(list)
    for p in preguntas_alta:
        por_pagina[p['pagina']].append(p)

    output.append("RESUMEN POR PAGINA:")
    output.append("-" * 80)
    for pagina in sorted(por_pagina.keys()):
        nums = [p['numero_local'] for p in por_pagina[pagina]]
        output.append(f"  Pagina {pagina:3d}: Preguntas {', '.join(nums)}")

    output.append("")
    output.append("DETALLE:")
    output.append("-" * 80)

    for p in sorted(preguntas_alta, key=lambda x: x['pagina']):
        output.append(f"\n[ALTA] Pag {p['pagina']:3d} - Pregunta #{p['numero_local']}")
        output.append(f"       {p['pregunta']}")
        if p['matches_alta']:
            output.append(f"       Conceptos: {', '.join(p['matches_alta'][:3])}")

    # MEDIA PRIORIDAD
    output.append("\n\n")
    output.append("╔" + "="*78 + "╗")
    output.append("║" + " PREGUNTAS DE MEDIA PRIORIDAD (marcar con NARANJA) ".center(78) + "║")
    output.append("╚" + "="*78 + "╝")
    output.append("")
    output.append(f"Total: {len(preguntas_media)} preguntas")
    output.append("")

    por_pagina = defaultdict(list)
    for p in preguntas_media:
        por_pagina[p['pagina']].append(p)

    output.append("RESUMEN POR PAGINA:")
    output.append("-" * 80)
    for pagina in sorted(por_pagina.keys()):
        nums = [p['numero_local'] for p in por_pagina[pagina]]
        output.append(f"  Pagina {pagina:3d}: Preguntas {', '.join(nums)}")

    output.append("")
    output.append("DETALLE:")
    output.append("-" * 80)

    for p in sorted(preguntas_media, key=lambda x: x['pagina']):
        output.append(f"\n[MEDIA] Pag {p['pagina']:3d} - Pregunta #{p['numero_local']}")
        output.append(f"        {p['pregunta']}")
        conceptos = p['matches_alta'] + p['matches_media']
        if conceptos:
            output.append(f"        Conceptos: {', '.join(conceptos[:3])}")

    # ESTADISTICAS FINALES
    output.append("\n\n")
    output.append("="*80)
    output.append(" ESTADISTICAS Y RECOMENDACIONES")
    output.append("="*80)
    output.append("")

    total = len(preguntas_alta) + len(preguntas_media) + len(preguntas_otras)
    pct_alta = (len(preguntas_alta) / total * 100) if total > 0 else 0
    pct_media = (len(preguntas_media) / total * 100) if total > 0 else 0
    pct_prioritarias = pct_alta + pct_media

    output.append(f"Cobertura de preguntas prioritarias:")
    output.append(f"  • ALTA:   {len(preguntas_alta):3d} preguntas ({pct_alta:5.1f}%)")
    output.append(f"  • MEDIA:  {len(preguntas_media):3d} preguntas ({pct_media:5.1f}%)")
    output.append(f"  • TOTAL:  {len(preguntas_alta) + len(preguntas_media):3d} preguntas ({pct_prioritarias:5.1f}%)")
    output.append("")
    output.append("RECOMENDACION:")
    output.append("  1. Estudia primero el PDF condensado (13 paginas)")
    output.append(f"  2. Practica las {len(preguntas_alta)} preguntas marcadas ROJO (ALTA)")
    output.append(f"  3. Practica las {len(preguntas_media)} preguntas marcadas NARANJA (MEDIA)")
    output.append(f"  4. Esto cubre el {pct_prioritarias:.0f}% de las preguntas mas importantes")
    output.append("")
    output.append("="*80)

    return "\n".join(output)

def main():
    print("\n" + "="*80)
    print(" ANALIZADOR DE PREGUNTAS PRIORITARIAS")
    print("="*80)

    print("\nCargando datos...")
    completo, estructurado = cargar_jsons()

    print("Extrayendo conceptos prioritarios...")
    conceptos = extraer_conceptos_prioritarios(estructurado)
    print(f"  • {len(conceptos['alta'])} conceptos ALTA")
    print(f"  • {len(conceptos['media'])} conceptos MEDIA")

    print("\nAnalizando preguntas del PDF...")
    alta, media, otras = analizar_preguntas(completo, conceptos)

    print(f"\nResultados:")
    print(f"  • {len(alta)} preguntas ALTA prioridad")
    print(f"  • {len(media)} preguntas MEDIA prioridad")
    print(f"  • {len(otras)} preguntas otras")

    print(f"\nGenerando guia en: {OUTPUT_TXT}")
    guia = generar_guia(alta, media, otras)

    with open(OUTPUT_TXT, 'w', encoding='utf-8') as f:
        f.write(guia)

    print("\n" + "="*80)
    print(" GUIA GENERADA EXITOSAMENTE")
    print("="*80)
    print(f"\nArchivo: {OUTPUT_TXT}")
    print(f"\nAhora puedes:")
    print(f"  1. Abrir el archivo de texto")
    print(f"  2. Marcar con ROJO las {len(alta)} preguntas ALTA en tu PDF impreso")
    print(f"  3. Marcar con NARANJA las {len(media)} preguntas MEDIA")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
