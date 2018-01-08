from node import FunctionNode

class NodeMock:
    def __init__(self, value):
        self.value = value

def test_function_node_compute():
    """ Test the computation of value of function node """
    funnode = FunctionNode(0, [2, 0, 1])
    nodes = [NodeMock(4), NodeMock(8)]
    funset_mock = {}
    funset_mock[2] = lambda x, y: x + y

    funnode.compute(nodes, funset_mock)

    assert funnode.value == 12
