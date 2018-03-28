import random
from time import time
import sys
import os
import pickle
from functools import reduce
from operator import add
from copy import deepcopy

from pycgp.benchmarks.symbolic import * 
from pycgp import Params, EvParams
from pycgp.evolution import evolution
from pycgp.counter import Counter

experiment_count = 0

def run_experiment(params, ev_params, x, y):
    global experiment_count
    experiment_count += 1

    print('Experiment #{}'.format(experiment_count))
    start = time()
    exp_stats = []
    for i in range(0, 20):
        print(i, end=', ')

        result = evolution(params, ev_params, X, y)

        stats = result['stats']
        stats['best_fitness'] = [x.fitness for x in stats['best_of_generation']]
        del stats['best_of_generation']
        stats['number_of_evals'] = result['n_evals']
        stats['gem_data'] = result['gem_stats']
        exp_stats.append(deepcopy(stats))

    end = time()
    print('wall time {}'.format(end-start))

    return exp_stats

columns = [
    'mutation',
    'strategy',
    'gems',
    'n_cols',
    'overall_best',
    'overall_best_mean',
    'overall_best_std',
    'better_gems_total',
    'better_gems_mean',
    'worse_gems_total',
    'worse_gems_mean'
]


# params to change
# mutation, gems, expire, cols,
from pycgp.gems import MatchPMStrategy, MatchSMStrategy, MatchByActiveStrategy
from pycgp import point_mutation, probabilistic_mutation, single_mutation

mutations = [
        (single_mutation, MatchSMStrategy),
        (point_mutation, MatchPMStrategy),
        (probabilistic_mutation, MatchSMStrategy),
        (single_mutation, MatchByActiveStrategy),
        (probabilistic_mutation, MatchByActiveStrategy)]

output_folder = 'symbolic_out_pypy_50_gem_expire'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for mutation, strategy in mutations:
    for gems in [0, 5, 10]:
        ev_params = EvParams(
            cost_func,
            target_fitness=0,
            gems_box_size=gems,
            gem_match_strategy=strategy,
            mutation=mutation,
            gem_expire=50)
        for n_cols in [10, 50, 100]:
            params = Params(n_columns=n_cols, n_inputs=1, 
                n_outputs=1,
                funset=funset)

            row = [mutation.__name__, strategy.__name__, gems, n_cols]

            random.seed(1)

            filename = f'{mutation.__name__}-{strategy.__name__}-gems{gems}-n_cols{n_cols}.csv'

            print(filename)

            result = run_experiment(params, ev_params, X, y)

            with open(os.path.join(output_folder, filename), 'wb') as f:
                pickle.dump(result, f)


            # row += gem_data

            # data.loc[experiment_count] = row

            # filename = f'{mutation.__name__}-{strategy.__name__}-gems{gems}-n_cols{n_cols}.csv'
            # fitness_data = pd.DataFrame()
            # fitness_data['best_fitness'] = best_fitness
            # fitness_data['mean_fitness'] = mean_fitness
            # fitness_data.to_csv(filename)


#data.to_csv('sym_res_active.csv', sep=',')
