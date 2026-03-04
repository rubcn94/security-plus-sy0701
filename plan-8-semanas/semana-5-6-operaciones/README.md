# SEMANA 5-6: OPERACIONES DE SEGURIDAD (Dominio 4)

## ⚠️ DOMINIO MÁS IMPORTANTE - 28% DEL EXAMEN ⚠️

## OBJETIVOS DE APRENDIZAJE

**Dominio 4: Operaciones de Seguridad (28% del examen)**
- Monitoreo y logging (SIEM, logs, alertas)
- Respuesta a incidentes (fases, forensics, chain of custody)
- Análisis de vulnerabilidades (Nmap, OpenVAS, Nessus)
- Hardening de sistemas (CIS benchmarks, patching)
- Seguridad móvil y endpoint (MDM, EDR, DLP)
- Automation y orchestration (SOAR, playbooks)

---

## MATERIALES DISPONIBLES EN ESTA CARPETA

### Laboratorios Prácticos (3 labs - ~7 horas)
- [ ] LAB-4.1_Hardening_de_Servidor_Linux_con_CIS_Benchmarks.txt (2h)
- [ ] LAB-4.2_Respuesta_a_Incidentes_-_Análisis_Forense.txt (3h) **CRÍTICO**
- [ ] LAB-4.3_SIEM_con_Wazuh_-_Detección_y_Alertas.txt (2h)

### Guías de Referencia
- [ ] CHEAT_SHEET_COMANDOS_PBQs.md - **Sección completa de troubleshooting**
- [ ] GUIA_ANALISIS_LOGS.md - **LOS 20 EJEMPLOS** (este es el dominio de logs)
- [ ] EJERCICIOS_CALCULOS_PRACTICOS.md - CVSS (ejercicios 6-7)

### Flashcards (en carpeta principal)
- Revisar términos ALTA prioridad de D4 (aprox. 65 términos - EL MÁS EXTENSO)
- Archivo: `../Flashcards/SecPlus_Flashcards_Interactivo.html`

---

## PLAN DE ESTUDIO DIARIO (14 días)

### SEMANA 5 (Respuesta a Incidentes y Forense)

#### Día 29: Respuesta a Incidentes - Teoría
- [ ] **Teoría (2h)**: Flashcards D4 - 6 fases IR (Preparation → Lessons Learned)
- [ ] **Memorizar orden**: Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned
- [ ] **Total**: 2h

**CRÍTICO**: El orden de las fases IR es una pregunta CASI SEGURA en el examen.

#### Día 30: Análisis Forense - Volatilidad
- [ ] **Teoría (1.5h)**: Flashcards D4 - Orden de volatilidad, chain of custody
- [ ] **Memorizar**: CPU/cache → RAM → Red → Procesos → Temp → Disco → Logs → Backups
- [ ] **Comandos (1h)**: CHEAT_SHEET - dd, certutil, hash validation
- [ ] **Total**: 2.5h

#### Día 31: LAB Respuesta a Incidentes
- [ ] **LAB (3h)**: LAB-4.2 - Análisis Forense COMPLETO **NO SALTAR**
- [ ] **Repaso (30min)**: Revisar pasos ejecutados
- [ ] **Total**: 3.5h

#### Día 32: Análisis de Logs - Parte 1
- [ ] **Teoría (1h)**: Flashcards D4 - Tipos de logs (syslog, Windows Event)
- [ ] **Práctica (2h)**: GUIA_ANALISIS_LOGS - Ejemplos 1-5
  - Ejemplo 1: Brute Force SSH
  - Ejemplo 2: SQL Injection
  - Ejemplo 3: Privilege Escalation
  - Ejemplo 4: Data Exfiltration
  - Ejemplo 5: Lateral Movement
- [ ] **Total**: 3h

#### Día 33: Análisis de Logs - Parte 2
- [ ] **Práctica (2.5h)**: GUIA_ANALISIS_LOGS - Ejemplos 6-10
  - Ejemplo 6: Ransomware
  - Ejemplo 7: DDoS
  - Ejemplo 8: Phishing
  - Ejemplo 9: DNS Tunneling
  - Ejemplo 10: Pass-the-Hash
