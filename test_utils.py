""" Test suite for general utility functions """

import utils


def test_evenly_list_split():
    """ Test spliting the list into chunks of size N"""
    test_list = [1, 2, 3, 4, 5, 6, 7]

    chunks = list(utils.split_to_chunks(test_list, 3))

    assert chunks[0] == [1, 2, 3]
    assert chunks[1] == [4, 5, 6]
    assert chunks[2] == [7]

def test_max_arity():
    """ Test getting the maximu arity from set of functions """
    functions = [
            lambda x: x,
            lambda x, y: x,
            lambda x, y, z: z,
            lambda x, y, z, a: x
            ]

    assert utils.max_arity(functions) == 4

def test_max_arity_from_dict():
    """ Test max arity from dict_values iterable """
    funset = {}
    funset[0] = lambda x, y, z: x
    funset[1] = lambda x: x

    assert utils.max_arity(funset.values())
