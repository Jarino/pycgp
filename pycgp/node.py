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

    @property
    def inputs(self):
        return []


class FunctionNode(Node):
    def __init__(self, index, genes):
        self.update(genes)
        self.genes = genes
        super().__init__(index)

    def compute(self, other_nodes, params):
        fun = params.funset[self.function_index]
        arity = params.arities[self.function_index]
        self.value = fun(*[other_nodes[x].value for x in self.inputs[:arity]])

    def update(self, genes):
        self.active = False
        self.function_index = genes[0]
        self.inputs = genes[1:]

        

class OutputNode(Node):
    def __init__(self, index, gene):
        self.input = gene
        self.genes = [gene]
        super().__init__(index)

    @property
    def inputs(self):
        return [self.input]
