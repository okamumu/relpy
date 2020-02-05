from setuptools import setup

__version__ = '0.8.1'

setup(
    name='relpy',
    version=__version__,
    author='Hiroyuki Okamura',
    author_email='okamu@hiroshima-u.ac.jp',
    url='https://github.com/okamumu/relpy',
    description='Reliability evaluation with Python',
    long_description='',
    packages=['relpy', 'relpy.sharpe'],
    install_requires=[
        'numpy',
        'scipy',
        'antlr4-python3-runtime',
        'nmarkov@git+https://github.com/okamumu/nmarkov.git'
    ],
)
