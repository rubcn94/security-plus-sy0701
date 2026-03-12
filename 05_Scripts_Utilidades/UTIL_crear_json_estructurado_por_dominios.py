#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crea un JSON estructurado y optimizado del Security+ SY0-701
Elimina redundancias y organiza por dominios/objetivos/prioridades
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import json
import re
from pathlib import Path
from collections import defaultdict

JSON_PATH = Path(r"D:\Users\cra\Desktop\Sec+\secplus_fusionado_completo.json")
OUTPUT_PATH = Path(r"D:\Users\cra\Desktop\Sec+\secplus_estructurado.json")

def cargar_json():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def extraer_mapa_prioridades(datos):
    """Extrae el mapa de prioridades de las paginas 3-5"""
    print("\n[1/5] Extrayendo mapa de prioridades...")

    mapa = {
        1: {'alta': [], 'media': [], 'complementario': []},
        2: {'alta': [], 'media': [], 'complementario': []},
        3: {'alta': [], 'media': [], 'complementario': []},
        4: {'alta': [], 'media': [], 'complementario': []},
        5: {'alta': [], 'media': [], 'complementario': []}
    }

    # El mapa esta en formato tabla con 3 columnas lado a lado
    # Estrategia: extraer el texto completo de pags 3-5 y parsear tabla manualmente
    bloque_1 = datos['bloques'][0]

    texto_completo = ""
    for pagina in bloque_1['paginas'][2:5]:  # Paginas 3, 4, 5
        texto_completo += pagina['texto'] + "\n"

    # Dividir por dominios
    dominios_texto = texto_completo.split('Dominio ')

    for dom_texto in dominios_texto[1:]:  # Saltar primera parte vacia
        # Extraer numero de dominio
        match = re.match(r'(\d+):', dom_texto)
        if not match:
            continue

        dom_num = int(match.group(1))
        if dom_num not in mapa:
            continue

        # Buscar seccion entre este dominio y el siguiente
        lineas = dom_texto.split('\n')

        # Usar heuristica: las lineas con  • al inicio son items de prioridad
        # Las columnas estan mezcladas, asi que detectamos por posicion aproximada
        for linea in lineas:
            linea_orig = linea
            linea = linea.strip()

            # Ignorar headers
            if not linea or 'PRIORIDAD' in linea or 'COMPLEMENTARIO' == linea:
                continue
            if 'Messer' in linea or 'Pagina' in linea or dom_texto.index(linea_orig) < 50:
                continue

            # Items empiezan con \x7f (simbolo de bullet en el PDF)
            if linea.startswith('\x7f') or linea_orig.lstrip().startswith('\x7f'):
                item = linea.lstrip('\x7f').strip()

                if len(item) > 5:
                    # Clasificar por palabras clave de alta prioridad
                    items_alta = ['preventivo', 'detectivo', 'correctivo', 'cia', 'aes', 'rsa',
                                  'pki', 'zero trust', 'aaa', 'radius', 'apt', 'phishing', 'sqli',
                                  'xss', 'virus', 'worm', 'ransomware', 'buffer overflow', 'mitre',
                                  'iaas', 'paas', 'saas', 'vpn', 'dlp', 'rto', 'rpo', 'ngfw',
                                  'ids', 'ips', 'hot', 'cold', 'gdpr', 'siem', 'mfa', 'fases ir',
                                  'volatilidad', 'rbac', 'vuln scan', 'pentest', 'av', 'edr',
                                  'riesgo =', 'sle', 'aro', 'ale', 'hipaa', 'pci', 'jerarquia']

                    if any(kw in item.lower() for kw in items_alta):
                        if item not in mapa[dom_num]['alta']:
                            mapa[dom_num]['alta'].append(item)
                    elif '/' in item and len(item) < 40:  # Acronimos cortos suelen ser media
                        if item not in mapa[dom_num]['media']:
                            mapa[dom_num]['media'].append(item)
                    else:
                        if item not in mapa[dom_num]['complementario']:
                            mapa[dom_num]['complementario'].append(item)

    # Estadisticas
    for dom in range(1, 6):
        total = len(mapa[dom]['alta']) + len(mapa[dom]['media']) + len(mapa[dom]['complementario'])
        print(f"   Dominio {dom}: {len(mapa[dom]['alta'])} alta | {len(mapa[dom]['media'])} media | {len(mapa[dom]['complementario'])} baja = {total} items")

    return mapa

