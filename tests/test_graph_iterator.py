""" test for individual iterators """

from pycgp.graph_iterator import iterate_active_nodes 

def test_iterate_active_nodes(individual):
    iterator = iterate_active_nodes(individual)

    visited_ids = [x.id for x in iterator]

    assert visited_ids == [7, 6, 3, 0, 0]

