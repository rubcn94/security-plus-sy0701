#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para fusionar diccionario base + extensiones SOC-level
y generar contenido inteligente para términos sin extensión manual
"""

import json
import sys
import io
from pathlib import Path
from datetime import datetime

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Rutas
BASE_DIR = Path(r'D:\Users\cra\Desktop\Sec+')
DICT_PATH = BASE_DIR / '02_Diccionarios_Referencia' / 'JSON' / 'SecPlus_SY0-701_Diccionario_Completo.json'
SOC_EXT_PATH = BASE_DIR / 'soc_extensions_database.json'
OUTPUT_JSON_PATH = BASE_DIR / '02_Diccionarios_Referencia' / 'JSON' / 'SecPlus_SY0-701_SOC_COMPLETO.json'
OUTPUT_MD_PATH = BASE_DIR / '02_Diccionarios_Referencia' / 'Markdown' / 'SecPlus_SY0-701_SOC_COMPLETO.md'

def load_json(path):
    """Carga archivo JSON con encoding UTF-8"""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, path):
    """Guarda JSON con formato legible"""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ JSON guardado: {path}")

def save_markdown(content, path):
    """Guarda archivo Markdown"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Markdown guardado: {path}")

def generate_smart_extension(term_key, term_data):
    """
    Genera extensión SOC-level inteligente basándose en el tipo de término
    Esto cubre términos sin extensión manual
    """
    termino = term_data.get('termino', term_key)
    definicion = term_data.get('definicion', '')

    # Categorizar por keywords en definición
    is_crypto = any(word in definicion.lower() for word in ['cifrado', 'encryption', 'hash', 'clave', 'key', 'algoritmo'])
    is_attack = any(word in definicion.lower() for word in ['ataque', 'attack', 'exploit', 'vulnerab', 'malware', 'threat'])
    is_network = any(word in definicion.lower() for word in ['red', 'network', 'firewall', 'router', 'switch', 'vpn'])
    is_auth = any(word in definicion.lower() for word in ['autenti', 'author', 'password', 'credencial', 'login', 'access'])
    is_compliance = any(word in definicion.lower() for word in ['cumpl', 'regulation', 'policy', 'gdpr', 'hipaa', 'pci'])

    extension = {
        "tools": [],
        "log_analysis": {
            "logs_to_check": [],
            "ioc_patterns": [],
            "example_log": ""
        },
        "mitre_attack": {
            "relevant_techniques": []
        },
        "response_playbook": {
            "scenario": f"Incidente relacionado con {termino}",
            "steps": []
        },
        "false_positives": [],
        "real_world_case": {
            "incident": "Por investigar - casos relevantes en industria",
            "summary": "",
            "timeline": [],
            "lessons_learned": []
        },
        "enterprise_integration": {
            "windows": "",
            "linux": "",
            "telemetry_required": [],
            "blind_spots": []
        }
    }

    # Agregar contenido específico por categoría
    if is_crypto:
        extension["tools"] = [
            {"tool": "openssl", "purpose": f"Operaciones con {termino}", "command": "openssl [subcommand]", "output": "Ver man openssl"},
            {"tool": "hashcat", "purpose": "Testing de fortaleza criptográfica", "command": "hashcat -m [mode] hash.txt wordlist.txt", "output": "Crackeo de hashes"}
        ]
        extension["log_analysis"]["logs_to_check"] = [
            "Windows: Event ID 4657 (registry value modification) para cambios en crypto settings",
            "Application logs: SSL/TLS handshake failures",
            "Syslog: openssl/crypto library errors"
        ]

    elif is_attack:
        extension["tools"] = [
            {"tool": "Wireshark", "purpose": f"Detectar tráfico asociado a {termino}", "command": "wireshark -i eth0 -f 'suspicious_filter'", "output": "Capturas PCAP"},
            {"tool": "Snort/Suricata", "purpose": "IDS rules para detectar ataque", "command": "alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)", "output": "Alertas IDS"}
        ]
        extension["log_analysis"]["ioc_patterns"] = [
            f"Patrones de tráfico asociados a {termino}",
            "Anomalías en logs de aplicación/sistema",
            "Picos en uso de recursos (CPU/RAM/Network)"
        ]
        extension["mitre_attack"]["relevant_techniques"] = [
            {"tactic": "Initial Access / Execution", "technique": "Ver MITRE ATT&CK matrix", "relevance": f"Relacionado con {termino}", "detection": "Monitoreo de logs + behavioral analysis"}
        ]

    elif is_network:
        extension["tools"] = [
            {"tool": "tcpdump", "purpose": f"Captura de tráfico relacionado con {termino}", "command": "tcpdump -i any -w capture.pcap", "output": "Archivo PCAP"},
            {"tool": "nmap", "purpose": "Escaneo y detección", "command": "nmap -sV -p- target", "output": "Puertos abiertos y servicios"}
        ]
        extension["log_analysis"]["logs_to_check"] = [
            "Firewall logs: conexiones permitidas/denegadas",
            "Router/Switch logs: cambios en configuración",
            "NetFlow/sFlow data: análisis de tráfico"
        ]

    elif is_auth:
        extension["tools"] = [
            {"tool": "Event Viewer", "purpose": "Análisis de autenticación", "command": "Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}", "output": "Eventos de logon"},
            {"tool": "grep", "purpose": "Búsqueda en auth logs Linux", "command": "grep 'Failed password' /var/log/auth.log", "output": "Intentos fallidos"}
        ]
        extension["log_analysis"]["logs_to_check"] = [
            "Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)",
            "Linux: /var/log/auth.log, /var/log/secure",
            "RADIUS/TACACS+ logs"
        ]
        extension["response_playbook"]["steps"] = [
            {"phase": "1. Detection", "actions": ["Monitor failed authentication attempts", "Alert on anomalous login patterns"]},
            {"phase": "2. Triage", "actions": ["Verify user legitimacy", "Check source IP reputation", "Review login history"]},
            {"phase": "3. Containment", "actions": ["Disable compromised account", "Block attacking IP", "Reset credentials"]}
        ]

    elif is_compliance:
        extension["tools"] = [
            {"tool": "Compliance scanner", "purpose": f"Verificar cumplimiento de {termino}", "command": "nessus/openscap scan", "output": "Reporte de compliance"},
            {"tool": "Audit logs", "purpose": "Evidencia para auditorías", "command": "Export logs para auditor", "output": "Logs estructurados"}
        ]
        extension["log_analysis"]["logs_to_check"] = [
            "Audit logs: cambios en configuración de seguridad",
            "Access logs: quién accedió a datos sensibles",
            "Change management logs: tickets y aprobaciones"
        ]

    return extension

