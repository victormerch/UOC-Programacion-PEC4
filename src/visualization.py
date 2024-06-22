import folium
import requests
import io
from PIL import Image
import os
import pandas as pd
import matplotlib.pyplot as plt

def time_evolution(df: pd.DataFrame):
    """
    Esta función crea un gráfico con la evolución temporal del número de permisos, pistolas y rifles,
    lo guarda como un archivo PNG e intenta abrirlo automáticamente.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a analizar.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El input tiene que ser un DataFrame.')
        
        # Agrupar por año y sumar
        df_grouped = df.groupby('year').sum()
        
        # Crear el gráfico
        plt.figure(figsize=(12, 6))
        for column in df_grouped.columns:
            plt.plot(df_grouped.index, df_grouped[column], label=column)
        
        plt.title('Evolución Temporal de Permisos, Pistolas y Rifles')
        plt.xlabel('Año')
        plt.ylabel('Cantidad')
        plt.legend()
        
        # Guardar el gráfico como PNG
        output_path = os.path.join('images', 'time_evolution_plot.png')
        plt.savefig(output_path)
        
        print(f"El gráfico se ha guardado como una imagen en la ruta y con nombre: {output_path}")
        
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')

def create_choropleth(data, column, geo_data):
    """
    Esta función crea un mapa coroplético para una columna específica.
    
    Args:
        data (pd.DataFrame): Los datos que se van a visualizar.
        column (str): La columna que se va a utilizar para el mapa coroplético.
        geo_data (dict): Los datos geográficos en formato GeoJSON.
    
    Returns:
        folium.Map: El mapa coroplético creado.
    """
    m = folium.Map(location=[37.8, -96], zoom_start=4)
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

def save_map_as_image(m, image_file):
    """
    Esta función guarda un mapa de Folium como una imagen PNG.
    
    Args:
        m (folium.Map): El mapa que se va a guardar.
        image_file (str): El archivo de imagen donde se guardará el mapa.
    """
    try:
        img_data = m._to_png(5)
        img = Image.open(io.BytesIO(img_data))
        img.save(image_file)
        print(f'Imagen guardada como {image_file}')
    except Exception as e:
        print(f'No se pudo guardar la imagen como PNG. Error: {e}')
        html_file = image_file.replace('.png', '.html')
        m.save(html_file)
        print(f'El mapa se ha guardado como HTML en lugar de PNG: {html_file}')

def save_usa_maps(df: pd.DataFrame):
    """
    Esta función crea mapas coropléticos para 'permit_perc', 'handgun_perc' y 'longgun_perc',
    y los guarda como imágenes PNG o HTML si no se puede guardar como PNG.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a visualizar.
    """
    print('Puede tardar unos minutos en ejecutarse...')
    
    # Descargar el archivo GeoJSON de las fronteras de los estados de EE.UU.
    url = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json"
    state_geo_data = requests.get(url).json()

    # Crear los mapas para cada variable
    columns = ['permit_perc', 'handgun_perc', 'longgun_perc']
    for column in columns:
        m = create_choropleth(df, column, state_geo_data)
        output_path = os.path.join('images', f'image_{column}.png')
        save_map_as_image(m, output_path)
