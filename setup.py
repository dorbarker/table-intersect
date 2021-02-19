from setuptools import setup, find_packages

setup(
    name='table-intersect',
    version='1.0.0',
    packages=find_packages(),
    author='Dillon O.R. Barker',
    author_email='dillon.barker@canada.ca',
    entry_points={
        'console_scripts': [
            'table-intersect=src.table_intersect:main',
        ]
    }
)
