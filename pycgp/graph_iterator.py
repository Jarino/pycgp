""" module containing iterators for graph of cgp individual """

from pycgp.node import FunctionNode, OutputNode


def iterate_active_nodes(individual):
    """
    Performs a depth-first recursive traversal, from output nodes
    to input nodes
    """
    stack = []

    for onode_index in range(0, len(individual.output_nodes)):
        stack.append(individual.output_nodes[onode_index])

    while len(stack) > 0:
        current_node = stack.pop()

        yield current_node

        n_inputs = len(current_node.inputs)

        # hackish way to check, whether it is a function node
        if 'function_index' in current_node.__dict__:
            # it is function node
            n_inputs = individual.params.arities[current_node.function_index]


        for index in range(0, n_inputs):
            stack.append(individual.nodes[current_node.inputs[index]])
        #for input_id in current_node.inputs:
        #    stack.append(individual.nodes[input_id])



