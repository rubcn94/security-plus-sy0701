================================================================================
 LAB-3.2 - IDS/IPS con Suricata + ELK Stack
================================================================================

DOMINIO: Dominio 3 - Arquitectura de Seguridad
OBJETIVOS: 3.2
CONCEPTOS: IDS, IPS, Suricata, SIEM, ELK
DIFICULTAD: Alta
TIEMPO ESTIMADO: 90 min

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • Linux VM
  • Suricata
  • Elasticsearch
  • Kibana

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Instalar Suricata IDS/IPS
  2. Configurar interfaz de red en modo promiscuo
  3. Descargar reglas ET Open (Emerging Threats)
  4. Configurar Suricata en modo IPS (inline)
  5. Instalar ELK Stack (Elasticsearch, Logstash, Kibana)
  6. Configurar Filebeat para enviar logs a ELK
  7. Generar tráfico malicioso de prueba (ej: nmap scan)
  8. Visualizar alertas en Kibana
  9. Crear dashboard personalizado para eventos

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------
# Instalar Suricata
sudo apt install suricata

# Descargar reglas
sudo suricata-update

# Ejecutar Suricata
sudo suricata -c /etc/suricata/suricata.yaml -i eth0

# Ver logs en tiempo real
sudo tail -f /var/log/suricata/fast.log

# Generar alerta (desde otra VM)
nmap -sS -p- 192.168.1.100

# Verificar alertas JSON
sudo cat /var/log/suricata/eve.json | jq '.event_type'

# Instalar ELK (Docker Compose recomendado)
docker-compose up -d elasticsearch kibana logstash

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------
  1. ¿Diferencia entre IDS e IPS?
  2. ¿Qué es un SIEM y por qué es importante?
  3. ¿Signature-based vs anomaly-based detection?
  4. ¿Por qué enviar logs a sistema externo?

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------


