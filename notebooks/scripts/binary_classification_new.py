from pycgp.benchmarks.classification import PARAMS, EV_PARAMS, X_train, X_test, y_train, y_test
from pycgp import Params, EvParams
from pycgp.evolution import evolution
from pycgp.counter import Counter
import random
import numpy as np
import pandas as pd
from time import time
import pandas as pd
import sys
from functools import reduce
from operator import add
experiment_count = 0

def get_data(gems):
    return [(
        x.n_uses, 
        x.match_checks, 
        x.match_count, 
        x.gene_possible_values,
        x.match_probability
        ) for x in gems]    
    
    columns = ['n_uses', 'match_checks', 'match_count', 'gene_possible_values', 'match_probability']
    data.columns = columns
    data['empiric'] = data.iloc[:,2]/data.iloc[:,1]
    return data

def run_experiment(params, ev_params, x, y):
    global experiment_count
    experiment_count += 1

    print('Experiment #{}'.format(experiment_count))
    start = time()
    n_better = []
    n_worse = []
    n_same = []
    best_fitness = []
    mean_fitness = []
    std_fitness = []
    test_error = []
    for i in range(0, 1):
        print(i, end=', ')

        result = evolution(params, ev_params, X_train, y_train)

        stats = result['stats']
        best_fitness.append([x.fitness for x in stats['best_of_generation']])
        mean_fitness.append(stats['mean_of_generation'])
        std_fitness.append(stats['std_of_generation'])
        n_better.append(stats['gem_better_after'])
        n_worse.append(stats['gem_worse_after'])

        index_of_best = np.argmin(best_fitness)
        test_error.append(ev_params.cost_function(y_test,
            stats['best_of_generation'][index_of_best].execute(X_test)))

    # make the best_fitness and mean_fitness lists the lists with same length
    for measurement in [best_fitness, mean_fitness]:
        longest = max([len(x) for x in measurement]) # since we know its only 2D its faster than np.max
        for l in measurement:
            extension = [l[-1]] * (longest - len(l))
            l.extend(extension)

    iob = np.unravel_index(np.argmin(best_fitness), np.array(best_fitness).shape)    
    results = [
        np.min(best_fitness), # best fitness of all
        mean_fitness[iob[0]][iob[1]], # best generation mean
        std_fitness[iob[0]][iob[1]], # std generation mean
        # TODO
        # get best test error and mean and std of test error
        np.min(test_error), # best test error
        np.mean(test_error), # mean of test error
        np.std(test_error), # std of test error
        np.sum(n_better), # total number of better after gem
        np.mean(n_better), # averge number of better after gem
        np.sum(n_worse), # total number of worse after gem
        np.mean(n_worse) # average number of worse after gem
    ]
    end = time()
    print('wall time {}'.format(end-start))

    # avg_gstat = reduce(add, gstat)/len(gstat) 
    return results, np.mean(best_fitness, axis=0), np.mean(mean_fitness, axis=0) #, avg_gstat

columns = [
    'mutation',
    'strategy',
    'gems',
    'n_cols',
    'overall_best',
    'overall_best_mean',
    'overall_best_std',
    'test_error_best',
    'test_error_mean',
    'test_error_std',
    'better_gems_total',
    'better_gems_mean',
    'worse_gems_total',
    'worse_gems_mean'
]

data = pd.DataFrame(columns=columns)

output_folder = 'bin_class_out/'

# params to change
# mutation, gems, expire, cols,
from pycgp.gems import MatchPMStrategy, MatchSMStrategy, MatchByActiveStrategy
from pycgp import point_mutation, probabilistic_mutation, single_mutation

mutations = [
        (point_mutation, MatchPMStrategy),
        (single_mutation, MatchSMStrategy),
        (single_mutation, MatchByActiveStrategy),
        (probabilistic_mutation, MatchSMStrategy),
        (probabilistic_mutation, MatchByActiveStrategy)]

for mutation, strategy in mutations:
    for gems in [0, 5, 10]:
        ev_params = EvParams(
            EV_PARAMS['cost_func'],
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
                funset=PARAMS['funset'])

            row = [mutation.__name__, strategy.__name__, gems, n_cols]

            random.seed(1)

            filename = f'{output_folder}{mutation.__name__}-{strategy.__name__}-gems{gems}-n_cols{n_cols}.csv'
            print(filename)
            gem_data, best_fitness, mean_fitness = run_experiment(
                params, ev_params, X_train, y_train)

            row += gem_data

            data.loc[experiment_count] = row

            fitness_data = pd.DataFrame()
            fitness_data['best_fitness'] = best_fitness
            fitness_data['mean_fitness'] = mean_fitness
            fitness_data.to_csv(filename)

            # gstat.to_csv(f'gstats-{filename}')

data.to_csv(f'{output_folder}result.csv', sep=',')