- [ ] **Total**: 2.5h

#### Día 34: Análisis de Logs - Parte 3
- [ ] **Práctica (2.5h)**: GUIA_ANALISIS_LOGS - Ejemplos 11-15
  - Ejemplo 11: Port Scan
  - Ejemplo 12: Insider Threat
  - Ejemplo 13: Cryptojacking
  - Ejemplo 14: XSS Attack
  - Ejemplo 15: Account Lockout
- [ ] **Total**: 2.5h

#### Día 35: Análisis de Logs - Parte 4 + Ejercicios
- [ ] **Práctica (2h)**: GUIA_ANALISIS_LOGS - Ejemplos 16-20
  - Ejemplo 16: MITM
  - Ejemplo 17: Scheduled Task Persistence
  - Ejemplo 18: Cloud Misconfiguration
  - Ejemplo 19: Credential Stuffing
  - Ejemplo 20: Fileless Malware
- [ ] **Ejercicios (1h)**: 3 ejercicios prácticos de análisis
- [ ] **Total**: 3h

---

### SEMANA 6 (SIEM, Hardening, Vulnerabilidades)

#### Día 36: SIEM y Correlación
- [ ] **Teoría (1.5h)**: Flashcards D4 - SIEM, SOAR, correlation rules
- [ ] **LAB (2h)**: LAB-4.3 - SIEM con Wazuh
- [ ] **Total**: 3.5h

#### Día 37: Hardening - Linux
- [ ] **Teoría (1h)**: Flashcards D4 - CIS benchmarks, least privilege
- [ ] **LAB (2h)**: LAB-4.1 - Hardening Servidor Linux
- [ ] **Comandos (1h)**: CHEAT_SHEET - permisos, usuarios, servicios
- [ ] **Total**: 4h

#### Día 38: Hardening - Windows
- [ ] **Teoría (1.5h)**: Flashcards D4 - GPO, LAPS, AppLocker
- [ ] **Comandos (1.5h)**: CHEAT_SHEET - gpupdate, whoami, net user
- [ ] **Logs (1h)**: Windows Event IDs (4624, 4625, 4672, 4688)
- [ ] **Total**: 4h

#### Día 39: Vulnerabilidades - Scanning
- [ ] **Teoría (1.5h)**: Flashcards D4 - Nmap, OpenVAS, Nessus
- [ ] **Comandos (1.5h)**: CHEAT_SHEET - Nmap (SYN, version, scripts)
- [ ] **Ejercicios (1h)**: EJERCICIOS_CALCULOS - CVSS (ej. 6-7)
- [ ] **Total**: 4h

#### Día 40: Patch Management
- [ ] **Teoría (1.5h)**: Flashcards D4 - Patch cadence, testing, rollback
- [ ] **Práctica (1h)**: Priorizar parches según CVSS
- [ ] **Total**: 2.5h

#### Día 41: Seguridad Móvil y Endpoint
- [ ] **Teoría (2h)**: Flashcards D4 - MDM, MAM, EDR, DLP
- [ ] **Práctica (1h)**: Configuraciones MDM
- [ ] **Total**: 3h

#### Día 42: Repaso D4 Completo
- [ ] **Repaso flashcards D4 (2h)**: TODOS los términos ALTA (~65)
- [ ] **Repaso logs (1h)**: Revisar 20 ejemplos (solo IOCs)
- [ ] **Orden IR (30min)**: Memorizar fases + volatilidad
- [ ] **Total**: 3.5h

---

## RECURSOS ADICIONALES

### Windows Event IDs (MEMORIZAR)

| Event ID | Descripción | Gravedad |
|----------|-------------|----------|
| 4624 | Logon exitoso | INFO |
| 4625 | Logon fallido | WARNING |
| 4672 | Privilegios especiales asignados | CRITICAL |
| 4688 | Nuevo proceso creado | INFO |
| 4698 | Tarea programada creada | WARNING |
| 4720 | Usuario creado | CRITICAL |
| 4732 | Usuario añadido a grupo | CRITICAL |
| 4740 | Cuenta bloqueada | WARNING |
| 7045 | Servicio instalado | WARNING |

