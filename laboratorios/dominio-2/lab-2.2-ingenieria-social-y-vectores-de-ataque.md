================================================================================
 LAB-2.2 - Ingeniería Social y Vectores de Ataque
================================================================================

DOMINIO: Dominio 2 - Amenazas, Vulnerabilidades y Mitigaciones
OBJETIVOS: 2.2
CONCEPTOS: Phishing, Spear phishing, Vishing, Pretexting, Typosquatting, Evil Twin, Baiting, BEC, SPF, DKIM, DMARC
DIFICULTAD: Media
TIEMPO ESTIMADO: 60 min

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • Kali Linux
  • theHarvester
  • GoPhish
  • dig / nslookup

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Reconocimiento OSINT con theHarvester (emails, subdominios)
  2. Analizar cabeceras de email de phishing (IOCs)
  3. Generar variantes de typosquatting de un dominio
  4. Analizar Evil Twin (detección por BSSID duplicado)
  5. Inspeccionar dispositivos USB conectados (baiting)
  6. Crear script de pretexto de vishing
  7. Instalar y explorar GoPhish (simulación de campaña)
  8. Verificar registros SPF, DKIM y DMARC de un dominio

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------
# theHarvester - reconocimiento OSINT
theHarvester -d tesla.com -b crtsh,hackertarget,rapiddns -l 50

# Cabeceras de email sospechoso
cat /tmp/email_sospechoso.txt

# Typosquatting con Python
python3 -c "..."

# Dispositivos USB
lsusb
sudo dmesg | tail -20 | grep -i usb

# GoPhish
cd /tmp/gophish && sudo ./gophish
# Admin: https://localhost:3333

# SPF
dig TXT google.com | grep spf

# DMARC
dig TXT _dmarc.google.com

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------
  1. ¿Diferencia entre phishing, spear phishing y whaling?
  2. ¿Qué es el pretexting y cómo se diferencia del phishing?
  3. ¿Cómo funciona SPF, DKIM y DMARC para prevenir phishing?
  4. ¿Por qué el Evil Twin es peligroso aunque la red use WPA2?

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------


