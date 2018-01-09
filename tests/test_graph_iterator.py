""" test for individual iterators """

import pycgp.graph_iterator as gi

def test_iterate_active_nodes(individual):
    iterator = gi.iterate_active_nodes(individual)

    visited_ids = [x.id for x in iterator]

    assert visited_ids == [7, 6, 3, 0, 0, 1]

