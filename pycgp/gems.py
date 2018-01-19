""" Module containing classes for Gems extension """

from pycgp.individual import Individual

from abc import ABC, abstractmethod


class GemPheno():
    def __init__(self, child: Individual, parent: Individual, m_index: int) -> None:
        self.mutated = child.genes[m_index]
        self.node_index = m_index//(child.params['arity'] + 1) + child.params['n_inputs']
        self.gene_index = m_index
        self.value = parent.fitness - child.fitness
        self.genes = parent.nodes[self.node_index].genes
        self.digits = [*self.genes, m_index, self.mutated]
        

    def __hash__(self):
        n = 0
        for d in self.digits:
            n = 10 * n + d
        return n

    def apply(self, individual: Individual) -> Individual:
        new_genes = individual.genes[:]
        new_genes[self.gene_index] = self.mutated
        return Individual(new_genes, individual.bounds, individual.params)
        

class GemSM():
    """ Class representing gem for single mutation """

    def __init__(self, child: Individual, parent: Individual, m_indices: list) -> None:
        self.m_indices = m_indices
        self.originals = [parent.genes[i] for i in m_indices]
        self.mutated = [child.genes[i] for i in m_indices]
        self.digits = [*m_indices, *self.originals]
        self.value = parent.fitness - child.fitness
    
    def __hash__(self):
        n = 0
        for d in self.digits:
            n = 10 * n + d
        return n

    def apply(self, individual: Individual) -> Individual:
        genes = individual.genes[:]
        for m_index, mutated in zip(self.m_indices, self.mutated):
            genes[m_index] = mutated
        return Individual(genes, individual.bounds, individual.params)
        


class Gem():
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


    def __hash__(self):
        n = 0
        for d in self.digits:
            n = 10 * n + d
        return n


    def apply(self, individual: Individual) -> Individual:
        if individual.active_genes[self.index] == 0:
            return None
        genes = individual.genes[:]
        genes[self.index] = self.mutated
        return Individual(genes, individual.bounds, individual.params)

class MatchStrategy(ABC):
    @abstractmethod
    def match(self, gem, individual):
        pass

class MatchPhenotypeStrategy(MatchStrategy):
    def match(self, gem: GemPheno, individual: Individual):
        return individual.nodes[gem.node_index].genes == gem.genes

class MatchGenotypeStrategy(MatchStrategy):
    def match(self, gem: Gem, individual: Individual):
        return individual.genes[gem.index] == gem.original

class MatchSMStrategy(MatchStrategy):
    def match(self, gem: GemSM, individual: Individual) -> bool:
        for m_index, original in zip(gem.m_indices, gem.originals):
            if individual.genes[m_index] != original:
                return False
        return True

class JewelleryBox():
    """ Container for existing gems """

    def __init__(self, match_strategy: MatchStrategy, max_size=5):
        self.gems = {}
        self.max_size = max_size
        self.match_strategy = match_strategy

    def add(self, gem: Gem) -> None:
        """ Add gem into box """

        if len(self.gems) >= self.max_size:
            min_gem = min(self.gems.keys(), key=lambda x: x.value)
            if min_gem.value < gem.value:
                del self.gems[min_gem]
            else:
                return

        self.gems[gem] = gem.value

    def match(self, individual: Individual) -> Gem:
        """ return matching gem """
        matching = None
        for gem, value in self.gems.items():
            same_original = self.match_strategy.match(gem, individual)
            larger_gain = gem.value > matching.value if matching is not None else True

            if same_original and larger_gain:
                matching = gem

        return matching
