""" Test suite for individual builder class """

from individual_builder import IndividualBuilder

from math import sin


def test_create():
    """ Test creation of individual """
    funset = {}
    funset[0] = lambda x, y: x + y
    funset[1] = lambda x, y: x * y
    funset[2] = lambda x: sin(x)  # built-in sin function has no signature

    n_inputs = 3
    n_outputs = 2
    n_cols = 2
    n_rows = 1

    params = {
        'n_inputs': 3,
        'n_outputs': 2,
        'n_cols': 2,
        'n_rows': 1,
        'funset': funset
    }

    ib = IndividualBuilder(params)

    individual = ib.build()

    assert True
