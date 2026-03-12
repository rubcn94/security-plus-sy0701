#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera un PDF condensado del Security+ SY0-701
Solo incluye contenido de prioridad ALTA y MEDIA
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import json
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

JSON_PATH = Path(r"D:\Users\cra\Desktop\Sec+\03_JSON_Datos\secplus_estructurado.json")
OUTPUT_PDF = Path(r"D:\Users\cra\Desktop\Sec+\01_PDFs_Finales\SecPlus_SY0-701_CONDENSADO.pdf")

# Colores
C_BLUE_DARK = colors.HexColor('#1a2744')
C_BLUE_MED = colors.HexColor('#2d5aa0')
C_RED = colors.HexColor('#e74c3c')
C_ORANGE = colors.HexColor('#f39c12')
C_GREEN = colors.HexColor('#27ae60')
C_GREY_BG = colors.HexColor('#f5f5f5')
C_GREY_LINE = colors.HexColor('#cccccc')
C_RED_BG = colors.HexColor('#fef2f2')
C_ORANGE_BG = colors.HexColor('#fffbf0')
C_WHITE = colors.white

def cargar_json():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def esc(t):
    """Escapa caracteres especiales para XML"""
    if not t: return ''
    return str(t).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def crear_estilos():
    """Crea los estilos para el PDF"""
    styles = getSampleStyleSheet()

    def sty(name, **kw):
        base = styles[name]
        return ParagraphStyle(name + '_custom', parent=base, **kw)

    return {
        'titulo': sty('Heading1', fontName='Helvetica-Bold', fontSize=24,
                      textColor=C_WHITE, alignment=TA_CENTER, spaceAfter=6),
        'subtitulo': sty('Heading2', fontName='Helvetica-Bold', fontSize=16,
                        textColor=C_WHITE, alignment=TA_CENTER, spaceAfter=4),
        'dominio': sty('Heading2', fontName='Helvetica-Bold', fontSize=18,
                      textColor=C_WHITE, spaceAfter=4, spaceBefore=0),
        'objetivo': sty('Heading3', fontName='Helvetica-Bold', fontSize=12,
                       textColor=C_WHITE, spaceAfter=3, spaceBefore=0),
        'seccion': sty('Heading4', fontName='Helvetica-Bold', fontSize=10,
                      textColor=C_BLUE_DARK, spaceAfter=3, spaceBefore=6),
        'alta': sty('Normal', fontName='Helvetica-Bold', fontSize=9,
                   textColor=C_RED, spaceAfter=2, leading=13, leftIndent=8),
        'media': sty('Normal', fontName='Helvetica', fontSize=9,
                    textColor=colors.HexColor('#b7770d'), spaceAfter=2, leading=13, leftIndent=8),
        'punto_clave': sty('Normal', fontName='Helvetica', fontSize=9,
                          textColor=colors.HexColor('#333'), spaceAfter=2, leading=12, leftIndent=10),
        'normal': sty('Normal', fontName='Helvetica', fontSize=9,
                     textColor=colors.black, spaceAfter=3, leading=12),
        'footer': sty('Normal', fontName='Helvetica', fontSize=7,
                     textColor=colors.HexColor('#888'), alignment=TA_CENTER)
    }

def crear_portada(story, styles, datos):
    """Crea la portada del PDF"""
    story.append(Spacer(1, 3*cm))

    # Titulo principal
    t_titulo = Table([[Paragraph('CompTIA Security+ SY0-701', styles['titulo'])]],
                     colWidths=[17*cm])
    t_titulo.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BLUE_DARK),
        ('TOPPADDING', (0,0), (-1,-1), 20),
        ('BOTTOMPADDING', (0,0), (-1,-1), 20)
    ]))
    story.append(t_titulo)
    story.append(Spacer(1, 0.3*cm))

    # Subtitulo
    t_sub = Table([[Paragraph('Guía CONDENSADA · Prioridad ALTA y MEDIA', styles['subtitulo'])]],
                  colWidths=[17*cm])
    t_sub.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BLUE_MED),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12)
    ]))
    story.append(t_sub)
    story.append(Spacer(1, 1*cm))

    # Estadisticas
    total_alta = sum(len(d['prioridades']['alta']) for d in datos['dominios'].values())
    total_media = sum(len(d['prioridades']['media']) for d in datos['dominios'].values())
    total_puntos = sum(
        len(obj['teoria_messer']['puntos_clave'])
        for dom in datos['dominios'].values()
        for obj in dom['objetivos'].values()
    )

    info = [
        ['Contenido:', 'Solo conceptos de ALTA y MEDIA prioridad'],
        ['Items ALTA:', f'{total_alta} conceptos críticos para el examen'],
        ['Items MEDIA:', f'{total_media} conceptos importantes'],
        ['Puntos clave Messer:', f'{total_puntos} puntos de teoría esencial'],
        ['Estructura:', '5 Dominios → 28 Objetivos → Conceptos prioritarios']
    ]

    t_info = Table(info, colWidths=[4*cm, 13*cm])
    t_info.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TEXTCOLOR', (0,0), (0,-1), C_BLUE_DARK),
        ('BACKGROUND', (0,0), (-1,-1), C_GREY_BG),
        ('GRID', (0,0), (-1,-1), 0.3, C_GREY_LINE),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8)
    ]))
    story.append(t_info)
    story.append(Spacer(1, 0.8*cm))

    # Leyenda
    leyenda = Table([[
        Paragraph('<b><font color="#e74c3c">ALTA</font></b> = Sale frecuentemente en tests', styles['normal']),
        Paragraph('<b><font color="#f39c12">MEDIA</font></b> = Importante conocer', styles['normal'])
    ]], colWidths=[8.5*cm, 8.5*cm])
    leyenda.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fffef0')),
        ('BOX', (0,0), (-1,-1), 1.5, C_ORANGE),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8)
    ]))
    story.append(leyenda)

    story.append(PageBreak())

