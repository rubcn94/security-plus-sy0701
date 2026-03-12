================================================================================
 LAB-4.2 - Respuesta a Incidentes - Análisis Forense
================================================================================

DOMINIO: Dominio 4 - Operaciones de Seguridad
OBJETIVOS: 4.8
CONCEPTOS: Incident Response, Digital Forensics, Chain of Custody, Memory Dump
DIFICULTAD: Alta
TIEMPO ESTIMADO: 90 min

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • Kali Linux
  • Volatility
  • Autopsy
  • VM comprometida

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Escenario: detectar sistema comprometido
  2. PRESERVAR evidencia (no modificar sistema)
  3. Crear imagen forense del disco con dd
  4. Calcular hash de la imagen (cadena de custodia)
  5. Capturar memoria RAM con LiME
  6. Analizar memoria con Volatility (procesos, conexiones)
  7. Analizar disco con Autopsy
  8. Identificar IOCs (malware, backdoors, logs)
  9. Documentar hallazgos en informe forense

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------
# Crear imagen forense del disco
sudo dd if=/dev/sda of=evidencia.img bs=4M status=progress

# Hash de imagen (chain of custody)
sha256sum evidencia.img > evidencia.sha256

# Capturar memoria RAM (LiME)
sudo insmod lime-*.ko "path=/tmp/memoria.lime format=lime"

# Analizar memoria con Volatility
volatility -f memoria.lime --profile=LinuxUbuntu imageinfo
volatility -f memoria.lime --profile=LinuxUbuntu linux_pslist
volatility -f memoria.lime --profile=LinuxUbuntu linux_netstat

# Buscar procesos ocultos
volatility -f memoria.lime --profile=LinuxUbuntu linux_psxview

# Montar imagen forense (read-only)
sudo mount -o ro,loop evidencia.img /mnt/forense

# Analizar con Autopsy (GUI)
autopsy

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------
  1. ¿Qué es la cadena de custodia y por qué es crítica?
  2. ¿Por qué capturar memoria RAM además del disco?
  3. ¿Orden de volatilidad en forensics (RFC 3227)?
  4. ¿Diferencia entre dead box y live response?

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------


