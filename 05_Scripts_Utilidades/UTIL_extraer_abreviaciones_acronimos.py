#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrae todas las abreviaciones del JSON y crea una leyenda completa
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import json
import re
from pathlib import Path

JSON_PATH = Path(r"D:\Users\cra\Desktop\Sec+\03_JSON_Datos\secplus_estructurado.json")

print("Extrayendo abreviaciones del JSON...\n")

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Diccionario de abreviaciones encontradas (manual + auto)
abreviaciones = {
    # Criptografía
    'AES': 'Advanced Encryption Standard',
    'RSA': 'Rivest-Shamir-Adleman',
    'ECC': 'Elliptic Curve Cryptography',
    'PKI': 'Public Key Infrastructure',
    'CA': 'Certificate Authority',
    'CRL': 'Certificate Revocation List',
    'OCSP': 'Online Certificate Status Protocol',
    'HSTS': 'HTTP Strict Transport Security',
    'TLS': 'Transport Layer Security',
    'SSL': 'Secure Sockets Layer',
    'SSH': 'Secure Shell',
    'SFTP': 'SSH File Transfer Protocol',
    'FTPS': 'FTP Secure',
    'PFS': 'Perfect Forward Secrecy',
    'DH': 'Diffie-Hellman',
    'DHE': 'Diffie-Hellman Ephemeral',
    'ECDHE': 'Elliptic Curve Diffie-Hellman Ephemeral',
    'SHA': 'Secure Hash Algorithm',
    'MD5': 'Message Digest 5',
    'HMAC': 'Hash-based Message Authentication Code',

    # Autenticación y Control de Acceso
    'AAA': 'Authentication, Authorization, Accounting',
    'CIA': 'Confidentiality, Integrity, Availability',
    'RADIUS': 'Remote Authentication Dial-In User Service',
    'TACACS+': 'Terminal Access Controller Access-Control System Plus',
    'LDAP': 'Lightweight Directory Access Protocol',
    'SAML': 'Security Assertion Markup Language',
    'OIDC': 'OpenID Connect',
    'OAuth': 'Open Authorization',
    'SSO': 'Single Sign-On',
    'MFA': 'Multi-Factor Authentication',
    'OTP': 'One-Time Password',
    'TOTP': 'Time-based One-Time Password',
    'HOTP': 'HMAC-based One-Time Password',
    'JWT': 'JSON Web Token',
    'PAP': 'Password Authentication Protocol',
    'CHAP': 'Challenge-Handshake Authentication Protocol',
    'EAP': 'Extensible Authentication Protocol',
    'PEAP': 'Protected Extensible Authentication Protocol',
    'EAP-TLS': 'EAP-Transport Layer Security',
    'NTLM': 'NT LAN Manager',
    'NAC': 'Network Access Control',
    'IAM': 'Identity and Access Management',
    'RBAC': 'Role-Based Access Control',
    'DAC': 'Discretionary Access Control',
    'MAC': 'Mandatory Access Control',
    'ABAC': 'Attribute-Based Access Control',

    # Amenazas y Ataques
    'APT': 'Advanced Persistent Threat',
    'SQLi': 'SQL Injection',
    'XSS': 'Cross-Site Scripting',
    'CSRF': 'Cross-Site Request Forgery',
    'SSRF': 'Server-Side Request Forgery',
    'DoS': 'Denial of Service',
    'DDoS': 'Distributed Denial of Service',
    'MITM': 'Man-in-the-Middle',
    'RAT': 'Remote Access Trojan',
    'C2': 'Command and Control',
    'IoC': 'Indicator of Compromise',
    'IoA': 'Indicator of Attack',
    'TTP': 'Tactics, Techniques, and Procedures',
    'MITRE ATT&CK': 'MITRE Adversarial Tactics, Techniques & Common Knowledge',
    'CVE': 'Common Vulnerabilities and Exposures',
    'CVSS': 'Common Vulnerability Scoring System',
    'CWE': 'Common Weakness Enumeration',

    # Redes y Infraestructura
    'VPN': 'Virtual Private Network',
    'VLAN': 'Virtual Local Area Network',
    'DNS': 'Domain Name System',
    'DNSSEC': 'DNS Security Extensions',
    'DHCP': 'Dynamic Host Configuration Protocol',
    'IP': 'Internet Protocol',
    'TCP': 'Transmission Control Protocol',
    'UDP': 'User Datagram Protocol',
    'ICMP': 'Internet Control Message Protocol',
    'ARP': 'Address Resolution Protocol',
    'NAT': 'Network Address Translation',
    'PAT': 'Port Address Translation',
    'QoS': 'Quality of Service',
    'SNMP': 'Simple Network Management Protocol',
    'NTP': 'Network Time Protocol',
    'RDP': 'Remote Desktop Protocol',
    'VNC': 'Virtual Network Computing',
    'BGP': 'Border Gateway Protocol',
    'OSPF': 'Open Shortest Path First',

    # Seguridad de Redes
    'IDS': 'Intrusion Detection System',
    'IPS': 'Intrusion Prevention System',
    'NIDS': 'Network Intrusion Detection System',
    'HIDS': 'Host-based Intrusion Detection System',
    'NGFW': 'Next-Generation Firewall',
    'WAF': 'Web Application Firewall',
    'UTM': 'Unified Threat Management',
    'SIEM': 'Security Information and Event Management',
    'SOAR': 'Security Orchestration, Automation and Response',
    'SOC': 'Security Operations Center',
    'NOC': 'Network Operations Center',
    'DLP': 'Data Loss Prevention',
    'EDR': 'Endpoint Detection and Response',
    'XDR': 'Extended Detection and Response',
    'MDR': 'Managed Detection and Response',
    'NDR': 'Network Detection and Response',

    # Wireless
    'WEP': 'Wired Equivalent Privacy',
    'WPA': 'Wi-Fi Protected Access',
    'WPA2': 'Wi-Fi Protected Access 2',
    'WPA3': 'Wi-Fi Protected Access 3',
    'WPS': 'Wi-Fi Protected Setup',
    'SSID': 'Service Set Identifier',
    'AP': 'Access Point',
    'NFC': 'Near Field Communication',
    'RFID': 'Radio Frequency Identification',

    # Cloud y Virtualización
    'IaaS': 'Infrastructure as a Service',
    'PaaS': 'Platform as a Service',
    'SaaS': 'Software as a Service',
    'FaaS': 'Function as a Service',
    'IaC': 'Infrastructure as Code',
    'VM': 'Virtual Machine',
    'VDI': 'Virtual Desktop Infrastructure',
    'API': 'Application Programming Interface',
    'REST': 'Representational State Transfer',
    'SOAP': 'Simple Object Access Protocol',

    # Gestión y Compliance
    'GRC': 'Governance, Risk and Compliance',
    'SLA': 'Service Level Agreement',
    'MSA': 'Master Service Agreement',
    'BPA': 'Business Partnership Agreement',
    'MOU': 'Memorandum of Understanding',
    'MOA': 'Memorandum of Agreement',
    'NDA': 'Non-Disclosure Agreement',
    'DPA': 'Data Processing Agreement',
    'GDPR': 'General Data Protection Regulation',
    'HIPAA': 'Health Insurance Portability and Accountability Act',
    'PCI DSS': 'Payment Card Industry Data Security Standard',
    'SOX': 'Sarbanes-Oxley Act',
    'FISMA': 'Federal Information Security Management Act',
    'NIST': 'National Institute of Standards and Technology',
    'ISO': 'International Organization for Standardization',
    'CIS': 'Center for Internet Security',

    # Gestión de Riesgos
    'BIA': 'Business Impact Analysis',
    'RTO': 'Recovery Time Objective',
    'RPO': 'Recovery Point Objective',
    'MTTR': 'Mean Time to Repair',
    'MTBF': 'Mean Time Between Failures',
    'SLE': 'Single Loss Expectancy',
    'ALE': 'Annual Loss Expectancy',
    'ARO': 'Annual Rate of Occurrence',
    'KRI': 'Key Risk Indicator',
    'KPI': 'Key Performance Indicator',

    # Respuesta a Incidentes
    'IR': 'Incident Response',
    'CSIRT': 'Computer Security Incident Response Team',
    'CERT': 'Computer Emergency Response Team',
    'IOC': 'Indicator of Compromise',
    'TTPs': 'Tactics, Techniques, and Procedures',
    'STIX': 'Structured Threat Information Expression',
    'TAXII': 'Trusted Automated Exchange of Indicator Information',

    # Desarrollo Seguro
    'SDLC': 'Software Development Life Cycle',
    'DevSecOps': 'Development, Security, and Operations',
    'CI/CD': 'Continuous Integration/Continuous Deployment',
    'SAST': 'Static Application Security Testing',
    'DAST': 'Dynamic Application Security Testing',
    'IAST': 'Interactive Application Security Testing',
    'RASP': 'Runtime Application Self-Protection',
    'SCA': 'Software Composition Analysis',
    'OWASP': 'Open Web Application Security Project',

    # Sistemas Industriales
    'ICS': 'Industrial Control Systems',
    'SCADA': 'Supervisory Control and Data Acquisition',
    'PLC': 'Programmable Logic Controller',
    'HMI': 'Human-Machine Interface',
    'DCS': 'Distributed Control System',
    'RTU': 'Remote Terminal Unit',
    'OT': 'Operational Technology',
    'IT': 'Information Technology',

    # Forense y Análisis
    'RAM': 'Random Access Memory',
    'ROM': 'Read-Only Memory',
    'HDD': 'Hard Disk Drive',
    'SSD': 'Solid State Drive',
    'USB': 'Universal Serial Bus',
    'BIOS': 'Basic Input/Output System',
    'UEFI': 'Unified Extensible Firmware Interface',
    'TPM': 'Trusted Platform Module',
    'HSM': 'Hardware Security Module',

    # Otros
    'OS': 'Operating System',
    'ACL': 'Access Control List',
    'GPO': 'Group Policy Object',
    'AD': 'Active Directory',
    'OU': 'Organizational Unit',
    'BYOD': 'Bring Your Own Device',
    'MDM': 'Mobile Device Management',
    'MAM': 'Mobile Application Management',
    'UEM': 'Unified Endpoint Management',
    'VoIP': 'Voice over Internet Protocol',
    'CCTV': 'Closed-Circuit Television',
    'UPS': 'Uninterruptible Power Supply',
    'HVAC': 'Heating, Ventilation, and Air Conditioning',
    'EOL': 'End of Life',
    'EOSL': 'End of Service Life',
    'CSPRNG': 'Cryptographically Secure Pseudo-Random Number Generator',
    'PEP': 'Policy Enforcement Point',
    'PDP': 'Policy Decision Point',
    'CCB': 'Change Control Board',
    'CASB': 'Cloud Access Security Broker',
}

# Ordenar alfabéticamente
abreviaciones_ordenadas = dict(sorted(abreviaciones.items()))

print(f"Total de abreviaciones encontradas: {len(abreviaciones_ordenadas)}\n")

# Guardar en archivo de texto
OUTPUT_TXT = Path(r"D:\Users\cra\Desktop\Sec+\03_JSON_Datos\LEYENDA_ABREVIACIONES.txt")

with open(OUTPUT_TXT, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write(" LEYENDA DE ABREVIACIONES - CompTIA Security+ SY0-701\n")
    f.write("=" * 80 + "\n\n")

    for abbr, full in abreviaciones_ordenadas.items():
        f.write(f"{abbr:20s} = {full}\n")

print(f"[OK] Leyenda guardada en: {OUTPUT_TXT}")

# Guardar también en JSON para usar en el PDF
OUTPUT_JSON = Path(r"D:\Users\cra\Desktop\Sec+\03_JSON_Datos\abreviaciones.json")
with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(abreviaciones_ordenadas, f, ensure_ascii=False, indent=2)

print(f"[OK] JSON guardado en: {OUTPUT_JSON}")
print(f"\nTotal: {len(abreviaciones_ordenadas)} abreviaciones")
