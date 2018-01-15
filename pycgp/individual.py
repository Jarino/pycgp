""" Individual """
from copy import deepcopy
from inspect import signature

import numpy as np

from pycgp.graph_iterator import iterate_active_nodes
from pycgp.mapper import map_to_phenotype
from pycgp.node import FunctionNode, InputNode, OutputNode
from pycgp.utils import split_to_chunks


class Individual():
    def __init__(self, genes, bounds, params):
        self.params = params
        self.genes = genes
        self.bounds = bounds

        self.nodes = map_to_phenotype(
            genes, self.params['n_inputs'], self.params['arity'], self.params['n_outputs'])

        self.fitness = None
        self.active_genes_vector = None

        self.__mark_active()

    def __len__(self):
        return len(self.genes)

    @property
    def input_nodes(self):
        return self.nodes[0:self.params['n_inputs']]

    @property
    def function_nodes(self):
        n_inodes = self.params['n_inputs']
        n_fnodes = (len(self.genes) -
                    self.params['n_outputs']) // (self.params['arity'] + 1)
        return self.nodes[n_inodes:n_inodes + n_fnodes]

    @property
    def output_nodes(self):
        n_inodes = self.params['n_inputs']
        n_fnodes = (len(self.genes) -
                    self.params['n_outputs']) // (self.params['arity'] + 1)
        return self.nodes[n_inodes + n_fnodes:]

    @property
    def output_genes(self):
        """ Return the list containing output genes as list of integers """
        return self.genes[-self.params['n_outputs']:]

    @property
    def active_genes(self):
        """ Return a bit array indicating, whether gene at given position
        is active or not """
        if self.active_genes_vector is not None:
            return self.active_genes_vector

        agenes = []
        chunk_size = self.params['arity'] + 1
        for fnode in self.function_nodes:
            if fnode.active:
                agenes = agenes + [1] * chunk_size
            else:
                agenes = agenes + [0] * chunk_size

        agenes = agenes + [1] * self.params['n_outputs']
        self.active_genes_vector = agenes
        return agenes

    def __mark_active(self):
        """ Mark nodes which are active and need to be computed """
        for node in iterate_active_nodes(self):
            node.active = True

    def __execute_single(self, data):
        for node, value in zip(self.input_nodes, data):
            node.value = value

        for node in self.function_nodes:
            if node.active:
                node.compute(self.nodes, self.params['funset'])

        return [self.nodes[i].value for i in self.output_genes]

    def __execute_many(self, data):
        return [self.__execute_single(x) for x in data]

    def execute(self, data):
        """ Execute the individual with given data """
        if np.isscalar(data[0]):
            return self.__execute_single(data)
        else:
            return self.__execute_many(data)

    def is_gene_active(self, gene_index):
        """ Checks, whether gene at given index belongs to
        active node or not """
        nodes = self.function_nodes + self.output_nodes

        node_index = gene_index // (self.params['arity'] + 1)

        if isinstance(nodes[node_index], OutputNode):
            return True

        return nodes[node_index].active

    def __str__(self):
        """ Print the resulting function """
        stack = []
        for node in reversed(list(iterate_active_nodes(self))):

            if isinstance(node, InputNode):
                stack.append(str(node))

            if isinstance(node, FunctionNode):
                fun = self.params['funset'][node.function_index]
                arity = len(signature(fun).parameters)
                operands = reversed([stack.pop() for _ in range(0, arity)])
                fname = fun.__name__
                stack.append('{}({})'.format(fname, ','.join(operands)))

        return stack.pop()

    def __eq__(self, other):
        """
        Check whether two individuals are the same according to their
        phenotypes (genes of active nodes)
        """
        active_genes = [x * y for x, y in zip(self.active_genes, self.genes)]
        other_active_genes = [x * y for x,
                              y in zip(other.active_genes, other.genes)]
        return active_genes == other_active_genes