### Orden Fases Respuesta a Incidentes (IR)
```
1. PREPARATION
   - Políticas, herramientas, training

2. IDENTIFICATION
   - Detectar anomalía, clasificar severidad

3. CONTAINMENT
   - Aislar host, prevenir propagación

4. ERADICATION
   - Eliminar malware, cerrar vulnerabilidad

5. RECOVERY
   - Restaurar sistemas, monitorear

6. LESSONS LEARNED
   - Documentar, actualizar procedimientos
```

### Orden de Volatilidad (Forense)
```
1. Registros CPU, caché
2. Memoria RAM (dump)
3. Estado de red (conexiones activas)
4. Procesos en ejecución
5. Archivos temporales
6. Disco duro
7. Logs remotos
8. Backups
```

---

## CHECKLIST SEMANAL

### Semana 5 (IR, Forense, Logs)
- [ ] Memorizar orden fases IR (6 fases)
- [ ] Memorizar orden volatilidad (8 niveles)
- [ ] Completar LAB-4.2 (respuesta a incidentes)
- [ ] Analizar LOS 20 EJEMPLOS de logs
- [ ] Completar 3 ejercicios prácticos de análisis
- [ ] **Meta**: Poder analizar cualquier log e identificar ataque

### Semana 6 (SIEM, Hardening, Vulns)
- [ ] Completar LAB-4.1 (hardening Linux)
- [ ] Completar LAB-4.3 (SIEM)
- [ ] Dominar comandos Nmap (5 tipos scan)
- [ ] Interpretar CVSS scores (2 ejercicios)
- [ ] Memorizar Windows Event IDs (9 críticos)
- [ ] **Meta**: Dominar 100% términos ALTA de D4

---

## CRITERIOS DE ÉXITO

Al finalizar estas 2 semanas deberías poder:

**Respuesta a Incidentes:**
- [ ] Recitar orden correcto de las 6 fases IR
- [ ] Recitar orden de volatilidad para recolección forense
- [ ] Explicar chain of custody y por qué es crítico
- [ ] Ejecutar respuesta completa a incidente (LAB-4.2)

**Análisis de Logs:**
- [ ] Identificar 20 tipos de ataques en logs (brute force, SQLi, XSS, etc.)
- [ ] Leer Windows Event Logs y correlacionar eventos
- [ ] Detectar lateral movement, privilege escalation, persistence
- [ ] Usar Wireshark para analizar tráfico sospechoso

**SIEM y Hardening:**
- [ ] Configurar SIEM con correlation rules
- [ ] Aplicar CIS benchmarks a Linux
- [ ] Configurar GPO para hardening Windows
- [ ] Implementar least privilege y separation of duties

**Vulnerabilidades:**
- [ ] Ejecutar Nmap scan completo (SYN, version, scripts)
- [ ] Interpretar scores CVSS y priorizar remediación
- [ ] Diseñar proceso patch management
- [ ] Diferenciar EDR, MDM, MAM, DLP

---

## EJERCICIOS PRÁCTICOS CLAVE

### Ejercicio 1: Análisis de Incidente Completo
**Escenario**: Servidor web comprometido, detectado por SIEM.

**Tu tarea**:
1. Seguir las 6 fases IR
2. Recolectar evidencia (orden volatilidad)
3. Analizar logs (Apache + Windows Events)
4. Identificar IOCs
5. Crear report

**Tiempo**: 2 horas (LAB-4.2 cubre esto)

### Ejercicio 2: Log Analysis Speed Challenge
**Archivo**: GUIA_ANALISIS_LOGS.md

**Tu tarea**: Para cada uno de los 20 ejemplos:
1. Identificar tipo de ataque (< 30 segundos)
2. Listar 3 IOCs (< 1 minuto)
3. Recomendar 2 acciones (< 1 minuto)

**Objetivo**: Poder analizar cada log en < 3 minutos total

