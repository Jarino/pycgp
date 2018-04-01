import random
from time import time
from copy import deepcopy
import pickle
import os

from experiment import experiment_loop

from pycgp.gems import MatchPMStrategy, MatchSMStrategy, MatchByActiveStrategy
from pycgp import point_mutation, probabilistic_mutation, single_mutation
from pycgp.benchmarks.classification import *

experiment_count = 0

output_folder = 'bin_class_out'

mutations = [
        (point_mutation, MatchPMStrategy),
        (single_mutation, MatchSMStrategy),
        (single_mutation, MatchByActiveStrategy),
        (probabilistic_mutation, MatchSMStrategy),
        (probabilistic_mutation, MatchByActiveStrategy)]

gems_range = [5, 10]
n_cols_range = [10, 50, 100]

experiment_loop(
    output_folder,
    mutations,
    n_cols_range,
    gems_range,
    cost_func,
    {'target_fitness': -1},
    {'n_inputs': 30, 'n_outputs': 1, 'funset': funset},
    X_train,
    y_train,
    X_test,
    y_test
    )