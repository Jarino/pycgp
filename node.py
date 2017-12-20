from abc import ABC

class Node(ABC):
    def __init__(self):
        self.value = None


class InputNode(Node):
    def __init__(self, index):
        # not really needed, occurs in test
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
