================================================================================
 LAB-1.1 - Configuración de PKI y Certificados
================================================================================

DOMINIO: Dominio 1 - Conceptos Generales de Seguridad
OBJETIVOS: 1.4
CONCEPTOS: PKI, CA, Certificados X.509, CRL, OCSP
DIFICULTAD: Media
TIEMPO ESTIMADO: 45-60 min

--------------------------------------------------------------------------------
 REQUISITOS PREVIOS
--------------------------------------------------------------------------------
  • Windows Server o Linux
  • OpenSSL

--------------------------------------------------------------------------------
 TAREAS A REALIZAR
--------------------------------------------------------------------------------
  1. Instalar OpenSSL y verificar versión
  2. Crear CA raíz (Root CA) privada
  3. Generar certificado autofirmado para la CA
  4. Crear solicitud de certificado (CSR) para servidor web
  5. Firmar el CSR con la CA raíz
  6. Verificar cadena de certificados
  7. Configurar CRL (Certificate Revocation List)
  8. Revocar un certificado y verificar CRL
  9. EXTRA: Implementar OCSP responder

--------------------------------------------------------------------------------
 COMANDOS Y CONFIGURACIONES
--------------------------------------------------------------------------------
# Generar clave privada CA
openssl genrsa -aes256 -out ca-key.pem 4096

# Crear certificado CA autofirmado
openssl req -new -x509 -days 3650 -key ca-key.pem -sha256 -out ca.pem

# Generar clave privada servidor
openssl genrsa -out server-key.pem 4096

# Crear CSR
openssl req -new -key server-key.pem -out server.csr

# Firmar certificado servidor
openssl x509 -req -days 365 -in server.csr -CA ca.pem -CAkey ca-key.pem -CAcreateserial -out server-cert.pem

# Verificar certificado
openssl x509 -in server-cert.pem -text -noout

# Verificar cadena
openssl verify -CAfile ca.pem server-cert.pem

--------------------------------------------------------------------------------
 PREGUNTAS DE REPASO
--------------------------------------------------------------------------------
  1. ¿Cuál es la diferencia entre CA raíz e intermedia?
  2. ¿Qué información contiene un certificado X.509?
  3. ¿Por qué es importante la CRL/OCSP?
  4. ¿Qué es un certificado wildcard vs SAN?

--------------------------------------------------------------------------------
 NOTAS
--------------------------------------------------------------------------------


