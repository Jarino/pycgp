""" Test suite for selection operators """

from pycgp.selection import truncation_selection

from collections import namedtuple

Individual = namedtuple('Individual', ['id', 'fitness'])

def test_truncation_selection():
    population = [
        Individual('a', 10),
        Individual('b', 90),
        Individual('c', 56),
        Individual('x', 78)
            ]

    best = truncation_selection(population, 1)[0]

    assert best.fitness == 10
