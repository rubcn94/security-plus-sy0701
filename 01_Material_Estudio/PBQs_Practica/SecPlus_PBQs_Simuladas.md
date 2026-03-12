# PBQs Simuladas - Security+ SY0-701

**15 Performance-Based Questions con soluciones paso a paso**

---

## PBQ_01: Configurar Segmentacin de Red con DMZ

**Dominio:** Dominio 3 - Arquitectura de Seguridad  
**Dificultad:** MEDIA  
**Tiempo estimado:** 15 minutos  

### Escenario

Tu empresa necesita exponer un servidor web al pblico mientras protege la red interna. Tienes 2 firewalls disponibles y necesitas configurar una DMZ. La red interna es 10.0.1.0/24, la DMZ ser 192.168.100.0/24, y el servidor web es 192.168.100.10.

### Tareas

1. Dibujar diagrama de red con: Internet - Firewall Externo - DMZ - Firewall Interno - LAN
2. Configurar reglas del firewall externo
3. Configurar reglas del firewall interno
4. Identificar puertos necesarios

### Solucion Paso a Paso

#### Paso 1: Diagrama de arquitectura

Internet <-> [Firewall Externo] <-> DMZ (192.168.100.0/24) <-> [Firewall Interno] <-> LAN (10.0.1.0/24)

#### Paso 2: Reglas Firewall Externo (Internet  DMZ)

- ALLOW: any  192.168.100.10:443 (HTTPS pblico)
- ALLOW: any  192.168.100.10:80 (HTTP pblico, redirect a 443)
- DENY: any  192.168.100.0/24:* (todo lo dems bloqueado)

#### Paso 3: Reglas Firewall Interno (DMZ  LAN)

- ALLOW: 192.168.100.10  10.0.1.50:3306 (web server  database interno)
- ALLOW: 10.0.1.0/24  192.168.100.10:22 (admin SSH desde LAN)
- DENY: 192.168.100.0/24  10.0.1.0/24:* (DMZ NO inicia conexiones a LAN)
- ALLOW: 10.0.1.0/24  192.168.100.0/24:* (LAN puede monitorear DMZ)

#### Paso 4: Reglas salida DMZ  Internet (para updates)

- ALLOW: 192.168.100.10  any:443 (HTTPS para updates)
- ALLOW: 192.168.100.10  any:80 (HTTP para updates)
- DENY: 192.168.100.0/24  any:* (resto bloqueado)

### Conceptos Clave

DMZ, Network_Segmentation, Firewall, Defense_in_Depth

### Errores Comunes

- Permitir DMZ  LAN en cualquier puerto = anula la segmentacin
- No bloquear puertos innecesarios en firewall externo
- Olvidar reglas para updates del servidor (quedar sin parchear)

---

## PBQ_02: Implementar Autenticacin 802.1X para Red Corporativa

**Dominio:** Dominio 3 - Arquitectura de Seguridad  
**Dificultad:** ALTA  
**Tiempo estimado:** 20 minutos  

### Escenario

La empresa quiere asegurar el acceso a la red LAN usando 802.1X. Tienes: switches con soporte 802.1X, servidor RADIUS, Active Directory, usuarios con certificados digitales. Necesitas configurar autenticacin tanto para usuarios de dominio como para dispositivos invitados.

### Tareas

1. Seleccionar mtodo EAP apropiado para usuarios corporativos
2. Configurar autenticacin para invitados
3. Definir VLANs de seguridad
4. Configurar fallback para dispositivos no-802.1X

### Solucion Paso a Paso

#### Paso 1: Seleccionar mtodos EAP

**usuarios_corporativos:** EAP-TLS (ms seguro, usa certificados digitales de AD)

**invitados:** PEAP-MSCHAPv2 (usuario/contrasea temporal)

**dispositivos_IoT:** MAB (MAC Authentication Bypass) con whitelist

#### Paso 2: Arquitectura 802.1X

- Supplicant (cliente): Windows con certificado de usuario + mquina
- Authenticator (switch): Cisco con 'dot1x port-control auto'
- Authentication Server (RADIUS): Microsoft NPS integrado con AD

#### Paso 3: Configurar VLANs dinmicas