def merge_dictionaries():
    """Fusiona diccionario base con extensiones SOC"""
    print("🔄 Cargando archivos...")
    base_dict = load_json(DICT_PATH)
    soc_extensions = load_json(SOC_EXT_PATH)

    print(f"📊 Diccionario base: {base_dict['metadata']['total_terminos']} términos")
    print(f"🔧 Extensiones SOC manuales: {len([k for k in soc_extensions.keys() if not k.startswith('_')])} términos")

    # Crear estructura de salida
    output = {
        "metadata": {
            "title": "Security+ SY0-701 - Diccionario SOC-Level COMPLETO",
            "version": "4.0 - SOC Professional",
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "base_terms": base_dict['metadata']['total_terminos'],
            "high_priority_terms": base_dict['metadata']['estadisticas_prioridad']['ALTA'],
            "manual_soc_extensions": len([k for k in soc_extensions.keys() if not k.startswith('_')]),
            "focus": "Operacional - Comandos, Logs, MITRE ATT&CK, Playbooks, Casos Reales, False Positives",
            "target_audience": "SOC Analyst Level 1/2, Security Engineer, Security+ Exam Prep"
        },
        "dominios": {}
    }

    # Procesar cada dominio
    print("\n🏗️  Procesando dominios...")
    total_extended = 0

    for domain_key, domain_data in base_dict.items():
        if domain_key == 'metadata':
            continue

        print(f"\n  📁 {domain_key}...")

        output_domain = {
            "peso_examen": domain_data.get('peso_examen', 'N/A'),
            "terminos_alta_prioridad": 0,
            "terminos": {}
        }

        if 'definiciones' in domain_data:
            for term_key, term_data in domain_data['definiciones'].items():
                # Solo procesar términos ALTA prioridad
                if term_data.get('prioridad') != 'ALTA':
                    continue

                output_domain["terminos_alta_prioridad"] += 1

                # Estructura base
                extended_term = {
                    "base": {
                        "termino": term_data.get('termino', term_key),
                        "definicion": term_data.get('definicion', ''),
                        "ejemplos_basicos": term_data.get('ejemplos', []),
                        "prioridad": "ALTA"
                    }
                }

                # Buscar extensión SOC (manual o generada)
                if term_key in soc_extensions:
                    # Usar extensión manual
                    extended_term["soc_level"] = soc_extensions[term_key]
                    extended_term["extension_type"] = "manual"
                    total_extended += 1
                else:
                    # Generar extensión inteligente
                    extended_term["soc_level"] = generate_smart_extension(term_key, term_data)
                    extended_term["extension_type"] = "auto-generated"

                output_domain["terminos"][term_key] = extended_term

        output["dominios"][domain_key] = output_domain

    print(f"\n✅ Procesamiento completado:")
    print(f"   - Términos ALTA prioridad: {base_dict['metadata']['estadisticas_prioridad']['ALTA']}")
    print(f"   - Extensiones manuales: {total_extended}")
    print(f"   - Extensiones auto-generadas: {base_dict['metadata']['estadisticas_prioridad']['ALTA'] - total_extended}")

    return output

