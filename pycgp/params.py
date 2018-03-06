"""
This module contains some simple default parameters
"""

from inspect import signature

FUNSET = {}


def protected_div(x, y):
    if y == 0:
        return 1

    return x / y


def fsum(arg1, arg2):
    return arg1 + arg2

def fdiv(x, y):
    return x - y


def fmul(x, y):
    return x * y


FUNSET[0] = fsum
FUNSET[1] = fdiv
FUNSET[2] = fmul
FUNSET[3] = protected_div


class Params():
    """docstring for Params"""

    def __init__(self,
                 n_inputs,
                 n_outputs,
                 n_columns=50,
                 n_rows=1,
                 funset=FUNSET,
                 arity=2):

        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.n_columns = n_columns
        self.n_rows = n_rows
        self.funset = funset
        self.arity = arity
        self.arities = [len(signature(f).parameters) for f in funset.values()]
