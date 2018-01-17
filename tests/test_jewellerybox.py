""" Test suite for jewellery box """

from pycgp.gems import Gem, JewelleryBox
from pycgp.individual import Individual

def test_match(jewellerybox: JewelleryBox, individual: Individual):
    """ Should return matching gem """

    matching_gem = jewellerybox.match(individual)

    assert hash(matching_gem) == 102


def test_add_to_full(jewellerybox: JewelleryBox):
    """ Should replace the gem with least value """

    # first we need to fill it up, default max size is 5

    jewellerybox.add(Gem(1, 0, 1, 10))
    jewellerybox.add(Gem(1, 1, 0, 9))
    jewellerybox.add(Gem(0, 1, 1, 2))

    # get the smallest
    min_value = min(jewellerybox.gems.values())
    assert min_value == 2

    # add another
    new_gem = Gem(0, 0, 1, 8)
    jewellerybox.add(new_gem)

    min_value = min(jewellerybox.gems.values())
    assert min_value == 4

    jewellerybox.add(Gem(0, 0, 0, 1))
    
    min_value = min(jewellerybox.gems.values())
    assert min_value == 4
    
