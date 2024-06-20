### Ejercicio 1.1. (0.25 puntos)

# Implementad una función llamada *read_csv*:
# - **Inputs:** La función recibirá como datos de entrada un único parámetro que será la url del fichero que queremos leer. 
# - **Funcionalidad:** La función deberá ser capaz de leer el fichero csv *nics-firearm-background-checks.csv*. Para comprobar que se han cargado correctamente esos datos, la función deberá mostrar por pantalla las cinco primeras filas de la base de datos así como su estructura.
# - **Outputs:** La función devolverá el dataframe que se ha leído.
import pandas as pd
from matplotlib import pyplot as plt
import pandas as pd
import folium
import requests
import io
from PIL import Image
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def read_csv(url: str) -> pd.DataFrame:
    """
    This function reads a csv file and displays the first five rows and its structure.
    
    Args:
        url (str): The URL of the csv file to be read.
    
    Returns:
        pd.DataFrame: The dataframe that has been read.
    """
    try:
        if not isinstance(url, str):
            raise ValueError('The URL must be a string.')
        if not url.endswith('.csv'):
            raise ValueError('The URL must be a csv file.')
        path = 'Data/{url}'.format(url=url)
        df = pd.read_csv(path)
        print(df.head())
        print(df.info())
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None
    
    
### Ejercicio 1.2. (0.25 puntos)

# Implementad una función llamada *clean_csv*:
# - **Inputs:** Como datos de entrada la función recibirá la estructura de datos (dataframe). 
# - **Funcionalidad:** La función deberá ser capaz de limpiar el dataset inicial, eliminando todas sus columnas excepto las cinco que utilizaremos a lo largo del ejercicio: *month, state, permit, handgun, long_gun*. Para aseguraros de que la función es correcta, se deberá mostrar por pantalla dentro de la misma el nombre de todas las columnas del dataframe.
# - **Outputs:** La función devolverá el dataframe conteniendo unicamente las columnas *month, state, permit, handgun, long_gun*.


def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function cleans the dataframe by removing all columns except 'month', 'state', 'permit', 'handgun', 'long_gun'.
    
    Args:
        df (pd.DataFrame): The dataframe to be cleaned.
    
    Returns:
        pd.DataFrame: The cleaned dataframe.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The input must be a dataframe.')
        columns = ['month', 'state', 'permit', 'handgun', 'long_gun']
        df = df[columns]
        print(df.columns)
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None


### Ejercicio 1.3. (0.25 puntos)

# Implementad una función llamada *rename_col*:
# - **Inputs:** El dataframe con todas sus columnas. 
# - **Funcionalidad:** La función deberá ser capaz de cambiar el nombre de la columna *longgun* por *long_gun* Para aseguraros de que la función es correcta, nos debemos de asegurar de que esa columna efectivamente existe en el dataframe. Asimismo, deberemos mostrar por pantalla el nombre de todas las columnas del dataframe dentro de la misma función.
# - **Outputs:** La función devolverá el dataframe con el nombre de la columna cambiado.

def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function renames the column 'longgun' to 'long_gun'.
    
    Args:
        df (pd.DataFrame): The dataframe to be modified.
    
    Returns:
        pd.DataFrame: The modified dataframe.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The input must be a dataframe.')
        
        if 'longgun' not in df.columns:
            if 'long_gun' in df.columns:
                print('The column long_gun already exists in the dataframe.')
                print(df.columns)
                return df
            else:
                raise ValueError('The column longgun does not exist in the dataframe.')
        df.rename(columns={'longgun': 'long_gun'}, inplace=True)
        print(df.columns)
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None 
    
    

## Ejercicio 2: Procesamiento de datos (1 punto)

# La información de la columna meses se encuentra en un formato que no es demasiado manejable. Por ejemplo Febrero del año 2020 aparece como *2020-2*. Vamos a solucionar este problema: 

# ### Ejercicio 2.1 (0.5 puntos)

# Implementad una función llamada *breakdown_date*:
# - **Inputs:** La función recibirá el dataframe conteniendo la columna *month* con el formato de datos igual que en el ejemplo. 
# - **Funcionalidad:** La función dividirá la información que hay en la columna *month* creando dos nuevas columnas en el dataframe. Una de ellas llamada *year* y que contendrá el número del año y la otra columna llamada *month*. y que será el número del mes. Siguiendo nuestro ejemplo, para el valor *2020-2* la columna *year* deberá tener el valor **2020** y la columna *month* deberá tener el valor **2**. Para asegurarnos de que la función es correcta, será necesario mostrar las cinco primeras filas del dataframe resultante.
# - **Outputs:** El dataframe con la información de la fecha dividida en las dos columnas.

