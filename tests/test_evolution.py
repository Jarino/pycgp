""" Integration test for the whole evolution process """

def test_evolution():
    """ Should pass without error """

    # first import everything important
    from pycgp.evolution import evolution
    from pycgp.mutation import single_mutation
    from pycgp.gems import GemMultipleGenes, MatchSMStrategy
    from pycgp.counter import Counter
    from pycgp.params import DEFAULT_PARAMS

    from sklearn.metrics import mean_squared_error

    X = [[1], [2], [3], [4]]
    y = [[1], [2], [3], [4]]

    ev_params = {
            'cost_func': mean_squared_error,
            'target_fitness': 0,
            'gems': True,
            'j_box_size': 50
    }

    DEFAULT_PARAMS['n_rows'] = 1
    DEFAULT_PARAMS['n_cols'] = 5
    DEFAULT_PARAMS['n_inputs'] = 1
    DEFAULT_PARAMS['n_outputs'] = 1

    result = evolution(DEFAULT_PARAMS, ev_params, X, y)

    assert True
