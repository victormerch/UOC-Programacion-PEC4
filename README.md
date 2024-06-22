# Programación para la ciencia de datos - PEC4 0 - Proyecto de Análisis de Datos y Visualización

Este proyecto realiza un análisis de datos de comprobaciones de antecedentes de armas de fuego en EE.UU. y genera visualizaciones coropléticas y gráficos de evolución temporal.

## Requisitos

### Opcion 1: Usando requirements.txt

1. Crear el entorno virtual

   Usa `venv` para crear un nuevo entorno virtual llamado `env`.

```bash
   python -m venv env
```

2. Activar entorno virtual

   - En Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - En macOS y Linux:
     ```bash
     source env/bin/activate
     ```
3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### Opcion 2: Usando setup.py

1. Crear el entorno virtual

   Usa `venv` para crear un nuevo entorno virtual llamado `env`.

```bash
   python -m venv env
```

2. Instalar el paquete y sus dependencias usando setup.py:

```bash
pip install .
```

Esta opción instalará tu paquete y las dependencias especificadas en el archivo setup.py.

## Ejecución

Para ejecutar el proyecto, simplemente ejecuta el archivo `main.py`:

- En Windows:

  ```bash
  python src/main.py
  ```
- En macOS y Linux:

  ```bash
  python3 src/main.py
  ```

## Funcionamiento

Cada ejercicio se mostrará secuencialmente en la pantalla, proporcionando la salida correspondiente a medida que se ejecuta. Para facilitar la revisión y asegurar que el usuario pueda observar los resultados detalladamente, se incluirá una pausa después de cada ejercicio. Esta pausa requerirá que el usuario presione la tecla "Enter" para continuar y proceder con la visualización del siguiente ejercicio. Esta interacción permite un control más cómodo del flujo del programa y asegura que el usuario tenga el tiempo necesario para analizar cada paso antes de avanzar.

## Descripción

### Procesamiento de Datos

* **`read_csv(url: str) -> pd.DataFrame`** : Esta función lee un archivo CSV y muestra las primeras cinco filas y su estructura.
* **`clean_csv(df: pd.DataFrame) -> pd.DataFrame`** : Esta función limpia el DataFrame eliminando todas las columnas excepto 'month', 'state', 'permit', 'handgun', 'long_gun'.
* **`rename_col(df: pd.DataFrame) -> pd.DataFrame`** : Esta función renombra la columna 'longgun' a 'long_gun'.
* **`breakdown_date(df: pd.DataFrame) -> pd.DataFrame`** : Esta función divide la columna 'month' en dos nuevas columnas: 'year' y 'month'.
* **`erase_month(df: pd.DataFrame) -> pd.DataFrame`** : Esta función elimina la columna 'month' del DataFrame.
* **`groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame`** : Esta función agrupa los datos por año y estado y calcula los valores acumulados totales.
* **`print_biggest_handguns(df: pd.DataFrame)`** : Esta función imprime el estado y año con el mayor número de pistolas.
* **`print_biggest_longguns(df: pd.DataFrame)`** : Esta función imprime el estado y año con el mayor número de rifles de asalto.
* **`groupby_state(df: pd.DataFrame) -> pd.DataFrame`** : Esta función agrupa los datos únicamente por estado y calcula los valores acumulados totales.
* **`clean_states(df: pd.DataFrame) -> pd.DataFrame`** : Esta función elimina los estados Guam, Mariana Islands, Puerto Rico y Virgin Islands del DataFrame.
* **`merge_datasets(df: pd.DataFrame, url: str) -> pd.DataFrame`** : Esta función fusiona el DataFrame dado con otro DataFrame leído desde la URL proporcionada.
* **`calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame`** : Esta función calcula los valores relativos de permisos, pistolas y rifles de asalto.
* **`print_kentucky_info(df: pd.DataFrame)`** : Esta función imprime información sobre el estado de Kentucky y reemplaza el valor atípico de permisos con la media.

### Visualización

* **`time_evolution(df: pd.DataFrame)`** : Esta función crea un gráfico con la evolución temporal del número de permisos, pistolas y rifles de asalto.
* **`save_usa_maps(df: pd.DataFrame)`** : Esta función crea mapas coropléticos para 'permit_perc', 'handgun_perc' y 'longgun_perc', y los guarda como imágenes PNG.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```css
.
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── data/
│   └── us-state-populations.csv
├── images/
└── src/
    ├── __init__.py
    ├── main.py
    ├── data_processing.py
    ├── visualization.py
└── tests/
    ├── __init__.py
    └── test_functions.py
```

### main.py

Este archivo es el punto de entrada del programa. Importa funciones de los otros módulos y ejecuta las tareas principales.

### data_processing.py

Este archivo contiene todas las funciones de procesamiento de datos con sus respectivos docstrings.

### visualization.py

Este archivo contiene todas las funciones de visualización.

### test_functions.py

Este archivo contiene pruebas unitarias para verificar que las funciones funcionan correctamente.

## Pruebas

Para ejecutar las pruebas unitarias, usa el siguiente comando:

- En Windows:

  ```bash
  python -m unittest discover -s test
  ```
- En macOS y Linux:

  ```bash
  python3 -m unittest discover -s test
  ```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
