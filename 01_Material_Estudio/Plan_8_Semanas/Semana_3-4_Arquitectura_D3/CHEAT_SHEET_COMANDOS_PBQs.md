# CHEAT SHEET: COMANDOS PARA PBQs - Security+ SY0-701

**Para PBQs (Performance-Based Questions)**
**1 página - IMPRIME Y LLEVA AL EXAMEN**

---

## COMANDOS WINDOWS

### NETWORKING
```cmd
ipconfig /all                    # Ver config IP completa + DNS
ipconfig /release               # Liberar IP DHCP
ipconfig /renew                 # Renovar IP DHCP
ipconfig /flushdns              # Limpiar caché DNS

netstat -ano                    # Ver conexiones + PID proceso
netstat -an | find "ESTABLISHED" # Solo conexiones activas
netstat -r                      # Ver tabla de rutas

nslookup google.com             # Resolver DNS
nslookup -type=MX example.com   # Buscar registros MX (mail)

ping 8.8.8.8                    # Test conectividad
ping -t 8.8.8.8                 # Ping continuo
tracert google.com              # Traza ruta a destino

arp -a                          # Ver tabla ARP
route print                     # Ver tabla de rutas
pathping google.com             # Ping + tracert combinado
```

### SEGURIDAD Y USUARIOS
```cmd
net user                        # Listar usuarios locales
net user backdoor /delete       # Eliminar usuario
net localgroup Administrators   # Ver miembros grupo Admin

gpupdate /force                 # Forzar actualización GPO
gpresult /r                     # Ver GPOs aplicadas

whoami                          # Ver usuario actual
whoami /priv                    # Ver privilegios
whoami /groups                  # Ver grupos

runas /user:admin cmd           # Ejecutar como otro usuario
```

### PROCESOS Y SERVICIOS
```cmd
tasklist                        # Listar procesos
tasklist /svc                   # Procesos + servicios asociados
taskkill /PID 1234 /F           # Matar proceso por PID
taskkill /IM malware.exe /F     # Matar por nombre

sc query                        # Listar servicios
sc stop "ServiceName"           # Detener servicio
sc delete "ServiceName"         # Eliminar servicio

schtasks /query                 # Listar tareas programadas
schtasks /delete /TN "TaskName" # Eliminar tarea
```

### FIREWALL
```cmd
netsh advfirewall show allprofiles          # Ver estado firewall
netsh advfirewall set allprofiles state on  # Activar firewall
netsh advfirewall firewall add rule name="Block Port 445" dir=in action=block protocol=TCP localport=445
netsh advfirewall firewall delete rule name="Block Port 445"
```

### LOGS Y AUDITORÍA
```cmd
eventvwr                        # Abrir Event Viewer
wevtutil qe Security /c:10 /rd:true /f:text  # Últimos 10 eventos Security
```

---

## COMANDOS LINUX

### NETWORKING
```bash
ip addr show                    # Ver IPs (reemplaza ifconfig)
ip route show                   # Ver tabla rutas
ip link set eth0 up            # Activar interfaz

ifconfig eth0 192.168.1.10 netmask 255.255.255.0  # Asignar IP (legacy)

netstat -tulpn                  # Ver puertos abiertos + procesos
ss -tulpn                       # Reemplazo moderno de netstat
lsof -i :80                     # Ver qué usa puerto 80

nslookup google.com             # Resolver DNS
dig google.com                  # DNS query avanzado
dig @8.8.8.8 example.com MX     # Consultar MX con DNS específico

ping -c 4 8.8.8.8               # Ping (4 paquetes)
traceroute google.com           # Traza ruta
mtr google.com                  # Ping + traceroute continuo

arp -a                          # Ver tabla ARP
route -n                        # Ver tabla rutas
```

### FIREWALL (iptables/ufw)
```bash
# UFW (Ubuntu Firewall - simple)
ufw status                      # Ver estado
ufw enable                      # Activar firewall
ufw allow 22/tcp                # Permitir SSH
ufw deny 445/tcp                # Bloquear SMB
ufw delete allow 80/tcp         # Eliminar regla

# iptables (avanzado)
iptables -L -n -v               # Listar reglas
iptables -A INPUT -p tcp --dport 22 -j ACCEPT   # Permitir SSH
iptables -A INPUT -s 203.0.113.0/24 -j DROP     # Bloquear subnet
iptables -F                     # Flush todas las reglas (¡PELIGRO!)
```

### USUARIOS Y PERMISOS
```bash
whoami                          # Usuario actual
id                              # UID, GID, grupos
sudo -l                         # Ver permisos sudo

useradd -m newuser              # Crear usuario
userdel -r olduser              # Eliminar usuario + home
passwd username                 # Cambiar contraseña

chmod 644 file.txt              # Permisos: rw-r--r--
chmod 755 script.sh             # Permisos: rwxr-xr-x
chown user:group file.txt       # Cambiar propietario

ls -la                          # Listar archivos + permisos
```

