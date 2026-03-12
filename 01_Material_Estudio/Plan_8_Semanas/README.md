# PLAN DE ESTUDIO 8 SEMANAS - Security+ SY0-701

## 🎯 OBJETIVO: 85%+ EN EL EXAMEN

Este directorio contiene TODO el material organizado por semanas para aprobar el Security+ SY0-701 con 85%+ de score.

---

## ESTRUCTURA DEL PLAN

```
Plan_8_Semanas/
├── Semana_1-2_Fundamentos_D1-D2/        (Conceptos + Amenazas - 34%)
├── Semana_3-4_Arquitectura_D3/          (Diseño Seguro - 18%)
├── Semana_5-6_Operations_D4/            (Operaciones - 28% ¡MÁS PESADO!)
└── Semana_7-8_Governance_D5_Repaso/     (Governance + Repaso - 20%)
```

Cada carpeta contiene:
- **Laboratorios prácticos** (3-5 labs por dominio)
- **Guías de referencia** (comandos, logs, cálculos)
- **README.md** con plan diario detallado

---

## CÓMO USAR ESTE PLAN

### Opción 1: Seguir el plan completo (8 semanas)
1. Empieza por `Semana_1-2_Fundamentos_D1-D2/README.md`
2. Sigue el plan día a día (2-3 horas/día)
3. Completa TODOS los labs y ejercicios
4. Avanza secuencialmente a las siguientes semanas
5. **Tiempo total**: ~130 horas

### Opción 2: Plan acelerado (4 semanas)
1. Salta labs opcionales (marca prioridad en cada README)
2. Enfócate solo en flashcards ALTA (220 términos)
3. Analiza solo 10 ejemplos de logs (en vez de 20)
4. Reduce ejercicios de cálculo a básicos
5. **Tiempo total**: ~60 horas

### Opción 3: Plan ultra-rápido (2 semanas)
1. **NO RECOMENDADO** a menos que tengas experiencia previa
2. Solo flashcards ALTA (220 términos)
3. Labs críticos: LAB-1.2, LAB-2.1, LAB-3.1, LAB-4.2, LAB-5.1
4. Análisis logs: ejemplos 1, 2, 6, 8, 13, 15
5. **Tiempo total**: ~40 horas

---

## DISTRIBUCIÓN POR DOMINIO

| Dominio | Peso Examen | Semanas | Horas Estudio | Flashcards ALTA |
|---------|-------------|---------|---------------|-----------------|
| D1: Conceptos Generales | 12% | 1 | 15h | ~35 |
| D2: Amenazas y Mitigaciones | 22% | 1 | 20h | ~45 |
| D3: Arquitectura | 18% | 2 | 25h | ~50 |
| D4: Operaciones | **28%** | 2 | **40h** | ~65 |
| D5: Governance | 20% | 1 | 15h | ~50 |
| Repaso Final | - | 1 | 15h | 220 (todos) |
| **TOTAL** | **100%** | **8** | **130h** | **220** |

**Nota**: D4 es el dominio más importante (28% del examen) - dedícale el mayor esfuerzo.

---

## MATERIALES INCLUIDOS EN CADA SEMANA

### Laboratorios Prácticos (15 labs totales - ~17 horas)
Cada lab incluye:
- Objetivos claros
- Pasos detallados
- Comandos completos
- Troubleshooting
- Validación de resultados

### Guías de Referencia
- **CHEAT_SHEET_COMANDOS_PBQs.md**: Comandos Windows/Linux/Wireshark (IMPRIME Y LLEVA AL EXAMEN)
- **GUIA_ANALISIS_LOGS.md**: 20 ejemplos reales de ataques con IOCs y remediación
- **EJERCICIOS_CALCULOS_PRACTICOS.md**: 12 ejercicios con soluciones (ALE, CVSS, subnetting, RTO/RPO)

### Flashcards (en carpeta principal)
- **HTML interactivo**: `01_Material_Estudio/Flashcards/SecPlus_Flashcards_Interactivo.html`
- **PDF completo**: `01_Material_Estudio/PDFs_Estudio/SecPlus_Flashcards_COMPLETO_382.pdf`
- **Anki CSV**: `01_Material_Estudio/Flashcards/SecPlus_382_Flashcards.csv`

---

## CRONOGRAMA DETALLADO

### SEMANA 1-2: FUNDAMENTOS (D1+D2)
**Objetivo**: Dominar conceptos básicos y amenazas

**Qué aprenderás**:
- CIA Triad, AAA, Zero Trust
- Criptografía (simétrico, asimétrico, hashing)
- PKI y certificados
- Tipos de malware y vectores de ataque
- MITRE ATT&CK framework

