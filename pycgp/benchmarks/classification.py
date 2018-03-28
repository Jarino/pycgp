""" Probides parameters and data for binary classification benchmark
Inludes:
    PARAMS: dict, containing settings for CGP
    EV_PARAMS: dict, containing settings for evolutionary algorithm
    X: input vector
    y: target vector
"""
import os
import pickle
from math import log as olog
from math import sin as osin
from math import cos as ocos
from math import exp


def safe_sigmoid(x):
    return 1 / (1 + exp(-x))


base_path = os.path.dirname(__file__)

names = ['X_train', 'X_test', 'y_train', 'y_test']
# just so linter wouldn't bitch about nonexistent variables
X_train = X_test = y_train = y_test = None

for name in names:
    path = os.path.join(base_path, 'bin_class_' + name)

    with open(path, 'rb') as f:
        data = pickle.load(f)

    exec('{} = data'.format(name))

#def class_cost_function(target, output):
#    return -accuracy_score(target, np.round(expit(output)))

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

def cost_func(target, output):
    # P - number of 1s in output 
    # N - number of 0s in output
    # TP - number of 1s in both target and output
    # TN - number of 0s in both target and output
    output = [0 if x[0] <= 0 else 1 for x in output]

    return -len([1 for t, o in zip(target, output) if t == o])/len(target)

__all__ = [
    'cost_func', 'X_train', 'X_test', 'y_train', 'y_test', 'funset'
]