### PROCESOS Y SERVICIOS
```bash
ps aux                          # Listar todos los procesos
ps aux | grep malware           # Buscar proceso específico
top                             # Monitor procesos en tiempo real
htop                            # Monitor mejorado (si está instalado)

kill 1234                       # Matar proceso (SIGTERM)
kill -9 1234                    # Forzar muerte (SIGKILL)
killall firefox                 # Matar por nombre

# systemd (servicios)
systemctl status nginx          # Ver estado servicio
systemctl start nginx           # Iniciar servicio
systemctl stop nginx            # Detener servicio
systemctl restart nginx         # Reiniciar servicio
systemctl enable nginx          # Auto-inicio al boot
systemctl disable nginx         # Deshabilitar auto-inicio
```

### LOGS
```bash
tail -f /var/log/auth.log       # Ver log en tiempo real
tail -100 /var/log/syslog       # Últimas 100 líneas
grep "Failed password" /var/log/auth.log  # Buscar intentos fallidos
journalctl -u ssh -f            # Ver logs SSH (systemd)
journalctl --since "1 hour ago" # Logs última hora
```

### SEGURIDAD Y FORENSE
```bash
# Búsqueda de malware/archivos sospechosos
find / -name "*.php" -mtime -1  # PHP modificados última 24h
find /tmp -type f -executable   # Ejecutables en /tmp (sospechoso)
find / -perm -4000              # Archivos con SUID (posible escalación)

# Hash de archivos
md5sum file.txt                 # Hash MD5
sha256sum file.txt              # Hash SHA-256

# Conexiones de red sospechosas
lsof -i -P -n                   # Listar conexiones + procesos
netstat -antp | grep ESTABLISHED # Conexiones activas

# Usuarios logueados
w                               # Quién está logueado
last                            # Historial de logins
lastb                           # Intentos fallidos de login
```

---

## WIRESHARK / TCPDUMP

### tcpdump (captura de paquetes)
```bash
tcpdump -i eth0                 # Capturar en eth0
tcpdump -i eth0 -w capture.pcap # Guardar a archivo
tcpdump -r capture.pcap         # Leer archivo
tcpdump host 192.168.1.10       # Solo tráfico de/hacia host
tcpdump port 80                 # Solo puerto 80
tcpdump src 192.168.1.10 and dst port 443  # Combinación filtros
tcpdump -nn -A 'tcp[13] = 2'    # Capturar solo SYN packets
```

### Wireshark Display Filters (PBQs comunes)
```
ip.addr == 192.168.1.10         # Tráfico de/hacia IP
ip.src == 192.168.1.10          # Solo origen
tcp.port == 80                  # Puerto TCP 80
http.request.method == "POST"   # Solo POST requests
dns.qry.name contains "malware" # DNS queries con "malware"
tcp.flags.syn == 1 && tcp.flags.ack == 0  # Solo SYN (port scan)
ssl.handshake.type == 1         # TLS Client Hello
http.response.code == 404       # HTTP 404 errors
```

---

## NMAP (RECONNAISSANCE)

```bash
nmap 192.168.1.1                # Scan básico (top 1000 puertos)
nmap -p 1-65535 192.168.1.1     # Scan todos los puertos
nmap -p 22,80,443 192.168.1.1   # Puertos específicos

nmap -sS 192.168.1.1            # SYN scan (stealth)
nmap -sT 192.168.1.1            # TCP connect scan
nmap -sU 192.168.1.1            # UDP scan
nmap -sV 192.168.1.1            # Detectar versiones servicios
nmap -O 192.168.1.1             # Detectar OS

nmap -A 192.168.1.1             # Aggressive scan (OS, version, scripts)
nmap 192.168.1.0/24             # Scan subnet completo

nmap -Pn 192.168.1.1            # Sin ping (útil si firewall bloquea ICMP)
nmap --script vuln 192.168.1.1  # Scan vulnerabilidades
```

---

## CÁLCULOS DE RED (SUBNETTING)

### Conversión Decimal ↔ Binario
```
128  64  32  16   8   4   2   1   (potencias de 2)
  1   1   0   0   0   0   0   0   = 192
  1   1   1   1   1   1   1   1   = 255
  1   1   1   1   1   1   1   0   = 254
```

