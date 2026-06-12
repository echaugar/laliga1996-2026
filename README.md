# LaLiga 1996-2026

Análisis estadístico y científico de la liga española de fútbol profesional (LaLiga) desde la temporada 1996-97 hasta 2025-26. Este proyecto implementa 7 ejercicios de análisis de datos con visualizaciones y validación rigurosa del código.

**Autor:** Eric Chaume García

**Licencia:** MIT

# Descprición del proyecto
Este proyecto realiza un análisis exhaustivo de las temporadas de LaLiga a lo largo de 30 años, incluyendo:

- Análisis exploratorio (EDA): estadísticas descriptivas y distribuciones de goles. (Ejs. 1 y 3)
- Rendimiento de equipos: partidos jugados, victorias, empates y derrotas (Ej. 2)
- Acumulación de puntos: cálculo de clasificaciones finales (Ej. 5)
- Análisis de resultados: estudio de patrones en partidos de la liga finalizados FTR (Full-Time Result) (Ej. 4)
- Visualizaciones avanzadas: gráficos comparativos, podiums, y análisis de conectividad entre equipos (Ejs. 6 y 7)


## Estructura del proyecto

```
laliga1996-2026/
├── doc/                           # Documentación generada con Pydoc
├── screenshots/                   # Capturas de pantalla (Aquí se comprueba mi autoría de la PEC)
├── src/
│   ├── main.py                    # Ejecución de prints y gráficas
│   ├── exercises/                 # Definición funciones requeridas
│   │   └──  ex1.py ... ex7.py 
│   ├── data/
│   │   └── LaLiga_Matches.csv     # Dataset con información sobre todos los partidos jugados, permitiendo análisis tanto a nivel agregado como por temporada.
│   └── Img                        # Gráficas guardadas en .png
├── tests/                         # Tests unitarios
│   ├── fun_total_goals            # Test Ej. 6
│   └── test_puntos_por_resultado  # Test Ej. 5
├── LICENSE                        # Fichero de licencia
├── README.md                      # Información
└── requirements.txt               # Librerías necesarias
```

## Instalación

Las librerías necesarias del proyecto aparecen en `requirements.txt`:

```
pandas: procesamiento y manipulación de datos
matplotlib: generación de gráficos
numpy: cálculos numéricos
networkx: análisis de redes/grafos
```

Instalarlas en la consola de Pycharm con:

```bash
pip install -r requirements.txt
```

## Licencia

Este proyecto se distribuye bajo la licencia **MIT**. Consulta el fichero [LICENSE](LICENSE) para más detalles.

---

## Comprobación del análisis estático: Pylint

El código sigue la guía de estilo PEP8. Para comprobarlo se utiliza **pylint**.

### Cómo ejecutar el linting

Desde la raíz del proyecto:

```bash
pylint src/exercises/*.py src/main.py
```

Para generar un informe detallado:

```bash
pylint src/exercises/*.py src/main.py --output-format=text
```

### Resultado de Pylint

La comprobación realizada sobre el proyecto obtiene una puntuación de **9.15/10**. La siguiente captura de la terminal lo muestra:

![Resultado pylint](screenshots/Análisis_estático_con_Pylint.png)

---

## Generación de la documentación: Pydoc

La documentación del proyecto se genera automáticamente a partir de los docstrings de cada módulo utilizando **pydoc**.

### Cómo generar la documentación

Para generar la documentación se debe ejecutar el siguiente comando en la terminal Windows desde el directorio /src del proyecto:

```bash
python -m pydoc -w main exercises.ex1 exercises.ex2 exercises.ex3 exercises.ex4 exercises.ex5 exercises.ex6 exercises.ex7
```

Los archivos HTML generados se guardan en la carpeta `doc/`:

| Archivo                    | Módulo                           |
| -------------------------- | --------------------------------- |
| `doc/main.html`          | Módulo principal                 |
| `doc/exercises.ex1.html` | EDA y visualización de goles     |
| `doc/exercises.ex2.html` | Total de partidos por equipo      |
| `doc/exercises.ex3.html` | Distribución de goles            |
| `doc/exercises.ex4.html` | Análisis de resultados (FTR)     |
| `doc/exercises.ex5.html` | Puntos totales por equipo         |
| `doc/exercises.ex6.html` | Goles por equipo y podium         |
| `doc/exercises.ex7.html` | Grafo de nodos de conexiones entre equipos |

Los archivos HTML generados con Pydoc se basan en los docstrings definidos para cada función puesto que no hay un docstring general para cada script.

La siguiente captura muestra la ejecución de Pydoc desde la terminal integrada de Pycharm:

![Resultado Pytest](screenshots/Pydoc.png)

Además, a modo de ejemplo, se muestra una captura de la página web "main.html" abierta con el navegador Chrome.

![Resultado Pytest](screenshots/Pydoc_2.png)

---

## Comprobación de los tests

El proyecto incluye pruebas unitarias para validar funciones críticas usando Pytest.


### Cómo ejecutar los tests

Desde la raíz del proyecto:

```bash
pytest tests/ -v
```

Para ejecutar únicamente el test del ejercicio 6:

```bash
pytest tests/test_ex6.py -v
```

### Descripción de los tests

Los tests están implementados con `unittest.TestCase` y son compatibles con pytest.

| Test                                         | Función                    | Descripción                                                                   |
| -------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------ |
| `TestFunTotalGoals::test_goles_correctos`  | `fun_total_goals` (ej. 6) | Verifica que los goles locales, visitantes y totales se calculan correctamente |
| `TestAddPoints::test_puntos_por_resultado` | `add_points` (ej. 5)      | Verifica que se asignan (puntos_local/puntos_visitante) 3/0 en victoria, 1/1 en empate y 0/3 en derrota    |

Captura de la ejecución de los tests:

![Resultado Pytest](screenshots/Unittest.png)

Se observa que las pruebas son con datos de juguete para simplemente corroborar que las funciones funcionan correctamente.

## Subir el proyecto a GitHub

```bash
# 1. Inicializar el repositorio (solo la primera vez)
git init
git remote add origin https://github.com/echaugar/laliga1996-2026.git

# 2. Añadir los ficheros y hacer el primer commit
git add .
git commit -m "Initial commit"

# 3. Subir al repositorio remoto
git push -u origin main
```

## Ejecución

Para ejecutar el archivo se puede acceder a la terminal y ejecutar el siguiente comando:

```bash
python src/main.py
```