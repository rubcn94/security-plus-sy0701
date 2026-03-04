# 📘 Security+ SY0-701 - Material SOC-Level COMPLETO

## 🎯 ¿Qué es esto?

Material de estudio Security+ **extendido a nivel operacional SOC Analyst** que va mucho más allá del exam prep estándar.

**Diferencia clave:**
- ❌ **Material normal Security+:** Definiciones teóricas para aprobar examen
- ✅ **Este material:** Comandos reales, logs, playbooks, casos reales, MITRE ATT&CK → **Nivel profesional**

---

## 📦 Archivos Principales

### 1. `SecPlus_SY0-701_SOC_COMPLETO.json`
- **Formato:** JSON estructurado
- **Contenido:** 220 términos HIGH priority con extensiones SOC
  - 8 términos con extensión **manual completa** (SIEM, EDR, Ransomware, APT, Phishing, SQLi, XSS, DDoS)
  - 212 términos con extensión **auto-generada inteligente**
- **Uso:** Programación, scripts, automation

### 2. `SecPlus_SY0-701_SOC_COMPLETO.md`
- **Formato:** Markdown legible
- **Contenido:** Mismo que JSON pero en formato lectura humana
- **Uso:** Estudio directo, imprimir, leer en móvil

### 3. `soc_extensions_database.json`
- **Formato:** JSON (base de datos extensible)
- **Contenido:** Solo extensiones SOC (separadas del diccionario base)
- **Uso:** **AGREGA AQUÍ** más términos manualmente

---

## 🔧 Estructura de Cada Término

Cada uno de los 220 términos HIGH priority incluye:

### 📚 Sección Base (exam-focused)
- Definición oficial Security+
- Ejemplos básicos
- Prioridad (ALTA)

### 🚀 Sección SOC-Level (profesional)

#### 1. **🔧 Herramientas y Comandos**
```bash
# Ejemplo real (de SIEM):
index=windows EventCode=4625 | stats count by src_ip, user | where count > 10
# Detecta brute force attacks
```

#### 2. **📊 Log Analysis**
- **Logs a revisar:** Event IDs específicos, rutas de archivos
- **IOC Patterns:** Qué buscar en los logs
- **Ejemplo de log real:** Con análisis incluido

#### 3. **🎭 MITRE ATT&CK Mapping**
- Tactic (ej: Initial Access)
- Technique (ej: T1566 - Phishing)
- Detection methods específicos

#### 4. **📋 Response Playbook**
Paso a paso de respuesta a incidentes:
1. Detection (< 1 min)
2. Triage (< 5 min)
3. Containment (< 15 min)
4. Investigation
5. Remediation
6. Lessons Learned

#### 5. **⚠️ False Positives**
- Escenarios comunes de FP
- Por qué se triggerea
- Cómo validar si es FP
- Tuning de reglas

#### 6. **🌍 Caso Real de Incidente**
- Incidente famoso relacionado (ej: WannaCry, Equifax, SolarWinds)
- Timeline del ataque
- Lessons learned
- Detection gaps

#### 7. **🔗 Enterprise Integration**
- Windows: Event IDs, comandos PowerShell
- Linux: paths, comandos bash
- Cloud AWS/Azure: servicios específicos
- Telemetría requerida
- Blind spots conocidos

---

## 🚀 Cómo Usar Este Material

### Opción 1: Estudio para Security+ Exam
1. Lee `SecPlus_SY0-701_SOC_COMPLETO.md`
2. Enfócate en secciones **Base** para exam prep teórico
3. Usa secciones **SOC-Level** para entender contexto real

### Opción 2: Preparación para Job Interview SOC
1. Lee términos con extensión **manual completa** (SIEM, EDR, Ransomware, APT, Phishing, SQLi, XSS, DDoS)
2. Practica comandos en labs (VirtualBox, AWS Free Tier)
3. Memoriza playbooks de respuesta (te preguntarán "¿qué harías si...?")

### Opción 3: Reference durante trabajo SOC
1. Usa JSON para buscar rápido: `Ctrl+F` en VSCode
2. Consulta playbooks cuando hay incidente real
3. Copia comandos directamente (ya están validados)

---

## 🎨 Cómo Expandir el Material

¿Quieres agregar más términos con extensión manual completa?

### Paso 1: Edita `soc_extensions_database.json`

Agrega un término nuevo siguiendo esta estructura:

