================================================================================
 LAB-2.3 - Reconnaissance y OSINT con MITRE ATT&CK
================================================================================

DOMINIO: Dominio 2 - Amenazas, Vulnerabilidades y Mitigaciones
OBJETIVOS: 2.5
CONCEPTOS: MITRE ATT&CK, OSINT, Reconnaissance, Footprinting, TTP
DIFICULTAD: Baja
TIEMPO ESTIMADO: 45 min

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • Kali Linux
  • theHarvester
  • subfinder
  • dnsrecon
  • nmap
  • curl + python3

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Mapear tácticas de Reconnaissance en MITRE ATT&CK (TA0043)
  2. WHOIS lookup del dominio objetivo
  3. Enumeración DNS completa con dnsrecon
  4. Recopilar subdominios con theHarvester
  5. Enumeración masiva de subdominios con subfinder
  6. Buscar leaks de credenciales en HaveIBeenPwned
  7. Documentar hallazgos en formato TTP
  8. Escaneo activo con nmap

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------
# WHOIS lookup
whois tesla.com | grep -E "Registrar:|Creation Date:|Registry Expiry|Name Server:" | head -15

# DNSRecon - enumeración completa de registros DNS
dnsrecon -d tesla.com -t std

# theHarvester - subdominios y emails
theHarvester -d tesla.com -b crtsh,hackertarget,rapiddns -l 50

# subfinder - enumeración masiva de subdominios
subfinder -d tesla.com -o /tmp/subdominios_tesla.txt

# HaveIBeenPwned - credenciales filtradas
curl -s "https://haveibeenpwned.com/api/v3/breaches" | python3 -c "
import json,sys
data=json.load(sys.stdin)
tesla=[b for b in data if 'tesla' in b.get('Domain','').lower()]
for b in tesla:
    print(b['Name'], '-', b['Domain'], '-', b['BreachDate'])
print(f'Total brechas: {len(data)}')
"

# Documentar TTPs
cat > /tmp/ttp_objetivo.txt << 'EOF'
TA0043 - Reconnaissance
  T1590.002  DNS/Passive DNS
  T1596.001  Search Open Technical Databases
  T1589.001  Credentials
  T1592.002  Software
  T1590.001  IP Addresses
EOF

# Nmap - escaneo activo (T1595)
nmap -sV --open -F tesla.com

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------
  1. ¿Cuáles son las 14 tácticas de MITRE ATT&CK?
  2. ¿Diferencia entre reconocimiento activo y pasivo?
  3. ¿Por qué es importante OSINT en pentesting?
  4. ¿Qué es footprinting y cómo se diferencia de enumeration?

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------


