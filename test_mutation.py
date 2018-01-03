""" Test suite for mutation operators """

from individual import Individual
from mutation import point_mutation
import pdb

def test_point_mutation(monkeypatch):
    """ Test for simple point mutation """

    def mock_values_generator():
        for v in [0, 1, 1, 1]:
            yield v

    values_generator = mock_values_generator()

    def mock_values():
        return next(values_generator)

    monkeypatch.setattr('mutation.randint', lambda x, y:  mock_values())

    genes = [2, 0, 1, 2, 1, 1, 2, 2, 2, 3]
    bounds = [2, 1, 1, 2, 2, 2, 2, 3, 3, 4]

    individual = Individual(genes, bounds, {
        'n_inputs': 2,
        'n_outputs': 1,
        'arity': 2,
        'funset': {}})

    mutated_individual = point_mutation(individual)

    assert mutated_individual.genes == [1, 0, 1, 2, 1, 1, 2, 2, 2, 3]
    assert mutated_individual.function_nodes[0].function_index == 1

    
    mutated_individual = point_mutation(individual)

    assert mutated_individual.genes == [2, 1, 1, 2, 1, 1, 2, 2, 2, 3]

