import random

from sklearn.metrics import mean_squared_error

from pycgp import Params, EvParams, tabu_search


def test_tabu_search():
    """ Should pass without an error """

    X = [[1], [2], [3], [4]]
    y = [[1], [2], [3], [4]]

    ev_params = EvParams(mean_squared_error, gems_box_size=5)


    params = Params(1, 1, n_columns=5)

    result = tabu_search(params, ev_params, X, y)

    assert True

