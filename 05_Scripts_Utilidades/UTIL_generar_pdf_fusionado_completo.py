#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera SecPlus_SY0-701_FUSIONADO.pdf v2
- Teoria de Messer (57p) organizada por dominio/objetivo
- Mapa de prioridades con colores ALTA/MEDIA/COMPLEMENTARIO reales
- 590 preguntas ExamCompass con respuestas corregidas
- 190 respuestas faltantes completadas manualmente
- 65 preguntas nuevas adicionales por objetivo
"""
import sys, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import pypdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, CondPageBreak,
    Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

BASE = r"D:\Users\cra\Desktop\Sec+"
PATH_MESSER   = BASE + r"\Messer_Conceptos_COMPLETO_ES.pdf"
PATH_SECPLUS  = BASE + r"\SecPlus_SY0-701_ESPANOL.pdf"
PATH_Q_ES     = BASE + r"\secplus_questions_ES.json"
PATH_Q_EN     = BASE + r"\secplus_questions.json"
PATH_CORREC   = BASE + r"\corrections.json"
PATH_NUEVAS   = BASE + r"\preguntas_nuevas.json"
PATH_PRIO     = BASE + r"\prioridades.json"
PATH_FLASH    = BASE + r"\flashcards.json"
PATH_OUT      = BASE + r"\SecPlus_SY0-701_FUSIONADO.pdf"

# ── LOAD ──────────────────────────────────────────────────────────────────────
print("Cargando datos...")
def load_pdf(path):
    with open(path, 'rb') as f:
        r = pypdf.PdfReader(f)
        return [r.pages[i].extract_text() or '' for i in range(len(r.pages))]

messer_pages  = load_pdf(PATH_MESSER)
secplus_pages = load_pdf(PATH_SECPLUS)

with open(PATH_Q_ES, 'r', encoding='utf-8') as f: q_es = json.load(f)
with open(PATH_Q_EN, 'r', encoding='utf-8') as f: q_en = json.load(f)
with open(PATH_CORREC, 'r', encoding='utf-8') as f: corrections_data = json.load(f)
with open(PATH_NUEVAS, 'r', encoding='utf-8') as f: new_questions = json.load(f)
with open(PATH_PRIO, 'r', encoding='utf-8') as f: prio_data = json.load(f)
with open(BASE + r"\flashcards.json", 'r', encoding='utf-8') as f: flashcards_all = json.load(f)

corrections = {int(k): v for k, v in corrections_data['corrections'].items()}
no_opts_notes = {int(k): v for k, v in corrections_data.get('no_options_questions', {}).items()}

print(f"  Messer: {len(messer_pages)}p | SecPlus: {len(secplus_pages)}p")
print(f"  Q ES: {len(q_es)} | Q EN: {len(q_en)} | Correcciones: {len(corrections)}")
print(f"  Preguntas nuevas: {len(new_questions)}")

# ── STYLES ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

C_BLUE_DARK  = colors.HexColor('#1a2744')
C_BLUE_MED   = colors.HexColor('#2d5aa0')
C_BLUE_LIGHT = colors.HexColor('#4a7fd4')
C_ORANGE     = colors.HexColor('#e8751a')
C_RED        = colors.HexColor('#c0392b')
C_RED_PRIO   = colors.HexColor('#e74c3c')
C_GREEN      = colors.HexColor('#27ae60')
C_AMBER      = colors.HexColor('#f39c12')
C_YELLOW_BG  = colors.HexColor('#fff9e6')
C_BLUE_BG    = colors.HexColor('#eef4fb')
C_GREEN_BG   = colors.HexColor('#eafaf1')
C_RED_BG     = colors.HexColor('#fdf2f2')
C_AMBER_BG   = colors.HexColor('#fef9ec')
C_GREY_BG    = colors.HexColor('#f5f5f5')
C_GREY_LINE  = colors.HexColor('#cccccc')
C_WHITE      = colors.white

def sty(name, **kw):
    base = styles[name]
    return ParagraphStyle(name + '_' + str(abs(hash(str(kw)))), parent=base, **kw)

S_H1   = sty('Heading1', fontName='Helvetica-Bold', fontSize=22, textColor=C_WHITE,
              spaceAfter=4, spaceBefore=0, leading=26, alignment=TA_CENTER)
S_H2   = sty('Heading2', fontName='Helvetica-Bold', fontSize=14, textColor=C_WHITE,
              spaceAfter=3, spaceBefore=0, leading=17, alignment=TA_LEFT)
S_H3   = sty('Heading3', fontName='Helvetica-Bold', fontSize=11, textColor=C_BLUE_DARK,
              spaceAfter=4, spaceBefore=8, leading=14)
S_H4   = sty('Heading4', fontName='Helvetica-Bold', fontSize=9.5, textColor=C_BLUE_MED,
              spaceAfter=2, spaceBefore=5, leading=12)
S_BODY = sty('Normal', fontName='Helvetica', fontSize=9.5, textColor=colors.black,
             spaceAfter=4, spaceBefore=1, leading=15, alignment=TA_JUSTIFY)
S_BULLET = sty('Normal', fontName='Helvetica', fontSize=9.5, textColor=colors.black,
               spaceAfter=3, spaceBefore=1, leading=14, leftIndent=14)
S_CODE = sty('Normal', fontName='Courier', fontSize=8.5, textColor=C_BLUE_DARK,
             spaceAfter=3, spaceBefore=3, leading=12, leftIndent=8)

# Priority styles
S_HI   = sty('Normal', fontName='Helvetica-Bold', fontSize=9, textColor=C_RED_PRIO,
             spaceAfter=2, leading=12, leftIndent=4)
S_MED  = sty('Normal', fontName='Helvetica', fontSize=9, textColor=colors.HexColor('#b7770d'),
             spaceAfter=2, leading=12, leftIndent=4)
S_LOW  = sty('Normal', fontName='Helvetica', fontSize=9, textColor=C_GREEN,
             spaceAfter=2, leading=12, leftIndent=4)

# Question styles
S_Q_NUM     = sty('Normal', fontName='Helvetica-Bold', fontSize=9.5, textColor=C_BLUE_DARK,
                  spaceAfter=3, spaceBefore=9, leading=14)
S_Q_CORRECT = sty('Normal', fontName='Helvetica-Bold', fontSize=9.5, textColor=C_GREEN,
                  spaceAfter=2, leading=13, leftIndent=14, backColor=C_GREEN_BG)
S_Q_WRONG   = sty('Normal', fontName='Helvetica', fontSize=9.5, textColor=colors.HexColor('#555'),
                  spaceAfter=2, leading=13, leftIndent=14)
S_Q_UNANS   = sty('Normal', fontName='Helvetica-Oblique', fontSize=8.5, textColor=colors.HexColor('#888'),
                  spaceAfter=2, leading=12, leftIndent=14)
S_Q_NOTE    = sty('Normal', fontName='Helvetica-Oblique', fontSize=8.5, textColor=colors.HexColor('#666'),
                  spaceAfter=3, leading=12, leftIndent=14)
S_SOURCE    = sty('Normal', fontName='Helvetica-Oblique', fontSize=7.5, textColor=colors.HexColor('#999'),
                  spaceAfter=5, leading=11)
S_NOTE      = sty('Normal', fontName='Helvetica-Oblique', fontSize=8, textColor=colors.HexColor('#555'),
                  spaceAfter=3, leading=11, leftIndent=8)
S_TOC       = sty('Normal', fontName='Helvetica', fontSize=9, textColor=C_BLUE_DARK,
                  spaceAfter=2, leading=13, leftIndent=8)
S_TOC_H     = sty('Normal', fontName='Helvetica-Bold', fontSize=10, textColor=C_BLUE_DARK,
                  spaceAfter=4, spaceBefore=6, leading=13)
S_NEW_Q_TAG = sty('Normal', fontName='Helvetica-Bold', fontSize=7.5, textColor=C_WHITE,
                  spaceAfter=0, leading=10)

def esc(t):
    if not t: return ''
    return str(t).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def domain_box(num, title, pct, color=C_BLUE_DARK):
    t = Table([[Paragraph(
        f"<font size='20' color='white'><b>DOMINIO {num}</b></font>  "
        f"<font size='13' color='#aaccff'>{esc(title)}</font>"
        f"<font size='11' color='#88aadd'>  ({pct}% del examen)</font>", S_H1)]],
        colWidths=[17*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),color),
        ('TOPPADDING',(0,0),(-1,-1),12),('BOTTOMPADDING',(0,0),(-1,-1),12),
        ('LEFTPADDING',(0,0),(-1,-1),14),
    ]))
    return t

def obj_box(obj_id, title, color=C_BLUE_MED):
    t = Table([[Paragraph(
        f"<font color='white'><b>{esc(obj_id)}</b>  {esc(title)}</font>", S_H2)]],
        colWidths=[17*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),color),
        ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
        ('LEFTPADDING',(0,0),(-1,-1),10),
    ]))
    return t

def section_box(title, bg=C_BLUE_BG, border=C_BLUE_LIGHT):
    t = Table([[Paragraph(f"<b>{esc(title)}</b>",
        sty('Normal', fontName='Helvetica-Bold', fontSize=10, textColor=C_BLUE_DARK, leading=13))]],
        colWidths=[17*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),('LINEBELOW',(0,0),(-1,-1),2,border),
        ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
        ('LEFTPADDING',(0,0),(-1,-1),8),
    ]))
    return t

def info_box(text, bg=C_YELLOW_BG, border=C_ORANGE):
    t = Table([[Paragraph(esc(text), S_NOTE)]], colWidths=[17*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),('LINEBELOW',(0,0),(-1,-1),1.5,border),
        ('LINEBEFORE',(0,0),(-1,-1),3,border),
        ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LEFTPADDING',(0,0),(-1,-1),8),
    ]))
    return t

def priority_table(d_num):
    """Build 3-col priority table from prioridades.json for a domain."""
    d = prio_data.get(str(d_num), {})
    hi  = d.get('high', [])
    med = d.get('med',  [])
    lo  = d.get('low',  [])

    def col_items(items, style, bg):
        out = []
        for x in items:
            out.append(Paragraph(f"• {esc(x)}", style))
        return out

    hi_col  = [Paragraph("<b>ALTA PRIORIDAD</b>",
        sty('Normal', fontName='Helvetica-Bold', fontSize=8, textColor=C_RED_PRIO, leading=11))] \
              + col_items(hi, S_HI, None)
    med_col = [Paragraph("<b>MEDIA PRIORIDAD</b>",
        sty('Normal', fontName='Helvetica-Bold', fontSize=8, textColor=C_AMBER, leading=11))] \
              + col_items(med, S_MED, None)
    lo_col  = [Paragraph("<b>COMPLEMENTARIO</b>",
        sty('Normal', fontName='Helvetica-Bold', fontSize=8, textColor=C_GREEN, leading=11))] \
              + col_items(lo, S_LOW, None)

    maxlen = max(len(hi_col), len(med_col), len(lo_col))
    emp = Paragraph('', S_LOW)
    while len(hi_col)  < maxlen: hi_col.append(emp)
    while len(med_col) < maxlen: med_col.append(emp)
    while len(lo_col)  < maxlen: lo_col.append(emp)

    data = list(zip(hi_col, med_col, lo_col))
    t = Table(list(data), colWidths=[5.5*cm, 5.5*cm, 5.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,-1),colors.HexColor('#fef2f2')),
        ('BACKGROUND',(1,0),(1,-1),colors.HexColor('#fffbf0')),
        ('BACKGROUND',(2,0),(2,-1),colors.HexColor('#f0fdf4')),
        ('GRID',(0,0),(-1,-1),0.3,C_GREY_LINE),
        ('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2),
        ('LEFTPADDING',(0,0),(-1,-1),4),('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    return t

# ── PARSE MESSER ──────────────────────────────────────────────────────────────
def parse_messer():
    result = {}
    cur_d, cur_obj, cur_title, cur_lines = None, None, '', []
    for page_text in messer_pages[1:]:
        for line in page_text.split('\n'):
            line = line.strip()
            if not line: continue
            dm = re.match(r'Dominio\s+(\d+)', line)
            if dm and len(line) < 80:
                if cur_d and cur_obj:
                    result.setdefault(cur_d, []).append((cur_obj, cur_title, cur_lines[:]))
                cur_d = int(dm.group(1)); cur_obj = None; cur_title = ''; cur_lines = []
                continue
            om = re.match(r'Objetivo\s+(\d+\.\d+)', line)
            if om:
                if cur_d and cur_obj:
                    result.setdefault(cur_d, []).append((cur_obj, cur_title, cur_lines[:]))
                cur_obj = om.group(1)
                cur_title = line.replace(f'Objetivo {cur_obj}','').strip('( )')
                cur_lines = []
                continue
            if cur_obj: cur_lines.append(line)
    if cur_d and cur_obj:
        result.setdefault(cur_d, []).append((cur_obj, cur_title, cur_lines[:]))
    return result

messer_data = parse_messer()
print(f"Messer parsed: {sum(len(v) for v in messer_data.values())} objectives")

# ── SECPLUS THEORY PAGES ──────────────────────────────────────────────────────
SECPLUS_OBJ_PAGES = {
    '1.1':(2,5),'1.2':(5,19),'1.3':(19,20),'1.4':(20,69),
    '2.1':(69,72),'2.2':(72,77),'2.3':(77,81),'2.4':(81,85),'2.5':(85,98),
    '3.1':(98,105),'3.2':(105,115),'3.3':(115,126),'3.4':(126,133),
    '4.1':(133,140),'4.2':(140,141),'4.3':(141,143),'4.4':(143,148),
    '4.5':(148,157),'4.6':(157,168),'4.7':(168,171),'4.8':(171,175),
    '4.9':(175,179),'5.1':(179,182),'5.2':(182,188),'5.3':(188,197),
    '5.4':(197,202),'5.5':(202,205),'5.6':(205,212),
}

def get_secplus_theory(obj_id):
    if obj_id not in SECPLUS_OBJ_PAGES: return []
    s, e = SECPLUS_OBJ_PAGES[obj_id]
    lines = []
    for pg in range(s-1, min(e-1, len(secplus_pages))):
        for line in secplus_pages[pg].split('\n'):
            line = line.strip()
            if not line: continue
            if re.match(r'^\d+\.', line) and '¿' in line: break
            if re.match(r'^[A-F]\)', line) or line.startswith('✓'): continue
            lines.append(line)
    return lines

# ── CLEAN QUESTIONS ───────────────────────────────────────────────────────────
def clean_question(idx, q_es_item, q_en_item):
    q_text  = q_es_item.get('question','')
    opts_es = q_es_item.get('options',[])
    correct_es = q_es_item.get('correct_answers',[])
    opts_en = q_en_item.get('options',[]) if q_en_item else []
    correct_en = q_en_item.get('correct_answers',[]) if q_en_item else []

    has_enc = '?' in q_text or any('?' in o for o in opts_es)
    valid = [a for a in correct_es if a in opts_es]
    valid_en = [a for a in correct_en if a in opts_en]

    # Apply manual correction
    if idx in corrections:
        corr = corrections[idx]
        # Map correction (EN answers) to ES options by position if needed
        mapped = []
        for ans in corr:
            if ans in opts_es:
                mapped.append(ans)
            elif opts_es and opts_en and ans in opts_en:
                pos = opts_en.index(ans)
                if pos < len(opts_es):
                    mapped.append(opts_es[pos])
            else:
                # Answer might be direct (acronyms/True/False)
                if ans in opts_es:
                    mapped.append(ans)
        if mapped:
            valid = mapped
        elif corr:
            # Try matching by content
            for ans in corr:
                if ans in opts_es:
                    valid.append(ans)

    note = no_opts_notes.get(idx, {}).get('note', '') if idx in no_opts_notes else ''

    return {
        'question': q_text,
        'options': opts_es,
        'correct': valid,
        'correct_en': valid_en,
        'question_en': q_en_item.get('question','') if q_en_item else '',
        'options_en': opts_en,
        'source': q_es_item.get('source',''),
        'has_enc': has_enc,
        'unanswered': not valid and not note,
        'note': note,
        'corrected': idx in corrections,
    }

questions_clean = []
for i, es in enumerate(q_es):
    en = q_en[i] if i < len(q_en) else None
    questions_clean.append(clean_question(i, es, en))

# Group by objective
TOPIC_TO_OBJ = {
    'Topic: Security Controls':'1.1', 'Topic: Encryption':'1.4', 'Topic: Hashing':'1.4',
    'Topic: Digital Signatures':'1.4', 'Topic: Digital Certificates':'1.4',
    'Topic: Threat Actor Types':'2.1', 'Topic: Threat Vectors':'2.2',
    'Topic: Social Engineering':'2.2', 'Topic: Security Vulnerabilities':'2.3',
    'Topic: Malware Attacks':'2.4', 'Topic: Network Attacks':'2.4',
    'Topic: Application Attacks':'2.4', 'Topic: Indicators Malicious Activity':'2.4',
    'Topic: Data Protection':'3.3', 'Topic: Resilience & Recovery':'3.4',
    'Topic: Wireless Security':'2.2', 'Topic: Application Security':'4.1',
    'Topic: Vulnerability Management':'4.3', 'Topic: Secure Network Protocols':'3.2',
    'Topic: Access Controls':'4.6', 'Topic: Password Concepts':'4.6',
    'Topic: Incident Response':'4.8', 'Topic: Risk Management':'5.2',
    'Topic: Agreement Types':'5.1', 'Topic: Penetration Testing':'4.3',
}

q_by_obj = {}
practice_qs = []
acronym_qs  = []
for q in questions_clean:
    src = q['source']
    if src.startswith('Topic:'):
        obj = TOPIC_TO_OBJ.get(src)
        if obj: q_by_obj.setdefault(obj, []).append(q)
    elif src.startswith('Practice'):
        practice_qs.append(q)
    elif src.startswith('Acronyms'):
        acronym_qs.append(q)

new_by_obj = {}
for q in new_questions:
    obj = q.get('objective')
    if obj: new_by_obj.setdefault(obj, []).append(q)

# Stats
answered = sum(1 for q in questions_clean if q['correct'])
unanswered = sum(1 for q in questions_clean if q['unanswered'])
corrected = sum(1 for q in questions_clean if q['corrected'])
print(f"Questions: {len(questions_clean)} total | {answered} con respuesta | {corrected} corregidas | {unanswered} sin resolver")
print(f"New questions: {len(new_questions)}")

# ── RENDER FUNCTIONS ──────────────────────────────────────────────────────────
LETTERS = 'ABCDEFGHIJ'

def render_question(q, num, story, is_new=False):
    q_text = q.get('question','')
    opts   = q.get('options', q.get('options_es', []))
    correct = set(q.get('correct', q.get('correct_answers', [])))
    src    = q.get('source','')
    note   = q.get('note','')
    unanswered = q.get('unanswered', not correct)
    corrected_flag = q.get('corrected', False)
    has_enc = q.get('has_enc', False)

    story.append(Paragraph(f"<b>{num}.</b> {esc(q_text)}", S_Q_NUM))
    if not is_new and has_enc and q.get('question_en'):
        story.append(Paragraph(f"<i>[EN: {esc(q.get('question_en','')[:120])}]</i>", S_NOTE))

    # Drag-and-drop note (no options)
    if note and not opts:
        story.append(info_box(f"Pregunta interactiva (drag-and-drop). {esc(note)}", C_BLUE_BG, C_BLUE_LIGHT))
        story.append(Paragraph(f"Fuente: {esc(src)}", S_SOURCE))
        return

    # Options
    if opts:
        for i, opt in enumerate(opts):
            letter = LETTERS[i] if i < len(LETTERS) else str(i)
            is_correct = opt in correct
            if is_correct:
                story.append(Paragraph(f"<font color='#27ae60'>&#x2713;</font> {letter}) {esc(opt)}", S_Q_CORRECT))
            else:
                story.append(Paragraph(f"    {letter}) {esc(opt)}", S_Q_WRONG))

    if unanswered and not note:
        story.append(info_box("Respuesta no disponible en la fuente. Consulta ExamCompass o la teoria.", C_RED_BG, C_RED))
    elif corrected_flag and not is_new:
        story.append(Paragraph("<font color='#27ae60'><i>* Respuesta corregida manualmente</i></font>", S_NOTE))

    if src:
        story.append(Paragraph(f"Fuente: {esc(src)}", S_SOURCE))

def render_messer_section(obj_id, story):
    d = int(obj_id.split('.')[0])
    if d not in messer_data: return
    matching = [o for o in messer_data[d] if o[0].startswith(obj_id)]
    if not matching: return

    story.append(section_box('Conceptos Clave — Professor Messer', C_BLUE_BG, C_BLUE_LIGHT))
    story.append(Spacer(1, 4))

    for obj_id_m, title, lines in matching:
        if title:
            story.append(Paragraph(f"<b>{esc(obj_id_m)}</b> {esc(title)}", S_H4))
        in_key = False
        for line in lines:
            line = line.strip()
            if not line: continue
            if 'Puntos Clave' in line or 'Puntos clave' in line:
                in_key = True
                story.append(Paragraph('Puntos clave para el examen:',
                    sty('Normal', fontName='Helvetica-Bold', fontSize=9,
                        textColor=C_ORANGE, spaceBefore=4, spaceAfter=2, leading=12)))
                continue
            if 'Conceptos y Definiciones' in line:
                in_key = False; continue
            if line.startswith('•') or line.startswith('-') or line.startswith('▸'):
                story.append(Paragraph(f"• {esc(line.lstrip('•-▸ '))}", S_BULLET))
            elif re.match(r'^[A-Z][A-Za-z /]+$', line) and len(line) < 50:
                story.append(Paragraph(f"<b>{esc(line)}</b>",
                    sty('Normal', fontName='Helvetica-Bold', fontSize=9,
                        textColor=C_BLUE_DARK, spaceBefore=3, spaceAfter=1, leading=12)))
            else:
                story.append(Paragraph(esc(line),
                    sty('Normal', fontName='Helvetica', fontSize=9,
                        textColor=colors.HexColor('#333' if not in_key else '#444'),
                        leading=12, leftIndent=10 if in_key else 0, spaceAfter=2)))
    story.append(Spacer(1, 6))

def render_flashcards(obj_id, story):
    """Render flashcard section for a given objective."""
    cards = [c for c in flashcards_all if c.get('obj') == obj_id]
    if not cards:
        return

    story.append(Spacer(1, 6))
    story.append(section_box(
        f'Flashcards — {obj_id}  ({len(cards)} tarjetas)',
        colors.HexColor('#fff9e6'), C_ORANGE))
    story.append(Spacer(1, 6))

    S_FRONT = sty('Normal', fontName='Helvetica-Bold', fontSize=9,
                  textColor=C_BLUE_DARK, leading=13, spaceAfter=2)
    S_BACK  = sty('Normal', fontName='Helvetica', fontSize=9,
                  textColor=colors.HexColor('#333333'), leading=13,
                  leftIndent=10, spaceAfter=0)

    for card in cards:
        front = esc(card.get('front',''))
        back  = card.get('back','')
        # Render as 2-col table: question | answer
        back_lines = back.split('\n')
        back_paras = [Paragraph(esc(l), S_BACK) for l in back_lines if l.strip()]
        front_para = Paragraph(f"<b>Q:</b> {front}", S_FRONT)

        row = Table(
            [[front_para, back_paras[0] if back_paras else Paragraph('', S_BACK)]],
            colWidths=[6.5*cm, 10.5*cm]
        )
        # If multiple back lines, add extra rows
        data = [[front_para, back_paras[0] if back_paras else Paragraph('—', S_BACK)]]
        for extra in back_paras[1:]:
            data.append([Paragraph('', S_BACK), extra])

        t = Table(data, colWidths=[6.5*cm, 10.5*cm])
        t.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(0,-1), colors.HexColor('#fff3cd')),
            ('BACKGROUND',(1,0),(1,-1), colors.HexColor('#ffffff')),
            ('LINEBELOW', (0,0),(-1,-1), 0.5, C_GREY_LINE),
            ('LINEBEFORE',(1,0),(1,-1), 1.5, C_ORANGE),
            ('TOPPADDING',(0,0),(-1,-1), 3),
            ('BOTTOMPADDING',(0,0),(-1,-1), 3),
            ('LEFTPADDING',(0,0),(-1,-1), 6),
            ('VALIGN',(0,0),(-1,-1),'TOP'),
        ]))
        story.append(t)
    story.append(Spacer(1, 8))

def render_secplus_theory(obj_id, story):
    theory = get_secplus_theory(obj_id)
    if not theory: return
    story.append(section_box('Teoria Complementaria — ExamCompass', C_GREY_BG, C_GREY_LINE))
    story.append(Spacer(1, 4))
    for line in theory[:35]:
        line = line.strip()
        if not line or len(line) < 3: continue
        if any(x in line for x in ['Teoria detallada','Conceptos clave','Fuente:']): continue
        if line.startswith('•') or line.startswith('-'):
            story.append(Paragraph(f"• {esc(line.lstrip('•- '))}", S_BULLET))
        elif re.match(r'^[A-Z][A-Z\s]+[:]', line):
            story.append(Paragraph(f"<b>{esc(line)}</b>", S_H4))
        else:
            story.append(Paragraph(esc(line), S_BODY))
    story.append(Spacer(1, 6))

# ── DOCUMENT STRUCTURE ────────────────────────────────────────────────────────
DOMAINS = [
    (1,'Conceptos Generales de Seguridad',12),
    (2,'Amenazas, Vulnerabilidades y Mitigaciones',22),
    (3,'Arquitectura de Seguridad',18),
    (4,'Operaciones de Seguridad',28),
    (5,'Gestion del Programa de Seguridad',20),
]
OBJECTIVES = {
    1:[('1.1','Tipos de controles de seguridad'),('1.2','CIA, AAA y Zero Trust'),
       ('1.3','Gestion del cambio'),('1.4','Criptografia')],
    2:[('2.1','Actores de amenaza'),('2.2','Vectores e ingenieria social'),
       ('2.3','Vulnerabilidades'),('2.4','Indicadores de actividad maliciosa'),
       ('2.5','Tecnicas de mitigacion')],
    3:[('3.1','Seguridad en entornos cloud y fisicos'),('3.2','Principios de seguridad en infraestructura'),
       ('3.3','Proteccion de datos y privacidad'),('3.4','Resiliencia y recuperacion')],
    4:[('4.1','Hardening y seguridad de aplicaciones'),('4.2','Gestion de activos'),
       ('4.3','Gestion de vulnerabilidades y pentest'),('4.4','Monitorizacion y alertas'),
       ('4.5','Seguridad en endpoint y email'),('4.6','IAM y control de acceso'),
       ('4.7','Automatizacion y orquestacion'),('4.8','Respuesta a incidentes y forense'),
       ('4.9','Logs y fuentes de datos')],
    5:[('5.1','Gobernanza y politicas'),('5.2','Gestion de riesgos'),
       ('5.3','Riesgos de terceros'),('5.4','Cumplimiento normativo'),
       ('5.5','Auditorias y evaluaciones'),('5.6','Concienciacion y formacion')],
}

# ── BUILD ─────────────────────────────────────────────────────────────────────
print("Construyendo PDF...")
story = []

# COVER
story.append(Spacer(1, 2.5*cm))
cover = Table([[Paragraph('<font color="white"><b>CompTIA Security+</b></font>',
    sty('Normal', fontName='Helvetica-Bold', fontSize=34, textColor=C_WHITE,
        alignment=TA_CENTER, leading=40))]],colWidths=[17*cm])
cover.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),C_BLUE_DARK),
    ('TOPPADDING',(0,0),(-1,-1),20),('BOTTOMPADDING',(0,0),(-1,-1),20)]))
story.append(cover)
story.append(Spacer(1, 0.4*cm))

sub = Table([[Paragraph('<font color="white"><b>SY0-701 · Guia Completa Fusionada v2 · En Espanol</b></font>',
    sty('Normal', fontName='Helvetica-Bold', fontSize=15, textColor=C_WHITE,
        alignment=TA_CENTER, leading=19))]],colWidths=[17*cm])
sub.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),C_BLUE_MED),
    ('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
story.append(sub)
story.append(Spacer(1, 0.8*cm))

cover_info = [
    ['Teoria:','Professor Messer SY0-701 (57p) — Todos los objetivos 1.1-5.6'],
    ['Tests:',f'ExamCompass 590 preguntas — {answered} con respuesta valida ({corrected} corregidas manualmente)'],
    ['Extra:',f'{len(new_questions)} preguntas nuevas (una por objetivo + temas clave sin cobertura)'],
    ['Mapa:','Prioridades ALTA/MEDIA/COMPLEMENTARIO con colores reales por dominio'],
    ['Estructura:','Dominio → Objetivo → Teoria → Prioridades → Preguntas Topic → Preguntas Nuevas'],
]
ci = Table(cover_info, colWidths=[3.5*cm, 13.5*cm])
ci.setStyle(TableStyle([
    ('FONTNAME',(0,0),(0,-1),'Helvetica-Bold'),('FONTNAME',(1,0),(1,-1),'Helvetica'),
    ('FONTSIZE',(0,0),(-1,-1),9),('TEXTCOLOR',(0,0),(0,-1),C_BLUE_DARK),
    ('BACKGROUND',(0,0),(-1,-1),C_BLUE_BG),('LINEBELOW',(0,0),(-1,-2),0.3,C_GREY_LINE),
    ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
    ('LEFTPADDING',(0,0),(-1,-1),6),
]))
story.append(ci)
story.append(Spacer(1, 0.6*cm))

stats = [
    ['Total preguntas',str(len(questions_clean)),'Con respuesta valida',str(answered)],
    ['Corregidas manualmente',str(corrected),'Sin respuesta posible',str(unanswered)],
    ['Practice Tests (mixtos)',str(len(practice_qs)),'Acronyms Quizzes',str(len(acronym_qs))],
    ['Preguntas nuevas añadidas',str(len(new_questions)),'Dominios cubiertos','5 (12+22+18+28+20%)'],
]
st = Table(stats, colWidths=[4.5*cm, 2.5*cm, 4.5*cm, 5.5*cm])
st.setStyle(TableStyle([
    ('FONTNAME',(0,0),(0,-1),'Helvetica-Bold'),('FONTNAME',(2,0),(2,-1),'Helvetica-Bold'),
    ('FONTNAME',(1,0),(1,-1),'Helvetica'),('FONTNAME',(3,0),(3,-1),'Helvetica'),
    ('FONTSIZE',(0,0),(-1,-1),9),('BACKGROUND',(0,0),(-1,-1),C_YELLOW_BG),
    ('GRID',(0,0),(-1,-1),0.3,C_GREY_LINE),
    ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),
    ('LEFTPADDING',(0,0),(-1,-1),6),
    ('TEXTCOLOR',(1,0),(1,-1),C_BLUE_DARK),('TEXTCOLOR',(3,0),(3,-1),C_BLUE_DARK),
]))
story.append(st)
story.append(PageBreak())

# TOC
story.append(Paragraph('<b>Tabla de Contenidos</b>',
    sty('Normal', fontName='Helvetica-Bold', fontSize=16, textColor=C_BLUE_DARK,
        spaceAfter=10, alignment=TA_CENTER)))
story.append(HRFlowable(width='100%', thickness=2, color=C_BLUE_DARK))
story.append(Spacer(1, 0.3*cm))
for d_num, d_name, d_pct in DOMAINS:
    story.append(Paragraph(f"<b>Dominio {d_num}: {esc(d_name)}</b>  ({d_pct}%)", S_TOC_H))
    for obj_id, obj_title in OBJECTIVES[d_num]:
        topic_count = len(q_by_obj.get(obj_id, []))
        new_count   = len(new_by_obj.get(obj_id, []))
        line = f"    {obj_id}  {esc(obj_title)}"
        if topic_count: line += f"  · <i>{topic_count}p ExamCompass</i>"
        if new_count:   line += f"  · <font color='#2d5aa0'><i>+{new_count}p nuevas</i></font>"
        story.append(Paragraph(line, S_TOC))
story.append(Spacer(1,0.4*cm))
story.append(Paragraph('<b>Practice Tests Mixtos</b>  (24 tests)', S_TOC_H))
story.append(Paragraph(f"    {len(practice_qs)} preguntas mezcladas de todos los dominios", S_TOC))
story.append(Paragraph('<b>Acronyms Quizzes</b>  (10 quizzes)', S_TOC_H))
story.append(Paragraph(f"    {len(acronym_qs)} preguntas de siglas y terminos clave", S_TOC))
story.append(PageBreak())

# MAPA GLOBAL
story.append(Paragraph('<b>Mapa Global de Prioridades para el Examen</b>',
    sty('Normal', fontName='Helvetica-Bold', fontSize=14, textColor=C_BLUE_DARK,
        spaceAfter=4, alignment=TA_CENTER)))
legend = Table([[
    Paragraph("<font color='#e74c3c'><b>ROJO = ALTA PRIORIDAD</b></font>  (sale con frecuencia en tests)", S_BODY),
    Paragraph("<font color='#f39c12'><b>NARANJA = MEDIA</b></font>  (importante conocer)", S_BODY),
    Paragraph("<font color='#27ae60'><b>VERDE = COMPLEMENTARIO</b></font>  (profundidad)", S_BODY),
]], colWidths=[5.7*cm, 5.5*cm, 5.8*cm])
legend.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,-1),C_GREY_BG),('GRID',(0,0),(-1,-1),0.3,C_GREY_LINE),
    ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
    ('LEFTPADDING',(0,0),(-1,-1),6),
]))
story.append(legend)
story.append(Spacer(1, 0.4*cm))

for d_num, d_name, d_pct in DOMAINS:
    story.append(Paragraph(f"<b>Dominio {d_num}: {esc(d_name)}</b>",
        sty('Normal', fontName='Helvetica-Bold', fontSize=10,
            textColor=C_BLUE_DARK, spaceAfter=3, spaceBefore=8, leading=13)))
    story.append(priority_table(d_num))
    story.append(Spacer(1, 6))

story.append(PageBreak())

# MAIN CONTENT
for d_num, d_name, d_pct in DOMAINS:
    story.append(PageBreak())          # dominio siempre empieza en pagina nueva
    story.append(domain_box(d_num, d_name, d_pct))
    story.append(Spacer(1, 0.4*cm))

    for obj_id, obj_title in OBJECTIVES[d_num]:
        story.append(CondPageBreak(5*cm))   # solo salta si quedan < 5 cm libres
        story.append(obj_box(obj_id, obj_title))
        story.append(Spacer(1, 0.3*cm))

        # Teoria Messer
        render_messer_section(obj_id, story)

        # Teoria SecPlus complementaria
        render_secplus_theory(obj_id, story)

        # Preguntas ExamCompass (Topic)
        topic_qs = q_by_obj.get(obj_id, [])
        if topic_qs:
            story.append(section_box(
                f'Preguntas Topic — ExamCompass ({len(topic_qs)} preguntas)',
                C_GREEN_BG, C_GREEN))
            story.append(Spacer(1, 4))
            for i, q in enumerate(topic_qs, 1):
                render_question(q, i, story, is_new=False)
                story.append(HRFlowable(width='100%', thickness=0.3, color=C_GREY_LINE))

        # Preguntas nuevas
        new_qs = new_by_obj.get(obj_id, [])
        if new_qs:
            story.append(Spacer(1, 6))
            story.append(section_box(
                f'Preguntas Adicionales — Generadas ({len(new_qs)} preguntas)',
                C_BLUE_BG, C_BLUE_LIGHT))
            story.append(Spacer(1, 4))
            for i, q in enumerate(new_qs, 1):
                render_question(q, i, story, is_new=True)
                story.append(HRFlowable(width='100%', thickness=0.3, color=C_GREY_LINE))

        if not topic_qs and not new_qs:
            story.append(info_box(
                f'Sin preguntas de Topic Quiz para {obj_id}. Ver Practice Tests al final.'))

        render_flashcards(obj_id, story)
        story.append(Spacer(1, 0.5*cm))

# PRACTICE TESTS
from collections import defaultdict
pt_hdr = Table([[Paragraph(
    '<font color="white"><b>Practice Tests Mixtos</b>  —  24 tests de todos los dominios</font>',
    sty('Normal', fontName='Helvetica-Bold', fontSize=14, textColor=C_WHITE,
        alignment=TA_CENTER, leading=18))]],colWidths=[17*cm])
pt_hdr.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),C_ORANGE),
    ('TOPPADDING',(0,0),(-1,-1),12),('BOTTOMPADDING',(0,0),(-1,-1),12)]))
story.append(pt_hdr)
story.append(Spacer(1, 0.4*cm))

# Map each practice question to a domain using TOPIC_TO_OBJ keywords in the question text,
# or fallback heuristics based on keyword matching.
DOMAIN_KEYWORDS = {
    1: ['control','cia','confidential','integridad','disponib','cifrado','criptograf','hash',
        'certificado','pki','aes','rsa','ecc','zero trust','aaa','radius','tls','firma digital',
        'encrypt','cryptograph','certificate','digital sign'],
    2: ['amenaza','malware','phishing','ransomware','virus','worm','trojan','botnet','rootkit',
        'exploit','vulnerabilidad','ataque','sql','xss','buffer','dos','ddos','arp','dns poison',
        'insider','nation-state','apt','mitre','ioc','social engineer','attack','threat'],
    3: ['cloud','iaas','paas','saas','vpn','firewall','red','network','dlp','backup','rto','rpo',
        'sitio','site','gdpr','privacidad','dato','data','proxy','nat','segmentac','vlan',
        'failover','redundan','continuidad','disaster'],
    4: ['siem','mfa','autenticac','pentest','vulnerabilidad','edr','incident','forense','forensi',
        'log','syslog','activo','asset','mdm','byod','monitori','automatiz','playbook','soar',
        'hardening','parche','patch','endpoint','iam','rbac','privilege','access control'],
    5: ['riesgo','risk','cumplimiento','compliance','politica','policy','hipaa','pci','nist',
        'iso 27','auditoria','audit','tercero','vendor','sla','bpa','mou','contrato','gdpr',
        'concienciacion','awareness','formacion','training'],
}

def guess_domain(q):
    text = (q.get('question','') + ' ' + ' '.join(q.get('options',[])) +
            ' ' + ' '.join(q.get('correct',[])) + ' ' + q.get('question_en','')).lower()
    scores = {}
    for d, kws in DOMAIN_KEYWORDS.items():
        scores[d] = sum(1 for kw in kws if kw in text)
    best = max(scores, key=lambda d: scores[d])
    return best if scores[best] > 0 else 0  # 0 = unclassified

# Group practice questions by domain
pt_by_domain = defaultdict(list)
for q in practice_qs:
    d = guess_domain(q)
    pt_by_domain[d].append(q)

DOMAIN_NAMES = {d_num: d_name for d_num, d_name, _ in DOMAINS}
DOMAIN_COLORS = {1: C_BLUE_MED, 2: C_RED, 3: C_GREEN, 4: C_ORANGE, 5: C_BLUE_DARK}

q_global = 0
for d_num in sorted(pt_by_domain.keys()):
    qs_domain = pt_by_domain[d_num]
    if d_num == 0:
        d_label = 'Sin clasificar'
        d_color = C_GREY_LINE
    else:
        d_label = f'Dominio {d_num}: {DOMAIN_NAMES[d_num]}'
        d_color = DOMAIN_COLORS.get(d_num, C_BLUE_MED)
    hdr = Table([[Paragraph(
        f'<font color="white"><b>{esc(d_label)}</b>  ({len(qs_domain)} preguntas)</font>',
        sty('Normal', fontName='Helvetica-Bold', fontSize=11, textColor=C_WHITE,
            alignment=TA_LEFT, leading=15))]],colWidths=[17*cm])
    hdr.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),d_color),
        ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
        ('LEFTPADDING',(0,0),(-1,-1),10)]))
    story.append(Spacer(1, 0.3*cm))
    story.append(hdr)
    story.append(Spacer(1, 4))
    for i, q in enumerate(qs_domain, 1):
        q_global += 1
        render_question(q, q_global, story)
        story.append(HRFlowable(width='100%', thickness=0.3, color=C_GREY_LINE))

story.append(PageBreak())

# ACRONYMS
acro_hdr = Table([[Paragraph(
    '<font color="white"><b>Acronyms Quizzes</b>  —  10 quizzes de siglas clave</font>',
    sty('Normal', fontName='Helvetica-Bold', fontSize=14, textColor=C_WHITE,
        alignment=TA_CENTER, leading=18))]],colWidths=[17*cm])
acro_hdr.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),C_BLUE_LIGHT),
    ('TOPPADDING',(0,0),(-1,-1),12),('BOTTOMPADDING',(0,0),(-1,-1),12)]))
story.append(acro_hdr)
story.append(Spacer(1, 0.4*cm))

acro_g = defaultdict(list)
for q in acronym_qs: acro_g[q['source']].append(q)
for name in sorted(acro_g.keys(), key=lambda x: int(re.search(r'\d+',x).group())):
    qs = acro_g[name]
    story.append(Paragraph(f"<b>{esc(name)}</b>  ({len(qs)} preguntas)",
        sty('Normal', fontName='Helvetica-Bold', fontSize=11, textColor=C_BLUE_LIGHT,
            spaceBefore=8, spaceAfter=4, leading=14)))
    story.append(HRFlowable(width='100%', thickness=1, color=C_BLUE_LIGHT))
    for i, q in enumerate(qs, 1):
        render_question(q, i, story)
        story.append(HRFlowable(width='100%', thickness=0.3, color=C_GREY_LINE))

# COMPILE
print("Compilando PDF...")
doc = SimpleDocTemplate(PATH_OUT, pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm,
    title='CompTIA Security+ SY0-701 Fusionado v2',
    author='Claude Code | Messer + ExamCompass',
    subject='CompTIA Security+ SY0-701')

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 7)
    canvas.setFillColor(colors.HexColor('#888888'))
    canvas.drawString(2*cm, 1.2*cm, f'CompTIA Security+ SY0-701 Fusionado v2 | Pagina {doc.page}')
    canvas.drawRightString(19*cm, 1.2*cm, 'Messer + ExamCompass | Uso personal')
    canvas.restoreState()

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)

import os
size = os.path.getsize(PATH_OUT)
print(f"\nPDF generado: {PATH_OUT}")
print(f"Paginas estimadas: ~200+ | Tamano: {size/1024/1024:.1f} MB")
