from pycgp.benchmarks.classification import X_train, y_train, X_test, y_test, PARAMS, EV_PARAMS
from pycgp.evolution import evolution
from pycgp.counter import Counter
import random
import numpy as np
from time import time
import pandas as pd

experiment_count = 0
X = None
y = None
def run_experiment(PARAMS,EV_PARAMS, dum1, dum2):
    global experiment_count
    experiment_count += 1
    print('Experiment #{}'.format(experiment_count))
    start = time()
    
    n_better = []
    n_worse = []
    n_same = []
    
    train_stat = []
    test_stat = []
    for i in range(0, 5):
        print(i, end=', ')
        result = evolution(PARAMS, EV_PARAMS, X_train, y_train)
        
        train_stat.append([x.fitness for x in result['final']])
        test_stat.append([EV_PARAMS['cost_func'](y_test, x.execute(X_test)) for x in result['final']   ])
        n_better.append(Counter.get().dict['g_better'])
        n_worse.append(Counter.get().dict['g_worse'])
        n_same.append(Counter.get().dict['g_same_as_parent'])
    
    
    train_results = [
        np.min(train_stat), # best fitness
        np.mean(train_stat), # mean of fitnesses of all last generations
        np.std(train_stat), # std of fitnesses of all last generations
        np.mean(np.min(train_stat, axis=1)), # mean of best individuals from run
        np.std(np.min(train_stat, axis=1)), # std of best individuals from run
        np.sum(n_better), np.mean(n_better),
        np.sum(n_worse), np.mean(n_worse),
        np.sum(n_same), np.mean(n_same)
    ]
    
    test_results = [
        np.min(test_stat), # best fitness
        np.mean(test_stat), # mean of fitnesses of all last generations
        np.std(test_stat), # std of fitnesses of all last generations
        np.mean(np.min(test_stat, axis=1)), # mean of best individuals from run
        np.std(np.min(test_stat, axis=1)), # std of best individuals from run
        np.sum(n_better), np.mean(n_better),
        np.sum(n_worse), np.mean(n_worse),
        np.sum(n_same), np.mean(n_same)
    ]
    print('Train: ', train_results)
    print('Test: ', test_results)
    end = time()
    print('wall time {}'.format(end-start))
    return train_results, test_results
        
        

from pycgp.mutation import point_mutation
train_measurements = {}
test_measurements = {}
EV_PARAMS['gems'] = 0
EV_PARAMS['mutation'] = point_mutation
EV_PARAMS['expire_gems'] = 0
#
# POINT MUTATION 
# without gems
# 
random.seed(1)
PARAMS['n_cols'] = 10
key = '10,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 5, expire 0
#
EV_PARAMS['gems'] = 5

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]



random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 5, expire 30
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]


#
# POINT MUTATION
# with gems, 10, expire 30
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 10, expire 0
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

df = pd.DataFrame.from_dict(train_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/binclass_pm_train.csv')

df = pd.DataFrame.from_dict(train_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/binclass_pm_test.csv')

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
key = '10,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 5, expire 0
#
EV_PARAMS['gems'] = 5

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 5, expire 30
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]


#
# POINT MUTATION
# with gems, 10, expire 30
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 10, expire 0
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

df = pd.DataFrame.from_dict(train_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/binclass_sm_all_train.csv')

df = pd.DataFrame.from_dict(train_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/binclass_sm_all_test.csv')


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
key = '10,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 5, expire 0
#
EV_PARAMS['gems'] = 5

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 5, expire 30
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]


#
# POINT MUTATION
# with gems, 10, expire 30
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 10, expire 0
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

df = pd.DataFrame.from_dict(train_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/binclass_sm_active_train.csv')

df = pd.DataFrame.from_dict(train_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/binclass_sm_active_test.csv')



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
key = '10,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 5, expire 0
#
EV_PARAMS['gems'] = 5

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 5, expire 30
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]


#
# POINT MUTATION
# with gems, 10, expire 30
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 10, expire 0
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

df = pd.DataFrame.from_dict(train_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/binclass_probm_all_train.csv')

df = pd.DataFrame.from_dict(train_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/binclass_probm_all_test.csv')

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
key = '10,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,0,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,0,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 5, expire 0
#
EV_PARAMS['gems'] = 5

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,5,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,5,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 5, expire 30
#
EV_PARAMS['gems'] = 5
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,5,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,5,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]


#
# POINT MUTATION
# with gems, 10, expire 30
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 0

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,10,0'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,10,0'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

#
# POINT MUTATION
# with gems, 10, expire 0
#
EV_PARAMS['gems'] = 10
EV_PARAMS['expire_gems'] = 30

random.seed(1)
PARAMS['n_cols'] = 10
#all_measurements['10,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '10,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 50
#all_measurements['50,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '50,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

random.seed(1)
PARAMS['n_cols'] = 100
#all_measurements['100,10,30'] = run_experiment(PARAMS, EV_PARAMS, X, y)
key = '100,10,30'
results = run_experiment(PARAMS, EV_PARAMS, X, y)
train_measurements[key] = results[0]
test_measurements[key] = results[1]

df = pd.DataFrame.from_dict(train_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/binclass_probm_actve_train.csv')

df = pd.DataFrame.from_dict(train_measurements, orient='index')
df.columns = ['best fitness', 'mean of last gen', 'std of last gen', 'mean of best individual', 'std of best indvidiual',
             'g_better', 'g_better avg', 'g_worse', 'g_worse avg', 'g_same', 'g_same avg']
df.to_csv('out/binclass_probm_active_test.csv')