from pycgp.individual_builder import IndividualBuilder
from pycgp.gems import JewelleryBox, Gem, GemPheno, MatchGenotypeStrategy
from pycgp.selection import truncation_selection
from pycgp.mutation import point_mutation
from pycgp.counter import Counter

from pdb import set_trace

def evolution(cgp_params, ev_params, X, y, verbose=False):
    """
    ev_params fields:
    - cost_func: callable, cost function, recieving target vector and computed vector as parameters
    - target_fitness: int, target fitness upon which reaching terminate the evolution
    - gems: bool, whether to use gems extension in evolution, defaults to False
    - j_box_size: int, maximum capacity of jewellery box, defaults to 5
    - max_evaluations: int, maximum number of cost function evaluations, upon which evolution will be stopped, defaults to 5000
    - pop: int, number of individuals in population, defaults to 5
    - selection: callable, selection operator
    - mutation: callable, mutation operator
    - match_strategy
    - gem_type
    """
    builder = IndividualBuilder(cgp_params)
    mutation = ev_params.get('mutation', point_mutation)
    selection = ev_params.get('selection', truncation_selection)
    pop_size = ev_params.get('pop', 5)
    apply_gem = ev_params.get('gems', False)
    cost_func = ev_params['cost_func']
    gem_type = ev_params.get('gem_type', Gem)
    match_strategy = ev_params.get('match_strategy', MatchGenotypeStrategy)


    population = [builder.build() for _ in range(0, pop_size)]
    evaluations_counter = 0
    Counter.get().dict['g_better'] = 0
    Counter.get().dict['g_worse'] = 0

    j_box = JewelleryBox(match_strategy(), max_size=ev_params.get('j_box_size', 5))

    for individual in population:
        output = individual.execute(X)
        individual.fitness = ev_params['cost_func'](y, output)
        evaluations_counter += 1
   
    Counter.get().dict['gens'] = 0
    gens = 0
    while evaluations_counter < ev_params.get('max_evaluations', 5000):
        gens += 1
        #set_trace()
        parent = selection(population, 1)[0]

        if parent.fitness <= ev_params['target_fitness']:
            break
        
        population = []
        m_indices = []
        for _ in range(0, pop_size - 1):
            individual, mutated_index = mutation(parent)
            population.append(individual)
            m_indices.append(mutated_index)

            if parent == individual:
                individual.fitness = parent.fitness
            else:
                # place the gem application here?
                # then it wouldn't be necessary to evaluate individual twice
                # on the other hand, it also would not be possible to 
                # store the gem, because we need to compute the fitness gain
                output = individual.execute(X)
                individual.fitness = cost_func(y, output)
                evaluations_counter += 1
        
        

        if not apply_gem:
            # skip this whole gem-jewellery mumbo-jumbo
            population = population + [parent]
            continue

        for index, (individual, m_index) in enumerate(zip(population, m_indices)):
            if individual.fitness < parent.fitness:
                j_box.add(gem_type(individual, parent, m_index))
            else:
                # apply gem
                matching_gem = j_box.match(individual)
                if matching_gem is not None:
                    new_individual = matching_gem.apply(individual)
                    # recalculate fitness
                    new_individual.fitness = cost_func(y, new_individual.execute(X))
                    if new_individual.fitness < individual.fitness:
                        Counter.get().dict['g_better'] += 1
                        population[index] = new_individual
                    else:
                        Counter.get().dict['g_worse'] += 1
                    evaluations_counter += 1 

        population = population + [parent]

    Counter.get().dict['gens'] = gens
    s_pop = sorted(population, key=lambda x: x.fitness)

    if verbose:
        print('Evolution ended with {} of cost function evaluations'.format(evaluations_counter))
        print('Final population:')
        for ind in s_pop:
            print('Fitness: {}, function: {}'.format(ind.fitness, ind))

    
    results = {
            'evals': evaluations_counter,
            'final': s_pop
    }

    return results

