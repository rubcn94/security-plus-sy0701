# LAB-1.3: Cifrado Simétrico vs Asimétrico - Guía de Ejecución

**Estado**: ✅ Kali VM iniciada
**Tiempo estimado**: 30-45 minutos
**Dificultad**: Baja (ideal para empezar)

---

## Paso 1: Acceder a Kali

La VM ya está iniciada. Ahora accede de una de estas formas:

### Opción A: Consola VirtualBox (más fácil)
- La ventana de VirtualBox debería estar abierta
- Login con tus credenciales de Kali

### Opción B: SSH (si tienes configurado)
```bash
ssh kali@<ip-de-kali>
```

---

## Paso 2: Crear Directorio de Trabajo

Una vez dentro de Kali:

```bash
# Crear directorio para el lab
mkdir -p ~/security-labs/lab1.3
cd ~/security-labs/lab1.3

# Verificar que OpenSSL está instalado
openssl version
# Deberías ver: OpenSSL 3.x.x o similar
```

---

## Paso 3: EJERCICIO 1 - Cifrado Simétrico (AES-256)

### 3.1 Crear archivo de prueba

```bash
# Crear archivo con texto de prueba
echo "Este es un mensaje secreto para cifrar con AES-256" > mensaje_secreto.txt

# Ver contenido original
cat mensaje_secreto.txt
```

### 3.2 Cifrar con AES-256-CBC

```bash
# Cifrar el archivo (te pedirá una contraseña)
openssl enc -aes-256-cbc -salt -in mensaje_secreto.txt -out mensaje_secreto.enc

# Usar password: SecretPass123 (para el ejercicio)
```

**¿Qué está pasando?**
- `-aes-256-cbc`: Algoritmo de cifrado simétrico AES con clave de 256 bits
- `-salt`: Añade sal aleatoria para evitar ataques de diccionario
- `-in`: Archivo de entrada
- `-out`: Archivo cifrado de salida

### 3.3 Verificar que está cifrado

```bash
# Intentar leer el archivo cifrado (verás basura)
cat mensaje_secreto.enc

# Ver en hexadecimal
xxd mensaje_secreto.enc | head
```

### 3.4 Descifrar

```bash
# Descifrar (usa la misma contraseña)
openssl enc -d -aes-256-cbc -in mensaje_secreto.enc -out mensaje_descifrado.txt

# Verificar que se descifró correctamente
cat mensaje_descifrado.txt
```

**✅ Checkpoint 1**: El archivo descifrado debe ser idéntico al original.

---

## Paso 4: EJERCICIO 2 - Cifrado Asimétrico (RSA)

### 4.1 Generar par de claves RSA

```bash
# Generar clave privada RSA de 2048 bits
openssl genrsa -out private_rsa.pem 2048

# Ver la clave privada
cat private_rsa.pem

# Extraer clave pública
openssl rsa -in private_rsa.pem -pubout -out public_rsa.pem

# Ver la clave pública
cat public_rsa.pem
```

**¿Qué tenemos ahora?**
- `private_rsa.pem`: Clave privada (NUNCA compartir)
- `public_rsa.pem`: Clave pública (se puede compartir libremente)

### 4.2 Crear mensaje pequeño

```bash
# RSA solo puede cifrar mensajes pequeños
echo "Mensaje corto para RSA" > mensaje_rsa.txt
```

**IMPORTANTE**: RSA no puede cifrar archivos grandes directamente. Solo datos hasta el tamaño de la clave (2048 bits = 256 bytes - overhead).

### 4.3 Cifrar con clave pública

```bash
# Cualquiera con la clave pública puede cifrar
openssl rsautl -encrypt -inkey public_rsa.pem -pubin -in mensaje_rsa.txt -out mensaje_rsa.enc

# Ver archivo cifrado
xxd mensaje_rsa.enc | head
```

### 4.4 Descifrar con clave privada

```bash
# Solo quien tiene la clave privada puede descifrar
openssl rsautl -decrypt -inkey private_rsa.pem -in mensaje_rsa.enc -out mensaje_rsa_descifrado.txt

# Verificar
cat mensaje_rsa_descifrado.txt
```

**✅ Checkpoint 2**: Solo la clave privada puede descifrar lo que se cifró con la pública.

---

## Paso 5: EJERCICIO 3 - Hash e Integridad (SHA-256)

### 5.1 Calcular hash de un archivo

```bash
# Crear archivo importante
echo "Documento importante que no debe modificarse" > contrato.txt

# Calcular hash SHA-256
openssl dgst -sha256 contrato.txt

# Guardar hash en archivo
openssl dgst -sha256 contrato.txt > contrato.hash
cat contrato.hash
```

**¿Qué es un hash?**
- Función unidireccional
- Cualquier cambio en el archivo produce un hash completamente diferente
- Usado para verificar integridad

### 5.2 Verificar integridad

```bash
# Hash original
cat contrato.hash

# Modificar el archivo
echo "Texto añadido" >> contrato.txt

# Calcular nuevo hash
openssl dgst -sha256 contrato.txt

# Comparar: ¿Son iguales? NO → El archivo fue modificado
```

**✅ Checkpoint 3**: Los hashes deben ser diferentes después de modificar el archivo.

---

## Paso 6: EJERCICIO 4 - Firma Digital

### 6.1 Firmar un documento

```bash
# Crear documento a firmar
echo "Acuerdo legal entre las partes" > acuerdo.txt

# Firmar con clave privada
openssl dgst -sha256 -sign private_rsa.pem -out acuerdo.sig acuerdo.txt

# Ver firma (binario)
ls -lh acuerdo.sig
```

