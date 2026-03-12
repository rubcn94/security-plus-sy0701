# Mapas Conceptuales Security+ SY0-701

Visualizar en: https://mermaid.live

---

## Criptografa y PKI End-to-End

Flujo completo desde generacin de claves hasta uso de certificados

```mermaid
graph TD
    asymmetric["Criptografa Asimtrica"]
    key_pair["Key Pair (pblica + privada)"]
    ca["Certificate Authority (CA)"]
    csr["Certificate Signing Request"]
    certificate["Certificado Digital X.509"]
    tls["TLS/HTTPS"]
    revocation["Revocacin (CRL/OCSP)"]

    asymmetric -->|genera| key_pair
    key_pair -->|se incluye en| csr
    csr -->|se enva a| ca
    ca -->|firma y emite| certificate
    certificate -->|se usa en| tls
    ca -->|publica lista de| revocation
```

---

## Email Security - Defensa en Capas

Cmo SPF, DKIM y DMARC trabajan juntos

```mermaid
graph TD
    email_threat["Amenaza: Phishing/Spoofing"]
    spf["SPF (Sender Policy Framework)"]
    dkim["DKIM (DomainKeys Identified Mail)"]
    dmarc["DMARC (Domain-based Message Auth)"]
    email_gateway["Email Gateway/Filter"]
    user_training["Security Awareness Training"]

    email_threat -->|mitigado por| spf
    email_threat -->|mitigado por| dkim
    spf -->|verificado por| dmarc
    dkim -->|verificado por| dmarc
    dmarc -->|informa decisin a| email_gateway
    email_gateway -->|complementado con| user_training
```

**Notas:** SPF verifica IP del remitente. DKIM verifica firma digital. DMARC combina ambos y define poltica (reject/quarantine/none).

---

## Incident Response - Ciclo Completo

Fases del incident response segn NIST

```mermaid
graph TD
    preparation["1. Preparation"]
    detection["2. Detection & Analysis"]
    containment["3. Containment"]
    eradication["4. Eradication"]
    recovery["5. Recovery"]
    post_incident["6. Post-Incident"]

    preparation -->|permite| detection
    detection -->|activa| containment
    containment -->|seguido de| eradication
    eradication -->|seguido de| recovery
    recovery -->|concluye con| post_incident
    post_incident -->|mejora continua| preparation
```

---

## Zero Trust Architecture

Componentes y principios de Zero Trust

```mermaid
graph TD
    zt_principle["Principio: Never Trust, Always Verify"]
    identity["Identity Verification (MFA, Adaptive Auth)"]
    device["Device Posture Check (NAC, EDR)"]
    microseg["Microsegmentation"]
    least_privilege["Least Privilege Access (JIT, JEA)"]
    continuous["Continuous Monitoring (SIEM, UBA)"]

    zt_principle -->|requiere| identity
    zt_principle -->|requiere| device
    zt_principle -->|implementa| microseg
    zt_principle -->|aplica| least_privilege
    zt_principle -->|usa| continuous
```

---

## Controles de Seguridad - Clasificacin Completa

Tipos de controles: tcnicos, administrativos, fsicos / preventivos, detectivos, correctivos

```mermaid
graph TD
    preventive["Preventivo"]
    detective["Detectivo"]
    corrective["Correctivo"]
    tech_prev["Tcnico-Preventivo: Firewall, Cifrado, ACL"]
    tech_det["Tcnico-Detectivo: IDS, SIEM, Antivirus"]
    tech_corr["Tcnico-Correctivo: Patch, Backup restore, IPS"]
    admin_prev["Administrativo-Preventivo: Polticas, Training"]
    admin_det["Administrativo-Detectivo: Auditoras, Log review"]
    phys_prev["Fsico-Preventivo: Guardias, Cerraduras, Vallas"]

    preventive -->|incluye| tech_prev
    preventive -->|incluye| admin_prev
    preventive -->|incluye| phys_prev
    detective -->|incluye| tech_det
    detective -->|incluye| admin_det
    corrective -->|incluye| tech_corr
```

---

