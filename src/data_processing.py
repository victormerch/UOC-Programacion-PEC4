import pandas as pd

def read_csv(url: str) -> pd.DataFrame:
    """
    Esta función lee un archivo csv y muestra las primeras cinco filas y su estructura.
    
    Args:
        url (str): La URL del archivo csv que se va a leer.
    
    Returns:
        pd.DataFrame: El dataframe que se ha leído.
    """
    try:
        if not isinstance(url, str):
            raise ValueError('La variable url tiene que ser de tipo string.')
        if not url.endswith('.csv'):
            raise ValueError('La url tiene que ser de tipo .csv')
        path = f'Data/{url}'
        df = pd.read_csv(path)
        print(df.head())
        print(df.info())
        return df
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None

def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función limpia el dataframe eliminando todas las columnas excepto 'month', 'state', 'permit', 'handgun', 'long_gun'.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a limpiar.
    
    Returns:
        pd.DataFrame: El dataframe limpio.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El input tiene que ser de tipo DataFrame')
        columns = ['month', 'state', 'permit', 'handgun', 'long_gun']
        df = df[columns]
        print(df.columns)
        return df
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None

def rename_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función renombra la columna 'long_gun' a 'longgun'.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a modificar.
    
    Returns:
        pd.DataFrame: El dataframe modificado.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El input tiene que ser de tipo DataFrame')
        
        if 'long_gun' not in df.columns:
            if 'longgun' in df.columns:
                print('La columna longgun ya existe en el dataframe.')
                print(df.columns)
                return df
            else:
                raise ValueError('La columna long_gun no existe en el dataframe.')
        df.rename(columns={'long_gun': 'longgun'}, inplace=True)
        print(df.columns)
        return df
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None 

def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función desglosa la columna 'month' en dos nuevas columnas: 'year' y 'month'.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a modificar.
    
    Returns:
        pd.DataFrame: El dataframe modificado.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El input tiene que ser de tipo DataFrame')
        df[['year', 'month']] = df['month'].str.split('-', expand=True)
        df['year'] = df['year'].astype(int)
        df['month'] = df['month'].astype(int)
        print(df.head())
        return df
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None

def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función elimina la columna 'month' del dataframe.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a modificar.
    
    Returns:
        pd.DataFrame: El dataframe modificado.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El input tiene que ser de tipo DataFrame')
        df.drop(columns=['month'], inplace=True)
        print(df.head())
        print(df.columns)
        return df
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None

def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función calcula los valores acumulados totales agrupando los datos por año y estado.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a agrupar.
    
    Returns:
        pd.DataFrame: El dataframe agrupado.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El input tiene que ser de tipo DataFrame')
        df = df.groupby(['year', 'state']).sum().reset_index().set_index(['year', 'state'])
        return df
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None

def print_biggest_handguns(df: pd.DataFrame):
    """
    Esta función imprime el estado y el año con el mayor número de pistolas.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a analizar.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El input tiene que ser de tipo DataFrame')
        max_handgun = df['handgun'].idxmax()
        print(f'El estado con el mayor número de pistolas es {max_handgun[1]} en el año {max_handgun[0]}.')
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None

def print_biggest_longguns(df: pd.DataFrame):
    """
    Esta función imprime el estado y el año con el mayor número de rifles.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a analizar.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El input tiene que ser de tipo DataFrame')
        max_longgun = df['longgun'].idxmax()
        print(f'El estado con el mayor número de rifles es {max_longgun[1]} en el año {max_longgun[0]}.')
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None

def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función calcula los valores acumulados totales agrupando los datos por estado.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a agrupar.
    
    Returns:
        pd.DataFrame: El dataframe agrupado.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El input tiene que ser de tipo DataFrame')
        df = df.groupby('state').sum()
        print(df.head())
        return df
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None

def clean_states(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función elimina los estados Guam, Islas Marianas, Puerto Rico y las Islas Vírgenes del dataframe.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a modificar.
    
    Returns:
        pd.DataFrame: El dataframe modificado.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El input tiene que ser de tipo DataFrame')
        states_to_remove = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
        for state in states_to_remove:
            if state in df.index:
                df.drop(index=state, inplace=True)
        print(f'El número de diferentes estados es: {len(df)}')
        return df
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None

def merge_datasets(df: pd.DataFrame, url: str) -> pd.DataFrame:
    """
    Esta función fusiona los dataframes df y el que se lee de la URL.
    
    Args:
        df (pd.DataFrame): El primer dataframe que se va a fusionar.
        url (str): La URL del segundo dataframe que se va a fusionar.
    
    Returns:
        pd.DataFrame: El dataframe fusionado.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El primer input tiene que ser de tipo DataFrame.')
        if not isinstance(url, str):
            raise ValueError('La URL tiene que ser de tipo string.')
        if not url.endswith('.csv'):
            raise ValueError('La URL tiene que ser de tipo .csv.')
        
        df2 = read_csv(url)
        df2['state'] = df2['state'].astype(str)
        df = pd.merge(df, df2, on='state', how='left')
        print(df.head())
        return df
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None


def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función calcula los valores relativos de permisos, rifles y pistolas.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a modificar.
    
    Returns:
        pd.DataFrame: El dataframe modificado.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El input tiene que ser de tipo DataFrame.')
        df['permit_perc'] = (df['permit'] * 100) / df['pop_2014']
        df['longgun_perc'] = (df['longgun'] * 100) / df['pop_2014']
        df['handgun_perc'] = (df['handgun'] * 100) / df['pop_2014']
        print(df.head())
        return df
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None

def print_kentucky_info(df: pd.DataFrame):
    """
    Esta función calcula el porcentaje promedio de permisos con dos decimales y muestra la información de Kentucky.
    
    Args:
        df (pd.DataFrame): El dataframe que se va a analizar.
    """
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError('El input tiene que ser de tipo DataFrame.')
        
        # Calcular el porcentaje promedio de permisos con dos decimales
        avg_permit_perc = df['permit_perc'].mean()
        print(f'El porcentaje promedio de permisos es: {avg_permit_perc:.2f}')
        
        # Mostrar la información de Kentucky
        kentucky_info = df[df.state == 'Kentucky']
        print('Información de Kentucky:')
        print(kentucky_info)
        
        # Reemplazar el porcentaje de permisos de Kentucky con el valor promedio
        df.loc[df.state == 'Kentucky', 'permit_perc'] = avg_permit_perc
        
        # Calcular el porcentaje promedio de permisos con dos decimales nuevamente
        avg_permit_perc = df['permit_perc'].mean()
        print(f'El nuevo porcentaje promedio de permisos es: {avg_permit_perc:.2f}')
        
        # Conclusión
        print('\nAl principio, nuestros datos estaban inflados por el estado de Kentucky, que tenía un porcentaje de permisos desproporcionadamente alto. Esto hacía que la media fuera de 34.88, mucho más alta de lo que realmente debería ser. Kentucky era un valor atípico, algo así como una oveja negra que distorsionaba nuestra percepción del conjunto de datos. Al identificar este problema, decidimos reemplazar su valor de permit_perc con el promedio general de la columna, para así nivelar el terreno.')
        print('\nDespués de hacer este ajuste, recalculamos la media y vimos que bajó a 21.12. Esto nos mostró que Kentucky realmente estaba inflando los números. Al eliminar o ajustar los valores atípicos, conseguimos una visión mucho más clara y precisa de la situación real. Este proceso es fundamental para evitar conclusiones erróneas y asegurarnos de que nuestros datos reflejen la realidad de manera más fiel. Así, podemos tomar decisiones más acertadas basadas en datos más precisos y confiables.\n')
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        return None