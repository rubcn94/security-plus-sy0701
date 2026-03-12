#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Organiza la carpeta Sec+ en una estructura limpia y logica
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import os
import shutil
from pathlib import Path

BASE = Path(r"D:\Users\cra\Desktop\Sec+")

# Estructura de carpetas
ESTRUCTURA = {
    "01_PDFs_Finales": [
        "SecPlus_SY0-701_CONDENSADO.pdf",
        "SecPlus_SY0-701_FUSIONADO.pdf",
        "GUIA_PREGUNTAS_PRIORITARIAS.txt"
    ],
    "02_PDFs_Referencia": [
        "comptia-security-plus-sy0-701-exam-objectives.pdf",
        "Messer_Conceptos_COMPLETO_ES.pdf",
        "SecPlus_SY0-701_ESPANOL.pdf",
        "SecPlus_SY0-701_COMPLETO.pdf",
        "SecPlus_SY0-701_Preguntas_Completas.pdf",
        "Guia_Completa_5_Dominios.pdf",
        "Mapa_Conceptos_SY0701.pdf",
        "Leyenda_Colores_Security+.pdf",
        "Security+_Mapa_Relacional.pdf"
    ],
    "03_JSON_Datos": [
        "secplus_estructurado.json",
        "secplus_fusionado_completo.json",
        "secplus_questions.json",
        "secplus_questions_ES.json",
        "corrections.json",
        "prioridades.json",
        "flashcards.json",
        "preguntas_nuevas.json",
        "broken_questions.json"
    ],
    "04_Scripts_Python": [
        "generar_fusionado.py",
        "generar_pdf_condensado.py",
        "crear_json_estructurado.py",
        "extraer_json_bloques.py",
        "dividir_pdf.py",
        "analizar_json.py",
        "identificar_preguntas_prioritarias.py",
        "ampliar_preguntas.py",
        "organizar_carpeta.py"
    ],
    "05_Bloques_PDF": [
        "bloques_pdf"
    ],
    "06_Otros": [
        "RESUMEN_ESTRATEGIA_COMPLETA.md",
        "Roadmap_Ciberseguridad_Ruben.docx",
        "nul"
    ]
}

def crear_estructura():
    """Crea las carpetas de la estructura"""
    print("\n[1/3] Creando estructura de carpetas...")

    for carpeta in ESTRUCTURA.keys():
        ruta = BASE / carpeta
        ruta.mkdir(exist_ok=True)
        print(f"  ✓ {carpeta}")

def mover_archivos():
    """Mueve los archivos a sus carpetas correspondientes"""
    print("\n[2/3] Organizando archivos...")

    movidos = 0
    no_encontrados = []

    for carpeta, archivos in ESTRUCTURA.items():
        destino = BASE / carpeta

        for archivo in archivos:
            origen = BASE / archivo

            if origen.exists():
                dest_final = destino / archivo

                # Si es directorio
                if origen.is_dir():
                    if dest_final.exists():
                        shutil.rmtree(dest_final)
                    shutil.move(str(origen), str(dest_final))
                    print(f"  ✓ {archivo} → {carpeta}/")
                    movidos += 1
                # Si es archivo
                else:
                    shutil.move(str(origen), str(dest_final))
                    print(f"  ✓ {archivo} → {carpeta}/")
                    movidos += 1
            else:
                no_encontrados.append(archivo)

    if no_encontrados:
        print(f"\n  ⚠ Archivos no encontrados: {len(no_encontrados)}")
        for arch in no_encontrados[:5]:
            print(f"    - {arch}")

    print(f"\n  Total archivos movidos: {movidos}")

def crear_readme():
    """Crea un README con la estructura"""
    print("\n[3/3] Creando README...")

    readme = """# CompTIA Security+ SY0-701 - Estructura de Archivos

## 📁 Estructura de Carpetas

### 01_PDFs_Finales ⭐
**Los archivos que necesitas para estudiar**
- `SecPlus_SY0-701_CONDENSADO.pdf` - **PDF condensado** (32 KB, 13 páginas)
  - Solo contenido ALTA y MEDIA prioridad
  - 144 conceptos clave + 144 puntos teoría
  - Perfecto para repaso rápido

- `SecPlus_SY0-701_FUSIONADO.pdf` - PDF completo fusionado (530 KB)
  - 590 preguntas + teoría completa
  - Para estudio profundo

- `GUIA_PREGUNTAS_PRIORITARIAS.txt` - Guía de qué preguntas marcar
  - 24 preguntas ALTA (marcar ROJO)
  - 126 preguntas MEDIA (marcar NARANJA)

### 02_PDFs_Referencia
PDFs de referencia y consulta

### 03_JSON_Datos
Archivos JSON con datos estructurados:
- `secplus_estructurado.json` - Datos organizados sin redundancias
- `secplus_fusionado_completo.json` - PDF completo en JSON
- Preguntas, correcciones, prioridades, flashcards

### 04_Scripts_Python
Scripts de generación y análisis

### 05_Bloques_PDF
21 bloques de 10 páginas del PDF original

### 06_Otros
Documentos varios y roadmaps

## 🎯 Plan de Estudio Recomendado

### Opción A: Rápido (2-3 semanas)
1. Estudiar `01_PDFs_Finales/SecPlus_SY0-701_CONDENSADO.pdf`
2. Usar `GUIA_PREGUNTAS_PRIORITARIAS.txt` para practicar
3. Repasar conceptos fallados

### Opción B: Completo (4-6 semanas)
1. Estudiar `SecPlus_SY0-701_FUSIONADO.pdf` completo
2. Practicar las 590 preguntas
3. Repasar con el condensado antes del examen

## 📊 Estadísticas

- **PDF Original:** 209 páginas, 530 KB
- **PDF Condensado:** 13 páginas, 32 KB (94% reducción)
- **Preguntas totales:** 590
- **Preguntas prioritarias:** 150 (20.7%)
- **Conceptos ALTA:** 50
- **Conceptos MEDIA:** 94

---
Generado automáticamente
"""

    readme_path = BASE / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme)

    print(f"  ✓ README.md creado")

def main():
    print("="*80)
    print(" ORGANIZADOR DE CARPETA Sec+")
    print("="*80)

    crear_estructura()
    mover_archivos()
    crear_readme()

    print("\n" + "="*80)
    print(" ✅ CARPETA ORGANIZADA EXITOSAMENTE")
    print("="*80)
    print(f"\nEstructura creada en: {BASE}")
    print("\nCarpetas principales:")
    print("  📁 01_PDFs_Finales      ← EMPIEZA AQUÍ")
    print("  📁 02_PDFs_Referencia")
    print("  📁 03_JSON_Datos")
    print("  📁 04_Scripts_Python")
    print("  📁 05_Bloques_PDF")
    print("  📁 06_Otros")
    print("\nAbre README.md para más información")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
