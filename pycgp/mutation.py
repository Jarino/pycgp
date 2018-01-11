""" Mutation operations """

from random import randint
from random import choice

from pycgp.individual import Individual


def point_mutation(individual):
    """ perform a point mutation on given individual """

    index = randint(0, len(individual) - 1)

    genes = individual.genes[:]

    bounds = individual.bounds  # this does not change

    params = individual.params

    genes[index] = randint(0, bounds[index])

    return Individual(genes, bounds, params)


def single_mutation(individual):
    """ perform a 'single' mutation - mutate untile active gene is changed """

    active_changed = False
    genes = individual.genes[:]
    bounds = individual.bounds
    params = individual.params

    while not active_changed:
        index = randint(0, len(genes) - 1)
        genes[index] = randint(0, bounds[index])

        if individual.is_gene_active(index):
            active_changed = True
    
    return Individual(genes, bounds, params)


def active_mutation(individual):
    """ Perform an active mutation - to-be mutated gene is chosen only
    from active genes """

    active_changed = False
    genes = individual.genes[:]
    bounds = individual.bounds
    params = individual.params

    while not active_changed:
        index = randint(0, len(genes) - 1)

        if individual.is_gene_active(index):
            active_changed = True
            genes[index] = randint(0, bounds[index])
    
    return Individual(genes, bounds, params)

    
