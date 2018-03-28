import random

from pycgp import Params, EvParams
from pycgp.evolution import evolution
from pycgp.benchmarks.classification import *


params = Params(30, 1, funset=funset)
ev_params = EvParams(cost_func, target_fitness=-1)

random.seed(1)

res = evolution(params, ev_params, X_train, y_train)