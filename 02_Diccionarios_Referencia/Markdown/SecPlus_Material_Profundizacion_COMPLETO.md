# Material de Profundizacion Security+ SY0-701

**Objetivo:** Alcanzar 85%+ en el examen
**Fecha de creacion:** 2026-03-02
**Total terminos ALTA prioridad:** 220

---

## Tabla de Contenidos

1. [Terminos Profundizados por Dominio](#terminos-profundizados)
2. [Mapas Conceptuales](#mapas-conceptuales)
3. [PBQs Simuladas](#pbqs-simuladas)
4. [Plan de Estudio](#plan-de-estudio)

---

## Terminos Profundizados


### Conceptos Generales de Seguridad (12%)

**Terminos ALTA:** 45

#### CIA_Triad

**Prioridad:** ALTA

**Definicion base:** Tríada de seguridad fundamental: Confidencialidad (solo personas autorizadas acceden), Integridad (datos no modificados sin autorización), Disponibilidad (acceso cuando se necesita)

**Explicacion detallada:**

Marco fundamental de seguridad de la informacin. Confidencialidad: proteger contra divulgacin no autorizada (cifrado, control de acceso). Integridad: proteger contra modificacin no autorizada (hashing, firma digital). Disponibilidad: garantizar acceso cuando se necesita (redundancia, backup, DDoS protection).

**Ejemplos practicos:**

- Confidencialidad: Cifrar base de datos con AES-256
- Integridad: Usar SHA-256 para verificar archivos descargados
- Disponibilidad: Implementar load balancer + failover automtico

**Conceptos relacionados:** AAA, Zero_Trust, Defense_in_Depth

**Errores comunes:**

- Pensar que solo cifrar = seguridad completa (falta integridad y disponibilidad)
- Olvidar que DDoS ataca la DISPONIBILIDAD, no confidencialidad

---

#### AAA

**Prioridad:** ALTA

**Definicion base:** Authentication (verificar identidad), Authorization (dar permisos), Accounting (registrar acciones). Marco de control de acceso

**Explicacion detallada:**

Marco de control de acceso en 3 fases: 1) Authentication (autenticar): verificar identidad (usuario/contrasea, MFA, certificados). 2) Authorization (autorizar): determinar permisos (RBAC, ACLs). 3) Accounting (auditar): registrar todas las acciones (logs, SIEM).

**Ejemplos practicos:**

- Authentication: Usuario ingresa credenciales  validacin contra AD/LDAP
- Authorization: Usuario tiene rol 'editor'  puede modificar pero no eliminar
- Accounting: Cada accin se registra en syslog con timestamp + usuario + accin

**Conceptos relacionados:** RADIUS, TACACS+, Kerberos, LDAP

**Errores comunes:**

- Confundir authentication con authorization
- No implementar accounting = imposible forensics

---

#### Zero_Trust

**Prioridad:** ALTA

**Definicion base:** Modelo de seguridad que NO confía en ninguna entidad automáticamente. Verificar siempre, dentro o fuera de la red. 'Never trust, always verify'

**Explicacion detallada:**

Modelo de seguridad que elimina la confianza implcita. Principio: 'Never trust, always verify'. No importa si ests dentro o fuera de la red corporativa. Cada acceso requiere verificacin continua: identidad + dispositivo + contexto + comportamiento.

**Ejemplos practicos:**

- Microsegmentacin: cada servicio en VLAN separada con firewall entre ellas
- Verificacin continua: reautenticar cada 15 min aunque ya ests logueado
- Device posture: solo permitir acceso si antivirus actualizado + SO parcheado

**Conceptos relacionados:** Microsegmentation, NAC, Adaptive_Identity, SASE

**Errores comunes:**

- Pensar que VPN = Zero Trust (VPN da acceso amplio, Zero Trust es granular)
- No verificar dispositivos, solo usuarios

---

#### Defense_in_Depth

**Prioridad:** ALTA

**Definicion base:** Múltiples capas de seguridad. Si una falla, las demás protegen. Concepto de defensa en profundidad

**Explicacion detallada:**

Estrategia de mltiples capas de seguridad. Si una capa falla, las dems protegen. Capas tpicas: fsica, red, host, aplicacin, datos. Combina controles tcnicos, administrativos y fsicos.

**Ejemplos practicos:**

- Capa fsica: guardias + cmaras + acceso biomtrico
- Capa red: firewall perimetral + IPS + segmentacin VLAN
- Capa host: antivirus + EDR + host firewall + hardening
- Capa aplicacin: WAF + input validation + CSRF tokens
- Capa datos: cifrado at-rest + cifrado in-transit + DLP

**Conceptos relacionados:** CIA_Triad, Security_Controls, DMZ

**Errores comunes:**

- Redundancia intil: 3 antivirus en el mismo host (no es defense in depth)
- Olvidar la capa fsica: toda la seguridad tcnica intil si roban el servidor

---

#### Security_Control_Types

**Prioridad:** ALTA

**Definicion base:** Preventivo (evita incidentes), Detective (detecta incidentes), Correctivo (corrige tras incidente), Compensatorio (alternativa cuando el control preferido no es viable), Directivo (políticas y procedimientos), Disuasorio (desalienta ataques)

---

#### Security_Control_Categories

**Prioridad:** ALTA

**Definicion base:** Técnico/Lógico (tecnología/sistemas), Gerencial/Administrativo (políticas/procedimientos), Operacional (personas/procesos diarios), Físico (instalaciones materiales)

---

#### AES

**Prioridad:** ALTA

**Definicion base:** Algoritmo de cifrado simétrico estándar. Claves de 128, 192 o 256 bits. Rápido y seguro

---

#### RSA

**Prioridad:** ALTA

**Definicion base:** Algoritmo de cifrado asimétrico. Par de claves pública/privada. Usado para cifrado y firmas digitales

---

#### DHE

**Prioridad:** ALTA

**Definicion base:** Intercambio de claves Diffie-Hellman con claves efimeras temporales. Perfect Forward Secrecy. Nueva clave cada sesion

---

#### Hashing

**Prioridad:** ALTA

**Definicion base:** Función criptográfica unidireccional que genera un valor de longitud fija (hash) a partir de datos de cualquier tamaño. NO es reversible

---

#### SHA

**Prioridad:** ALTA

**Definicion base:** Familia de funciones hash criptográficas. SHA-1 (obsoleto), SHA-2 (SHA-256, SHA-512 - recomendado), SHA-3 (último estándar)

---

#### Digital_Signature

**Prioridad:** ALTA

**Definicion base:** Firma digital para verificar autenticidad e integridad de documentos. Usa criptografia asimetrica (firma con clave privada, verifica con publica)

---

#### DSA

**Prioridad:** ALTA

**Definicion base:** Algoritmo para firmas digitales. Autenticacion, integridad, no repudio. Basado en logaritmo discreto. No para cifrado

---

#### ECDSA

**Prioridad:** ALTA

**Definicion base:** DSA basado en criptografia de curva eliptica. Mas eficiente computacionalmente. Menor tamaño de clave para misma seguridad

---

#### PKI

**Prioridad:** ALTA

**Definicion base:** Infraestructura de gestión de certificados digitales. Incluye CA (Certificate Authority), RA (Registration Authority), certificados X.509

---

#### Certificate

**Prioridad:** ALTA

**Definicion base:** Documento que vincula una clave pública a una identidad. Firmado por una CA. Contiene: titular, clave pública, CA emisora, periodo validez

---

#### CA

**Prioridad:** ALTA

**Definicion base:** Tercera parte confiable que emite, revoca y gestiona certificados digitales. Raiz de confianza en PKI

---

#### OCSP

**Prioridad:** ALTA

**Definicion base:** Protocolo para verificar estado de revocacion de certificado en tiempo real. Mas rapido que CRL

---

#### TPM

**Prioridad:** ALTA

**Definicion base:** Chip criptográfico en placa base para almacenar claves, certificados y realizar operaciones de seguridad. Secure boot, cifrado de disco

---

#### FDE

**Prioridad:** ALTA

**Definicion base:** Cifrado completo del disco por software. Protege TODOS los datos en reposo

---

#### WPA2_WPA3

**Prioridad:** ALTA

**Definicion base:** Protocolos de seguridad Wi-Fi. WPA2 usa AES-CCMP. WPA3 añade SAE (mejor proteccion contra fuerza bruta) y cifrado individualizado

---

#### SAE

**Prioridad:** ALTA

**Definicion base:** Metodo de autenticacion en WPA3 que reemplaza el handshake PSK de WPA2. Resistente a ataques offline de fuerza bruta

---

#### 802.1X

**Prioridad:** ALTA

**Definicion base:** Estandar IEEE para control de acceso a red basado en puertos (NAC). Usa EAP para autenticacion. Requiere: Suplicante, Autenticador, Servidor AAA (RADIUS)

---

#### MDM

**Prioridad:** ALTA

**Definicion base:** Gestion centralizada de dispositivos moviles: configuracion, seguridad, aplicaciones, politicas. Control remoto de smartphones/tablets corporativos

---

#### DKIM

**Prioridad:** ALTA

**Definicion base:** Firma digital en cabeceras de email para verificar autenticidad del remitente y que no fue modificado. Usa criptografia asimetrica

---

#### DMARC

**Prioridad:** ALTA

**Definicion base:** Politica de autenticacion de email que usa SPF y DKIM. Define que hacer con emails que fallan validacion (none/quarantine/reject)

---

#### SPF

**Prioridad:** ALTA

**Definicion base:** Record DNS que especifica que servidores pueden enviar email desde un dominio. Previene email spoofing

---

#### OpenID_Connect

**Prioridad:** ALTA

**Definicion base:** Capa de identidad sobre OAuth 2.0. Permite autenticacion federada (Single Sign-On). Devuelve ID token (JWT) con info del usuario

---

#### SAML_Features

**Prioridad:** ALTA

**Definicion base:** Estandar XML para intercambio de autenticacion/autorizacion entre Identity Provider (IdP) y Service Provider (SP). SSO empresarial

---

#### Biometrics_Types

**Prioridad:** ALTA

**Definicion base:** Autenticacion basada en caracteristicas fisicas/comportamentales. Fisiologica: huella, iris, facial. Comportamental: firma, patron de tecleo, voz

---

#### Hardware_Tokens

**Prioridad:** ALTA

**Definicion base:** Dispositivos fisicos para autenticacion. Tipos: Key fob (OTP), Security key (FIDO2/U2F), RFID badge, Smart card

---

#### Security_Key

**Prioridad:** ALTA

**Definicion base:** Token de hardware para autenticacion sin contraseña. Soporta FIDO2/U2F/WebAuthn. Resistente a phishing

---

#### Password_Policies

**Prioridad:** ALTA

**Definicion base:** Reglas de complejidad, longitud, historial, expiracion. Requisitos: minimo caracteres, mayusculas, numeros, simbolos

---

#### OTP

**Prioridad:** ALTA

**Definicion base:** Contraseña valida para una sola sesion o transaccion. Genera codigo temporal. Componente MFA. Caduca rapidamente

---

#### Just_in_Time_Permissions

**Prioridad:** ALTA

**Definicion base:** Acceso efimero temporal. Privilegios otorgados solo cuando se necesitan. Se revocan automaticamente tras uso. Reduce superficie de ataque

---

#### SHA_3

**Prioridad:** ALTA

**Definicion base:** Familia de funciones hash criptograficas mas reciente. Mayor seguridad que SHA-2. Algoritmo Keccak

---

#### Digital_Certificate

**Prioridad:** ALTA

**Definicion base:** Documento digital que verifica identidad de individuo/dispositivo/organizacion. Emitido por CA. Contiene clave publica + info del titular

---

#### Vishing

**Prioridad:** ALTA

**Definicion base:** Phishing por voz (telefono/VoIP). Atacante llama haciendose pasar por entidad legitima para robar informacion

---

#### Pharming

**Prioridad:** ALTA

**Definicion base:** Redireccion de trafico web a sitio falso mediante envenenamiento DNS o modificacion de archivo hosts. Sin interaccion del usuario

---

#### MSSP

**Prioridad:** ALTA

**Definicion base:** Proveedor externo especializado en seguridad IT. Ofrece SOC, SIEM, gestion de vulnerabilidades, respuesta a incidentes

---

#### STARTTLS

**Prioridad:** ALTA

**Definicion base:** Comando para actualizar conexion no cifrada a cifrada con TLS. Usado en SMTP, IMAP, POP3. Puerto 587 para SMTP

---

#### CCMP

**Prioridad:** ALTA

**Definicion base:** Protocolo de cifrado en WPA2. Basado en AES. Reemplaza TKIP. Mayor seguridad

---

#### Password_Manager

**Prioridad:** ALTA

**Definicion base:** Aplicacion que almacena y gestiona contraseñas de forma segura. Cifrado de boveda. Genera contraseñas fuertes. Una contraseña maestra

---

#### Dictionary_Attack

**Prioridad:** ALTA

**Definicion base:** Ataque de fuerza bruta que usa lista de palabras comunes. Prueba contraseñas probables (diccionario). Mas eficiente que fuerza bruta pura

---

#### ML

**Prioridad:** ALTA

**Definicion base:** Aprendizaje automatico. IA que aprende de datos sin programacion explicita. Deteccion anomalias, threat hunting

---


### Amenazas, Vulnerabilidades y Mitigaciones (22%)

**Terminos ALTA:** 49

#### Threat_Actor

**Prioridad:** ALTA

**Definicion base:** Entidad que representa una amenaza. Tipos: Nation-state (estado), APT (amenaza persistente avanzada), Hacktivist (activismo), Insider (interno), Script kiddie (aficionado)

---

#### APT

**Prioridad:** ALTA

**Definicion base:** Ataque cibernetico sofisticado y prolongado. Bien financiado (nation-states). Objetivo especifico. Persistente en red

**Explicacion detallada:**

Advanced Persistent Threat: ataque sofisticado, bien financiado (nation-states), dirigido a objetivos especficos de alto valor. Fases tpicas: reconocimiento  initial access  establish foothold  escalate privileges  lateral movement  data exfiltration  maintain persistence. Duracin: meses o aos sin ser detectado.

**Ejemplos practicos:**

- APT29 (Cozy Bear, Rusia): compromiso de SolarWinds 2020
- APT28 (Fancy Bear): phishing spear con exploit 0-day
- Tcnicas: living off the land, cifrado custom, C2 mediante DNS tunneling

**Conceptos relacionados:** Threat_Actor, C2, Lateral_Movement, Persistence

**Errores comunes:**

- Confundir APT con ransomware (APT busca espionaje prolongado, no dinero rpido)
- Pensar que solo antivirus detecta APT (necesitas EDR + threat hunting)

---

#### Phishing

**Prioridad:** ALTA

**Definicion base:** Ataque de ingeniería social mediante email fraudulento que simula ser legítimo para robar credenciales o instalar malware

**Explicacion detallada:**

Ataque de ingeniera social mediante comunicacin fraudulenta (email, SMS, llamada) que simula ser legtima. Objetivo: robar credenciales, instalar malware, obtener informacin sensible. Tipos: phishing genrico (masivo), spear phishing (dirigido), whaling (ejecutivos), vishing (voz), smishing (SMS).

**Ejemplos practicos:**

- Email que simula ser banco  link a pgina falsa  robo de credenciales
- Archivo adjunto malicioso (macro en Word)  ejecuta payload  ransomware
- SMS urgente 'tu cuenta ser bloqueada'  click en link  instalacin de troyano

**Conceptos relacionados:** DKIM, SPF, DMARC, Email_Gateway, Security_Awareness

**Errores comunes:**

- Pensar que solo tecnologa previene phishing (training de usuarios es crtico)
- Confiar en 'De:' del email (fcilmente falsificable sin SPF/DKIM)

---

#### Spear_Phishing

**Prioridad:** ALTA

**Definicion base:** Phishing dirigido a persona o organización específica. Altamente personalizado con información de OSINT

---

#### BEC

**Prioridad:** ALTA

**Definicion base:** Ataque sofisticado de phishing dirigido a empresas. Suplanta identidad de ejecutivo o proveedor para transferencias fraudulentas

---

#### Impersonation

**Prioridad:** ALTA

**Definicion base:** Hacerse pasar por otra persona u organización legítima para ganar confianza y acceso

---

#### Typosquatting

**Prioridad:** ALTA

**Definicion base:** Registro de dominios con errores tipograficos de sitios populares. Explota errores de escritura usuarios. Phishing y distribucion malware

---

#### Malware

**Prioridad:** ALTA

**Definicion base:** Software malicioso diseñado para dañar, explotar o comprometer sistemas. Tipos: virus, gusano, troyano, ransomware, spyware, rootkit

---

#### Ransomware

**Prioridad:** ALTA

**Definicion base:** Malware que cifra archivos de victima. Exige pago (rescate) para clave de descifrado. Doble extorsion: cifrado + amenaza de publicacion

**Explicacion detallada:**

Malware que cifra archivos de la vctima y exige rescate para descifrar. Variantes modernas: double extortion (cifra + exfiltra datos para amenazar con publicarlos). Vectores: phishing, RDP expuesto, vulnerabilidades sin parchear, drive-by download. Prevencin: backup offline + segmentacin + EDR + patch management.

**Ejemplos practicos:**

- WannaCry (2017): explot EternalBlue (SMBv1)  cifr 200k+ equipos globalmente
- REvil: ransomware-as-a-service  ataque a Kaseya VSA  afect 1500 empresas
- Prevencin: backup 3-2-1 (3 copias, 2 medios, 1 offsite) + air gap

**Conceptos relacionados:** Backup, EDR, Network_Segmentation, Patch_Management

**Errores comunes:**

- Backup conectado a la red = ransomware tambin lo cifra
- Pagar rescate  garanta de recuperacin (70% no recupera todo)

---

#### Trojan

**Prioridad:** ALTA

**Definicion base:** Malware disfrazado de software legítimo. NO se auto-replica. Puerta trasera para el atacante

---

#### RAT

**Prioridad:** ALTA

**Definicion base:** Troyano que permite control remoto completo del sistema comprometido. Acceso backdoor persistente

---

#### Worm

**Prioridad:** ALTA

**Definicion base:** Malware autorreplicante. Se propaga automaticamente por red sin intervencion humana. Consume recursos de red

---

#### Botnet

**Prioridad:** ALTA

**Definicion base:** Red de equipos infectados (zombies) controlados remotamente. Usada para DDoS, spam, cryptomining. Comando y control (C2)

---

#### C2

**Prioridad:** ALTA

**Definicion base:** Servidor que controla malware/bots remotamente. Envía comandos y recibe datos robados

---

#### SQL_Injection

**Prioridad:** ALTA

**Definicion base:** Vulnerabilidad que permite inyectar código SQL malicioso en queries. Compromete base de datos

---

#### XSS

**Prioridad:** ALTA

**Definicion base:** Inyeccion de script malicioso en sitio web confiable. Browser del usuario ejecuta script del atacante. Roba cookies/sesiones

---

#### CSRF

**Prioridad:** ALTA

**Definicion base:** Ataque que engaña a usuario para ejecutar acciones no deseadas en sitio donde esta autenticado. Explota confianza del sitio en navegador

---

#### RCE

**Prioridad:** ALTA

**Definicion base:** Vulnerabilidad que permite ejecutar código arbitrario en sistema remoto. Muy crítica (CVSS 9-10)

---

#### XML_Injection

**Prioridad:** ALTA

**Definicion base:** Inyeccion de codigo XML malicioso. Manipula parseo de XML. XXE (External Entity) para leer archivos. Ataque a aplicaciones que procesan XML

---

#### Directory_Traversal

**Prioridad:** ALTA

**Definicion base:** Ataque que accede a archivos fuera de directorio web. Usa secuencias "../" para subir directorios. Lectura de archivos sensibles del sistema

---

#### Zero_Day

**Prioridad:** ALTA

**Definicion base:** Vulnerabilidad desconocida por el fabricante. No existe parche. Ventana de 0 días para defenderse

---

#### DoS

**Prioridad:** ALTA

**Definicion base:** Ataque que satura un servicio para hacerlo inaccesible. Desde una sola fuente

---

#### DDoS

**Prioridad:** ALTA

**Definicion base:** Ataque desde múltiples fuentes (botnet) para saturar un servicio y hacerlo inaccesible. Versión distribuida del DoS

---

#### Reflected_DDoS

**Prioridad:** ALTA

**Definicion base:** Ataque DDoS que usa servidores intermedios para amplificar trafico. Falsifica IP origen (spoofing). Servidores reflejan respuestas a victima

---

#### DNS_Spoofing

**Prioridad:** ALTA

**Definicion base:** Proporcionar información DNS falsa al resolver para redirigir tráfico a servidor malicioso

---

#### MitM

**Prioridad:** ALTA

**Definicion base:** Atacante se interpone entre dos partes que se comunican para interceptar/modificar tráfico. También llamado On-Path attack

---

#### Session_Hijacking

**Prioridad:** ALTA

**Definicion base:** Robo de Session ID válido para suplantar usuario autenticado. NO requiere credenciales

---

#### Brute_Force

**Prioridad:** ALTA

**Definicion base:** Ataque que prueba TODAS las combinaciones posibles de contraseñas hasta encontrar la correcta. Alto uso de recursos

---

#### Dictionary_Attack

**Prioridad:** ALTA

**Definicion base:** Ataque que prueba contraseñas desde lista predefinida (diccionario) de passwords comunes. Más rápido que brute force

---

#### Password_Spraying

**Prioridad:** ALTA

**Definicion base:** Probar POCAS contraseñas comunes contra MUCHAS cuentas. Evita lockout de cuenta individual

---

#### Privilege_Escalation

**Prioridad:** ALTA

**Definicion base:** Obtener permisos superiores a los asignados inicialmente. Vertical (usuario → admin) u horizontal (usuario → otro usuario)

---

#### CVE

**Prioridad:** ALTA

**Definicion base:** Sistema de identificacion unica de vulnerabilidades. Formato: CVE-YEAR-NUMBER. Mantenido por MITRE

---

#### CVSS

**Prioridad:** ALTA

**Definicion base:** Sistema de puntuación de gravedad de vulnerabilidades. Escala 0.0-10.0. Crítico (9.0-10.0), Alto (7.0-8.9), Medio (4.0-6.9), Bajo (0.1-3.9)

---

#### IoC

**Prioridad:** ALTA

**Definicion base:** Evidencia forense que indica posible intrusión o actividad maliciosa. Hashes, IPs, dominios, patrones de comportamiento

---

#### Input_Validation

**Prioridad:** ALTA

**Definicion base:** Validar toda entrada de usuario antes de procesarla. Previene injection, XSS, buffer overflow. Whitelist mejor que blacklist

---

#### Error_Handling

**Prioridad:** ALTA

**Definicion base:** Manejo seguro de errores sin revelar informacion sensible. Mensajes genericos al usuario, detalles solo en logs internos

---

#### Data_Sanitization

**Prioridad:** ALTA

**Definicion base:** Eliminar/sobrescribir datos de forma permanente. Metodos: Overwriting, Degaussing, Destruccion fisica, Crypto-shredding

---

#### False_Negative

**Prioridad:** ALTA

**Definicion base:** Sistema de seguridad NO detecta amenaza real. Falso sentido de seguridad. MAS PELIGROSO que falso positivo

---

#### False_Positive

**Prioridad:** ALTA

**Definicion base:** Sistema de seguridad alerta sobre actividad normal como amenaza. Genera fatiga de alertas y reduce eficiencia

---

#### MITRE_ATT&CK

**Prioridad:** ALTA

**Definicion base:** Framework de tacticas y tecnicas de adversarios. Base de conocimiento de comportamiento de atacantes. Matriz de TTPs

---

#### Attack_Surface

**Prioridad:** ALTA

**Definicion base:** Suma de todos los puntos de vulnerabilidad donde atacante puede interactuar/comprometer sistema. Mayor superficie = mayor riesgo

---

#### Threat_Vector

**Prioridad:** ALTA

**Definicion base:** Metodo/ruta que atacante usa para introducir amenaza. Email, malware, drive-by download, ingenieria social

---

#### SQLi

**Prioridad:** ALTA

**Definicion base:** Inyeccion de codigo SQL malicioso en campos de entrada para ejecutar comandos no autorizados en base de datos

---

#### Memory_Injection

**Prioridad:** ALTA

**Definicion base:** Introducir codigo externo en espacio de memoria de proceso en ejecucion. Tecnica de evasion de AV

---

#### Malicious_Update

**Prioridad:** ALTA

**Definicion base:** Malware instalado via actualizacion falsa de software. Vector: codigo sin firmar, canal HTTP, servidor comprometido, supply chain attack

---

#### Legacy_Hardware_Vulnerability

**Prioridad:** ALTA

**Definicion base:** Vulnerabilidad principal: falta de actualizaciones de seguridad y parches. Hardware obsoleto sin soporte

---

#### VM_Escape

**Prioridad:** ALTA

**Definicion base:** Vulnerabilidad de virtualizacion donde activos de una VM acceden/comprometen otra VM. Rompe aislamiento entre VMs

---

#### Wireless_Disassociation

**Prioridad:** ALTA

**Definicion base:** Ataque que envia frames de desasociacion falsos. Desconecta clientes de AP. Tipo de DoS inalambrico. Frames de gestion no autenticados

---

#### Session_Replay

**Prioridad:** ALTA

**Definicion base:** Ataque que captura y reenvía sesion valida. Intercepta trafico autenticado. Replay de tokens o cookies de sesion. Bypass de autenticacion

---


### Arquitectura de Seguridad (18%)

**Terminos ALTA:** 60

#### Firewall

**Prioridad:** ALTA

**Definicion base:** Dispositivo o software que filtra tráfico de red según reglas. Tipos: filtrado de paquetes, stateful, capa de aplicación (L7), NGFW

---

#### Layer_7_Firewall

**Prioridad:** ALTA

**Definicion base:** Firewall que inspecciona capa de aplicacion OSI. Analiza contenido payload (no solo headers). Filtrado profundo pero mas lento

---

#### WAF

**Prioridad:** ALTA

**Definicion base:** Firewall específico para proteger aplicaciones web. Filtra tráfico HTTP/HTTPS. Protege contra SQLi, XSS, CSRF

---

#### IDS

**Prioridad:** ALTA

**Definicion base:** Sistema que DETECTA intrusiones pero NO bloquea. Genera alertas. Tipos: NIDS (red), HIDS (host)

---

#### NIDS

**Prioridad:** ALTA

**Definicion base:** Sistema de deteccion de intrusiones a nivel de red. Monitorea trafico sin bloquearlo. Modo pasivo. Genera alertas

---

#### IPS

**Prioridad:** ALTA

**Definicion base:** Sistema que DETECTA Y BLOQUEA intrusiones en línea (inline). IDS + prevención activa

---

#### HIPS

**Prioridad:** ALTA

**Definicion base:** IPS instalado en host individual. Monitorea y bloquea actividad maliciosa en sistema. Respuesta activa a amenazas locales

---

#### NIPS

**Prioridad:** ALTA

**Definicion base:** Sistema de prevencion de intrusiones a nivel de red. Modo inline - puede bloquear trafico. Accion proactiva

---

#### VPN

**Prioridad:** ALTA

**Definicion base:** Túnel cifrado sobre red pública. Conecta sitios remotos o usuarios de forma segura. Protocolos: IPSec, SSL/TLS, WireGuard

**Explicacion detallada:**

Virtual Private Network: tnel cifrado sobre internet para conectar recursos remotos de forma segura. Tipos: Site-to-Site (conecta dos redes, gateway-a-gateway), Remote Access (usuario remoto a red corporativa), SSL/TLS VPN (navegador), IPsec VPN (cliente). Protocolos: IPsec, IKEv2, OpenVPN, WireGuard.

**Ejemplos practicos:**

- Remote access: empleado desde casa usa VPN client  IPsec tunnel  accede recursos corporativos
- Site-to-site: oficina Madrid - oficina Barcelona  tnel permanente IPsec
- Split tunnel: solo trfico corporativo va por VPN, Netflix va directo (ahorra ancho de banda)

**Conceptos relacionados:** IPsec, TLS, Authentication, Encryption, Zero_Trust

**Errores comunes:**

- VPN sin MFA = compromiso de credenciales  acceso total a red
- Full tunnel en remoto = lentitud innecesaria (usar split tunnel inteligente)

---

#### Site_to_Site_VPN

**Prioridad:** ALTA

**Definicion base:** VPN que conecta dos redes completas. Tipicamente entre oficinas. Gateway VPN en cada lado. IPsec comun. Always-on

---

#### SASE

**Prioridad:** ALTA

**Definicion base:** Framework Gartner. Red + seguridad en servicio cloud unico. SD-WAN + CASB + FWaaS + ZTNA + SWG. Cloud-native

---

#### SDN

**Prioridad:** ALTA

**Definicion base:** Red definida por software. Separa plano de control de plano de datos. Gestion centralizada via controlador. Programable y flexible

---

#### VLAN

**Prioridad:** ALTA

**Definicion base:** Segmentacion logica de red. Divide red fisica en multiples redes virtuales. Aislamiento de broadcast. Seguridad por segmentacion

---

#### DMZ

**Prioridad:** ALTA

**Definicion base:** Segmento de red aislado entre Internet y red interna. Aloja servicios públicos (web, email) accesibles desde exterior

**Explicacion detallada:**

Demilitarized Zone: red perimetral semi-segura entre internet y red interna. Contiene servicios pblicos (web, mail, DNS). Arquitectura tpica: firewall externo (internet-DMZ) + firewall interno (DMZ-LAN). Reglas: internet  DMZ (permitir solo puertos pblicos), DMZ  LAN (muy restrictivo), LAN  DMZ (monitoreo).

**Ejemplos practicos:**

- Web server en DMZ: internet accede puerto 443, DMZ accede DB interno puerto 3306
- Mail server en DMZ: recibe SMTP (25) desde internet, reenva a Exchange interno
- Doble firewall: Cisco ASA externo + Palo Alto interno con IPS

**Conceptos relacionados:** Firewall, Network_Segmentation, IDS_IPS, Defense_in_Depth

**Errores comunes:**

- DMZ con acceso directo a LAN = anula el propsito
- No segmentar DMZ: compromiso de web  acceso a mail server

---

#### ACL

**Prioridad:** ALTA

**Definicion base:** Lista de reglas de control de acceso. Filtra trafico por IP, puerto, protocolo. Implementada en routers, switches, firewalls

---

#### IEEE_802_1X

**Prioridad:** ALTA

**Definicion base:** Estandar de control de acceso de red basado en puerto. Autenticacion antes de acceso a red. Usa EAP. Supplicant-Authenticator-Auth Server

---

#### Proxy

**Prioridad:** ALTA

**Definicion base:** Intermediario entre cliente e Internet. Filtra, cachea y anonimiza trafico. Forward o reverse proxy. Control y seguridad

---

#### RAS

**Prioridad:** ALTA

**Definicion base:** Servicio que proporciona acceso remoto seguro a red. VPN, dial-up, terminal services. Permite trabajo remoto

---

#### Air_Gap

**Prioridad:** ALTA

**Definicion base:** Aislamiento fisico completo de red. Sistema sin conexion a redes externas. Maxima seguridad por separacion fisica

---

#### SIEM

**Prioridad:** ALTA

**Definicion base:** Plataforma centralizada que recopila, correlaciona y analiza logs de múltiples fuentes. Genera alertas de seguridad

---

#### EDR

**Prioridad:** ALTA

**Definicion base:** Solución que detecta amenazas en endpoints por comportamiento. Permite investigación forense y respuesta remota

---

#### NGFW

**Prioridad:** ALTA

**Definicion base:** Firewall avanzado con deep packet inspection, IPS, application awareness, threat intelligence integrada

---

#### DLP

**Prioridad:** ALTA

**Definicion base:** Sistema que detecta y previene exfiltración/fuga de datos sensibles. Monitoriza datos en reposo, uso y tránsito

---

#### RTO

**Prioridad:** ALTA

**Definicion base:** Tiempo máximo aceptable de inactividad de un sistema tras un desastre. Cuánto tiempo puede estar caído

---

#### RPO

**Prioridad:** ALTA

**Definicion base:** Cantidad máxima aceptable de pérdida de datos medida en tiempo. Cuánto dato puedes perder

---

#### Backup_3_2_1

**Prioridad:** ALTA

**Definicion base:** 3 copias de datos, en 2 tipos de medios diferentes, 1 copia offsite (fuera del sitio)

---

#### Snapshot

**Prioridad:** ALTA

**Definicion base:** Captura punto-en-tiempo de VM o volumen. Estado completo en momento especifico. Rollback rapido. NO es backup completo a largo plazo

---

#### Replication

**Prioridad:** ALTA

**Definicion base:** Copia continua de datos a ubicacion secundaria. Sincrona (RPO=0) o asincrona (RPO>0). Alta disponibilidad y DR

---

#### Load_Balancing

**Prioridad:** ALTA

**Definicion base:** Distribución de carga de trabajo entre múltiples servidores para mejorar rendimiento y disponibilidad

---

#### Hot_Site

**Prioridad:** ALTA

**Definicion base:** Centro de datos de backup completamente operacional con replicación en tiempo real. RTO/RPO mínimos (minutos). MUY costoso

---

#### Warm_Site

**Prioridad:** ALTA

**Definicion base:** Sitio DR con infraestructura basica. Equipos instalados pero no completamente configurados. RTO medio (horas/dias). Balance costo/tiempo

---

#### Cold_Site

**Prioridad:** ALTA

**Definicion base:** Sitio DR solo con espacio fisico y servicios basicos. Sin equipos preinstalados. RTO largo (dias/semanas). Opcion mas economica

---

#### UPS

**Prioridad:** ALTA

**Definicion base:** Sistema de alimentación ininterrumpida. Batería que proporciona energía temporal durante corte eléctrico

---

#### Cloud_IaaS

**Prioridad:** ALTA

**Definicion base:** Modelo cloud que proporciona infraestructura virtualizada. Usuario gestiona OS, aplicaciones. Proveedor gestiona hardware

---

#### Cloud_SaaS

**Prioridad:** ALTA

**Definicion base:** Aplicación completa en cloud. Usuario solo consume el servicio. Proveedor gestiona todo

---

#### Screened_Subnet

**Prioridad:** ALTA

**Definicion base:** Subred ligeramente protegida entre Internet y red interna. Servidores publicos en DMZ. Doble firewall tipico. Buffer zone de seguridad

---

#### Firewall_Implicit_Deny

**Prioridad:** ALTA

**Definicion base:** Regla por defecto: denegar todo trafico no explicitamente permitido. Ultima regla implicita en ACLs

---

#### URL_Scanning

**Prioridad:** ALTA

**Definicion base:** Analisis de URLs en tiempo real para detectar phishing, malware, sitios maliciosos. Reputacion de dominios

---

#### DNS_Filtering

**Prioridad:** ALTA

**Definicion base:** Bloquear resoluciones DNS de dominios maliciosos. Previene acceso a phishing, malware, C&C. Nivel de red

---

#### Group_Policy

**Prioridad:** ALTA

**Definicion base:** Configuracion centralizada en Active Directory para controlar usuarios/computadoras Windows. Politicas de seguridad, software, scripts

---

#### FIM

**Prioridad:** ALTA

**Definicion base:** Monitoreo de cambios en archivos criticos. Detecta modificaciones no autorizadas. Hash baseline + comparacion. Alerta cambios sospechosos

---

#### MAC_Model

**Prioridad:** ALTA

**Definicion base:** Control de acceso basado en clasificacion de seguridad. Sistema operativo impone politicas. Usuario NO puede modificar permisos

---

#### PEAP

**Prioridad:** ALTA

**Definicion base:** Protocolo de autenticacion 802.1X. Crea tunel TLS antes de autenticar. Protege credenciales. EAP dentro de TLS

---

#### EAP_TLS

**Prioridad:** ALTA

**Definicion base:** EAP Transport Layer Security. Metodo mas seguro 802.1X. Requiere certificados en cliente Y servidor. Mutual authentication

---

#### WPA_Enterprise

**Prioridad:** ALTA

**Definicion base:** WPA/WPA2/WPA3 con autenticacion 802.1X. Servidor RADIUS. Credenciales individuales por usuario. Para empresas

---

#### DAC

**Prioridad:** ALTA

**Definicion base:** Control de acceso discrecional. Propietario del recurso decide permisos. Usuarios pueden compartir recursos. Menos restrictivo

---

#### Least_Privilege

**Prioridad:** ALTA

**Definicion base:** Principio de minimo privilegio. Usuarios/procesos solo acceso necesario para tarea. Reduce superficie de ataque. Best practice seguridad

---

#### Adaptive_Identity

**Prioridad:** ALTA

**Definicion base:** Control de acceso Zero Trust dinamico. Considera contexto: identidad, dispositivo, ubicacion, comportamiento. Decisiones de acceso en tiempo real

---

#### IPsec

**Prioridad:** ALTA

**Definicion base:** Suite de protocolos para seguridad IP. Cifrado, autenticacion e integridad. VPNs site-to-site. Layer 3 del modelo OSI

---

#### PSK

**Prioridad:** ALTA

**Definicion base:** Clave secreta compartida previamente entre partes. Usado en WPA/WPA2-Personal. Autenticacion simetrica. Mas simple que 802.1X

---

#### GDPR

**Prioridad:** ALTA

**Definicion base:** Reglamento UE de proteccion de datos personales. Derecho privacidad ciudadanos UE. Multas severas por incumplimiento. RGPD en español

---

#### Secure_Baseline

**Prioridad:** ALTA

**Definicion base:** Configuracion estandar de seguridad minima. Template de hardening. Configuraciones y ajustes fundamentales. Punto de partida seguro

---

#### Remote_Wipe

**Prioridad:** ALTA

**Definicion base:** Borrado remoto de datos en dispositivo movil perdido/robado. MDM feature. Protege datos corporativos. Factory reset remoto

---

#### Data_Retention_Policy

**Prioridad:** ALTA

**Definicion base:** Politica que especifica cuanto tiempo retener datos antes de eliminarlos. Requisitos legales y compliance. Ciclo de vida de datos

---

#### STARTTLS

**Prioridad:** ALTA

**Definicion base:** Comando para upgradear conexion plaintext a TLS. Usado en SMTP, IMAP, POP3. Explicit TLS. Puerto estandar + upgrade

---

#### SOW

**Prioridad:** ALTA

**Definicion base:** Declaracion de trabajo detallada. Describe trabajo a realizar en proyecto. Alcance, entregables, timeline, costo

---

#### CCMP

**Prioridad:** ALTA

**Definicion base:** Protocolo cifrado WPA2/WPA3. Basado en AES. Reemplazo de TKIP. Modo contador + autenticacion CBC-MAC

---

#### CBC_Mode

**Prioridad:** ALTA

**Definicion base:** Modo cifrado de bloques. Cada bloque XOR con anterior. IV para primer bloque. Popular pero vulnerable a padding oracle

---

#### ECB_Mode

**Prioridad:** ALTA

**Definicion base:** Modo cifrado de bloques MAS DEBIL. Cada bloque cifrado independiente. Patrones visibles. NO USAR

---

#### AUP

**Prioridad:** ALTA

**Definicion base:** Politica de uso aceptable. Reglas de comportamiento para usuarios de sistemas IT. Que esta permitido/prohibido

---


### Operaciones de Seguridad (28%)

**Terminos ALTA:** 34

#### Static_Code_Analysis

**Prioridad:** ALTA

**Definicion base:** Analisis de codigo fuente sin ejecutarlo. Busca bugs, vulnerabilidades, code smells. SAST. Parte de DevSecOps

---

#### Dynamic_Code_Analysis

**Prioridad:** ALTA

**Definicion base:** Analisis de aplicacion en EJECUCION. Detecta vulnerabilidades en runtime. Parte de DAST

---

#### Package_Monitoring

**Prioridad:** ALTA

**Definicion base:** Monitoreo de dependencias de software (bibliotecas, frameworks). Detecta vulnerabilidades conocidas en paquetes terceros

---

#### DLP

**Prioridad:** ALTA

**Definicion base:** Tecnologia para prevenir fuga de datos sensibles. Monitorea, detecta, bloquea transferencias no autorizadas. Network-based, Endpoint-based, Cloud-based

---

#### Signatures

**Prioridad:** ALTA

**Definicion base:** Patrones conocidos de malware/ataques. Usados por antivirus, IDS/IPS. Requiere actualizacion constante. Inefectivo contra zero-day

---

#### Orchestration

**Prioridad:** ALTA

**Definicion base:** Coordinacion y gestion automatizada de multiples tareas y sistemas. Workflow automation complejo. Mas avanzado que automatizacion simple

---

#### Automation

**Prioridad:** ALTA

**Definicion base:** Automatizacion de tareas repetitivas de seguridad. Scripts, runbooks, respuestas automaticas. Reduce tiempo de respuesta

---

#### PCAP

**Prioridad:** ALTA

**Definicion base:** Captura de paquetes de red para analisis. Formato de archivo .pcap. Wireshark, tcpdump. Analisis trafico y troubleshooting

---

#### Vulnerability_Scanning

**Prioridad:** ALTA

**Definicion base:** Escaneo automatizado de vulnerabilidades. Identifica debilidades de seguridad. Nessus, Qualys, OpenVAS

---

#### SASE

**Prioridad:** ALTA

**Definicion base:** Framework cloud que combina funciones de red (SD-WAN) y seguridad (SWG, CASB, FWaaS, ZTNA) en servicio unico

---

#### AUP

**Prioridad:** ALTA

**Definicion base:** Politica que define uso aceptable de recursos IT de organizacion. Control directivo que guia comportamiento de usuarios

---

#### Red_Team

**Prioridad:** ALTA

**Definicion base:** Equipo que simula atacantes reales. Pentest ofensivo y realista. Prueba controles de seguridad. Tacticas adversarias

---

#### Blue_Team

**Prioridad:** ALTA

**Definicion base:** Equipo de defensa. Detecta y responde a ataques. Monitoriza logs y alertas. Defiende contra Red Team

---

#### Gray_Box_Testing

**Prioridad:** ALTA

**Definicion base:** Pentest con conocimiento parcial. Informacion limitada del sistema. Mezcla de black-box y white-box. Mas realista que white-box

---

#### Active_Reconnaissance

**Prioridad:** ALTA

**Definicion base:** Reconocimiento activo. Interaccion directa con objetivo. Genera trafico detectable. Escaneos, sondeos

---

#### Passive_Reconnaissance

**Prioridad:** ALTA

**Definicion base:** Reconocimiento pasivo. Sin contacto directo con objetivo. Recopilacion de info publica. No genera alertas

---

#### Fuzzing

**Prioridad:** ALTA

**Definicion base:** Tecnica de testing automatizada. Envia inputs invalidos/aleatorios/inesperados. Busca crashes o comportamiento anormal. Encuentra vulnerabilidades

---

#### Code_Signing

**Prioridad:** ALTA

**Definicion base:** Firma digital de codigo/software. Verifica autenticidad y integridad. Certificado del desarrollador. Previene modificacion maliciosa

---

#### Impossible_Travel

**Prioridad:** ALTA

**Definicion base:** Indicador de compromiso. Login desde ubicaciones geograficamente imposibles en tiempo corto. Usuario en Madrid y luego 1h despues en Tokio

---

#### Missing_Logs

**Prioridad:** ALTA

**Definicion base:** Indicador de compromiso. Ausencia o borrado de logs. Atacantes eliminan evidencia. Gap en logs de auditoria

---

#### Incident_Response_Preparation

**Prioridad:** ALTA

**Definicion base:** Primera fase de IR. Preparacion previa a incidentes. Crear plan IR, entrenar equipo, herramientas listas. Proactividad

---

#### Incident_Response_Detection

**Prioridad:** ALTA

**Definicion base:** Segunda fase de IR. Detectar e identificar incidentes. Analizar alcance, impacto y causa raiz. Determinar severidad

---

#### Incident_Response_Containment

**Prioridad:** ALTA

**Definicion base:** Tercera fase de IR. Contener amenaza, erradicar malware, recuperar sistemas. Limitar daño y restaurar operaciones

---

#### Incident_Response_Post_Incident

**Prioridad:** ALTA

**Definicion base:** Cuarta fase de IR. Actividades tras incidente. Lessons learned, actualizar procedimientos, mejorar defensas. Documentacion

---

#### SDLC

**Prioridad:** ALTA

**Definicion base:** Proceso de creacion y mantenimiento de software. Fases: Planificacion, Analisis, Diseño, Implementacion, Testing, Deploy, Mantenimiento

---

#### IoC

**Prioridad:** ALTA

**Definicion base:** Evidencia forense de actividad maliciosa. Artefactos que indican breach o compromiso. Hash malware, IP C2, dominios maliciosos

---

#### MDM

**Prioridad:** ALTA

**Definicion base:** Gestion centralizada de dispositivos moviles. Control configuracion, seguridad, apps. Remote wipe. Enforce policies

---

#### CVE

**Prioridad:** ALTA

**Definicion base:** Sistema de identificacion de vulnerabilidades publicas. ID unico CVE-YEAR-NUMBER. MITRE mantiene base de datos. Referencia estandar

---

#### DKIM

**Prioridad:** ALTA

**Definicion base:** Autenticacion de email mediante firma digital. Verifica remitente y integridad mensaje. Clave privada firma, publica en DNS verifica

---

#### DMARC

**Prioridad:** ALTA

**Definicion base:** Politica que especifica como manejar emails que fallan SPF/DKIM. Quarantine, Reject o None. Reportes de compliance

---

#### OpenID_Connect

**Prioridad:** ALTA

**Definicion base:** Capa de autenticacion sobre OAuth 2.0. Verifica identidad usuario. ID Token (JWT). SSO moderno para web/mobile

---

#### Biometrics

**Prioridad:** ALTA

**Definicion base:** Autenticacion mediante caracteristicas biologicas o comportamentales. Huella, facial, iris, voz. Algo que eres

---

#### Security_Key

**Prioridad:** ALTA

**Definicion base:** Token hardware de autenticacion. USB/NFC. FIDO2/U2F. Phishing-resistant MFA. Dispositivo fisico para 2FA

---

#### IRP

**Prioridad:** ALTA

**Definicion base:** Plan documentado de respuesta a incidentes. Describe pasos en cada fase. Roles, responsabilidades, procedimientos. Playbooks

---


### Gestin del Programa de Seguridad (20%)

**Terminos ALTA:** 32

#### BCP

**Prioridad:** ALTA

**Definicion base:** Plan para mantener operaciones criticas durante/despues de desastre. Estrategias de continuidad de negocio

---

#### DRP

**Prioridad:** ALTA

**Definicion base:** Plan para recuperar sistemas IT despues de desastre. Subset de BCP enfocado en tecnologia. RTO/RPO objectives

---

#### IRP

**Prioridad:** ALTA

**Definicion base:** Plan documentado para responder a incidentes de seguridad. Define roles, procedimientos, comunicacion, escalacion

---

#### Incident_Response_Stages

**Prioridad:** ALTA

**Definicion base:** Preparacion → Deteccion/Analisis → Contencion → Erradicacion → Recuperacion → Lecciones Aprendidas (NIST 800-61)

---

#### NTP

**Prioridad:** ALTA

**Definicion base:** Protocolo sincronizacion de relojes en red. UDP puerto 123. Critico para logs, Kerberos, certificados

---

#### ICMP

**Prioridad:** ALTA

**Definicion base:** Protocolo mensajes de error y control IP. Ping, traceroute. Usado para diagnostico red. Puede ser abusado

---

#### BYOD

**Prioridad:** ALTA

**Definicion base:** Modelo donde empleados usan dispositivos personales para trabajo. Riesgos seguridad. Require MDM, policies

---

#### UEM

**Prioridad:** ALTA

**Definicion base:** Gestion unificada de todos endpoints. Moviles, PCs, tablets, IoT, wearables. Evolucion de MDM + EMM

---

#### Risk_Exception

**Prioridad:** ALTA

**Definicion base:** Aprobacion formal para NO remediar riesgo identificado. Decision de negocio. Acepta riesgo temporalmente con justificacion. Requiere autorizacion senior

---

#### Risk_Mitigation

**Prioridad:** ALTA

**Definicion base:** Reducir probabilidad o impacto de riesgo. Implementar controles de seguridad. Estrategia mas comun. No elimina riesgo completamente

---

#### MTTR

**Prioridad:** ALTA

**Definicion base:** Tiempo promedio para reparar sistema tras fallo. Metrica de disponibilidad. Incluye deteccion + resolucion. Menor MTTR = mejor

---

#### MTBF

**Prioridad:** ALTA

**Definicion base:** Tiempo promedio entre fallos de sistema. Metrica de fiabilidad. Mayor MTBF = mas confiable. Predice disponibilidad

---

#### RPO

**Prioridad:** ALTA

**Definicion base:** Maxima perdida de datos aceptable. Medido en tiempo. Frecuencia minima de backups. RPO 1 hora = backup cada hora

---

#### RTO

**Prioridad:** ALTA

**Definicion base:** Tiempo maximo aceptable para restaurar servicio. Downtime maximo tolerable. Define urgencia de recuperacion. Menor RTO = mayor costo

---

#### Risk_Transference

**Prioridad:** ALTA

**Definicion base:** Transferir riesgo a tercero. Tipicamente via seguro o contrato. Compartir impacto financiero. No elimina riesgo tecnico

---

#### SLA

**Prioridad:** ALTA

**Definicion base:** Acuerdo formal de nivel de servicio. Define expectativas y metricas. Uptime, tiempo de respuesta. Penalizaciones por incumplimiento

---

#### Tabletop_Exercise

**Prioridad:** ALTA

**Definicion base:** Ejercicio de simulacion de incidente basado en discusion. Participantes discuten respuesta a escenario. Sin ejecucion tecnica. Training de IR

---

#### Root_Cause_Analysis

**Prioridad:** ALTA

**Definicion base:** Analisis de causa raiz. Investigacion profunda de incidente. Identifica causa fundamental (no sintomas). Previene recurrencia

---

#### Chain_of_Custody

**Prioridad:** ALTA

**Definicion base:** Cadena de custodia de evidencia digital. Documentacion de quien manejo evidencia y cuando. Preserva integridad legal. Forense

---

#### RAID_0

**Prioridad:** ALTA

**Definicion base:** Disk Striping sin redundancia. Datos distribuidos en multiples discos. Mayor rendimiento. SIN tolerancia a fallos. Fallo de 1 disco = perdida total

---

#### RAID_5

**Prioridad:** ALTA

**Definicion base:** Disk Striping con paridad distribuida. Tolera fallo de 1 disco. Buen balance rendimiento/redundancia. Minimo 3 discos

---

#### RAID_10

**Prioridad:** ALTA

**Definicion base:** RAID 1+0. Combinacion de mirroring y striping. Mirrors primero, luego stripes. Alta redundancia y rendimiento. Minimo 4 discos

---

#### Hot_Site

**Prioridad:** ALTA

**Definicion base:** Sitio DR completamente equipado y operacional. Replica exacta de produccion. RTO minimo (minutos/horas). Costo mas alto

---

#### Warm_Site

**Prioridad:** ALTA

**Definicion base:** Sitio DR parcialmente equipado. Infraestructura basica disponible. Requiere configuracion y datos. RTO medio (horas/dias). Costo moderado

---

#### Cold_Site

**Prioridad:** ALTA

**Definicion base:** Sitio DR solo con espacio fisico y servicios basicos. Sin equipos preinstalados. RTO largo (dias/semanas). Menor costo

---

#### Snapshot

**Prioridad:** ALTA

**Definicion base:** Imagen punto-en-tiempo de sistema/datos. Captura estado instantaneo. Restauracion rapida. NO reemplaza backup completo

---

#### Replication

**Prioridad:** ALTA

**Definicion base:** Copia continua de datos a ubicacion secundaria. Sincrona o asincrona. Alta disponibilidad. Parte de estrategia DR

---

#### Risk_Register

**Prioridad:** ALTA

**Definicion base:** Documento que identifica, evalua y rastrea riesgos. Lista completa de riesgos con: descripcion, probabilidad, impacto, mitigacion

---

#### PCI_DSS

**Prioridad:** ALTA

**Definicion base:** Estandar de seguridad para industria de pagos. Protege datos de tarjetas. 12 requisitos. Obligatorio para procesadores de tarjetas

---

#### ISO

**Prioridad:** ALTA

**Definicion base:** Organizacion internacional de estandarizacion. Desarrolla estandares globales. ISO 27001 (seguridad info), ISO 9001 (calidad)

---

#### CSP

**Prioridad:** ALTA

**Definicion base:** Proveedor servicios cloud. Ofrece IaaS, PaaS, SaaS via Internet. AWS, Azure, GCP

---

#### SNMP

**Prioridad:** ALTA

**Definicion base:** Protocolo gestion y monitoreo dispositivos de red. Colecta metricas. UDP 161/162. SNMPv3 seguro

---


## Mapas Conceptuales

### Criptografa y PKI End-to-End

Flujo completo desde generacin de claves hasta uso de certificados

**Nodos:**

- **Criptografa Asimtrica** (concepto_base)
- **Key Pair (pblica + privada)** (componente)
- **Certificate Authority (CA)** (componente)
- **Certificate Signing Request** (proceso)
- **Certificado Digital X.509** (componente)
- **TLS/HTTPS** (uso)
- **Revocacin (CRL/OCSP)** (proceso)

**Relaciones:**

- asymmetric -> key_pair: genera
- key_pair -> csr: se incluye en
- csr -> ca: se enva a
- ca -> certificate: firma y emite
- certificate -> tls: se usa en
- ca -> revocation: publica lista de

---

### Email Security - Defensa en Capas

Cmo SPF, DKIM y DMARC trabajan juntos

**Nodos:**

- **Amenaza: Phishing/Spoofing** (amenaza)
- **SPF (Sender Policy Framework)** (control)
- **DKIM (DomainKeys Identified Mail)** (control)
- **DMARC (Domain-based Message Auth)** (control)
- **Email Gateway/Filter** (control)
- **Security Awareness Training** (control)

**Relaciones:**

- email_threat -> spf: mitigado por
- email_threat -> dkim: mitigado por
- spf -> dmarc: verificado por
- dkim -> dmarc: verificado por
- dmarc -> email_gateway: informa decisin a
- email_gateway -> user_training: complementado con

---

### Incident Response - Ciclo Completo

Fases del incident response segn NIST

**Nodos:**

- **1. Preparation** (fase)
- **2. Detection & Analysis** (fase)
- **3. Containment** (fase)
- **4. Eradication** (fase)
- **5. Recovery** (fase)
- **6. Post-Incident** (fase)

**Relaciones:**

- preparation -> detection: permite
- detection -> containment: activa
- containment -> eradication: seguido de
- eradication -> recovery: seguido de
- recovery -> post_incident: concluye con
- post_incident -> preparation: mejora continua

---

### Zero Trust Architecture

Componentes y principios de Zero Trust

**Nodos:**

- **Principio: Never Trust, Always Verify** (principio)
- **Identity Verification (MFA, Adaptive Auth)** (componente)
- **Device Posture Check (NAC, EDR)** (componente)
- **Microsegmentation** (componente)
- **Least Privilege Access (JIT, JEA)** (componente)
- **Continuous Monitoring (SIEM, UBA)** (componente)

**Relaciones:**

- zt_principle -> identity: requiere
- zt_principle -> device: requiere
- zt_principle -> microseg: implementa
- zt_principle -> least_privilege: aplica
- zt_principle -> continuous: usa

---

### Controles de Seguridad - Clasificacin Completa

Tipos de controles: tcnicos, administrativos, fsicos / preventivos, detectivos, correctivos

**Nodos:**

- **Preventivo** (categoria)
- **Detectivo** (categoria)
- **Correctivo** (categoria)
- **Tcnico-Preventivo: Firewall, Cifrado, ACL** (control)
- **Tcnico-Detectivo: IDS, SIEM, Antivirus** (control)
- **Tcnico-Correctivo: Patch, Backup restore, IPS** (control)
- **Administrativo-Preventivo: Polticas, Training** (control)
- **Administrativo-Detectivo: Auditoras, Log review** (control)
- **Fsico-Preventivo: Guardias, Cerraduras, Vallas** (control)

**Relaciones:**

- preventive -> tech_prev: incluye
- preventive -> admin_prev: incluye
- preventive -> phys_prev: incluye
- detective -> tech_det: incluye
- detective -> admin_det: incluye
- corrective -> tech_corr: incluye

---


## PBQs Simuladas

### PBQ_01: Configurar Segmentacin de Red con DMZ

**Dominio:** Dominio 3 - Arquitectura de Seguridad  
**Dificultad:** MEDIA  
**Tiempo estimado:** 15 minutos  

**Escenario:**

Tu empresa necesita exponer un servidor web al pblico mientras protege la red interna. Tienes 2 firewalls disponibles y necesitas configurar una DMZ. La red interna es 10.0.1.0/24, la DMZ ser 192.168.100.0/24, y el servidor web es 192.168.100.10.

**Tareas:**

- Dibujar diagrama de red con: Internet - Firewall Externo - DMZ - Firewall Interno - LAN
- Configurar reglas del firewall externo
- Configurar reglas del firewall interno
- Identificar puertos necesarios

**Conceptos clave:** DMZ, Network_Segmentation, Firewall, Defense_in_Depth

---

### PBQ_02: Implementar Autenticacin 802.1X para Red Corporativa

**Dominio:** Dominio 3 - Arquitectura de Seguridad  
**Dificultad:** ALTA  
**Tiempo estimado:** 20 minutos  

**Escenario:**

La empresa quiere asegurar el acceso a la red LAN usando 802.1X. Tienes: switches con soporte 802.1X, servidor RADIUS, Active Directory, usuarios con certificados digitales. Necesitas configurar autenticacin tanto para usuarios de dominio como para dispositivos invitados.

**Tareas:**

- Seleccionar mtodo EAP apropiado para usuarios corporativos
- Configurar autenticacin para invitados
- Definir VLANs de seguridad
- Configurar fallback para dispositivos no-802.1X

**Conceptos clave:** 802.1X, RADIUS, EAP-TLS, NAC, VLAN, Microsegmentation

---

### PBQ_03: Responder a Incidente de Ransomware

**Dominio:** Dominio 4 - Operaciones de Seguridad  
**Dificultad:** ALTA  
**Tiempo estimado:** 25 minutos  

**Escenario:**

Es lunes 9:00 AM. El sistema de monitoreo alerta que 15 estaciones de trabajo muestran alta actividad de cifrado de archivos. Los usuarios reportan archivos con extensin .locked y nota de rescate exigiendo 50 BTC. Eres el incident responder. El backup ms reciente es de ayer domingo 2:00 AM.

**Tareas:**

- Ejecutar las 6 fases del incident response
- Priorizar acciones inmediatas
- Preservar evidencia para forensics
- Decidir si pagar rescate

**Conceptos clave:** Incident_Response, Ransomware, Containment, Forensics, Backup, BCP

---

### PBQ_04: Configurar SIEM para Detectar Compromiso de Credenciales

**Dominio:** Dominio 4 - Operaciones de Seguridad  
**Dificultad:** MEDIA  
**Tiempo estimado:** 20 minutos  

**Escenario:**

Tu SIEM (Splunk) recibe logs de: Active Directory, firewalls, VPN, Office 365. Necesitas crear reglas de correlacin para detectar: 1) Brute force attacks, 2) Impossible travel, 3) Privilege escalation. Define las reglas y umbrales.

