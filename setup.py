from setuptools import setup, find_packages

setup(
    name='analisis_datos_visualizacion',
    version='1.0.0',
    author='Victor Merchan Ventura',
    author_email='1Victormerch@gmail.com',  
    description='Análisis de datos de comprobaciones de antecedentes de armas de fuego en EE.UU. y generación de visualizaciones coropléticas y gráficos de evolución temporal.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/victormerchan/analisis_datos_visualizacion',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'matplotlib',
        'folium',
        'requests',
        'Pillow',
        'selenium'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)