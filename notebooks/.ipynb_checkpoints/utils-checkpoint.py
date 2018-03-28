import os 
import pickle
from itertools import product

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file, minimization=True, has_test_error=False):
    """
    Load data from Pickle dump
    Returns raw measurement data, agg list, best_fitness vectors, mean_fitness vectors
    agg list contains:
    - best of all, 
    - mean fitness of generation with best
    - std fitness of generation with best
    - mean count of gems created
    
    """
    if minimization:
        argmin_fn = np.argmin
        min_fn = np.min
    else:
        argmin_fn = np.argmax
        min_fn = np.max
    
    with open (file, 'rb') as fp:
        data = pickle.load(fp)

   # print(data[0].keys())
    
    best_fitness = [x['best_fitness'] for x in data]
    mean_fitness = [x['mean_of_generation'] for x in data]
    std_fitness  = [x['std_of_generation'] for x in data]
    gems_count   = [len(x['gem_data']) for x in data]
    gem_better   = [x['gem_better_after'] for x in data]
    gem_worse    = [x['gem_worse_after'] for x in data]
    
    if has_test_error:
        test_error = [x['test_error'] for x in data]
    
    for measurement in [best_fitness, mean_fitness]:
        longest = max([len(x) for x in measurement]) # since we know its only 2D its faster than np.max
        for l in measurement:
            extension = [l[-1]] * (longest - len(l))
            l.extend(extension)
    
    iob = np.unravel_index(argmin_fn(best_fitness), np.array(best_fitness).shape)
    agg = [
        min_fn(best_fitness),
        mean_fitness[iob[0]][iob[1]],
        std_fitness[iob[0]][iob[1]],
        np.mean(gems_count),
        np.mean(gem_better),
        np.mean(gem_worse)
    ]
    
    if has_test_error:
        agg.append(test_error[iob[0]])
    
        
    return data, agg, best_fitness, mean_fitness


def aggregate_statistics(folder, mutations, has_test_error=False):
    """
    Create aggregate dataframe for data files in given folder
    Mutations is a list of tuples specifying which files should be loaded
    """
    gems = [0, 5, 10]
    columns = [10, 50, 100]

    column_names = ['mutation', 'strategy', 'gems', 'columns','best', 'mean', 'std', 'avg_gem_count', 'gem_better', 'gem_worse']
    
    if has_test_error:
        column_names.append('test_error')
        
    column_names += ['bf', 'mf']

    data = pd.DataFrame(columns=column_names)
    bf = []
    mf = []

    for index, ((mutation, strategy), gem, column) in enumerate(product(mutations, gems, columns)):
        file = os.path.join(folder,  f'bin_class_out{mutation.__name__}-{strategy.__name__}-gems{gem}-n_cols{column}.csv')

        row = [mutation.__name__, strategy.__name__, gem, column]

        raw, agg, best_fitness, mean_fitness = load_data(file, has_test_error=has_test_error)

        row += [*agg, np.mean(best_fitness, axis=0), np.mean(mean_fitness, axis=0)]
        
        data.loc[index] = row

    return data


def plot_fitnesses(data, mutation_type, ylim):
    """
    Plot the fitnesses grouped by gems count
    """
    prob_data = data[data['mutation'] == mutation_type][['gems','bf']]
    plt_data = pd.DataFrame([*prob_data['bf']])
    plt_data['gems'] = prob_data['gems'].values

    fig, ax = plt.subplots(1,2)
    plt_data.groupby('gems').min().T.plot(ax=ax[0])
    plt_data.groupby('gems').max().T.plot(ax=ax[1])
    ax[0].set_ylim(*ax[1].set_ylim(*ylim))
    ax[0].set_title('best run')
    ax[1].set_title('mean of all runs')
    fig.suptitle(mutation_type);
    
def plot_distributions(folder, mutations):    
    gems = [0,5,10]
    columns = [10,50,100]

    hist_data = []
    names = []

    for index, ((mutation, strategy), gem, column) in enumerate(product(mutations, gems, columns)):
        file = os.path.join(folder,  f'{mutation.__name__}-{strategy.__name__}-gems{gem}-n_cols{column}.csv')
        raw, _, _, _ = load_data(file)

        [hist_data.append([gem, x['best'].fitness]) for x in raw]


    hist_data = pd.DataFrame(hist_data)
    hist_data
    hist_data.columns = ['gems', 'best']


    for x in [0, 5, 10]:
        sns.kdeplot(hist_data[hist_data.gems==x]['best'], label=x, shade=True)
