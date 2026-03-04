# Instrucciones para Subir a GitHub

## Paso 1: Revisar el Contenido

Antes de subir, verifica que todo está correcto:

```bash
cd D:\Users\cra\Desktop\Sec+\GitHub_Repo

# Listar estructura
tree /F
# o en PowerShell:
Get-ChildItem -Recurse | Select-Object FullName
```

**Deberías ver**:
```
GitHub_Repo/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
├── INSTRUCCIONES_GITHUB.md (este archivo)
│
├── plan-8-semanas/
│   ├── README.md
│   ├── semana-1-2-fundamentos/README.md
│   ├── semana-3-4-arquitectura/README.md
│   ├── semana-5-6-operaciones/README.md
│   └── semana-7-8-governance/README.md
│
├── flashcards/
│   ├── flashcards.html
│   ├── flashcards.csv (si existe)
│   └── flashcards.pdf
│
├── laboratorios/
│   ├── README.md
│   ├── quick_start.md
│   ├── dominio-1/ (3 labs)
│   ├── dominio-2/ (2 labs)
│   ├── dominio-3/ (3 labs)
│   ├── dominio-4/ (3 labs)
│   └── dominio-5/ (3 labs)
│
├── guias-practicas/
│   ├── cheat-sheet-comandos-pbqs.md
│   ├── guia-analisis-logs.md
│   └── ejercicios-calculos-practicos.md
│
└── diccionario/
    ├── diccionario-completo.json
    └── diccionario-completo.md
```

---

## Paso 2: Personalizar README.md

Edita `README.md` y cambia:

1. **Tu usuario GitHub** (línea 3):
   ```markdown
   [![Licencia](https://img.shields.io/badge/...)](LICENSE)
   ```
   Busca `tu-usuario` y reemplaza por tu usuario real

2. **URLs de issues** (varias líneas):
   ```markdown
   https://github.com/tu-usuario/security-plus-sy0701/issues
   ```

3. **URLs de stats** (al final):
   ```markdown
   ![GitHub stars](https://img.shields.io/github/stars/tu-usuario/security-plus-sy0701?style=social)
   ```

4. **Copyright en LICENSE** (año y nombre):
   ```
   Copyright (c) 2026 [Tu Nombre]
   Email: [tu-email@example.com]
   ```

---

## Paso 3: Crear Repositorio en GitHub

### 3.1 Desde GitHub.com

1. Ve a https://github.com
2. Click en `+` (arriba derecha) → `New repository`
3. Rellena:
   - **Repository name**: `security-plus-sy0701` (o el que prefieras)
   - **Description**: `Material de estudio completo para CompTIA Security+ SY0-701 con plan de 8 semanas`
   - **Public** (para que otros lo vean)
   - **NO marques** "Initialize with README" (ya tienes uno)
   - **NO añadas** .gitignore ni licencia (ya tienes)
4. Click `Create repository`

### 3.2 Copia la URL

GitHub te mostrará algo como:
```
https://github.com/tu-usuario/security-plus-sy0701.git
```

**Cópiala**, la usarás en el paso 4.

---

## Paso 4: Inicializar Git Local

### 4.1 Abrir Terminal

**Windows**:
- Abre `Git Bash` (si instalaste Git for Windows)
- O `PowerShell` / `CMD`

**Mac/Linux**:
- Abre `Terminal`

### 4.2 Navegar a la carpeta

```bash
cd D:\Users\cra\Desktop\Sec+\GitHub_Repo
```

### 4.3 Verificar Git instalado

```bash
git --version
```

Si dice `git version 2.x.x` → OK

Si dice `command not found`:
- Windows: Descarga https://git-scm.com/download/win
- Mac: `brew install git` o instala Xcode Command Line Tools
- Linux: `sudo apt install git` (Ubuntu/Debian) o `sudo yum install git` (RHEL/CentOS)

---

## Paso 5: Inicializar Repositorio

