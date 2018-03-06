"""Test suite for Params object"""

from copy import deepcopy

from pycgp import Params
from pycgp.params import FUNSET

def test_arities_table():
    def dummy_sin(x):
        return x

    funset = deepcopy(FUNSET)
    funset[4] = dummy_sin

    params = Params(3, 1, funset=funset)

    assert params.arities == [2, 2, 2, 2, 1]
