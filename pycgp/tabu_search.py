""" Search for the solution using the Tabu Search metaheuristic """

from pycgp.individual_builder import IndividualBuilder

def tabu_search(cgp_params, ev_params, X, y, verbose=False):
    ib = IndividualBuilder(cgp_params)

    parent = ib.build()

    output = parent.execute(X)
    parent.fitness = ev_params.cost_function(y, output)
    n_evals = 1


    moves = []
    tabu_set = set()
    fitnesses = []

    while n_evals < ev_params.max_evaluations:
        fitnesses.append(parent.fitness)
        # create new individual 
        child, m_index = ev_params.mutation(
                parent, ev_params.mutation_probability)
        
        move = (m_index, child.genes[m_index])

        if move in tabu_set:
            continue
           
        moves.append(move)

        # evaluate the individual
        if parent == child:
            child.fitness = parent.fitness
        else:
            output = child.execute(X)
            child.fitness = ev_params.cost_function(y, output)
            n_evals += 1

        # replace if better
        if child.fitness <= parent.fitness:
            parent = child
            tabu_set.add(move)

        if len(tabu_set) > 15:
            tabu_set.pop()
            

    return child, moves, tabu_set, fitnesses

        
