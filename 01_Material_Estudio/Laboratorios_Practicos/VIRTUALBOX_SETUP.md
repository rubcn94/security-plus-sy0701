# Configuración de Laboratorios Security+ con VirtualBox

## VMs Disponibles Detectadas

```
VMs identificadas en tu sistema:
├── Kali                          (Ubuntu 64-bit, 8GB RAM, 1 CPU)
├── UbuntuLiveServerM8            (Ubuntu 64-bit, 4GB RAM, 3 CPUs)
├── WindowsServer2025M6           (Win Server 2022, 4GB RAM, 3 CPUs)
├── UbuntuDesktopM6               (Ubuntu Desktop)
├── Windows11ProM6                (Windows 11)
└── Otras VMs clonadas y de módulos ASYR
```

## Plan de Configuración para Labs Security+

### Opción 1: Configuración Mínima (Usar VMs Existentes)

**VM Principal: Kali Linux** (8GB RAM, 1 CPU)
- ✅ Ya disponible
- Uso: Mayoría de labs (2.1, 2.2, 2.3, 4.2, 4.3)
- Herramientas preinstaladas: Nmap, Wireshark, OpenSSL, etc.

**VM Secundaria: UbuntuLiveServerM8** (4GB RAM, 3 CPUs)
- ✅ Ya disponible
- Uso: Labs de hardening (4.1), SIEM (4.3), IDS/IPS (3.2)
- Instalar: Suricata, Wazuh, Lynis

**VM Windows: WindowsServer2025M6** (4GB RAM, 3 CPUs)
- ✅ Ya disponible
- Uso: Labs de AD, GPO, Windows hardening (opcional)

### Opción 2: Crear VMs Específicas para Security+

**Recomendación**: Crear 2-3 VMs nuevas optimizadas:

1. **SecPlus-Attack** (Kali Linux modificada)
   - Base: Clonar Kali existente
   - RAM: 4-6GB
   - Propósito: Pentesting, análisis malware, OSINT
   - Labs: 2.1, 2.2, 2.3, 4.2

2. **SecPlus-Defense** (Ubuntu Server 22.04)
   - Nueva VM o clonar UbuntuLiveServerM8
   - RAM: 4GB
   - Propósito: SIEM, IDS/IPS, hardening
   - Labs: 3.1, 3.2, 4.1, 4.3

3. **SecPlus-Vulnerable** (Ubuntu/Debian ligero)
   - Nueva VM (2GB RAM suficiente)
   - Propósito: Target para ataques, DVWA, apps vulnerables
   - Labs: 2.2 (SQLi/XSS), pruebas de pentesting

## Configuración de Red en VirtualBox

### Red Interna (Aislada para Labs)

```
Configuración recomendada:
┌─────────────────────────────────────────────────────┐
│  Host (Windows)                                     │
│  ├── NAT Network: 10.0.2.0/24 (Internet)           │
│  └── Internal Network: "SecPlusLab" 192.168.100.0/24│
│      ├── SecPlus-Attack    (192.168.100.10)        │
│      ├── SecPlus-Defense   (192.168.100.20)        │
│      ├── SecPlus-Vulnerable (192.168.100.30)       │
│      └── pfSense (opcional) (192.168.100.1)        │
└─────────────────────────────────────────────────────┘
```

### Pasos de Configuración

**Crear red interna:**
```powershell
# Desde PowerShell
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' natnetwork add --netname SecPlusNAT --network "10.0.2.0/24" --enable
```

**Configurar adaptadores de red en VMs:**
- **Adaptador 1**: NAT Network (para internet)
- **Adaptador 2**: Internal Network "SecPlusLab" (para comunicación entre VMs)

## Mapeo de Laboratorios a VMs

| Lab ID | Nombre | VM Principal | VM Secundaria | Conexión Internet |
|--------|--------|--------------|---------------|-------------------|
| LAB-1.1 | PKI y Certificados | Kali | - | No necesaria |
| LAB-1.2 | VPN + MFA | UbuntuServer | Kali (cliente) | Sí |
| LAB-1.3 | Cifrado AES/RSA | Kali | - | No |
| LAB-2.1 | Análisis Malware | Kali | - | **NO** (desconectar) |
| LAB-2.2 | SQLi/XSS | Kali | SecPlus-Vulnerable | No necesaria |
| LAB-2.3 | OSINT | Kali | - | Sí |
| LAB-3.1 | Firewall pfSense | pfSense | Kali + Ubuntu | No necesaria |
| LAB-3.2 | IDS/IPS Suricata | UbuntuServer | Kali (atacante) | Sí (rules) |
| LAB-3.3 | Crypto-shredding | UbuntuServer | - | No |
| LAB-4.1 | Hardening Linux | UbuntuServer | - | Sí (updates) |
| LAB-4.2 | Forense | Kali | VM comprometida | No necesaria |
| LAB-4.3 | SIEM Wazuh | UbuntuServer | Kali (agent) | Sí (Docker) |
| LAB-5.1 | Análisis Riesgos | Host Windows | - | No |
| LAB-5.2 | Compliance | Host Windows | - | No |
| LAB-5.3 | Third-Party | Host Windows | - | Sí (research) |

