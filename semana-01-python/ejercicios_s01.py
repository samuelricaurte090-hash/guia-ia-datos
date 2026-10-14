"""Semana 1 · Python sólido para datos.

Completa cada función en orden. Borra la línea `raise NotImplementedError(...)`
y escribe tu solución. Para comprobar tu avance:

    uv run pytest semana-01-python -x

`-x` se detiene en el primer ejercicio que falle, así que avanzas de uno en uno.
Para correr un solo ejercicio: `uv run pytest semana-01-python -k ej07`.

Regla: no pidas la solución completa a una IA. Pide pistas o una revisión
cuando ya tengas un intento. En una prueba técnica estarás solo.
"""

from __future__ import annotations

from pathlib import Path


# ---------------------------------------------------------------------------
# Nivel 1 · Básicos
# ---------------------------------------------------------------------------

def celsius_a_fahrenheit(c: float) -> float:
    """Ejercicio 1. Convierte grados Celsius a Fahrenheit.

    >>> celsius_a_fahrenheit(100)
    212.0
    """
    raise NotImplementedError("Ejercicio 1: escribe tu solución")


def promedio(valores: list[float]) -> float:
    """Ejercicio 2. Devuelve el promedio de la lista.

    Si la lista está vacía, lanza ValueError con un mensaje claro.

    >>> promedio([2, 4, 6])
    4.0
    """
    raise NotImplementedError("Ejercicio 2: escribe tu solución")


def contar_pares(numeros: list[int]) -> int:
    """Ejercicio 3. Cuenta cuántos números pares hay (el 0 es par).

    Intenta resolverlo en una sola línea con sum() y una expresión generadora.

    >>> contar_pares([1, 2, 3, 4, 0])
    3
    """
    raise NotImplementedError("Ejercicio 3: escribe tu solución")


def normalizar_nombre(texto: str) -> str:
    """Ejercicio 4. Limpia un nombre escrito a mano en un formulario.

    Quita espacios al inicio y al final, deja un solo espacio entre palabras
    y pone cada palabra con mayúscula inicial.

    >>> normalizar_nombre("  juan   PÉREZ ")
    'Juan Pérez'
    """
    raise NotImplementedError("Ejercicio 4: escribe tu solución")


def es_palindromo(texto: str) -> bool:
    """Ejercicio 5. ¿Se lee igual al derecho y al revés?

    Ignora mayúsculas, espacios y signos de puntuación (solo cuentan letras y
    dígitos). Pista: str.isalnum() y el slicing [::-1].

    >>> es_palindromo("Anita lava la tina")
    True
    """
    raise NotImplementedError("Ejercicio 5: escribe tu solución")


# ---------------------------------------------------------------------------
# Nivel 2 · Estructuras de datos
# ---------------------------------------------------------------------------

def frecuencias(palabras: list[str]) -> dict[str, int]:
    """Ejercicio 6. Cuenta cuántas veces aparece cada palabra.

    No distingue mayúsculas: "Hola" y "hola" son la misma palabra y la clave
    queda en minúsculas. Pista: collections.Counter.

    >>> frecuencias(["Hola", "hola", "mundo"])
    {'hola': 2, 'mundo': 1}
    """
    raise NotImplementedError("Ejercicio 6: escribe tu solución")


