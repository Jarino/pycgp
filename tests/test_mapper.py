"""
Test suite for mapper module
"""

from pycgp.mapper import map_to_phenotype
from pycgp.node import FunctionNode,OutputNode,InputNode

def test_map_to_phenotype(individual):
    """ Test, whether mapping of genes to nodes works """

    genes = individual.genes
    n_inputs = individual.params.n_inputs
    arity = individual.params.arity
    n_outputs = individual.params.n_outputs

    nodes = map_to_phenotype(genes, n_inputs, arity, n_outputs)
    assert [x.id for x in nodes] == [0,1,2,3,4,5,6,7]
    assert isinstance(nodes[0], InputNode)
    assert isinstance(nodes[3], FunctionNode)
    assert isinstance(nodes[7], OutputNode)

    assert nodes[7].input == 6



