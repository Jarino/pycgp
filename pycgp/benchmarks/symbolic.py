""" Provides parameters and data for symbolic regression benchmark
Includes:
    PARAMS: dict, containing settings for CGP
    EV_PARAMS: dict, containing settings for evolutionary algorithm
    X: input vector
    y: target vector
"""
from functools import reduce
from math import log as olog
from math import sin as osin
from math import cos as ocos

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

def pdiv(x, y):
    if y == 0:
        return x
    return x / y

def sub(x, y):
    return x - y

def plog(x):
    if x <= 0:
        return x
    return olog(x)

def sin(x):
    return osin(x)

def cos(x):
    return ocos(x)

funset = {}
funset[0] = add
funset[1] = mul
funset[2] = pdiv 
funset[3] = sub 
funset[4] = plog 
funset[5] = sin 
funset[6] = cos 

def square(acc, ys):
    return acc + (ys[0] - ys[1][0])**2

def mean_squared_error(y_pred, y_true):
    return reduce(square, zip(y_pred, y_true), 0)/len(y_pred)

def target_function(x):
    return osin(x**2) + osin(x + x**2)

X = [x/10 for x in range(-50,50)]
y = [target_function(x) for x in X]
X = [[x] for x in X]

cost_func = mean_squared_error

target_fitness = 0

__all__ = [
    'funset', 'cost_func', 'target_fitness', 'X', 'y'
]