**Labs críticos**:
- LAB-1.2: Zero Trust con VPN y MFA
- LAB-2.1: Análisis de Malware con Sandboxing

**Meta**: 100% términos ALTA de D1+D2 (~80 flashcards)

---

### SEMANA 3-4: ARQUITECTURA (D3)
**Objetivo**: Diseñar arquitecturas seguras

**Qué aprenderás**:
- Segmentación de red (VLANs, DMZ, subnetting)
- Firewalls y reglas ACL
- IDS/IPS (Suricata, Snort)
- Seguridad cloud (IaaS/PaaS/SaaS, responsabilidad compartida)
- Resiliencia (RAID, backups, RPO/RTO)

**Labs críticos**:
- LAB-3.1: Firewall y Segmentación de Red
- LAB-3.2: IDS/IPS con Suricata + ELK Stack

**Cálculos**: Subnetting (MEMORIZAR /24, /26, /27, /28, /30)

**Meta**: Poder diseñar arquitectura de red completa en < 30 min

---

### SEMANA 5-6: OPERACIONES (D4) ⚠️ MÁS IMPORTANTE
**Objetivo**: Dominar operaciones de seguridad (28% del examen)

**Qué aprenderás**:
- Respuesta a incidentes (6 fases IR)
- Análisis forense (orden de volatilidad)
- Análisis de logs (20 ejemplos de ataques reales)
- SIEM y correlación (Wazuh, Splunk)
- Hardening (CIS benchmarks, GPO)
- Vulnerability scanning (Nmap, OpenVAS)

**Labs críticos**:
- LAB-4.2: Respuesta a Incidentes - Análisis Forense (NO SALTAR)
- LAB-4.3: SIEM con Wazuh

**Memorizar**:
- Orden IR: Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned
- Orden volatilidad: CPU/cache → RAM → Red → Procesos → Temp → Disco → Logs → Backups
- Windows Event IDs: 4624, 4625, 4672, 4688, 4698, 4720, 4732, 4740, 7045

**Meta**: Analizar cualquier log e identificar ataque en < 3 min

---

### SEMANA 7-8: GOVERNANCE + REPASO (D5)
**Objetivo**: Governance y preparación final para 85%+

**Qué aprenderás**:
- Análisis de riesgos (SLE, ALE, ARO, ROI)
- Compliance (GDPR, HIPAA, PCI DSS, SOX)
- Frameworks (ISO 27001, NIST CSF, CIS Controls)
- Business continuity (RTO, RPO, MTTR, MTBF)

**Labs críticos**:
- LAB-5.1: Cálculo ALE-SLE-ARO

**Repaso final**:
- Día 50: Repaso D1+D2
- Día 51: Repaso D3
- Día 52-53: Repaso D4 (logs + comandos)
- Día 54: Repaso D5 + cálculos
- Día 55: Simulacro completo 90 preguntas
- Día 56: Descanso activo
- **Día 57: EXAMEN REAL**

**Meta**: 85%+ en simulacro = LISTO PARA EXAMEN

---

## FÓRMULAS Y CONCEPTOS CRÍTICOS

### Risk Management (CASI SEGURO en examen)
```
SLE = Asset Value × Exposure Factor
ALE = SLE × ARO
ROI = (ALE_before - ALE_after - Cost) / Cost × 100%
```

### Subnetting (CASI SEGURO en examen)
```
Hosts = 2^(32 - CIDR) - 2

/24 = 254 hosts
/26 = 62 hosts
/28 = 14 hosts
/30 = 2 hosts (enlaces punto-a-punto)
```

### Business Continuity
```
RTO = Tiempo máximo aceptable de downtime
RPO = Pérdida máxima aceptable de datos
MTTR = Downtime total / Número reparaciones
MTBF = Uptime / Número fallos
Availability = (Total_Time - Downtime) / Total_Time × 100%
```

### Incident Response (CASI SEGURO en examen)
```
1. Preparation
2. Identification
3. Containment
4. Eradication
5. Recovery
6. Lessons Learned
```

### Order of Volatility (CASI SEGURO en examen)
```
1. CPU, caché
2. Memoria RAM
3. Estado de red
4. Procesos
5. Archivos temporales
6. Disco duro
7. Logs remotos
8. Backups
```

---

## CHECKLIST PRE-EXAMEN

### ¿Estás listo? Verifica que puedes:

**Cálculos (sin calculadora):**
- [ ] Calcular ALE en < 1 minuto
- [ ] Calcular subnetting en < 2 minutos
- [ ] Interpretar CVSS score (0-10 scale)
- [ ] Calcular availability percentage

