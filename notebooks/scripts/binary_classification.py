import random
from time import time
from copy import deepcopy
import pickle
import os

from pycgp.benchmarks.classification import * 
from pycgp import Params, EvParams
from pycgp.evolution import evolution
from pycgp.gems import MatchPMStrategy, MatchSMStrategy, MatchByActiveStrategy
from pycgp import point_mutation, probabilistic_mutation, single_mutation

experiment_count = 0

def run_experiment(params, ev_params, x, y):
    global experiment_count
    experiment_count += 1

    print('Experiment #{}'.format(experiment_count))
    start = time()

    exp_stats = []

    for i in range(0, 20):
        print(i, end=', ')

        result = evolution(params, ev_params, X_train, y_train)

        stats = result['stats']
        stats['best_fitness'] = [x.fitness for x in stats['best_of_generation']]
        del stats['best_of_generation']
        stats['test_error'] = ev_params.cost_function(y_test,
                                stats['best'].execute(X_test))
        stats['gem_data'] = result['gem_stats']

        exp_stats.append(deepcopy(stats))


    end = time()
    print('wall time {}'.format(end-start))

    return exp_stats


output_folder = 'bin_class_out'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


mutations = [
        (point_mutation, MatchPMStrategy),
        (single_mutation, MatchSMStrategy),
        (single_mutation, MatchByActiveStrategy),
        (probabilistic_mutation, MatchSMStrategy),
        (probabilistic_mutation, MatchByActiveStrategy)]

for mutation, strategy in mutations:
    for gems in [0, 5, 10]:
        ev_params = EvParams(
            cost_func,
            target_fitness=-1,
            gems_box_size=gems,
            gem_match_strategy=strategy,
            mutation=mutation,
            fitness_of_invalid=0)
        for n_cols in [100, 50, 10]:
            params = Params(
                n_columns=n_cols,
                n_inputs=30, 
                n_outputs=1,
                funset=funset)


            random.seed(1)

            filename = f'{output_folder}{mutation.__name__}-{strategy.__name__}-gems{gems}-n_cols{n_cols}.csv'
            print(filename)

            result = run_experiment(params, ev_params, X_train, y_train)

            with open(os.path.join(output_folder, filename), 'wb') as f:
                pickle.dump(result, f)
