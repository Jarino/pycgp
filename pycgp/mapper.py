"""
Module containing functions for genotype-phenotype mapping
"""
from pycgp.node import FunctionNode, InputNode, OutputNode
from pycgp.utils import split_to_chunks


def map_to_phenotype(genes, n_inputs, arity, n_outputs):
    """ Map genotype to phenotype """
    input_nodes = [InputNode(i) for i in range(n_inputs)]

    chunks = split_to_chunks(genes, arity + 1)

    function_nodes = []

    n_nodes = (len(genes) - n_outputs) // (arity + 1)

    for index in range(n_nodes):
        function_nodes.append(FunctionNode(index + n_inputs, next(chunks)))

    output_nodes = []
    output_genes = genes[(index + 1) * (arity + 1):]

    for index, gene in zip(range(n_outputs), output_genes):
        output_nodes.append(OutputNode(index + n_inputs + n_nodes, gene))

    return input_nodes + function_nodes + output_nodes