**Tareas:**

- Disear regla de deteccin de brute force
- Disear regla de impossible travel
- Disear regla de privilege escalation
- Definir severidad y respuesta automatizada

**Conceptos clave:** SIEM, Correlation, Brute_Force, Lateral_Movement, SOAR, Threat_Hunting

---

### PBQ_05: Disear Poltica de Backup segn BCP/DRP

**Dominio:** Dominio 5 - Gestin del Programa de Seguridad  
**Dificultad:** MEDIA  
**Tiempo estimado:** 15 minutos  

**Escenario:**

Tu empresa tiene: 1) Base de datos de facturacin (RTO=2h, RPO=15min), 2) File server de documentos (RTO=8h, RPO=24h), 3) Email server (RTO=4h, RPO=1h). Presupuesto limitado. Disea estrategia de backup que cumpla objetivos.

**Tareas:**

- Seleccionar tipo de backup para cada sistema
- Definir frecuencia de backups
- Elegir ubicacin de almacenamiento
- Calcular ventana de recovery

**Conceptos clave:** RTO, RPO, BCP, DRP, Backup, 3-2-1_Rule, Air_Gap

---

### PBQ_06: Implementar Email Security: SPF, DKIM, DMARC

**Dominio:** Dominio 2 - Amenazas y Mitigaciones  
**Dificultad:** MEDIA  
**Tiempo estimado:** 15 minutos  

