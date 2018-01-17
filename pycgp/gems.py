""" Module containing classes for Gems extension """

from pycgp.individual import Individual


class Gem():
    """ Class representing one gem.
    Gem is represented as triple of integers:
    -- index in genotype
    -- original value of gene
    -- mutated value of gene
    """

    def __init__(self, index: int, original: int, mutated: int, value: float) -> None:
        self.index = index
        self.original = original
        self.mutated = mutated
        self.digits = [index, original, mutated]
        self.value = value

    def __eq__(self, other):
        same_index = self.index == other.index
        same_original = self.original == other.original
        same_mutated = self.mutated == other.mutated
        return same_index and same_original and same_mutated

    def __hash__(self):
        n = 0
        for d in self.digits:
            n = 10 * n + d
        return n

    def __lt__(self, other):
        return self.value > other

    def apply(self, individual: Individual) -> Individual:
        genes = individual.genes[:]
        genes[self.index] = self.mutated
        return Individual(genes, individual.bounds, individual.params)


class JewelleryBox():
    """ Container for existing gems """

    def __init__(self, max_size=5):
        self.gems = {}
        self.max_size = max_size

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
            same_original = individual.genes[gem.index] == gem.original
            larger_gain = gem.value > matching.value if matching is not None else True

            if same_original and larger_gain:
                matching = gem

        return matching
