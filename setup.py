from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'numpy',
    'scipy',
    'IPython'
]

setup(
    name='gosset',
    version='0.1.0',
    author='Tim Book',
    author_email='TimothyKBook@gmail.com',
    description='A Python library for classical inference and working with random variables.',
    url='https://github.com/timbook/gosset/tree/main',
    license='GPL',
    packages=find_packages(),
    python_requires='>=3.6'
)
