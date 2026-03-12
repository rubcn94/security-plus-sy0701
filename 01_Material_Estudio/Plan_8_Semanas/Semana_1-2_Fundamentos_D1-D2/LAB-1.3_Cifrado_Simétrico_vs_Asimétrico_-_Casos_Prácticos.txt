================================================================================
 LAB-1.3 - Cifrado Simétrico vs Asimétrico - Casos Prácticos
================================================================================

DOMINIO: Dominio 1 - Conceptos Generales de Seguridad
OBJETIVOS: 1.4
CONCEPTOS: AES, RSA, ECC, Hash, SHA-256
DIFICULTAD: Baja
TIEMPO ESTIMADO: 30-45 min

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • OpenSSL
  • Python 3

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Cifrar archivo con AES-256-CBC (simétrico)
  2. Descifrar archivo con clave simétrica
  3. Generar par de claves RSA (asimétrico)
  4. Cifrar datos pequeños con RSA público
  5. Descifrar con RSA privado
  6. Generar hash SHA-256 de un archivo
  7. Verificar integridad con hash
  8. Firmar digitalmente un documento
  9. Verificar firma digital

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------
# Cifrar archivo con AES-256
openssl enc -aes-256-cbc -salt -in archivo.txt -out archivo.enc

# Descifrar
openssl enc -d -aes-256-cbc -in archivo.enc -out archivo.txt

# Generar par RSA
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem

# Cifrar con RSA (archivos pequeños)
openssl rsautl -encrypt -inkey public.pem -pubin -in mensaje.txt -out mensaje.enc

# Descifrar con RSA
openssl rsautl -decrypt -inkey private.pem -in mensaje.enc -out mensaje.txt

# Hash SHA-256
openssl dgst -sha256 archivo.txt

# Firmar digitalmente
openssl dgst -sha256 -sign private.pem -out firma.sig archivo.txt

# Verificar firma
openssl dgst -sha256 -verify public.pem -signature firma.sig archivo.txt

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------
  1. ¿Cuándo usar cifrado simétrico vs asimétrico?
  2. ¿Por qué RSA no se usa para cifrar archivos grandes?
  3. ¿Diferencia entre cifrado e integridad?
  4. ¿Qué es una firma digital y cómo funciona?

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------