**Escenario:**

Tu empresa 'ejemplo.com' sufre ataques de email spoofing. Necesitas configurar SPF, DKIM y DMARC. Mail enviado desde: Office 365 (outlook.office365.com) y servidor marketing (mailchimp.com).

**Tareas:**

- Crear registro SPF en DNS
- Configurar DKIM
- Configurar DMARC con poltica progresiva
- Explicar cmo funciona la validacin

**Conceptos clave:** SPF, DKIM, DMARC, Email_Security, Phishing, DNS

---

### PBQ_07: Configurar MFA con Conditional Access

**Dominio:** Dominio 1  
**Dificultad:** MEDIA  

**Escenario:**

Implementar MFA en Azure AD: siempre para admins, solo fuera de oficina para usuarios normales

**Conceptos clave:** MFA, Conditional_Access, Adaptive_Identity, Azure_AD

---

### PBQ_08: Analizar Logs de Firewall para Detectar Port Scan

**Dominio:** Dominio 2  
**Dificultad:** FCIL  

**Escenario:**

Logs muestran conexiones desde misma IP a puertos 20-1000 en 2 minutos. Identificar ataque y mitigar

**Conceptos clave:** Port_Scan, Reconnaissance, IDS, Firewall

---

### PBQ_09: Configurar VPN Site-to-Site con IPsec

