""" Selection operators for evolution """


def truncation_selection(population, fitness, n_best):
    """ Sort the individuals according to their fitness and
    pick the first `n_best` for reproduction 
    returns a tuple, with individual and its fitness 
    """

    sorted_population = sorted(zip(population, fitness), key=lambda x: x[1])

    return sorted_population[0:n_best]
