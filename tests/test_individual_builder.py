""" Test suite for individual builder class """

from pycgp.individual_builder import IndividualBuilder
from pycgp import Params

from math import sin


def test_create():
    """ Test creation of individual """

    params = Params(3, 2)

    ib = IndividualBuilder(params)

    individual = ib.build()

    assert True
