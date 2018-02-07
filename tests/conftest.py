""" """

import pytest

from pycgp.individual import Individual
from pycgp.gems import JewelleryBox, GemPM, MatchPMStrategy


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

bounds = [2, 2, 2, 2, 3, 3, 2, 4, 4, 2, 5, 5, 6]

params = {'arity': 2, 'n_inputs': 3, 'n_outputs': 1, 'funset': funset}

@pytest.fixture
def individual():
    genes = [1, 0, 0, 1, 1, 1, 0, 4, 2, 2, 1, 3, 6]
    #active [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

    return Individual(genes, bounds, params)


@pytest.fixture
def jewellerybox():
    box = JewelleryBox(MatchPMStrategy())

    parent_genes =    [1, 0, 0, 1, 1, 1, 0, 4, 2, 2, 1, 3, 6]
    mutated_genes_1 = [1, 0, 0, 1, 3, 1, 0, 4, 2, 2, 1, 3, 6]
    mutated_genes_2 = [1, 0, 0, 1, 1, 1, 0, 4, 2, 2, 5, 3, 6]

    parent = Individual(parent_genes, bounds, params)
    mutated_1 = Individual(mutated_genes_1, bounds, params)
    mutated_2 = Individual(mutated_genes_2, bounds, params)

    mutated_1.fitness = 95
    mutated_2.fitness = 90
    parent.fitness = 100
    box.add(GemPM(mutated_1, parent, 4))
    box.add(GemPM(mutated_2, parent, 10))

    return box
    

