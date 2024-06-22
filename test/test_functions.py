import unittest
import pandas as pd
import sys
import os

# Añadir el directorio base del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processing import *
from src.visualization import time_evolution

class TestDataProcessing(unittest.TestCase):
    """
    Clase de pruebas para las funciones de procesamiento de datos.
    """
    
    def setUp(self) -> None:
        """
        Configuración inicial para las pruebas.
        """
        # Datos de prueba iniciales
        self.data = {'month': ['2020-1'], 'state': ['Alabama'], 'permit': [100], 'handgun': [200], 'long_gun': [300]}
        self.df = pd.DataFrame(self.data)
    
    def test_read_csv(self) -> None:
        """
        Prueba la función read_csv.
        """
        url = 'nics-firearm-background-checks.csv'
        df = read_csv(url)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)
    
    def test_clean_csv(self) -> None:
        """
        Prueba la función clean_csv.
        """
        df = clean_csv(self.df.copy())
        self.assertEqual(list(df.columns), ['month', 'state', 'permit', 'handgun', 'long_gun'])
    
    def test_rename_col(self) -> None:
        """
        Prueba la función rename_col.
        """
        data = {'longgun': [1], 'other': [2]}
        df = pd.DataFrame(data)
        df = rename_col(df)
        self.assertIn('longgun', df.columns)
    
    def test_breakdown_date(self) -> None:
        """
        Prueba la función breakdown_date.
        """
        df = breakdown_date(self.df.copy())
        self.assertIn('year', df.columns)
        self.assertIn('month', df.columns)
        self.assertEqual(df.at[0, 'year'], 2020)
        self.assertEqual(df.at[0, 'month'], 1)
    
    def test_erase_month(self) -> None:
        """
        Prueba la función erase_month.
        """
        df = breakdown_date(self.df.copy())
        df = erase_month(df)
        self.assertNotIn('month', df.columns)
    
    def test_groupby_state_and_year(self) -> None:
        """
        Prueba la función groupby_state_and_year.
        """
        df = breakdown_date(self.df.copy())
        df = erase_month(df)
        df = groupby_state_and_year(df)
        self.assertIn((2020, 'Alabama'), df.index)
    
    def test_groupby_state(self) -> None:
        """
        Prueba la función groupby_state.
        """
        df = groupby_state(self.df.copy())
        self.assertIn('Alabama', df.index)
    
    def test_clean_states(self) -> None:
        """
        Prueba la función clean_states.
        """
        data = {'state': ['Alabama', 'Guam']}
        df = pd.DataFrame(data)
        df.set_index('state', inplace=True)
        df = clean_states(df)
        self.assertNotIn('Guam', df.index)
    
    def test_merge_datasets(self) -> None:
        """
        Prueba la función merge_datasets.
        """
        df1 = self.df.copy()
        url = 'us-state-populations.csv'
        df = merge_datasets(df1, url)
        self.assertIsNotNone(df)
        self.assertIn('pop_2014', df.columns)
    
    def test_calculate_relative_values(self) -> None:
        """
        Prueba la función calculate_relative_values.
        """
        data = {'permit': [100], 'handgun': [200], 'longgun': [300], 'pop_2014': [1000]}
        df = pd.DataFrame(data)
        df = calculate_relative_values(df)
        self.assertIn('permit_perc', df.columns)
        self.assertIn('handgun_perc', df.columns)
        self.assertIn('longgun_perc', df.columns)
        self.assertEqual(df.at[0, 'permit_perc'], 10.0)
    
    def test_print_kentucky_info(self) -> None:
        """
        Prueba la función print_kentucky_info.
        """
        data = {'state': ['Kentucky', 'Alabama'], 'permit_perc': [1000, 10]}
        df = pd.DataFrame(data)
        print_kentucky_info(df)
        self.assertEqual(df.loc[df.state == 'Kentucky', 'permit_perc'].values[0], 505.0)

class TestVisualization(unittest.TestCase):
    """
    Clase de pruebas para las funciones de visualización.
    """
    
    def setUp(self) -> None:
        """
        Configuración inicial para las pruebas.
        """
        # Datos de prueba iniciales
        self.data = {'year': [2020], 'permit': [100], 'handgun': [200], 'longgun': [300]}
        self.df = pd.DataFrame(self.data)
    
    def test_time_evolution(self) -> None:
        """
        Prueba la función time_evolution.
        """
        time_evolution(self.df.copy())

if __name__ == '__main__':
    unittest.main()