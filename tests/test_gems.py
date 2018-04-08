""" Test suite for gems module """
from copy import deepcopy

import pytest

from pycgp import Params
from pycgp.gems import GemSingleGene
from pycgp.gems import GemPheno, MatchPhenotypeStrategy
from pycgp.individual import Individual


def test_phenotype_match(individual):
    """ Test the behaviour of phenotype match """
    mutated_genes = individual.genes[:]
    mutated_genes[10] = 4
    mutated_individual = Individual(mutated_genes, individual.bounds, individual.params)
    individual.fitness = 100
    mutated_individual.fitness = 10
    gem = GemPheno(mutated_individual, individual, 10)

    matching_individual = Individual(
            [1, 0, 1, 1, 1, 1, 0, 4, 2, 1, 1, 1, 6], 
            individual.bounds, individual.params)

    strategy = MatchPhenotypeStrategy()

    assert strategy.match(gem, matching_individual)

    non_matching_individual = Individual(
            [1, 0, 1, 1, 0, 1, 0, 4, 2, 1, 1, 1, 6], 
            individual.bounds, individual.params)

    assert not strategy.match(gem, non_matching_individual)

def test_phenotype_match_output_node(individual):
    """ Test the behaviour of phenotype match, when output node is mutated """
    mutated_genes = individual.genes[:]
    m_index=len(mutated_genes) - 1
    mutated_genes[m_index] = 3
    mutated_individual = Individual(mutated_genes, individual.bounds, individual.params)
    individual.fitness = 100
    mutated_individual.fitness = 10
    gem = GemPheno(mutated_individual, individual, m_index)

    strategy = MatchPhenotypeStrategy()
    matching_individual = Individual(
            [1, 0, 0, 1, 1, 1, 0, 4, 2, 1, 1, 1, 1], 
            individual.bounds, individual.params)

    non_matching_individual = Individual(
            [1, 0, 1, 1, 1, 1, 0, 4, 2, 1, 1, 1, 1], 
            individual.bounds, individual.params)

    assert strategy.match(gem, matching_individual)
    assert not strategy.match(gem, non_matching_individual)

def test_hash(individual):
    """ Hash should be the same for Gems with
    same parameters """

    mutated_genes = individual.genes[:]
    mutated_genes_2 = individual.genes[:]
    mutated_genes[1] = 2
    mutated_genes_2[1] = 1
    mutated = Individual(mutated_genes, individual.bounds, individual.params)
    mutated2 = Individual(mutated_genes_2, individual.bounds, individual.params)

    mutated.fitness = 100
    mutated2.fitness = 100
    individual.fitness = 100

    g = GemSingleGene(mutated, individual, 1)
    gg = GemSingleGene(mutated, individual, 1)
    ggg = GemSingleGene(mutated2, individual, 1)

    assert hash(g) == hash(gg)
    assert hash(g) != hash(ggg)
    assert hash(g) == hash(g)


@pytest.mark.skip(reason='unused feature')
def test_probability_calculation():
    params = Params(0, 0)

    child = Individual([2,2,2,1], [2,2,2,3], params)
    child.fitness = 10
    parent = Individual([2,1,2,1], [2,2,2,3], params)
    parent.fitness = 100

    gem = GemSingleGene(child, parent, 1)

    assert gem.match_probability == 1/3

    gem = GemSingleGene(child, parent, 3)

    assert gem.match_probability == 1/4
