""" Module containing classes for Gems extension """

from pycgp.individual import Individual
from pycgp.node import OutputNode

from abc import ABC, abstractmethod

class Gem(ABC):

    def __hash__(self):
        n = 0
        for d in self.digits:
            n = 10 * n + d
        return n

    @abstractmethod
    def apply(self, individual: Individual) -> Individual:
        pass

class GemPheno(Gem):
    '''Gem for parent phenotype match strategy''' 
    def __init__(self, child: Individual, parent: Individual, m_index: int) -> None:
        # store genes of parents of given child node
        self.mutated_node = child.node_of_gene(m_index)
        self.parents_nodes = []

        if isinstance(self.mutated_node, OutputNode):
            input_genes = self.mutated_node.genes[:]
        else:
            input_genes = self.mutated_node.genes[1:]

        for parent_index in input_genes:
            self.parents_nodes.append(
                child.nodes[parent_index])

    def apply(self, individual: Individual) -> Individual:
        new_genes = individual.genes[:]
        new_genes[self.gene_index] = self.mutated
        return Individual(new_genes, individual.bounds, individual.params)
        

class GemMultipleGenes(Gem):
    """ Class representing gem for single mutation """

    def __init__(self, child: Individual, parent: Individual, m_indices: list) -> None:
        self.m_indices = m_indices
        self.originals = [parent.genes[i] for i in m_indices]
        self.mutated = [child.genes[i] for i in m_indices]
        self.digits = [*m_indices, *self.originals]
        self.value = parent.fitness - child.fitness
        self.n_uses = 0
    

    def apply(self, individual: Individual) -> Individual:
        self.n_uses += 1
        genes = individual.genes[:]
        for m_index, mutated in zip(self.m_indices, self.mutated):
            genes[m_index] = mutated
        return Individual(genes, individual.bounds, individual.params)
        


class GemSingleGene(Gem):
    """ Class representing one gem.
    Gem is represented as triple of integers:
    -- index in genotype
    -- original value of gene
    -- mutated value of gene
    """

    def __init__(self, child: Individual, parent: Individual, m_index: int) -> None:
        self.index = m_index
        self.original = parent.genes[m_index]
        self.mutated = child.genes[m_index]
        self.digits = [m_index, self.original, self.mutated]
        self.value = parent.fitness - child.fitness
        self.n_uses = 0



    def apply(self, individual: Individual) -> Individual:
        if individual.active_genes[self.index] == 0:
            return None
        self.n_uses += 1
        genes = individual.genes[:]
        genes[self.index] = self.mutated
        return Individual(genes, individual.bounds, individual.params)



