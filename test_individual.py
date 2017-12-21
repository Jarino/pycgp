""" Test suite for CGP individual """

from individual import FunctionNode, Individual


def test_creating_nodes():
    """ Test the creation of input nodes """
    genes = [1, 0, 0, 1, 1, 1, 0, 4, 2, 2, 1, 3, 6]
    bounds = []

    params = {
        'arity': 2, 'n_inputs': 3, 'n_outputs': 1, 'funset': {}}

    ind = Individual(genes, bounds, params)

    assert [x.id for x in ind.input_nodes] == [0, 1, 2]


def test_n_nodes():
    """ Test whether individual correctly computes the number of fun nodes """
    genes = [1, 0, 0, 1, 1, 1, 0, 4, 2, 2, 1, 3, 6]
    bounds = []

    params = {
        'arity': 2, 'n_inputs': 3, 'n_outputs': 1, 'funset': {}}

    ind = Individual(genes, bounds, params)

    assert ind.n_nodes == 4


def test_evaluation():
    """ Test the evaluation of the individual """

    genes = [1, 0, 0, 1, 1, 1, 0, 4, 2, 2, 1, 3, 6]
    bounds = []

    funset = {}
    funset[0] = lambda x, y: x + y
    funset[1] = lambda x, y: x * y
    funset[2] = lambda x, y: x - y

    params = {
        'arity': 2, 'n_inputs': 3, 'n_outputs': 1, 'funset': funset}

    ind = Individual(genes, bounds, params)
    input_data = [10, 8, 4]

    output = ind.execute(input_data)

    assert output[0] == -92


class NodeMock:
    def __init__(self, value):
        self.value = value


def test_function_node_compute():
    """ Test the computation of value of function node """
    funnode = FunctionNode([2, 0, 1])
    nodes = [NodeMock(4), NodeMock(8)]
    funset_mock = {}
    funset_mock[2] = lambda x, y: x + y

    funnode.compute(nodes, funset_mock)

    assert funnode.value == 12


def test_marking_active():
    """ Test whether individual correctly marks its nodes as (in)active """

    genes = [1, 0, 0, 1, 1, 1, 0, 4, 2, 2, 1, 3, 6]
    bounds = []

    params = {
        'arity': 2, 'n_inputs': 3, 'n_outputs': 1, 'funset': {}}

    ind = Individual(genes, bounds, params)

    assert ind.nodes[3].active
    assert not ind.nodes[4].active
    assert not ind.nodes[5].active
    assert ind.nodes[6].active
