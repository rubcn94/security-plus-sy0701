#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrae TODAS las siglas del JSON y verifica cuáles faltan en la leyenda
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import json
import re
from pathlib import Path

JSON_PATH = Path(r"D:\Users\cra\Desktop\Sec+\03_JSON_Datos\secplus_estructurado.json")
LEYENDA_PATH = Path(r"D:\Users\cra\Desktop\Sec+\03_JSON_Datos\abreviaciones.json")

print("="*80)
print(" VERIFICACION DE SIGLAS FALTANTES EN LEYENDA")
print("="*80)
print()

# Cargar datos
with open(JSON_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(LEYENDA_PATH, 'r', encoding='utf-8') as f:
    leyenda_actual = json.load(f)

print(f"Siglas en leyenda actual: {len(leyenda_actual)}")
print()

# Extraer TODAS las siglas del JSON (mayúsculas de 2+ letras)
siglas_encontradas = set()

def extraer_siglas(texto):
    """Extrae siglas (mayúsculas de 2+ caracteres) de un texto"""
    if not texto:
        return []

    # Patrón: 2+ letras mayúsculas, opcionalmente seguidas de números o guiones
    patron = r'\b[A-Z][A-Z0-9\-]{1,}(?:\s*[A-Z0-9\-]+)*\b'
    matches = re.findall(patron, str(texto))

    # Filtrar solo siglas válidas (no palabras normales en mayúsculas)
    siglas = []
    for match in matches:
        # Limpiar espacios
        match = match.strip()
        # Ignorar si es muy largo (probablemente no es sigla)
        if len(match) <= 20:
            # Ignorar palabras comunes que no son siglas
            if match not in ['TODOS', 'NO', 'SI', 'OK', 'IMPORTANTE', 'NUNCA', 'SIEMPRE']:
                siglas.append(match)

    return siglas

# Recorrer todo el JSON
print("Extrayendo siglas del JSON...")
print()

# Prioridades
for dom_id, dom_data in data['dominios'].items():
    for tipo_prioridad in ['alta', 'media', 'complementario']:
        if tipo_prioridad in dom_data.get('prioridades', {}):
            for item in dom_data['prioridades'][tipo_prioridad]:
                siglas_encontradas.update(extraer_siglas(item))

    # Puntos clave de teoría
    for obj_id, obj_data in dom_data.get('objetivos', {}).items():
        puntos = obj_data.get('teoria_messer', {}).get('puntos_clave', [])
        for punto in puntos:
            siglas_encontradas.update(extraer_siglas(punto))

print(f"Total de siglas únicas encontradas en el JSON: {len(siglas_encontradas)}")
print()

# Comparar con leyenda actual
siglas_faltantes = []
for sigla in sorted(siglas_encontradas):
    if sigla not in leyenda_actual:
        siglas_faltantes.append(sigla)

print("="*80)
print(f" SIGLAS FALTANTES: {len(siglas_faltantes)}")
print("="*80)
print()

if siglas_faltantes:
    for sigla in siglas_faltantes:
        print(f"  ❌ {sigla}")
else:
    print("  ✅ Todas las siglas están en la leyenda")

print()
print("="*80)
print(" RECOMENDACIONES")
print("="*80)
print()

if siglas_faltantes:
    print("Siglas que definitivamente deben añadirse:")
    print()

    # Definiciones para las siglas más importantes que faltan
    definiciones_sugeridas = {
        # Análisis basado en contexto Security+
        'MTPD': 'Maximum Tolerable Period of Disruption',
        'MBCO': 'Maximum Bearable Cost of Outage',
        'CSPM': 'Cloud Security Posture Management',
        'SASE': 'Secure Access Service Edge',
        'DMARC': 'Domain-based Message Authentication, Reporting & Conformance',
        'DKIM': 'DomainKeys Identified Mail',
        'SPF': 'Sender Policy Framework',
        'PGP': 'Pretty Good Privacy',
        'STARTTLS': 'START Transport Layer Security',
        'EIGRP': 'Enhanced Interior Gateway Routing Protocol',
        'RIP': 'Routing Information Protocol',
        'BCP': 'Business Continuity Plan',
        'DRP': 'Disaster Recovery Plan',
        'CCM': 'Change Control Manager',
        'UAT': 'User Acceptance Testing',
        'FAAS': 'Function as a Service (ya tienes FaaS)',
        'IR': 'Incident Response (ya lo tienes)',
    }

    importantes = []
    for sigla in siglas_faltantes:
        if sigla in definiciones_sugeridas or len(sigla) <= 6:
            importantes.append(sigla)

    print(f"Siglas importantes a añadir ({len(importantes)}):")
    for sigla in importantes:
        if sigla in definiciones_sugeridas:
            print(f"  '{sigla}': '{definiciones_sugeridas[sigla]}',")
        else:
            print(f"  '{sigla}': '[DEFINIR]',")

print()
print("="*80)
