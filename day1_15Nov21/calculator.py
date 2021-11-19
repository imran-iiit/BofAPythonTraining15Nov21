### one module == 1 py file

import os, sys

def square(x):
    '''This is a docstring - squares the params '''
    return x*x

def cube(x):
    '''returns x*x*x '''
    return x*x*x

#pip install pydoc - it will create a nice document (pdf) based on the docstrings
### A module must NEVER have a print()!!!!

