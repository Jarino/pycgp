from .mutation import point_mutation
from .selection import truncation_selection
from .gems import MatchPMStrategy

class EvParams():
    """docstring for EvParams"""

    def __init__(self, cost_function,
                target_fitness=None,
                fitness_of_invalid=1e100,
                mutation=point_mutation,
                mutation_probability=0.25,
                selection=truncation_selection,
                population_size=5,
                max_evaluations=5000,
                gems_box_size=0,
                gem_match_strategy=MatchPMStrategy,
                gem_expire=30):
        self.cost_function = cost_function
        self.target_fitness = target_fitness
        self.mutation = mutation
        self.mutation_probability = 0.25 # used only with probabilistic mutation
        self.selection = truncation_selection
        self.population_size = population_size
        self.gems_box_size = gems_box_size
        self.gem_expire = 30
        self.gem_match_strategy = gem_match_strategy      
        self.max_evaluations = max_evaluations
        self.fitness_of_invalid = fitness_of_invalid