def crear_caja_dominio(num, nombre, porcentaje, styles):
    """Crea la caja de cabecera de dominio"""
    t = Table([[Paragraph(
        f'<b>DOMINIO {num}</b>  ·  {esc(nombre)}  ({porcentaje}% del examen)',
        styles['dominio']
    )]], colWidths=[17*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BLUE_DARK),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 12)
    ]))
    return t

def crear_caja_objetivo(obj_id, titulo, styles):
    """Crea la caja de cabecera de objetivo"""
    t = Table([[Paragraph(
        f'<b>{esc(obj_id)}</b>  {esc(titulo)}',
        styles['objetivo']
    )]], colWidths=[17*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BLUE_MED),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10)
    ]))
    return t

def generar_leyenda_abreviaciones(story, styles):
    """Genera la sección de leyenda de abreviaciones al final del PDF"""
    import json
    from pathlib import Path

    # Cargar abreviaciones
    abbr_path = Path(r"D:\Users\cra\Desktop\Sec+\03_JSON_Datos\abreviaciones.json")
    with open(abbr_path, 'r', encoding='utf-8') as f:
        abreviaciones = json.load(f)

    # Nueva página para la leyenda
    story.append(PageBreak())

    # Título de la sección
    t_titulo = Table([[Paragraph('LEYENDA DE ABREVIACIONES', styles['dominio'])]],
                     colWidths=[17*cm])
    t_titulo.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BLUE_DARK),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 12)
    ]))
    story.append(t_titulo)
    story.append(Spacer(1, 0.4*cm))

    # Crear tabla de abreviaciones en 2 columnas
    datos_tabla = []
    items = list(abreviaciones.items())

    # Dividir en 2 columnas
    mid = len(items) // 2 + len(items) % 2
    col1 = items[:mid]
    col2 = items[mid:]

    for i in range(max(len(col1), len(col2))):
        row = []

        # Columna 1
        if i < len(col1):
            abbr1, full1 = col1[i]
            cell1 = Paragraph(f'<b>{esc(abbr1)}</b>: {esc(full1)}', styles['punto_clave'])
        else:
            cell1 = Paragraph('', styles['punto_clave'])

        # Columna 2
        if i < len(col2):
            abbr2, full2 = col2[i]
            cell2 = Paragraph(f'<b>{esc(abbr2)}</b>: {esc(full2)}', styles['punto_clave'])
        else:
            cell2 = Paragraph('', styles['punto_clave'])

        row.append(cell1)
        row.append(cell2)
        datos_tabla.append(row)

    t_abbr = Table(datos_tabla, colWidths=[8.5*cm, 8.5*cm])
    t_abbr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_GREY_BG),
        ('GRID', (0,0), (-1,-1), 0.3, C_GREY_LINE),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP')
    ]))
    story.append(t_abbr)

    print(f"  [Leyenda] {len(abreviaciones)} abreviaciones añadidas")

