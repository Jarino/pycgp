""" Individual """
from copy import deepcopy

import numpy as np

from mapper import map_to_phenotype
from node import FunctionNode, InputNode
from utils import split_to_chunks


class Individual():

    def __init__(self, genes, bounds, params):
        self.params = params
        self.genes = genes
        self.bounds = bounds

        self.nodes = map_to_phenotype(
            genes, self.params['n_inputs'], self.params['arity'], self.params['n_outputs'])

        self.__mark_active()

    def __len__(self):
        return len(self.genes)

    @property
    def input_nodes(self):
        return self.nodes[0:self.params['n_inputs']]

    @property
    def function_nodes(self):
        n_inodes = self.params['n_inputs']
        n_fnodes = (len(self.genes) - self.params['n_outputs']) // (self.params['arity'] + 1)
        return self.nodes[n_inodes:n_inodes + n_fnodes]

    @property
    def output_nodes(self):
        n_inodes = self.params['n_inputs']
        n_fnodes = (len(self.genes) - self.params['n_outputs']) // (self.params['arity'] + 1)
        return self.nodes[n_inodes + n_fnodes:]

    @property
    def output_genes(self):
        """ Return the list containing output genes as list of integers """
        return self.genes[-self.params['n_outputs']:]

    def copy(self):
        """ Return the copy of individual for mutation """
        return deepcopy(self)

    def __mark_active(self):
        """ Mark nodes which are active and need to be computed """
        stack = []
        for node_id in self.output_genes:
            stack.append(node_id)

        while len(stack) > 0:
            current_node = self.nodes[stack.pop()]
            current_node.active = True

            if type(current_node) is InputNode:
                continue

            for input_id in current_node.inputs:
                stack.append(input_id)

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

    def update(self):
        """ Update the values in function nodes """

        chunks = split_to_chunks(self.genes, self.params['arity'] + 1)
        for index, chunk in enumerate(chunks):
            if index == len(self.function_nodes):
                break

            self.function_nodes[index].update(chunk)

        self.__mark_active()

    def __str__(self):
        """ Print the resulting function """
        pass
