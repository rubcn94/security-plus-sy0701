#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para ampliar flashcards añadiendo términos MEDIA (162 términos)
Genera:
1. JSON actualizado con flashcards ALTA + MEDIA (382 total)
2. HTML flashcards con 382 términos
3. Anki CSV con 382 términos
4. PDF separado con solo flashcards MEDIA
"""

import json
import os
from pathlib import Path

# Rutas
BASE_DIR = Path(r"D:\Users\cra\Desktop\Sec+")
DICCIONARIO_COMPLETO = BASE_DIR / "02_Diccionarios_Referencia" / "JSON" / "SecPlus_SY0-701_Diccionario_Completo.json"
PROFUNDIZACION_JSON = BASE_DIR / "02_Diccionarios_Referencia" / "JSON" / "SecPlus_SY0-701_Material_Profundizacion_COMPLETO.json"
MATERIAL_ESTUDIO = BASE_DIR / "01_Material_Estudio"

def extraer_terminos_media(diccionario_completo):
    """Extrae todos los términos MEDIA del diccionario completo"""
    with open(diccionario_completo, 'r', encoding='utf-8') as f:
        data = json.load(f)

    terminos_media = []

    # Recorrer cada dominio
    for dominio_key, dominio_data in data.items():
        if dominio_key == "metadata":
            continue

        dominio_num = dominio_key.split("_")[1]  # Extraer número de dominio
        definiciones = dominio_data.get("definiciones", {})

        for termino_key, termino_data in definiciones.items():
            if termino_data.get("prioridad") == "MEDIA":
                flashcard = {
                    "termino": termino_data.get("termino", termino_key),
                    "definicion": termino_data.get("definicion", ""),
                    "ejemplos": termino_data.get("ejemplos", []),
                    "prioridad": "MEDIA",
                    "dominio": f"D{dominio_num}"
                }
                terminos_media.append(flashcard)

    print(f"Extraidos {len(terminos_media)} terminos MEDIA")
    return terminos_media

def actualizar_json_profundizacion(flashcards_media):
    """Actualiza JSON de profundización añadiendo flashcards MEDIA"""
    with open(PROFUNDIZACION_JSON, 'r', encoding='utf-8') as f:
        material = json.load(f)

    flashcards_alta = material.get("flashcards", [])
    print(f"Flashcards ALTA actuales: {len(flashcards_alta)}")

    # Añadir flashcards MEDIA
    material["flashcards"] = flashcards_alta + flashcards_media

    # Actualizar metadata
    material["metadata"]["flashcards_total"] = len(material["flashcards"])
    material["metadata"]["flashcards_alta"] = len(flashcards_alta)
    material["metadata"]["flashcards_media"] = len(flashcards_media)
    material["metadata"]["fecha_actualizacion"] = "2026-03-03"

    # Guardar
    with open(PROFUNDIZACION_JSON, 'w', encoding='utf-8') as f:
        json.dump(material, f, ensure_ascii=False, indent=2)

    print(f"JSON actualizado: {len(material['flashcards'])} flashcards totales")
    return material

def generar_html_flashcards_completo(material):
    """Genera HTML con todas las flashcards (ALTA + MEDIA)"""
    flashcards = material.get("flashcards", [])

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flashcards Security+ SY0-701 (382 terminos ALTA+MEDIA)</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}

        .container {{
            max-width: 800px;
            width: 100%;
        }}

        .header {{
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }}

        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}

        .stats {{
            display: flex;
            justify-content: center;
            gap: 20px;
            color: white;
            font-size: 1.1em;
        }}

        .card-container {{
            perspective: 1000px;
            margin-bottom: 30px;
        }}

        .flashcard {{
            width: 100%;
            min-height: 400px;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.6s;
            cursor: pointer;
        }}

        .flashcard.flipped {{
            transform: rotateY(180deg);
        }}

        .card-face {{
            position: absolute;
            width: 100%;
            min-height: 400px;
            backface-visibility: hidden;
            border-radius: 15px;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}

        .card-front {{
            background: white;
        }}

        .card-back {{
            background: #f8f9fa;
            transform: rotateY(180deg);
        }}

        .termino {{
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 20px;
            text-align: center;
        }}

        .prioridad-badge {{
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
            margin-bottom: 15px;
        }}

        .prioridad-ALTA {{
            background: #ff6b6b;
            color: white;
        }}

        .prioridad-MEDIA {{
            background: #ffa500;
            color: white;
        }}

        .dominio {{
            color: #6c757d;
            font-size: 1.2em;
            margin-bottom: 20px;
        }}

        .definicion {{
            font-size: 1.2em;
            line-height: 1.6;
            color: #333;
            text-align: center;
            margin-bottom: 20px;
        }}

        .ejemplos {{
            width: 100%;
            text-align: left;
            margin-top: 20px;
        }}

        .ejemplos h4 {{
            color: #667eea;
            margin-bottom: 10px;
        }}

        .ejemplos ul {{
            list-style-position: inside;
            color: #555;
        }}

        .ejemplos li {{
            margin-bottom: 8px;
            line-height: 1.4;
        }}

        .controls {{
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 20px;
        }}

        button {{
            padding: 12px 30px;
            font-size: 1.1em;
            border: none;
            border-radius: 25px;
            background: white;
            color: #667eea;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        }}

        .progress {{
            background: white;
            border-radius: 15px;
            padding: 15px;
            text-align: center;
            color: #333;
        }}

        .progress-bar {{
            width: 100%;
            height: 20px;
            background: #e9ecef;
            border-radius: 10px;
            overflow: hidden;
            margin-top: 10px;
        }}

        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            transition: width 0.3s;
        }}

        .hint {{
            color: white;
            text-align: center;
            margin-top: 20px;
            font-size: 0.9em;
            opacity: 0.8;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Security+ SY0-701</h1>
            <div class="stats">
                <span id="total-cards">382 flashcards</span>
                <span>|</span>
                <span>220 ALTA + 162 MEDIA</span>
            </div>
        </div>

        <div class="card-container">
            <div class="flashcard" id="flashcard" onclick="flipCard()">
                <div class="card-face card-front">
                    <span class="prioridad-badge" id="prioridad-front"></span>
                    <div class="dominio" id="dominio-front"></div>
                    <div class="termino" id="termino"></div>
                    <p style="color: #6c757d; margin-top: 20px;">Click para ver definicion</p>
                </div>
                <div class="card-face card-back">
                    <span class="prioridad-badge" id="prioridad-back"></span>
                    <div class="dominio" id="dominio-back"></div>
                    <div class="definicion" id="definicion"></div>
                    <div class="ejemplos" id="ejemplos-container"></div>
                </div>
            </div>
        </div>

        <div class="controls">
            <button onclick="previousCard()">Anterior</button>
            <button onclick="randomCard()">Aleatorio</button>
            <button onclick="nextCard()">Siguiente</button>
        </div>

        <div class="progress">
            <strong>Progreso:</strong> <span id="current">1</span> / <span id="total">{len(flashcards)}</span>
            <div class="progress-bar">
                <div class="progress-fill" id="progress-fill"></div>
            </div>
        </div>

        <div class="hint">
            Usa flechas izquierda/derecha para navegar | Espacio para voltear | R para aleatorio
        </div>
    </div>

    <script>
        const flashcards = {json.dumps(flashcards, ensure_ascii=False)};
        let currentIndex = 0;
        let isFlipped = false;

        function loadCard(index) {{
            const card = flashcards[index];
            const flashcardEl = document.getElementById('flashcard');

            // Reset flip
            if (isFlipped) {{
                flashcardEl.classList.remove('flipped');
                isFlipped = false;
            }}

            // Front
            document.getElementById('prioridad-front').textContent = card.prioridad;
            document.getElementById('prioridad-front').className = 'prioridad-badge prioridad-' + card.prioridad;
            document.getElementById('dominio-front').textContent = card.dominio;
            document.getElementById('termino').textContent = card.termino;

            // Back
            document.getElementById('prioridad-back').textContent = card.prioridad;
            document.getElementById('prioridad-back').className = 'prioridad-badge prioridad-' + card.prioridad;
            document.getElementById('dominio-back').textContent = card.dominio;
            document.getElementById('definicion').textContent = card.definicion;

            // Ejemplos
            const ejemplosContainer = document.getElementById('ejemplos-container');
            if (card.ejemplos && card.ejemplos.length > 0) {{
                ejemplosContainer.innerHTML = '<h4>Ejemplos:</h4><ul>' +
                    card.ejemplos.map(ej => '<li>' + ej + '</li>').join('') +
                    '</ul>';
                ejemplosContainer.style.display = 'block';
            }} else {{
                ejemplosContainer.style.display = 'none';
            }}

            // Progress
            document.getElementById('current').textContent = index + 1;
            document.getElementById('progress-fill').style.width = ((index + 1) / flashcards.length * 100) + '%';
        }}

        function flipCard() {{
            const flashcardEl = document.getElementById('flashcard');
            flashcardEl.classList.toggle('flipped');
            isFlipped = !isFlipped;
        }}

        function nextCard() {{
            currentIndex = (currentIndex + 1) % flashcards.length;
            loadCard(currentIndex);
        }}

        function previousCard() {{
            currentIndex = (currentIndex - 1 + flashcards.length) % flashcards.length;
            loadCard(currentIndex);
        }}

        function randomCard() {{
            currentIndex = Math.floor(Math.random() * flashcards.length);
            loadCard(currentIndex);
        }}

        // Keyboard navigation
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'ArrowRight') nextCard();
            else if (e.key === 'ArrowLeft') previousCard();
            else if (e.key === ' ') {{ e.preventDefault(); flipCard(); }}
            else if (e.key === 'r' || e.key === 'R') randomCard();
        }});

        // Load first card
        loadCard(0);
    </script>
</body>
</html>"""

    # Guardar HTML
    output_path = MATERIAL_ESTUDIO / "Flashcards" / "SecPlus_Flashcards_Interactivo.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"HTML flashcards guardado: {output_path}")
    print(f"Total flashcards en HTML: {len(flashcards)}")
    return output_path

