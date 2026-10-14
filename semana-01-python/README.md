# Semana 1 · Python sólido para datos

**Fechas:** 19 al 25 de octubre de 2026 · **Tiempo:** 10 horas

En marzo y abril ya usaste NumPy y pandas. Esta semana no repite eso. Se enfoca en el Python "puro" que los cursos suelen saltarse y que aparece en las pruebas técnicas: estructuras de datos bien elegidas, funciones limpias, archivos, errores, clases y pruebas automáticas.

## Cómo trabajar

1. Lee la lección de abajo (30 minutos).
2. Abre `ejercicios_s01.py` y resuelve los 20 ejercicios en orden.
3. Después de cada ejercicio, corre las pruebas:

```powershell
uv run pytest semana-01-python -x
```

`-x` se detiene en el primer ejercicio que falla. Lee el error de abajo hacia arriba: la última línea dice qué esperaba la prueba y qué devolvió tu función.

4. Haz el reto (`reto_reporte.py`).
5. Responde en voz alta las preguntas de entrevista.
6. Commit y push.

**Diagnóstico:** si resuelves los primeros 11 ejercicios en menos de 2 horas sin buscar nada, vas bien. Haz el resto y adelanta la semana 2. Si te trabas en más de 5, no pasa nada: para eso es esta semana.

## La lección

### 1. Elige bien la estructura

| Estructura | Úsala cuando | Ejemplo |
|---|---|---|
| `list` | El orden importa y hay repetidos | Lecturas de un sensor en el tiempo |
| `tuple` | Es un registro fijo que no cambia | `(15, 35)` como rango permitido |
| `dict` | Buscas por una clave | `{"T-01": 28.6}` |
| `set` | Preguntas "¿está?" o quitas repetidos | Sensores únicos |

Preguntar `x in lista` revisa elemento por elemento. `x in conjunto` es casi instantáneo aunque tenga un millón de elementos. Esa diferencia sale en entrevistas.

### 2. Comprensiones

```python
cuadrados = [x ** 2 for x in range(10)]
pares = [x for x in valores if x % 2 == 0]
por_sensor = {l["sensor"]: l["valor"] for l in lecturas}
total = sum(l["valor"] for l in lecturas)   # generador: no crea una lista intermedia
```

Si una comprensión no cabe en una línea legible, usa un `for` normal.

### 3. Funciones claras

```python
def promedio(valores: list[float]) -> float:
    """Promedio de una lista no vacía."""
    if not valores:
        raise ValueError("No puedo promediar una lista vacía")
    return sum(valores) / len(valores)
```

- Las anotaciones de tipo (`list[float]`, `-> float`) no cambian la ejecución, pero documentan y ayudan al editor.
- Valida al inicio y sal temprano (`raise` o `return`), en vez de anidar `if`.
- Nunca uses una lista como valor por defecto: `def f(x, acumulado=[])` comparte la misma lista entre llamadas. Usa `acumulado=None` y créala adentro.

### 4. Ordenar con `key`

```python
sorted(conteos.items(), key=lambda par: par[1], reverse=True)
max(lecturas, key=lambda l: l["valor"])
sorted(personas, key=lambda p: (-p["edad"], p["nombre"]))   # edad desc, nombre asc
```

`sorted()` devuelve una lista nueva; `lista.sort()` modifica la original y devuelve `None`.

### 5. `collections`: Counter y defaultdict

```python
from collections import Counter, defaultdict

Counter(["a", "b", "a"]).most_common(1)     # [('a', 2)]

grupos = defaultdict(list)
for l in lecturas:
    grupos[l["sensor"]].append(l["valor"])   # no hay que crear la lista antes
```

### 6. Texto

```python
" juan  PÉREZ ".split()           # ['juan', 'PÉREZ']: separa por cualquier espacio
"23,5".replace(",", ".")          # '23.5'
f"{28.6512:.2f}"                  # '28.65'
f"{'T-01':<8}|{3.5:>7.2f}"        # alineado para tablas en la terminal
```

### 7. Archivos con `pathlib` y `csv`

```python
import csv
from pathlib import Path

ruta = Path("semana-01-python") / "datos" / "sensores.csv"
with ruta.open(encoding="utf-8", newline="") as f:
    for fila in csv.DictReader(f):
        print(fila["sensor"], fila["valor"])   # cada fila es un dict de textos
```

