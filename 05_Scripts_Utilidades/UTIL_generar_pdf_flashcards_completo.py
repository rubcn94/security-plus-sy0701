#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar PDF con TODAS las flashcards (382 = 220 ALTA + 162 MEDIA)
"""

import json
from pathlib import Path

# Rutas
BASE_DIR = Path(r"D:\Users\cra\Desktop\Sec+")
PROFUNDIZACION_JSON = BASE_DIR / "02_Diccionarios_Referencia" / "JSON" / "SecPlus_SY0-701_Material_Profundizacion_COMPLETO.json"
MATERIAL_ESTUDIO = BASE_DIR / "01_Material_Estudio"

def generar_pdf_flashcards_completo():
    """Genera PDF con TODAS las flashcards (382 términos ALTA + MEDIA)"""
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
        from reportlab.lib.units import inch
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
        from reportlab.lib import colors
    except ImportError:
        print("ERROR: reportlab no instalado.")
        print("Instala con: pip install reportlab")
        return None

    # Cargar flashcards
    with open(PROFUNDIZACION_JSON, 'r', encoding='utf-8') as f:
        material = json.load(f)

    flashcards = material.get("flashcards", [])
    flashcards_alta = [fc for fc in flashcards if fc.get("prioridad") == "ALTA"]
    flashcards_media = [fc for fc in flashcards if fc.get("prioridad") == "MEDIA"]

    print(f"Total flashcards: {len(flashcards)}")
    print(f"  - ALTA: {len(flashcards_alta)}")
    print(f"  - MEDIA: {len(flashcards_media)}")

    output_path = MATERIAL_ESTUDIO / "PDFs_Estudio" / "SecPlus_Flashcards_COMPLETO_382.pdf"

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

    # Estilos personalizados
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=26,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    subtitle_style = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontSize=14,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#764ba2')
    )

    term_alta_style = ParagraphStyle(
        'TermAltaStyle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#ff6b6b'),
        spaceAfter=8,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold'
    )

    term_media_style = ParagraphStyle(
        'TermMediaStyle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#ffa500'),
        spaceAfter=8,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold'
    )

    def_style = ParagraphStyle(
        'DefStyle',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=10,
        alignment=TA_LEFT,
        leading=14
    )

    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.grey,
        spaceAfter=8
    )

    # === PORTADA ===
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("Security+ SY0-701", title_style))
    story.append(Paragraph("Flashcards Completo", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("382 Términos Esenciales", subtitle_style))
    story.append(Paragraph("220 ALTA + 162 MEDIA", subtitle_style))
    story.append(Spacer(1, 0.5*inch))

    # Tabla de contenido
    toc_data = [
        ["Prioridad", "Cantidad", "Descripción"],
        ["ALTA", "220", "Términos críticos para el examen (50.5%)"],
        ["MEDIA", "162", "Términos complementarios importantes (37.2%)"],
        ["TOTAL", "382", "Cobertura del 88% del diccionario completo"]
    ]

    toc_table = Table(toc_data, colWidths=[1.5*inch, 1.5*inch, 3*inch])
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
    ]))

    story.append(toc_table)
    story.append(PageBreak())

    # === FLASHCARDS ALTA ===
    story.append(Paragraph("PARTE 1: TÉRMINOS ALTA PRIORIDAD (220)", title_style))
    story.append(Paragraph("Conceptos críticos que DEBES dominar para 85%+", subtitle_style))
    story.append(PageBreak())

    for i, fc in enumerate(flashcards_alta, 1):
        # Header
        header = f"[{i}/220] - {fc.get('dominio', '')} - ALTA PRIORIDAD"
        story.append(Paragraph(header, header_style))
        story.append(Spacer(1, 0.05*inch))

        # Término
        story.append(Paragraph(fc.get('termino', ''), term_alta_style))

        # Definición
        story.append(Paragraph(fc.get('definicion', ''), def_style))

        # Ejemplos
        ejemplos = fc.get('ejemplos', [])
        if ejemplos:
            story.append(Paragraph("<b>Ejemplos:</b>", styles['Normal']))
            for ej in ejemplos:
                # Escapar caracteres especiales
                ej_safe = ej.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                story.append(Paragraph(f"• {ej_safe}", styles['Normal']))

        story.append(Spacer(1, 0.25*inch))

        # Line separator
        story.append(Paragraph("<hr width='100%'/>", styles['Normal']))
        story.append(Spacer(1, 0.15*inch))

        # Page break cada 3 flashcards
        if i % 3 == 0 and i < len(flashcards_alta):
            story.append(PageBreak())

    # === FLASHCARDS MEDIA ===
    story.append(PageBreak())
    story.append(Paragraph("PARTE 2: TÉRMINOS MEDIA PRIORIDAD (162)", title_style))
    story.append(Paragraph("Conceptos complementarios importantes", subtitle_style))
    story.append(PageBreak())

    for i, fc in enumerate(flashcards_media, 1):
        # Header
        header = f"[{i}/162] - {fc.get('dominio', '')} - MEDIA PRIORIDAD"
        story.append(Paragraph(header, header_style))
        story.append(Spacer(1, 0.05*inch))

        # Término
        story.append(Paragraph(fc.get('termino', ''), term_media_style))

        # Definición
        story.append(Paragraph(fc.get('definicion', ''), def_style))

        # Ejemplos
        ejemplos = fc.get('ejemplos', [])
        if ejemplos:
            story.append(Paragraph("<b>Ejemplos:</b>", styles['Normal']))
            for ej in ejemplos:
                # Escapar caracteres especiales
                ej_safe = ej.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                story.append(Paragraph(f"• {ej_safe}", styles['Normal']))

        story.append(Spacer(1, 0.25*inch))

        # Line separator
        story.append(Paragraph("<hr width='100%'/>", styles['Normal']))
        story.append(Spacer(1, 0.15*inch))

        # Page break cada 3 flashcards
        if i % 3 == 0 and i < len(flashcards_media):
            story.append(PageBreak())

    # Construir PDF
    doc.build(story)
    print(f"\nPDF flashcards completo guardado: {output_path}")
    return output_path

def main():
    print("=" * 70)
    print("GENERANDO PDF FLASHCARDS COMPLETO (382 TERMINOS)")
    print("=" * 70)
    print()

    pdf_path = generar_pdf_flashcards_completo()

    if pdf_path:
        print()
        print("=" * 70)
        print("PDF GENERADO EXITOSAMENTE")
        print("=" * 70)
        print()
        print(f"Archivo: {pdf_path.name}")
        print(f"Ubicacion: {pdf_path.parent}")
        print()
        print("Contenido:")
        print("  - Portada con resumen")
        print("  - 220 flashcards ALTA (prioridad maxima)")
        print("  - 162 flashcards MEDIA (complementarias)")
        print("  - Total: 382 flashcards")
        print()
        print("El PDF esta organizado en 2 secciones claramente diferenciadas:")
        print("  1. ALTA: terminos criticos (rojo)")
        print("  2. MEDIA: terminos complementarios (naranja)")
        print()

if __name__ == "__main__":
    main()
