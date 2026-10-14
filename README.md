# Guía de estudio · IA y ciencia de datos

**Meta:** conseguir el primer empleo en datos durante 2027, mientras estudio Ingeniería en Inteligencia Artificial y Ciencia de Datos en la UNAD (desde el periodo 16-01 de 2027), con base en lo que ya cursé de Ingeniería Mecatrónica en la UNAL.

El plan completo, con la homologación estimada y casillas para marcar avance, está en la [página del plan](https://claude.ai/artifact/P5arNeNTANLFG3XoqA8c2Z).

## Cómo funciona esta guía

Cada semana tiene su carpeta con tres cosas:

1. **Lección** (`README.md`): lo que necesitas saber, sin relleno, y por qué importa en un trabajo.
2. **Práctica**: ejercicios con pruebas automáticas (`uv run pytest semana-XX -x`) o un proyecto con criterios claros de "terminado".
3. **Ruta de empleo**: una tarea pequeña para que en febrero tengas portafolio, CV y perfil listos.

Las semanas se preparan una a la vez, según cómo te fue en la anterior. Cuando termines una, abre esta carpeta en Claude Code y escribe:

> Revisa mi semana 1 y prepara la semana 2.

Claude revisa tu código, te dice qué mejorar y arma la siguiente semana ajustada a tu nivel.

### Rutina semanal (unas 10 horas)

| Día | Tiempo | Qué hacer |
|---|---|---|
| Lunes | 1,5 h | Leer la lección y empezar la práctica |
| Martes a jueves | 1,5 h | Práctica |
| Sábado | 4 h | Reto o proyecto, preguntas de entrevista y tarea de empleo |
| Viernes y domingo | — | Descanso |

Al cierre de cada sesión: `git add .`, `git commit -m "..."`, `git push`. Al cierre de cada semana: anota en [PROGRESO.md](PROGRESO.md) y marca las casillas en la página del plan.

## Mapa de semanas

| Semana | Fechas | Tema | Entregable | Estado |
|---|---|---|---|---|
| [S0](semana-00-entorno/) | 14 – 18 oct | Entorno de trabajo | Repositorio en GitHub | Lista |
| [S1](semana-01-python/) | 19 – 25 oct | Python sólido para datos | 20 ejercicios y reporte de sensores | Lista |
| S2 | 26 oct – 1 nov | pandas a nivel profesional | Análisis de un dataset de datos.gov.co | Se prepara al terminar S1 |
| S3 | 2 – 8 nov | Limpieza y visualización | **Proyecto 1:** análisis exploratorio | |
| S4 | 9 – 15 nov | SQL básico | Base PostgreSQL con tus datos | |
| S5 | 16 – 22 nov | SQL intermedio | LeetCode SQL 50, primera mitad | |
| S6 | 23 – 29 nov | Modelado de datos | **Proyecto 2:** SQL y tablero en Power BI | |
| S7 | 30 nov – 6 dic | Álgebra lineal para ML | Compresión de imágenes con SVD | |
| S8 | 7 – 13 dic | Cálculo para ML | Descenso de gradiente desde cero | |
| S9 | 14 – 20 dic | Probabilidad e inferencia | Prueba A/B | |
| S10 | 21 – 27 dic | Primeros modelos de ML | Regresión y clasificación | |
| — | 28 dic – 3 ene | Receso | — | |
| S11 | 4 – 10 ene | scikit-learn | Pipeline con validación cruzada | |
| S12 | 11 – 17 ene | Árboles, boosting y Kaggle | Primera entrega en Kaggle | |
| S13 | 18 – 24 ene | Mantenimiento predictivo | **Proyecto 3:** modelo de fallas | |
| S14 | 25 – 31 ene | Despliegue y hoja de vida | App en Streamlit, CV y LinkedIn | |
| S15 | 1 – 7 feb | Inicio UNAD | Primeras postulaciones | |

Tus notebooks del curso de marzo y abril (Spotify, Movies, Food) son materia prima: en la semana 3 puedes convertir uno de ellos en el Proyecto 1 en vez de empezar de cero.

## Ruta de empleo

El primer objetivo realista es **analista de datos o analista BI junior**: es el rol con más vacantes y piden justo lo que vas a tener en febrero (SQL, Python, Power BI, estadística y saber explicar resultados). Desde ahí se sube a científico de datos o ingeniero de ML. Tu diferencial: entiendes máquinas, sensores y procesos industriales.

| Semana | Tarea |
|---|---|
| S1 | Perfil de GitHub con foto, bio y este repositorio fijado |
| S2 | Anotar 20 vacantes junior en [empleo/vacantes.csv](empleo/) |
| S3 | Analizar esas vacantes con pandas: qué habilidades piden más |
| S4 | LinkedIn: titular, sección "Acerca de" y foto |
| S5 | Seguir 15 empresas que contratan perfiles de datos en Colombia |
| S6 | CV de una página en español con los proyectos 1 y 2 |
| S7 – S9 | 30 minutos por semana de preguntas de entrevista de SQL y estadística |
| S10 | CV en inglés |
| S11 | Unirte a una comunidad de Python o datos y asistir a un encuentro virtual |
| S12 | Publicar en LinkedIn un post corto sobre tu Proyecto 2 |
| S13 | Ensayar la explicación de un proyecto en 3 minutos |
| S14 | Lista de 30 empresas objetivo y primeras 5 postulaciones |
| S15 en adelante | 5 postulaciones por semana |

**Cuándo renunciar:** cuando tengas una oferta firmada, no antes. Mientras tanto, busca un problema de datos en tu trabajo actual (un reporte manual, tiempos, una base desordenada) y resuélvelo con lo que aprendas. Eso cuenta como experiencia real en tu CV.

## Reglas de la guía

1. **Escribe tú el código.** Usa a Claude como tutor: pide pistas, explicaciones o revisión de un intento tuyo. En una prueba técnica no vas a tener ayuda, y el empleador lo nota en cinco minutos.
2. **No saltes las bases.** Si te atrasas, mueve el calendario; no te saltes SQL ni matemáticas.
3. **Explica en voz alta.** Si no puedes explicar algo en un minuto, todavía no lo sabes.
4. **Commits pequeños y frecuentes.** Tu historial en GitHub también es parte del portafolio.
5. **Descansa.** El receso de diciembre está en el plan a propósito.

## Estructura

```text
guia-ia-datos/
├── README.md              esta guía
├── PROGRESO.md            tu bitácora semanal
├── pyproject.toml         librerías del proyecto (uv sync)
├── empleo/                vacantes y material para postular
├── semana-00-entorno/     instalación y verificación
└── semana-01-python/      lección, ejercicios, pruebas y reto
```