def generar_anki_csv(material):
    """Genera CSV para Anki con todas las flashcards"""
    flashcards = material.get("flashcards", [])

    csv_lines = ["Termino;Definicion;Ejemplos;Prioridad;Dominio"]

    for fc in flashcards:
        termino = fc.get("termino", "").replace(";", ",")
        definicion = fc.get("definicion", "").replace(";", ",")
        ejemplos = " | ".join(fc.get("ejemplos", [])).replace(";", ",")
        prioridad = fc.get("prioridad", "")
        dominio = fc.get("dominio", "")

        csv_lines.append(f"{termino};{definicion};{ejemplos};{prioridad};{dominio}")

    output_path = MATERIAL_ESTUDIO / "Flashcards" / "SecPlus_Flashcards_Anki.csv"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(csv_lines))

    print(f"CSV Anki guardado: {output_path}")
    print(f"Total flashcards en CSV: {len(flashcards)}")
    return output_path

def generar_pdf_flashcards_media(flashcards_media):
    """Genera PDF con solo las flashcards MEDIA (162 términos)"""
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
        from reportlab.lib.units import inch
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
    except ImportError:
        print("AVISO: reportlab no instalado. Saltando generacion de PDF.")
        print("Instala con: pip install reportlab")
        return None

    output_path = MATERIAL_ESTUDIO / "PDFs_Estudio" / "SecPlus_Flashcards_MEDIA.pdf"

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch,
        leftMargin=0.75*inch,
        rightMargin=0.75*inch
    )

    story = []
    styles = getSampleStyleSheet()

    # Estilo personalizado
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='#667eea',
        spaceAfter=30,
        alignment=TA_CENTER
    )

    term_style = ParagraphStyle(
        'TermStyle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor='#ffa500',
        spaceAfter=10,
        alignment=TA_LEFT
    )

    def_style = ParagraphStyle(
        'DefStyle',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=10,
        alignment=TA_LEFT
    )

    # Portada
    story.append(Paragraph("Security+ SY0-701", title_style))
    story.append(Paragraph("Flashcards Prioridad MEDIA", title_style))
    story.append(Paragraph(f"162 Terminos Complementarios", styles['Normal']))
    story.append(Spacer(1, 0.5*inch))
    story.append(PageBreak())

    # Flashcards
    for i, fc in enumerate(flashcards_media, 1):
        # Encabezado de flashcard
        header = f"{i}/162 - {fc.get('dominio', '')} - MEDIA"
        story.append(Paragraph(header, styles['Normal']))
        story.append(Spacer(1, 0.1*inch))

        # Término
        story.append(Paragraph(fc.get('termino', ''), term_style))

        # Definición
        story.append(Paragraph(fc.get('definicion', ''), def_style))

        # Ejemplos
        ejemplos = fc.get('ejemplos', [])
        if ejemplos:
            story.append(Paragraph("<b>Ejemplos:</b>", styles['Normal']))
            for ej in ejemplos:
                story.append(Paragraph(f"• {ej}", styles['Normal']))

        story.append(Spacer(1, 0.3*inch))

        # Page break cada 3 flashcards
        if i % 3 == 0 and i < len(flashcards_media):
            story.append(PageBreak())

    doc.build(story)
    print(f"PDF flashcards MEDIA guardado: {output_path}")
    print(f"Total flashcards en PDF: {len(flashcards_media)}")
    return output_path

