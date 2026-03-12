================================================================================
 LAB-3.1 - Configuración de Firewall y Segmentación de Red
================================================================================

DOMINIO: Dominio 3 - Arquitectura de Seguridad
OBJETIVOS: 3.2
CONCEPTOS: Firewall, VLAN, ACL, Network Segmentation
DIFICULTAD: Media
TIEMPO ESTIMADO: 60 min

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • pfSense VM
  • 2+ VMs Linux
  • VirtualBox/VMware

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Instalar pfSense como firewall virtual
  2. Configurar 3 interfaces: WAN, LAN, DMZ
  3. Crear reglas de firewall para separar redes
  4. Configurar VLAN para segmentar DMZ
  5. Implementar regla deny-all por defecto
  6. Permitir solo HTTP/HTTPS desde LAN a DMZ
  7. Bloquear todo tráfico directo Internet → DMZ
  8. Configurar NAT para LAN
  9. Probar conectividad y verificar logs

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------
# Desde VM en LAN - probar conectividad
ping 192.168.1.1  # Gateway pfSense

# Probar acceso web a DMZ
curl http://192.168.2.10

# Intentar SSH (debería fallar si está bloqueado)
ssh user@192.168.2.10

# Verificar rutas
ip route show

# Traceroute para ver saltos
traceroute 8.8.8.8

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------
  1. ¿Qué es una DMZ y por qué es importante?
  2. ¿Diferencia entre stateful y stateless firewall?
  3. ¿Qué es una VLAN y cómo ayuda a la seguridad?
  4. ¿Por qué usar deny-all como regla por defecto?

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------


