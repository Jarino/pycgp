""" Test suite for jewellery box """

from pycgp.gems import GemSingleGene, JewelleryBox
from pycgp.individual import Individual
import pdb
def test_match(jewellerybox: JewelleryBox, individual: Individual):
    """ Should return matching gem """

    matching_gem = jewellerybox.match(individual)

    assert hash(matching_gem) == 1015


def test_add_to_full(individual: Individual, jewellerybox: JewelleryBox):
    """ Should replace the gem with least value """

    # there are already two individuals in jewellerybox (from conftest.py)
    jewellerybox.max_size = 2

    # individual fixture has no fitness
    individual.fitness = 100

    # get the smallest
    min_value = min(jewellerybox.gems.values())
    assert min_value == 5
    
    # add another
    better_ind = Individual(individual.genes[:], individual.bounds, individual.params)
    better_ind.fitness = 30 
    new_gem = GemSingleGene(better_ind, individual, 7)
    jewellerybox.add(new_gem)

    min_value = min(jewellerybox.gems.values())
    assert min_value ==  10

    
