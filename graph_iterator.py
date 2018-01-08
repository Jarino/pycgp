""" module containing iterators for graph of cgp individual """

from node import FunctionNode, OutputNode


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

        if isinstance(current_node, FunctionNode):
            for input_id in current_node.inputs:
                stack.append(individual.nodes[input_id])

        if isinstance(current_node, OutputNode):
            stack.append(individual.nodes[current_node.input])
