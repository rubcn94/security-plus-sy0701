# -*- coding: utf-8 -*-
"""
Generador del Ecosistema Completo de Estudio Security+ SY0-701
Objetivo: 85%+ en el examen
"""

import json
import os
from datetime import datetime, timedelta

print("="*70)
print("GENERADOR DE ECOSISTEMA COMPLETO - Security+ SY0-701")
print("Objetivo: 85%+ en el examen")
print("="*70)

# Cargar material de profundizacion
print("\n[1/7] Cargando material de profundizacion...")
with open('SecPlus_SY0-701_Material_Profundizacion_COMPLETO.json', 'r', encoding='utf-8') as f:
    material = json.load(f)

print(f"   -> {material['metadata']['total_terminos_profundizados']} terminos cargados")
print(f"   -> {len(material['flashcards'])} flashcards")
print(f"   -> {len(material['mapas_conceptuales'])} mapas conceptuales")
print(f"   -> {len(material['pbqs_simuladas'])} PBQs")

# =============================================================================
# 1. GENERAR MARKDOWN COMPLETO (para convertir a PDF)
# =============================================================================
print("\n[2/7] Generando markdown completo...")

markdown_content = f"""# Material de Profundizacion Security+ SY0-701

**Objetivo:** Alcanzar 85%+ en el examen
**Fecha de creacion:** {material['metadata']['fecha_creacion']}
**Total terminos ALTA prioridad:** {material['metadata']['total_terminos_profundizados']}

---

## Tabla de Contenidos

1. [Terminos Profundizados por Dominio](#terminos-profundizados)
2. [Mapas Conceptuales](#mapas-conceptuales)
3. [PBQs Simuladas](#pbqs-simuladas)
4. [Plan de Estudio](#plan-de-estudio)

---

## Terminos Profundizados

"""

# Agregar terminos por dominio
for dominio_key, dominio_data in material['dominios'].items():
    markdown_content += f"\n### {dominio_data['nombre']} ({dominio_data['peso_examen']})\n\n"
    markdown_content += f"**Terminos ALTA:** {dominio_data['total_terminos_alta']}\n\n"

    for termino in dominio_data['terminos_profundizados']:
        markdown_content += f"#### {termino['termino']}\n\n"
        markdown_content += f"**Prioridad:** {termino['prioridad']}\n\n"
        markdown_content += f"**Definicion base:** {termino['definicion_base']}\n\n"

        if termino.get('profundizacion') and termino['profundizacion'].get('explicacion_detallada'):
            markdown_content += f"**Explicacion detallada:**\n\n{termino['profundizacion']['explicacion_detallada']}\n\n"

            if termino['profundizacion'].get('ejemplos_practicos'):
                markdown_content += "**Ejemplos practicos:**\n\n"
                for ejemplo in termino['profundizacion']['ejemplos_practicos']:
                    markdown_content += f"- {ejemplo}\n"
                markdown_content += "\n"

        if termino.get('conexiones') and len(termino['conexiones']) > 0:
            markdown_content += f"**Conceptos relacionados:** {', '.join(termino['conexiones'])}\n\n"

        if termino.get('errores_comunes') and len(termino['errores_comunes']) > 0:
            markdown_content += "**Errores comunes:**\n\n"
            for error in termino['errores_comunes']:
                markdown_content += f"- {error}\n"
            markdown_content += "\n"

        markdown_content += "---\n\n"

# Mapas conceptuales
markdown_content += "\n## Mapas Conceptuales\n\n"
for mapa in material['mapas_conceptuales']:
    markdown_content += f"### {mapa['titulo']}\n\n"
    markdown_content += f"{mapa['descripcion']}\n\n"
    markdown_content += "**Nodos:**\n\n"
    for nodo in mapa['nodos']:
        markdown_content += f"- **{nodo['label']}** ({nodo['tipo']})\n"
    markdown_content += "\n**Relaciones:**\n\n"
    for rel in mapa['relaciones']:
        markdown_content += f"- {rel['from']} -> {rel['to']}: {rel['label']}\n"
    markdown_content += "\n---\n\n"

