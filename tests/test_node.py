from pycgp.node import FunctionNode


class NodeMock:
    def __init__(self, value):
        self.value = value

def test_function_node_compute():
    """ Test the computation of value of function node """
    funnode = FunctionNode(0, [2, 0, 1])
    nodes = [NodeMock(4), NodeMock(8)]
    funset_mock = {}
    funset_mock[2] = lambda x, y: x + y

    arities = [0]*3
    arities[2] = 2

    class ParamsMock():
        def __init__(self, funset, arities):
            self.funset = funset
            self.arities = arities
            


    funnode.compute(nodes, ParamsMock(funset_mock, arities))

    assert funnode.value == 12
