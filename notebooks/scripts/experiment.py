import os, random
from time import time
from copy import deepcopy
import pickle

from pycgp import EvParams, Params
from pycgp.evolution import evolution

def run_experiment(params, ev_params, x, y, test_error=False, x_test=None, y_test=None):
    if test_error and (x_test is None or y_test is None):
        raise Exception('Test error is set to True, but no test or train data provided (x_test, y_test parameters)')

    start = time()
    exp_stats = []
    for i in range(0, 20):
        print(i, end=', ')

        result = evolution(params, ev_params, x, y)

        stats = result['stats']
        stats['best_fitness'] = [x.fitness for x in stats['best_of_generation']]
        del stats['best_of_generation']
        stats['number_of_evals'] = result['n_evals']
        stats['gem_data'] = result['gem_stats']

        if test_error:
            stats['test_error'] = ev_params.cost_function(y_test,
                                stats['best'].execute(x_test))

        exp_stats.append(deepcopy(stats))

    end = time()
    print('wall time {}'.format(end-start))

    return exp_stats

def experiment_loop(output_folder,
                    mutations,
                    cols,
                    gems_range,
                    cost_func,
                    ev_params_dict,
                    params_dict,
                    X_train,
                    y_train,
                    X_test=None,
                    y_test=None):

    if (X_test is None and y_test is not None) or (X_test is not None and y_test is None):
        raise Exception('Only one of the test sets was specified, for test evaluation X_test and y_test need to be set.')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    experiment_index = 1

    for mutation, strategy in mutations:
        for gems in gems_range:
            ev_params = EvParams(
                cost_func,
                **ev_params_dict,
                gems_box_size=gems,
                gem_match_strategy=strategy,
                mutation=mutation,
                population_size=5)
            for n_cols in cols:
                params = Params(n_columns=n_cols, **params_dict)

                row = [mutation.__name__, strategy.__name__, gems, n_cols]

                random.seed(1)

                filename = f'{mutation.__name__}-{strategy.__name__}-gems{gems}-n_cols{n_cols}.csv'

                print('Experiment #{}, {}'.format(experiment_index, filename))

                if X_test and y_test:
                    result = run_experiment(params, ev_params, X_train, y_train, True, X_test, y_test)
                else:
                    result = run_experiment(params, ev_params, X_train, y_train)

                with open(os.path.join(output_folder, filename), 'wb') as f:
                    pickle.dump(result, f)

                experiment_index += 1
