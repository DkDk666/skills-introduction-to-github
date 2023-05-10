from setuptools import setup, find_packages

setup(
    name='GUI',
    version='1.0',
    packages=find_packages(),
    install_requires=[
    'PyQt5==5.15.9',
    'pyserial==3.5',
    'tinydb==4.7.1',
    ],
)







