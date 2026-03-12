# ✅ Setup de Laboratorios Completado

**Fecha**: 23 de febrero de 2026
**Ubicación**: `D:\Users\cra\Desktop\Sec+\07_Laboratorios`

---

## Resumen de Configuración

### VMs Configuradas

#### 1. Kali Linux
```
✓ RAM: 4096MB (4GB)
✓ CPUs: 2
✓ Nested Paging: Habilitado
✓ NIC 1: NAT (Internet)
✓ NIC 2: Internal Network 'SecPlusLab'
✓ Snapshot: Lab_Clean_State (2026-02-23 12:47:56)

Uso: Pentesting, Análisis de Malware, OSINT
Labs: 2.1, 2.2, 2.3, 4.2
```

#### 2. UbuntuLiveServerM8
```
✓ RAM: 4096MB (4GB)
✓ CPUs: 3
✓ Nested Paging: Habilitado
✓ NIC 1: NAT (Internet)
✓ NIC 2: Internal Network 'SecPlusLab'
✓ Snapshot: Lab_Clean_State (2026-02-23 12:47:56)

Uso: SIEM, IDS/IPS, Hardening, Servicios de red
Labs: 3.2, 4.1, 4.3
```

### Redes Configuradas

#### NAT Network: SecPlusNAT
```
Red: 10.0.2.0/24
DHCP: Habilitado
Propósito: Acceso a Internet (updates, descargas, OSINT)
```

#### Internal Network: SecPlusLab
```
Red: 192.168.100.0/24
Propósito: Comunicación entre VMs para labs
IPs sugeridas:
  - Kali: 192.168.100.10
  - Ubuntu: 192.168.100.20
```

---

## Estado Actual

```
✓ VirtualBox: Detectado y funcional
✓ VMs: 2 configuradas correctamente
✓ Snapshots: 2 creados (estado limpio)
✓ Red NAT: Creada (SecPlusNAT)
✓ Red Interna: Configurada (SecPlusLab)
✓ Nested Virtualization: Habilitada (para Docker)
✓ Scripts: 3 scripts PowerShell listos
✓ Laboratorios: 15 guías creadas
```

---

## Próximos Pasos - Empezar Labs

### Opción 1: Lab Fácil para Empezar (Recomendado)

**LAB-1.3: Cifrado Simétrico vs Asimétrico** (30 min)

```powershell
# 1. Iniciar Kali
cd "D:\Users\cra\Desktop\Sec+\07_Laboratorios\SCRIPTS"
.\vbox_start_vm.ps1 Kali

# 2. Acceder a Kali (usuario/password de tu instalación)
# SSH o consola gráfica

# 3. Seguir la guía
cat ../LAB-1.3_Cifrado_Simetrico_vs_Asimetrico_-_Casos_Practicos.txt
```

### Opción 2: Lab de PKI (Medio)

**LAB-1.1: PKI y Certificados** (45 min)

```powershell
# 1. Iniciar Kali
.\vbox_start_vm.ps1 Kali

# 2. Ejecutar script automático PKI (opcional)
# Desde Kali:
sudo bash /mnt/shared/SCRIPTS/lab1.1_pki_setup.sh

# 3. O seguir guía manual
cat ../LAB-1.1_Configuracion_de_PKI_y_Certificados.txt
```

### Opción 3: Lab de Hardening (Medio)

**LAB-4.1: Hardening Linux** (60 min)

```powershell
# 1. Iniciar Ubuntu Server
.\vbox_start_vm.ps1 UbuntuLiveServerM8

# 2. Ejecutar script de hardening
# Desde Ubuntu:
sudo bash /mnt/shared/SCRIPTS/lab4.1_hardening.sh

# 3. Revisar cambios aplicados
```

---

## Configuración de IP Estática (Opcional)

### Para Kali Linux

Editar configuración de red:

```bash
sudo nano /etc/netplan/01-netcfg.yaml
```

Contenido:

```yaml
network:
  version: 2
  ethernets:
    enp0s3:  # Adaptador 1 (NAT - Internet)
      dhcp4: true
    enp0s8:  # Adaptador 2 (Internal Network)
      addresses:
        - 192.168.100.10/24
```

Aplicar:

```bash
sudo netplan apply
```

### Para Ubuntu Server (igual pero IP diferente)

```yaml
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: true
    enp0s8:
      addresses:
        - 192.168.100.20/24
```

---

## Comandos Rápidos VirtualBox

### Gestión de VMs

```powershell
# Iniciar VM
.\vbox_start_vm.ps1 Kali

# Apagar VM (correcto)
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' controlvm Kali acpipowerbutton

# Apagar VM (forzado)
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' controlvm Kali poweroff

# Ver estado
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' showvminfo Kali | Select-String "State:"
```

### Gestión de Snapshots

```powershell
# Crear nuevo snapshot
.\vbox_create_snapshots.ps1 -VMName Kali -SnapshotName "Lab_1.1_Completed"

# Listar snapshots
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' snapshot Kali list

# Restaurar snapshot limpio
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' snapshot Kali restore Lab_Clean_State

# Eliminar snapshot
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' snapshot Kali delete "Snapshot_Name"
```

