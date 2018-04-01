from pycgp.benchmarks.santafe import *
from pycgp import Params, EvParams
from time import time

from experiment import experiment_loop

output_folder = 'santa_fe_out/'

from pycgp.gems import MatchPMStrategy, MatchSMStrategy, MatchByActiveStrategy
from pycgp import point_mutation, probabilistic_mutation, single_mutation

mutations = [
        (point_mutation, MatchPMStrategy),
        (single_mutation, MatchSMStrategy),
        (single_mutation, MatchByActiveStrategy),
        (probabilistic_mutation, MatchSMStrategy),
        (probabilistic_mutation, MatchByActiveStrategy)]

gems_range = [0, 5, 10]

n_cols_range = [10, 50, 100]

experiment_loop(
    output_folder,
    mutations,
    n_cols_range,
    gems_range,
    cost_func,
    {'target_fitness': target_fitness},
    {'n_inputs': 3, 'n_outputs': 1, 'funset': funset, 'arity': 3},
    X,
    None
)