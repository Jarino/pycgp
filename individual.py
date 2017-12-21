""" Individual """
import numpy as np
from utils import split_to_chunks
from node import InputNode, FunctionNode
from copy import deepcopy

class Individual():


    def __init__(self, genes, bounds, params):
        arity = params['arity']
        n_inputs = params['n_inputs']
        self.n_outputs = params['n_outputs']

        self.funset = params['funset']

        self.genes = genes
        self.bounds = bounds

        self.n_nodes = (len(genes) - self.n_outputs) // (arity + 1)

        self.input_nodes = [InputNode(i) for i in range(n_inputs)]

        chunks = split_to_chunks(genes, arity + 1)

        self.function_nodes = []

        for _ in range(self.n_nodes):
            self.function_nodes.append(FunctionNode(next(chunks)))

        self.nodes = self.input_nodes + self.function_nodes

        self._mark_active()

    def __len__(self):
        return len(self.genes)

    @property
    def output_genes(self):
        return self.genes[-self.n_outputs:]
    
    def copy(self):
        """ Return the copy of individual for mutation """
        return deepcopy(self)


    def _mark_active(self):
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
                node.compute(self.nodes, self.funset)

        return [self.nodes[i].value for i in self.output_genes]

    def __execute_many(self, data):
        return [self.__execute_single(x) for x in data]
        

    def execute(self, data):
        """ Execute the individual with given data """
        if np.isscalar(data[0]):
            return self.__execute_single(data)
        else:
            return self.__execute_many(data) 
