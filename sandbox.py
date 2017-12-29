from individual_builder import IndividualBuilder
from selection import truncation_selection
from mutation import point_mutation
from params import DEFAULT_PARAMS

from sklearn import datasets
from sklearn.metrics import mean_squared_error

import math
import pdb

data = datasets.load_iris()
X = data.data
Y = data.target

DEFAULT_PARAMS['n_rows'] = 1
DEFAULT_PARAMS['n_cols'] = 3
DEFAULT_PARAMS['n_inputs'] = 4
DEFAULT_PARAMS['n_outputs'] = 1

builder = IndividualBuilder(DEFAULT_PARAMS)

population = [builder.build() for _ in range(0, 5)]
prev_fitness = 0

for gen in range(0, 500):
    output = [i.execute(X) for i in population]

#    pdb.set_trace()

    fitness = [mean_squared_error(Y, y_pred) for y_pred in output]

    parent, parent_fitness = truncation_selection(population, fitness, 1)[0]

    print(gen, parent_fitness)

    population = [point_mutation(parent) for _ in range(0,4)] + [parent]


output = [i.execute(X) for i in population]

fitness = [mean_squared_error(Y, y_pred) for y_pred in output]

print(fitness)



