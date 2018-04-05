import os 
import pickle
from itertools import product

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pycgp import probabilistic_mutation, point_mutation, single_mutation
from pycgp.gems import MatchByActiveStrategy, MatchSMStrategy, MatchPMStrategy

class DataIterator():
    def __init__(self, folder):
        self.mutations = [
          #  (probabilistic_mutation, MatchSMStrategy),
            (point_mutation, MatchPMStrategy),
            (single_mutation, MatchSMStrategy),
            (single_mutation, MatchByActiveStrategy),
            (probabilistic_mutation, MatchByActiveStrategy)
        ]
        self.gems = [5, 10]
        
        self.cols = [10, 50, 100]
        
        data = []
        for m,s,g,c,dd in self.__iterate_folder(folder):
            data.append([m, s, g, c, [x['ga_values'] for x in dd]])
        data = pd.DataFrame(data)
        data.columns = ['m', 's', 'g', 'c', 'gem_data']
        self.data = data      
    
    def __iterate_folder(self,folder):
        for index, ((mutation, strategy), gem, column) in enumerate(product(self.mutations, self.gems, self.cols)):
            file = os.path.join(folder,  f'{mutation.__name__}-{strategy.__name__}-gems{gem}-n_cols{column}.csv')
            with open (file, 'rb') as fp:
                data = pickle.load(fp)

                yield mutation.__name__, strategy.__name__, gem, column, data
    
    def iterate_gem_data(self, mutation, strategy, axis=False):
        gdatas = self.data[(self.data.m == mutation) & (self.data.s == strategy) & (self.data.g != 0)]

        if axis:
            _, axs = plt.subplots(2, len(gdatas)//2, figsize=(8,6))

        for i, (_, gdata) in enumerate(gdatas.iterrows()):
            pgdata = []
            #pdb.set_trace()
            for gem in [item for sublist in gdata.gem_data for item in sublist]:
                row = [gdata.g, gdata.c, gdata.g, gdata.c, gem.match_checks, gem.match_count, gem.n_uses, gem.value, gem.match_probability, gdata.better_after, gdata.worse_after, gdata.safe_after, gem[0], gem[1], gem[2]]
                pgdata.append(row)

            pgdata = pd.DataFrame(pgdata)
            pgdata.columns = ['gems', 'columns', 'match_checks', 'match_count', 'n_uses', 'value', 'match_probability', 'better_after', 'worse_after', 'same_after', 'stored_value', 'new_value', 'old_value']
            pgdata['gain'] = pgdata['old_value'] - pgdata['new_value']
            pgdata['success_rate_counts'] = pgdata.n_uses / pgdata.match_count
            pgdata['success_rate_checks'] = pgdata.n_uses / pgdata.match_checks
            
            if axis:
                yield pgdata, axs[i//3][i%3]
            else:
                yield pgdata, None
    
    def stats(self):
        frames = []
        for m, s in self.mutations:
            for pgdata, _ in self.iterate_gem_data(m.__name__, s.__name__):
                pgdata['m'] = m.__name__
                pgdata['s'] = s.__name__
                frames.append(pgdata)
        data = pd.concat(frames)
        return data

#import pdb
            

#symreg = DataIterator('scripts/symbolic_basic/')


def density_plots(folder, value_gttr):
    best = []

    for raw in iterate_folder(folder):
            m, s, g, c, data = raw
            best.append([g, m, s] + [value_gttr(x) for x in data])

    df = pd.DataFrame(best)
    df.columns = ['gems', 'mutation', 'strategy', *list(range(1,21))]

    _, axs = plt.subplots(1,3, figsize=(12,3))

    choices = [
        (point_mutation.__name__, MatchPMStrategy.__name__),
        (single_mutation.__name__, MatchSMStrategy.__name__),
        (probabilistic_mutation.__name__, MatchByActiveStrategy.__name__)
    ]

    titles = ['Point mutation', 'Single mutation', 'Probabilistic mutation']
    
    ylims = [
        (0, 20), (0, 20), (0, 20)
    ]
    
    for i, (m, s) in enumerate(choices):
        avgs = []
        nonzero = []
        for g in gems:
            d = df[(df.mutation == m) & (df.strategy == s)]
            values = d.iloc[:,3:][d.gems == g].values.flatten()
            sns.kdeplot(values, ax=axs[i], label=g, shade=True)
            avgs.append(np.mean(values)*100)
            nonzero.append(np.count_nonzero(values == 0))
            
        axs[i].set_title('{}\n{}\n0 - {:3f}, {}\n5 - {:3f}, {}\n10 - {:3f}, {}'.format(m,s,avgs[0], nonzero[0], avgs[1], nonzero[1], avgs[2], nonzero[2]))
        print('{}\n{}\n0 - {:3f}, {}\n5 - {:3f}, {}\n10 - {:3f}, {}'.format(m,s,avgs[0], nonzero[0], avgs[1], nonzero[1], avgs[2], nonzero[2]))
        axs[i].set_title(titles[i])
        axs[i].set_xlabel('Accuracy score')
        axs[i].set_ylim(ylims[i])
        axs[i].set_xlim(0.75, 1)
    print(df.groupby('gems').median().mean(axis=1))
