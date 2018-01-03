""" """

import pytest

from individual import Individual


@pytest.fixture
def individual():
    genes = [1, 0, 0, 1, 1, 1, 0, 4, 2, 2, 1, 3, 6]
    bounds = []

    funset = {}

    def fsum(x, y):
        return x + y

    def fmul(x, y):
        return x * y

    def fsub(x, y):
        return x - y
    funset[0] = fsum
    funset[1] = fmul
    funset[2] = fsub

    params = {
        'arity': 2, 'n_inputs': 3, 'n_outputs': 1, 'funset': funset}

    return Individual(genes, bounds, params)
