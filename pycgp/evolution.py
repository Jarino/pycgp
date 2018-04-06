from pycgp.individual_builder import IndividualBuilder
from pycgp.gems import JewelleryBox, GemSingleGene, MatchPMStrategy
from pycgp.selection import truncation_selection
from pycgp.mutation import point_mutation, probabilistic_mutation
from pycgp.counter import Counter

import statistics
import pdb

from pycgp.individual import Individual

def initialize_stats_dict(tuples_with_init):
    stats = {}
    for key, init in tuples_with_init:
        stats[key] = init
    return stats

def evolution(cgp_params, ev_params, X, y, verbose=False):
    """
    Performs the evolutionary search defined by ev_params for CGP system defined
    by cgp_params on input data X and target data y
    """
    builder = IndividualBuilder(cgp_params)
    apply_gem = ev_params.gems_box_size
    target_fitness_is_set = ev_params.target_fitness is not None
    j_box = JewelleryBox(ev_params.gem_match_strategy(), max_size=apply_gem)
    stats = initialize_stats_dict([
        ('mean_of_generation', []),
        ('median_of_generation', []),
        ('std_of_generation', []),
        ('best_of_generation', []),
        ('best', None),
        ('gem_better_after', 0),
        ('gem_same_after', 0),
        ('ga_values', []),
        ('gem_worse_after', 0)
    ])
    evaluations_counter = 0
    Counter.get().dict['gems'] = []

    population = [builder.build() for _ in range(0, ev_params.population_size)]

    stats['best'] = population[0] # doesn't matter which one

    for individual in population:
        output = individual.execute(X)
        try:
            individual.fitness = ev_params.cost_function(y, output)
        except ValueError as e:
            individual.fitness = ev_params.fitness_of_invalid # arbitrary large penalty 
        evaluations_counter += 1
   
    gens = 0

    while evaluations_counter < ev_params.max_evaluations:#gens < 5000:
        gens += 1



        # store mean of population and best individual
        fitness_values = [x.fitness for x in population]
        stats['mean_of_generation'].append(statistics.mean(
            fitness_values
        ))

        stats['median_of_generation'].append(statistics.median(
            fitness_values
        ))

        try:
            stats['std_of_generation'].append(statistics.stdev(
                fitness_values
            ))
        except OverflowError as e:
            # just append last one as a fallback
            stats['std_of_generation'].append(stats['std_of_generation'][-1])
        
        

        # store the best individual of population
        stats['best_of_generation'].append(min(
            enumerate(population), key=lambda x: x[1].fitness
            )[1]
        )

        if stats['best_of_generation'][-1].fitness < stats['best'].fitness:
            stats['best'] = stats['best_of_generation'][-1]

        if verbose and evaluations_counter % 1000 == 0:
            print('Number of evals: {}, mean: {}, best: {}'.format(
                evaluations_counter, stats['mean_of_generation'][-1],
                stats['best'].fitness
            ))

        parent = ev_params.selection(population, 1)[0]

        # while this works in case of truncation selection with one parent
        # it wouldn't work with any other type of selection operators
        # stats['best_of_generation'].append(parent)

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
                try:
                    individual.fitness = ev_params.cost_function(y, output)
                except ValueError as e:
                    individual.fitness = ev_params.fitness_of_invalid # arbitrary large penalty 
                evaluations_counter += 1
       
        if not apply_gem:
            # skip this whole gem-jewellery mumbo-jumbo
            population = population + [parent]
            continue

        for index, (individual, m_index) in enumerate(zip(population, m_indices)):
            if individual.fitness < parent.fitness:
                j_box.add(
                    ev_params.gem_match_strategy.associated_gem_type(
                        individual, parent, m_index))
            else:
                # apply gem
                matching_gem = j_box.match(individual)
                if matching_gem is not None:
                    new_individual = matching_gem.apply(individual)

                    if new_individual is not None: 
                        if ev_params.gem_expire and matching_gem.n_uses >= ev_params.gem_expire:
                            j_box.remove(matching_gem)

                        try:
                            new_individual.fitness = ev_params.cost_function(y, new_individual.execute(X))
                        except ValueError as e:
                            new_individual.fitness = ev_params.fitness_of_invalid # arbitrary large penalty 
                        evaluations_counter += 1
                        
                        stats['ga_values'].append((matching_gem.value, new_individual.fitness, individual.fitness))
                        if new_individual.fitness < individual.fitness:
                            stats['gem_better_after'] += 1
                            population[index] = new_individual
                        elif new_individual.fitness == individual.fitness:
                            stats['gem_same_after'] += 1
                        else:
                            stats['gem_worse_after'] += 1
                    
                        population[index] = new_individual


        population = population + [parent]

    s_pop = sorted(population, key=lambda x: x.fitness)

    for gem in j_box.gems.keys():
        Counter.get().dict['gems'].append(gem)

    if verbose:
        print('Evolution ended with {} of cost function evaluations'.format(evaluations_counter))
        print('Final population:')
        for ind in s_pop:
            print('Fitness: {}, function: {}'.format(ind.fitness, ind))
            
    # store mean of population and best individual
    fitness_values = [x.fitness for x in population]
    stats['mean_of_generation'].append(statistics.mean(
        fitness_values
    ))

    stats['median_of_generation'].append(statistics.median(
        fitness_values
    ))

    try:
        stats['std_of_generation'].append(statistics.stdev(
            fitness_values
        ))
    except OverflowError as e:
        # just append last one as a fallback
        stats['std_of_generation'].append(stats['std_of_generation'][-1])

    # store the best individual of population
    stats['best_of_generation'].append(min(
        enumerate(population), key=lambda x: x[1].fitness
        )[1]
    )

    if stats['best_of_generation'][-1].fitness < stats['best'].fitness:
        stats['best'] = stats['best_of_generation'][-1]

    if verbose and evaluations_counter % 1000 == 0:
        print('Number of evals: {}, mean: {}, best: {}'.format(
            evaluations_counter, stats['mean_of_generation'][-1],
            stats['best'].fitness
        ))
    
    results = {
            'n_evals': evaluations_counter,
            'final': s_pop,
            'stats': stats,
            'gem_stats': Counter.get().dict['gems']
    }

    return results