def extraer_dominios_objetivos(datos):
    """Extrae la estructura de dominios y objetivos"""
    print("\n[2/5] Parseando dominios y objetivos...")

    dominios = {
        1: {'nombre': 'Conceptos Generales de Seguridad', 'porcentaje': 12, 'objetivos': {}},
        2: {'nombre': 'Amenazas, Vulnerabilidades y Mitigaciones', 'porcentaje': 22, 'objetivos': {}},
        3: {'nombre': 'Arquitectura de Seguridad', 'porcentaje': 18, 'objetivos': {}},
        4: {'nombre': 'Operaciones de Seguridad', 'porcentaje': 28, 'objetivos': {}},
        5: {'nombre': 'Gestion del Programa de Seguridad', 'porcentaje': 20, 'objetivos': {}}
    }

    # Mapeo manual de objetivos por dominio
    objetivos_mapa = {
        1: [
            ('1.1', 'Tipos de controles de seguridad'),
            ('1.2', 'CIA, AAA y Zero Trust'),
            ('1.3', 'Gestion del cambio'),
            ('1.4', 'Criptografia')
        ],
        2: [
            ('2.1', 'Actores de amenaza'),
            ('2.2', 'Vectores e ingenieria social'),
            ('2.3', 'Vulnerabilidades'),
            ('2.4', 'Indicadores de actividad maliciosa'),
            ('2.5', 'Tecnicas de mitigacion')
        ],
        3: [
            ('3.1', 'Seguridad en entornos cloud y fisicos'),
            ('3.2', 'Principios de seguridad en infraestructura'),
            ('3.3', 'Proteccion de datos y privacidad'),
            ('3.4', 'Resiliencia y recuperacion')
        ],
        4: [
            ('4.1', 'Hardening y seguridad de aplicaciones'),
            ('4.2', 'Gestion de activos'),
            ('4.3', 'Gestion de vulnerabilidades y pentest'),
            ('4.4', 'Monitorizacion y alertas'),
            ('4.5', 'Seguridad en endpoint y email'),
            ('4.6', 'IAM y control de acceso'),
            ('4.7', 'Automatizacion y orquestacion'),
            ('4.8', 'Respuesta a incidentes y forense'),
            ('4.9', 'Logs y fuentes de datos')
        ],
        5: [
            ('5.1', 'Gobernanza y politicas'),
            ('5.2', 'Gestion de riesgos'),
            ('5.3', 'Riesgos de terceros'),
            ('5.4', 'Cumplimiento normativo'),
            ('5.5', 'Auditorias y evaluaciones'),
            ('5.6', 'Concienciacion y formacion')
        ]
    }

    for dom_num, objetivos in objetivos_mapa.items():
        for obj_id, obj_titulo in objetivos:
            dominios[dom_num]['objetivos'][obj_id] = {
                'titulo': obj_titulo,
                'teoria_messer': {'puntos_clave': [], 'conceptos': []},
                'teoria_examcompass': [],
                'preguntas_topic': [],
                'preguntas_nuevas': [],
                'flashcards': []
            }

    total_obj = sum(len(d['objetivos']) for d in dominios.values())
    print(f"   Estructura creada: 5 dominios, {total_obj} objetivos")

    return dominios

