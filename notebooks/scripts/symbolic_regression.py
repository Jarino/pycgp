import random
from time import time
import os
import pickle
from copy import deepcopy

from pycgp.benchmarks.symbolic import * 
from pycgp import Params, EvParams
from pycgp.evolution import evolution
from pycgp.gems import MatchPMStrategy, MatchSMStrategy, MatchByActiveStrategy
from pycgp import point_mutation, probabilistic_mutation, single_mutation

from experiment import experiment_loop

experiment_count = 0


mutations = [
        (single_mutation, MatchSMStrategy),
        (point_mutation, MatchPMStrategy),
        (probabilistic_mutation, MatchSMStrategy),
        (single_mutation, MatchByActiveStrategy),
        (probabilistic_mutation, MatchByActiveStrategy)]

gems_range = [5, 10]
n_cols_range = [10, 50, 100]

experiment_loop(
    'or_symbolic_basic_equal',

    mutations,
    n_cols_range,
    gems_range,
    cost_func,
    {'target_fitness': target_fitness},
    {'n_inputs': 1, 'n_outputs': 1, 'funset': funset},
    X,
    y
)

