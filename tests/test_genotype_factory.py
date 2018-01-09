""" Test suite for genotype factory """

from pycgp.genotype_factory import GenotypeFactory

def test_generate(monkeypatch):
    """ test the random generation of genotypes """

    monkeypatch.setattr('pycgp.genotype_factory.randint', lambda x, y: y)

    n_inputs = 4
    n_outputs = 2
    arity = 2
    n_cols = 3
    n_rows = 2
    funset = {}
    funset[0] = lambda x, y: x

    gfactory = GenotypeFactory(
        n_inputs, n_outputs, n_cols, n_rows, arity, funset)

    genes, bounds = gfactory.create()

    print(genes)

    assert genes == [
        0, 3, 3, 0, 3, 3, 0, 5, 5, 0, 5, 5, 0, 7, 7, 0, 7, 7, 9, 9
    ]

    assert bounds == [
        0, 3, 3, 0, 3, 3, 0, 5, 5, 0, 5, 5, 0, 7, 7, 0, 7, 7, 9, 9
    ]


def test_generate_2(monkeypatch):
    """ test the random generation of genotypes with different conf """

    monkeypatch.setattr('pycgp.genotype_factory.randint', lambda x, y: y)

    n_inputs = 3
    n_outputs = 1
    arity = 3
    n_cols = 3
    n_rows = 1
    funset = {}
    funset[0] = lambda x, y, z: x

    gfactory = GenotypeFactory(
        n_inputs, n_outputs, n_cols, n_rows, arity, funset)

    genes, bounds = gfactory.create()

    assert genes == [
        0, 2, 2, 2, 0, 3, 3, 3, 0, 4, 4, 4, 5
    ]

    assert bounds == [
        0, 2, 2, 2, 0, 3, 3, 3, 0, 4, 4, 4, 5
    ]
