================================================================================
 LAB-4.3 - SIEM con Wazuh - Detección y Alertas
================================================================================

DOMINIO: Dominio 4 - Operaciones de Seguridad
OBJETIVOS: 4.4, 4.9
CONCEPTOS: SIEM, Log Management, Correlation Rules, Wazuh
DIFICULTAD: Alta
TIEMPO ESTIMADO: 90 min

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • Wazuh Manager
  • Agents (Linux/Windows)
  • Docker

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Desplegar Wazuh Manager con Docker
  2. Instalar agentes Wazuh en VMs (Linux + Windows)
  3. Configurar recolección de logs centralizados
  4. Crear regla personalizada (alerta login fallido 5+ veces)
  5. Generar eventos de prueba (intentos login fallidos)
  6. Verificar alertas en dashboard Wazuh
  7. Configurar integración con VirusTotal (file integrity)
  8. Probar FIM (File Integrity Monitoring)
  9. Crear reporte de eventos de seguridad

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------
# Desplegar Wazuh con Docker
docker-compose -f wazuh-docker.yml up -d

# Instalar agente Linux
wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.x.x_amd64.deb
sudo WAZUH_MANAGER='192.168.1.100' dpkg -i wazuh-agent_*.deb
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent

# Verificar conectividad agente
sudo /var/ossec/bin/agent_control -lc

# Ver logs del agente
sudo tail -f /var/ossec/logs/ossec.log

# Generar eventos de prueba (login fallido)
for i in {1..6}; do ssh wronguser@localhost; done

# Acceder dashboard Wazuh
# https://localhost:443
# admin / admin (cambiar contraseña)

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------
  1. ¿Qué es un SIEM y cuál es su función principal?
  2. ¿Por qué centralizar logs es crítico?
  3. ¿Qué es correlation en un SIEM?
  4. ¿Diferencia entre SIEM y SOAR?

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------