def generar_contenido(story, styles, datos):
    """Genera el contenido principal del PDF"""
    print("\nGenerando contenido del PDF condensado...")

    for dom_num_str in sorted(datos['dominios'].keys(), key=lambda x: int(x)):
        dominio = datos['dominios'][dom_num_str]
        dom_num = dominio['numero']

        print(f"\n  [Dominio {dom_num}] {dominio['nombre']}")

        # Cabecera de dominio
        story.append(PageBreak())
        story.append(crear_caja_dominio(dom_num, dominio['nombre'], dominio['porcentaje_examen'], styles))
        story.append(Spacer(1, 0.4*cm))

        # Prioridades del dominio
        alta = dominio['prioridades']['alta']
        media = dominio['prioridades']['media']

        if alta or media:
            story.append(Paragraph('Conceptos Clave por Prioridad', styles['seccion']))
            story.append(Spacer(1, 0.2*cm))

            # Tabla de prioridades
            datos_tabla = []

            # Cabecera
            datos_tabla.append([
                Paragraph('<b>ALTA PRIORIDAD</b>', styles['normal']),
                Paragraph('<b>MEDIA PRIORIDAD</b>', styles['normal'])
            ])

            # Contenido
            max_len = max(len(alta), len(media))
            for i in range(max_len):
                item_alta = f'• {esc(alta[i])}' if i < len(alta) else ''
                item_media = f'• {esc(media[i])}' if i < len(media) else ''

                datos_tabla.append([
                    Paragraph(item_alta, styles['alta']) if item_alta else Paragraph('', styles['alta']),
                    Paragraph(item_media, styles['media']) if item_media else Paragraph('', styles['media'])
                ])

            t_prio = Table(datos_tabla, colWidths=[8.5*cm, 8.5*cm])
            t_prio.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (0,0), C_RED_BG),
                ('BACKGROUND', (1,0), (1,0), C_ORANGE_BG),
                ('BACKGROUND', (0,1), (0,-1), colors.HexColor('#fffafa')),
                ('BACKGROUND', (1,1), (1,-1), colors.HexColor('#fffef9')),
                ('GRID', (0,0), (-1,-1), 0.3, C_GREY_LINE),
                ('TOPPADDING', (0,0), (-1,-1), 4),
                ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                ('LEFTPADDING', (0,0), (-1,-1), 6),
                ('VALIGN', (0,0), (-1,-1), 'TOP')
            ]))
            story.append(t_prio)
            story.append(Spacer(1, 0.5*cm))

            print(f"    Prioridades: {len(alta)} ALTA, {len(media)} MEDIA")

        # Objetivos del dominio
        for obj_id in sorted(dominio['objetivos'].keys()):
            objetivo = dominio['objetivos'][obj_id]

            print(f"    [{obj_id}] {objetivo['titulo']}")

            story.append(Spacer(1, 0.3*cm))
            story.append(crear_caja_objetivo(obj_id, objetivo['titulo'], styles))
            story.append(Spacer(1, 0.2*cm))

            # Teoria Messer - Puntos clave
            puntos_clave = objetivo['teoria_messer']['puntos_clave']
            if puntos_clave:
                story.append(Paragraph('Puntos Clave — Professor Messer', styles['seccion']))
                for punto in puntos_clave:
                    story.append(Paragraph(f'■ {esc(punto)}', styles['punto_clave']))

                print(f"        {len(puntos_clave)} puntos clave")
                story.append(Spacer(1, 0.3*cm))

    print("\n  [Contenido generado completamente]")

def generar_pdf():
    """Funcion principal de generacion"""
    print("="*70)
    print(" GENERADOR DE PDF CONDENSADO - Security+ SY0-701")
    print("="*70)

    # Cargar datos
    print("\nCargando JSON estructurado...")
    datos = cargar_json()

    # Crear PDF
    print(f"Creando PDF: {OUTPUT_PDF}")
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm,
        title='CompTIA Security+ SY0-701 - Guia Condensada',
        author='Security+ Study Guide'
    )

    # Estilos
    styles = crear_estilos()

    # Contenido
    story = []

    # Portada
    crear_portada(story, styles, datos)

    # Contenido principal
    generar_contenido(story, styles, datos)

    # Leyenda de abreviaciones
    generar_leyenda_abreviaciones(story, styles)

    # Pie de pagina
    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 7)
        canvas.setFillColor(colors.HexColor('#888'))
        canvas.drawString(2*cm, 1.2*cm, f'CompTIA Security+ SY0-701 CONDENSADO | Pag {doc.page}')
        canvas.drawRightString(19*cm, 1.2*cm, 'ALTA + MEDIA Prioridad')
        canvas.restoreState()

    # Construir PDF
    print("\nConstruyendo PDF final...")
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)

    # Estadisticas
    size_mb = OUTPUT_PDF.stat().st_size / 1024 / 1024

    print("\n" + "="*70)
    print(" PDF CONDENSADO GENERADO EXITOSAMENTE")
    print("="*70)
    print(f"Archivo: {OUTPUT_PDF}")
    print(f"Tamaño: {size_mb:.2f} MB")

    total_alta = sum(len(d['prioridades']['alta']) for d in datos['dominios'].values())
    total_media = sum(len(d['prioridades']['media']) for d in datos['dominios'].values())
    total_puntos = sum(
        len(obj['teoria_messer']['puntos_clave'])
        for dom in datos['dominios'].values()
        for obj in dom['objetivos'].values()
    )

    # Contar abreviaciones
    import json
    abbr_path = Path(r"D:\Users\cra\Desktop\Sec+\03_JSON_Datos\abreviaciones.json")
    with open(abbr_path, 'r', encoding='utf-8') as f:
        abreviaciones = json.load(f)

    print(f"\nContenido incluido:")
    print(f"  • {total_alta} conceptos de ALTA prioridad")
    print(f"  • {total_media} conceptos de MEDIA prioridad")
    print(f"  • {total_puntos} puntos clave de teoria Messer")
    print(f"  • {len(abreviaciones)} abreviaciones en leyenda")
    print(f"  • 5 dominios completos")
    print(f"  • 28 objetivos organizados")
    print("="*70 + "\n")

if __name__ == "__main__":
    generar_pdf()
