""" Mutation operations """

from random import randint

def point_mutation(individual):
    """ perform a point mutation on given individual """

    index = randint(0, len(individual))

    upper_bound = individual.bounds[index]

    new_individual = individual.copy()

    new_individual.genes[index] = randint(0, upper_bound)

    return new_individual