def top_n(conteos: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Ejercicio 7. Las n claves con mayor conteo.

    Ordena de mayor a menor conteo; si hay empate, en orden alfabético.
    Pista: sorted() con key=lambda y un conteo negativo.

    >>> top_n({"a": 3, "b": 5, "c": 3, "d": 1}, 2)
    [('b', 5), ('a', 3)]
    """
    raise NotImplementedError("Ejercicio 7: escribe tu solución")


def invertir_diccionario(d: dict[str, str]) -> dict[str, list[str]]:
    """Ejercicio 8. Agrupa las claves según su valor.

    Las listas resultantes van ordenadas alfabéticamente.

    >>> invertir_diccionario({"T-01": "temperatura", "T-02": "temperatura", "V-01": "vibracion"})
    {'temperatura': ['T-01', 'T-02'], 'vibracion': ['V-01']}
    """
    raise NotImplementedError("Ejercicio 8: escribe tu solución")


def elementos_comunes(a: list, b: list) -> list:
    """Ejercicio 9. Elementos que están en ambas listas, sin repetir y ordenados.

    Pista: conjuntos (set).

    >>> elementos_comunes([3, 1, 2, 2], [2, 3, 4])
    [2, 3]
    """
    raise NotImplementedError("Ejercicio 9: escribe tu solución")


def agrupar_por(registros: list[dict], clave: str) -> dict[str, list[dict]]:
    """Ejercicio 10. Agrupa registros según el valor de una clave.

    Dentro de cada grupo se conserva el orden original.
    Pista: collections.defaultdict(list).

    >>> agrupar_por([{"s": "A", "v": 1}, {"s": "B", "v": 2}, {"s": "A", "v": 3}], "s")
    {'A': [{'s': 'A', 'v': 1}, {'s': 'A', 'v': 3}], 'B': [{'s': 'B', 'v': 2}]}
    """
    raise NotImplementedError("Ejercicio 10: escribe tu solución")


def aplanar(listas: list[list]) -> list:
    """Ejercicio 11. Une una lista de listas en una sola lista (un nivel).

    Hazlo con una comprensión de listas.

    >>> aplanar([[1, 2], [3], []])
    [1, 2, 3]
    """
    raise NotImplementedError("Ejercicio 11: escribe tu solución")


# ---------------------------------------------------------------------------
# Nivel 3 · Cálculos con datos
# ---------------------------------------------------------------------------

def media_movil(valores: list[float], ventana: int) -> list[float]:
    """Ejercicio 12. Media móvil simple.

    El resultado tiene len(valores) - ventana + 1 elementos. Si la ventana es
    menor que 1 o mayor que la cantidad de valores, lanza ValueError.

    >>> media_movil([1, 2, 3, 4, 5], 2)
    [1.5, 2.5, 3.5, 4.5]
    """
    raise NotImplementedError("Ejercicio 12: escribe tu solución")


def estadisticas(valores: list[float]) -> dict[str, float]:
    """Ejercicio 13. Resumen estadístico de una lista.

    Devuelve un diccionario con las claves: "n", "min", "max", "media",
    "mediana" y "desviacion" (desviación estándar MUESTRAL, dividiendo por
    n - 1). Con un solo valor, la desviación es 0.0. Lista vacía: ValueError.

    Intenta calcular la mediana y la desviación a mano. Después compara con
    el módulo statistics.

    >>> estadisticas([2, 4, 4, 6])["mediana"]
    4.0
    """
    raise NotImplementedError("Ejercicio 13: escribe tu solución")


def detectar_atipicos(valores: list[float], z: float = 3.0) -> list[int]:
    """Ejercicio 14. Índices de los valores atípicos según el puntaje z.

    Un valor es atípico si |valor - media| / desviación > z, usando la
    desviación muestral. Si la desviación es 0, no hay atípicos.

    >>> detectar_atipicos([10] * 9 + [50], z=2.0)
    [9]
    """
    raise NotImplementedError("Ejercicio 14: escribe tu solución")


def normalizar_min_max(valores: list[float]) -> list[float]:
    """Ejercicio 15. Escala los valores al rango [0, 1].

    Si todos los valores son iguales, devuelve una lista de ceros.
    Lista vacía: devuelve lista vacía.

    >>> normalizar_min_max([2, 4, 6])
    [0.0, 0.5, 1.0]
    """
    raise NotImplementedError("Ejercicio 15: escribe tu solución")


def parsear_lectura(linea: str) -> dict:
    """Ejercicio 16. Convierte una línea exportada desde Excel en un diccionario.

    Formato: "fecha;sensor;variable;valor", separado por punto y coma.
    El valor puede venir con coma decimal ("23,5") o con punto ("23.5").
    Quita espacios sobrantes de cada campo.

    Lanza ValueError si la línea no tiene exactamente 4 campos o si el valor
    no es un número.

    >>> parsear_lectura("2026-10-19T08:00;T-01;temperatura;23,5")
    {'fecha': '2026-10-19T08:00', 'sensor': 'T-01', 'variable': 'temperatura', 'valor': 23.5}
    """
    raise NotImplementedError("Ejercicio 16: escribe tu solución")


# ---------------------------------------------------------------------------
# Nivel 4 · Archivos y clases
# ---------------------------------------------------------------------------

def leer_lecturas(ruta: str | Path) -> list[dict]:
    """Ejercicio 17. Lee un CSV de lecturas de sensores, sin pandas.

    Columnas: fecha, sensor, variable, valor. Devuelve una lista de
    diccionarios con "valor" convertido a float. Omite las filas cuyo valor
    esté vacío. Acepta la ruta como texto o como Path.

    Pista: pathlib.Path, open(..., encoding="utf-8", newline="") y
    csv.DictReader.
    """
    raise NotImplementedError("Ejercicio 17: escribe tu solución")


def resumen_por_sensor(lecturas: list[dict]) -> dict[str, dict]:
    """Ejercicio 18. Resumen por sensor.

    Para cada sensor devuelve {"n": ..., "media": ..., "min": ..., "max": ...}.

    >>> resumen_por_sensor([{"sensor": "A", "valor": 1.0}, {"sensor": "A", "valor": 3.0}])
    {'A': {'n': 2, 'media': 2.0, 'min': 1.0, 'max': 3.0}}
    """
    raise NotImplementedError("Ejercicio 18: escribe tu solución")


class Lectura:
    """Ejercicio 19. Una lectura de sensor como objeto.

    1. Conviértela en dataclass (from dataclasses import dataclass) con los
       campos fecha: str, sensor: str, variable: str y valor: float.
    2. Implementa fuera_de_rango: True si el valor es menor que minimo o
       mayor que maximo. Los límites mismos están dentro del rango.
    3. Implementa desde_dict: crea una Lectura a partir de un diccionario como
       los de leer_lecturas, convirtiendo "valor" a float aunque venga como
       texto.
    """

    def fuera_de_rango(self, minimo: float, maximo: float) -> bool:
        raise NotImplementedError("Ejercicio 19: escribe tu solución")

    @classmethod
    def desde_dict(cls, d: dict) -> "Lectura":
        raise NotImplementedError("Ejercicio 19: escribe tu solución")


def contar_alertas(
    lecturas: list[dict], limites: dict[str, tuple[float, float]]
) -> dict[str, int]:
    """Ejercicio 20. Cuenta las lecturas fuera de rango por sensor.

    `limites` asocia cada variable con su rango permitido, por ejemplo
    {"temperatura": (15, 35)}. Las variables sin límite nunca generan alerta.
    Todos los sensores presentes aparecen en el resultado, aunque tengan 0.

    Reutiliza tu clase Lectura.
    """
    raise NotImplementedError("Ejercicio 20: escribe tu solución")
