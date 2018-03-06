import graphviz as gv

from pycgp.node import InputNode, FunctionNode

def to_graph(individual, output_path='individual'):
    """ visualize graph """
    # add input nodes
    graph = gv.Digraph(format='png')

    for input_node in individual.input_nodes:
        graph.node(str(input_node))

    # add function nodes
    for index, fnode in enumerate(individual.function_nodes):
        if fnode.active:
            color='black'
        else:
            color='gray'

        graph.node('f{}'.format(index), color=color)

    # add output nodes
    for index, _ in enumerate(individual.output_genes):
        graph.node('o{}'.format(index))

    # add edges of function nodes
    for index, fnode in enumerate(individual.function_nodes):
        if fnode.active:
            color = 'black'
        else:
            color = 'gray'

        for order, parent_id in enumerate(fnode.inputs):
            parent = individual.nodes[parent_id]
            if order >= individual.params.arities[fnode.function_index]:
                color = 'gray'

            if type(parent) is InputNode:
                graph.edge(str(parent), 'f{}'.format(index), color=color)

            if type(parent) is FunctionNode:
                graph.edge('f{}'.format(parent_id - len(individual.input_nodes)), 'f{0}'.format(index), color=color)

    # add edges of output nodes

    for index, ogene in enumerate(individual.output_genes):
        parent = individual.nodes[ogene]

        if type(parent) is InputNode:
            graph.edge(str(parent), 'o{}'.format(index))

        if type(parent) is FunctionNode:
            graph.edge('f{}'.format(ogene - len(individual.input_nodes)), 'o{}'.format(index))

    graph.attr(rankdir='LR')
    graph.render(output_path)