- VLAN 10 (Empleados): acceso completo, asignada tras EAP-TLS exitoso
- VLAN 20 (Invitados): solo internet, asignada tras PEAP-MSCHAPv2
- VLAN 30 (IoT): segmentada, asignada tras MAB
- VLAN 99 (Cuarentena): sin acceso, asignada si auth falla

#### Paso 4: Configurar switch (ejemplo Cisco)

- interface GigabitEthernet1/0/1
-   switchport mode access
-   authentication port-control auto
-   dot1x pae authenticator
-   authentication order dot1x mab
-   authentication priority dot1x mab
-   authentication fallback GUEST_VLAN

#### Paso 5: Configurar RADIUS (NPS)

- Network Policy 1: IF user in 'Domain Users'  ACCEPT  VLAN 10
- Network Policy 2: IF user in 'Guests'  ACCEPT  VLAN 20
- Network Policy 3: IF MAC in whitelist  ACCEPT  VLAN 30
- Default: REJECT  VLAN 99

### Conceptos Clave

802.1X, RADIUS, EAP-TLS, NAC, VLAN, Microsegmentation

### Errores Comunes

- Usar PEAP para corporativos (menos seguro que EAP-TLS con certificados)
- No configurar fallback = dispositivos legacy sin acceso
- VLAN de cuarentena con acceso a recursos crticos

---

## PBQ_03: Responder a Incidente de Ransomware

**Dominio:** Dominio 4 - Operaciones de Seguridad  
**Dificultad:** ALTA  
**Tiempo estimado:** 25 minutos  

### Escenario

Es lunes 9:00 AM. El sistema de monitoreo alerta que 15 estaciones de trabajo muestran alta actividad de cifrado de archivos. Los usuarios reportan archivos con extensin .locked y nota de rescate exigiendo 50 BTC. Eres el incident responder. El backup ms reciente es de ayer domingo 2:00 AM.

### Tareas

1. Ejecutar las 6 fases del incident response
2. Priorizar acciones inmediatas
3. Preservar evidencia para forensics
4. Decidir si pagar rescate

### Solucion Paso a Paso

#### Paso 1 - Detection & Analysis

**Tiempo:** 9:00-9:15 (15 min)

- Confirmar incidente: verificar en 2-3 estaciones sntomas de ransomware
- Identificar paciente cero: revisar logs (primer equipo infectado)
- Clasificar severidad: CRTICO (ransomware con propagacin activa)
- Activar CSIRT: notificar a equipo de respuesta + management
- Determinar alcance: escanear red completa, identificar 15 hosts afectados

#### Paso 2 - Containment - Short Term

**Tiempo:** 9:15-9:30 (15 min)

- AISLAR hosts infectados: desconectar de red (cable + WiFi), NO APAGAR (preservar RAM)
- Bloquear propagacin: deshabilitar SMBv1, bloquear IPs/dominios C2 en firewall
- Revocar credenciales: resetear contraseas de usuarios afectados (posible robo de credenciales)
- Alertar usuarios: email/Teams indicando NO abrir archivos adjuntos sospechosos

#### Paso 3 - Containment - Long Term

**Tiempo:** 9:30-10:30 (1 hora)

- Segmentar red: crear VLAN de cuarentena para hosts sospechosos no confirmados
- Fortalecer monitoreo: aumentar logging en SIEM, deploy EDR en hosts crticos
- Preservar evidencia: imagen forense de RAM de 1 host infectado, captura trfico red, copiar nota de rescate + archivos cifrados samples

#### Paso 4 - Eradication

**Tiempo:** 10:30-12:00 (1.5 horas)

- Identificar variante: analizar sample con sandbox (ANY.RUN), buscar en ID Ransomware
- Verificar si existe decryptor: consultar No More Ransom Project
- Eliminar malware: format + reinstall OS en 15 hosts afectados
- Cerrar vector de entrada: si fue phishing  reforzar email gateway; si fue RDP  deshabilitar RDP pblico
- Parchear vulnerabilidad: si explot CVE conocido  aplicar patches en toda la red

#### Paso 5 - Recovery

**Tiempo:** 12:00-14:00 (2 horas)

