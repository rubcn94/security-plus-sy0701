#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrae el contenido de los 21 bloques PDF y genera un JSON estructurado
con toda la informacion del Security+ SY0-701 Fusionado
"""

import PyPDF2
import json
import re
from pathlib import Path

BASE_PATH = Path(r"D:\Users\cra\Desktop\Sec+")
BLOQUES_PATH = BASE_PATH / "bloques_pdf"
OUTPUT_JSON = BASE_PATH / "secplus_fusionado_completo.json"

def extraer_texto_pdf(ruta_pdf):
    """Extrae todo el texto de un PDF"""
    with open(ruta_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        texto_completo = []

        for i, page in enumerate(pdf_reader.pages, 1):
            texto_pagina = page.extract_text()
            texto_completo.append({
                "pagina_relativa": i,
                "texto": texto_pagina
            })

        return texto_completo

def procesar_todos_bloques():
    """Procesa los 21 bloques y genera la estructura JSON"""

    datos = {
        "metadata": {
            "titulo": "CompTIA Security+ SY0-701 Fusionado v2",
            "descripcion": "Guia Completa Fusionada En Espanol",
            "version": "2.0",
            "fuentes": ["Professor Messer SY0-701", "ExamCompass"],
            "total_paginas_pdf": 209,
            "total_bloques": 21,
            "estadisticas": {
                "total_preguntas": 590,
                "preguntas_validas": 582,
                "corregidas_manual": 182,
                "practice_tests": 281,
                "acronyms_quizzes": 135,
                "preguntas_nuevas": 83,
                "dominios": 5
            }
        },
        "bloques": []
    }

    print(f"[INICIO] Extrayendo contenido de 21 bloques PDF...\n")

    for bloque_num in range(1, 22):
        archivo = f"SecPlus_bloque_{bloque_num:02d}.pdf"
        ruta = BLOQUES_PATH / archivo

        if not ruta.exists():
            print(f"  [!] Bloque {bloque_num:02d}: ARCHIVO NO ENCONTRADO")
            continue

        print(f"  [>>] Bloque {bloque_num:02d}/21: {archivo}")

        try:
            # Calcular paginas originales
            pagina_inicio = (bloque_num - 1) * 10 + 1
            pagina_fin = min(bloque_num * 10, 209)

            # Extraer texto
            paginas_extraidas = extraer_texto_pdf(ruta)

            bloque_info = {
                "bloque_numero": bloque_num,
                "archivo": archivo,
                "rango_paginas_original": {
                    "inicio": pagina_inicio,
                    "fin": pagina_fin,
                    "total": pagina_fin - pagina_inicio + 1
                },
                "paginas": paginas_extraidas,
                "total_caracteres": sum(len(p["texto"]) for p in paginas_extraidas),
                "total_paginas_bloque": len(paginas_extraidas)
            }

            datos["bloques"].append(bloque_info)

            print(f"      OK - {len(paginas_extraidas)} pags | {bloque_info['total_caracteres']:,} caracteres")

        except Exception as e:
            print(f"      [ERROR] {str(e)}")

    # Guardar JSON
    print(f"\n[GUARDANDO] Generando JSON...")

    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

    # Estadisticas finales
    total_bloques = len(datos["bloques"])
    total_chars = sum(b["total_caracteres"] for b in datos["bloques"])
    total_pags = sum(b["total_paginas_bloque"] for b in datos["bloques"])

    print(f"\n{'='*60}")
    print(f"[COMPLETADO] JSON generado exitosamente")
    print(f"{'='*60}")
    print(f"  Archivo:          {OUTPUT_JSON}")
    print(f"  Bloques procesados:  {total_bloques}/21")
    print(f"  Paginas totales:     {total_pags}")
    print(f"  Caracteres extraidos: {total_chars:,}")
    print(f"  Tamano JSON:         {OUTPUT_JSON.stat().st_size / 1024 / 1024:.2f} MB")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    procesar_todos_bloques()
