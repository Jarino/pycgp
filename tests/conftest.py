""" """

import pytest

from pycgp.individual import Individual
from pycgp.gems import JewelleryBox, Gem

@pytest.fixture
def individual():
    genes = [1, 0, 0, 1, 1, 1, 0, 4, 2, 2, 1, 3, 6]
    #active [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    bounds = [2, 2, 2, 2, 3, 3, 2, 4, 4, 2, 5, 5, 6]

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


@pytest.fixture
def jewellerybox():
    box = JewelleryBox()

    box.add(Gem(1, 0, 2, 4))
    box.add(Gem(2, 3, 4, 5))

    return box
    

