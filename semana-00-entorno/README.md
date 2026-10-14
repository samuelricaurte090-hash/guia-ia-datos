# Semana 0 · Entorno de trabajo

**Fechas:** 14 al 18 de octubre de 2026 · **Tiempo:** 2 a 3 horas

Antes de estudiar, deja listo el taller. Lo que montes hoy lo vas a usar en todo el plan y en cualquier trabajo de datos: Git, un entorno de Python por proyecto y un editor bien configurado.

Ya tienes Python 3.14, uv y VS Code. Te falta Git.

## Paso 1 · Instalar Git

Abre PowerShell y ejecuta:

```powershell
winget install --id Git.Git -e
```

Cierra la terminal y abre una nueva. Luego dile a Git quién eres (usa el mismo correo de tu cuenta de GitHub):

```powershell
git config --global user.name "Tu Nombre"
git config --global user.email "tu@correo.com"
git config --global init.defaultBranch main
```

## Paso 2 · Instalar las librerías del proyecto

En la carpeta `guia-ia-datos` hay un archivo `pyproject.toml` con las librerías que vas a usar. uv crea un entorno virtual (`.venv`) solo para este proyecto y las instala ahí, sin tocar el resto de tu computador:

```powershell
cd $HOME\Documents\Programacion\guia-ia-datos
uv sync
```

**Por qué importa:** en tu curso anterior tenías un entorno distinto en cada carpeta (`env`, `ds_env`). Así se trabaja en empresas: cada proyecto declara sus dependencias en un archivo y cualquiera puede reproducirlo con un comando.

Comandos que vas a usar todo el tiempo:

| Comando | Qué hace |
|---|---|
| `uv sync` | Instala o actualiza las librerías del `pyproject.toml` |
| `uv add scikit-learn` | Agrega una librería nueva al proyecto |
| `uv run python archivo.py` | Corre un script con el entorno del proyecto |
| `uv run pytest semana-01-python -x` | Corre las pruebas de una semana |
| `uv run jupyter lab` | Abre Jupyter Lab con el entorno del proyecto |

## Paso 3 · Configurar VS Code

1. Abre la carpeta: `code .` desde la terminal, dentro de `guia-ia-datos`.
2. Instala las extensiones **Python** y **Jupyter** de Microsoft.
3. `Ctrl+Shift+P` → **Python: Select Interpreter** → elige el que dice `.venv`.

## Paso 4 · Verificar

```powershell
uv run python semana-00-entorno/verificar_entorno.py
```

Corrige lo que salga marcado con `[FALTA]` y vuelve a correrlo. El paso de GitHub saldrá pendiente hasta que hagas el paso 5.

## Paso 5 · Subir tu guía a GitHub

Tu GitHub es tu hoja de vida técnica: los reclutadores de datos lo miran. Un historial con commits constantes durante meses dice mucho.

1. Crea una cuenta en [github.com](https://github.com) si no tienes, con una foto y tu nombre real.
2. Crea un repositorio nuevo llamado `guia-ia-datos`, **sin** README ni .gitignore (ya los tienes).
3. En la terminal, dentro de la carpeta:

```powershell
git init
git add .
git commit -m "Semana 0: entorno de trabajo listo"
git remote add origin https://github.com/TU_USUARIO/guia-ia-datos.git
git push -u origin main
```

La primera vez, Git abre una ventana para iniciar sesión en GitHub.

Desde ahora, al terminar cada sesión de estudio:

```powershell
git add .
git commit -m "Semana 1: ejercicios 1 a 5"
git push
```

## Paso 6 · Fijar tu horario

Escribe tu horario real en `PROGRESO.md`. La propuesta del plan es:

- Lunes a jueves: 1,5 horas (por ejemplo, 8:00 a 9:30 p. m.)
- Sábado: 4 horas
- Viernes y domingo: libres

Diez horas constantes valen más que veinte un fin de semana y cero el siguiente.

## Terminado si

- [ ] `verificar_entorno.py` no muestra nada con `[FALTA]`
- [ ] Tu repositorio `guia-ia-datos` está en GitHub con el primer commit
- [ ] Tu horario está escrito en `PROGRESO.md`
