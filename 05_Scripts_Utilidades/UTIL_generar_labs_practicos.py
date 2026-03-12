#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera guías de laboratorios prácticos basados en los conceptos de Security+
Organizado por dominios con ejercicios hands-on
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import json
from pathlib import Path

JSON_PATH = Path(r"D:\Users\cra\Desktop\Sec+\03_JSON_Datos\secplus_estructurado.json")
OUTPUT_DIR = Path(r"D:\Users\cra\Desktop\Sec+\07_Laboratorios")

print("="*80)
print(" GENERADOR DE LABORATORIOS PRACTICOS - Security+ SY0-701")
print("="*80)

# Crear directorio si no existe
OUTPUT_DIR.mkdir(exist_ok=True)

# Cargar datos
with open(JSON_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Definir laboratorios por dominio
laboratorios = {
    "1": {
        "nombre": "Dominio 1 - Conceptos Generales de Seguridad",
        "labs": [
            {
                "id": "LAB-1.1",
                "titulo": "Configuración de PKI y Certificados",
                "objetivos": ["1.4"],
                "conceptos": ["PKI", "CA", "Certificados X.509", "CRL", "OCSP"],
                "dificultad": "Media",
                "tiempo": "45-60 min",
                "requisitos": ["Windows Server o Linux", "OpenSSL"],
                "tareas": [
                    "1. Instalar OpenSSL y verificar versión",
                    "2. Crear CA raíz (Root CA) privada",
                    "3. Generar certificado autofirmado para la CA",
                    "4. Crear solicitud de certificado (CSR) para servidor web",
                    "5. Firmar el CSR con la CA raíz",
                    "6. Verificar cadena de certificados",
                    "7. Configurar CRL (Certificate Revocation List)",
                    "8. Revocar un certificado y verificar CRL",
                    "9. EXTRA: Implementar OCSP responder"
                ],
                "comandos": [
                    "# Generar clave privada CA",
                    "openssl genrsa -aes256 -out ca-key.pem 4096",
                    "",
                    "# Crear certificado CA autofirmado",
                    "openssl req -new -x509 -days 3650 -key ca-key.pem -sha256 -out ca.pem",
                    "",
                    "# Generar clave privada servidor",
                    "openssl genrsa -out server-key.pem 4096",
                    "",
                    "# Crear CSR",
                    "openssl req -new -key server-key.pem -out server.csr",
                    "",
                    "# Firmar certificado servidor",
                    "openssl x509 -req -days 365 -in server.csr -CA ca.pem -CAkey ca-key.pem -CAcreateserial -out server-cert.pem",
                    "",
                    "# Verificar certificado",
                    "openssl x509 -in server-cert.pem -text -noout",
                    "",
                    "# Verificar cadena",
                    "openssl verify -CAfile ca.pem server-cert.pem"
                ],
                "preguntas_repaso": [
                    "¿Cuál es la diferencia entre CA raíz e intermedia?",
                    "¿Qué información contiene un certificado X.509?",
                    "¿Por qué es importante la CRL/OCSP?",
                    "¿Qué es un certificado wildcard vs SAN?"
                ]
            },
            {
                "id": "LAB-1.2",
                "titulo": "Implementación de Zero Trust con VPN y MFA",
                "objetivos": ["1.2"],
                "conceptos": ["Zero Trust", "VPN", "MFA", "RADIUS"],
                "dificultad": "Alta",
                "tiempo": "90 min",
                "requisitos": ["Linux VM", "FreeRADIUS", "OpenVPN", "Google Authenticator"],
                "tareas": [
                    "1. Instalar y configurar OpenVPN server",
                    "2. Configurar FreeRADIUS como AAA server",
                    "3. Integrar Google Authenticator (TOTP) con RADIUS",
                    "4. Configurar OpenVPN para usar RADIUS",
                    "5. Crear usuarios con MFA obligatorio",
                    "6. Probar conexión VPN con usuario+password+OTP",
                    "7. Verificar logs de autenticación",
                    "8. Implementar política de least privilege",
                    "9. EXTRA: Configurar split-tunneling"
                ],
                "comandos": [
                    "# Instalar OpenVPN",
                    "sudo apt update && sudo apt install openvpn easy-rsa",
                    "",
                    "# Instalar FreeRADIUS",
                    "sudo apt install freeradius freeradius-utils",
                    "",
                    "# Instalar Google Authenticator",
                    "sudo apt install libpam-google-authenticator",
                    "",
                    "# Generar secreto OTP para usuario",
                    "google-authenticator",
                    "",
                    "# Verificar RADIUS",
                    "sudo freeradius -X",
                    "",
                    "# Probar autenticación",
                    "radtest usuario password localhost 0 testing123"
                ],
                "preguntas_repaso": [
                    "¿Cuál es el principio fundamental de Zero Trust?",
                    "¿Qué es AAA en el contexto de RADIUS?",
                    "¿Diferencia entre TOTP y HOTP?",
                    "¿Por qué es importante el split-tunneling?"
                ]
            },
            {
                "id": "LAB-1.3",
                "titulo": "Cifrado Simétrico vs Asimétrico - Casos Prácticos",
                "objetivos": ["1.4"],
                "conceptos": ["AES", "RSA", "ECC", "Hash", "SHA-256"],
                "dificultad": "Baja",
                "tiempo": "30-45 min",
                "requisitos": ["OpenSSL", "Python 3"],
                "tareas": [
                    "1. Cifrar archivo con AES-256-CBC (simétrico)",
                    "2. Descifrar archivo con clave simétrica",
                    "3. Generar par de claves RSA (asimétrico)",
                    "4. Cifrar datos pequeños con RSA público",
                    "5. Descifrar con RSA privado",
                    "6. Generar hash SHA-256 de un archivo",
                    "7. Verificar integridad con hash",
                    "8. Firmar digitalmente un documento",
                    "9. Verificar firma digital"
                ],
                "comandos": [
                    "# Cifrar archivo con AES-256",
                    "openssl enc -aes-256-cbc -salt -in archivo.txt -out archivo.enc",
                    "",
                    "# Descifrar",
                    "openssl enc -d -aes-256-cbc -in archivo.enc -out archivo.txt",
                    "",
                    "# Generar par RSA",
                    "openssl genrsa -out private.pem 2048",
                    "openssl rsa -in private.pem -pubout -out public.pem",
                    "",
                    "# Cifrar con RSA (archivos pequeños)",
                    "openssl rsautl -encrypt -inkey public.pem -pubin -in mensaje.txt -out mensaje.enc",
                    "",
                    "# Descifrar con RSA",
                    "openssl rsautl -decrypt -inkey private.pem -in mensaje.enc -out mensaje.txt",
                    "",
                    "# Hash SHA-256",
                    "openssl dgst -sha256 archivo.txt",
                    "",
                    "# Firmar digitalmente",
                    "openssl dgst -sha256 -sign private.pem -out firma.sig archivo.txt",
                    "",
                    "# Verificar firma",
                    "openssl dgst -sha256 -verify public.pem -signature firma.sig archivo.txt"
                ],
                "preguntas_repaso": [
                    "¿Cuándo usar cifrado simétrico vs asimétrico?",
                    "¿Por qué RSA no se usa para cifrar archivos grandes?",
                    "¿Diferencia entre cifrado e integridad?",
                    "¿Qué es una firma digital y cómo funciona?"
                ]
            }
        ]
    },
    "2": {
        "nombre": "Dominio 2 - Amenazas, Vulnerabilidades y Mitigaciones",
        "labs": [
            {
                "id": "LAB-2.1",
                "titulo": "Análisis de Malware con Sandboxing",
                "objetivos": ["2.4"],
                "conceptos": ["Malware", "Sandbox", "IOC", "Análisis dinámico"],
                "dificultad": "Media",
                "tiempo": "60 min",
                "requisitos": ["VirtualBox", "VM Windows/Linux", "Wireshark"],
                "tareas": [
                    "1. Crear snapshot de VM limpia (sandboxing)",
                    "2. Descargar muestra de malware (ej: EICAR test file)",
                    "3. Desactivar red o crear red aislada",
                    "4. Monitorizar con Process Monitor (Windows) o strace (Linux)",
                    "5. Ejecutar malware y observar comportamiento",
                    "6. Capturar tráfico de red con Wireshark",
                    "7. Analizar cambios en sistema de archivos",
                    "8. Identificar IOCs (IPs, dominios, hashes)",
                    "9. Restaurar snapshot y documentar hallazgos"
                ],
                "comandos": [
                    "# Crear snapshot VM (VirtualBox)",
                    "vboxmanage snapshot 'NombreVM' take 'Clean_State'",
                    "",
                    "# Hash del archivo",
                    "sha256sum malware.exe",
                    "",
                    "# Captura de red",
                    "sudo tcpdump -i eth0 -w captura.pcap",
                    "",
                    "# Monitorizar procesos (Linux)",
                    "strace -f -o trace.log ./malware",
                    "",
                    "# Buscar cambios en archivos",
                    "find / -type f -mmin -5 2>/dev/null",
                    "",
                    "# Restaurar snapshot",
                    "vboxmanage snapshot 'NombreVM' restore 'Clean_State'"
                ],
                "preguntas_repaso": [
                    "¿Qué es un IOC y por qué es importante?",
                    "¿Diferencia entre análisis estático y dinámico?",
                    "¿Por qué es crítico usar sandbox para malware?",
                    "¿Qué son fileless malware y cómo detectarlos?"
                ]
            },
            {
                "id": "LAB-2.2",
                "titulo": "Ataques Web: SQLi y XSS Práctico",
                "objetivos": ["2.3"],
                "conceptos": ["SQLi", "XSS", "OWASP Top 10", "WAF"],
                "dificultad": "Media",
                "tiempo": "75 min",
                "requisitos": ["DVWA", "Burp Suite Community", "Docker"],
                "tareas": [
                    "1. Desplegar DVWA (Damn Vulnerable Web App) con Docker",
                    "2. Configurar nivel de seguridad bajo",
                    "3. Identificar input vulnerable a SQLi",
                    "4. Realizar SQLi manual (1' OR '1'='1)",
                    "5. Extraer datos con UNION SELECT",
                    "6. Probar XSS reflejado con <script>alert(1)</script>",
                    "7. Probar XSS almacenado en comentarios",
                    "8. Configurar Burp Suite como proxy",
                    "9. Capturar y modificar peticiones",
                    "10. Implementar mitigaciones (prepared statements, sanitización)"
                ],
                "comandos": [
                    "# Desplegar DVWA con Docker",
                    "docker run -d -p 80:80 vulnerables/web-dvwa",
                    "",
                    "# Acceder a DVWA",
                    "# http://localhost",
                    "# Login: admin / password",
                    "",
                    "# SQLi básico en campo de login",
                    "# Usuario: admin' OR '1'='1' --",
                    "# Password: cualquiera",
                    "",
                    "# SQLi para extraer datos",
                    "# ' UNION SELECT user, password FROM users --",
                    "",
                    "# XSS reflejado",
                    "# <script>alert(document.cookie)</script>",
                    "",
                    "# XSS almacenado",
                    "# <img src=x onerror=alert('XSS')>"
                ],
                "preguntas_repaso": [
                    "¿Cómo funciona un ataque de SQL Injection?",
                    "¿Diferencia entre XSS reflejado y almacenado?",
                    "¿Qué son prepared statements y cómo previenen SQLi?",
                    "¿Cómo mitigar XSS con Content Security Policy (CSP)?"
                ]
            },
            {
                "id": "LAB-2.3",
                "titulo": "Reconnaissance y OSINT con MITRE ATT&CK",
                "objetivos": ["2.5"],
                "conceptos": ["MITRE ATT&CK", "OSINT", "Reconnaissance", "Footprinting"],
                "dificultad": "Baja",
                "tiempo": "45 min",
                "requisitos": ["Kali Linux", "theHarvester", "Shodan", "Maltego CE"],
                "tareas": [
                    "1. Mapear tácticas de Reconnaissance en MITRE ATT&CK",
                    "2. Usar theHarvester para recopilar emails/subdominios",
                    "3. Consultar Shodan para dispositivos IoT expuestos",
                    "4. Realizar whois lookup de dominio objetivo",
                    "5. Enumerar subdominios con subfinder",
                    "6. Buscar leaks de credenciales en HaveIBeenPwned",
                    "7. Documentar hallazgos en formato TTP",
                    "8. Mapear hallazgos a MITRE ATT&CK Navigator"
                ],
                "comandos": [
                    "# theHarvester - recopilar info",
                    "theHarvester -d example.com -b google,bing,linkedin",
                    "",
                    "# Whois lookup",
                    "whois example.com",
                    "",
                    "# Subfinder - enumerar subdominios",
                    "subfinder -d example.com -o subdominios.txt",
                    "",
                    "# Shodan CLI (requiere API key)",
                    "shodan search 'org:\"Example Corp\"'",
                    "",
                    "# DNSRecon",
                    "dnsrecon -d example.com -t std",
                    "",
                    "# Nmap para OS fingerprinting",
                    "nmap -O -sV example.com"
                ],
                "preguntas_repaso": [
                    "¿Cuáles son las 14 tácticas de MITRE ATT&CK?",
                    "¿Diferencia entre activo y pasivo reconnaissance?",
                    "¿Por qué es importante OSINT en pentesting?",
                    "¿Qué es footprinting y enumeration?"
                ]
            }
        ]
    },
    "3": {
        "nombre": "Dominio 3 - Arquitectura de Seguridad",
        "labs": [
            {
                "id": "LAB-3.1",
                "titulo": "Configuración de Firewall y Segmentación de Red",
                "objetivos": ["3.2"],
                "conceptos": ["Firewall", "VLAN", "ACL", "Network Segmentation"],
                "dificultad": "Media",
                "tiempo": "60 min",
                "requisitos": ["pfSense VM", "2+ VMs Linux", "VirtualBox/VMware"],
                "tareas": [
                    "1. Instalar pfSense como firewall virtual",
                    "2. Configurar 3 interfaces: WAN, LAN, DMZ",
                    "3. Crear reglas de firewall para separar redes",
                    "4. Configurar VLAN para segmentar DMZ",
                    "5. Implementar regla deny-all por defecto",
                    "6. Permitir solo HTTP/HTTPS desde LAN a DMZ",
                    "7. Bloquear todo tráfico directo Internet → DMZ",
                    "8. Configurar NAT para LAN",
                    "9. Probar conectividad y verificar logs"
                ],
                "comandos": [
                    "# Desde VM en LAN - probar conectividad",
                    "ping 192.168.1.1  # Gateway pfSense",
                    "",
                    "# Probar acceso web a DMZ",
                    "curl http://192.168.2.10",
                    "",
                    "# Intentar SSH (debería fallar si está bloqueado)",
                    "ssh user@192.168.2.10",
                    "",
                    "# Verificar rutas",
                    "ip route show",
                    "",
                    "# Traceroute para ver saltos",
                    "traceroute 8.8.8.8"
                ],
                "preguntas_repaso": [
                    "¿Qué es una DMZ y por qué es importante?",
                    "¿Diferencia entre stateful y stateless firewall?",
                    "¿Qué es una VLAN y cómo ayuda a la seguridad?",
                    "¿Por qué usar deny-all como regla por defecto?"
                ]
            },
            {
                "id": "LAB-3.2",
                "titulo": "IDS/IPS con Suricata + ELK Stack",
                "objetivos": ["3.2"],
                "conceptos": ["IDS", "IPS", "Suricata", "SIEM", "ELK"],
                "dificultad": "Alta",
                "tiempo": "90 min",
                "requisitos": ["Linux VM", "Suricata", "Elasticsearch", "Kibana"],
                "tareas": [
                    "1. Instalar Suricata IDS/IPS",
                    "2. Configurar interfaz de red en modo promiscuo",
                    "3. Descargar reglas ET Open (Emerging Threats)",
                    "4. Configurar Suricata en modo IPS (inline)",
                    "5. Instalar ELK Stack (Elasticsearch, Logstash, Kibana)",
                    "6. Configurar Filebeat para enviar logs a ELK",
                    "7. Generar tráfico malicioso de prueba (ej: nmap scan)",
                    "8. Visualizar alertas en Kibana",
                    "9. Crear dashboard personalizado para eventos"
                ],
                "comandos": [
                    "# Instalar Suricata",
                    "sudo apt install suricata",
                    "",
                    "# Descargar reglas",
                    "sudo suricata-update",
                    "",
                    "# Ejecutar Suricata",
                    "sudo suricata -c /etc/suricata/suricata.yaml -i eth0",
                    "",
                    "# Ver logs en tiempo real",
                    "sudo tail -f /var/log/suricata/fast.log",
                    "",
                    "# Generar alerta (desde otra VM)",
                    "nmap -sS -p- 192.168.1.100",
                    "",
                    "# Verificar alertas JSON",
                    "sudo cat /var/log/suricata/eve.json | jq '.event_type'",
                    "",
                    "# Instalar ELK (Docker Compose recomendado)",
                    "docker-compose up -d elasticsearch kibana logstash"
                ],
                "preguntas_repaso": [
                    "¿Diferencia entre IDS e IPS?",
                    "¿Qué es un SIEM y por qué es importante?",
                    "¿Signature-based vs anomaly-based detection?",
                    "¿Por qué enviar logs a sistema externo?"
                ]
            },
            {
                "id": "LAB-3.3",
                "titulo": "Destrucción Segura de Datos y Crypto-Shredding",
                "objetivos": ["3.3"],
                "conceptos": ["Data Sanitization", "Crypto-shredding", "Secure Erase"],
                "dificultad": "Media",
                "tiempo": "45 min",
                "requisitos": ["Linux VM", "USB/disco adicional", "LUKS", "shred"],
                "tareas": [
                    "1. Crear disco virtual o usar USB para pruebas",
                    "2. Escribir datos sensibles en disco",
                    "3. Usar 'shred' para sobrescritura múltiple (método tradicional)",
                    "4. Verificar que datos no son recuperables",
                    "5. Crear volumen cifrado con LUKS (crypto-shredding)",
                    "6. Copiar datos al volumen cifrado",
                    "7. Realizar crypto-shredding (borrar solo la clave)",
                    "8. Intentar recuperar datos (imposible sin clave)",
                    "9. Comparar tiempo: shred vs crypto-shredding"
                ],
                "comandos": [
                    "# Método 1: Shred (sobrescritura múltiple)",
                    "sudo shred -vfz -n 7 /dev/sdb  # 7 pasadas",
                    "",
                    "# Crear archivo de prueba",
                    "dd if=/dev/urandom of=datos_sensibles.txt bs=1M count=100",
                    "",
                    "# Shred de archivo",
                    "shred -vfz -n 3 datos_sensibles.txt",
                    "",
                    "# Método 2: Crypto-shredding con LUKS",
                    "sudo cryptsetup luksFormat /dev/sdb",
                    "",
                    "# Abrir volumen cifrado",
                    "sudo cryptsetup luksOpen /dev/sdb datos_cifrados",
                    "",
                    "# Crear filesystem",
                    "sudo mkfs.ext4 /dev/mapper/datos_cifrados",
                    "",
                    "# Montar y copiar datos",
                    "sudo mount /dev/mapper/datos_cifrados /mnt",
                    "sudo cp datos_sensibles.txt /mnt/",
                    "",
                    "# Crypto-shredding (borrar header LUKS)",
                    "sudo cryptsetup luksErase /dev/sdb",
                    "",
                    "# Datos ahora irrecuperables (clave destruida)"
                ],
                "preguntas_repaso": [
                    "¿Por qué shred tradicional NO funciona bien en SSD?",
                    "¿Qué es wear leveling en SSD?",
                    "¿Cómo funciona crypto-shredding?",
                    "¿Cuándo usar ATA Secure Erase vs crypto-shredding?"
                ]
            }
        ]
    },
    "4": {
        "nombre": "Dominio 4 - Operaciones de Seguridad",
        "labs": [
            {
                "id": "LAB-4.1",
                "titulo": "Hardening de Servidor Linux con CIS Benchmarks",
                "objetivos": ["4.1"],
                "conceptos": ["Hardening", "CIS Benchmark", "Least Privilege", "AppArmor"],
                "dificultad": "Media",
                "tiempo": "60 min",
                "requisitos": ["Ubuntu Server VM", "OpenSCAP", "Lynis"],
                "tareas": [
                    "1. Realizar auditoría inicial con Lynis",
                    "2. Desactivar servicios innecesarios",
                    "3. Configurar firewall UFW (deny-all + allow SSH)",
                    "4. Implementar fail2ban contra brute force",
                    "5. Deshabilitar root login por SSH",
                    "6. Configurar autenticación por clave SSH (sin password)",
                    "7. Actualizar sistema y aplicar parches",
                    "8. Configurar AppArmor para confinar aplicaciones",
                    "9. Re-auditar con Lynis y comparar score"
                ],
                "comandos": [
                    "# Auditoría inicial",
                    "sudo lynis audit system",
                    "",
                    "# Ver servicios activos",
                    "systemctl list-unit-files --state=enabled",
                    "",
                    "# Desactivar servicio innecesario",
                    "sudo systemctl disable cups",
                    "",
                    "# Configurar UFW",
                    "sudo ufw default deny incoming",
                    "sudo ufw default allow outgoing",
                    "sudo ufw allow 22/tcp",
                    "sudo ufw enable",
                    "",
                    "# Instalar fail2ban",
                    "sudo apt install fail2ban",
                    "sudo systemctl enable fail2ban",
                    "",
                    "# Deshabilitar root SSH (/etc/ssh/sshd_config)",
                    "# PermitRootLogin no",
                    "# PasswordAuthentication no",
                    "sudo systemctl restart sshd",
                    "",
                    "# Verificar AppArmor",
                    "sudo aa-status",
                    "",
                    "# Actualizar sistema",
                    "sudo apt update && sudo apt upgrade -y"
                ],
                "preguntas_repaso": [
                    "¿Qué es hardening y por qué es importante?",
                    "¿Qué son los CIS Benchmarks?",
                    "¿Diferencia entre AppArmor y SELinux?",
                    "¿Por qué deshabilitar servicios innecesarios?"
                ]
            },
            {
                "id": "LAB-4.2",
                "titulo": "Respuesta a Incidentes - Análisis Forense",
                "objetivos": ["4.8"],
                "conceptos": ["Incident Response", "Digital Forensics", "Chain of Custody", "Memory Dump"],
                "dificultad": "Alta",
                "tiempo": "90 min",
                "requisitos": ["Kali Linux", "Volatility", "Autopsy", "VM comprometida"],
                "tareas": [
                    "1. Escenario: detectar sistema comprometido",
                    "2. PRESERVAR evidencia (no modificar sistema)",
                    "3. Crear imagen forense del disco con dd",
                    "4. Calcular hash de la imagen (cadena de custodia)",
                    "5. Capturar memoria RAM con LiME",
                    "6. Analizar memoria con Volatility (procesos, conexiones)",
                    "7. Analizar disco con Autopsy",
                    "8. Identificar IOCs (malware, backdoors, logs)",
                    "9. Documentar hallazgos en informe forense"
                ],
                "comandos": [
                    "# Crear imagen forense del disco",
                    "sudo dd if=/dev/sda of=evidencia.img bs=4M status=progress",
                    "",
                    "# Hash de imagen (chain of custody)",
                    "sha256sum evidencia.img > evidencia.sha256",
                    "",
                    "# Capturar memoria RAM (LiME)",
                    "sudo insmod lime-*.ko \"path=/tmp/memoria.lime format=lime\"",
                    "",
                    "# Analizar memoria con Volatility",
                    "volatility -f memoria.lime --profile=LinuxUbuntu imageinfo",
                    "volatility -f memoria.lime --profile=LinuxUbuntu linux_pslist",
                    "volatility -f memoria.lime --profile=LinuxUbuntu linux_netstat",
                    "",
                    "# Buscar procesos ocultos",
                    "volatility -f memoria.lime --profile=LinuxUbuntu linux_psxview",
                    "",
                    "# Montar imagen forense (read-only)",
                    "sudo mount -o ro,loop evidencia.img /mnt/forense",
                    "",
                    "# Analizar con Autopsy (GUI)",
                    "autopsy"
                ],
                "preguntas_repaso": [
                    "¿Qué es la cadena de custodia y por qué es crítica?",
                    "¿Por qué capturar memoria RAM además del disco?",
                    "¿Orden de volatilidad en forensics (RFC 3227)?",
                    "¿Diferencia entre dead box y live response?"
                ]
            },
            {
                "id": "LAB-4.3",
                "titulo": "SIEM con Wazuh - Detección y Alertas",
                "objetivos": ["4.4", "4.9"],
                "conceptos": ["SIEM", "Log Management", "Correlation Rules", "Wazuh"],
                "dificultad": "Alta",
                "tiempo": "90 min",
                "requisitos": ["Wazuh Manager", "Agents (Linux/Windows)", "Docker"],
                "tareas": [
                    "1. Desplegar Wazuh Manager con Docker",
                    "2. Instalar agentes Wazuh en VMs (Linux + Windows)",
                    "3. Configurar recolección de logs centralizados",
                    "4. Crear regla personalizada (alerta login fallido 5+ veces)",
                    "5. Generar eventos de prueba (intentos login fallidos)",
                    "6. Verificar alertas en dashboard Wazuh",
                    "7. Configurar integración con VirusTotal (file integrity)",
                    "8. Probar FIM (File Integrity Monitoring)",
                    "9. Crear reporte de eventos de seguridad"
                ],
                "comandos": [
                    "# Desplegar Wazuh con Docker",
                    "docker-compose -f wazuh-docker.yml up -d",
                    "",
                    "# Instalar agente Linux",
                    "wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.x.x_amd64.deb",
                    "sudo WAZUH_MANAGER='192.168.1.100' dpkg -i wazuh-agent_*.deb",
                    "sudo systemctl enable wazuh-agent",
                    "sudo systemctl start wazuh-agent",
                    "",
                    "# Verificar conectividad agente",
                    "sudo /var/ossec/bin/agent_control -lc",
                    "",
                    "# Ver logs del agente",
                    "sudo tail -f /var/ossec/logs/ossec.log",
                    "",
                    "# Generar eventos de prueba (login fallido)",
                    "for i in {1..6}; do ssh wronguser@localhost; done",
                    "",
                    "# Acceder dashboard Wazuh",
                    "# https://localhost:443",
                    "# admin / admin (cambiar contraseña)"
                ],
                "preguntas_repaso": [
                    "¿Qué es un SIEM y cuál es su función principal?",
                    "¿Por qué centralizar logs es crítico?",
                    "¿Qué es correlation en un SIEM?",
                    "¿Diferencia entre SIEM y SOAR?"
                ]
            }
        ]
    },
    "5": {
        "nombre": "Dominio 5 - Gestión del Programa de Seguridad",
        "labs": [
            {
                "id": "LAB-5.1",
                "titulo": "Análisis de Riesgos - Cálculo ALE/SLE/ARO",
                "objetivos": ["5.2"],
                "conceptos": ["Risk Management", "ALE", "SLE", "ARO", "Risk Matrix"],
                "dificultad": "Baja",
                "tiempo": "45 min",
                "requisitos": ["Excel/LibreOffice", "Calculadora"],
                "tareas": [
                    "1. Identificar 5 activos críticos de tu organización",
                    "2. Identificar amenazas para cada activo",
                    "3. Calcular SLE (pérdida por incidente único)",
                    "4. Estimar ARO (frecuencia anual)",
                    "5. Calcular ALE = SLE × ARO",
                    "6. Crear matriz de riesgos (probabilidad × impacto)",
                    "7. Proponer controles y calcular coste",
                    "8. Decidir estrategia: Aceptar/Transferir/Mitigar/Evitar",
                    "9. Documentar en risk register"
                ],
                "ejemplos": [
                    "Ejemplo 1:",
                    "  Activo: Servidor web producción",
                    "  Amenaza: Ataque DDoS",
                    "  SLE: $50,000 (pérdida ventas + reputación)",
                    "  ARO: 0.5 (1 vez cada 2 años)",
                    "  ALE = $50,000 × 0.5 = $25,000/año",
                    "  Control: Servicio anti-DDoS = $15,000/año",
                    "  Decisión: MITIGAR (ROI positivo)",
                    "",
                    "Ejemplo 2:",
                    "  Activo: Laptops empleados",
                    "  Amenaza: Robo/pérdida",
                    "  SLE: $2,000 (hardware + datos)",
                    "  ARO: 2 (2 pérdidas al año)",
                    "  ALE = $2,000 × 2 = $4,000/año",
                    "  Control: Cifrado disco + seguro = $3,000/año",
                    "  Decisión: MITIGAR + TRANSFERIR"
                ],
                "preguntas_repaso": [
                    "¿Qué es ALE y cómo se calcula?",
                    "¿Diferencia entre riesgo inherente y residual?",
                    "¿Cuándo aceptar un riesgo vs mitigarlo?",
                    "¿Qué es risk appetite vs risk tolerance?"
                ]
            },
            {
                "id": "LAB-5.2",
                "titulo": "Auditoría de Compliance - GDPR/HIPAA/PCI DSS",
                "objetivos": ["5.4", "5.5"],
                "conceptos": ["Compliance", "GDPR", "PCI DSS", "Audit", "Gap Analysis"],
                "dificultad": "Media",
                "tiempo": "60 min",
                "requisitos": ["Checklist compliance", "Documentación organización"],
                "tareas": [
                    "1. Seleccionar framework aplicable (GDPR/HIPAA/PCI DSS)",
                    "2. Descargar checklist oficial del framework",
                    "3. Realizar gap analysis (estado actual vs requerido)",
                    "4. Documentar controles implementados",
                    "5. Identificar gaps críticos",
                    "6. Crear plan de remediación priorizado",
                    "7. Estimar coste y tiempo de implementación",
                    "8. Preparar evidencias para auditoría externa",
                    "9. Generar informe ejecutivo para dirección"
                ],
                "ejemplos": [
                    "GDPR - Ejemplos de verificación:",
                    "  ☐ ¿Hay DPO (Data Protection Officer) designado?",
                    "  ☐ ¿Existe registro de actividades de tratamiento?",
                    "  ☐ ¿Se puede ejercer derecho de supresión (<30 días)?",
                    "  ☐ ¿Hay proceso de notificación de brechas (<72h)?",
                    "  ☐ ¿DPIAs realizadas para alto riesgo?",
                    "",
                    "PCI DSS - Ejemplos:",
                    "  ☐ ¿Datos de tarjetas cifrados en reposo (AES-256)?",
                    "  ☐ ¿Segmentación de red (CDE aislado)?",
                    "  ☐ ¿Logs centralizados y retenidos 1+ año?",
                    "  ☐ ¿Pentesting anual + scan trimestral ASV?",
                    "  ☐ ¿Política de contraseñas cumple requisitos?"
                ],
                "preguntas_repaso": [
                    "¿Diferencia entre GDPR y HIPAA?",
                    "¿Qué es un gap analysis?",
                    "¿Cuándo es obligatorio PCI DSS?",
                    "¿Qué es una DPIA y cuándo es necesaria?"
                ]
            },
            {
                "id": "LAB-5.3",
                "titulo": "Evaluación de Proveedores (Third-Party Risk)",
                "objetivos": ["5.3"],
                "conceptos": ["Third-Party Risk", "Vendor Assessment", "SLA", "Due Diligence"],
                "dificultad": "Baja",
                "tiempo": "45 min",
                "requisitos": ["Cuestionario vendor assessment", "Template SLA"],
                "tareas": [
                    "1. Crear cuestionario de seguridad para proveedores",
                    "2. Evaluar proveedor cloud (ej: AWS, Azure, GCP)",
                    "3. Verificar certificaciones (ISO 27001, SOC 2)",
                    "4. Revisar política de retención de datos",
                    "5. Verificar ubicación geográfica de datos (GDPR)",
                    "6. Analizar SLA (uptime, tiempo respuesta incidentes)",
                    "7. Revisar cláusula de right-to-audit",
                    "8. Verificar exit strategy (portabilidad datos)",
                    "9. Documentar fourth-party risks (sub-proveedores)"
                ],
                "ejemplos": [
                    "Cuestionario de evaluación (ejemplos):",
                    "",
                    "Seguridad Técnica:",
                    "  ☐ ¿Cifrado en tránsito (TLS 1.2+)?",
                    "  ☐ ¿Cifrado en reposo (AES-256)?",
                    "  ☐ ¿MFA obligatorio para acceso administrativo?",
                    "  ☐ ¿Pentesting periódico por terceros?",
                    "",
                    "Compliance:",
                    "  ☐ ¿Certificación ISO 27001 vigente?",
                    "  ☐ ¿SOC 2 Type II report disponible?",
                    "  ☐ ¿Cumple GDPR (si datos UE)?",
                    "",
                    "Continuidad:",
                    "  ☐ ¿SLA de uptime (99.9%+)?",
                    "  ☐ ¿RTO/RPO documentados?",
                    "  ☐ ¿Plan de backup y DR probado?",
                    "",
                    "Contractual:",
                    "  ☐ ¿Cláusula right-to-audit incluida?",
                    "  ☐ ¿Data ownership clarificado?",
                    "  ☐ ¿Exit strategy y portabilidad datos?"
                ],
                "preguntas_repaso": [
                    "¿Qué es third-party risk?",
                    "¿Por qué es importante el right-to-audit?",
                    "¿Qué es vendor lock-in y cómo mitigarlo?",
                    "¿Diferencia entre SLA, MSA y BPA?"
                ]
            }
        ]
    }
}

print("\nGenerando guías de laboratorio...")

# Generar índice general
index_content = []
index_content.append("="*80)
index_content.append(" INDICE DE LABORATORIOS PRACTICOS - Security+ SY0-701")
index_content.append("="*80)
index_content.append("")
index_content.append("Total de laboratorios: 15 (3 por dominio)")
index_content.append("Tiempo total estimado: ~17 horas de práctica")
index_content.append("")

for dom_id, dom_data in sorted(laboratorios.items()):
    index_content.append(f"\n{dom_data['nombre']}")
    index_content.append("-"*80)
    for lab in dom_data['labs']:
        index_content.append(f"  {lab['id']} - {lab['titulo']}")
        index_content.append(f"           Dificultad: {lab['dificultad']} | Tiempo: {lab['tiempo']}")
        index_content.append(f"           Conceptos: {', '.join(lab['conceptos'])}")
    index_content.append("")

# Guardar índice
with open(OUTPUT_DIR / "00_INDICE_LABORATORIOS.txt", 'w', encoding='utf-8') as f:
    f.write("\n".join(index_content))

print(f"[OK] Índice creado: {OUTPUT_DIR / '00_INDICE_LABORATORIOS.txt'}")

# Generar guía detallada para cada laboratorio
for dom_id, dom_data in sorted(laboratorios.items()):
    for lab in dom_data['labs']:
        lab_content = []
        lab_content.append("="*80)
        lab_content.append(f" {lab['id']} - {lab['titulo']}")
        lab_content.append("="*80)
        lab_content.append("")
        lab_content.append(f"DOMINIO: {dom_data['nombre']}")
        lab_content.append(f"OBJETIVOS: {', '.join(lab['objetivos'])}")
        lab_content.append(f"CONCEPTOS: {', '.join(lab['conceptos'])}")
        lab_content.append(f"DIFICULTAD: {lab['dificultad']}")
        lab_content.append(f"TIEMPO ESTIMADO: {lab['tiempo']}")
        lab_content.append("")

        lab_content.append("-"*80)
        lab_content.append(" REQUISITOS PREVIOS")
        lab_content.append("-"*80)
        for req in lab['requisitos']:
            lab_content.append(f"  • {req}")
        lab_content.append("")

        lab_content.append("-"*80)
        lab_content.append(" TAREAS A REALIZAR")
        lab_content.append("-"*80)
        for tarea in lab['tareas']:
            lab_content.append(f"  {tarea}")
        lab_content.append("")

        if 'comandos' in lab:
            lab_content.append("-"*80)
            lab_content.append(" COMANDOS Y CONFIGURACIONES")
            lab_content.append("-"*80)
            for cmd in lab['comandos']:
                lab_content.append(f"{cmd}")
            lab_content.append("")

        if 'ejemplos' in lab:
            lab_content.append("-"*80)
            lab_content.append(" EJEMPLOS Y CASOS PRACTICOS")
            lab_content.append("-"*80)
            for ejemplo in lab['ejemplos']:
                lab_content.append(f"{ejemplo}")
            lab_content.append("")

        lab_content.append("-"*80)
        lab_content.append(" PREGUNTAS DE REPASO")
        lab_content.append("-"*80)
        for i, pregunta in enumerate(lab['preguntas_repaso'], 1):
            lab_content.append(f"  {i}. {pregunta}")
        lab_content.append("")

        lab_content.append("-"*80)
        lab_content.append(" NOTAS")
        lab_content.append("-"*80)
        lab_content.append("")
        lab_content.append("")
        lab_content.append("")

        # Guardar laboratorio individual
        filename = f"{lab['id']}_{lab['titulo'].replace(' ', '_').replace('/', '-')[:50]}.txt"
        with open(OUTPUT_DIR / filename, 'w', encoding='utf-8') as f:
            f.write("\n".join(lab_content))

        print(f"  [OK] {lab['id']} - {lab['titulo']}")

print("\n" + "="*80)
print(" LABORATORIOS GENERADOS EXITOSAMENTE")
print("="*80)
print(f"Directorio: {OUTPUT_DIR}")
print(f"Total archivos: 16 (1 índice + 15 laboratorios)")
print("="*80)
