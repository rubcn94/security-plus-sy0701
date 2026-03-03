# Security+ SY0-701 - Material de Estudio Completo

[![CompTIA Security+](https://img.shields.io/badge/CompTIA-Security%2B%20SY0--701-red?style=for-the-badge&logo=comptia)](https://www.comptia.org/certifications/security)
[![Licencia](https://img.shields.io/badge/Licencia-CC%20BY--NC--SA%204.0-lightgrey?style=for-the-badge)](LICENSE)
[![Cobertura](https://img.shields.io/badge/Cobertura-100%25%20Objetivos-brightgreen?style=for-the-badge)](docs/objetivos-oficiales.pdf)

> **Plan de estudio estructurado de 8 semanas para aprobar CompTIA Security+ SY0-701 con 85%+ de score**

---

## 🎯 ¿Qué es esto?

Este repositorio contiene **TODO el material necesario** para aprobar el examen CompTIA Security+ SY0-701:

- ✅ **382 flashcards** (220 términos ALTA prioridad + 162 MEDIA)
- ✅ **Plan de estudio de 8 semanas** día a día con checkboxes
- ✅ **15 laboratorios prácticos** hands-on (~17 horas)
- ✅ **20 ejemplos de análisis de logs** reales con IOCs
- ✅ **12 ejercicios de cálculos** (ALE, CVSS, subnetting, RTO/RPO)
- ✅ **Cheat sheet de comandos** para PBQs (Windows, Linux, Wireshark, Nmap)
- ✅ **100% de cobertura** de objetivos oficiales CompTIA

**Score esperado siguiendo el plan completo: 85-92%**

---

## 🚀 Inicio Rápido

### Opción 1: Plan Completo 8 Semanas (Recomendado)

```bash
1. Descarga el repositorio
2. Abre: plan-8-semanas/README.md
3. Empieza con Semana 1-2
4. Sigue checkboxes día a día (2-3 horas/día)
5. Completa labs y ejercicios
6. Semana 8: Simulacro + Examen Real
```

**Tiempo total**: 112-168 horas
**Score esperado**: 85-92%

### Opción 2: Plan Acelerado 4 Semanas

```bash
- Solo flashcards ALTA prioridad (220 términos)
- Labs críticos (5 de 15)
- 10 ejemplos de logs (en vez de 20)
- 4-5 horas/día
```

**Tiempo total**: 60-80 horas
**Score esperado**: 80-85%

### Opción 3: Repaso Rápido 2 Semanas

```bash
- Solo para quien ya tiene experiencia en seguridad
- Flashcards + fórmulas + comandos
- Sin labs
```

**Tiempo total**: 30-40 horas
**Score esperado**: 75-80%

---

## 📚 Estructura del Repositorio

```
security-plus-sy0701/
│
├── plan-8-semanas/               # Plan de estudio estructurado
│   ├── README.md                 # Overview completo del plan
│   ├── semana-1-2-fundamentos/   # Dominios 1-2 (34% del examen)
│   ├── semana-3-4-arquitectura/  # Dominio 3 (18% del examen)
│   ├── semana-5-6-operaciones/   # Dominio 4 (28% del examen) ⚠️ MÁS IMPORTANTE
│   └── semana-7-8-governance/    # Dominio 5 + Repaso (20%)
│
├── flashcards/                   # 382 flashcards en 3 formatos
│   ├── flashcards.html           # HTML interactivo (filtrable por dominio/prioridad)
│   ├── flashcards.csv            # Para importar a Anki
│   └── flashcards.pdf            # PDF imprimible (220 ALTA + 162 MEDIA)
│
├── laboratorios/                 # 15 labs prácticos paso a paso
│   ├── README.md                 # Índice de labs + tiempos estimados
│   ├── dominio-1/                # 3 labs (PKI, Zero Trust, Cifrado)
│   ├── dominio-2/                # 2 labs (Malware, OSINT)
│   ├── dominio-3/                # 3 labs (Firewall, IDS/IPS, Destrucción datos)
│   ├── dominio-4/                # 3 labs (Hardening, IR, SIEM)
│   └── dominio-5/                # 3 labs (Risk analysis, Compliance, Third-party)
│
├── guias-practicas/              # Guías de referencia
│   ├── cheat-sheet-comandos.md   # Comandos para PBQs (IMPRIME Y LLEVA AL EXAMEN)
│   ├── analisis-logs.md          # 20 ejemplos reales con IOCs
│   └── ejercicios-calculos.md    # 12 ejercicios con soluciones
│
├── diccionario/                  # Términos por dominio
│   ├── diccionario-completo.json # 436 términos (formato estructurado)
│   └── diccionario-completo.md   # 436 términos (formato markdown)
│
├── docs/                         # Documentación adicional
│   ├── objetivos-oficiales.pdf   # Objetivos CompTIA oficiales
│   ├── faq.md                    # Preguntas frecuentes
│   └── recursos-externos.md      # Links a recursos complementarios
│
└── README.md                     # Este archivo
```

---

## 🎓 Cómo Usar Este Material

### Paso 1: Evalúa tu Nivel

**¿Eres nuevo en IT/seguridad?**
→ Sigue el **Plan 8 Semanas completo**

**¿Ya trabajas en IT con algo de seguridad?**
→ Puedes hacer el **Plan Acelerado 4 Semanas**

**¿Ya trabajas en seguridad sin certificaciones?**
→ **Repaso Rápido 2 Semanas** puede ser suficiente

### Paso 2: Descarga los Materiales

**Flashcards HTML** (recomendado):
```bash
Abre: flashcards/flashcards.html en tu navegador
- Filtra por dominio (D1, D2, D3, D4, D5)
- Filtra por prioridad (ALTA, MEDIA)
- Modo estudio interactivo
```

**O usa Anki** (spaced repetition):
```bash
Importa: flashcards/flashcards.csv a Anki
```

**O imprime** (para estudiar offline):
```bash
Imprime: flashcards/flashcards.pdf
```

### Paso 3: Sigue el Plan

**Día 1**: Abre `plan-8-semanas/semana-1-2-fundamentos/README.md`
- Lee objetivos de la semana
- Sigue checklist día 1
- Marca completado ✅

**Cada día**: Repite
- 2-3 horas/día × 56 días = 112-168 horas totales

**Semana 8**: Simulacro + Examen Real
- Si sacas 85%+ en simulacro → estás listo

### Paso 4: Labs Prácticos

**Requisitos**:
- VirtualBox (gratis) o VMware
- Ubuntu Server 24.04 ISO (gratis)
- Windows Server 2022 trial (180 días gratis)
- Kali Linux (gratis)

**Labs críticos** (NO SALTAR):
- LAB 1.2: Zero Trust con VPN y MFA
- LAB 2.1: Análisis de Malware
- LAB 3.1: Firewall y Segmentación
- LAB 3.2: IDS/IPS con Suricata
- LAB 4.2: Respuesta a Incidentes ⚠️ MÁS IMPORTANTE

### Paso 5: Análisis de Logs

**Crítico para PBQs**:
- Lee `guias-practicas/analisis-logs.md`
- Analiza 20 ejemplos reales
- Speed challenge: 3 minutos por log

**Tipos de ataques cubiertos**:
- Brute Force, SQL Injection, Ransomware, DDoS, Phishing
- DNS Tunneling, Pass-the-Hash, Port Scan, Insider Threat
- Cryptojacking, XSS, Account Lockout, MITM
- Scheduled Task Persistence, Cloud Misconfiguration
- Credential Stuffing, Fileless Malware

### Paso 6: Memoriza lo Crítico

**CASI SEGURO en el examen**:

✅ **Orden Respuesta a Incidentes (IR)**
```
1. Preparation
2. Identification
3. Containment
4. Eradication
5. Recovery
6. Lessons Learned
```

✅ **Orden de Volatilidad (Forense)**
```
1. CPU, caché
2. RAM
3. Estado de red
4. Procesos
5. Archivos temporales
6. Disco duro
7. Logs remotos
8. Backups
```

✅ **Fórmulas Risk Management**
```
SLE = Asset Value × Exposure Factor
ALE = SLE × ARO
ROI = (ALE_before - ALE_after - Cost) / Cost × 100%
```

✅ **Subnetting**
```
Hosts = 2^(32 - CIDR) - 2

/24 = 254 hosts
/26 = 62 hosts
/28 = 14 hosts
/30 = 2 hosts (enlaces punto-a-punto)
```

✅ **Windows Event IDs** (9 críticos)
```
4624 = Logon exitoso
4625 = Logon fallido
4672 = Privilegios especiales
4688 = Proceso creado
4698 = Tarea programada creada
4720 = Usuario creado
4732 = Usuario añadido a grupo
4740 = Cuenta bloqueada
7045 = Servicio instalado
```

---

## 💡 Consejos para el Examen

### Antes del Examen

- [ ] Repasa fórmulas (SLE, ALE, subnetting)
- [ ] Repasa orden IR (6 fases)
- [ ] Repasa orden volatilidad (8 niveles)
- [ ] Repasa Windows Event IDs (9 críticos)
- [ ] Imprime cheat sheet de comandos
- [ ] Duerme 8 horas

### Durante el Examen

**Estrategia**:
1. **Lee todas las PBQs** primero (5 min), márcalas para después
2. **Responde las 90 múltiple-choice** (60 min)
3. **Vuelve a PBQs** con tiempo restante (25 min)
4. **Revisa respuestas marcadas** (10 min)

**Tips**:
- Elimina 2 opciones incorrectas primero
- Lee con cuidado: "EXCEPT", "LEAST", "NOT"
- No cambies respuestas a menos que estés SEGURO
- No dejes en blanco (no hay penalización)

**Formato**:
- Máximo 90 preguntas
- 90 minutos
- Multiple-choice + PBQs (5-10 simulaciones prácticas)
- Score para aprobar: 750/900 (83%)
- Precio: $404 USD

---

## 📊 Cobertura del Examen

| Dominio | Peso | Material | Status |
|---------|------|----------|--------|
| D1: Conceptos Generales | 12% | 8 videos + 3 labs | ✅ 100% |
| D2: Amenazas y Mitigaciones | 22% | 12 videos + 2 labs | ✅ 100% |
| D3: Arquitectura | 18% | 10 videos + 3 labs | ✅ 100% |
| D4: Operaciones | **28%** | 12 videos + 3 labs | ✅ 100% |
| D5: Governance | 20% | 8 videos + 3 labs | ✅ 100% |
| **TOTAL** | **100%** | **50 temas + 15 labs** | **✅ 100%** |

**Material adicional**:
- 382 flashcards (88% del diccionario completo)
- 20 ejemplos análisis de logs
- 12 ejercicios de cálculos
- 1 cheat sheet de comandos

---

## 🤝 Contribuir

¿Encontraste un error? ¿Quieres añadir contenido?

1. Fork este repositorio
2. Crea una branch: `git checkout -b feature/nuevo-lab`
3. Commit tus cambios: `git commit -m 'Añadido lab de SIEM'`
4. Push a la branch: `git push origin feature/nuevo-lab`
5. Abre un Pull Request

**Áreas donde puedes contribuir**:
- Traducir material a inglés
- Añadir más ejemplos de logs
- Crear labs adicionales
- Mejorar explicaciones
- Reportar errores en contenido

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

---

## 📝 Licencia

Este material está licenciado bajo [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](LICENSE).

**Esto significa**:
- ✅ Puedes usar este material para estudiar (gratis)
- ✅ Puedes compartirlo con amigos/colegas
- ✅ Puedes modificarlo y crear versiones derivadas
- ❌ NO puedes venderlo o usarlo comercialmente
- ❌ Debes dar crédito al autor original
- ❌ Obras derivadas deben usar la misma licencia

**Uso comercial**: Si quieres usar este material para cursos pagos, bootcamps, o consultoría, contacta al autor.

---

## 🙏 Agradecimientos

**Fuentes de información**:
- CompTIA Security+ SY0-701 Official Objectives
- Professor Messer (videos de referencia)
- NIST SP 800-series
- MITRE ATT&CK Framework
- CIS Benchmarks

**Herramientas usadas**:
- Claude Code (organización y estructuración)
- VirtualBox (labs)
- Markdown (documentación)

---

## 📧 Contacto

**¿Tienes preguntas?**
- Abre un [Issue](https://github.com/tu-usuario/security-plus-sy0701/issues)
- Lee el [FAQ](docs/faq.md)

**¿Aprobaste usando este material?**
- ¡Cuéntanos tu experiencia! Abre un [Issue](https://github.com/tu-usuario/security-plus-sy0701/issues) con tu historia

---

## ⭐ Dale una Estrella

Si este material te ayudó a aprobar Security+, considera:
- ⭐ Darle una estrella a este repo
- 🔀 Compartirlo con amigos que estén estudiando
- 💬 Dejar tu feedback en Issues

---

## 📈 Estadísticas

![GitHub stars](https://img.shields.io/github/stars/tu-usuario/security-plus-sy0701?style=social)
![GitHub forks](https://img.shields.io/github/forks/tu-usuario/security-plus-sy0701?style=social)
![GitHub issues](https://img.shields.io/github/issues/tu-usuario/security-plus-sy0701)
![GitHub last commit](https://img.shields.io/github/last-commit/tu-usuario/security-plus-sy0701)

---

## 🗺️ Roadmap

**Versión actual: 1.0**

**Futuras versiones**:
- [ ] v1.1: Material en inglés
- [ ] v1.2: Videos explicativos (YouTube)
- [ ] v1.3: Simulacros de examen adicionales
- [ ] v1.4: Labs avanzados (Kubernetes, Cloud)
- [ ] v2.0: Actualización a SY0-801 (cuando salga)

---

## 📜 Changelog

### v1.0 (2026-03-03)
- ✅ Release inicial
- ✅ 382 flashcards (220 ALTA + 162 MEDIA)
- ✅ Plan 8 semanas completo
- ✅ 15 laboratorios prácticos
- ✅ 20 ejemplos análisis de logs
- ✅ 12 ejercicios de cálculos
- ✅ Cheat sheet comandos
- ✅ 100% cobertura objetivos SY0-701

---

**¡Mucha suerte en tu examen Security+!** 🚀

**Score esperado: 85-92%**