- Restaurar desde backup: recuperar archivos desde backup del domingo 2 AM (prdida: 31 horas de trabajo = aceptable si RPO > 24h)
- Verificar integridad: calcular hash de archivos restaurados vs originales
- Reconectar gradualmente: volver a conectar hosts a red en VLAN monitoreada
- Monitoreo intensivo: vigilar 48 horas por reinfeccin (ransomware puede tener persistencia)

#### Paso 6 - Post-Incident

**Tiempo:** Da 2

- Lessons learned: reunin CSIRT + management
- Actualizar runbook: documentar procedimiento ejecutado
- Mejoras: 1) implementar email sandboxing, 2) training antiphishing, 3) deshabilitar macros por default, 4) considerar segmentacin adicional
- Reportar: notificar a autoridades si aplica (GDPR data breach), informar a cyber insurance

### Conceptos Clave

Incident_Response, Ransomware, Containment, Forensics, Backup, BCP

### Errores Comunes

- Apagar equipos inmediatamente = prdida de evidencia en RAM
- No aislar red = propagacin a toda la empresa
- Restaurar backup sin eliminar malware = reinfeccin inmediata
- No documentar acciones = chain of custody rota

---

## PBQ_04: Configurar SIEM para Detectar Compromiso de Credenciales

**Dominio:** Dominio 4 - Operaciones de Seguridad  
**Dificultad:** MEDIA  
**Tiempo estimado:** 20 minutos  

### Escenario

Tu SIEM (Splunk) recibe logs de: Active Directory, firewalls, VPN, Office 365. Necesitas crear reglas de correlacin para detectar: 1) Brute force attacks, 2) Impossible travel, 3) Privilege escalation. Define las reglas y umbrales.

### Tareas

1. Disear regla de deteccin de brute force
2. Disear regla de impossible travel
3. Disear regla de privilege escalation
4. Definir severidad y respuesta automatizada

### Solucion Paso a Paso

#### Paso 1

#### Paso 2

#### Paso 3

#### Paso 4

### Conceptos Clave

SIEM, Correlation, Brute_Force, Lateral_Movement, SOAR, Threat_Hunting

### Errores Comunes

- No hacer baseline = alertas desde da 1 todas falsas positivas
- Umbrales muy agresivos = alert fatigue  ignorar alertas reales
- No automatizar respuesta = SOC sobrecargado de alertas manuales

---

## PBQ_05: Disear Poltica de Backup segn BCP/DRP

**Dominio:** Dominio 5 - Gestin del Programa de Seguridad  
**Dificultad:** MEDIA  
**Tiempo estimado:** 15 minutos  

### Escenario

Tu empresa tiene: 1) Base de datos de facturacin (RTO=2h, RPO=15min), 2) File server de documentos (RTO=8h, RPO=24h), 3) Email server (RTO=4h, RPO=1h). Presupuesto limitado. Disea estrategia de backup que cumpla objetivos.

### Tareas

1. Seleccionar tipo de backup para cada sistema
2. Definir frecuencia de backups
3. Elegir ubicacin de almacenamiento
4. Calcular ventana de recovery

### Solucion Paso a Paso

#### Paso 1

#### Paso 2

#### Paso 3

#### Paso 4

**3_copias:** Original + copia local + copia cloud

**2_medios:** Disk (NAS) + Tape/Cloud

**1_offsite:** Cloud (protege contra desastre fsico en datacenter)

#### Paso 5

### Conceptos Clave

RTO, RPO, BCP, DRP, Backup, 3-2-1_Rule, Air_Gap

### Errores Comunes

- Backup cada 24h pero RPO=1h = incumplimiento de objetivo
- Todas las copias en mismo datacenter = desastre fsico pierde todo
- Nunca testear recovery = descubrir que backup est corrupto durante emergencia

---

## PBQ_06: Implementar Email Security: SPF, DKIM, DMARC

**Dominio:** Dominio 2 - Amenazas y Mitigaciones  
**Dificultad:** MEDIA  
**Tiempo estimado:** 15 minutos  

### Escenario

