""" Probides parameters and data for binary classification benchmark
Inludes:
    PARAMS: dict, containing settings for CGP
    EV_PARAMS: dict, containing settings for evolutionary algorithm
    X: input vector
    y: target vector
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from scipy.special import expit
from sklearn.metrics import accuracy_score

data = load_breast_cancer(return_X_y=True)
X = data[0]
y = data[1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)

def class_cost_function(target, output):
    return -accuracy_score(target, np.round(expit(output)))

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

def plog(x, _):
    if x <= 0:
        return x
    return olog(x)

def sin(x, _):
    return osin(x)

def cos(x, _):
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
    'n_inputs': 30,
    'n_outputs': 1,
    'n_cols': 10,
    'arity': 2,
    'n_rows': 1,
    'funset': FUNSET
}

EV_PARAMS = {
    'cost_func': class_cost_function,
    'target_fitness': 0
}
