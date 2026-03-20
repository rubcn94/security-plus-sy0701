# Labs Prácticos — Roadmap Post Security+

## Por qué labs > teoría en esta fase
- Security+ ya demuestra que sabes los conceptos
- Los reclutadores de security miran GitHub y perfiles HTB/THM
- Los labs son portfolio directo en el CV y LinkedIn
- HTB/THM: setup 0 minutos, puedes empezar hoy

---

## FASE 1 — Empezar aquí (gratis, 1-2 semanas)

### flaws.cloud — AWS misconfigurations reales
**URL:** http://flaws.cloud
**Tiempo:** 2-3 días
**Qué aprenderás:**
- S3 buckets públicos y misconfiguraciones comunes
- Metadata service (IMDS) abuse
- IAM privilege escalation
- Snapshot y AMI exposure
**Por qué:** Creado por Scott Piper (experto AWS security). Referente en entrevistas.

### flaws2.cloud — Attacker + Defender
**URL:** http://flaws2.cloud
**Tiempo:** 2-3 días
**Qué aprenderás:**
- Mismo contenido pero desde perspectiva de defensa
- CloudTrail analysis, GuardDuty alerts
- Detectar ataques en logs reales
**Por qué:** Completa el anterior. Muestra la misma vulnerabilidad desde ambos lados.

---

## FASE 2 — TryHackMe (cuenta gratuita suficiente para empezar)

**URL:** https://tryhackme.com
**Perfil público** visible en LinkedIn → poner URL en CV

### Path recomendado: SOC Level 1
**URL:** https://tryhackme.com/path/outline/soclevel1
**Tiempo estimado:** ~40 horas (~4-6 semanas a ritmo parcial)
**Módulos clave:**
- Cyber Defense Frameworks (MITRE ATT&CK, Pyramid of Pain, Unified Kill Chain)
- Cyber Threat Intelligence (OpenCTI, MISP, threat feeds)
- Network Security & Traffic Analysis (Wireshark, Zeek, Snort)
- Endpoint Security Monitoring (Core Windows Processes, Sysinternals, Sysmon)
- Security Information & Event Management (Splunk, ELK Stack)
- Digital Forensics & Incident Response (Volatility, Redline, Autopsy)
- Phishing Analysis

**Certificación al completar:** SOC Level 1 Certificate — poner en LinkedIn

### Path complementario: Pre-Security
Si necesitas reforzar networking antes del SOC path:
**URL:** https://tryhackme.com/path/outline/presecurity

### Módulos sueltos de alto valor (cloud + blue team)
- **AWS** (si disponible en THM): búscar "cloud" en la búsqueda
- **Splunk** rooms — SIEM muy demandado en el mercado
- **Wireshark** rooms — análisis de tráfico
- **Active Directory Basics** — imprescindible para blue team

---

## FASE 3 — HackTheBox (cuando tengas base)

**URL:** https://app.hackthebox.com
**Modo:** HTB Academy (guiado) + HTB Labs (máquinas individuales)

### HTB Academy — Módulos de Blue Team / Cloud
**URL:** https://academy.hackthebox.com

| Módulo | Relevancia |
|---|---|
| SOC Analyst Path | Blue team completo |
| Introduction to Cloud Security | AWS/Azure/GCP security |
| Active Directory Enumeration & Attacks | Movimiento lateral, AD attacks |
| SIEM & Log Analysis | Splunk, ELK |
| Incident Handling Process | IR metodología |
| Introduction to Web Application Security | Para entender ataques que luego defienden |

### Certificación HTB CDSA (Certified Defensive Security Analyst)
**Relevancia:** Alta. Específica de blue team / SOC. Valorada por empresas de seguridad europeas.
**Cuándo:** Después de completar el SOC path en HTB Academy.

### Máquinas recomendadas para empezar (blue team focus)
- **Sherlock challenges** en HTB (forensics y blue team) — buscar en el apartado Challenges
- Máquinas **Easy/Medium** con etiqueta "forensics" o "cloud"

---

## FASE 4 — CloudGoat (AWS hands-on con tu propia cuenta)