def extraer_teoria_messer(datos, dominios):
    """Extrae la teoria de Professor Messer para cada objetivo"""
    print("\n[3/5] Extrayendo teoria Messer...")

    objetivo_actual = None
    en_puntos_clave = False
    contador = 0

    for bloque in datos['bloques']:
        for pagina in bloque['paginas']:
            texto = pagina['texto']
            lineas = texto.split('\n')

            for linea in lineas:
                linea = linea.strip()

                # Detectar objetivo
                match_obj = re.match(r'^(\d+\.\d+)\s+(.+)', linea)
                if match_obj:
                    obj_id = match_obj.group(1)
                    # Buscar en que dominio esta
                    for dom_num, dom_data in dominios.items():
                        if obj_id in dom_data['objetivos']:
                            objetivo_actual = (dom_num, obj_id)
                            en_puntos_clave = False
                            break

                # Detectar seccion "Conceptos Clave — Professor Messer"
                if objetivo_actual and 'Conceptos Clave' in linea and 'Messer' in linea:
                    continue

                # Detectar "Puntos clave para el examen"
                if objetivo_actual and ('Puntos clave' in linea or 'Puntos Clave' in linea):
                    en_puntos_clave = True
                    continue

                # Detectar fin de seccion Messer
                if 'Teoria Complementaria' in linea or 'ExamCompass' in linea:
                    objetivo_actual = None
                    en_puntos_clave = False
                    continue

                # Extraer contenido
                if objetivo_actual and linea:
                    dom_num, obj_id = objetivo_actual

                    # Ignorar headers/footers
                    if 'Messer + ExamCompass' in linea or 'Pagina' in linea:
                        continue

                    # Punto clave (empieza con ■ o •)
                    if en_puntos_clave and (linea.startswith('■') or linea.startswith('•')):
                        punto = linea[1:].strip()
                        if len(punto) > 5:
                            dominios[dom_num]['objetivos'][obj_id]['teoria_messer']['puntos_clave'].append(punto)
                            contador += 1
                    # Concepto general
                    elif not en_puntos_clave and len(linea) > 20 and not linea.startswith('Fuente:'):
                        dominios[dom_num]['objetivos'][obj_id]['teoria_messer']['conceptos'].append(linea)

    print(f"   Extraidos {contador} puntos clave de teoria Messer")
    return dominios

def extraer_preguntas(datos, dominios):
    """Extrae preguntas Topic y Nuevas"""
    print("\n[4/5] Extrayendo preguntas...")

    # Mapeo de topics a objetivos
    topic_to_obj = {
        'Security Controls': '1.1',
        'Encryption': '1.4',
        'Hashing': '1.4',
        'Digital Signatures': '1.4',
        'Digital Certificates': '1.4',
        'Threat Actor Types': '2.1',
        'Threat Vectors': '2.2',
        'Social Engineering': '2.2',
        'Security Vulnerabilities': '2.3',
        'Malware Attacks': '2.4',
        'Network Attacks': '2.4',
        'Application Attacks': '2.4',
        'Indicators Malicious Activity': '2.4',
        'Data Protection': '3.3',
        'Resilience & Recovery': '3.4',
        'Wireless Security': '2.2',
        'Application Security': '4.1',
        'Vulnerability Management': '4.3',
        'Secure Network Protocols': '3.2',
        'Access Controls': '4.6',
        'Password Concepts': '4.6',
        'Incident Response': '4.8',
        'Risk Management': '5.2',
        'Agreement Types': '5.1',
        'Penetration Testing': '4.3'
    }

    pregunta_actual = None
    objetivo_actual = None
    tipo_pregunta = None  # 'topic' o 'nueva'
    contador_topic = 0
    contador_nuevas = 0

    for bloque in datos['bloques']:
        for pagina in bloque['paginas']:
            texto = pagina['texto']
            lineas = texto.split('\n')

            for i, linea in enumerate(lineas):
                linea = linea.strip()

                # Detectar seccion de preguntas Topic
                if 'Preguntas Topic' in linea and 'ExamCompass' in linea:
                    tipo_pregunta = 'topic'
                    continue

                # Detectar seccion de preguntas Nuevas/Adicionales
                if 'Preguntas Adicionales' in linea or 'Preguntas Nuevas' in linea:
                    tipo_pregunta = 'nueva'
                    continue

                # Detectar fuente para identificar objetivo
                if linea.startswith('Fuente:'):
                    for topic_name, obj_id in topic_to_obj.items():
                        if topic_name in linea:
                            # Buscar dominio
                            dom_num = int(obj_id.split('.')[0])
                            if obj_id in dominios[dom_num]['objetivos']:
                                objetivo_actual = (dom_num, obj_id)
                                break

                # Detectar inicio de pregunta (numero seguido de punto y texto)
                match_pregunta = re.match(r'^(\d+)\.\s+(.+)', linea)
                if match_pregunta and objetivo_actual and tipo_pregunta:
                    num = match_pregunta.group(1)
                    texto_pregunta = match_pregunta.group(2)

                    if len(texto_pregunta) > 20:  # Pregunta real
                        pregunta_actual = {
                            'numero': num,
                            'pregunta': texto_pregunta,
                            'opciones': [],
                            'correctas': []
                        }

                # Detectar opciones (A), B), C), etc)
                if pregunta_actual and re.match(r'^[✓\s]*[A-J]\)', linea):
                    es_correcta = linea.startswith('✓')
                    opcion_texto = re.sub(r'^[✓\s]*[A-J]\)\s*', '', linea)

                    if len(opcion_texto) > 0:
                        pregunta_actual['opciones'].append(opcion_texto)
                        if es_correcta:
                            pregunta_actual['correctas'].append(opcion_texto)

                # Fin de pregunta (siguiente pregunta o fuente)
                if pregunta_actual and (linea.startswith('Fuente:') or (i > 0 and re.match(r'^\d+\.', linea))):
                    if len(pregunta_actual['opciones']) > 0:
                        dom_num, obj_id = objetivo_actual

                        if tipo_pregunta == 'topic':
                            dominios[dom_num]['objetivos'][obj_id]['preguntas_topic'].append(pregunta_actual)
                            contador_topic += 1
                        elif tipo_pregunta == 'nueva':
                            dominios[dom_num]['objetivos'][obj_id]['preguntas_nuevas'].append(pregunta_actual)
                            contador_nuevas += 1

                    pregunta_actual = None

    print(f"   Extraidas {contador_topic} preguntas Topic")
    print(f"   Extraidas {contador_nuevas} preguntas Nuevas")

    return dominios