# PBQs
markdown_content += "\n## PBQs Simuladas\n\n"
for pbq in material['pbqs_simuladas']:
    markdown_content += f"### {pbq['id']}: {pbq['titulo']}\n\n"
    markdown_content += f"**Dominio:** {pbq['dominio']}  \n"
    markdown_content += f"**Dificultad:** {pbq['dificultad']}  \n"
    if pbq.get('tiempo_estimado'):
        markdown_content += f"**Tiempo estimado:** {pbq['tiempo_estimado']}  \n"
    markdown_content += f"\n**Escenario:**\n\n{pbq['escenario']}\n\n"

    if pbq.get('tareas'):
        markdown_content += "**Tareas:**\n\n"
        for tarea in pbq['tareas']:
            markdown_content += f"- {tarea}\n"
        markdown_content += "\n"

    markdown_content += "**Conceptos clave:** " + ", ".join(pbq['conceptos_clave']) + "\n\n"
    markdown_content += "---\n\n"

# Guardar markdown
with open('SecPlus_Material_Profundizacion_COMPLETO.md', 'w', encoding='utf-8') as f:
    f.write(markdown_content)

file_size_md = os.path.getsize('SecPlus_Material_Profundizacion_COMPLETO.md') / 1024
print(f"   -> Markdown generado: SecPlus_Material_Profundizacion_COMPLETO.md ({file_size_md:.1f} KB)")

# =============================================================================
# 2. GENERAR FLASHCARDS HTML INTERACTIVO
# =============================================================================
print("\n[3/7] Generando flashcards HTML interactivo...")

