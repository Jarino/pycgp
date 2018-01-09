""" General utility methods """

from inspect import signature


def split_to_chunks(list_to_split, chunk_size):
    """ Split the given list into chunks of chunk_size. """
    for i in range(0, len(list_to_split), chunk_size):
        yield list_to_split[i:chunk_size + i]


def max_arity(functions):
    """ Returns the maximum arity from list of functions """
    arities = map(lambda x: len(signature(x).parameters), functions)
    return max(arities)

def parse_genes(genes):
    """ Parse genes and returns the list of nodes """

    