def generate_markdown(json_data):
    """Genera archivo Markdown legible del JSON"""
    md = []
    md.append("# 📘 Security+ SY0-701 - Material SOC-Level COMPLETO\n")
    md.append(f"**Versión:** {json_data['metadata']['version']}  ")
    md.append(f"**Creado:** {json_data['metadata']['created']}  ")
    md.append(f"**Total términos ALTA prioridad:** {json_data['metadata']['high_priority_terms']}  ")
    md.append(f"**Extensiones manuales SOC:** {json_data['metadata']['manual_soc_extensions']}  \n")
    md.append("---\n\n")

    md.append("## 🎯 Objetivo\n\n")
    md.append("Material extendido para **superar nivel SOC Analyst 1** y **aprobar Security+ con 85%+**.\n\n")
    md.append("Cada término incluye:\n")
    md.append("- ✅ **Herramientas y comandos prácticos**\n")
    md.append("- ✅ **Log analysis con ejemplos reales**\n")
    md.append("- ✅ **MITRE ATT&CK mapping**\n")
    md.append("- ✅ **Response playbooks paso a paso**\n")
    md.append("- ✅ **False positives comunes y tuning**\n")
    md.append("- ✅ **Casos reales de incidentes**\n")
    md.append("- ✅ **Enterprise integration (Windows/Linux/Cloud)**\n\n")

    md.append("---\n\n")

    # Generar contenido por dominio
    for domain_key, domain_data in json_data['dominios'].items():
        domain_name = domain_key.replace('_', ' ')
        md.append(f"## {domain_name}\n\n")
        md.append(f"**Peso examen:** {domain_data['peso_examen']}  ")
        md.append(f"**Términos ALTA prioridad:** {domain_data['terminos_alta_prioridad']}  \n\n")

        # Listar términos
        for term_key, term_info in domain_data['terminos'].items():
            base = term_info['base']
            soc = term_info['soc_level']
            ext_type = term_info.get('extension_type', 'unknown')

            md.append(f"### {base['termino']}\n\n")
            md.append(f"**Definición:** {base['definicion']}\n\n")

            if base['ejemplos_basicos']:
                md.append("**Ejemplos:**\n")
                for ej in base['ejemplos_basicos']:
                    md.append(f"- {ej}\n")
                md.append("\n")

            # SOC-Level content
            md.append(f"#### 🔧 Herramientas (Extension: {ext_type})\n\n")
            if soc.get('tools'):
                for tool in soc['tools']:
                    md.append(f"**{tool.get('tool', 'N/A')}:**  \n")
                    md.append(f"- Propósito: {tool.get('purpose', 'N/A')}  \n")
                    md.append(f"- Comando: `{tool.get('command', 'N/A')}`  \n")
                    md.append(f"- Output: {tool.get('output', 'N/A')}  \n\n")
            else:
                md.append("*No hay herramientas específicas documentadas.*\n\n")

            # Log Analysis
            logs = soc.get('log_analysis', {})
            if logs.get('logs_to_check'):
                md.append("#### 📊 Log Analysis\n\n")
                md.append("**Logs a revisar:**\n")
                for log in logs['logs_to_check']:
                    md.append(f"- {log}\n")
                md.append("\n")

            if logs.get('ioc_patterns'):
                md.append("**IOC Patterns:**\n")
                for ioc in logs['ioc_patterns']:
                    md.append(f"- {ioc}\n")
                md.append("\n")

            if logs.get('example_log'):
                md.append("**Ejemplo de log:**\n```\n")
                md.append(logs['example_log'])
                md.append("\n```\n\n")

            # MITRE ATT&CK
            mitre = soc.get('mitre_attack', {})
            if mitre.get('relevant_techniques'):
                md.append("#### 🎭 MITRE ATT&CK\n\n")
                for tech in mitre['relevant_techniques']:
                    md.append(f"**{tech.get('technique', 'N/A')}**  \n")
                    md.append(f"- Tactic: {tech.get('tactic', 'N/A')}  \n")
                    md.append(f"- Relevance: {tech.get('relevance', 'N/A')}  \n")
                    md.append(f"- Detection: {tech.get('detection', 'N/A')}  \n\n")

            md.append("---\n\n")

    return ''.join(md)

