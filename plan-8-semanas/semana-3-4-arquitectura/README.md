# SEMANA 3-4: ARQUITECTURA DE SEGURIDAD (Dominio 3)

## OBJETIVOS DE APRENDIZAJE

**Dominio 3: Arquitectura y Diseño de Seguridad (18% del examen)**
- Arquitecturas seguras (Zero Trust, microsegmentación, SDN)
- Seguridad de red (firewalls, IDS/IPS, VPN, NAC)
- Seguridad cloud (IaaS, PaaS, SaaS, responsabilidad compartida)
- Seguridad de aplicaciones (DevSecOps, SAST/DAST)
- Resiliencia y recuperación (backups, redundancia, RAID)
- Destrucción segura de datos

---

## MATERIALES DISPONIBLES EN ESTA CARPETA

### Laboratorios Prácticos (3 labs - ~6 horas)
- [ ] LAB-3.1_Configuración_de_Firewall_y_Segmentación_de_Red.txt (2.5h)
- [ ] LAB-3.2_IDS-IPS_con_Suricata_+_ELK_Stack.txt (2.5h)
- [ ] LAB-3.3_Destrucción_Segura_de_Datos_y_Crypto-Shredding.txt (1h)

### Guías de Referencia
- [ ] CHEAT_SHEET_COMANDOS_PBQs.md - Firewall (iptables/ufw/netsh), Wireshark
- [ ] GUIA_ANALISIS_LOGS.md - Ejemplos 4, 7, 11, 16 (firewall, DDoS, IDS, MITM)
- [ ] EJERCICIOS_CALCULOS_PRACTICOS.md - Subnetting (ejercicios 8-10)

### Flashcards (en carpeta principal)
- Revisar términos ALTA prioridad de D3 (aprox. 50 términos)
- Archivo: `../Flashcards/SecPlus_Flashcards_Interactivo.html`

---

## PLAN DE ESTUDIO DIARIO (14 días)

### SEMANA 3 (Arquitecturas y Red)

#### Día 15: Arquitecturas Seguras
- [ ] **Teoría (1.5h)**: Flashcards D3 - Zero Trust, microsegmentación, CASB
- [ ] **Práctica (30min)**: Revisar diagramas de arquitectura
- [ ] **Total**: 2h

#### Día 16: Segmentación de Red
- [ ] **Teoría (1h)**: Flashcards D3 - VLANs, DMZ, subnetting
- [ ] **LAB (2.5h)**: LAB-3.1 - Firewall y Segmentación
- [ ] **Ejercicios (30min)**: EJERCICIOS_CALCULOS - Subnetting (ej. 8-10)
- [ ] **Total**: 4h

#### Día 17: Firewalls y ACLs
- [ ] **Teoría (1h)**: Flashcards D3 - Tipos firewall, reglas ACL
- [ ] **Comandos (1h)**: CHEAT_SHEET - iptables, ufw, netsh advfirewall
- [ ] **Logs (30min)**: GUIA_ANALISIS_LOGS - Ejemplo 4 (data exfiltration)
- [ ] **Total**: 2.5h

#### Día 18: IDS/IPS
- [ ] **Teoría (1h)**: Flashcards D3 - IDS vs IPS, firmas, anomalías
- [ ] **LAB (2.5h)**: LAB-3.2 - IDS/IPS con Suricata + ELK
- [ ] **Logs (30min)**: GUIA_ANALISIS_LOGS - Ejemplos 7, 11 (DDoS, port scan)
- [ ] **Total**: 4h

#### Día 19: VPN y Acceso Remoto
- [ ] **Teoría (1.5h)**: Flashcards D3 - VPN (site-to-site, remote), IPsec, SSL/TLS
- [ ] **Comandos (1h)**: Configuraciones VPN, troubleshooting
- [ ] **Total**: 2.5h

#### Día 20: Repaso Semana 3
- [ ] **Repaso flashcards D3 (1h)**: Arquitecturas y red
- [ ] **Ejercicios (1h)**: Subnetting + reglas firewall
- [ ] **Total**: 2h

#### Día 21: DESCANSO

---

### SEMANA 4 (Cloud, Apps, Resiliencia)

#### Día 22: Seguridad Cloud
- [ ] **Teoría (1.5h)**: Flashcards D3 - IaaS/PaaS/SaaS, responsabilidad compartida
- [ ] **Logs (30min)**: GUIA_ANALISIS_LOGS - Ejemplo 18 (AWS CloudTrail)
- [ ] **Total**: 2h