**Memoria:**
- [ ] Recitar 6 fases IR de memoria
- [ ] Recitar orden volatilidad (8 niveles)
- [ ] Listar 9 Windows Event IDs críticos
- [ ] Explicar CIA Triad, AAA, Zero Trust

**Práctico:**
- [ ] Leer log y identificar tipo de ataque
- [ ] Crear reglas firewall (iptables, ufw, netsh)
- [ ] Usar Wireshark filters (ip.addr, tcp.port, tcp.flags)
- [ ] Troubleshoot conectividad (5 pasos)

**Conceptual:**
- [ ] Comparar IDS vs IPS
- [ ] Explicar modelo responsabilidad compartida cloud
- [ ] Diferenciar GDPR/HIPAA/PCI DSS
- [ ] Mapear ataque a MITRE ATT&CK

---

## ESTRATEGIA PARA EL EXAMEN

### Timing
- **90 preguntas en 90 minutos** = 1 min/pregunta
- **PBQs**: 5-10 minutos cada una
- **Múltiple-choice**: 30-45 segundos cada una

### Orden Recomendado
1. **Lee todas las PBQs** (5 min) - márcalas para después
2. **Responde las 90 múltiple-choice** (60 min)
3. **Vuelve a PBQs** con tiempo restante (25 min)
4. **Revisa marcadas** (10 min)

### Técnicas
- **Elimina incorrectas**: Descarta 2 opciones primero
- **Lee con cuidado**: "EXCEPT", "LEAST", "NOT" cambian todo
- **No cambies respuestas** a menos que estés SEGURO
- **No dejes en blanco**: No hay penalización por fallar

---

## RECURSOS ADICIONALES

### Dentro de este material
- **Flashcards HTML**: `01_Material_Estudio/Flashcards/SecPlus_Flashcards_Interactivo.html`
- **PDF Flashcards**: `01_Material_Estudio/PDFs_Estudio/SecPlus_Flashcards_COMPLETO_382.pdf`
- **150 Preguntas**: `01_Material_Estudio/Preguntas_Practica/SecPlus_150_Preguntas_Prioridad_ALTA.md`
- **Mapas conceptuales**: `01_Material_Estudio/Mapas_Conceptuales/`
- **Objetivos oficiales**: `03_PDFs_Referencia/comptia-security-plus-sy0-701-exam-objectives.pdf`

### Externos recomendados
- **Professor Messer**: Videos gratis en YouTube (SY0-701)
- **Jason Dion**: Practice exams en Udemy
- **Cyberdefenders.org**: Blue Team challenges (logs)
- **TryHackMe**: Hands-on security labs

---

## TROUBLESHOOTING

### "Voy atrasado"
- Salta labs opcionales (cada README indica prioridad)
- Enfócate solo en flashcards ALTA (220 términos)
- Reduce análisis de logs a 10 ejemplos más comunes
- Prioriza D4 (28% del examen)

### "Voy adelantado"
- Añade flashcards MEDIA (162 términos adicionales)
- Completa TODOS los 20 ejemplos de logs
- Practica más ejercicios de cálculo
- Haz simulacros adicionales

### "No entiendo algo"
- Consulta PDF objetivos oficiales (más detalle)
- Busca término en diccionario JSON completo
- Pregunta en foros (Reddit r/CompTIA, Discord)
- Mira videos Professor Messer sobre el tema

---

## ESTADÍSTICAS DEL MATERIAL

**Contenido total**:
- 15 laboratorios prácticos (~17 horas)
- 220 flashcards ALTA prioridad
- 162 flashcards MEDIA prioridad
- 20 ejemplos de análisis de logs
- 12 ejercicios de cálculo con soluciones
- 150 preguntas de práctica
- 1 cheat sheet de comandos (1 página)

**Cobertura**:
- 100% de objetivos oficiales SY0-701
- 88% del diccionario completo (382/436 términos)
- 5 dominios con material específico

**Tiempo estimado**:
- Plan completo (8 semanas): 130 horas
- Plan acelerado (4 semanas): 60 horas
- Plan ultra-rápido (2 semanas): 40 horas

**Score esperado con plan completo: 85-92%**

---

## MOTIVACIÓN FINAL

Has llegado hasta aquí. Tienes TODO el material necesario para aprobar con 85%+.

**130 horas de preparación = ESTÁS LISTO**

No es suerte. Es preparación + ejecución.

Ahora ve, abre `Semana_1-2_Fundamentos_D1-D2/README.md` y empieza tu viaje.

**¡MUCHA SUERTE! 🚀**

---

**Última actualización**: 2026-03-03
**Versión**: 1.0 (Completo y listo para usar)
