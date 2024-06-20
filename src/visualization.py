import folium
import requests
import io
from PIL import Image
import os
import pandas as pd
import matplotlib.pyplot as plt

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
        
        # Create 'images' directory if it doesn't exist
        if not os.path.exists('images'):
            os.makedirs('images')
        
        # Save the plot as PNG
        output_path = os.path.join('images', 'time_evolution_plot.png')
        plt.savefig(output_path)
        
        print(f"Graph saved as: {output_path}")
        
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None

def save_usa_maps(df: pd.DataFrame):
    """
    This function creates choropleth maps for 'permit_perc', 'handgun_perc', and 'longgun_perc',
    and saves them as PNG images.
    
    Args:
        df (pd.DataFrame): The dataframe to be visualized.
    """
    print('Puede tardar unos minutos en ejecutarse...')
    # Paso 2: Descargar el archivo GeoJSON de las fronteras de los estados de EE.UU.
    url = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json"
    state_geo_data = requests.get(url).json()

    # Paso 3: Crear los mapas coropléticos
    def create_choropleth(data, column, geo_data):
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

    # Crear los mapas para cada variable
    m1 = create_choropleth(df, 'permit_perc', state_geo_data)
    m2 = create_choropleth(df, 'handgun_perc', state_geo_data)
    m3 = create_choropleth(df, 'longgun_perc', state_geo_data)

    # Create 'images' directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')

    # Paso 4: Convertir los mapas a imágenes utilizando Folium
    def save_map_as_image(m, image_file):
        img_data = m._to_png(5)
        img = Image.open(io.BytesIO(img_data))
        img.save(image_file)
        print(f'Imagen guardada como {image_file}')

    # Guardar los mapas como imágenes
    save_map_as_image(m1, os.path.join('images', 'image_permit_perc.png'))
    save_map_as_image(m2, os.path.join('images', 'image_handgun_perc.png'))
    save_map_as_image(m3, os.path.join('images', 'image_longgun_perc.png'))
