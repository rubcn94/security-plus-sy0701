# EJERCICIOS DE CÁLCULOS - Security+ SY0-701

**Dominio 5: Security Program Management (20%)**
**Objetivo 5.2**: Risk Management Process

---

## TABLA DE CONTENIDOS

1. [Risk Management (ALE, SLE, ARO)](#risk-management)
2. [CVSS Scoring](#cvss-scoring)
3. [Subnetting](#subnetting)
4. [Business Continuity (RTO, RPO, MTTR, MTBF)](#business-continuity)
5. [Ejercicios Combinados](#ejercicios-combinados)

---

## RISK MANAGEMENT

### FÓRMULAS CLAVE

```
SLE  = Asset Value × Exposure Factor
ALE  = SLE × ARO
ARO  = Annualized Rate of Occurrence (veces al año)
EF   = Exposure Factor (% de pérdida)
```

---

### EJERCICIO 1: Cálculo Básico de ALE

**Escenario**:
Tu empresa tiene un servidor de base de datos valorado en **$50,000**.
Un análisis de riesgos determinó que un ataque de ransomware podría destruir **80%** del valor del servidor.
Históricamente, este tipo de ataque ocurre **2 veces al año**.

**Preguntas**:
1. ¿Cuál es el SLE (Single Loss Expectancy)?
2. ¿Cuál es el ALE (Annualized Loss Expectancy)?
3. Si implementas un backup sistema que reduce la exposición a 20%, ¿cuál sería el nuevo ALE?
4. ¿Cuánto puedes justificar gastar en la solución de backup?

<details>
<summary>SOLUCIÓN</summary>

**1. SLE**:
```
SLE = Asset Value × Exposure Factor
SLE = $50,000 × 0.80 = $40,000
```

**2. ALE**:
```
ALE = SLE × ARO
ALE = $40,000 × 2 = $80,000/año
```

**3. Nuevo ALE con backup**:
```
Nuevo EF = 20% = 0.20
Nuevo SLE = $50,000 × 0.20 = $10,000
Nuevo ALE = $10,000 × 2 = $20,000/año
```

**4. Justificación de gasto**:
```
Reducción de riesgo = ALE_original - ALE_nuevo
Reducción = $80,000 - $20,000 = $60,000/año

Puedes justificar gastar hasta $60,000/año en el backup.
Si la solución cuesta $30,000/año → ROI positivo de $30,000/año
```

</details>

---

### EJERCICIO 2: Múltiples Amenazas

**Escenario**:
Un servidor web crítico (valor: **$100,000**) enfrenta varias amenazas:

| Amenaza | Exposure Factor | ARO |
|---------|----------------|-----|
| DDoS Attack | 30% | 4 veces/año |
| Data Breach | 60% | 0.5 veces/año |
| Hardware Failure | 100% | 0.1 veces/año |

**Pregunta**: ¿Cuál es el ALE total combinado?

<details>
<summary>SOLUCIÓN</summary>

**Amenaza 1: DDoS**
```
SLE = $100,000 × 0.30 = $30,000
ALE = $30,000 × 4 = $120,000/año
```

**Amenaza 2: Data Breach**
```
SLE = $100,000 × 0.60 = $60,000
ALE = $60,000 × 0.5 = $30,000/año
```

**Amenaza 3: Hardware Failure**
```
SLE = $100,000 × 1.00 = $100,000
ALE = $100,000 × 0.1 = $10,000/año
```

**ALE Total**:
```
ALE_total = $120,000 + $30,000 + $10,000 = $160,000/año
```

**Interpretación**:
- DDoS es el riesgo más alto ($120k) → priorizar solución anti-DDoS
- Justificar inversión hasta $160k/año para mitigar todos los riesgos

</details>

---

### EJERCICIO 3: ROI de Controles de Seguridad

**Escenario**:
Situación actual:
- Asset value: **$200,000**
- ARO (phishing exitoso): **3 veces/año**
- Exposure Factor: **40%**

Propuesta: Implementar MFA + Security Awareness Training
- Costo anual: **$25,000**
- Reduce ARO a: **0.5 veces/año**
- Reduce EF a: **10%**

**Pregunta**: ¿Vale la pena la inversión? Calcula el ROI.

<details>
<summary>SOLUCIÓN</summary>

**Situación Actual**:
```
SLE = $200,000 × 0.40 = $80,000
ALE_actual = $80,000 × 3 = $240,000/año
```

**Con Controles**:
```
Nuevo SLE = $200,000 × 0.10 = $20,000
Nuevo ALE = $20,000 × 0.5 = $10,000/año
```

**ROI**:
```
Reducción de riesgo = $240,000 - $10,000 = $230,000/año
Costo de solución = $25,000/año
Beneficio neto = $230,000 - $25,000 = $205,000/año

ROI = (Beneficio neto / Costo) × 100
ROI = ($205,000 / $25,000) × 100 = 820%
```

**Conclusión**: SÍ vale la pena. Por cada $1 invertido, obtienes $9.20 de retorno.

</details>

---

## CVSS SCORING

### FÓRMULA CVSS v3.1 (SIMPLIFICADA)

**CVSS Score**: 0.0 - 10.0

**Métricas Base**:
- **Attack Vector (AV)**: Network (N), Adjacent (A), Local (L), Physical (P)
- **Attack Complexity (AC)**: Low (L), High (H)
- **Privileges Required (PR)**: None (N), Low (L), High (H)
- **User Interaction (UI)**: None (N), Required (R)
- **Impact**: Confidentiality (C), Integrity (I), Availability (A) - High/Low/None

**Rangos de Severidad**:
```
0.0       = None
0.1 - 3.9 = Low
4.0 - 6.9 = Medium
7.0 - 8.9 = High
9.0 - 10.0 = Critical
```

---

### EJERCICIO 4: Interpretar CVSS Score

**Escenario**:
Recibes un reporte de vulnerabilidad con **CVSS Score: 9.8 (CRITICAL)**

Vector: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

**Pregunta**: Interpreta qué significa este score y qué tan urgente es parchear.

<details>
<summary>SOLUCIÓN</summary>

**Desglose del Vector**:
```
AV:N  = Attack Vector: Network (remotamente explotable)
AC:L  = Attack Complexity: Low (fácil de explotar)
PR:N  = Privileges Required: None (no requiere autenticación)
UI:N  = User Interaction: None (no necesita que usuario haga nada)
S:U   = Scope: Unchanged
C:H   = Confidentiality Impact: High (leak de datos sensibles)
I:H   = Integrity Impact: High (puede modificar datos)
A:H   = Availability Impact: High (puede causar DoS)
```

**Interpretación**:
- **9.8 = CRÍTICO**
- Explotable remotamente sin credenciales
- No necesita interacción del usuario
- Impacto total en CIA Triad
- Probablemente tiene exploit público disponible

**Acción**:
- **URGENCIA: INMEDIATA** (parchear en < 24 horas)
- Considerar apagar sistema si patch no disponible
- Implementar WAF/IPS como mitigación temporal
- Monitoreo intensivo de logs

**Ejemplos reales con 9.8**:
- Log4Shell (CVE-2021-44228)
- ProxyShell (CVE-2021-34473)
- EternalBlue (CVE-2017-0144)

</details>

---

### EJERCICIO 5: Priorizar Vulnerabilidades

**Escenario**:
Tienes 4 vulnerabilidades descubiertas. Recursos limitados. ¿Cuál parchear primero?

| CVE | CVSS | Sistema | Exposición |
|-----|------|---------|------------|
| CVE-A | 9.1 (Critical) | Web server público | Internet-facing |
| CVE-B | 7.5 (High) | Database server | Red interna |
| CVE-C | 5.3 (Medium) | File server | Red interna |
| CVE-D | 3.1 (Low) | Test server | Isolated VLAN |

**Pregunta**: Ordena la priorización considerando CVSS + contexto.

<details>
<summary>SOLUCIÓN</summary>

**Priorización Correcta**:

**1. CVE-A (9.1, Web server público)**
- CVSS más alto + expuesto a Internet
- Mayor probabilidad de ser explotado
- Impacto reputacional si comprometido
- **Acción**: Parchear INMEDIATAMENTE

**2. CVE-B (7.5, Database server interno)**
- Aunque es interno, contiene datos sensibles
- CVSS High
- Si atacante llega a red interna, es target valioso
- **Acción**: Parchear en < 7 días

**3. CVE-C (5.3, File server interno)**
- CVSS Medium
- Impacto limitado
- **Acción**: Parchear en < 30 días

**4. CVE-D (3.1, Test server aislado)**
- CVSS Low + aislado en VLAN
- Bajo riesgo
- **Acción**: Parchear en próximo ciclo de mantenimiento

**Factores de Contexto** (no solo CVSS):
- Exposición a Internet
- Valor de datos
- Disponibilidad de exploit
- Criticidad del sistema
- Compensating controls existentes

</details>

---

## SUBNETTING

### FÓRMULA BÁSICA
```
Número de hosts = 2^(bits de host) - 2

Bits de host = 32 - máscara CIDR
```

---

### EJERCICIO 6: Subnetting Básico

**Pregunta**: Tienes la red **192.168.10.0/26**. Calcula:
1. Máscara de subred en decimal
2. Número de hosts utilizables
3. Rango de IPs válidas
4. IP de red
5. IP de broadcast

<details>
<summary>SOLUCIÓN</summary>

**1. Máscara de subred**:
```
/26 = 11111111.11111111.11111111.11000000
    = 255.255.255.192
```

**2. Número de hosts**:
```
Bits de host = 32 - 26 = 6 bits
Hosts = 2^6 - 2 = 64 - 2 = 62 hosts utilizables
```

**3. Rango de IPs**:
```
Primer host: 192.168.10.1
Último host: 192.168.10.62
```

**4. IP de red**:
```
192.168.10.0 (primera IP del rango)
```

**5. IP de broadcast**:
```
192.168.10.63 (última IP del rango)
```

**Desglose completo**:
```
Red:        192.168.10.0      (no asignable)
Hosts:      192.168.10.1-62   (asignables)
Broadcast:  192.168.10.63     (no asignable)
```

</details>

---

### EJERCICIO 7: Dividir Red en Subnets

**Escenario**:
Tienes la red **10.0.0.0/24** y necesitas dividirla en **4 subnets** de igual tamaño.

**Pregunta**:
1. ¿Qué máscara usar?
2. ¿Cuántos hosts por subnet?
3. Define los 4 rangos

<details>
<summary>SOLUCIÓN</summary>

**1. Máscara necesaria**:
```
Para 4 subnets = 2^2 → necesitas 2 bits adicionales
Nueva máscara = /24 + 2 = /26
Máscara decimal = 255.255.255.192
```

**2. Hosts por subnet**:
```
Bits de host = 32 - 26 = 6
Hosts = 2^6 - 2 = 62 hosts/subnet
```

**3. Los 4 rangos**:

**Subnet 1**:
```
Red:        10.0.0.0
Hosts:      10.0.0.1 - 10.0.0.62
Broadcast:  10.0.0.63
```

**Subnet 2**:
```
Red:        10.0.0.64
Hosts:      10.0.0.65 - 10.0.0.126
Broadcast:  10.0.0.127
```

**Subnet 3**:
```
Red:        10.0.0.128
Hosts:      10.0.0.129 - 10.0.0.190
Broadcast:  10.0.0.191
```

**Subnet 4**:
```
Red:        10.0.0.192
Hosts:      10.0.0.193 - 10.0.0.254
Broadcast:  10.0.0.255
```

**Salto entre subnets**: 64 (2^6)

</details>

---

### EJERCICIO 8: Identificar Subnet

**Pregunta**:
Un host tiene IP **172.16.45.130/27**.
1. ¿A qué subnet pertenece?
2. ¿Cuál es su gateway (primera IP utilizable)?
3. ¿Cuántos hosts más caben en esta subnet?

<details>
<summary>SOLUCIÓN</summary>

**1. Identificar subnet**:
```
/27 = 255.255.255.224
Bits de host = 32 - 27 = 5
Tamaño de subnet = 2^5 = 32 IPs

Encontrar el múltiplo de 32 más cercano <= 130:
130 / 32 = 4.06... → múltiplo 4
Inicio de subnet = 32 × 4 = 128

Subnet: 172.16.45.128/27
```

**2. Gateway (primera IP utilizable)**:
```
Gateway = 172.16.45.129
```

**3. Capacidad restante**:
```
Rango completo: 172.16.45.128 - 159
Red: 172.16.45.128 (no asignable)
Hosts: 172.16.45.129 - 158 (30 IPs)
Broadcast: 172.16.45.159 (no asignable)

Ya usado: 172.16.45.130 (el host en cuestión)
Disponibles: 30 - 1 = 29 hosts más
```

**Resumen**:
- Subnet: 172.16.45.128/27
- Gateway: 172.16.45.129
- Hosts disponibles: 29

</details>

---

## BUSINESS CONTINUITY

### FÓRMULAS CLAVE

```
RTO  = Recovery Time Objective (tiempo máximo aceptable de downtime)
RPO  = Recovery Point Objective (máxima pérdida de datos aceptable)
MTTR = Mean Time To Repair (tiempo promedio de reparación)
MTBF = Mean Time Between Failures (tiempo promedio entre fallos)

Availability = (MTBF) / (MTBF + MTTR) × 100%
```

---

### EJERCICIO 9: RTO y RPO

**Escenario**:
Tu base de datos de clientes tiene los siguientes requisitos de negocio:
- **RTO**: 4 horas
- **RPO**: 1 hora

Actualmente:
- Backups completos: cada 24 horas (1:00 AM)
- Backups incrementales: cada 6 horas
- Tiempo de restauración: 2 horas

**Pregunta**:
1. ¿Cumples con el RTO?
2. ¿Cumples con el RPO?
3. ¿Qué ajustes recomiendas?

<details>
<summary>SOLUCIÓN</summary>

**1. RTO (4 horas requerido)**:
```
Tiempo actual de restauración = 2 horas
2 horas < 4 horas → SÍ cumple RTO ✅
```

**2. RPO (1 hora requerido)**:
```
Backup incremental cada 6 horas
Si falla a las 6:59, pierdes 6 horas de datos
6 horas > 1 hora RPO → NO cumple RPO ❌
```

**3. Ajustes recomendados**:
```
Problema: Backups cada 6h no cumplen RPO de 1h

Soluciones:
a) Backups incrementales cada 1 hora (cumple RPO exacto)
b) Backups cada 30 min (margen de seguridad)
c) Replicación continua a standby server (RPO ~0)
d) Transaction log shipping cada 15 min

Recomendación: Opción C (replicación continua)
- RPO: ~0 minutos
- RTO: Failover automático en < 1 hora
- Mayor costo pero cumple requerimientos con margen
```

**Trade-offs**:
- RPO más bajo = más recursos de storage
- RTO más bajo = infraestructura redundante costosa
- Balance: necesidades del negocio vs presupuesto

</details>

---

### EJERCICIO 10: Availability Calculation

**Escenario**:
Un servidor tiene las siguientes estadísticas del año pasado:
- **MTBF**: 720 horas (30 días)
- **MTTR**: 8 horas

**Pregunta**:
1. Calcula el porcentaje de disponibilidad (Availability)
2. ¿Cuántos "9s" de disponibilidad tiene?
3. ¿Cuánto downtime anual implica?

<details>
<summary>SOLUCIÓN</summary>

**1. Availability**:
```
Availability = (MTBF) / (MTBF + MTTR) × 100%
Availability = 720 / (720 + 8) × 100%
Availability = 720 / 728 × 100%
Availability = 98.90%
```

**2. "Nines" de disponibilidad**:
```
98.90% = dos "9s" (99% roundeado)

Referencia:
- 99% = "two nines" = 3.65 días downtime/año
- 99.9% = "three nines" = 8.76 horas/año
- 99.99% = "four nines" = 52.6 min/año
- 99.999% = "five nines" = 5.26 min/año
```

**3. Downtime anual**:
```
Uptime = 98.90%
Downtime = 100% - 98.90% = 1.10%

Horas en un año = 365 × 24 = 8,760 horas
Downtime anual = 8,760 × 0.011 = 96.36 horas
Downtime = 96.36 horas ≈ 4 días/año
```

**Mejoras para llegar a 99.9%**:
```
Target: 99.9% = 8.76 horas downtime/año
Actual: 96.36 horas downtime/año
Necesitas reducir downtime en: 96.36 - 8.76 = 87.6 horas/año

Opciones:
a) Reducir MTTR de 8h a 0.7h (muy difícil)
b) Aumentar MTBF con hardware redundante
c) Implementar failover automático (MTTR ~minutos)
```

</details>

---

## EJERCICIOS COMBINADOS

### EJERCICIO 11: Caso Completo - Ransomware

**Escenario**:
Compañía financiera con:
- Servidor de aplicaciones crítico: valor **$500,000**
- Backup actual: daily backups a las 2 AM
- Tiempo de restauración: 6 horas
- ARO de ransomware: 0.3 veces/año (1 cada ~3 años)
- EF sin controles: 90%

Propuesta: Implementar sistema de backup inmutable + EDR
- Costo: **$50,000/año**
- Reduce EF a: 10%
- Reduce ARO a: 0.05 veces/año
- Nuevo tiempo restauración: 2 horas

**Preguntas**:
1. Calcula ALE actual
2. Calcula ALE con controles
3. ¿Vale la pena la inversión? (ROI)
4. Actualmente, ¿cumple con RTO de 4 horas?
5. Con controles, ¿cumple RTO de 4 horas?

<details>
<summary>SOLUCIÓN COMPLETA</summary>

**1. ALE Actual**:
```
SLE = $500,000 × 0.90 = $450,000
ALE = $450,000 × 0.3 = $135,000/año
```

**2. ALE con Controles**:
```
Nuevo SLE = $500,000 × 0.10 = $50,000
Nuevo ALE = $50,000 × 0.05 = $2,500/año
```

**3. ROI**:
```
Reducción riesgo = $135,000 - $2,500 = $132,500/año
Costo solución = $50,000/año
Beneficio neto = $132,500 - $50,000 = $82,500/año

ROI = ($82,500 / $50,000) × 100 = 165%

SÍ vale la pena. Por cada $1 invertido, recuperas $1.65.
Payback period = $50,000 / $82,500 = 0.6 años (7 meses)
```

**4. RTO Actual**:
```
Tiempo de restauración actual = 6 horas
RTO requerido = 4 horas
6 > 4 → NO cumple RTO ❌
```

**5. RTO con Controles**:
```
Nuevo tiempo de restauración = 2 horas
RTO requerido = 4 horas
2 < 4 → SÍ cumple RTO ✅
```

**Conclusión**:
- **Reducción de riesgo**: $132,500/año
- **ROI**: 165% (excelente)
- **Cumplimiento RTO**: Pasa de NO a SÍ
- **Recomendación**: APROBAR la inversión

**Factores adicionales** (cualitativos):
- Cumplimiento regulatorio (PCI DSS, SOX)
- Reputación (evitar breach público)
- Continuidad de negocio
- Multas potenciales por breach

</details>

---

### EJERCICIO 12: Subnetting para Segmentación

**Escenario**:
Diseñas segmentación de red para empresa con **192.168.0.0/22**.
Necesitas:
- **Subnet 1** (Servidores): 200 hosts
- **Subnet 2** (Usuarios): 400 hosts
- **Subnet 3** (IoT): 50 hosts
- **Subnet 4** (DMZ): 10 hosts

**Pregunta**: Diseña la división óptima de subnets (VLSM).

<details>
<summary>SOLUCIÓN</summary>

**Análisis inicial**:
```
Red disponible: 192.168.0.0/22
Hosts totales = 2^(32-22) - 2 = 2^10 - 2 = 1,022 hosts
Necesarios = 200 + 400 + 50 + 10 = 660 hosts ✅ Cabe
```

**VLSM (Variable Length Subnet Masking)** - de mayor a menor:

**Subnet 2 (Usuarios): 400 hosts**
```
Necesita 400 hosts → mínimo 2^9 = 512 (bits de host = 9)
Máscara = 32 - 9 = /23
Subnet: 192.168.0.0/23
Rango: 192.168.0.1 - 192.168.1.254 (510 hosts)
```

**Subnet 1 (Servidores): 200 hosts**
```
Necesita 200 hosts → mínimo 2^8 = 256 (bits de host = 8)
Máscara = 32 - 8 = /24
Subnet: 192.168.2.0/24
Rango: 192.168.2.1 - 192.168.2.254 (254 hosts)
```

**Subnet 3 (IoT): 50 hosts**
```
Necesita 50 hosts → mínimo 2^6 = 64 (bits de host = 6)
Máscara = 32 - 6 = /26
Subnet: 192.168.3.0/26
Rango: 192.168.3.1 - 192.168.3.62 (62 hosts)
```

**Subnet 4 (DMZ): 10 hosts**
```
Necesita 10 hosts → mínimo 2^4 = 16 (bits de host = 4)
Máscara = 32 - 4 = /28
Subnet: 192.168.3.64/28
Rango: 192.168.3.65 - 192.168.3.78 (14 hosts)
```

**Resumen Final**:
| Subnet | Red | Máscara | Hosts | Uso |
|--------|-----|---------|-------|-----|
| Usuarios | 192.168.0.0/23 | 255.255.254.0 | 510 | 400 necesarios |
| Servidores | 192.168.2.0/24 | 255.255.255.0 | 254 | 200 necesarios |
| IoT | 192.168.3.0/26 | 255.255.255.192 | 62 | 50 necesarios |
| DMZ | 192.168.3.64/28 | 255.255.255.240 | 14 | 10 necesarios |

**Ventajas de esta segmentación**:
- VLANs separadas para cada tipo de dispositivo
- Firewall rules entre subnets
- IoT aislado de servidores críticos
- DMZ sin acceso directo a LAN interna

</details>

---

## TABLA DE REFERENCIA RÁPIDA

### Risk Management
```
SLE = Asset Value × Exposure Factor
ALE = SLE × ARO
ROI = (Reducción - Costo) / Costo × 100%
```

### CVSS Severity
```
0.0       = None
0.1 - 3.9 = Low
4.0 - 6.9 = Medium
7.0 - 8.9 = High
9.0 - 10.0 = Critical
```

### Subnetting
```
Hosts = 2^(32-CIDR) - 2
/24 = 254 hosts
/25 = 126 hosts
/26 = 62 hosts
/27 = 30 hosts
/28 = 14 hosts
/29 = 6 hosts
/30 = 2 hosts
```

### Business Continuity
```
Availability = MTBF / (MTBF + MTTR)
99% = 3.65 days/year downtime
99.9% = 8.76 hours/year
99.99% = 52.6 minutes/year
99.999% = 5.26 minutes/year
```

---

**¡Practica estos cálculos hasta que puedas hacerlos sin calculadora!**

En el examen Security+, tendrás:
- Calculadora disponible en pantalla
- ~2 minutos por cálculo
- Escenarios del mundo real

**Tip**: Memoriza las fórmulas y practica con números redondos primero.