### Máscaras de Subred Comunes
```
/8  = 255.0.0.0         = 16,777,216 hosts
/16 = 255.255.0.0       = 65,536 hosts
/24 = 255.255.255.0     = 254 hosts
/25 = 255.255.255.128   = 126 hosts
/26 = 255.255.255.192   = 62 hosts
/27 = 255.255.255.224   = 30 hosts
/28 = 255.255.255.240   = 14 hosts
/29 = 255.255.255.248   = 6 hosts
/30 = 255.255.255.252   = 2 hosts (enlaces punto-a-punto)
```

### Fórmula Rápida
```
Número de hosts = 2^(32 - máscara) - 2

Ejemplo: /26
Hosts = 2^(32-26) - 2 = 2^6 - 2 = 64 - 2 = 62 hosts
```

---

## PUERTOS COMUNES (MEMORIZAR)

| Puerto | Protocolo | Uso |
|--------|-----------|-----|
| 20/21  | FTP       | Transferencia archivos (DATA/CONTROL) |
| 22     | SSH       | Shell seguro / SFTP |
| 23     | Telnet    | Shell inseguro (NO USAR) |
| 25     | SMTP      | Envío email |
| 53     | DNS       | Resolución nombres |
| 67/68  | DHCP      | Asignación IP dinámica |
| 80     | HTTP      | Web sin cifrar |
| 110    | POP3      | Recepción email (descarga) |
| 123    | NTP       | Sincronización tiempo |
| 143    | IMAP      | Recepción email (server-side) |
| 161/162| SNMP      | Gestión dispositivos red |
| 389    | LDAP      | Directorio (Active Directory) |
| 443    | HTTPS     | Web cifrada |
| 445    | SMB       | Compartir archivos Windows |
| 636    | LDAPS     | LDAP sobre SSL |
| 993    | IMAPS     | IMAP sobre SSL |
| 995    | POP3S     | POP3 sobre SSL |
| 1433   | MSSQL     | Microsoft SQL Server |
| 1812   | RADIUS    | Autenticación AAA |
| 3306   | MySQL     | Base de datos MySQL |
| 3389   | RDP       | Remote Desktop Protocol |
| 5060   | SIP       | VoIP señalización |
| 5432   | PostgreSQL| Base de datos PostgreSQL |
| 8080   | HTTP-ALT  | Web alternativo (proxy) |

---

## TROUBLESHOOTING RÁPIDO

### No hay conectividad
```
1. ping 127.0.0.1       # Verificar stack TCP/IP local
2. ping <IP_local>      # Verificar interfaz local
3. ping <Gateway>       # Verificar conexión a router
4. ping 8.8.8.8         # Verificar salida a Internet
5. nslookup google.com  # Verificar DNS
```

### Problema de DNS
```
ipconfig /flushdns      # Windows
resolvectl flush-caches # Linux (systemd-resolved)
cat /etc/resolv.conf    # Ver servidores DNS configurados
```

### Aplicación no conecta
```
netstat -ano | find "PORT"  # Windows: ver si puerto está en uso
ss -tulpn | grep PORT       # Linux: ver proceso usando puerto
telnet <IP> <PORT>          # Test conectividad a puerto específico
```

---

## RESPUESTA A INCIDENTES (ORDEN CORRECTO)

```
1. PREPARACIÓN
   - Políticas, herramientas, training

2. IDENTIFICACIÓN
   - Detectar anomalía
   - Clasificar severidad

3. CONTENCIÓN
   - Aislar host comprometido
   - Prevenir propagación

4. ERRADICACIÓN
   - Eliminar malware
   - Cerrar vulnerabilidad

5. RECUPERACIÓN
   - Restaurar sistemas
   - Monitorear normalidad

6. LESSONS LEARNED
   - Documentar
   - Actualizar procedimientos
```

---

## FORENSE (ORDEN DE VOLATILIDAD)

**Recolectar en este orden** (de más volátil a menos):
```
1. Registros CPU, caché
2. Memoria RAM (dump)
3. Estado de red (conexiones activas)
4. Procesos en ejecución
5. Archivos temporales
6. Disco duro
7. Logs remotos
8. Backups
```

**Comandos forenses**:
```bash
# Linux: captura memoria RAM
dd if=/dev/mem of=memory.img

# Linux: crear imagen disco
dd if=/dev/sda of=disk.img bs=4M

# Windows: hash de archivo (verificar integridad)
certutil -hashfile file.exe SHA256
```

---

**¡IMPRIME ESTA HOJA Y LLÉVALA AL EXAMEN!**

En PBQs te darán escenarios donde necesitarás:
- Identificar comando correcto para diagnosticar
- Configurar firewall
- Troubleshoot conectividad
- Analizar logs
- Calcular subnets

**Recuerda**: En Windows usa `help <comando>` o `<comando> /?`
En Linux usa `man <comando>` o `<comando> --help`
