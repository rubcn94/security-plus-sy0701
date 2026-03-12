# Laboratorios Prácticos - CompTIA Security+ SY0-701

## Descripción

Colección de 15 laboratorios prácticos diseñados para reforzar los conceptos del examen Security+ SY0-701. Cada laboratorio incluye ejercicios hands-on con comandos reales y configuraciones paso a paso.

## Estructura

```
07_Laboratorios/
├── 00_INDICE_LABORATORIOS.txt          # Índice completo de todos los labs
├── LAB-1.1_*.txt                        # Laboratorios individuales
├── LAB-1.2_*.txt
├── ...
├── LAB-5.3_*.txt
├── SCRIPTS/                             # Scripts de automatización
│   ├── setup_lab_environment.sh         # Setup inicial del entorno
│   ├── lab1.1_pki_setup.sh             # Automatización PKI
│   └── lab4.1_hardening.sh             # Automatización hardening
└── README.md                            # Este archivo
```

## Resumen de Laboratorios

### Dominio 1 - Conceptos Generales de Seguridad (3 labs)
- **LAB-1.1**: PKI y Certificados (OpenSSL, CA, CSR, X.509)
- **LAB-1.2**: Zero Trust con VPN y MFA (OpenVPN, RADIUS, TOTP)
- **LAB-1.3**: Cifrado Simétrico vs Asimétrico (AES, RSA, Hash)

### Dominio 2 - Amenazas y Vulnerabilidades (3 labs)
- **LAB-2.1**: Análisis de Malware con Sandboxing (VM, IOC, análisis dinámico)
- **LAB-2.2**: SQLi y XSS Práctico (DVWA, Burp Suite, OWASP Top 10)
- **LAB-2.3**: Reconnaissance con MITRE ATT&CK (OSINT, theHarvester, Shodan)

### Dominio 3 - Arquitectura de Seguridad (3 labs)
- **LAB-3.1**: Firewall y Segmentación de Red (pfSense, VLAN, ACL)
- **LAB-3.2**: IDS/IPS con Suricata + ELK (SIEM, detección amenazas)
- **LAB-3.3**: Destrucción Segura de Datos (shred, crypto-shredding, LUKS)

### Dominio 4 - Operaciones de Seguridad (3 labs)
- **LAB-4.1**: Hardening Linux (CIS Benchmarks, Lynis, AppArmor)
- **LAB-4.2**: Respuesta a Incidentes y Forense (Volatility, Autopsy, evidencia)
- **LAB-4.3**: SIEM con Wazuh (logs centralizados, correlación, alertas)

### Dominio 5 - Gestión del Programa (3 labs)
- **LAB-5.1**: Análisis de Riesgos (ALE, SLE, ARO, matriz de riesgos)
- **LAB-5.2**: Auditoría de Compliance (GDPR, PCI DSS, gap analysis)
- **LAB-5.3**: Evaluación de Proveedores (third-party risk, SLA, due diligence)

## Requisitos Generales

### Hardware Recomendado
- **CPU**: 4+ cores (virtualización habilitada)
- **RAM**: 16GB+ (para múltiples VMs)
- **Disco**: 100GB+ libres
- **Hypervisor**: VirtualBox, VMware Workstation, o Hyper-V

### Software Base
- **Linux**: Ubuntu Server 22.04 LTS, Kali Linux, o similar
- **Windows**: Windows 10/11 Pro (para algunos labs)
- **Docker**: Para contenedores (DVWA, ELK, etc.)
- **ISO recomendadas**:
  - Kali Linux 2024+
  - Ubuntu Server 22.04
  - pfSense 2.7+

### Herramientas Principales
- OpenSSL, Nmap, Wireshark, tcpdump
- Docker + Docker Compose
- Python 3.8+
- Git

## Instalación Rápida

### 1. Setup Automático del Entorno (Linux)

```bash
# Descargar script de setup
cd /tmp
wget https://[tu-repo]/setup_lab_environment.sh

# Ejecutar como root
sudo chmod +x setup_lab_environment.sh
sudo ./setup_lab_environment.sh
```

### 2. Instalación Manual (Windows)

```powershell
# Instalar chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Instalar herramientas
choco install -y virtualbox docker-desktop python git openssh
```