if __name__ == "__main__":
    print("=" * 70)
    print("🚀 GENERADOR DE MATERIAL SOC-LEVEL COMPLETO")
    print("=" * 70)

    # 1. Fusionar diccionarios
    print("\n📦 PASO 1: Fusionando diccionario base + extensiones SOC...")
    merged_data = merge_dictionaries()

    # 2. Guardar JSON
    print("\n💾 PASO 2: Guardando JSON completo...")
    save_json(merged_data, OUTPUT_JSON_PATH)

    # 3. Generar Markdown
    print("\n📝 PASO 3: Generando Markdown legible...")
    markdown_content = generate_markdown(merged_data)
    save_markdown(markdown_content, OUTPUT_MD_PATH)

    # 4. Resumen final
    print("\n" + "=" * 70)
    print("✅ COMPLETADO CON ÉXITO")
    print("=" * 70)
    print(f"\n📄 Archivos generados:")
    print(f"   1. JSON: {OUTPUT_JSON_PATH}")
    print(f"   2. Markdown: {OUTPUT_MD_PATH}")
    print(f"\n📊 Estadísticas:")
    print(f"   - Términos ALTA prioridad: {merged_data['metadata']['high_priority_terms']}")
    print(f"   - Extensiones manuales: {merged_data['metadata']['manual_soc_extensions']}")
    print(f"   - Extensiones auto-generadas: {merged_data['metadata']['high_priority_terms'] - merged_data['metadata']['manual_soc_extensions']}")
    print("\n💡 Próximo paso: Revisar el Markdown y expandir términos críticos")
    print("=" * 70)
