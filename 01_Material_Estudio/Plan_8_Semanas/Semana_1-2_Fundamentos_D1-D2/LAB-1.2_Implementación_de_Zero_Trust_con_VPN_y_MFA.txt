================================================================================
 LAB-1.2 - Implementación de Zero Trust con VPN y MFA
================================================================================

DOMINIO: Dominio 1 - Conceptos Generales de Seguridad
OBJETIVOS: 1.2
CONCEPTOS: Zero Trust, VPN, MFA, RADIUS
DIFICULTAD: Alta
TIEMPO ESTIMADO: 90 min

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • Linux VM
  • FreeRADIUS
  • OpenVPN
  • Google Authenticator

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Instalar y configurar OpenVPN server
  2. Configurar FreeRADIUS como AAA server
  3. Integrar Google Authenticator (TOTP) con RADIUS
  4. Configurar OpenVPN para usar RADIUS
  5. Crear usuarios con MFA obligatorio
  6. Probar conexión VPN con usuario+password+OTP
  7. Verificar logs de autenticación
  8. Implementar política de least privilege
  9. EXTRA: Configurar split-tunneling

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------
# Instalar OpenVPN
sudo apt update && sudo apt install openvpn easy-rsa

# Instalar FreeRADIUS
sudo apt install freeradius freeradius-utils

# Instalar Google Authenticator
sudo apt install libpam-google-authenticator

# Generar secreto OTP para usuario
google-authenticator

# Verificar RADIUS
sudo freeradius -X

# Probar autenticación
radtest usuario password localhost 0 testing123

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------
  1. ¿Cuál es el principio fundamental de Zero Trust?
  2. ¿Qué es AAA en el contexto de RADIUS?
  3. ¿Diferencia entre TOTP y HOTP?
  4. ¿Por qué es importante el split-tunneling?

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------


