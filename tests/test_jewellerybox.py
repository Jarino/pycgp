""" Test suite for jewellery box """


def test_match(jewellerybox, individual):
    """ Should return matching gem """
    
    matching_gem = jewellerybox.match(individual)

    assert hash(matching_gem) == 102
