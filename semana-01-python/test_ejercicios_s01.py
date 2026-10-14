"""Pruebas de la semana 1. No las modifiques: tu código es el que debe pasar.

Correr todo:            uv run pytest semana-01-python -x
Correr un ejercicio:    uv run pytest semana-01-python -k ej07
"""

from dataclasses import is_dataclass
from pathlib import Path

import pytest

from ejercicios_s01 import (
    Lectura,
    agrupar_por,
    aplanar,
    celsius_a_fahrenheit,
    contar_alertas,
    contar_pares,
    detectar_atipicos,
    elementos_comunes,
    es_palindromo,
    estadisticas,
    frecuencias,
    invertir_diccionario,
    leer_lecturas,
    media_movil,
    normalizar_min_max,
    normalizar_nombre,
    parsear_lectura,
    promedio,
    resumen_por_sensor,
    top_n,
)

CSV = Path(__file__).parent / "datos" / "sensores.csv"
LIMITES = {"temperatura": (15, 35), "vibracion": (0, 5), "presion": (5.5, 7.0)}


# Nivel 1 ------------------------------------------------------------------

def test_ej01_celsius_a_fahrenheit():
    assert celsius_a_fahrenheit(100) == pytest.approx(212)
    assert celsius_a_fahrenheit(0) == pytest.approx(32)
    assert celsius_a_fahrenheit(-40) == pytest.approx(-40)
    assert celsius_a_fahrenheit(36.6) == pytest.approx(97.88)


def test_ej02_promedio():
    assert promedio([2, 4, 6]) == pytest.approx(4)
    assert promedio([1.5]) == pytest.approx(1.5)
    with pytest.raises(ValueError):
        promedio([])


def test_ej03_contar_pares():
    assert contar_pares([1, 2, 3, 4, 0]) == 3
    assert contar_pares([-2, -1, 7]) == 1
    assert contar_pares([]) == 0


def test_ej04_normalizar_nombre():
    assert normalizar_nombre("  juan   PÉREZ ") == "Juan Pérez"
    assert normalizar_nombre("maría josé\tgómez") == "María José Gómez"
    assert normalizar_nombre("ANA") == "Ana"


def test_ej05_es_palindromo():
    assert es_palindromo("Anita lava la tina") is True
    assert es_palindromo("A man, a plan, a canal: Panama") is True
    assert es_palindromo("Python") is False
    assert es_palindromo("") is True


# Nivel 2 ------------------------------------------------------------------

def test_ej06_frecuencias():
    assert frecuencias(["Hola", "hola", "mundo"]) == {"hola": 2, "mundo": 1}
    assert frecuencias([]) == {}
    assert frecuencias(["a", "B", "b"]) == {"a": 1, "b": 2}


def test_ej07_top_n():
    conteos = {"a": 3, "b": 5, "c": 3, "d": 1}
    assert top_n(conteos, 2) == [("b", 5), ("a", 3)]
    assert top_n(conteos, 3) == [("b", 5), ("a", 3), ("c", 3)]
    assert top_n(conteos, 10) == [("b", 5), ("a", 3), ("c", 3), ("d", 1)]
    assert top_n({}, 3) == []


def test_ej08_invertir_diccionario():
    sensores = {"V-01": "vibracion", "T-02": "temperatura", "T-01": "temperatura"}
    assert invertir_diccionario(sensores) == {
        "temperatura": ["T-01", "T-02"],
        "vibracion": ["V-01"],
    }
    assert invertir_diccionario({}) == {}


def test_ej09_elementos_comunes():
    assert elementos_comunes([3, 1, 2, 2], [2, 3, 4]) == [2, 3]
    assert elementos_comunes(["T-01", "P-01"], ["V-01"]) == []


def test_ej10_agrupar_por():
    registros = [{"s": "A", "v": 1}, {"s": "B", "v": 2}, {"s": "A", "v": 3}]
    grupos = agrupar_por(registros, "s")
    assert dict(grupos) == {
        "A": [{"s": "A", "v": 1}, {"s": "A", "v": 3}],
        "B": [{"s": "B", "v": 2}],
    }
    assert dict(agrupar_por([], "s")) == {}


def test_ej11_aplanar():
    assert aplanar([[1, 2], [3], []]) == [1, 2, 3]
    assert aplanar([]) == []
    assert aplanar([["a"], ["b", "c"]]) == ["a", "b", "c"]


# Nivel 3 ------------------------------------------------------------------

def test_ej12_media_movil():
    assert media_movil([1, 2, 3, 4, 5], 2) == pytest.approx([1.5, 2.5, 3.5, 4.5])
    assert media_movil([1, 2, 3, 4, 5], 5) == pytest.approx([3.0])
    assert media_movil([4, 8], 1) == pytest.approx([4.0, 8.0])
    with pytest.raises(ValueError):
        media_movil([1, 2, 3], 0)
    with pytest.raises(ValueError):
        media_movil([1, 2, 3], 4)


