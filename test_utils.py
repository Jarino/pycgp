""" Test suite for general utility functions """

import utils


def test_evenly_list_split():
    """ Test spliting the list into chunks of size N"""
    test_list = [1, 2, 3, 4, 5, 6, 7]

    chunks = list(utils.split_to_chunks(test_list, 3))

    assert chunks[0] == [1, 2, 3]
    assert chunks[1] == [4, 5, 6]
    assert chunks[2] == [7]