#### Día 23: Contenedores y Virtualización
- [ ] **Teoría (1.5h)**: Flashcards D3 - Docker, Kubernetes, hypervisors
- [ ] **Práctica (1h)**: Configuración básica de contenedores
- [ ] **Total**: 2.5h

#### Día 24: Seguridad de Aplicaciones
- [ ] **Teoría (1.5h)**: Flashcards D3 - SAST/DAST, OWASP Top 10, DevSecOps
- [ ] **Logs (1h)**: GUIA_ANALISIS_LOGS - Ejemplos 2, 14 (SQL injection, XSS)
- [ ] **Total**: 2.5h

#### Día 25: Resiliencia y Backups
- [ ] **Teoría (1.5h)**: Flashcards D3 - RAID, backups, snapshots, replicación
- [ ] **Ejercicios (1h)**: EJERCICIOS_CALCULOS - RPO/RTO (ej. 12)
- [ ] **Total**: 2.5h

#### Día 26: Destrucción de Datos
- [ ] **Teoría (1h)**: Flashcards D3 - Wiping, degaussing, crypto-shredding
- [ ] **LAB (1h)**: LAB-3.3 - Destrucción Segura de Datos
- [ ] **Total**: 2h

#### Día 27: Repaso D3 Completo
- [ ] **Repaso flashcards D3 (1.5h)**: Todos los términos ALTA
- [ ] **Ejercicios integrados (1h)**: Diseñar arquitectura segura completa
- [ ] **Logs (30min)**: Revisar ejemplos 4, 7, 11, 16, 18
- [ ] **Total**: 3h

#### Día 28: Simulacro D3
- [ ] **Simulacro (1.5h)**: Preguntas de práctica D3
- [ ] **Análisis errores (1h)**: Identificar puntos débiles
- [ ] **Refuerzo (30min)**: Revisar términos fallados
- [ ] **Total**: 3h

---

## RECURSOS ADICIONALES

### Flashcards HTML (Carpeta principal)
Ubicación: `D:\Users\cra\Desktop\Sec+\01_Material_Estudio\Flashcards\SecPlus_Flashcards_Interactivo.html`

Filtrar por Dominio 3 (D3): ~50 términos ALTA

### Wireshark Filters (CRÍTICO para PBQs)
Del CHEAT_SHEET_COMANDOS_PBQs.md:
```
ip.addr == 192.168.1.10         # Tráfico de/hacia IP
tcp.port == 80                  # Puerto TCP 80
tcp.flags.syn == 1 && tcp.flags.ack == 0  # Solo SYN (port scan)
ssl.handshake.type == 1         # TLS Client Hello
```

### Subnetting (MEMORIZAR)
```
/24 = 255.255.255.0     = 254 hosts
/25 = 255.255.255.128   = 126 hosts
/26 = 255.255.255.192   = 62 hosts
/27 = 255.255.255.224   = 30 hosts
/28 = 255.255.255.240   = 14 hosts
/29 = 255.255.255.248   = 6 hosts
/30 = 255.255.255.252   = 2 hosts (enlaces punto-a-punto)

Fórmula: Hosts = 2^(32 - CIDR) - 2
```

---

## CHECKLIST SEMANAL

### Semana 3 (Arquitecturas y Red)
- [ ] Completar 5.5h estudio teórico (flashcards)
- [ ] Completar LAB-3.1 y LAB-3.2 (5h)
- [ ] Dominar subnetting (3 ejercicios completos)
- [ ] Practicar reglas firewall (iptables, ufw, netsh)
- [ ] **Meta**: Poder diseñar segmentación de red completa

### Semana 4 (Cloud, Apps, Resiliencia)
- [ ] Completar 6h estudio teórico (flashcards)
- [ ] Completar LAB-3.3 (1h)
- [ ] Entender modelo responsabilidad compartida cloud
- [ ] Calcular RPO/RTO para escenarios
- [ ] **Meta**: Dominar 100% términos ALTA de D3

---

## CRITERIOS DE ÉXITO

Al finalizar estas 2 semanas deberías poder:

