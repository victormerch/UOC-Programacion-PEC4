import unittest
import pandas as pd
from src.data_processing import *
from src.visualization import time_evolution
import os

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        # Datos de prueba iniciales
        self.data = {'month': ['2020-1'], 'state': ['Alabama'], 'permit': [100], 'handgun': [200], 'long_gun': [300]}
        self.df = pd.DataFrame(self.data)
    
    def test_read_csv(self):
        url = 'nics-firearm-background-checks.csv'
        df = read_csv(url)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)
    
    def test_clean_csv(self):
        df = clean_csv(self.df.copy())
        self.assertEqual(list(df.columns), ['month', 'state', 'permit', 'handgun', 'long_gun'])
    
    def test_rename_col(self):
        data = {'longgun': [1], 'other': [2]}
        df = pd.DataFrame(data)
        df = rename_col(df)
        self.assertIn('long_gun', df.columns)
        self.assertNotIn('longgun', df.columns)
    
    def test_breakdown_date(self):
        df = breakdown_date(self.df.copy())
        self.assertIn('year', df.columns)
        self.assertIn('month', df.columns)
        self.assertEqual(df.at[0, 'year'], 2020)
        self.assertEqual(df.at[0, 'month'], 1)
    
    def test_erase_month(self):
        df = breakdown_date(self.df.copy())
        df = erase_month(df)
        self.assertNotIn('month', df.columns)
    
    def test_groupby_state_and_year(self):
        df = breakdown_date(self.df.copy())
        df = erase_month(df)
        df = groupby_state_and_year(df)
        self.assertIn((2020, 'Alabama'), df.index)
    
    def test_groupby_state(self):
        df = groupby_state(self.df.copy())
        self.assertIn('Alabama', df.index)
    
    def test_clean_states(self):
        data = {'state': ['Alabama', 'Guam']}
        df = pd.DataFrame(data)
        df.set_index('state', inplace=True)
        df = clean_states(df)
        self.assertNotIn('Guam', df.index)
    
    def test_merge_datasets(self):
        df1 = self.df.copy()
        url = 'us-state-populations.csv'
        df = merge_datasets(df1, url)
        self.assertIsNotNone(df)
        self.assertIn('pop_2014', df.columns)
    
    def test_calculate_relative_values(self):
        data = {'permit': [100], 'handgun': [200], 'long_gun': [300], 'pop_2014': [1000]}
        df = pd.DataFrame(data)
        df = calculate_relative_values(df)
        self.assertIn('permit_perc', df.columns)
        self.assertIn('handgun_perc', df.columns)
        self.assertIn('longgun_perc', df.columns)
        self.assertEqual(df.at[0, 'permit_perc'], 10.0)
    
    def test_print_kentucky_info(self):
        data = {'state': ['Kentucky', 'Alabama'], 'permit_perc': [1000, 10]}
        df = pd.DataFrame(data)
        print_kentucky_info(df)
        self.assertEqual(df.loc[df.state == 'Kentucky', 'permit_perc'].values[0], 505.0)

class TestVisualization(unittest.TestCase):
    def setUp(self):
        # Datos de prueba iniciales
        self.data = {'year': [2020], 'permit': [100], 'handgun': [200], 'long_gun': [300]}
        self.df = pd.DataFrame(self.data)
    
    def test_time_evolution(self):
        time_evolution(self.df.copy())
        self.assertTrue(os.path.exists('time_evolution_plot.png'))

if __name__ == '__main__':
    unittest.main()