def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function breaks down the 'month' column into two new columns: 'year' and 'month'.
    
    Args:
        df (pd.DataFrame): The dataframe to be modified.
    
    Returns:
        pd.DataFrame: The modified dataframe.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The input must be a dataframe.')
        df[['year', 'month']] = df['month'].str.split('-', expand=True)
        df['year'] = df['year'].astype(int)
        df['month'] = df['month'].astype(int)
        print(df.head())
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None

### Ejercicio 2.2 (0.5 puntos)

# Implementad una función llamada *erase_month*:
# - **Inputs:** La función recibirá el dataframe conteniendo la columna *month*. 
# - **Funcionalidad:** Eliminar la columna month. Para comprobar que se ha realizado correctamente, la función deberá mostrar por pantalla también las cinco primeras filas de datos y el nombre de todas sus columnas.
# - **Outputs:** El dataframe sin la columna *month*.

def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function removes the 'month' column from the dataframe.
    
    Args:
        df (pd.DataFrame): The dataframe to be modified.
    
    Returns:
        pd.DataFrame: The modified dataframe.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The input must be a dataframe.')
        df.drop(columns=['month'], inplace=True)
        print(df.head())
        print(df.columns)
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None


## Ejercicio 3: Agrupamiento de datos (1 punto)


### Ejercicio 3.1 (0.5 puntos)

# Implementad una función llamada *groupby_state_and_year* 
# - **Inputs:** La función recibirá el dataframe obtenido en el ejercicio 2.2. 
# - **Funcionalidad:** La función deberá ser capaz de calcular los valores acumulados totales agrupando los datos por año y por estado: (columnas *year* y *state*).
# - **Outputs:** El dataframe resultante con los datos agrupados.


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function calculates the total accumulated values grouping the data by year and state.
    
    Args:
        df (pd.DataFrame): The dataframe to be grouped.
    
    Returns:
        pd.DataFrame: The grouped dataframe.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The input must be a dataframe.')
        df = df.groupby(['year', 'state']).sum()
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None



### Ejercicio 3.2 (0.25 puntos)

# Implementad una función llamada *print_biggest_handguns* 
# - **Inputs:** La función recibirá el dataframe con los datos agrupados por estado y por año como resultado del ejercicio 3.1. 
# - **Funcionalidad:** La función deberá imprimir por pantalla un mensaje informativo indicando el nombre del estado y el año en donde se ha registrado un mayor numero de *hand_guns*.
# - **Outputs:** Esta función no devolverá ningún valor.

def print_biggest_handguns(df: pd.DataFrame):
    """
    This function prints the state and year with the highest number of hand guns.
    
    Args:
        df (pd.DataFrame): The dataframe to be analyzed.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The input must be a dataframe.')
        max_handgun = df['handgun'].idxmax()
        print(f'The state with the highest number of hand guns is {max_handgun[1]} in the year {max_handgun[0]}.')
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None

### Ejercicio 3.3 (0.25 puntos)

# Implementad una función llamada *print_biggest_longguns* 
# - **Inputs:** La función recibirá el dataframe con los datos agrupados por estado y por año como resultado del ejercicio 3.1. 
# - **Funcionalidad:** La función deberá imprimir por pantalla un mensaje informativo indicando el nombre del estado y el año en donde se ha registrado un mayor numero de *long_guns*.
# - **Outputs:** Esta función no devolverá ningún valor.

def print_biggest_longguns(df: pd.DataFrame):
    """
    This function prints the state and year with the highest number of long guns.
    
    Args:
        df (pd.DataFrame): The dataframe to be analyzed.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The input must be a dataframe.')
        max_longgun = df['long_gun'].idxmax()
        print(f'The state with the highest number of long guns is {max_longgun[1]} in the year {max_longgun[0]}.')
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None

# ## Ejercicio 4: Análisis temporal (1 punto)

# Para este ejercicio se pedirá hacer un análisis temporal para ver la evolución de las licencias, pistolas y rifles de asalto a lo largo de los años. Para ello será necesario:

# ### Ejercicio 4.1 (0.75 puntos)