**URL:** https://github.com/RhinoSecurityLabs/cloudgoat
**Requisito:** Cuenta AWS Free Tier
**Tiempo:** 1 semana por scenario

### Scenarios por orden de dificultad

| Scenario | Dificultad | Qué enseña |
|---|---|---|
| `iam_privesc_by_rollback` | Fácil | IAM privilege escalation |
| `cloud_breach_s3` | Fácil | S3 misconfiguration, SSRF |
| `iam_privesc_by_attachment` | Media | IAM policy abuse |
| `vulnerable_cognito` | Media | Cognito misconfiguration |
| `detection_evasion` | Difícil | Evasión de GuardDuty/CloudTrail |
| `lambda_privesc` | Media | Lambda role abuse |
| `ecs_efs_attack` | Difícil | Container security, EFS |

**Setup:**
```bash
pip install cloudgoat
cloudgoat config profile  # configura AWS credentials
cloudgoat create iam_privesc_by_rollback
```

---

## FASE 5 — Proyecto propio en GitHub

**Cuándo:** Mientras haces las fases anteriores
**Objetivo:** UN proyecto bien documentado > 5 proyectos mediocres

### Ideas concretas ordenadas por impacto/esfuerzo

**Nivel básico (1-2 semanas):**
- Script Python que audita Security Groups de AWS buscando puertos abiertos a 0.0.0.0/0
- Script que lista buckets S3 públicos en una cuenta
- Analizador de logs CloudTrail que detecta patrones sospechosos (muchos AssumeRole, DeleteTrail, etc.)

**Nivel medio (2-4 semanas):**
- Dashboard HTML que visualiza findings de GuardDuty/Security Hub (leer via API, mostrar en HTML)
- Playbook SOAR básico en Python: recibe un alerta de GuardDuty → consulta threat intel → crea ticket en GitHub Issues
- Herramienta de hardening: evalúa una cuenta AWS contra CIS Benchmark y genera report

**Nivel avanzado:**
- Honeypot AWS: instancia EC2 con credenciales fake que alerta cuando alguien las usa (honeytoken)
- SIEM casero: agrega VPC Flow Logs + CloudTrail → ElasticSearch → Kibana dashboard

### Cómo documentar el proyecto
```
README.md debe incluir:
- Qué hace el proyecto (2-3 líneas)
- Por qué lo hice (aprendizaje, gap que cubre)
- Arquitectura / diagrama si aplica
- Screenshots del output
- Cómo instalarlo y usarlo (comandos exactos)
- Lo que aprendí / limitaciones conocidas
```

---

## PLATAFORMAS ADICIONALES

| Plataforma | Para qué | Precio |
|---|---|---|
| **PentesterLab** | Web app security, API testing | Freemium |
| **PortSwigger Web Academy** | OWASP Top 10 labs interactivos | Gratis |
| **Immersive Labs** | Blue team, threat intel | Gratis con algunas cuentas |
| **SANS Cyber Aces** | Fundamentos gratis de SANS | Gratis |
| **AWS Skill Builder** | Labs oficiales de AWS | Freemium |
| **Pwn.college** | Sistemas, binarios | Gratis |

---

## TIMELINE SUGERIDO POST-SECURITY+

| Semana | Actividad |
|---|---|
| 1-2 | flaws.cloud + flaws2.cloud |
| 3-6 | TryHackMe SOC Level 1 path |
| 7-10 | HTB Academy — SOC path + CloudGoat scenarios |
| 11-12 | Empezar proyecto GitHub |
| 13-16 | AWS SAA-C03 (base para AWS Security) |
| 17-24 | AWS Security Specialty SCS-C02 |

---

## QUÉ PONER EN EL CV / LINKEDIN

```
Certificaciones:
- CompTIA Security+ SY0-701 (marzo 2026)
- TryHackMe SOC Level 1 (fecha)
- AWS Solutions Architect Associate (fecha) [si aplica]
- AWS Security Specialty SCS-C02 (fecha)

Proyectos:
- [nombre del proyecto] — github.com/ruben/...
  Descripción de 1 línea. Stack: Python, AWS, boto3.

Perfil TryHackMe: https://tryhackme.com/p/...
```
