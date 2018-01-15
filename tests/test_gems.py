""" Test suite for gems module """

from pycgp.gems import Gem


def test_equality():
    g = Gem(1, 2, 3)
    gg = Gem(1, 2, 3)

    assert g == gg

    ggg = Gem(1, 3, 2)

    assert g != ggg
    assert ggg != g
    assert gg != ggg


def test_hash():
    """ Hash should be the same for Gems with
    same parameters """

    g = Gem(1, 2, 3)
    gg = Gem(1, 2, 3)
    ggg = Gem(2, 1, 3)

    assert hash(g) == hash(gg)
    assert hash(g) != hash(ggg)
    assert hash(g) == hash(g)
