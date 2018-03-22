from pycgp import Params, EvParams
from pycgp.evolution import evolution
from functools import reduce
from math import log as olog
from math import sin as osin
from math import cos as ocos

import random

random.seed(0)

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


def target_function(x):
    return osin(x**2) + osin(x + x**2)

X = [x/10 for x in range(-50,50)]
y = [target_function(x) for x in X]
X = [[x] for x in X]


def square(acc, ys):
    return acc + (ys[0] - ys[1][0])**2

def mean_squared_error(y_pred, y_true):
    return reduce(square, zip(y_pred, y_true), 0)/len(y_pred)
        

params = Params(1, 1)
ev_params = EvParams(mean_squared_error)

result = evolution(params, ev_params, X, y)

print('Done!')
[print(i.fitness) for i in result['final']]