# Implementad una función llamada *time_evolution()* que cree un gráfico con las siguientes características:
# - El eje X será el número del año (que en el caso de este dataframe debería variar desde 1998 hasta 2020), mientras que en el eje y se mostrarán tres series temporales con el número total de *permit*, *hand_gun* y *long_gun* registrado por cada uno de los años.
import pandas as pd
import matplotlib.pyplot as plt
import os
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt
import os
import subprocess

def time_evolution(df: pd.DataFrame):
    """
    This function creates a graph with the time evolution of the number of permits, hand guns and long guns,
    saves it as a PNG file, and attempts to open it automatically.
    
    Args:
        df (pd.DataFrame): The dataframe to be analyzed.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The input must be a dataframe.')
        
        # Group by year and sum
        df = df.groupby('year').sum()
        
        # Create the plot
        plt.figure(figsize=(12, 6))
        for column in df.columns:
            plt.plot(df.index, df[column], label=column)
        
        plt.title('Time Evolution of Permits, Hand Guns, and Long Guns')
        plt.xlabel('Year')
        plt.ylabel('Count')
        plt.legend()
        
        # Save the plot as PNG
        output_path = os.path.join(os.getcwd(), 'time_evolution_plot.png')
        plt.savefig(output_path)
        
        print(f"Graph saved as: {output_path}")
        
        # Attempt to open the image file
        try:
            if os.name == 'nt':  # For Windows
                os.startfile(output_path)
            elif os.name == 'posix':  # For macOS and Linux
                subprocess.call(('open', output_path))
            else:
                print("Unable to automatically open the image. Please open it manually.")
        except Exception as e:
            print(f"Unable to automatically open the image: {e}")
            print("Please open the image manually using the path provided above.")
        
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None
# ### Ejercicio 4.2 (0.25 puntos)

# Comenta el gráfico generado en el ejercicio 4.2. ¿Vemos una correlación en las licencias, pistolas y rifles de asalto a lo largo de los años? ¿Es la tendencia ascendente o descendente? ¿Ha habido cambios durante la pandemia? ¿Que podríamos esperar en los próximos años?

# **Nota**: En https://cnnespanol.cnn.com/2024/02/15/cultura-armas-estados-unidos-mundo-trax/ hay una gráfica sobre el número de víctimas de tiroteos masivos. En el 2017 hay un máximo, que parece coincidir con los resultados que habréis obtenido.


# ## Ejercicio 5: Análisis de los estados (1.25 puntos)

# A lo largo de este ejercicio aplicaremos un poco de ciencia de datos y sacaremos una serie de conclusiones agrupando los datos por cada uno de los estados:

# ### Ejercicio 5.1 (0.25 puntos)

# Implementad una función llamada *groupby_state* 
# - **Inputs:** La función recibirá el dataframe con los datos agrupados por estado y por año como resultado del ejercicio 3.1. 
# - **Funcionalidad:** La función mostrará los valores totales agrupando los valores unicamente por estado y no por año. Para comprobar que la función es correcta se pedirá también que muestre por pantalla las 5 primeras filas del dataframe resultante.
# - **Outputs:** Esta función deberá devolver el dataframe con los valores agrupados unicamente por estados.

# **Nota** Los resultados obtenidos en la función del ejercicio 5.1 nos muestran únicamente los valores absolutos. Sin embargo, también hay que tener en cuenta que no todos los estados son igual de poblados. Para establecer una comparación justa, deberíamos de tener en cuenta también la población total de cada estado, para calcular así los valores relativos. Para ello, utilizaremos un nuevo conjunto de datos que hemos obtenido de la siguiente dirección:
# * https://gist.githubusercontent.com/bradoyler/0fd473541083cfa9ea6b5da57b08461c/raw/fa5f59ff1ce7ad9ff792e223b9ac05c564b7c0fe/us-state-populations.csv

def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function calculates the total accumulated values grouping the data by state.
    
    Args:
        df (pd.DataFrame): The dataframe to be grouped.
    
    Returns:
        pd.DataFrame: The grouped dataframe.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The input must be a dataframe.')
        df = df.groupby('state').sum()
        print(df.head())
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None

# ### Ejercicio 5.2 (0.25 puntos)

# Los siguientes estados no aparecen en el archivo *us-state-populations.csv*: Guam, Mariana Islands, Puerto Rico y Virgin Islands. Por tanto, necesitaremos eliminarlos del dataframe para poder continuar con nuestro análisis de datos.

# Implementad una función llamada *clean_states*:
# - **Inputs:** La función recibirá el dataframe con los datos agrupados por estado como resultado del ejercicio 5.1. 
# - **Funcionalidad:** La función primero comprobará si existen esos cuatro estados (Guam, Mariana Islands, Puerto Rico y Virgin Islands) y, en el caso de que existan los eliminará. Para comprobar que la funcionalidad se ha implementado con éxito, la función también mostrará por pantalla el número de estados diferentes.
# - **Outputs:** Esta función devolverá el mismo dataset pero sin los cuatro estados mencionados.

def clean_states(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function removes the states Guam, Mariana Islands, Puerto Rico, and Virgin Islands from the dataframe.
    
    Args:
        df (pd.DataFrame): The dataframe to be modified.
    
    Returns:
        pd.DataFrame: The modified dataframe.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The input must be a dataframe.')
        states_to_remove = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
        for state in states_to_remove:
            if state in df.index:
                df.drop(index=state, inplace=True)
        print(f'The number of different states is: {len(df)}')
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None
# ### Ejercicio 5.3 (0.25 puntos)

# Ahora nuestro objetivo será fusionar los dos datasets:

# Implementad una función llamada *merge_datasets*:
# - **Inputs:** La función recibirá como parámetros de entrada el conjunto de datos resultante del ejercicio ejercicio 5.2 y el conjunto de datos poblacionales provenientes del fichero: *us-state-populations.csv*. (Para leer los datos de la población puedes utilizar la función creada en el ejercicio 1.1).
# - **Funcionalidad:** La función fusionará los datos de los dos datasets recibidos como parámetros de entrada, incluyendo por cada estado toda la información procedente de las dos fuentes de datos. Para comprobar que se ha hecho correctamente, la función imprimirá por pantalla las cinco primeras filas del dataset resultante.
# - **Outputs:** Esta función devolverá el dataset resultante al fusionar los datos.

def merge_datasets(df: pd.DataFrame, url: str) -> pd.DataFrame:
    """
    This function merges the dataframes df and the one read from the URL.
    
    Args:
        df (pd.DataFrame): The first dataframe to be merged.
        url (str): The URL of the second dataframe to be merged.
    
    Returns:
        pd.DataFrame: The merged dataframe.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The first input must be a dataframe.')
        if not isinstance(url, str):
            raise ValueError('The URL must be a string.')
        if not url.endswith('.csv'):
            raise ValueError('The URL must be a csv file.')
        path = 'Data/{url}'.format(url=url)
        df2 = pd.read_csv(path)
        df = pd.merge(df, df2, left_index=True, right_on='state')
        print(df.head())
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None
# ### Ejercicio 5.4 (0.25 puntos)

