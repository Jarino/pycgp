from pycgp.individual_builder import IndividualBuilder
from pycgp.selection import truncation_selection
from pycgp.mutation import point_mutation, active_mutation, single_mutation
from pycgp.params import DEFAULT_PARAMS
from pycgp.gems import JewelleryBox, Gem


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
fitness_evaluations = 0
gen = 0
target_fitness = 0

fitness_values = []
j_box = JewelleryBox(max_size=10)

for individual in population:
    output = individual.execute(X)
    if individual.fitness is None:
        individual.fitness = mean_squared_error(y, output)
        fitness_evaluations += 1

    fitness_values.append(individual.fitness)


while fitness_evaluations < 5000:
    gen += 1

    parent, parent_fitness = truncation_selection(population, fitness_values, 1)[0]

    if parent_fitness <= target_fitness:
        break

    if gen % 200 == 0:
        print(gen, parent_fitness)

    population = [point_mutation(parent) for _ in range(0,4)]

    fitness_values = []
    for individual in population:
        if parent == individual:
            individual.fitness = parent_fitness

        output = individual.execute(X)
        if individual.fitness is None:
            individual.fitness = mean_squared_error(y, output)
            fitness_evaluations += 1

        fitness_values.append(individual.fitness)

    for individual in population:
        if parent == individual:
            individual.fitness = parent_fitness

        continue

        if individual.fitness < parent_fitness:
            # create and store gem
            index, (original, mutated) = next(filter(
                    lambda x: x[1][0] != x[1][1],
                    enumerate(zip(parent.genes, individual.genes))
            ))
            j_box.add(Gem(index, original, mutated, parent_fitness - individual.fitness))
        else:
            # apply gem
            matching_gem = j_box.match(individual)
            if matching_gem is not None:
                individual = matching_gem.apply(individual)
                # recalculate fitness
                individual.fitness = mean_squared_error(y, individual.execute(X))
                fitness_evaluations += 1


    population = population + [parent]


print(gen, parent_fitness)
print('Number of fitness evaluations: {}'.format(fitness_evaluations))

output = [i.execute(X) for i in population]

fitness = [mean_squared_error(y, y_pred) for y_pred in output]

print('functions:')
for ind, fit in zip(population, fitness):
    print(ind, fit)

print(fitness)