html_flashcards = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flashcards Security+ SY0-701 (220 terminos ALTA)</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }
        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .stats {
            background: rgba(255,255,255,0.2);
            padding: 15px 30px;
            border-radius: 10px;
            display: flex;
            gap: 30px;
            margin-bottom: 20px;
        }
        .stat {
            text-align: center;
            color: white;
        }
        .stat-value {
            font-size: 2em;
            font-weight: bold;
        }
        .stat-label {
            font-size: 0.9em;
            opacity: 0.9;
        }
        .card-container {
            perspective: 1000px;
            width: 100%;
            max-width: 700px;
            height: 450px;
            margin-bottom: 30px;
        }
        .card {
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.6s;
            cursor: pointer;
        }
        .card.flipped {
            transform: rotateY(180deg);
        }
        .card-face {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 40px;
            text-align: center;
        }
        .card-front {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
        }
        .card-back {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            transform: rotateY(180deg);
        }
        .card-number {
            position: absolute;
            top: 20px;
            left: 30px;
            font-size: 1.2em;
            font-weight: bold;
            opacity: 0.8;
        }
        .card-priority {
            position: absolute;
            top: 20px;
            right: 30px;
            background: rgba(255,255,255,0.3);
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
        }
        .card-domain {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 0.85em;
            opacity: 0.8;
            background: rgba(0,0,0,0.2);
            padding: 5px 15px;
            border-radius: 15px;
        }
        .question {
            font-size: 1.8em;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .answer {
            font-size: 1.3em;
            line-height: 1.6;
        }
        .hint {
            font-size: 0.9em;
            margin-top: 20px;
            opacity: 0.9;
            font-style: italic;
        }
        .controls {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }
        button {
            padding: 15px 30px;
            font-size: 1.1em;
            font-weight: bold;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .btn-prev {
            background: #ff6b6b;
            color: white;
        }
        .btn-prev:hover {
            background: #ee5a52;
            transform: translateY(-2px);
        }
        .btn-flip {
            background: #4ecdc4;
            color: white;
        }
        .btn-flip:hover {
            background: #45b8b0;
            transform: translateY(-2px);
        }
        .btn-next {
            background: #95e1d3;
            color: #333;
        }
        .btn-next:hover {
            background: #82d4c6;
            transform: translateY(-2px);
        }
        .btn-random {
            background: #f38181;
            color: white;
        }
        .btn-random:hover {
            background: #e06f6f;
            transform: translateY(-2px);
        }
        .progress-bar {
            width: 100%;
            max-width: 700px;
            height: 8px;
            background: rgba(255,255,255,0.3);
            border-radius: 10px;
            overflow: hidden;
        }
        .progress-fill {
            height: 100%;
            background: #95e1d3;
            transition: width 0.3s;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Security+ SY0-701 Flashcards</h1>
        <p>220 Terminos ALTA Prioridad</p>
    </div>

    <div class="stats">
        <div class="stat">
            <div class="stat-value" id="current-card">1</div>
            <div class="stat-label">Tarjeta actual</div>
        </div>
        <div class="stat">
            <div class="stat-value">220</div>
            <div class="stat-label">Total tarjetas</div>
        </div>
        <div class="stat">
            <div class="stat-value" id="progress-percent">0%</div>
            <div class="stat-label">Progreso</div>
        </div>
    </div>

    <div class="progress-bar">
        <div class="progress-fill" id="progress-fill"></div>
    </div>
    <br>

    <div class="card-container">
        <div class="card" id="flashcard" onclick="flipCard()">
            <div class="card-face card-front">
                <div class="card-number" id="card-number-front">1/220</div>
                <div class="card-priority" id="card-priority">ALTA</div>
                <div class="question" id="question">Cargando...</div>
                <div class="hint">(Click para ver respuesta)</div>
                <div class="card-domain" id="domain-front">Dominio</div>
            </div>
            <div class="card-face card-back">
                <div class="card-number" id="card-number-back">1/220</div>
                <div class="answer" id="answer">Respuesta...</div>
                <div class="hint">(Click para volver a pregunta)</div>
                <div class="card-domain" id="domain-back">Dominio</div>
            </div>
        </div>
    </div>

    <div class="controls">
        <button class="btn-prev" onclick="previousCard()">&#8592; Anterior</button>
        <button class="btn-flip" onclick="flipCard()">Voltear</button>
        <button class="btn-next" onclick="nextCard()">Siguiente &#8594;</button>
        <button class="btn-random" onclick="randomCard()">Aleatorio</button>
    </div>

    <script>
        const flashcards = """ + json.dumps(material['flashcards'], ensure_ascii=False) + """;

        let currentIndex = 0;
        let isFlipped = false;

        function updateCard() {
            const card = flashcards[currentIndex];
            document.getElementById('question').textContent = card.pregunta;
            document.getElementById('answer').textContent = card.respuesta;
            document.getElementById('card-number-front').textContent = `${currentIndex + 1}/220`;
            document.getElementById('card-number-back').textContent = `${currentIndex + 1}/220`;
            document.getElementById('card-priority').textContent = card.prioridad;
            document.getElementById('domain-front').textContent = card.dominio;
            document.getElementById('domain-back').textContent = card.dominio;
            document.getElementById('current-card').textContent = currentIndex + 1;

            const progress = ((currentIndex + 1) / 220 * 100).toFixed(1);
            document.getElementById('progress-percent').textContent = progress + '%';
            document.getElementById('progress-fill').style.width = progress + '%';

            if (isFlipped) {
                document.getElementById('flashcard').classList.remove('flipped');
                isFlipped = false;
            }
        }

        function flipCard() {
            document.getElementById('flashcard').classList.toggle('flipped');
            isFlipped = !isFlipped;
        }

        function nextCard() {
            currentIndex = (currentIndex + 1) % 220;
            updateCard();
        }

        function previousCard() {
            currentIndex = (currentIndex - 1 + 220) % 220;
            updateCard();
        }

        function randomCard() {
            currentIndex = Math.floor(Math.random() * 220);
            updateCard();
        }

        // Atajos de teclado
        document.addEventListener('keydown', function(event) {
            if (event.key === 'ArrowLeft') previousCard();
            if (event.key === 'ArrowRight') nextCard();
            if (event.key === ' ') {
                event.preventDefault();
                flipCard();
            }
            if (event.key === 'r' || event.key === 'R') randomCard();
        });

        // Inicializar
        updateCard();
    </script>
</body>
</html>
"""

with open('SecPlus_Flashcards_Interactivo.html', 'w', encoding='utf-8') as f:
    f.write(html_flashcards)

print("   -> Flashcards HTML generado: SecPlus_Flashcards_Interactivo.html")
print("      (Abre en navegador, usa flechas o click para navegar)")

# =============================================================================
# 3. GENERAR ARCHIVO ANKI (CSV para importar)
# =============================================================================
print("\n[4/7] Generando CSV para Anki...")

anki_csv = "Pregunta;Respuesta;Dominio;Prioridad\n"
for card in material['flashcards']:
    # Escapar punto y coma y comillas
    pregunta = card['pregunta'].replace(';', ',').replace('"', '""')
    respuesta = card['respuesta'].replace(';', ',').replace('"', '""')
    dominio = card['dominio'].replace(';', ',')
    anki_csv += f'"{pregunta}";"{respuesta}";"{dominio}";"{card["prioridad"]}"\n'

with open('SecPlus_Flashcards_Anki.csv', 'w', encoding='utf-8') as f:
    f.write(anki_csv)

print("   -> CSV Anki generado: SecPlus_Flashcards_Anki.csv")
print("      (Importar en Anki: File > Import > Separador: punto y coma)")

# =============================================================================
# 4. GENERAR MAPAS CONCEPTUALES EN MERMAID
# =============================================================================
print("\n[5/7] Generando mapas conceptuales en Mermaid...")

mermaid_file = "# Mapas Conceptuales Security+ SY0-701\n\n"
mermaid_file += "Visualizar en: https://mermaid.live\n\n"
mermaid_file += "---\n\n"

for mapa in material['mapas_conceptuales']:
    mermaid_file += f"## {mapa['titulo']}\n\n"
    mermaid_file += f"{mapa['descripcion']}\n\n"
    mermaid_file += "```mermaid\ngraph TD\n"

    # Nodos
    for nodo in mapa['nodos']:
        node_id = nodo['id']
        label = nodo['label'].replace('"', "'")
        mermaid_file += f'    {node_id}["{label}"]\n'

    mermaid_file += "\n"

    # Relaciones
    for rel in mapa['relaciones']:
        from_node = rel['from']
        to_node = rel['to']
        label = rel['label'].replace('"', "'")
        mermaid_file += f'    {from_node} -->|{label}| {to_node}\n'

    mermaid_file += "```\n\n"

    if mapa.get('notas'):
        mermaid_file += f"**Notas:** {mapa['notas']}\n\n"

    mermaid_file += "---\n\n"

with open('SecPlus_Mapas_Conceptuales.md', 'w', encoding='utf-8') as f:
    f.write(mermaid_file)

print("   -> Mapas Mermaid generados: SecPlus_Mapas_Conceptuales.md")
print("      (Copiar codigo y pegar en https://mermaid.live)")

# =============================================================================
# 5. GENERAR DOCUMENTO DE PBQs
# =============================================================================
print("\n[6/7] Generando documento de PBQs...")

pbqs_md = "# PBQs Simuladas - Security+ SY0-701\n\n"
pbqs_md += "**15 Performance-Based Questions con soluciones paso a paso**\n\n"
pbqs_md += "---\n\n"

for pbq in material['pbqs_simuladas']:
    pbqs_md += f"## {pbq['id']}: {pbq['titulo']}\n\n"
    pbqs_md += f"**Dominio:** {pbq['dominio']}  \n"
    pbqs_md += f"**Dificultad:** {pbq['dificultad']}  \n"

    if pbq.get('tiempo_estimado'):
        pbqs_md += f"**Tiempo estimado:** {pbq['tiempo_estimado']}  \n"

    pbqs_md += f"\n### Escenario\n\n{pbq['escenario']}\n\n"

    if pbq.get('tareas'):
        pbqs_md += "### Tareas\n\n"
        for i, tarea in enumerate(pbq['tareas'], 1):
            pbqs_md += f"{i}. {tarea}\n"
        pbqs_md += "\n"

    if pbq.get('solucion_paso_a_paso'):
        pbqs_md += "### Solucion Paso a Paso\n\n"
        for paso in pbq['solucion_paso_a_paso']:
            pbqs_md += f"#### Paso {paso['paso']}"
            if paso.get('fase'):
                pbqs_md += f" - {paso['fase']}"
            if paso.get('descripcion'):
                pbqs_md += f": {paso['descripcion']}"
            pbqs_md += "\n\n"

            if paso.get('tiempo'):
                pbqs_md += f"**Tiempo:** {paso['tiempo']}\n\n"

            if paso.get('contenido'):
                if isinstance(paso['contenido'], list):
                    for item in paso['contenido']:
                        pbqs_md += f"- {item}\n"
                    pbqs_md += "\n"
                elif isinstance(paso['contenido'], dict):
                    for key, value in paso['contenido'].items():
                        pbqs_md += f"**{key}:** {value}\n\n"
                else:
                    pbqs_md += f"{paso['contenido']}\n\n"

            if paso.get('acciones'):
                for accion in paso['acciones']:
                    pbqs_md += f"- {accion}\n"
                pbqs_md += "\n"

    pbqs_md += f"### Conceptos Clave\n\n{', '.join(pbq['conceptos_clave'])}\n\n"

    if pbq.get('errores_comunes'):
        pbqs_md += "### Errores Comunes\n\n"
        for error in pbq['errores_comunes']:
            pbqs_md += f"- {error}\n"
        pbqs_md += "\n"

    pbqs_md += "---\n\n"

with open('SecPlus_PBQs_Simuladas.md', 'w', encoding='utf-8') as f:
    f.write(pbqs_md)

print("   -> PBQs generadas: SecPlus_PBQs_Simuladas.md")

# =============================================================================
# 6. GENERAR PLAN DE ESTUDIO
# =============================================================================
print("\n[7/7] Generando plan de estudio...")

# Calcular duracion estimada (8 semanas)
fecha_inicio = datetime.now()
semanas = 8

plan_estudio = f"""# Plan de Estudio - Security+ SY0-701 (8 semanas)

**Objetivo:** 85%+ en el examen
**Fecha inicio:** {fecha_inicio.strftime('%d/%m/%Y')}
**Fecha estimada examen:** {(fecha_inicio + timedelta(weeks=semanas)).strftime('%d/%m/%Y')}
**Horas semanales:** 15-20 horas

---

## Semana 1-2: Dominio 4 (Operaciones - 28% del examen)

**Prioridad:** MAXIMA (mayor peso en el examen)

**Objetivos:**
- Dominar los 34 terminos ALTA prioridad del Dominio 4
- Completar PBQ_03 (Incident Response Ransomware)
- Completar PBQ_04 (SIEM Configuration)

**Actividades diarias:**
- Dia 1-2: Incident Response (fases NIST) + flashcards
- Dia 3-4: SIEM, SOAR, Log Management + flashcards
- Dia 5-6: Forensics, Chain of Custody + PBQ_03
- Dia 7: Vulnerability Management, Patch Management
- Dia 8-9: Code Analysis (SAST/DAST), DevSecOps + flashcards
- Dia 10-11: Backup, Recovery, Testing + PBQ_04
- Dia 12-14: Repaso completo Dominio 4 + autoevaluacion

**Recursos:**
- Flashcards: terminos 1-34 (Dominio 4)
- PBQs: 03, 04, 11
- Mapa conceptual: Incident Response

---

## Semana 3-4: Dominio 2 (Amenazas - 22% del examen)

**Prioridad:** ALTA

**Objetivos:**
- Dominar los 49 terminos ALTA prioridad del Dominio 2
- Completar PBQ_06 (Email Security: SPF/DKIM/DMARC)
- Identificar todos los tipos de malware y ataques

**Actividades diarias:**
- Dia 15-16: Threat Actors, APT, Attack Vectors + flashcards
- Dia 17-18: Malware (tipos completos) + flashcards
- Dia 19-20: Social Engineering (Phishing, Spear Phishing, etc.)
- Dia 21-22: Network Attacks (DDoS, MitM, DNS attacks) + PBQ_08
- Dia 23-24: Vulnerabilities (CVE, CVSS, 0-day) + flashcards
- Dia 25-26: Mitigation Techniques + PBQ_06
- Dia 27-28: Repaso completo Dominio 2 + autoevaluacion

**Recursos:**
- Flashcards: terminos 35-83 (Dominio 2)
- PBQs: 06, 08
- Mapa conceptual: Email Security

---

## Semana 5: Dominio 3 (Arquitectura - 18% del examen)

**Prioridad:** MEDIA-ALTA

**Objetivos:**
- Dominar los 60 terminos ALTA prioridad del Dominio 3
- Completar PBQ_01 (DMZ), PBQ_02 (802.1X), PBQ_09 (VPN IPsec)

**Actividades diarias:**
- Dia 29-30: PKI completa (CA, certificates, CRL, OCSP) + flashcards
- Dia 31-32: Network Security (DMZ, VPN, firewalls) + PBQ_01, PBQ_09
- Dia 33-34: Wireless Security (802.1X, WPA3, EAP) + PBQ_02
- Dia 35: Repaso Dominio 3 + autoevaluacion

**Recursos:**
- Flashcards: terminos 84-143 (Dominio 3)
- PBQs: 01, 02, 09, 10, 13, 15
- Mapas conceptuales: PKI End-to-End, Zero Trust

---

## Semana 6: Dominios 1 y 5 (Conceptos + Gestion - 32% combinados)

**Objetivos:**
- Dominar 45 terminos ALTA del Dominio 1
- Dominar 32 terminos ALTA del Dominio 5
- Completar PBQs de compliance y gestion

**Actividades diarias:**
- Dia 36-37: CIA Triad, AAA, Zero Trust + flashcards
- Dia 38-39: Security Controls, Defense in Depth + flashcards
- Dia 40-41: Risk Management, BCP/DRP + PBQ_05
- Dia 42: Compliance (GDPR, HIPAA, PCI-DSS) + PBQ_14
- Dia 43: Repaso Dominios 1 y 5

**Recursos:**
- Flashcards: terminos 144-220 (Dominios 1 y 5)
- PBQs: 05, 07, 12, 14
- Mapas conceptuales: Controles de Seguridad

---

## Semana 7: Repaso Intensivo + PBQs

**Objetivos:**
- Repasar todos los 220 terminos ALTA
- Completar todas las 15 PBQs
- Identificar puntos debiles

**Actividades diarias:**
- Dia 44: Flashcards aleatorias (100 terminos)
- Dia 45: PBQs pendientes + revisar errores
- Dia 46: Mapas conceptuales (dibujar de memoria)
- Dia 47: Simulacro de examen (preguntas online)
- Dia 48: Repaso de errores comunes
- Dia 49: Flashcards debiles (marcar las que fallas)
- Dia 50: Descanso mental

---

## Semana 8: Preparacion Final

**Objetivos:**
- Llegar al examen con 95%+ de confianza
- Repasar solo puntos criticos

**Actividades:**
- Dia 51-52: Simulacros de examen completos
- Dia 53: Repaso express de 220 terminos (solo definicion rapida)
- Dia 54: PBQs criticas (Incident Response, SIEM, Email Security)
- Dia 55: Cheat sheet mental (acrónimos, puertos, algoritmos)
- Dia 56: Descanso completo
- **Dia 57: EXAMEN**

---

## Recursos de Apoyo

1. **Flashcards HTML:** Abrir SecPlus_Flashcards_Interactivo.html
   - Usar modo aleatorio para evitar memorizacion por orden
   - Revisar diariamente las tarjetas que fallas

2. **Anki (opcional):** Importar SecPlus_Flashcards_Anki.csv
   - Sistema de repeticion espaciada automatico

3. **Mapas Conceptuales:** Copiar codigo de SecPlus_Mapas_Conceptuales.md
   - Visualizar en https://mermaid.live
   - Imprimir y poner en pared

4. **PBQs:** Practicar en SecPlus_PBQs_Simuladas.md
   - Hacer cada PBQ sin mirar solucion primero
   - Cronometrar tiempo real

5. **Material completo:** Leer SecPlus_Material_Profundizacion_COMPLETO.md
   - Buscar terminos especificos con Ctrl+F

---

## Metricas de Progreso

**Autoevaluacion semanal:**

- [ ] Semana 1: Dominio 4 completado (34/34 terminos)
- [ ] Semana 2: PBQs Dominio 4 completadas (3/3)
- [ ] Semana 3: Dominio 2 completado (49/49 terminos)
- [ ] Semana 4: PBQs Dominio 2 completadas (2/2)
- [ ] Semana 5: Dominio 3 completado (60/60 terminos + 6 PBQs)
- [ ] Semana 6: Dominios 1+5 completados (77/77 terminos + 4 PBQs)
- [ ] Semana 7: Repaso 220 terminos + 15 PBQs completas
- [ ] Semana 8: Simulacros >85% + confianza maxima

**Objetivo final:** 85%+ en el examen real

---

## Tips Finales

1. **No memorices, ENTIENDE:** Enfócate en el "por qué", no solo el "qué"
2. **PBQs primero en el examen:** Son las que más valen
3. **Gestiona el tiempo:** 90 minutos, 90 preguntas = 1 min/pregunta
4. **Elimina opciones incorrectas:** Tecnica de descarte
5. **Confía en tu primera respuesta:** No cambies sin razon clara

**¡Exito en el examen!**
"""

with open('SecPlus_Plan_Estudio_8_Semanas.md', 'w', encoding='utf-8') as f:
    f.write(plan_estudio)

print("   -> Plan de estudio generado: SecPlus_Plan_Estudio_8_Semanas.md")

# =============================================================================
# RESUMEN FINAL
# =============================================================================
print("\n" + "="*70)
print("ECOSISTEMA COMPLETO GENERADO!")
print("="*70)
print("\nArchivos creados:\n")
print("1. SecPlus_Material_Profundizacion_COMPLETO.md")
print("   -> Material completo en markdown (convertir a PDF con pandoc/typora)")
print()
print("2. SecPlus_Flashcards_Interactivo.html")
print("   -> Abrir en navegador, usar flechas o click")
print("   -> Atajos: Espacio=voltear, R=aleatorio")
print()
print("3. SecPlus_Flashcards_Anki.csv")
print("   -> Importar en Anki (File > Import, separador: punto y coma)")
print()
print("4. SecPlus_Mapas_Conceptuales.md")
print("   -> Copiar codigo y visualizar en https://mermaid.live")
print()
print("5. SecPlus_PBQs_Simuladas.md")
print("   -> 15 PBQs con soluciones paso a paso")
print()
print("6. SecPlus_Plan_Estudio_8_Semanas.md")
print("   -> Plan completo con objetivos y metricas")
print()
print("="*70)
print("TODO LISTO PARA ALCANZAR 85%+ EN EL EXAMEN!")
print("="*70)