# A continuación necesitaremos calcular los valores relativos:

# Implementad una función llamada *calculate_relative_values*:
# - **Inputs:** La función recibirá como parámetros de entrada, el conjunto de datos resultante del ejercicio ejercicio 5.3.
# - **Funcionalidad:** La función creará 3 nuevas columnas llamadas *permit_perc*, *longgun_perc* y *handgun_perc* (por si hay algún despistado que se confunda con la regla de tres como ya pasó con la PEC2 os voy a dar una pista, por ejemplo, en el caso de *permit_perc* los valores relativos se calcularían con la fórmula: (permit * 100) / poblacionTotal ).
# - **Outputs:** Esta función devolverá el dataset resultante con las tres columnas nuevas: *permit_perc*, *loggun_perc* y *shotgun_perc* y los valores relativos ya calculados.

def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function calculates the relative values of permit, long gun, and hand gun.
    
    Args:
        df (pd.DataFrame): The dataframe to be modified.
    
    Returns:
        pd.DataFrame: The modified dataframe.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The input must be a dataframe.')
        df['permit_perc'] = (df['permit'] * 100) / df['pop_2014']
        df['longgun_perc'] = (df['long_gun'] * 100) / df['pop_2014']
        df['handgun_perc'] = (df['handgun'] * 100) / df['pop_2014']
        print(df.head())
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None
# ### Ejercicio 5.5 (0.25 puntos)

# 1 - En primer lugar, calcularemos la media de permisos *permit_perc* con dos decimales y mostraremos el resultado en pantalla.
# 2 - En segundo lugar, mostraremos por pantalla toda la información relativa al estado de *Kentucky*.

