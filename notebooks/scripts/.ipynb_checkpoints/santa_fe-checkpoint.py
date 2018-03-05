from pycgp.benchmarks.santafe import PARAMS, EV_PARAMS, X, santafe_cost_function
from pycgp.evolution import evolution
from pycgp.counter import Counter
import random
import numpy as np
from time import time
import pandas as pd

experiment_count = 0
y=None

def run_experiment(params, ev_params, x, y):
    global experiment_count
    experiment_count += 1

    print('Experiment #{}'.format(experiment_count))
    start = time()
    rstat = []
    n_better = []
    n_worse = []
    n_same = []
    for i in range(0, 10):
        print(i, end=', ')

        result = evolution(PARAMS, EV_PARAMS, X, None)

        rstat.append([EV_PARAMS['cost_func'](y, individual.execute(X)) for individual in result['final']])
        n_better.append(Counter.get().dict['g_better'])
        n_worse.append(Counter.get().dict['g_worse'])
        n_same.append(Counter.get().dict['g_same_as_parent'])
        
    
    #print('Best fitness: {}'.format(np.min(stats)))
    #print('mean and std of fitness of last generation: {}, {}'.format(np.mean(stats), np.std(stats)))
    #print('Mean and std of best fitness: {}, {}'.format(np.mean(np.min(stats, axis=1)), np.std(np.min(stats, axis=1))))
    # best fitness, mean of last generation, std of last generation, mean of best individual, std of best individual
    results = [
        np.min(rstat), np.mean(rstat), np.std(rstat), np.mean(np.min(rstat, axis=1)), np.std(np.min(rstat, axis=1)),
        np.sum(n_better), np.mean(n_better),
        np.sum(n_worse), np.mean(n_worse),
        np.sum(n_same), np.mean(n_same)
    ]
    print(results)
    end = time()
    print('wall time {}'.format(end-start))
    return results

from pycgp.mutation import point_mutation
all_measurements = {}
EV_PARAMS['gems'] = 0
EV_PARAMS['mutation'] = point_mutation
EV_PARAMS['expire_gems'] = 0
#
# POINT MUTATION 
# without gems
# 
random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# POINT MUTATION
# with gems, 5, expire 0
#
EV_PARAMS['gems'] = 5

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# POINT MUTATION
# with gems, 5, expire 30
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)


#
# POINT MUTATION
# with gems, 10, expire 30
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# POINT MUTATION
# with gems, 10, expire 0
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

df = pd.DataFrame.from_dict(all_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/santafe_pm.csv')

#########################################################################
#
# Single mutation, match all
#
#########################################################################


from pycgp.mutation import single_mutation
from pycgp.gems import GemSM, MatchSMStrategy
all_measurements = {}
EV_PARAMS['gems'] = 0
EV_PARAMS['gem_type'] = GemSM
EV_PARAMS['match_strategy'] = MatchSMStrategy
EV_PARAMS['mutation'] = single_mutation

EV_PARAMS['expire_gems'] = 0

#
# SINGLE MUTATION 
# without gems
# 
random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# SINGLE MUTATION
# with gems, 5, expire 0
#
EV_PARAMS['gems'] = 5

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# SINGLE MUTATION
# with gems, 5, expire 30
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)


#
# with gems, 10, expire 0
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# with gems, 10, expire 30
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

df = pd.DataFrame.from_dict(all_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/santafe_sm_all.csv')



#########################################################################
#
# Single mutation, match active
#
#########################################################################


from pycgp.mutation import single_mutation
from pycgp.gems import MatchByActiveStrategy
all_measurements = {}
EV_PARAMS['gems'] = 0
EV_PARAMS['gem_type'] = GemSM
EV_PARAMS['match_strategy'] = MatchByActiveStrategy
EV_PARAMS['mutation'] = single_mutation


#
# SINGLE MUTATION 
# without gems
# 
random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# SINGLE MUTATION
# with gems, 5, expire 0
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# SINGLE MUTATION
# with gems, 5, expire 30
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)


#
# SINGLE MUTATION
# with gems, 10, expire 30
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# SINGLE MUTATION
# with gems, 10, expire 0
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

df = pd.DataFrame.from_dict(all_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/santafe_sm_active.csv')




#########################################################################
#
# Probabilistic mutation, match all
#
#########################################################################


from pycgp.mutation import probabilistic_mutation
all_measurements = {}
EV_PARAMS['gems'] = 0
EV_PARAMS['gem_type'] = GemSM
EV_PARAMS['match_strategy'] = MatchSMStrategy
EV_PARAMS['mutation'] = probabilistic_mutation


#
# without gems
# 
random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# with gems, 5, expire 0
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# with gems, 5, expire 30
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)


#
# with gems, 10, expire 30
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# with gems, 10, expire 0
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

df = pd.DataFrame.from_dict(all_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/santafe_probm_all.csv')


#########################################################################
#
# Probabilistic mutation, match active
#
#########################################################################


from pycgp.mutation import probabilistic_mutation
all_measurements = {}
EV_PARAMS['gems'] = 0
EV_PARAMS['gem_type'] = GemSM
EV_PARAMS['match_strategy'] = MatchByActiveStrategy
EV_PARAMS['mutation'] = probabilistic_mutation


#
# without gems
# 
random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# with gems, 5, expire 0
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# with gems, 5, expire 30
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)


#
# with gems, 10, expire 30
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)

#
# with gems, 10, expire 0
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
all_measurements['10,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 50
all_measurements['50,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

random.seed(1)
PARAMS['n_cols'] = 100
all_measurements['100,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)

df = pd.DataFrame.from_dict(all_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/santafe_probm_active.csv')