def main():
    print("=" * 70)
    print("AMPLIACION DE FLASHCARDS: AÑADIENDO TERMINOS MEDIA")
    print("=" * 70)
    print()

    # 1. Extraer términos MEDIA
    print("1. Extrayendo terminos MEDIA del diccionario completo...")
    flashcards_media = extraer_terminos_media(DICCIONARIO_COMPLETO)
    print(f"   Extraidos: {len(flashcards_media)} terminos MEDIA")
    print()

    # 2. Actualizar JSON de profundización
    print("2. Actualizando JSON de profundizacion...")
    material = actualizar_json_profundizacion(flashcards_media)
    print(f"   Total flashcards: {len(material['flashcards'])}")
    print(f"   - ALTA: {material['metadata']['flashcards_alta']}")
    print(f"   - MEDIA: {material['metadata']['flashcards_media']}")
    print()

    # 3. Regenerar HTML flashcards
    print("3. Regenerando HTML flashcards (ALTA + MEDIA)...")
    generar_html_flashcards_completo(material)
    print()

    # 4. Regenerar CSV Anki
    print("4. Regenerando CSV Anki (ALTA + MEDIA)...")
    generar_anki_csv(material)
    print()

    # 5. Generar PDF con flashcards MEDIA
    print("5. Generando PDF con flashcards MEDIA...")
    pdf_path = generar_pdf_flashcards_media(flashcards_media)
    print()

    print("=" * 70)
    print("AMPLIACION COMPLETADA")
    print("=" * 70)
    print()
    print("Archivos generados:")
    print("  - JSON: SecPlus_SY0-701_Material_Profundizacion_COMPLETO.json (actualizado)")
    print("  - HTML: SecPlus_Flashcards_Interactivo.html (382 flashcards)")
    print("  - CSV: SecPlus_Flashcards_Anki.csv (382 flashcards)")
    if pdf_path:
        print("  - PDF: SecPlus_Flashcards_MEDIA.pdf (162 flashcards MEDIA)")
    print()
    print("Totales:")
    print("  - 220 flashcards ALTA (prioridad maxima)")
    print("  - 162 flashcards MEDIA (complementarias)")
    print("  - 382 flashcards TOTALES")
    print()

if __name__ == "__main__":
    main()
