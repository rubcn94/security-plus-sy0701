================================================================================
 LAB-3.3 - Destrucción Segura de Datos y Crypto-Shredding
================================================================================

DOMINIO: Dominio 3 - Arquitectura de Seguridad
OBJETIVOS: 3.3
CONCEPTOS: Data Sanitization, Crypto-shredding, Secure Erase
DIFICULTAD: Media
TIEMPO ESTIMADO: 45 min

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • Linux VM
  • USB/disco adicional
  • LUKS
  • shred

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Crear disco virtual o usar USB para pruebas
  2. Escribir datos sensibles en disco
  3. Usar 'shred' para sobrescritura múltiple (método tradicional)
  4. Verificar que datos no son recuperables
  5. Crear volumen cifrado con LUKS (crypto-shredding)
  6. Copiar datos al volumen cifrado
  7. Realizar crypto-shredding (borrar solo la clave)
  8. Intentar recuperar datos (imposible sin clave)
  9. Comparar tiempo: shred vs crypto-shredding

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------
# Método 1: Shred (sobrescritura múltiple)
sudo shred -vfz -n 7 /dev/sdb  # 7 pasadas

# Crear archivo de prueba
dd if=/dev/urandom of=datos_sensibles.txt bs=1M count=100

# Shred de archivo
shred -vfz -n 3 datos_sensibles.txt

# Método 2: Crypto-shredding con LUKS
sudo cryptsetup luksFormat /dev/sdb

# Abrir volumen cifrado
sudo cryptsetup luksOpen /dev/sdb datos_cifrados

# Crear filesystem
sudo mkfs.ext4 /dev/mapper/datos_cifrados

# Montar y copiar datos
sudo mount /dev/mapper/datos_cifrados /mnt
sudo cp datos_sensibles.txt /mnt/

# Crypto-shredding (borrar header LUKS)
sudo cryptsetup luksErase /dev/sdb

# Datos ahora irrecuperables (clave destruida)

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------
  1. ¿Por qué shred tradicional NO funciona bien en SSD?
  2. ¿Qué es wear leveling en SSD?
  3. ¿Cómo funciona crypto-shredding?
  4. ¿Cuándo usar ATA Secure Erase vs crypto-shredding?

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------


