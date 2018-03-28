from pycgp.gems import MatchStrategy
from pycgp.individual import Individual
from pycgp.gems import Gem
from pycgp.counter import Counter
from copy import deepcopy

class JewelleryBox():
    """ Container for existing gems """

    def __init__(self, match_strategy: MatchStrategy, max_size=5):
        self.gems = {}
        self.max_size = max_size
        self.match_strategy = match_strategy

    def add(self, gem: Gem) -> None:
        """ Add gem into box """

        if len(self.gems) >= self.max_size:
            #min_gem = max(self.gems.keys(), key=lambda x: x.match_checks)
            #del self.gems[min_gem]
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
            gem.match_checks += 1

            same_original = self.match_strategy.match(gem, individual)

            if same_original:
                gem.match_count += 1

            larger_gain = gem.value > matching.value if matching is not None else True

            if same_original and larger_gain:
                matching = gem

        return matching

    def remove(self, gem: Gem):
        Counter.get().dict['gems'].append(deepcopy(gem))
        del self.gems[gem]