`with` cierra el archivo aunque ocurra un error. `Path` funciona igual en Windows y en Linux, que es donde corren los servidores.

### 8. Errores

```python
try:
    valor = float(texto)
except ValueError:
    raise ValueError(f"Valor no numérico: {texto!r}") from None
```

Captura el error específico que esperas. Un `except:` solo esconde los errores que sí quieres ver.

### 9. Clases con `dataclass`

```python
from dataclasses import dataclass

@dataclass
class Punto:
    x: float
    y: float

    def distancia_al_origen(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

Punto(3, 4) == Punto(3, 4)   # True: dataclass compara por campos
```

`@dataclass` escribe por ti `__init__`, `__repr__` y `__eq__`. Un `@classmethod` es un constructor alternativo, por ejemplo `Punto.desde_texto("3,4")`.

### 10. Pruebas con pytest

Una prueba es una función que empieza con `test_` y usa `assert`:

```python
def test_promedio():
    assert promedio([2, 4]) == 3
```

Con decimales usa `pytest.approx`, porque `0.1 + 0.2 == 0.3` es `False` en cualquier lenguaje. Las pruebas de esta semana están en `test_ejercicios_s01.py`: léelas, muestran exactamente qué se espera de cada función.

## El reto: reporte de sensores

Completa `reto_reporte.py` usando tus funciones. El archivo `datos/sensores.csv` simula seis horas de una línea de producción con dos termocuplas, un sensor de vibración y uno de presión.

```powershell
uv run python semana-01-python/reto_reporte.py semana-01-python/datos/sensores.csv
```

Tu salida debe parecerse a esta:

```text
Reporte de sensores · sensores.csv
Lecturas válidas: 23 · descartadas: 1

Sensor  Variable       n   Media     Mín     Máx  Alertas
T-01    temperatura    6   28.65   24.10   36.40        1
T-02    temperatura    5   26.94   25.30   28.10        0
V-01    vibracion      6    2.90    2.10    5.80        1
P-01    presion        6    6.12    5.90    6.30        0

Alertas:
- 2026-10-19T11:00  V-01  vibracion = 5.8 (permitido 0 a 5)
- 2026-10-19T13:00  T-01  temperatura = 36.4 (permitido 15 a 35)
```

**Extra opcional:** agrega una columna con la media móvil de las últimas 3 lecturas de cada sensor, o marca con `*` los valores atípicos según `detectar_atipicos`.

## Preguntas de entrevista

Respóndelas en voz alta, en menos de un minuto cada una. Si no puedes, vuelve a la lección.

1. ¿Qué diferencia hay entre una lista y una tupla? ¿Cuándo usarías cada una?
2. ¿Por qué buscar en un `set` es más rápido que en una `list`?
3. ¿Qué problema tiene `def f(x, datos=[])`?
4. ¿Qué hace `with open(...)` y por qué es mejor que `open()` solo?
5. ¿Cuál es la diferencia entre `sorted(lista)` y `lista.sort()`?
6. Explica una de tus funciones como si se la mostraras a un compañero de trabajo.

## Ruta de empleo de esta semana

Arregla tu perfil de GitHub: foto, nombre real, una línea de bio ("Ingeniero en formación en IA y ciencia de datos · Colombia") y el repositorio `guia-ia-datos` fijado (*pinned*).

## Recursos

- [Documentación oficial de Python en español: el tutorial](https://docs.python.org/es/3/tutorial/), capítulos 4, 5, 7, 8 y 9
- [Kaggle Learn: Python](https://www.kaggle.com/learn/python), si quieres más ejercicios cortos
- [Documentación de pytest: primeros pasos](https://docs.pytest.org/en/stable/getting-started.html)

## Terminado si

- [ ] `uv run pytest semana-01-python` muestra **20 passed**
- [ ] El reto imprime el reporte completo
- [ ] Respondiste las 6 preguntas de entrevista sin mirar
- [ ] Hiciste commit y push, y anotaste la semana en `PROGRESO.md`
- [ ] Marcaste las tareas de la semana 1 en la página del plan
