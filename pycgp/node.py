from abc import ABC

class Node(ABC):
    """
    Contains two basic attributes:
    - id: is the index of node in phenotype of individual 
    - value: computed value of this node (input value in case of InputNode, 
             computed value of FunctionNode and output value of OutputNode)
    """
    def __init__(self, _id):
        self.id = _id
        self.value = None


class InputNode(Node):
    def __init__(self, index):
        super().__init__(index)

    def __str__(self):
        return 'x{}'.format(self.id)


class FunctionNode(Node):
    def __init__(self, index, genes):
        self.update(genes)
        super().__init__(index)

    def compute(self, other_nodes, funset):
        fun = funset[self.function_index]
        self.value = fun(*[other_nodes[x].value for x in self.inputs])

    def update(self, genes):
        self.active = False
        self.function_index = genes[0]
        self.inputs = genes[1:]

class OutputNode(Node):
    def __init__(self, index, gene):
        self.input = gene
        super().__init__(index)
