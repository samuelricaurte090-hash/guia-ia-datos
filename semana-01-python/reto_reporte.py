"""Reto de la semana 1: reporte de sensores desde la terminal.

Uso:
    uv run python semana-01-python/reto_reporte.py semana-01-python/datos/sensores.csv

Este reto no tiene pruebas automáticas. Sabes que terminaste cuando la salida
se parece a la del README de la semana y cumples la lista de "Terminado si".
Reutiliza tus funciones de ejercicios_s01.py: no copies código.
"""

import sys
from pathlib import Path

from ejercicios_s01 import contar_alertas, leer_lecturas, resumen_por_sensor  # noqa: F401

# Rangos de operación permitidos por variable (unidades: °C, mm/s, bar)
LIMITES = {
    "temperatura": (15, 35),
    "vibracion": (0, 5),
    "presion": (5.5, 7.0),
}


def main(ruta: Path) -> None:
    # TODO 1: si el archivo no existe, imprime un mensaje claro y termina con sys.exit(1).
    # TODO 2: lee las lecturas válidas y cuenta cuántas filas se descartaron
    #         (filas del archivo sin contar el encabezado, menos lecturas válidas).
    # TODO 3: imprime el encabezado del reporte con el nombre del archivo.
    # TODO 4: imprime una tabla por sensor con: sensor, variable, n, media, mín, máx y alertas.
    #         Alinea las columnas con f-strings, por ejemplo f"{texto:<8}" y f"{numero:>7.2f}".
    # TODO 5: imprime la lista de alertas con fecha, sensor, valor y rango permitido.
    raise NotImplementedError("Reto: escribe tu solución")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python reto_reporte.py <ruta_al_csv>")
        sys.exit(2)
    main(Path(sys.argv[1]))
