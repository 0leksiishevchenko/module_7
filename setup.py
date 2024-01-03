from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.1',
    description='Very strange code',
    url='https://github.com/0leksiishevchenko/sorter',
    author='Oleksii Shevchenko',
    license='MIT',
    packages=['clean_folder'],
    entry_points={
        'console_scripts': [
            'clean_folder = clean_folder.clean:main',
        ],
    },
)