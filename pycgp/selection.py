""" Selection operators for evolution """


def truncation_selection(population, n_best):
    """ Sort the individuals according to their fitness and
    pick the first `n_best` for reproduction 
    returns a tuple, with individual and its fitness 
    """

    sorted_population = sorted(population, key=lambda x: x.fitness)

    return sorted_population[0:n_best]
