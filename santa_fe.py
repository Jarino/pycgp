""" Dev script for santa fe trail problem """

from random import choice
from functools import partial

def move():
    print('move')
    pass

def turn_left():
    print('turn_left')
    pass

def turn_right():
    print('turn_right')
    pass

def if_food_ahead(opt1, opt2, _):
    if choice([True, False]):
        return opt1
    else:
        return opt2

def progn(*args):
    for arg in args:
        arg()

def prog2(opt1, opt2, _):
    return partial(progn, opt1, opt2)

def prog3(opt1, opt2, opt3):
    return partial(progn, opt1, opt2, opt3)

FUNSET = {}
FUNSET[0] = if_food_ahead
FUNSET[1] = prog2
FUNSET[2] = prog3

PARAMS = {
    'n_inputs': 3,
    'n_outputs': 1,
    'n_rows': 1,
    'n_cols': 10,
    'funset': FUNSET
}

X = [move, turn_left, turn_right]

# example usage

from pycgp.individual_builder import IndividualBuilder

ib = IndividualBuilder(PARAMS)

individual = ib.build()

machine = individual.execute([X])[0][0]

machine()




