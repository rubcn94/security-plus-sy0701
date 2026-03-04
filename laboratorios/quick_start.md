# Quick Start - Security+ Labs con VirtualBox

## Setup Inicial (Solo una vez)

### 1. Configurar VMs para Labs

```powershell
# Abrir PowerShell como Administrador
cd "D:\Users\cra\Desktop\Sec+\07_Laboratorios\SCRIPTS"

# Configurar VMs automáticamente
.\vbox_setup_vms.ps1
```

Esto configurará:
- ✅ RAM y CPUs optimizadas
- ✅ Adaptadores de red (NAT + Internal)
- ✅ Nested virtualization habilitada

### 2. Crear Snapshots Iniciales

```powershell
# Crear snapshots de estado limpio
.\vbox_create_snapshots.ps1
```

## Workflow para Cada Laboratorio

### Antes de Empezar un Lab

```powershell
# 1. Restaurar snapshot limpio (si necesario)
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' snapshot Kali restore Lab_Clean_State

# 2. Iniciar VM necesaria
.\vbox_start_vm.ps1 Kali

# 3. Leer guía del laboratorio
cat ..\LAB-X.X_*.txt
```

### Durante el Lab

1. **Seguir los pasos** del archivo LAB-X.X
2. **Documentar resultados** en la sección NOTAS
3. **Responder preguntas** de repaso

### Después del Lab

```powershell
# 1. Apagar VM correctamente
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' controlvm Kali acpipowerbutton

# 2. (Opcional) Crear snapshot con progreso
.\vbox_create_snapshots.ps1 -VMName Kali -SnapshotName "Lab_1.1_Completed"
```

## Inicio Rápido por Laboratorio

### LAB-1.1: PKI y Certificados

```powershell
# VM: Kali
.\vbox_start_vm.ps1 Kali

# Dentro de Kali (SSH o terminal)
cd /home/kali
sudo bash /mnt/shared/SCRIPTS/lab1.1_pki_setup.sh
```

### LAB-2.2: SQLi y XSS

```powershell
# VM: Kali
.\vbox_start_vm.ps1 Kali

# Dentro de Kali
docker run -d -p 80:80 vulnerables/web-dvwa
# Acceder: http://localhost
```

### LAB-4.1: Hardening Linux

```powershell
# VM: UbuntuLiveServerM8
.\vbox_start_vm.ps1 UbuntuLiveServerM8

# Dentro de Ubuntu
sudo bash /mnt/shared/SCRIPTS/lab4.1_hardening.sh
```

## Configuración de Red en las VMs

### Kali Linux

Editar `/etc/network/interfaces` o usar Netplan:

```yaml
# /etc/netplan/01-netcfg.yaml
network:
  version: 2
  ethernets:
    enp0s3:  # NAT (Internet)
      dhcp4: true
    enp0s8:  # Internal Network
      addresses:
        - 192.168.100.10/24
```

Aplicar:
```bash
sudo netplan apply
```

### Ubuntu Server

Igual que Kali, pero IP diferente:

```yaml
enp0s8:
  addresses:
    - 192.168.100.20/24
```

## Comandos Rápidos VirtualBox

```powershell
# Listar todas las VMs
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' list vms

# Listar VMs en ejecución
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' list runningvms

# Ver info de una VM
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' showvminfo Kali

# Iniciar VM
.\vbox_start_vm.ps1 Kali

# Iniciar en modo headless (sin GUI)
.\vbox_start_vm.ps1 Kali -Headless

# Apagar VM (ACPI - correcto)
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' controlvm Kali acpipowerbutton

# Apagar VM (forzado)
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' controlvm Kali poweroff

# Pausar VM
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' controlvm Kali pause

# Reanudar VM
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' controlvm Kali resume

# Crear snapshot
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' snapshot Kali take "Snapshot_Name"

# Listar snapshots
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' snapshot Kali list

# Restaurar snapshot
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' snapshot Kali restore "Snapshot_Name"

# Eliminar snapshot
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' snapshot Kali delete "Snapshot_Name"
```

## Carpetas Compartidas (Opcional)

Para compartir archivos entre host y VMs:

```powershell
# Crear carpeta compartida
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' sharedfolder add Kali `
  --name "SecPlusLabs" `
  --hostpath "D:\Users\cra\Desktop\Sec+\07_Laboratorios" `
  --automount
```

Dentro de la VM:
```bash
# Instalar Guest Additions primero
sudo apt install virtualbox-guest-utils

# Montar carpeta compartida
sudo mkdir -p /mnt/shared
sudo mount -t vboxsf SecPlusLabs /mnt/shared

# Auto-montar en boot (añadir a /etc/fstab)
SecPlusLabs /mnt/shared vboxsf defaults 0 0
```

## Troubleshooting

### VM no inicia

```powershell
# Verificar logs
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' showvminfo Kali --log 0
```

### No hay conexión a internet en la VM

```bash
# Verificar interfaces
ip addr show

# Verificar NAT
ping 8.8.8.8

# Reiniciar networking
sudo systemctl restart networking
```

### Snapshot ocupa mucho espacio

```powershell
# Listar tamaño de snapshots
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' snapshot Kali list --details

# Eliminar snapshots antiguos
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' snapshot Kali delete "Old_Snapshot"
```

## Recomendaciones

✅ **Siempre** crear snapshot antes de un lab
✅ **Apagar** VMs correctamente (no forzar)
✅ **Documentar** todo en la sección NOTAS de cada lab
✅ **Cerrar** VMs no usadas para liberar RAM
❌ **Nunca** ejecutar malware sin desconectar red
❌ **No** modificar VMs base sin snapshot previo

## Orden Recomendado de Labs

**Principiantes:**
1. LAB-1.3 (Cifrado) - 30 min
2. LAB-1.1 (PKI) - 45 min
3. LAB-5.1 (Análisis Riesgos) - 45 min

**Intermedios:**
4. LAB-4.1 (Hardening) - 60 min
5. LAB-2.2 (SQLi/XSS) - 75 min
6. LAB-3.1 (Firewall) - 60 min

**Avanzados:**
7. LAB-3.2 (IDS/IPS) - 90 min
8. LAB-4.2 (Forense) - 90 min
9. LAB-4.3 (SIEM) - 90 min

---

**¡Todo listo para empezar los labs!** 🔒

Siguiente paso: `.\vbox_setup_vms.ps1`