# **Nota** ¡Tenemos un problema técnico! El estado de *Kentucky* es lo que se llama un *outlier* o valor atípico. Los *outliers* son valores atípicamente altos que distorsionan cualquier tipo de métricas estadísticas. En este caso, la media está inflada debido a los valores que tiene este estado. Los *outliers* no solamente distorsionan las métricas estadísticas, también hacen que algoritmos de aprendizaje máquina lleguen a conclusiones erróneas y eso es un problema.

# 3- Reemplazar el valor *permit_perc* de *Kentucky* con el valor de la media de esta columna.
# 4- Volveremos a calcular la media con dos decimales.
# 5- ¿Ha cambiado mucho el valor? ¿Entiendes el proceso de quitar valores atípicos? Escribe tus conclusiones.

def print_kentucky_info(df: pd.DataFrame):
    """
    This function calculates the average permit percentage with two decimals and shows the information of Kentucky.
    
    Args:
        df (pd.DataFrame): The dataframe to be analyzed.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('The input must be a dataframe.')
        
        # Calculate the average permit percentage with two decimals
        avg_permit_perc = df['permit_perc'].mean()
        print(f'The average permit percentage is: {avg_permit_perc:.2f}')
        
        # Show the information of Kentucky
        kentucky_info = df[df.state == 'Kentucky']
        print('Kentucky information:')
        print(kentucky_info)
        
        # Replace the permit percentage of Kentucky with the average value
        df.loc[df.state == 'Kentucky', 'permit_perc'] = avg_permit_perc
        
        # Calculate the average permit percentage with two decimals again
        avg_permit_perc = df['permit_perc'].mean()
        print(f'The new average permit percentage is: {avg_permit_perc:.2f}')
        
        # Conclusion
        print('The value has changed significantly. Removing outliers is important to avoid distorting the statistics.')
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None
def save_usa_maps(df: pd.DataFrame):
    print('Puede tardar unos minutos en ejecutarse...')
    # Paso 2: Descargar el archivo GeoJSON de las fronteras de los estados de EE.UU.
    url = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json"
    state_geo_data = requests.get(url).json()

    # Paso 3: Crear los mapas coropléticos
    def create_choropleth(data, column, geo_data):
        m = folium.Map(location=[37.8, -96], zoom_start=4)
        # pasar a enteros
        folium.Choropleth(
            geo_data=geo_data,
            name='choropleth',
            data=data,
            columns=['code', column],
            key_on='feature.id',
            fill_color='YlGn',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name=f'{column} (%)'
        ).add_to(m)
        
        return m

    # Crear los mapas para cada variable
    m1 = create_choropleth(df, 'permit_perc', state_geo_data)
    m2 = create_choropleth(df, 'handgun_perc', state_geo_data)
    m3 = create_choropleth(df, 'longgun_perc', state_geo_data)


    # Paso 4: Convertir los mapas a imágenes utilizando Selenium
    def save_map_as_image(m, image_file):
        img_data = m._to_png(5)
        img = Image.open(io.BytesIO(img_data))
        img.save(image_file)
        
        
        print (f'Imagen guardada como {image_file}')

    # Guardar los mapas como imágenes
    save_map_as_image(m1, 'image_permit_perc.png')
    save_map_as_image(m2, 'image_handgun_perc.png')
    save_map_as_image(m3, 'image_longgun_perc.png')
    
if __name__ == '__main__':
    print('==============Ejercicio 1.1==============')
    url = 'nics-firearm-background-checks.csv'
    df = read_csv(url)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 1.2==============')
    df = clean_csv(df)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 1.3==============')
    df = rename_col(df)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 2.1==============')
    df = breakdown_date(df)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 2.2==============')
    df = erase_month(df)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 3.1==============')
    df = groupby_state_and_year(df)
    print(df)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 3.2==============')
    print_biggest_handguns(df)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 3.3==============')
    print_biggest_longguns(df)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 4.1==============')
    time_evolution(df)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 5.1==============')
    df = groupby_state(df)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 5.2==============')
    df = clean_states(df)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 5.3==============')
    url = 'us-state-populations.csv'
    df = merge_datasets(df, url)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 5.4==============')
    df = calculate_relative_values(df)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 5.5==============')
    print_kentucky_info(df)
    
    input('Press Enter to continue...')
    print('\n==============Ejercicio 6==============')
    save_usa_maps(df)