def test_ej13_estadisticas():
    e = estadisticas([2, 4, 4, 6])
    assert e["n"] == 4
    assert e["min"] == 2
    assert e["max"] == 6
    assert e["media"] == pytest.approx(4.0)
    assert e["mediana"] == pytest.approx(4.0)
    assert e["desviacion"] == pytest.approx(1.632993, rel=1e-5)

    impar = estadisticas([7, 1, 3])
    assert impar["mediana"] == pytest.approx(3.0)
    assert impar["desviacion"] == pytest.approx(3.05505, rel=1e-5)

    assert estadisticas([5])["desviacion"] == pytest.approx(0.0)
    with pytest.raises(ValueError):
        estadisticas([])


def test_ej14_detectar_atipicos():
    valores = [10] * 9 + [50]
    assert detectar_atipicos(valores, z=2.0) == [9]
    assert detectar_atipicos(valores) == []
    assert detectar_atipicos([3, 3, 3]) == []
    assert detectar_atipicos([1, 50, 1, 1, 1, 1, 1, 1, 1, 1], z=2.5) == [1]


def test_ej15_normalizar_min_max():
    assert normalizar_min_max([2, 4, 6]) == pytest.approx([0.0, 0.5, 1.0])
    assert normalizar_min_max([10, 0, 5]) == pytest.approx([1.0, 0.0, 0.5])
    assert normalizar_min_max([3, 3]) == [0.0, 0.0]
    assert normalizar_min_max([]) == []


def test_ej16_parsear_lectura():
    assert parsear_lectura("2026-10-19T08:00;T-01;temperatura;23,5") == {
        "fecha": "2026-10-19T08:00",
        "sensor": "T-01",
        "variable": "temperatura",
        "valor": 23.5,
    }
    assert parsear_lectura(" 2026-10-19T09:00 ; P-01 ; presion ; 6.1 ")["valor"] == pytest.approx(6.1)
    assert parsear_lectura("2026-10-19T09:00;P-01;presion;-2")["valor"] == pytest.approx(-2.0)
    with pytest.raises(ValueError):
        parsear_lectura("2026-10-19T08:00;T-01;temperatura")
    with pytest.raises(ValueError):
        parsear_lectura("2026-10-19T08:00;T-01;temperatura;alto")


# Nivel 4 ------------------------------------------------------------------

def test_ej17_leer_lecturas():
    lecturas = leer_lecturas(CSV)
    assert len(lecturas) == 23
    assert lecturas[0] == {
        "fecha": "2026-10-19T08:00",
        "sensor": "T-01",
        "variable": "temperatura",
        "valor": 24.1,
    }
    assert all(isinstance(l["valor"], float) for l in lecturas)
    assert len(leer_lecturas(str(CSV))) == 23


def test_ej18_resumen_por_sensor():
    resumen = resumen_por_sensor(leer_lecturas(CSV))
    assert set(resumen) == {"T-01", "T-02", "V-01", "P-01"}
    assert resumen["T-01"]["n"] == 6
    assert resumen["T-01"]["media"] == pytest.approx(28.65)
    assert resumen["T-01"]["min"] == pytest.approx(24.1)
    assert resumen["T-01"]["max"] == pytest.approx(36.4)
    assert resumen["T-02"]["n"] == 5
    assert resumen["T-02"]["media"] == pytest.approx(26.94)
    assert resumen["V-01"]["max"] == pytest.approx(5.8)
    assert resumen["P-01"]["media"] == pytest.approx(36.7 / 6)


def test_ej19_lectura():
    assert is_dataclass(Lectura), "Usa el decorador @dataclass"
    l = Lectura(fecha="2026-10-19T13:00", sensor="T-01", variable="temperatura", valor=36.4)
    assert l.fuera_de_rango(15, 35) is True
    assert l.fuera_de_rango(15, 40) is False
    assert Lectura("f", "s", "v", 35.0).fuera_de_rango(15, 35) is False
    assert Lectura("f", "s", "v", 15.0).fuera_de_rango(15, 35) is False

    d = {"fecha": "2026-10-19T08:00", "sensor": "P-01", "variable": "presion", "valor": "6.2"}
    desde = Lectura.desde_dict(d)
    assert desde == Lectura("2026-10-19T08:00", "P-01", "presion", 6.2)
    assert isinstance(desde.valor, float)


def test_ej20_contar_alertas():
    lecturas = leer_lecturas(CSV)
    assert contar_alertas(lecturas, LIMITES) == {"T-01": 1, "T-02": 0, "V-01": 1, "P-01": 0}
    solo_temp = contar_alertas(lecturas, {"temperatura": (25, 30)})
    assert solo_temp == {"T-01": 4, "T-02": 0, "V-01": 0, "P-01": 0}
