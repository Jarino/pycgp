from pycgp.individual_builder import IndividualBuilder
from pycgp.gems import JewelleryBox, GemSingleGene, MatchPMStrategy
from pycgp.selection import truncation_selection
from pycgp.mutation import point_mutation, probabilistic_mutation
from pycgp.counter import Counter

import statistics

from pycgp.individual import Individual


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
    - mutation_probability: float (0,1), probability of mutating a single gene, used only with probablisitic mutation
    """
    builder = IndividualBuilder(cgp_params)
    apply_gem = ev_params.gems_box_size
    target_fitness_is_set = ev_params.target_fitness is not None


    population = [builder.build() for _ in range(0, ev_params.population_size)]
    evaluations_counter = 0
    Counter.get().dict['g_better'] = 0
    Counter.get().dict['g_worse'] = 0
    Counter.get().dict['mean'] = []
    Counter.get().dict['best'] = []
    Counter.get().dict['g_better_fitness'] = []
    Counter.get().dict['remove_gem'] = 0
    Counter.get().dict['best_individual'] = []

    j_box = JewelleryBox(ev_params.gem_match_strategy(), max_size=apply_gem)

    for individual in population:
        output = individual.execute(X)
        individual.fitness = ev_params.cost_function(y, output)
        evaluations_counter += 1
   
    Counter.get().dict['gens'] = 0
    Counter.get().dict['g_same_as_parent'] = 0
    gens = 0
    while evaluations_counter < ev_params.max_evaluations:
        gens += 1
        # store mean of population and best
        Counter.get().dict['mean'].append(statistics.mean(
            [x.fitness for x in population]
        ))
        Counter.get().dict['best'].append(min(
            population, key=lambda x: x.fitness
        ).fitness)


        parent = ev_params.selection(population, 1)[0]
        Counter.get().dict['best_individual'].append(parent)

        if target_fitness_is_set and (parent.fitness <= ev_params.target_fitness):
            break
        
        population = []
        m_indices = []
        for _ in range(0, ev_params.population_size - 1):
            individual, mutated_index = ev_params.mutation(parent, ev_params.mutation_probability)
            population.append(individual)
            m_indices.append(mutated_index)

            if parent == individual:
                individual.fitness = parent.fitness
            else:
                output = individual.execute(X)
                individual.fitness = ev_params.cost_function(y, output)
                evaluations_counter += 1
       
        if not apply_gem:
            # skip this whole gem-jewellery mumbo-jumbo
            population = population + [parent]
            continue

        for index, (individual, m_index) in enumerate(zip(population, m_indices)):
            if individual.fitness < parent.fitness:
                Counter.get().dict['g_better_fitness'].append(individual.fitness - parent.fitness)
                j_box.add(
                    ev_params.gem_match_strategy.associated_gem_type(
                        individual, parent, m_index))
            else:
                # apply gem
                matching_gem = j_box.match(individual)
                if matching_gem is not None:
                    new_individual = matching_gem.apply(individual)

                    if new_individual is None:
                        Counter.get().dict['g_same_as_parent'] += 1
                    else:
                        # if gem exceeds 30 uses, remove
                        if ev_params.gem_expire and matching_gem.n_uses >= ev_params.gem_expire:
                            j_box.remove(matching_gem)

                        new_individual.fitness = ev_params.cost_function(y, new_individual.execute(X))
                        evaluations_counter += 1 
                        
                        if new_individual.fitness < individual.fitness:
                            Counter.get().dict['g_better'] += 1
                            population[index] = new_individual
                        else:
                            Counter.get().dict['g_worse'] += 1
                    
                        population[index] = new_individual


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

