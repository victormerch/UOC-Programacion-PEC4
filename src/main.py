from data_processing import *
from visualization import *

def main():
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
    print('\n==============Ejercicio 4.2==============')
    print('El gráfico muestra que desde el año 2000 hasta 2016, el número de licencias, pistolas y rifles de asalto aumentó, alcanzando su pico en 2016. Después de este año, hay una caída notable en todas las categorías, especialmente durante la pandemia de COVID-19, probablemente debido a las restricciones y medidas de seguridad de ese tiempo.')
    print('\nMirando hacia adelante, es probable que las licencias y ventas de armas se recuperen tras la pandemia, influenciadas por la economía, cambios en las leyes y cómo la gente percibe la seguridad. En 2017, cuando hubo un gran aumento en la compra de armas, también se registró un máximo en el número de víctimas de tiroteos masivos, como el trágico tiroteo en Las Vegas, lo que sugiere que más armas podrían estar relacionadas con más violencia​.\n')   
    print('Referencias:\nhttps://ktvz.com/cnn-spanish/2024/02/15/como-se-compara-la-cultura-de-armas-de-estados-unidos-con-el-resto-del-mundo-2/ \nhttps://es-us.noticias.yahoo.com/compara-cultura-armas-estados-unidos-130018064.html \nhttps://www.elobservador.com.uy/nota/masacre-en-texas-7-graficos-que-explican-la-cultura-de-armas-en-estados-unidos-20225265147 \n')
     
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

if __name__ == '__main__':
    main()
