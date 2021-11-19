
names = ['asdf', 'asdfjk', 'jkfdlj']
print(list(map(str.upper, names))) ### we can pass simple functions as well 
                                   ###  or built-n fns or even a Lambda

numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x*x, numbers)))

def CtoF(c):
    return 9/5 * c + 32

def FtoC(f):
    return (f-32) * 5/9

cTemps = [45, 35, 30]
print(list(map(CtoF, cTemps)))

fTemps = [125, 100, 90]
print(list(map(FtoC, fTemps)))

################    FILTER      ########################

scores = [34, 57, 75, 76, 82, 99]
def is_A_student(score):
    return score > 75

print(list(filter(is_A_student, scores)))
print(list(filter(lambda x: x > 75, scores)))

################    REDUCE      ########################
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def custom_sum(x, y):
    return x + y

print(reduce(custom_sum, numbers))

import os, os.path, operator

files = os.listdir(os.path.expanduser('.'))
print(reduce(operator.add, map(os.path.getsize, files))) ### Run this in Day1 manually 
                                            ### in terminal to get the total file size
                                            ### in the Day1 folder... else this gives 
                                            ### size of Day1 folder itself = 320 bytes

import numpy as np

x = np.array([1, 2, 3, 4, 5])

squarer = lambda x: x*x

squares = np.array([squarer(xi) for xi in x ])
print(squares)


