""" """

import pytest

from individual import Individual

@pytest.fixture
def individual():
    genes = [1, 0, 0, 1, 1, 1, 0, 4, 2, 2, 1, 3, 6]
    bounds = []

    funset = {}
    funset[0] = lambda x, y: x + y
    funset[1] = lambda x, y: x * y
    funset[2] = lambda x, y: x - y

    params = {
        'arity': 2, 'n_inputs': 3, 'n_outputs': 1, 'funset': funset}

    return Individual(genes, bounds, params)
