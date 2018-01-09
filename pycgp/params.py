"""
This module contains some simple default parameters to 
"""

FUNSET = {}


def protected_div(x, y):
    if y == 0:
        return 1

    return x / y


def fsum(x, y):
    return x + y


def fdiv(x, y):
    return x - y


def fmul(x, y):
    return x * y


FUNSET[0] = fsum
FUNSET[1] = fdiv
FUNSET[2] = fmul
FUNSET[3] = protected_div

DEFAULT_PARAMS = {
    'n_inputs': 3,
    'n_outputs': 2,
    'n_cols': 2,
    'n_rows': 1,
    'funset': FUNSET
}
