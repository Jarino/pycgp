""" module containing iterators for graph of cgp individual """

from pycgp.node import FunctionNode, OutputNode


def iterate_active_nodes(individual):
    """
    Performs a depth-first recursive traversal, from output nodes
    to input nodes
    """
    stack = []

    for onode in individual.output_nodes:
        stack.append(onode)

    while len(stack) > 0:
        current_node = stack.pop()

        yield current_node

        n_inputs = 1

        # hackish way to check, whether it is a function node
        if 'function_index' in current_node.__dict__:
            # it is function node
            n_inputs = individual.params.arities[current_node.function_index]


        for input_id in current_node.inputs[:n_inputs]:
            stack.append(individual.nodes[input_id])



