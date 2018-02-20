""" Test suite for mutation operators """

from pycgp.individual import Individual
from pycgp.mutation import point_mutation
from pycgp.mutation import single_mutation
from pycgp.mutation import active_mutation
from pycgp.mutation import probabilistic_mutation

def test_point_mutation(monkeypatch):
    """ Test for simple point mutation """

    def mock_values_generator():
        for v in [0, 1, 1, 1]:
            yield v

    values_generator = mock_values_generator()

    def mock_values():
        return next(values_generator)

    monkeypatch.setattr('pycgp.mutation.choice', lambda x:  mock_values())

    genes = [2, 0, 1, 2, 1, 1, 2, 2, 2, 3]
    bounds = [2, 1, 1, 2, 2, 2, 2, 3, 3, 4]

    individual = Individual(genes, bounds, {
        'n_inputs': 2,
        'n_outputs': 1,
        'arity': 2,
        'funset': {}})

    mutated_individual, _ = point_mutation(individual)

    assert mutated_individual.genes == [1, 0, 1, 2, 1, 1, 2, 2, 2, 3]
    assert mutated_individual.function_nodes[0].function_index == 1

    mutated_individual, _ = point_mutation(individual)

    assert mutated_individual.genes == [2, 1, 1, 2, 1, 1, 2, 2, 2, 3]
    assert not mutated_individual.function_nodes[0].active
    assert mutated_individual.function_nodes[1].active
    assert not mutated_individual.function_nodes[2].active


def test_single_mutation(individual, monkeypatch):
    """ Test for single mutation (mutate until active gene is changed) """

    def v_generator():
        for v in [3, 0, 1, 1]:
            yield v

    values_generator = v_generator()

    def mock_values():
        return next(values_generator)

    monkeypatch.setattr('pycgp.mutation.choice', lambda x: mock_values())

    mutated, _ = single_mutation(individual)

    assert mutated.genes == [1, 1, 0, 0, 1, 1, 0, 4, 2, 2, 1, 3, 6]


def test_active_mutation(individual, monkeypatch):
    """ Test for single mutation (mutate until active gene is changed) """

    
    def v_generator():
        for v in [1, 1]:
            yield v

    values_generator = v_generator()

    def choice_mock():
        return next(values_generator)

    monkeypatch.setattr('pycgp.mutation.choice', lambda x: choice_mock())

    mutated, _ = active_mutation(individual)

    assert mutated.genes == [1, 1, 0, 1, 1, 1, 0, 4, 2, 2, 1, 3, 6]


def test_probabilistic_mutation(individual, monkeypatch):
    """ should mutate multiple genes with certain probability """
    rate = 0.5

    def v_generator():
        random_values = [
                0.1, 0.2, 0.6, 0.7, 0.8, 0.9, 
                0.4, 0.3, 0.6, 0.7, 0.8, 0.9,
                0.5]

        for v in random_values:
            yield v

    values_generator = v_generator()

    def random_mock():
        return next(values_generator)

    monkeypatch.setattr('pycgp.mutation.random', random_mock)
    monkeypatch.setattr('pycgp.mutation.choice', lambda x: x[-1])

    mutated, changed_indices = probabilistic_mutation(individual, rate)

    assert mutated.genes != [1, 0, 0, 1, 1, 1, 0, 4, 2, 2, 1, 3, 6]
    assert changed_indices == [0, 1, 6, 7] 