**¿Qué es una firma digital?**
1. Se calcula hash del documento
2. Se cifra el hash con la clave **privada**
3. Cualquiera puede verificar con la clave **pública**

### 6.2 Verificar firma

```bash
# Verificar que la firma es válida
openssl dgst -sha256 -verify public_rsa.pem -signature acuerdo.sig acuerdo.txt

# Deberías ver: Verified OK
```

### 6.3 Probar con documento modificado

```bash
# Modificar documento
echo "Modificación fraudulenta" >> acuerdo.txt

# Intentar verificar (debería fallar)
openssl dgst -sha256 -verify public_rsa.pem -signature acuerdo.sig acuerdo.txt

# Deberías ver: Verification Failure
```

**✅ Checkpoint 4**: La firma NO verifica si el documento se modifica.

---

## Paso 7: Comparación Final

Ahora crea una tabla con tus resultados:

```bash
# Crear archivo resumen
cat > resumen_lab1.3.txt <<EOF
================================================================================
RESUMEN LAB-1.3: Cifrado Simétrico vs Asimétrico
================================================================================

CIFRADO SIMETRICO (AES-256):
  - Velocidad: Muy rápido
  - Uso de claves: 1 clave (compartida)
  - Tamaño: Sin límite práctico
  - Problema: ¿Cómo compartir la clave de forma segura?

CIFRADO ASIMETRICO (RSA):
  - Velocidad: Más lento
  - Uso de claves: 2 claves (pública/privada)
  - Tamaño: Limitado (256 bytes con RSA-2048)
  - Ventaja: No necesitas compartir secreto

HASH (SHA-256):
  - Propósito: Integridad (detectar cambios)
  - NO es cifrado (unidireccional)
  - Produce huella digital única

FIRMA DIGITAL:
  - Propósito: Autenticidad + Integridad + No repudio
  - Usa clave privada para firmar
  - Usa clave pública para verificar

COMBINACIÓN COMÚN (HTTPS/TLS):
  1. RSA para intercambiar clave simétrica (handshake)
  2. AES para cifrar datos (conexión)
  3. SHA para integridad
  4. Firma digital para autenticar servidor

================================================================================
EOF

cat resumen_lab1.3.txt
```

---

## Paso 8: Preguntas de Repaso

Responde estas preguntas en el archivo de notas:

```bash
nano respuestas_lab1.3.txt
```

### 1. ¿Cuándo usar cifrado simétrico vs asimétrico?

**Tu respuesta aquí**:
- Simétrico: Para cifrar grandes cantidades de datos (archivos, discos, comunicaciones)
- Asimétrico: Para intercambio de claves, autenticación, firmas digitales

### 2. ¿Por qué RSA no se usa para cifrar archivos grandes?

**Tu respuesta aquí**:
- Es muy lento (operaciones matemáticas complejas)
- Limitación de tamaño (solo puede cifrar hasta tamaño de la clave)
- Por eso HTTPS usa RSA solo para intercambiar clave AES

### 3. ¿Diferencia entre cifrado e integridad?

**Tu respuesta aquí**:
- Cifrado: Protege CONFIDENCIALIDAD (nadie puede leer)
- Integridad (hash): Protege contra MODIFICACIÓN (detecta cambios)
- Se complementan: TLS usa ambos

### 4. ¿Qué es una firma digital y cómo funciona?

**Tu respuesta aquí**:
1. Se calcula hash del documento
2. Se cifra hash con clave PRIVADA del firmante
3. Cualquiera verifica con clave PÚBLICA
4. Garantiza: autenticidad + integridad + no repudio

---

## Paso 9: Limpieza y Documentación

```bash
# Ver todos los archivos creados
ls -lh ~/security-labs/lab1.3/

# Deberías tener:
# - Archivos originales (.txt)
# - Archivos cifrados (.enc)
# - Claves RSA (.pem)
# - Firmas (.sig)
# - Hashes (.hash)
```

---

## ✅ Laboratorio Completado

Has aprendido:
- ✅ Cifrar/descifrar con AES-256 (simétrico)
- ✅ Generar par de claves RSA
- ✅ Cifrar/descifrar con RSA (asimétrico)
- ✅ Calcular hashes SHA-256
- ✅ Crear y verificar firmas digitales
- ✅ Entender cuándo usar cada técnica

---

## Paso 10: Apagar VM Correctamente

Desde tu terminal Windows:

```powershell
# Apagar Kali correctamente
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' controlvm Kali acpipowerbutton

# Esperar 30 segundos y verificar que se apagó
Start-Sleep -Seconds 30
& 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe' showvminfo Kali | Select-String "State:"
```

---

## Conceptos para el Examen Security+

| Concepto | Definición | Examen |
|----------|-----------|--------|
| AES-256 | Cifrado simétrico estándar | ⭐⭐⭐ |
| RSA | Cifrado asimétrico para claves | ⭐⭐⭐ |
| SHA-256 | Hash para integridad | ⭐⭐⭐ |
| Firma Digital | Autenticidad + No repudio | ⭐⭐ |
| Confidencialidad | Cifrado protege | ⭐⭐⭐ |
| Integridad | Hash detecta cambios | ⭐⭐⭐ |
| No repudio | Firma prueba autoría | ⭐⭐ |

---

**¡Excelente trabajo!** 🔐

Próximo lab recomendado: **LAB-1.1 (PKI y Certificados)** - Nivel medio, 45 min