```bash
# Inicializar git
git init

# Verificar archivos
git status
# Deberías ver todos los archivos en rojo (untracked)

# Añadir todos los archivos
git add .

# Verificar que se añadieron
git status
# Ahora deberían estar en verde (staged)

# Crear primer commit
git commit -m "Initial commit: Security+ SY0-701 material completo v1.0"

# Verificar commit
git log
# Deberías ver tu commit
```

---

## Paso 6: Conectar con GitHub

```bash
# Añadir remote (reemplaza TU-USUARIO y TU-REPO)
git remote add origin https://github.com/TU-USUARIO/security-plus-sy0701.git

# Verificar remote
git remote -v
# Debería mostrar:
# origin  https://github.com/TU-USUARIO/security-plus-sy0701.git (fetch)
# origin  https://github.com/TU-USUARIO/security-plus-sy0701.git (push)

# Renombrar branch a main (GitHub usa main por defecto ahora)
git branch -M main

# Subir a GitHub
git push -u origin main
```

**Si pide autenticación**:
- Username: tu usuario GitHub
- Password: **NO uses tu password**, usa **Personal Access Token**

### Crear Personal Access Token (si es necesario)

1. Ve a https://github.com/settings/tokens
2. Click `Generate new token (classic)`
3. Selecciona scopes: `repo` (acceso completo a repositorios)
4. Click `Generate token`
5. **COPIA el token** (solo se muestra UNA VEZ)
6. Úsalo como password cuando git te lo pida

---

## Paso 7: Verificar en GitHub

1. Ve a https://github.com/TU-USUARIO/security-plus-sy0701
2. Deberías ver:
   - README.md renderizado (bonito, con badges)
   - Todas las carpetas
   - Licencia detectada (esquina derecha)
   - .gitignore funcionando (no hay archivos .tmp, .log, etc.)

---

## Paso 8: Configurar Repositorio (Opcional)

### 8.1 Añadir Topics

1. En tu repo, click en ⚙️ (Settings) o rueda dentada arriba a la derecha junto a About
2. En la sección "About", click `⚙️` (edit)
3. Añade topics:
   ```
   comptia
   security-plus
   sy0-701
   cybersecurity
   certification
   study-guide
   flashcards
   labs
   español
   ```
4. Save changes

### 8.2 Editar About

En la misma sección "About":
- **Description**: `Material de estudio completo para CompTIA Security+ SY0-701 con plan de 8 semanas estructurado`
- **Website**: (deja vacío o pon tu sitio personal)
- Marca ✅ `Releases` y ✅ `Packages` si quieres

### 8.3 Crear Primer Release (Opcional)

1. En tu repo, click `Releases` (derecha)
2. Click `Create a new release`
3. Rellena:
   - **Tag**: `v1.0`
   - **Release title**: `v1.0 - Initial Release`
   - **Description**:
     ```markdown
     ## Security+ SY0-701 - Material Completo v1.0

     Primera versión pública del material de estudio.

     **Incluye**:
     - 382 flashcards (220 ALTA + 162 MEDIA)
     - Plan 8 semanas día a día
     - 15 laboratorios prácticos
     - 20 ejemplos análisis de logs
     - 12 ejercicios de cálculos
     - Cheat sheet comandos
     - 100% cobertura objetivos SY0-701

     **Score esperado**: 85-92%
     ```
4. Click `Publish release`

---

## Paso 9: Compartir

Una vez todo subido, puedes compartir:

### En Reddit

**r/CompTIA**:
```markdown
Título: [Security+] Creé material de estudio completo en español (gratis) - Plan 8 semanas

Hola! Después de aprobar Security+ con 87%, organicé TODO mi material
de estudio en un repo de GitHub:

[Link a tu repo]

Incluye:
- 382 flashcards interactivas
- Plan de 8 semanas día a día con checkboxes
- 15 labs prácticos
- 20 ejemplos de análisis de logs
- Ejercicios de cálculos (ALE, subnetting, etc.)

Todo gratis y open source. Si les sirve, denle una estrella! ⭐

¿Preguntas sobre Security+? Las respondo en los comentarios.
```

### En LinkedIn

