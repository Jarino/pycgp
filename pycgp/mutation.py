""" Mutation operations """

from random import randint

from pycgp.individual import Individual


def point_mutation(individual):
    """ perform a point mutation on given individual """

    index = randint(0, len(individual) - 1)

    genes = individual.genes[:]

    bounds = individual.bounds  # this does not change

    params = individual.params

    genes[index] = randint(0, bounds[index])

    return Individual(genes, bounds, params)
