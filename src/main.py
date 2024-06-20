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
