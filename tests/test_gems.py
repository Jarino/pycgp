""" Test suite for gems module """

from pycgp.gems import Gem


def test_equality():
    g = Gem(1, 2, 3, 0)
    gg = Gem(1, 2, 3, 0)

    assert g == gg

    ggg = Gem(1, 3, 2, 0)

    assert g != ggg
    assert ggg != g
    assert gg != ggg


def test_hash():
    """ Hash should be the same for Gems with
    same parameters """

    g = Gem(1, 2, 3, 0)
    gg = Gem(1, 2, 3, 0)
    ggg = Gem(2, 1, 3, 0)

    assert hash(g) == hash(gg)
    assert hash(g) != hash(ggg)
    assert hash(g) == hash(g)


def test_sorting():
    """ Should sort list of gems according to their value """

    small = Gem(0, 0, 0, 1)
    middle = Gem(0, 0, 0, 6)
    large = Gem(0, 0, 0, 10)

    gems = [middle, small, large]

    sorted_gems = sorted(gems)

    assert [x.value for x in sorted_gems] == [1, 6, 10]

