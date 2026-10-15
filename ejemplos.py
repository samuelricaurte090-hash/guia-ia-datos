personas = [
    {"nombre": "Laura",  "edad": 25},
    {"nombre": "Andrés", "edad": 31},
    {"nombre": "Camila", "edad": 25},
    {"nombre": "Bruno",  "edad": 31},
]

print(sorted(personas, key=lambda p: (-p["edad"], p["nombre"])))
