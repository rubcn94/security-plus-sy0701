#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open(r'D:\Users\cra\Desktop\Sec+\preguntas_nuevas.json', encoding='utf-8') as f:
    existing = json.load(f)

nuevas = [
    # DRAG-AND-DROP CONVERTIDAS (2.1)
    {"objective":"2.1","source":"Extra: Threat Actor Types",
     "question":"¿Cuál de los siguientes actores usa como vector principal el acceso INTERNO a la organización?",
     "options":["Insider threat","Nation-state","Script kiddie","Hacktivista"],
     "correct_answers":["Insider threat"]},
    {"objective":"2.1","source":"Extra: Threat Actor Types",
     "question":"Un nation-state actor tiene como motivación principal:",
     "options":["Espionaje / disrupción geopolítica","Notoriedad personal","Ganancia económica directa","Protesta ideológica"],
     "correct_answers":["Espionaje / disrupción geopolítica"]},
    {"objective":"2.1","source":"Extra: Threat Actor Types",
     "question":"¿Qué nivel de sofisticación técnica caracteriza a un script kiddie?",
     "options":["Bajo — usa herramientas ya creadas por otros","Alto — desarrolla sus propios zero-days","Medio — tiene conocimientos básicos de programación","Muy alto — respaldado por un Estado"],
     "correct_answers":["Bajo — usa herramientas ya creadas por otros"]},
    {"objective":"2.1","source":"Extra: Threat Actor Types",
     "question":"La motivación principal de un hacktivista es:",
     "options":["Ideología o protesta política/social","Ganancia económica","Espionaje gubernamental","Sabotaje de ex-empleado"],
     "correct_answers":["Ideología o protesta política/social"]},
    {"objective":"2.1","source":"Extra: Threat Actor Types",
     "question":"¿Cuál de los siguientes actores tiene típicamente el mayor nivel de financiación?",
     "options":["Nation-state","Hacktivista","Script kiddie","Insider sin privilegios"],
     "correct_answers":["Nation-state"]},
    # 4.2 ASSET MANAGEMENT
    {"objective":"4.2","source":"Extra: Asset Management",
     "question":"¿Qué es un CMDB (Configuration Management Database)?",
     "options":["Base de datos que almacena información sobre activos TI y sus relaciones","Sistema de backup de configuraciones","Herramienta de monitorización de rendimiento","Repositorio de políticas de seguridad"],
     "correct_answers":["Base de datos que almacena información sobre activos TI y sus relaciones"]},
    {"objective":"4.2","source":"Extra: Asset Management",
     "question":"¿Cuál es la diferencia entre BYOD y COPE en gestión de dispositivos?",
     "options":["BYOD: el empleado usa su propio dispositivo; COPE: la empresa lo provee pero permite uso personal","COPE: el empleado usa su propio dispositivo; BYOD: la empresa lo provee","Son sinónimos con diferente nombre de MDM","BYOD es para portátiles; COPE solo para móviles"],
     "correct_answers":["BYOD: el empleado usa su propio dispositivo; COPE: la empresa lo provee pero permite uso personal"]},
    {"objective":"4.2","source":"Extra: Asset Management",
     "question":"¿Qué implica llegar a EOSL (End of Service Life) para un activo de software?",
     "options":["El fabricante deja de publicar parches — el activo es un riesgo permanente","El software se desactiva automáticamente","Se requiere renovar la licencia para usarlo","Pasa a ser código abierto"],
     "correct_answers":["El fabricante deja de publicar parches — el activo es un riesgo permanente"]},
    {"objective":"4.2","source":"Extra: Asset Management",
     "question":"¿Para qué sirve un SBOM (Software Bill of Materials)?",
     "options":["Lista todos los componentes y dependencias para identificar vulnerabilidades en la cadena de suministro","Documenta el coste total de licencias","Registra los cambios de versión en producción","Audita el uso de software no licenciado"],
     "correct_answers":["Lista todos los componentes y dependencias para identificar vulnerabilidades en la cadena de suministro"]},
    # 4.4 MONITORING
    {"objective":"4.4","source":"Extra: Monitoring",
     "question":"¿Cuál es la diferencia entre Verdadero Positivo (TP) y Falso Positivo (FP)?",
     "options":["TP: ataque real detectado correctamente; FP: alerta sobre tráfico legítimo","FP: ataque real detectado; TP: alerta falsa","TP y FP son sinónimos — ambos indican alerta","TP aplica a IDS; FP a SIEM"],
     "correct_answers":["TP: ataque real detectado correctamente; FP: alerta sobre tráfico legítimo"]},
    {"objective":"4.4","source":"Extra: Monitoring",
     "question":"Un Falso Negativo (FN) en un IDS significa:",
     "options":["Un ataque real NO fue detectado — el error más peligroso","Una alerta generada por tráfico legítimo","Un ataque bloqueado correctamente","Una alerta duplicada en el SIEM"],
     "correct_answers":["Un ataque real NO fue detectado — el error más peligroso"]},
    {"objective":"4.4","source":"Extra: Monitoring",
     "question":"¿Qué es NetFlow y para qué se usa en seguridad?",
     "options":["Registra metadatos de flujos de red (IP, puertos, bytes) para detectar anomalías","Captura paquetes completos para análisis forense","Sistema de detección de intrusiones por firmas","Protocolo de enrutamiento dinámico"],
     "correct_answers":["Registra metadatos de flujos de red (IP, puertos, bytes) para detectar anomalías"]},
    {"objective":"4.4","source":"Extra: Monitoring",
     "question":"¿Cuál es la diferencia entre un Network TAP y un puerto SPAN?",
     "options":["TAP: copia física sin impacto en la red (más fiable); SPAN: copia software en el switch (puede perder paquetes bajo carga)","SPAN es hardware; TAP es configuración software","TAP solo captura tráfico entrante; SPAN es bidireccional","Son equivalentes"],
     "correct_answers":["TAP: copia física sin impacto en la red (más fiable); SPAN: copia software en el switch (puede perder paquetes bajo carga)"]},
    # 4.7 AUTOMATION
    {"objective":"4.7","source":"Extra: Automation",
     "question":"¿Cuál es la diferencia entre automatización y orquestación en seguridad?",
     "options":["Automatización ejecuta tareas individuales; orquestación coordina múltiples automatizaciones como flujo de trabajo","Orquestación ejecuta tareas individuales; automatización coordina sistemas","Son sinónimos en SOAR","Automatización requiere intervención humana; orquestación no"],
     "correct_answers":["Automatización ejecuta tareas individuales; orquestación coordina múltiples automatizaciones como flujo de trabajo"]},
    {"objective":"4.7","source":"Extra: Automation",
     "question":"¿Qué ventaja aporta CI/CD con SAST integrado al desarrollo seguro?",
     "options":["Detecta vulnerabilidades en cada commit antes de llegar a producción","Cifra el código fuente en el repositorio","Genera documentación de seguridad automáticamente","Sustituye las pruebas de penetración manuales"],
     "correct_answers":["Detecta vulnerabilidades en cada commit antes de llegar a producción"]},
    {"objective":"4.7","source":"Extra: Automation",
     "question":"¿Qué es un runbook en operaciones de seguridad?",
     "options":["Procedimiento documentado paso a paso para responder a un incidente o tarea operativa","Log de acciones del SOAR","Script de escaneo de vulnerabilidades","Informe de auditoría del equipo de seguridad"],
     "correct_answers":["Procedimiento documentado paso a paso para responder a un incidente o tarea operativa"]},
    # 2.5 MITIGACIÓN
    {"objective":"2.5","source":"Extra: Mitigation",
     "question":"¿Qué es EDR y en qué se diferencia de un antivirus?",
     "options":["EDR detecta amenazas por comportamiento y permite respuesta activa; el AV solo detecta firmas conocidas","EDR es un antivirus más moderno que lo sustituye completamente","EDR protege servidores; AV protege estaciones","EDR cifra endpoints; AV los escanea"],
     "correct_answers":["EDR detecta amenazas por comportamiento y permite respuesta activa; el AV solo detecta firmas conocidas"]},
    {"objective":"2.5","source":"Extra: Mitigation",
     "question":"¿Qué es UEBA (User and Entity Behavior Analytics)?",
     "options":["Detecta comportamientos anómalos de usuarios comparándolos con una línea base normal","Herramienta de gestión de identidades","Sistema MFA basado en comportamiento","Plataforma de análisis de logs de firewall"],
     "correct_answers":["Detecta comportamientos anómalos de usuarios comparándolos con una línea base normal"]},
    # 5.3 THIRD PARTY RISK
    {"objective":"5.3","source":"Extra: Third Party Risk",
     "question":"El ataque SolarWinds (2020) es el ejemplo más citado de ataque a la cadena de suministro. ¿Qué hicieron los atacantes?",
     "options":["Comprometieron el software de actualización de SolarWinds e inyectaron malware (SUNBURST) que se distribuyó a miles de clientes","Atacaron directamente las redes de los clientes por phishing","Explotaron un zero-day en el servidor web de SolarWinds","Realizaron un DDoS contra la infraestructura de SolarWinds"],
     "correct_answers":["Comprometieron el software de actualización de SolarWinds e inyectaron malware (SUNBURST) que se distribuyó a miles de clientes"]},
    {"objective":"5.3","source":"Extra: Third Party Risk",
     "question":"¿Qué es un MSA (Master Service Agreement)?",
     "options":["Contrato marco con términos generales de la relación, sobre el que se construyen acuerdos específicos","Acuerdo de confidencialidad","Contrato que define niveles mínimos de servicio","Acuerdo de intención sin fuerza legal"],
     "correct_answers":["Contrato marco con términos generales de la relación, sobre el que se construyen acuerdos específicos"]},
    # 5.5 AUDITS
    {"objective":"5.5","source":"Extra: Audits",
     "question":"¿Qué es una auditoría interna vs externa?",
     "options":["Interna: personal propio de la organización; externa: tercero independiente (mayor objetividad)","Externa: personal propio; interna: tercero","Interna evalúa controles técnicos; externa evalúa administrativos","Son equivalentes — solo difiere quién firma el informe"],
     "correct_answers":["Interna: personal propio de la organización; externa: tercero independiente (mayor objetividad)"]},
    {"objective":"5.5","source":"Extra: Audits",
     "question":"¿Qué es un 'right to audit' en un contrato con proveedor?",
     "options":["Cláusula que permite al cliente auditar las operaciones, instalaciones y registros del proveedor","Derecho del proveedor a auditar el uso del software por el cliente","Obligación de publicar resultados de auditoría externamente","Cláusula que limita las auditorías a una vez al año"],
     "correct_answers":["Cláusula que permite al cliente auditar las operaciones, instalaciones y registros del proveedor"]},
]

all_questions = existing + nuevas
with open(r'D:\Users\cra\Desktop\Sec+\preguntas_nuevas.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"Total preguntas nuevas: {len(all_questions)}")
objs = {}
for q in all_questions:
    objs[q['objective']] = objs.get(q['objective'], 0) + 1
for k in sorted(objs):
    print(f"  {k}: {objs[k]}")
