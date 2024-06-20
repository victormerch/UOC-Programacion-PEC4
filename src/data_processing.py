import pandas as pd

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
        path = f'Data/{url}'
        df = pd.read_csv(path)
        print(df.head())
        print(df.info())
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None

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
        df = df.groupby(['year', 'state']).sum().reset_index().set_index(['year', 'state'])
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None

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
        
        df2 = read_csv(url)
        df2['state'] = df2['state'].astype(str)
        df = pd.merge(df, df2, on='state', how='left')
        print(df.head())
        return df
    except Exception as e:
        print(f'An error has occurred: {e}')
        return None

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