Tu empresa 'ejemplo.com' sufre ataques de email spoofing. Necesitas configurar SPF, DKIM y DMARC. Mail enviado desde: Office 365 (outlook.office365.com) y servidor marketing (mailchimp.com).

### Tareas

1. Crear registro SPF en DNS
2. Configurar DKIM
3. Configurar DMARC con poltica progresiva
4. Explicar cmo funciona la validacin

### Solucion Paso a Paso

#### Paso 1: Configurar SPF (Sender Policy Framework)

#### Paso 2: Configurar DKIM (DomainKeys Identified Mail)

#### Paso 3: Configurar DMARC (Domain-based Message Authentication)

#### Paso 4: Flujo de Validacin Completo

### Conceptos Clave

SPF, DKIM, DMARC, Email_Security, Phishing, DNS

### Errores Comunes

- Poner p=reject desde da 1 = bloquear emails legtimos no configurados
- SPF con +all en vez de -all = autoriza a cualquiera (intil)
- No monitorear reportes rua = no detectar problemas de config

---

## PBQ_07: Configurar MFA con Conditional Access

**Dominio:** Dominio 1  
**Dificultad:** MEDIA  

### Escenario

Implementar MFA en Azure AD: siempre para admins, solo fuera de oficina para usuarios normales

### Conceptos Clave

MFA, Conditional_Access, Adaptive_Identity, Azure_AD

---

## PBQ_08: Analizar Logs de Firewall para Detectar Port Scan

**Dominio:** Dominio 2  
**Dificultad:** FCIL  

### Escenario

Logs muestran conexiones desde misma IP a puertos 20-1000 en 2 minutos. Identificar ataque y mitigar

### Conceptos Clave

Port_Scan, Reconnaissance, IDS, Firewall

---

## PBQ_09: Configurar VPN Site-to-Site con IPsec

**Dominio:** Dominio 3  
**Dificultad:** ALTA  

### Escenario

Conectar oficina Madrid (10.0.1.0/24) con Barcelona (10.0.2.0/24) usando IPsec

### Conceptos Clave

IPsec, VPN, IKE, Encryption, Tunnel_Mode

---

## PBQ_10: Hardening de Servidor Linux

**Dominio:** Dominio 3  
**Dificultad:** MEDIA  

### Escenario

Aplicar 10 controles de hardening en Ubuntu Server: deshabilitar servicios, firewall, SSH seguro, etc

### Conceptos Clave

Hardening, Least_Privilege, SSH, iptables, SELinux

---

## PBQ_11: Anlisis de Malware con Sandbox

**Dominio:** Dominio 4  
**Dificultad:** MEDIA  

### Escenario

Archivo adjunto sospechoso. Usar ANY.RUN para anlisis dinmico e identificar IOCs

### Conceptos Clave

Sandbox, Malware_Analysis, IOC, Dynamic_Analysis, Threat_Intelligence

---

## PBQ_12: Crear Poltica de Contraseas Segura

**Dominio:** Dominio 1  
**Dificultad:** FCIL  

### Escenario

Disear poltica de contraseas que balancee seguridad y usabilidad (longitud, complejidad, rotacin)

### Conceptos Clave

Password_Policy, Authentication, NIST_Guidelines, Password_Manager

---

## PBQ_13: Configurar Certificate Pinning en App Mvil

**Dominio:** Dominio 3  
**Dificultad:** ALTA  

### Escenario

Prevenir MITM en app Android haciendo pinning del certificado del servidor

### Conceptos Clave

Certificate_Pinning, MITM, TLS, Mobile_Security, PKI

---

## PBQ_14: Responder a Data Breach segn GDPR

**Dominio:** Dominio 5  
**Dificultad:** ALTA  

### Escenario

Base de datos con 50k usuarios UE comprometida. Pasos legales en 72h

### Conceptos Clave

GDPR, Data_Breach, Incident_Response, Notification, DPA

---

## PBQ_15: Configurar WAF para Prevenir SQLi y XSS

**Dominio:** Dominio 3  
**Dificultad:** MEDIA  

### Escenario

Configurar reglas en AWS WAF para bloquear inyeccin SQL y XSS en aplicacin web

### Conceptos Clave

WAF, SQLi, XSS, OWASP_Top_10, Input_Validation

---

