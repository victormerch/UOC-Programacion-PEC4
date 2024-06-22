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
        'pandas==2.2.2',
        'matplotlib==3.9.0',
        'folium==0.17.0',
        'requests==2.32.3',
        'Pillow==10.3.0',
        'selenium==4.22.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)