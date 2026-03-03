================================================================================
 LAB-2.3 - Reconnaissance y OSINT con MITRE ATT&CK
================================================================================

DOMINIO: Dominio 2 - Amenazas, Vulnerabilidades y Mitigaciones
OBJETIVOS: 2.5
CONCEPTOS: MITRE ATT&CK, OSINT, Reconnaissance, Footprinting
DIFICULTAD: Baja
TIEMPO ESTIMADO: 45 min

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • Kali Linux
  • theHarvester
  • Shodan
  • Maltego CE

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Mapear tácticas de Reconnaissance en MITRE ATT&CK
  2. Usar theHarvester para recopilar emails/subdominios
  3. Consultar Shodan para dispositivos IoT expuestos
  4. Realizar whois lookup de dominio objetivo
  5. Enumerar subdominios con subfinder
  6. Buscar leaks de credenciales en HaveIBeenPwned
  7. Documentar hallazgos en formato TTP
  8. Mapear hallazgos a MITRE ATT&CK Navigator

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------
# theHarvester - recopilar info
theHarvester -d example.com -b google,bing,linkedin

# Whois lookup
whois example.com

# Subfinder - enumerar subdominios
subfinder -d example.com -o subdominios.txt

# Shodan CLI (requiere API key)
shodan search 'org:"Example Corp"'

# DNSRecon
dnsrecon -d example.com -t std

# Nmap para OS fingerprinting
nmap -O -sV example.com

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------
  1. ¿Cuáles son las 14 tácticas de MITRE ATT&CK?
  2. ¿Diferencia entre activo y pasivo reconnaissance?
  3. ¿Por qué es importante OSINT en pentesting?
  4. ¿Qué es footprinting y enumeration?

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------


