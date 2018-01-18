from pycgp.individual_builder import IndividualBuilder
from pycgp.selection import truncation_selection
from pycgp.mutation import point_mutation, active_mutation, single_mutation
from pycgp.params import DEFAULT_PARAMS
from pycgp.gems import JewelleryBox, Gem, MatchPhenotypeStrategy, GemPheno

from pycgp.evolution import evolution

import numpy as np

from sklearn.metrics import mean_squared_error

import math
import pdb

x_range = np.arange(-50,50,0.5)
y = x_range**4 + x_range**3 + x_range**2 + x_range
X = np.array([x_range]).T

DEFAULT_PARAMS['n_rows'] = 1
DEFAULT_PARAMS['n_cols'] = 15
DEFAULT_PARAMS['n_inputs'] = 1
DEFAULT_PARAMS['n_outputs'] = 1

ev_params = {
        'cost_func': mean_squared_error,
        'target_fitness': 0,
        'gems': True,
        'selection': truncation_selection,
        'mutation': point_mutation,
        'match_strategy': MatchPhenotypeStrategy,
        'gem_type': GemPheno
        }



evolution(DEFAULT_PARAMS, ev_params, X, y)