**Dominio:** Dominio 3  
**Dificultad:** ALTA  

**Escenario:**

Conectar oficina Madrid (10.0.1.0/24) con Barcelona (10.0.2.0/24) usando IPsec

**Conceptos clave:** IPsec, VPN, IKE, Encryption, Tunnel_Mode

---

### PBQ_10: Hardening de Servidor Linux

**Dominio:** Dominio 3  
**Dificultad:** MEDIA  

**Escenario:**

Aplicar 10 controles de hardening en Ubuntu Server: deshabilitar servicios, firewall, SSH seguro, etc

**Conceptos clave:** Hardening, Least_Privilege, SSH, iptables, SELinux

---

### PBQ_11: Anlisis de Malware con Sandbox

**Dominio:** Dominio 4  
**Dificultad:** MEDIA  

**Escenario:**

Archivo adjunto sospechoso. Usar ANY.RUN para anlisis dinmico e identificar IOCs

**Conceptos clave:** Sandbox, Malware_Analysis, IOC, Dynamic_Analysis, Threat_Intelligence

---

### PBQ_12: Crear Poltica de Contraseas Segura

**Dominio:** Dominio 1  
**Dificultad:** FCIL  

**Escenario:**

Disear poltica de contraseas que balancee seguridad y usabilidad (longitud, complejidad, rotacin)

**Conceptos clave:** Password_Policy, Authentication, NIST_Guidelines, Password_Manager

---

### PBQ_13: Configurar Certificate Pinning en App Mvil

**Dominio:** Dominio 3  
**Dificultad:** ALTA  

**Escenario:**

Prevenir MITM en app Android haciendo pinning del certificado del servidor

**Conceptos clave:** Certificate_Pinning, MITM, TLS, Mobile_Security, PKI

---

### PBQ_14: Responder a Data Breach segn GDPR

**Dominio:** Dominio 5  
**Dificultad:** ALTA  

**Escenario:**

Base de datos con 50k usuarios UE comprometida. Pasos legales en 72h

**Conceptos clave:** GDPR, Data_Breach, Incident_Response, Notification, DPA

---

### PBQ_15: Configurar WAF para Prevenir SQLi y XSS

**Dominio:** Dominio 3  
**Dificultad:** MEDIA  

**Escenario:**

Configurar reglas en AWS WAF para bloquear inyeccin SQL y XSS en aplicacin web

**Conceptos clave:** WAF, SQLi, XSS, OWASP_Top_10, Input_Validation

---

