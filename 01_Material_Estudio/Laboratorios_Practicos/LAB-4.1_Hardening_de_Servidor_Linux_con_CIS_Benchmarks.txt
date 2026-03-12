================================================================================
 LAB-4.1 - Hardening de Servidor Linux con CIS Benchmarks
================================================================================

DOMINIO: Dominio 4 - Operaciones de Seguridad
OBJETIVOS: 4.1
CONCEPTOS: Hardening, CIS Benchmark, Least Privilege, AppArmor
DIFICULTAD: Media
TIEMPO ESTIMADO: 60 min

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • Ubuntu Server VM
  • OpenSCAP
  • Lynis

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Realizar auditoría inicial con Lynis
  2. Desactivar servicios innecesarios
  3. Configurar firewall UFW (deny-all + allow SSH)
  4. Implementar fail2ban contra brute force
  5. Deshabilitar root login por SSH
  6. Configurar autenticación por clave SSH (sin password)
  7. Actualizar sistema y aplicar parches
  8. Configurar AppArmor para confinar aplicaciones
  9. Re-auditar con Lynis y comparar score

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------
# Auditoría inicial
sudo lynis audit system

# Ver servicios activos
systemctl list-unit-files --state=enabled

# Desactivar servicio innecesario
sudo systemctl disable cups

# Configurar UFW
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw enable

# Instalar fail2ban
sudo apt install fail2ban
sudo systemctl enable fail2ban

# Deshabilitar root SSH (/etc/ssh/sshd_config)
# PermitRootLogin no
# PasswordAuthentication no
sudo systemctl restart sshd

# Verificar AppArmor
sudo aa-status

# Actualizar sistema
sudo apt update && sudo apt upgrade -y

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------
  1. ¿Qué es hardening y por qué es importante?
  2. ¿Qué son los CIS Benchmarks?
  3. ¿Diferencia entre AppArmor y SELinux?
  4. ¿Por qué deshabilitar servicios innecesarios?

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------


