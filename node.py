from abc import ABC

class Node(ABC):
    def __init__(self):
        self.value = None
        self.upper_bound = 0


class InputNode(Node):
    def __init__(self, index):
        # not really needed, occurs in test
        self.id = index
        super().__init__()


class FunctionNode(Node):
    def __init__(self, genes):
        self.update(genes)
        super().__init__()

    def compute(self, other_nodes, funset):
        fun = funset[self.function_index]
        self.value = fun(*[other_nodes[x].value for x in self.inputs])

    def update(self, genes):
        self.active = False
        self.function_index = genes[0]
        self.inputs = genes[1:]

class OutputNode(Node):
    def __init__(self):
        super().__init__()
