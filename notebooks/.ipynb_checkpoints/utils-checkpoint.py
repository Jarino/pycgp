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
            (probabilistic_mutation, MatchSMStrategy),
            (point_mutation, MatchPMStrategy),
            (single_mutation, MatchSMStrategy),
            (single_mutation, MatchByActiveStrategy),
            (probabilistic_mutation, MatchByActiveStrategy)
        ]
        self.gems = [0, 5, 10]
        
        self.cols = [10, 50, 100]
        
        self.folder = folder  
    
    def iterate_folder(self):
        for index, ((mutation, strategy), gem, column) in enumerate(product(self.mutations, self.gems, self.cols)):
            file = os.path.join(self.folder,  f'{mutation.__name__}-{strategy.__name__}-gems{gem}-n_cols{column}.csv')
            with open (file, 'rb') as fp:
                data = pickle.load(fp)

                yield mutation.__name__, strategy.__name__, gem, column, data
    
    def iterate_axes(self, value_gttr, choices = None, figsize=None):
        data = []
        for m, s, g, c, raw in self.iterate_folder():
            data.append([g,m,s] + [value_gttr(x) for x in raw])
        
        df = pd.DataFrame(data)
        df.columns = ['gems', 'mutation', 'strategy', *list(range(1, len(data[0]) - 2))]
        
        if choices is None:
            choices = self.mutations
        
        if figsize is None:
            figsize = (12,3)
        
        _, axs = plt.subplots(1,len(choices), figsize=figsize)

        for i, (m, s) in enumerate(choices):
            for g in self.gems:
                d = df[(df.mutation == m.__name__) & (df.strategy == s.__name__)]
                values = d.iloc[:,3:][d.gems == g].values.flatten()
                axs[i].set_title(f'{m.__name__}\n{s.__name__}')
                yield m, s, g, axs[i], values
        