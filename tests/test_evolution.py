""" Integration test for the whole evolution process """

import pytest

from pycgp import EvParams, Params
from pycgp.evolution import evolution
from pycgp.mutation import single_mutation
from pycgp.gems import GemMultipleGenes, MatchSMStrategy
from pycgp.counter import Counter

from sklearn.metrics import mean_squared_error

@pytest.mark.skip(reason='takes too long')
def test_evolution():
    """ Should pass without error """

    # first import everything important

    X = [[1], [2], [3], [4]]
    y = [[1], [2], [3], [4]]

    ev_params = EvParams(mean_squared_error, gems_box_size=5)


    params = Params(1, 1, n_columns=5)

    result = evolution(params, ev_params, X, y)

    assert True
