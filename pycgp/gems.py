""" Module containing classes for Gems extension """

class Gem():
    """ Class representing one gem.
    Gem is represented as triple of integers:
    -- index in genotype
    -- original value of gene
    -- mutated value of gene
    """
    def __init__(self, index, original, mutated):
        self.index = index
        self.original = original
        self.mutated = mutated
        self.digits = [index, original, mutated]

    def __eq__(self, other):
        same_index = self.index == other.index
        same_original = self.original == other.original
        same_mutated = self.mutated == other.mutated
        return same_index and same_original and same_mutated

    def __hash__(self):
        n = 0
        for d in self.digits:
            n = 10*n + d
        return n


class JewelleryBox():
    """ Container for existing gems """
    
