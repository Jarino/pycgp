from pycgp.individual_builder import IndividualBuilder
from pycgp.selection import truncation_selection
from pycgp.mutation import point_mutation, active_mutation, single_mutation
from pycgp.params import DEFAULT_PARAMS

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

builder = IndividualBuilder(DEFAULT_PARAMS)

population = [builder.build() for _ in range(0, 5)]
prev_fitness = 0

for gen in range(0, 1000):
    output = [i.execute(X) for i in population]

    fitness = []
    for index, y_pred in enumerate(output):
        fit = mean_squared_error(y, y_pred)
        fitness.append(fit)


    parent, parent_fitness = truncation_selection(population, fitness, 1)[0]

    if gen % 200 == 0:
        print(gen, parent_fitness)

    population = [single_mutation(parent) for _ in range(0,4)] + [parent]

print(gen, parent_fitness)

output = [i.execute(X) for i in population]

fitness = [mean_squared_error(y, y_pred) for y_pred in output]

print('functions:')
for ind, fit in zip(population, fitness):
    print(ind, fit)

print(fitness)