---

## Estructura de Archivos

```
D:\Users\cra\Desktop\Sec+\
├── 01_PDFs_Finales/
│   └── SecPlus_SY0-701_CONDENSADO.pdf        (Teoría condensada + leyenda)
│
├── 03_JSON_Datos/
│   ├── secplus_estructurado.json             (Datos completos)
│   ├── abreviaciones.json                    (196 abreviaciones)
│   └── LEYENDA_ABREVIACIONES.txt             (Texto plano)
│
├── 04_Scripts_Python/
│   ├── generar_pdf_condensado.py
│   ├── generar_laboratorios.py
│   └── [otros scripts de generación]
│
└── 07_Laboratorios/                          ← ESTÁS AQUÍ
    ├── 00_INDICE_LABORATORIOS.txt            (Índice de 15 labs)
    ├── LAB-1.1_*.txt                         (15 guías detalladas)
    ├── LAB-1.2_*.txt
    ├── ...
    ├── LAB-5.3_*.txt
    │
    ├── SCRIPTS/
    │   ├── setup_lab_environment.sh          (Setup Linux)
    │   ├── lab1.1_pki_setup.sh              (PKI automático)
    │   ├── lab4.1_hardening.sh              (Hardening automático)
    │   ├── vbox_setup_vms.ps1               (✓ EJECUTADO)
    │   ├── vbox_create_snapshots.ps1        (✓ EJECUTADO)
    │   └── vbox_start_vm.ps1
    │
    ├── README.md                             (Documentación completa)
    ├── VIRTUALBOX_SETUP.md                   (Config específica VirtualBox)
    ├── QUICK_START.md                        (Guía rápida)
    └── SETUP_COMPLETADO.md                   (Este archivo)
```

---

## Checklist de Verificación

Antes de empezar un lab, verificar:

- [ ] VM apagada correctamente (no forzar)
- [ ] Snapshot limpio existe
- [ ] Suficiente RAM libre en el host (4GB+)
- [ ] Guía del lab leída completamente
- [ ] Conexión a internet (si es necesario para el lab)
- [ ] **IMPORTANTE**: Para LAB-2.1 (Malware), desconectar red

---

## Recursos de Aprendizaje

### Incluidos en este Setup

1. **PDF Condensado** - Teoría priorizada (ALTA + MEDIA)
   - `01_PDFs_Finales/SecPlus_SY0-701_CONDENSADO.pdf`
   - 202 puntos clave + 196 abreviaciones

2. **15 Laboratorios** - Práctica hands-on
   - 3 labs por dominio
   - Comandos reales listos para ejecutar
   - Preguntas de repaso

3. **Scripts de Automatización**
   - Setup automático de entornos
   - Gestión de snapshots
   - Hardening y PKI automatizados

### Recursos Externos Recomendados

- **Professor Messer**: https://www.professormesser.com/
- **TryHackMe**: https://tryhackme.com/ (práctica adicional)
- **MITRE ATT&CK**: https://attack.mitre.org/
- **OWASP Top 10**: https://owasp.org/www-project-top-ten/

---

## Troubleshooting Común

### VM no inicia

```powershell
# Ver logs
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' showvminfo Kali --log 0

# Verificar virtualización habilitada en BIOS
systeminfo | findstr /C:"Hyper-V"
```

### Sin conexión a internet en VM

```bash
# Verificar interfaces
ip addr show

# Probar conectividad
ping 8.8.8.8

# Reiniciar red
sudo systemctl restart networking
```

### Poco espacio en disco

```powershell
# Eliminar snapshots antiguos
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' snapshot Kali delete "Old_Snapshot"

# Compactar disco virtual (con VM apagada)
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' modifymedium disk "ruta\al\disco.vdi" --compact
```

---

## Notas de Seguridad

⚠️ **IMPORTANTE**:

1. **Entorno Aislado**: Labs solo en VMs, NUNCA en host
2. **Snapshots**: Siempre restaurar antes de cada lab
3. **Red Desconectada**: LAB-2.1 (malware) requiere desconexión total
4. **Credenciales**: No usar contraseñas reales en labs
5. **Backup**: Exportar VMs importantes periódicamente (.ova)

---

## Estadísticas del Setup

```
Total de archivos generados:      19
  - Guías de laboratorio:         15
  - Scripts automatización:        6
  - Documentación:                 4

Total de VMs configuradas:         2
Total de snapshots:                2
Total de laboratorios disponibles: 15
Tiempo estimado labs:              ~17 horas

Líneas de código (scripts):        ~2000
Conceptos Security+ cubiertos:     144 (ALTA+MEDIA)
Abreviaciones documentadas:        196
```

---

## ¡Todo Listo! 🔒

**Setup completado exitosamente**

Ahora puedes empezar con cualquier laboratorio siguiendo la guía en `QUICK_START.md`

**Sugerencia**: Empieza con **LAB-1.3** (Cifrado) - es el más sencillo y te familiarizará con el workflow.

```powershell
# ¡A practicar!
.\vbox_start_vm.ps1 Kali
```

---

**Última actualización**: 23/02/2026 12:48
**Estado**: ✅ Operativo
