================================================================================
 LAB-4.1 - Hardening de Servidor Linux con CIS Benchmarks
================================================================================

DOMINIO: Dominio 4 - Operaciones de Seguridad
OBJETIVOS: 4.1
CONCEPTOS: Hardening, CIS Benchmark, Least Privilege, AppArmor, Lynis
DIFICULTAD: Media
TIEMPO ESTIMADO: 60 min
FECHA REALIZADO: 2026-03-10
ENTORNO: Ubuntu Server (srvsierra) - VM VirtualBox

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • Ubuntu Server VM (srvsierra)
  • Lynis instalado (sudo apt install lynis)
  • Acceso root o sudo
  • Conexión SSH activa

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Realizar auditoría inicial con Lynis                          [HECHO]
  2. Analizar warnings y sugerencias                               [HECHO]
  3. Actualizar sistema y aplicar parches                          [HECHO]
  4. Hardening de SSH (8 directivas)                               [HECHO]
  5. Deshabilitar protocolos de red innecesarios                   [HECHO]
  6. Reforzar política de contraseñas en login.defs                [HECHO]
  7. Instalar herramientas de auditoría faltantes                  [HECHO]
  8. Verificar AppArmor                                            [HECHO]
  9. Re-auditar con Lynis y comparar score                         [HECHO]

--------------------------------------------------------------------------------
 RESULTADOS DE AUDITORÍA
--------------------------------------------------------------------------------

  SCORE INICIAL:  59 / 100  [###########         ]
  SCORE FINAL:    68 / 100  [#############       ]
  MEJORA:        +9 puntos

  Tests realizados: 262
  Plugins activos:  1

  WARNINGS encontrados (auditoría inicial):
  ┌─────────────┬──────────────────────────────────────────────────────────┐
  │ ID          │ Descripción                                               │
  ├─────────────┼──────────────────────────────────────────────────────────┤
  │ PKGS-7392   │ Paquetes vulnerables instalados → RESUELTO (apt upgrade) │
  │ NETW-3015   │ Interfaz enp0s3 en modo promiscuo (intencional en lab)   │
  └─────────────┴──────────────────────────────────────────────────────────┘

  SUGERENCIAS PRINCIPALES abordadas:
  - SSH-7408:  8 directivas de SSH endurecidas
  - NETW-3200: 4 protocolos de red deshabilitados
  - AUTH-9286: Política de contraseñas configurada
  - PKGS-7370: debsums instalado
  - PKGS-7394: apt-show-versions instalado

  SUGERENCIAS NO ABORDADAS (requieren rediseño estructural):
  - FILE-6310: Particiones separadas para /home, /tmp, /var
  - USB-1000:  Deshabilitar USB storage (no aplica en VM)

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------

## 1. Auditoría inicial
sudo lynis audit system --no-colors 2>&1 | tee /tmp/lynis_inicial.txt

## 2. Ver warnings y sugerencias
grep -E "^\s*(warning|suggestion)" /var/log/lynis-report.dat

## 3. Actualizar paquetes vulnerables
sudo apt update && sudo apt upgrade -y

## 4. Hardening SSH - /etc/ssh/sshd_config
# Cambios aplicados:
PermitRootLogin no
PasswordAuthentication no
MaxAuthTries 3
MaxSessions 2
AllowTcpForwarding no
X11Forwarding no
ClientAliveCountMax 2
LogLevel VERBOSE
TCPKeepAlive no

# Verificar config antes de reiniciar
sudo sshd -t

# Crear directorio de privilege separation si falta
sudo mkdir -p /run/sshd

# Reiniciar SSH
sudo systemctl restart sshd

## 5. Deshabilitar protocolos de red innecesarios
echo "install dccp /bin/false
install sctp /bin/false
install rds /bin/false
install tipc /bin/false" | sudo tee /etc/modprobe.d/disable-protocols.conf

## 6. Política de contraseñas - /etc/login.defs
# Ajustar estas líneas:
PASS_MAX_DAYS   90
PASS_MIN_DAYS   1
PASS_WARN_AGE   7
UMASK           027

## 7. Instalar herramientas de auditoría
sudo apt install -y debsums apt-show-versions

## 8. Verificar AppArmor
sudo aa-status

## 9. Re-auditoría final
sudo lynis audit system --no-colors 2>&1 | tee /tmp/lynis_final.txt | grep -E "Hardening index|Tests performed"

## Comparar ambos reportes
diff /tmp/lynis_inicial.txt /tmp/lynis_final.txt | grep "^[<>]" | grep -i "suggest\|warn"

--------------------------------------------------------------------------------
 ESTADO DE APPARMOR (resultado real)
--------------------------------------------------------------------------------
  Módulo cargado:           SI
  Perfiles cargados:        123
  Perfiles en enforce:       28  (activos y bloqueando)
  Perfiles en complain:       4  (transmission-*)
  Perfiles unconfined:       91  (apps de escritorio - normal)
  Procesos en enforce:       24  (Wazuh bajo docker-default)

  Servicios críticos confinados:
  - rsyslogd       → enforce
  - tcpdump        → enforce
  - kea-dhcp4      → enforce
  - Wazuh (todos)  → enforce (docker-default)

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------

  1. ¿Qué es hardening y por qué es importante?

     Hardening es el proceso de reducir la superficie de ataque de un sistema
     eliminando servicios innecesarios, aplicando configuraciones seguras y
     restringiendo accesos. Es importante porque cada servicio activo o
     configuración débil es un vector potencial de compromiso.

  2. ¿Qué son los CIS Benchmarks?

     Son guías de configuración segura desarrolladas por el Center for Internet
     Security. Proporcionan estándares técnicos probados para sistemas operativos,
     aplicaciones y dispositivos de red. Lynis los usa como referencia para puntuar
     el nivel de hardening de un sistema.

  3. ¿Diferencia entre AppArmor y SELinux?

     AppArmor: basado en rutas de archivo. Más sencillo de configurar.
               Usado por defecto en Ubuntu/Debian.
     SELinux:  basado en etiquetas (labels) en cada objeto del sistema.
               Más granular y complejo. Usado por defecto en RHEL/Fedora.
     Ambos implementan MAC (Mandatory Access Control) como capa adicional
     sobre los permisos UNIX tradicionales (DAC).

  4. ¿Por qué deshabilitar servicios innecesarios?

     Cada servicio activo es una superficie de ataque potencial. Si un servicio
     tiene vulnerabilidades y no es necesario, su existencia solo añade riesgo.
     El principio de least privilege se aplica también a nivel de sistema:
     ejecutar solo lo estrictamente necesario.

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------

  - El warning NETW-3015 (interfaz promiscua) es intencional en entorno de lab.
    En producción habría que justificarlo o desactivarlo.

  - El error "Missing privilege separation directory: /run/sshd" ocurre en
    sistemas donde /run/sshd no persiste entre reinicios. Solución permanente:
    añadir 'RuntimeDirectory=sshd' al unit de systemd o crear el dir en rc.local.

  - Lynis 3.0.9 (instalado en srvsierra) vs 3.1.6 (en Kali). Versiones distintas
    pueden dar scores ligeramente diferentes en el mismo sistema.

  - Para subir más el score habría que configurar UFW explícitamente, configurar
    fail2ban, y separar particiones (requiere reinstalación).

  - Los procesos de Wazuh corriendo en enforce bajo docker-default confirman que
    el SIEM está activo y monitorizando el servidor (relevante para lab 4.3).

