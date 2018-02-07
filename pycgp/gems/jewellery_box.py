from pycgp.gems import MatchStrategy
from pycgp.individual import Individual
from pycgp.gems import Gem


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
