# Guía de Contribución

¡Gracias por tu interés en contribuir a este proyecto! 🎉

## Cómo Contribuir

### Reportar Errores

Si encuentras un error en el contenido (información incorrecta, typos, código que no funciona):

1. Busca en [Issues](https://github.com/tu-usuario/security-plus-sy0701/issues) si ya fue reportado
2. Si no existe, abre un nuevo Issue con:
   - **Título claro**: "Error en LAB 4.2: comando iptables incorrecto"
   - **Descripción**: Qué archivo/sección tiene el error
   - **Error encontrado**: Qué dice actualmente
   - **Corrección sugerida**: Qué debería decir
   - **Fuente** (opcional): Link a documentación oficial

### Sugerir Mejoras

¿Tienes ideas para mejorar el material?

1. Abre un Issue con etiqueta `enhancement`
2. Describe:
   - Qué quieres mejorar
   - Por qué sería útil
   - Ejemplo de implementación (opcional)

### Añadir Contenido Nuevo

#### Labs Nuevos

Si quieres contribuir un lab:

1. Fork el repositorio
2. Crea el lab en formato markdown en `laboratorios/dominio-X/`
3. Sigue esta estructura:

```markdown
# LAB X.X: Título del Lab

## Objetivos
- Objetivo 1
- Objetivo 2

## Requisitos
- Software necesario
- VMs necesarias
- Tiempo estimado: X horas

## Pasos

### Paso 1: Preparación
[Comandos y explicación]

### Paso 2: Configuración
[Comandos y explicación]

## Validación
[Cómo verificar que funcionó]

## Troubleshooting
[Problemas comunes y soluciones]

## Limpieza
[Cómo limpiar después del lab]
```

4. Añade el lab al índice en `laboratorios/README.md`
5. Commit: `git commit -m "Añadido LAB 3.4: VPN con OpenVPN"`
6. Push y abre Pull Request

#### Ejemplos de Logs Nuevos

Si quieres añadir ejemplos de análisis de logs:

1. Fork el repositorio
2. Edita `guias-practicas/analisis-logs.md`
3. Añade tu ejemplo siguiendo esta estructura:

```markdown
### Ejemplo 21: [Tipo de Ataque]

**Escenario**: [Breve descripción]

**Log**:
```
[Log real o simulado]
```

**Análisis**:
- IOC 1: [Indicador]
- IOC 2: [Indicador]
- IOC 3: [Indicador]

**Explicación**: [Qué pasó]

**Remediación**:
1. Acción 1
2. Acción 2

**Relación con examen**: [Qué preguntan sobre esto]
```

4. Commit: `git commit -m "Añadido ejemplo análisis: API abuse"`
5. Push y abre Pull Request

#### Ejercicios de Cálculo

Si quieres añadir ejercicios:

1. Fork el repositorio
2. Edita `guias-practicas/ejercicios-calculos.md`
3. Añade ejercicio + solución detallada
4. Commit y Pull Request

### Traducir a Inglés

¿Hablas inglés nativo o nivel C1+?

1. Fork el repositorio
2. Crea carpeta `en/` con estructura idéntica
3. Traduce archivos manteniendo formato markdown
4. Pull Request con etiqueta `translation`

## Estilo y Formato

### Markdown

- Usa headers correctamente (`#`, `##`, `###`)
- Bloques de código con syntax highlighting:
  ```bash
  comando aquí
  ```
- Listas con `-` o `1.`
- **Negrita** para términos importantes
- `Código inline` para comandos/archivos

### Comandos

```bash
# ✅ CORRECTO: comentarios explicativos
sudo apt update  # Actualizar repositorios
sudo apt install nmap -y

# ❌ INCORRECTO: sin explicación
sudo apt update
sudo apt install nmap -y
```

### Términos Técnicos

- Primera mención: **ALE (Annual Loss Expectancy)**
- Menciones siguientes: ALE
- Acrónimos en inglés: mantener en inglés (no traducir)
- Comandos: mantener en inglés

## Proceso de Review

1. **Abres Pull Request**
2. **Revisión automática** (checks de markdown, links rotos)
3. **Revisión humana** (maintainer revisa contenido)
4. **Feedback** (si hay cambios necesarios)
5. **Merge** (si todo OK)

**Tiempo estimado**: 3-7 días

## Qué NO Contribuir

❌ Material copiado de cursos pagos (copyright)
❌ Respuestas exactas de exámenes reales (viola NDA CompTIA)
❌ Contenido ofensivo o no relacionado
❌ Material comercial (promoción de productos)

## Código de Conducta

- Sé respetuoso con otros contribuidores
- No spam ni auto-promoción excesiva
- Críticas constructivas, no destructivas
- Acepta feedback con mente abierta

## Reconocimiento

Todos los contribuidores serán añadidos a:
- `README.md` (sección Contributors)
- Release notes cuando aplique

¡Gracias por hacer este proyecto mejor! 🙏
