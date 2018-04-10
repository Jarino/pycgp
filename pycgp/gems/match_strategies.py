from abc import ABC, abstractmethod
from pycgp.gems import GemPheno, GemSingleGene, GemMultipleGenes
from pycgp.individual import Individual


class MatchStrategy(ABC):
    @abstractmethod
    def match(self, gem, individual):
        pass

class MatchPhenotypeStrategy(MatchStrategy):
    associated_gem_type = GemPheno
    def match(self, gem: GemPheno, individual: Individual):
#        if individual.node_of_gene(gem.gene_index).genes != gem.original_node.genes:
#            return False
        for node in gem.parents_nodes:
            index = node.id
            if individual.nodes[index].genes != node.genes:
                return False
        return True 

class MatchPMStrategy(MatchStrategy):
    associated_gem_type = GemSingleGene
    def match(self, gem: GemSingleGene, individual: Individual):
        return individual.genes[gem.index] == gem.original

class MatchSMStrategy(MatchStrategy):

    associated_gem_type = GemMultipleGenes
    def match(self, gem: GemMultipleGenes, individual: Individual) -> bool:
        for m_index, original in zip(gem.m_indices, gem.originals):
            if individual.genes[m_index] != original:
                return False
        return True

class MatchByActiveStrategy(MatchStrategy):
    """Match gem by changes in active genes"""
    associated_gem_type = GemMultipleGenes
    def match(self, gem: GemMultipleGenes, individual: Individual) -> bool:
        for m_index, original in zip(gem.m_indices, gem.originals):
            is_active = individual.active_genes[m_index]
            if is_active and (individual.genes[m_index] != original):
                return False
        return True
