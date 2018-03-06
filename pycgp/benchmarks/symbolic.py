""" Provides parameters and data for symbolic regression benchmark
Includes:
    PARAMS: dict, containing settings for CGP
    EV_PARAMS: dict, containing settings for evolutionary algorithm
    X: input vector
    y: target vector
"""
from math import log as olog
from math import sin as osin
from math import cos as ocos

from sklearn.metrics import mean_squared_error
import numpy as np
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

FUNSET = {}
FUNSET[0] = add
FUNSET[1] = mul
FUNSET[2] = pdiv 
FUNSET[3] = sub 
FUNSET[4] = plog 
FUNSET[5] = sin 
FUNSET[6] = cos 

PARAMS = {
    'n_inputs': 1,
    'n_outputs': 1,
    'n_rows': 1,
    'n_cols': 10,
    'funset': FUNSET
}

EV_PARAMS = {
    'cost_func': mean_squared_error,
    'target_fitness': 0
}

def target_function(x):
    return osin(x**2) + osin(x + x**2)

X = np.arange(-5,5,0.1)
y = [target_function(x) for x in  X]
X = X.reshape(-1,1)