```
🔐 Lancé mi repositorio de Security+ SY0-701

Después de aprobar CompTIA Security+ con 87%, decidí organizar
todo mi material de estudio y hacerlo público (gratis).

Incluye:
✅ Plan de 8 semanas estructurado
✅ 382 flashcards interactivas
✅ 15 laboratorios hands-on
✅ 20 ejemplos de análisis de logs
✅ 100% cobertura de objetivos

Link: [tu repo]

Si estás estudiando Security+ o conoces a alguien que lo esté,
comparte! 🚀

#CompTIA #SecurityPlus #Cybersecurity #OpenSource
```

### En Twitter/X

```
🔐 Lancé repo GitHub con material COMPLETO Security+ SY0-701 (gratis)

- 382 flashcards
- Plan 8 semanas
- 15 labs
- 20 ejemplos logs
- 100% coverage

[Link]

RT si conoces a alguien estudiando Security+ 🚀

#CompTIA #SecurityPlus #Cybersecurity
```

---

## Paso 10: Mantenimiento

### Actualizar Material

Cuando hagas cambios:

```bash
# Navegar al repo
cd D:\Users\cra\Desktop\Sec+\GitHub_Repo

# Ver cambios
git status

# Añadir cambios
git add .

# Commit
git commit -m "Descripción de cambios"

# Subir
git push
```

### Responder Issues

Cuando alguien reporte un error o haga una pregunta:
1. Ve a tu repo → `Issues`
2. Lee el issue
3. Responde o cierra

### Aceptar Pull Requests

Cuando alguien contribuya:
1. Ve a tu repo → `Pull requests`
2. Revisa cambios
3. Si está bien: `Merge pull request`
4. Si no: Pide cambios en comentarios

---

## Troubleshooting

### Error: "permission denied"
```bash
# Verifica remote
git remote -v

# Si es https://, cambia a SSH (más fácil auth):
git remote set-url origin git@github.com:TU-USUARIO/security-plus-sy0701.git

# O usa credential helper:
git config --global credential.helper store
```

### Error: "repository not found"
- Verifica que creaste el repo en GitHub
- Verifica la URL del remote: `git remote -v`
- Verifica tu username en la URL

### Error: "failed to push some refs"
```bash
# Alguien subió cambios antes que tú
# Pull primero:
git pull origin main --rebase

# Luego push:
git push
```

### Archivos demasiado grandes
GitHub tiene límite de 100MB por archivo.

Si flashcards.pdf es muy grande:
```bash
# Ver tamaño
ls -lh flashcards/flashcards.pdf

# Si es > 100MB, comprime:
# Opción 1: Comprimir PDF (online: smallpdf.com, ilovepdf.com)
# Opción 2: Usar Git LFS:
git lfs install
git lfs track "*.pdf"
git add .gitattributes
git add flashcards/flashcards.pdf
git commit -m "Add large PDF with LFS"
git push
```

---

## Checklist Final

Antes de compartir públicamente:

- [ ] README.md personalizado (cambiado "tu-usuario")
- [ ] LICENSE con tu nombre y email
- [ ] Repo creado en GitHub (público)
- [ ] Todo subido (`git push` exitoso)
- [ ] README se ve bien en GitHub (bonito, con badges)
- [ ] Flashcards HTML funciona (abre en navegador)
- [ ] Flashcards PDF abre correctamente
- [ ] Labs tienen formato correcto (markdown)
- [ ] No hay información personal sensible (passwords, claves, etc.)
- [ ] Topics añadidos al repo
- [ ] Primer release creado (v1.0)

---

## ¡Listo!

Tu repositorio está público y listo para compartir.

**URL para compartir**:
```
https://github.com/TU-USUARIO/security-plus-sy0701
```

**¡Mucha suerte y gracias por contribuir a la comunidad!** 🚀

---

## Contacto

Si tienes problemas:
1. Revisa esta guía completa
2. Busca en Google: "github [tu error]"
3. Pregunta en r/github o r/git

**No compartas este archivo** (es solo para ti, tiene instrucciones técnicas que no son relevantes para usuarios del material).
