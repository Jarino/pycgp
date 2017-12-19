""" Individual """

from utils import split_to_chunks
from abc import ABC


class Node(ABC):
    def __init__(self):
        self.value = None
        

class InputNode(Node):
    def __init__(self, index):
        self.id = index
        super().__init__()

class FunctionNode(Node):
    def __init__(self, genes):
        self.active = False
        self.function_index = genes[0]
        self.inputs = genes[1:]
        super().__init__()

    def compute(self, other_nodes, funset):
        fun = funset[self.function_index]
        self.value = fun(*[other_nodes[x].value for x in self.inputs])


class Individual():

    def __init__(self, genes, arity, n_inputs, n_outputs):
        self.genes = genes
        self.n_nodes = (len(genes) - n_outputs)//(arity + 1)

        self.input_nodes = [InputNode(i) for i in range(n_inputs)]

        chunks = split_to_chunks(genes, arity + 1)

        self.function_nodes = []

        for _ in range(self.n_nodes):
            self.function_nodes.append(FunctionNode(next(chunks)))

        self.nodes = self.input_nodes + self.function_nodes

        self.output_genes = genes[(arity + 1) * self.n_nodes:]

        self._mark_active()

    def _mark_active(self):
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


    def execute(self, data, funset):
        """ Execute the individual with given data """

        for node, value in zip(self.input_nodes, data):
            node.value = value

        for node in self.function_nodes:
            if node.active:
                node.compute(self.nodes, funset)

        return [self.nodes[i].value for i in self.output_genes]
