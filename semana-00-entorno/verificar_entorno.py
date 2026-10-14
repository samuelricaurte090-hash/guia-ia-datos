"""Verifica que tu entorno de trabajo esté listo.

Uso (desde la carpeta guia-ia-datos):
    uv run python semana-00-entorno/verificar_entorno.py
"""

import importlib
import shutil
import subprocess
import sys

OK = "[ OK ]"
FALTA = "[FALTA]"
pendientes = 0


def revisar(condicion: bool, mensaje: str, solucion: str = "") -> None:
    global pendientes
    if condicion:
        print(f"{OK} {mensaje}")
    else:
        pendientes += 1
        print(f"{FALTA} {mensaje}")
        if solucion:
            print(f"        -> {solucion}")


def comando(*args: str) -> str:
    try:
        return subprocess.run(args, capture_output=True, text=True, check=False).stdout.strip()
    except OSError:
        return ""


print("Revisando tu entorno...\n")

version = sys.version_info
revisar(
    version >= (3, 12),
    f"Python {version.major}.{version.minor}.{version.micro}",
    "Necesitas Python 3.12 o superior.",
)
revisar(
    ".venv" in sys.prefix,
    "Estás usando el entorno virtual del proyecto (.venv)",
    "Ejecuta este script con 'uv run python ...' desde la carpeta guia-ia-datos.",
)

for paquete in ["numpy", "pandas", "matplotlib", "jupyterlab", "pytest"]:
    try:
        modulo = importlib.import_module(paquete)
        revisar(True, f"{paquete} {getattr(modulo, '__version__', '')}".strip())
    except ImportError:
        revisar(False, f"{paquete} instalado", "Ejecuta 'uv sync' en la carpeta guia-ia-datos.")

git = shutil.which("git")
revisar(git is not None, "Git instalado", "Instálalo con: winget install --id Git.Git -e  (y abre una terminal nueva)")
if git:
    nombre = comando("git", "config", "--global", "user.name")
    correo = comando("git", "config", "--global", "user.email")
    revisar(bool(nombre), f"Git sabe tu nombre: {nombre or '-'}", 'git config --global user.name "Tu Nombre"')
    revisar(bool(correo), f"Git sabe tu correo: {correo or '-'}", 'git config --global user.email "tu@correo.com"')
    remoto = comando("git", "remote", "get-url", "origin")
    revisar(bool(remoto), f"Repositorio conectado a GitHub: {remoto or '-'}", "Sigue el paso 5 del README de la semana 0.")

revisar(shutil.which("code") is not None, "VS Code disponible desde la terminal", "Reinstala VS Code marcando 'Add to PATH'.")

print()
if pendientes:
    cosas = "cosa" if pendientes == 1 else "cosas"
    print(f"Te falta{'' if pendientes == 1 else 'n'} {pendientes} {cosas}. Corrige lo marcado con {FALTA} y vuelve a correr el script.")
else:
    print("Todo listo. Ya puedes empezar la semana 1.")