```json
{
  "NOMBRE_TERMINO": {
    "tools": [
      {
        "tool": "nombre_herramienta",
        "purpose": "para qué sirve",
        "command": "comando real con flags",
        "output": "qué esperar en output"
      }
    ],
    "log_analysis": {
      "logs_to_check": ["Windows Event ID X", "Linux /var/log/X"],
      "ioc_patterns": ["Patrón 1", "Patrón 2"],
      "example_log": "LOG REAL aquí con análisis"
    },
    "mitre_attack": {
      "relevant_techniques": [
        {
          "tactic": "Tactic MITRE",
          "technique": "T#### - Nombre",
          "relevance": "Cómo se relaciona",
          "detection": "Cómo detectarlo"
        }
      ]
    },
    "response_playbook": {
      "scenario": "Escenario de incidente",
      "steps": [
        {
          "phase": "1. Detection",
          "actions": ["Acción 1", "Acción 2"]
        }
      ]
    },
    "false_positives": [
      {
        "scenario": "Escenario FP",
        "why_triggered": "Por qué",
        "how_to_validate": "Cómo validar",
        "tuning": "Cómo tunear"
      }
    ],
    "real_world_case": {
      "incident": "Nombre incidente real",
      "summary": "Resumen",
      "timeline": ["Evento 1", "Evento 2"],
      "lessons_learned": ["Lección 1"],
      "detection_gaps": ["Gap 1"]
    },
    "enterprise_integration": {
      "windows": "Info Windows",
      "linux": "Info Linux",
      "cloud_aws": "Info AWS",
      "cloud_azure": "Info Azure",
      "telemetry_required": ["Log 1", "Log 2"],
      "blind_spots": ["Blind spot 1"]
    }
  }
}
```

### Paso 2: Regenera archivos

```bash
cd D:\Users\cra\Desktop\Sec+
python merge_and_generate.py
```

Esto actualizará automáticamente:
- `SecPlus_SY0-701_SOC_COMPLETO.json`
- `SecPlus_SY0-701_SOC_COMPLETO.md`

---

## 📊 Estadísticas Actuales

| Métrica | Valor |
|---------|-------|
| Total términos diccionario base | 436 |
| Términos ALTA prioridad (Security+ críticos) | 220 |
| **Extensiones SOC manuales completas** | **8** |
| Extensiones SOC auto-generadas | 212 |
| Términos con extensión manual | SIEM, EDR, Ransomware, APT, Phishing, SQLi, XSS, DDoS |

---

## 🎯 Términos SOC Críticos Completados (8/50)

### ✅ Ya Completos
1. **SIEM** - Correlation, SPL/KQL queries, casos Target breach
2. **EDR** - Process injection, behavioral detection, NotPetya case
3. **Ransomware** - WannaCry case study, playbook completo
4. **APT** - SolarWinds supply chain, beaconing detection
5. **Phishing** - BEC, SPF/DKIM/DMARC, Google/Facebook $100M case
6. **SQLi** - sqlmap, ModSecurity, Sony Pictures breach
7. **XSS** - CSP, British Airways Magecart attack
8. **DDoS** - Mirai botnet, Dyn DNS 1.2 Tbps attack

### 🔄 Próximos Prioritarios (sugerencia)
9. IDS/IPS - Snort/Suricata rules
10. NGFW - Next-gen firewall features
11. Incident Response Phases - NIST framework
12. Chain of Custody - Forensics legal
13. MFA - Multi-factor auth bypass techniques
14. Brute Force Attack - Detection and response
15. MitM - Man-in-the-middle scenarios
16. DNS Spoofing - Cache poisoning
17. IoC - Indicator of Compromise hunting
18. MITRE ATT&CK - Framework usage
19. Firewall - Stateful vs stateless
20. VPN - IPSec, SSL/TLS configs

... (hasta completar 50+ términos críticos)

---

## 📚 Recursos Adicionales

### Para Practicar Comandos
- **Labs:** TryHackMe, HackTheBox, CyberDefenders
- **VMs:** Security Onion, SIFT Workstation, REMnux
- **Cloud:** AWS Free Tier, Azure Free Account

### Para Threat Intel
- **MITRE ATT&CK:** https://attack.mitre.org
- **AlienVault OTX:** https://otx.alienvault.com
- **VirusTotal:** https://virustotal.com

### Para Log Analysis
- **Splunk Free:** 500MB/day license
- **ELK Stack:** Elasticsearch + Kibana
- **Graylog:** Open source SIEM

---

## 🤝 Contribuir

Este material está diseñado para ser **extensible**. Si encuentras:
- Comandos mejores
- Casos reales más relevantes
- Errores en playbooks

→ Edita `soc_extensions_database.json` y regenera.

---

## ⚖️ Disclaimer

Este material es para **propósitos educativos** y preparación profesional.

- **NO uses** técnicas ofensivas (SQLi, XSS, DDoS) en sistemas sin autorización
- **SÍ practica** en labs controlados (TryHackMe, HackTheBox, tu propio homelab)
- **SÍ estudia** casos reales para aprender de errores de otros

---

## 📧 Soporte

Este material fue generado para acelerar tu preparación Security+ y nivel SOC.

**Generado:** 2026-03-04
**Versión:** 4.0 - SOC Professional
**Target Audience:** SOC Analyst L1/L2, Security+, Entry-level Security Engineer

---

**¡Buena suerte en tu examen Security+ y en tu carrera en ciberseguridad! 🚀**