### Ejercicio 3: Priorización de Vulnerabilidades
**Del archivo** EJERCICIOS_CALCULOS_PRACTICOS.md - Ejercicios 6-7

**Escenario**: 10 vulnerabilidades detectadas con diferentes CVSS scores.

**Tu tarea**: Priorizar remediación basado en CVSS + criticidad asset

---

## NOTAS IMPORTANTES

1. **D4 = 28% del examen**: Es el dominio MÁS PESADO
2. **PBQs de logs**: Casi seguro tendrás PBQ de analizar logs/eventos
3. **Orden IR**: Pregunta casi segura (memoriza las 6 fases)
4. **Orden volatilidad**: Pregunta casi segura (memoriza los 8 niveles)
5. **Windows Event IDs**: Conoce al menos los 9 críticos
6. **Labs D4**: NO SALTES NINGUNO, son los más importantes de todo el curso

---

## COMANDOS CLAVE PARA MEMORIZAR

### Troubleshooting Conectividad (CRÍTICO para PBQs)
```
1. ping 127.0.0.1       # Stack TCP/IP local
2. ping <IP_local>      # Interfaz local
3. ping <Gateway>       # Conexión a router
4. ping 8.8.8.8         # Salida a Internet
5. nslookup google.com  # DNS
```

### Linux - Análisis de Procesos
```bash
ps aux                          # Listar todos los procesos
ps aux | grep malware           # Buscar proceso específico
top                             # Monitor tiempo real
lsof -i -P -n                   # Conexiones + procesos
netstat -antp | grep ESTABLISHED # Conexiones activas
```

### Linux - Logs
```bash
tail -f /var/log/auth.log       # Ver log en tiempo real
grep "Failed password" /var/log/auth.log  # Buscar intentos fallidos
journalctl -u ssh -f            # Ver logs SSH (systemd)
journalctl --since "1 hour ago" # Logs última hora
```

### Windows - Logs
```cmd
eventvwr                        # Abrir Event Viewer
wevtutil qe Security /c:10 /rd:true /f:text  # Últimos 10 eventos Security
```

### Nmap (Reconnaissance)
```bash
nmap 192.168.1.1                # Scan básico (top 1000 puertos)
nmap -sS 192.168.1.1            # SYN scan (stealth)
nmap -sV 192.168.1.1            # Detectar versiones servicios
nmap -O 192.168.1.1             # Detectar OS
nmap -A 192.168.1.1             # Aggressive scan (OS, version, scripts)
nmap --script vuln 192.168.1.1  # Scan vulnerabilidades
```

---

## TROUBLESHOOTING

**Si vas atrasado:**
- Prioriza LAB-4.2 (IR) sobre todo
- Analiza solo ejemplos 1-10 de logs (los más comunes)
- Memoriza orden IR y volatilidad (son preguntas casi seguras)
- Salta LAB-4.1 si es necesario (hardening)

**Si vas adelantado:**
- Analiza los 20 ejemplos de logs 2 veces (primera identificar, segunda speed challenge)
- Añade términos MEDIA de D4
- Practica más con Wireshark (filtros avanzados)
- Configura SIEM real (ELK Stack o Splunk free)

**Si algo no se entiende:**
- Logs confusos: enfócate en fechas/horas, IPs, usuarios, eventos anómalos
- SIEM: piensa en "correlation" = conectar eventos relacionados
- Forense: el orden importa (volatilidad es clave)

---

## RECURSOS EXTERNOS RECOMENDADOS

**Práctica de Logs:**
- Cyberdefenders.org (Blue Team challenges)
- TryHackMe "Investigating Windows" rooms

**SIEM:**
- Wazuh documentation (free SIEM)
- Splunk Fundamentals (free course)

**Forense:**
- SANS Poster "Incident Handler's Handbook"
- Order of Volatility diagrams

---

**SIGUIENTE PASO**: Al terminar el día 42, pasa a `Semana_7-8_Governance_D5_Repaso/`

**FELICITACIONES**: Has completado el dominio MÁS DIFÍCIL. D5 es más teórico y el repaso final te preparará para 85%+.
