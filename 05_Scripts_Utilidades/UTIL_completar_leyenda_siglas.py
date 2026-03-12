#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Añade las siglas técnicas faltantes a la leyenda de abreviaciones
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import json
from pathlib import Path

LEYENDA_PATH = Path(r"D:\Users\cra\Desktop\Sec+\03_JSON_Datos\abreviaciones.json")

print("="*80)
print(" COMPLETANDO LEYENDA DE ABREVIACIONES")
print("="*80)
print()

# Cargar leyenda actual
with open(LEYENDA_PATH, 'r', encoding='utf-8') as f:
    leyenda = json.load(f)

print(f"Siglas actuales: {len(leyenda)}")
print()

# Siglas técnicas faltantes (solo las que son realmente siglas técnicas)
siglas_nuevas = {
    # Redes y Protocolos
    'DMZ': 'Demilitarized Zone',
    'SD-WAN': 'Software-Defined Wide Area Network',
    'MPLS': 'Multiprotocol Label Switching',
    'EIGRP': 'Enhanced Interior Gateway Routing Protocol',
    'RIP': 'Routing Information Protocol',
    'FTP': 'File Transfer Protocol',
    'HTTP': 'Hypertext Transfer Protocol',
    'HTTPS': 'HTTP Secure',
    'LDAPS': 'LDAP Secure',
    'SSL VPN': 'Secure Sockets Layer Virtual Private Network',
    'TAP': 'Test Access Point (network)',
    'SPAN': 'Switched Port Analyzer',
    'WMI': 'Windows Management Instrumentation',

    # Email Security
    'SPF': 'Sender Policy Framework',
    'DKIM': 'DomainKeys Identified Mail',
    'DMARC': 'Domain-based Message Authentication, Reporting & Conformance',
    'MIME': 'Multipurpose Internet Mail Extensions',
    'S/MIME': 'Secure/MIME',
    'PGP': 'Pretty Good Privacy',
    'STARTTLS': 'START Transport Layer Security',

    # Cloud y Seguridad Moderna
    'CSPM': 'Cloud Security Posture Management',
    'SASE': 'Secure Access Service Edge',
    'UEBA': 'User and Entity Behavior Analytics',
    'SBOM': 'Software Bill of Materials',

    # Datos y Privacidad
    'PII': 'Personally Identifiable Information',
    'PHI': 'Protected Health Information',
    'DPO': 'Data Protection Officer',
    'PCI': 'Payment Card Industry',
    'SSN': 'Social Security Number',
    'SAN': 'Subject Alternative Name (certificates)',

    # Forense y Análisis
    'FTK': 'Forensic Toolkit',
    'PCAP': 'Packet Capture',
    'IOA': 'Indicator of Attack',
    'KEV': 'Known Exploited Vulnerabilities',
    'NVD': 'National Vulnerability Database',

    # Autenticación y Acceso
    'FIDO2': 'Fast Identity Online 2',
    'PIN': 'Personal Identification Number',
    'KDC': 'Key Distribution Center (Kerberos)',
    'TGT': 'Ticket Granting Ticket (Kerberos)',
    'PAM': 'Privileged Access Management',
    'JIT': 'Just-in-Time (access)',
    'AUP': 'Acceptable Use Policy',

    # Seguridad de Sistemas
    'ASLR': 'Address Space Layout Randomization',
    'DEP': 'Data Execution Prevention',
    'FDE': 'Full Disk Encryption',
    'SGX': 'Software Guard Extensions (Intel)',
    'ATA': 'Advanced Technology Attachment',
    'HIPS': 'Host-based Intrusion Prevention System',
    'AV': 'Antivirus',
    'HA': 'High Availability',

    # Riesgos y Cumplimiento
    'BCP': 'Business Continuity Plan',
    'DRP': 'Disaster Recovery Plan',
    'DR': 'Disaster Recovery',
    'MTPD': 'Maximum Tolerable Period of Disruption',
    'MBCO': 'Maximum Bearable Cost of Outage',
    'SOC 2': 'Service Organization Control 2',
    'ISO 27001': 'International Organization for Standardization 27001',
    'NIST CSF': 'NIST Cybersecurity Framework',
    'NIST 800-88': 'NIST Guidelines for Media Sanitization',
    'CMMC': 'Cybersecurity Maturity Model Certification',
    'BAA': 'Business Associate Agreement (HIPAA)',
    'SOW': 'Statement of Work',

    # Métricas y Análisis
    'ROI': 'Return on Investment',
    'FAR': 'False Acceptance Rate',
    'FRR': 'False Rejection Rate',
    'CER': 'Crossover Error Rate',
    'FP': 'False Positive',
    'FN': 'False Negative',
    'CVSS': 'Common Vulnerability Scoring System',
    'CMDB': 'Configuration Management Database',

    # Autenticación Biométrica
    'SOD': 'Separation of Duties',

    # Mobile
    'COPE': 'Corporate-Owned, Personally Enabled',
    'SMS': 'Short Message Service',
    'QR': 'Quick Response (code)',

    # Otros
    'SQL': 'Structured Query Language',
    'TOCTOU': 'Time-of-Check to Time-of-Use',
    'CI/CD': 'Continuous Integration/Continuous Deployment',
    'SO': 'System Owner',
    'ID': 'Identifier',
    'PC': 'Personal Computer',
}

print(f"Añadiendo {len(siglas_nuevas)} siglas nuevas...")
print()

# Añadir a leyenda existente
for sigla, definicion in siglas_nuevas.items():
    if sigla not in leyenda:
        leyenda[sigla] = definicion
        print(f"  + {sigla}: {definicion}")

# Ordenar alfabéticamente
leyenda_ordenada = dict(sorted(leyenda.items()))

# Guardar
with open(LEYENDA_PATH, 'w', encoding='utf-8') as f:
    json.dump(leyenda_ordenada, f, ensure_ascii=False, indent=2)

# Actualizar también el TXT
OUTPUT_TXT = Path(r"D:\Users\cra\Desktop\Sec+\03_JSON_Datos\LEYENDA_ABREVIACIONES.txt")
with open(OUTPUT_TXT, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write(" LEYENDA DE ABREVIACIONES - CompTIA Security+ SY0-701\n")
    f.write("=" * 80 + "\n\n")

    for abbr, full in leyenda_ordenada.items():
        f.write(f"{abbr:20s} = {full}\n")

print()
print("="*80)
print(f" LEYENDA ACTUALIZADA: {len(leyenda_ordenada)} siglas totales")
print("="*80)
print()
print(f"JSON: {LEYENDA_PATH}")
print(f"TXT:  {OUTPUT_TXT}")
print()
print("Ahora regenera el PDF con:")
print("  python generar_pdf_condensado.py")
print("="*80)