## Uso de los Laboratorios

### Formato de cada Lab

Cada archivo de laboratorio contiene:

1. **Requisitos Previos**: Software/hardware necesario
2. **Tareas a Realizar**: Paso a paso del ejercicio
3. **Comandos**: Comandos exactos a ejecutar
4. **Preguntas de Repaso**: Verificación de conocimientos

### Workflow Recomendado

```bash
# 1. Leer el laboratorio completo
cat LAB-X.X_*.txt

# 2. Preparar el entorno
# - Crear snapshot de VM limpia
# - Verificar requisitos instalados

# 3. Ejecutar las tareas
# - Seguir paso a paso
# - Documentar resultados
# - Responder preguntas de repaso

# 4. Restaurar entorno (si es necesario)
# - Revertir snapshot para siguiente lab
```

## Scripts de Automatización

### setup_lab_environment.sh
Script maestro que instala todas las herramientas comunes.

**Uso**:
```bash
sudo ./SCRIPTS/setup_lab_environment.sh
```

### lab1.1_pki_setup.sh
Automatiza la creación de CA y certificados para LAB-1.1.

**Uso**:
```bash
bash SCRIPTS/lab1.1_pki_setup.sh
```

### lab4.1_hardening.sh
Aplica configuraciones de hardening automáticamente.

**Uso**:
```bash
sudo ./SCRIPTS/lab4.1_hardening.sh
```

## Notas de Seguridad

⚠️ **IMPORTANTE**:

1. **Entorno Aislado**: Todos los labs deben ejecutarse en VMs aisladas, NUNCA en sistemas de producción.

2. **Red Aislada**: Crear red interna en el hypervisor para evitar exposición.

3. **Snapshots**: Tomar snapshot antes de cada lab para poder restaurar.

4. **Malware**: Labs de malware (LAB-2.1) requieren precauciones extremas:
   - Red completamente desconectada
   - Usar muestras de prueba (EICAR) o malware viejo conocido
   - NUNCA ejecutar malware real fuera de sandbox

5. **Ataques Web**: DVWA y apps vulnerables solo en red local.

6. **Hardening SSH**: En LAB-4.1, configurar claves SSH ANTES de deshabilitar password auth.

## Tiempos Estimados

| Dificultad | Tiempo Promedio | Labs |
|------------|-----------------|------|
| Baja       | 30-45 min       | 3    |
| Media      | 45-75 min       | 9    |
| Alta       | 90+ min         | 3    |

**Tiempo total**: ~17 horas de práctica

## Troubleshooting

### Problemas Comunes

**Error: "Permission denied" al ejecutar scripts**
```bash
chmod +x script.sh
sudo ./script.sh
```

**Docker no inicia**
```bash
# Linux
sudo systemctl start docker
sudo systemctl enable docker

# Windows: Reiniciar Docker Desktop
```

**VM sin conexión a internet**
```bash
# Verificar modo de red en VirtualBox/VMware
# Cambiar a NAT o Bridge según necesidad
```

**Comandos OpenSSL fallan**
```bash
# Verificar instalación
openssl version

# Reinstalar si es necesario
sudo apt install --reinstall openssl
```

## Recursos Adicionales

### Documentación Oficial
- CompTIA Security+ Exam Objectives (SY0-701)
- Professor Messer Videos: https://www.professormesser.com/
- NIST Cybersecurity Framework
- MITRE ATT&CK: https://attack.mitre.org/

### Cheat Sheets
- OpenSSL: https://www.sslshopper.com/article-most-common-openssl-commands.html
- Nmap: https://www.stationx.net/nmap-cheat-sheet/
- Wireshark: https://www.comparitech.com/net-admin/wireshark-cheat-sheet/

### Plataformas de Práctica
- TryHackMe: https://tryhackme.com/
- HackTheBox: https://www.hackthebox.com/
- PentesterLab: https://pentesterlab.com/

## Contribuciones

Si encuentras errores o tienes mejoras:

1. Documentar el problema claramente
2. Proponer solución con comandos verificados
3. Incluir salida esperada

## Licencia

Uso educativo - CompTIA Security+ SY0-701

---

**¡Buena suerte con tus laboratorios!** 🔒🛡️
