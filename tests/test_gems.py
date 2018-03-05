""" Test suite for gems module """

from pycgp.gems import GemSingleGene
from pycgp.individual import Individual



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