**Arquitecturas y Red:**
- [ ] Diseñar arquitectura Zero Trust con microsegmentación
- [ ] Configurar firewall con reglas ACL específicas
- [ ] Calcular subnetting para cualquier escenario (/24, /26, /28, etc.)
- [ ] Diferenciar IDS vs IPS y ubicarlos correctamente en red
- [ ] Configurar VPN site-to-site y remote access

**Cloud y Apps:**
- [ ] Explicar modelo responsabilidad compartida (IaaS/PaaS/SaaS)
- [ ] Identificar vulnerabilidades OWASP Top 10 en logs
- [ ] Comparar SAST vs DAST y cuándo usar cada uno
- [ ] Diseñar pipeline DevSecOps básico

**Resiliencia:**
- [ ] Seleccionar nivel RAID apropiado para cada escenario
- [ ] Calcular RPO/RTO y diseñar estrategia backup
- [ ] Elegir método correcto destrucción datos (wiping, degaussing, crypto-shredding)

---

## EJERCICIOS PRÁCTICOS CLAVE

### Ejercicio 1: Diseño de Segmentación
**Escenario**: Empresa con 3 departamentos (Ventas, IT, Finanzas), DMZ para web servers, VPN para remote workers.

**Tu tarea**:
1. Diseñar subnetting (red 192.168.0.0/16)
2. Crear reglas firewall entre segmentos
3. Ubicar IDS/IPS
4. Configurar VPN

**Tiempo**: 1 hora

### Ejercicio 2: Análisis de Logs Firewall
**Archivo**: GUIA_ANALISIS_LOGS.md - Ejemplo 4 (Data Exfiltration)

**Tu tarea**:
1. Identificar tráfico anómalo
2. Crear reglas firewall para bloquear
3. Escribir filtros Wireshark para detectar

**Tiempo**: 30 minutos

### Ejercicio 3: Cálculo Subnetting
**Del archivo** EJERCICIOS_CALCULOS_PRACTICOS.md - Ejercicios 8, 9, 10

**Practica hasta poder resolver en < 2 minutos cada uno**

---

## NOTAS IMPORTANTES

1. **PBQs del examen**: D3 tiene muchas PBQs de diseño de red y configuración firewall
2. **Subnetting**: Practica hasta que sea automático (no puedes usar calculadora en el examen)
3. **Wireshark**: Conoce los filtros básicos (ip.addr, tcp.port, tcp.flags)
4. **Cloud**: Memoriza modelo responsabilidad compartida (pregunta casi segura en el examen)
5. **Labs**: LAB-3.1 y LAB-3.2 son los MÁS importantes de D3

---

## TROUBLESHOOTING

**Si vas atrasado:**
- Prioriza LAB-3.1 (firewall) sobre LAB-3.2 (IDS/IPS)
- Salta LAB-3.3 si es necesario
- Enfócate en subnetting (/24, /26, /28 solamente)

**Si vas adelantado:**
- Añade términos MEDIA de D3
- Practica más casos de subnetting VLSM
- Configura Wireshark con filtros avanzados
- Revisa todos los 20 ejemplos de logs

**Si algo no se entiende:**
- Subnetting confuso: usa calculadora online primero, luego manual
- Firewalls: dibuja diagrama de red primero
- Cloud: busca diagrama responsabilidad compartida (visual ayuda)

---

## COMANDOS CLAVE PARA MEMORIZAR

### Linux Firewall (iptables)
```bash
iptables -L -n -v               # Listar reglas
iptables -A INPUT -p tcp --dport 22 -j ACCEPT   # Permitir SSH
iptables -A INPUT -s 203.0.113.0/24 -j DROP     # Bloquear subnet
```

### Linux Firewall (ufw - más simple)
```bash
ufw status                      # Ver estado
ufw allow 22/tcp                # Permitir SSH
ufw deny 445/tcp                # Bloquear SMB
```

### Windows Firewall
```cmd
netsh advfirewall show allprofiles          # Ver estado
netsh advfirewall firewall add rule name="Block Port 445" dir=in action=block protocol=TCP localport=445
```

### Wireshark Filters
```
ip.src == 192.168.1.10          # Solo origen
tcp.port == 80                  # Puerto TCP 80
tcp.flags.syn == 1 && tcp.flags.ack == 0  # Solo SYN packets
```

---

**SIGUIENTE PASO**: Al terminar el día 28, pasa a `Semana_5-6_Operations_D4/`

**NOTA**: D4 es el dominio MÁS PESADO (28% del examen), prepárate para 2 semanas intensas.