## Snapshots Recomendados

Para cada VM, crear estos snapshots:

```
VM: Kali
├── 01_Clean_Install          (instalación base)
├── 02_Tools_Installed        (después de instalar extras)
└── 03_Lab_Ready              (configuración red, listo para labs)

VM: UbuntuServer
├── 01_Clean_Install
├── 02_Hardened_Base          (después LAB-4.1)
├── 03_SIEM_Installed         (Wazuh instalado)
└── 04_IDS_Installed          (Suricata + ELK)

VM: SecPlus-Vulnerable
├── 01_Clean
└── 02_DVWA_Installed         (apps vulnerables listas)
```

## Recursos de Sistema Necesarios

### Configuración Mínima
- **RAM Total**: 16GB (sistema) → 12GB disponible para VMs
  - Kali: 4GB
  - Ubuntu Server: 4GB
  - Vulnerable: 2GB
  - Host: 4GB

- **Disco**: 80GB libres
  - Kali: 30GB
  - Ubuntu Server: 25GB
  - Vulnerable: 15GB
  - Snapshots: 10GB

### Configuración Recomendada
- **RAM**: 32GB → 24GB para VMs
- **Disco**: 150GB+ SSD
- **CPU**: 6+ cores (habilitar VT-x/AMD-V)

## Verificación de Virtualización

```powershell
# Verificar si virtualización está habilitada
systeminfo | findstr /C:"Hyper-V"

# Debería mostrar:
# Hyper-V Requirements: VM Monitor Mode Extensions: Yes
#                      Virtualization Enabled In Firmware: Yes
```

Si no está habilitada, activar en BIOS:
- Intel: VT-x
- AMD: AMD-V / SVM

## Instalación de VMs Nuevas (si es necesario)

### Descargar ISOs

**Kali Linux** (si necesitas nueva instalación):
```
URL: https://www.kali.org/get-kali/#kali-installer-images
ISO: kali-linux-2024.4-installer-amd64.iso (3.8GB)
```

**Ubuntu Server 22.04 LTS**:
```
URL: https://ubuntu.com/download/server
ISO: ubuntu-22.04.5-live-server-amd64.iso (2.5GB)
```

**DVWA con Docker** (más fácil que VM dedicada):
```bash
# Desde Kali o Ubuntu Server
docker run -d -p 80:80 vulnerables/web-dvwa
```

## Próximos Pasos

1. **Preparar VMs Base**
   ```powershell
   # Ejecutar script de setup
   .\SCRIPTS\vbox_setup_vms.ps1
   ```

2. **Crear Snapshots Iniciales**
   ```powershell
   .\SCRIPTS\vbox_create_snapshots.ps1
   ```

3. **Configurar Red Interna**
   ```powershell
   .\SCRIPTS\vbox_setup_network.ps1
   ```

4. **Instalar Herramientas en Kali**
   ```bash
   # SSH a Kali y ejecutar
   sudo bash /mnt/shared/setup_kali_tools.sh
   ```

5. **Comenzar con LAB-1.1** (PKI)
   - VM: Kali
   - Snapshot: Lab_Ready
   - Internet: No necesaria

---

**Notas Importantes:**

⚠️ **Snapshots**: SIEMPRE tomar snapshot antes de cada lab
⚠️ **Malware**: LAB-2.1 requiere desconectar red completamente
⚠️ **Recursos**: Cerrar VMs no usadas para liberar RAM
⚠️ **Backups**: Exportar VMs importantes (.ova) periódicamente

---

**¿Qué configuración prefieres?**
- [ ] Opción 1: Usar VMs existentes (Kali + UbuntuLiveServerM8)
- [ ] Opción 2: Crear 3 VMs nuevas específicas para Security+
- [ ] Opción 3: Híbrido (usar Kali existente + crear SecPlus-Defense nueva)
