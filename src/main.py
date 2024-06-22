from data_processing import *
from visualization import *

def ejecutar_ejercicio(ejercicio, funcion, df=None, url=None, mensaje=None, final = None):
    """
    Ejecuta la función correspondiente al ejercicio indicado y espera a que el usuario presione Enter.
    
    Args:
        ejercicio (str): El número del ejercicio.
        funcion (function): La función a ejecutar.
        df (pd.DataFrame, optional): El DataFrame a pasar a la función.
        url (str, optional): La URL a pasar a la función.
        mensaje (str, optional): Mensaje a mostrar antes de continuar.
        
    Returns:
        pd.DataFrame: El DataFrame resultante si la función lo retorna.
        None: Si la función no retorna un DataFrame.
    """
    print(f'\n==============Ejercicio {ejercicio}==============')
    if url and df is not None:
        resultado = funcion(df, url)
    elif url:
        resultado = funcion(url)
    elif df is not None:
        resultado = funcion(df)
    else:
        resultado = funcion()
    
    if mensaje:
        print(mensaje)
        
    if final is None:
        input('Presiona Enter para continuar...')
    
    if isinstance(resultado, pd.DataFrame):
        return resultado
    return None

def main():
    df = ejecutar_ejercicio('1.1', read_csv, url='nics-firearm-background-checks.csv')
    
    df = ejecutar_ejercicio('1.2', clean_csv, df=df)
    
    df = ejecutar_ejercicio('1.3', rename_col, df=df)
    
    df = ejecutar_ejercicio('2.1', breakdown_date, df=df)
    
    df = ejecutar_ejercicio('2.2', erase_month, df=df)
    
    df = ejecutar_ejercicio('3.1', groupby_state_and_year, df=df)
    print(df)
    
    ejecutar_ejercicio('3.2', print_biggest_handguns, df=df)
    
    ejecutar_ejercicio('3.3', print_biggest_longguns, df=df)
    
    ejecutar_ejercicio('4.1', time_evolution, df=df)
    
    mensaje_4_2 = (
        'El gráfico muestra que desde el año 2000 hasta 2016, el número de licencias, pistolas y rifles de asalto aumentó, '
        'alcanzando su pico en 2016. Después de este año, hay una caída notable en todas las categorías, especialmente durante '
        'la pandemia de COVID-19, probablemente debido a las restricciones y medidas de seguridad de ese tiempo.\n'
        'Mirando hacia adelante, es probable que las licencias y ventas de armas se recuperen tras la pandemia, influenciadas por '
        'la economía, cambios en las leyes y cómo la gente percibe la seguridad. En 2017, cuando hubo un gran aumento en la compra '
        'de armas, también se registró un máximo en el número de víctimas de tiroteos masivos, como el trágico tiroteo en Las Vegas, '
        'lo que sugiere que más armas podrían estar relacionadas con más violencia.\n\n'
        'Referencias:\nhttps://ktvz.com/cnn-spanish/2024/02/15/como-se-compara-la-cultura-de-armas-de-estados-unidos-con-el-resto-del-mundo-2/ \n'
        'https://es-us.noticias.yahoo.com/compara-cultura-armas-estados-unidos-130018064.html \n'
        'https://www.elobservador.com.uy/nota/masacre-en-texas-7-graficos-que-explican-la-cultura-de-armas-en-estados-unidos-20225265147 \n'
    )
    ejecutar_ejercicio('4.2', lambda: None, mensaje=mensaje_4_2)
    
    df = ejecutar_ejercicio('5.1', groupby_state, df=df)
    
    df = ejecutar_ejercicio('5.2', clean_states, df=df)
    
    df = ejecutar_ejercicio('5.3', merge_datasets, df=df, url='us-state-populations.csv')
    
    df = ejecutar_ejercicio('5.4', calculate_relative_values, df=df)
    
    ejecutar_ejercicio('5.5', print_kentucky_info, df=df)
    
    ejecutar_ejercicio('6', save_usa_maps, df=df, final=1)

if __name__ == '__main__':
    main()
