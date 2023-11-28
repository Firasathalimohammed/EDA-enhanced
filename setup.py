from distutils.core import setup

setup(
    name='car_dataset',
    version='0.2.1',
    description='Classes for analysis of car dataset.',
    author='Firasat',
    author_email='fmohamm1@mail.yu.edu',
    license='MIT',
    url='https://github.com/Firasathalimohammed/Project-3',
    packages=['car_dataset'],
    install_requires=[
        'matplotlib>=3.0.2',
        'numpy>=1.15.2',
        'pandas>=0.23.4',
        'pandas-datareader>=0.7.0',
        'seaborn>=0.11.0',
        'statsmodels>=0.11.1',
    ],
)