def generar_json_estructurado(datos, mapa_prioridades, dominios):
    """Genera el JSON final estructurado"""
    print("\n[5/5] Generando JSON estructurado...")

    estructura = {
        'metadata': datos['metadata'],
        'mapa_prioridades': mapa_prioridades,
        'dominios': {}
    }

    # Convertir estructura de dominios
    for dom_num in range(1, 6):
        dom_data = dominios[dom_num]

        estructura['dominios'][str(dom_num)] = {
            'numero': dom_num,
            'nombre': dom_data['nombre'],
            'porcentaje_examen': dom_data['porcentaje'],
            'prioridades': mapa_prioridades[dom_num],
            'objetivos': {}
        }

        for obj_id, obj_data in dom_data['objetivos'].items():
            estructura['dominios'][str(dom_num)]['objetivos'][obj_id] = obj_data

    # Guardar
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(estructura, f, ensure_ascii=False, indent=2)

    # Estadisticas
    size_mb = OUTPUT_PATH.stat().st_size / 1024 / 1024

    total_puntos = sum(
        len(obj['teoria_messer']['puntos_clave'])
        for dom in estructura['dominios'].values()
        for obj in dom['objetivos'].values()
    )

    total_preguntas_topic = sum(
        len(obj['preguntas_topic'])
        for dom in estructura['dominios'].values()
        for obj in dom['objetivos'].values()
    )

    total_preguntas_nuevas = sum(
        len(obj['preguntas_nuevas'])
        for dom in estructura['dominios'].values()
        for obj in dom['objetivos'].values()
    )

    print(f"\n{'='*70}")
    print(f"JSON ESTRUCTURADO GENERADO EXITOSAMENTE")
    print(f"{'='*70}")
    print(f"Archivo: {OUTPUT_PATH}")
    print(f"Tamaño: {size_mb:.2f} MB")
    print(f"\nContenido:")
    print(f"  - 5 dominios con prioridades clasificadas")
    print(f"  - 28 objetivos estructurados")
    print(f"  - {total_puntos} puntos clave Messer")
    print(f"  - {total_preguntas_topic} preguntas Topic")
    print(f"  - {total_preguntas_nuevas} preguntas Nuevas")
    print(f"{'='*70}\n")

def main():
    print("\n" + "="*70)
    print(" CREACION DE JSON ESTRUCTURADO - Security+ SY0-701")
    print("="*70)

    datos = cargar_json()

    mapa_prioridades = extraer_mapa_prioridades(datos)
    dominios = extraer_dominios_objetivos(datos)
    dominios = extraer_teoria_messer(datos, dominios)
    dominios = extraer_preguntas(datos, dominios)
    generar_json_estructurado(datos, mapa_prioridades, dominios)

    print("[COMPLETADO] JSON estructurado creado con exito\n")

if __name__ == "__main__":
    main()
