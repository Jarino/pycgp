from abc import ABC, abstractmethod
from pycgp.gems import GemPheno, GemPM, GemSM
from pycgp.individual import Individual

class MatchStrategy(ABC):
    @abstractmethod
    def match(self, gem, individual):
        pass

class MatchPhenotypeStrategy(MatchStrategy):
    def match(self, gem: GemPheno, individual: Individual):
        return individual.nodes[gem.node_index].genes == gem.genes

class MatchPMStrategy(MatchStrategy):
    def match(self, gem: GemPM, individual: Individual):
        return individual.genes[gem.index] == gem.original

class MatchSMStrategy(MatchStrategy):
    def match(self, gem: GemSM, individual: Individual) -> bool:
        for m_index, original in zip(gem.m_indices, gem.originals):
            if individual.genes[m_index] != original:
                return False
        return True

class MatchByActiveStrategy(MatchStrategy):
    def match(self, gem: GemSM, individual: Individual) -> bool:
        for m_index, original in zip(gem.m_indices, gem.originals):
            is_active = individual.active_genes[m_index]
            if is_active and (individual.genes[m_index] != original):
                return False
        return True
