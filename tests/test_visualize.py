""" test suite for visualization module """

from pycgp import visualize

def test_to_graph(individual):
    visualize.to_graph(individual, 'test_visualization')

    assert True
