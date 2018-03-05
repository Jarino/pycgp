"""Test suite for EvParams class"""

from pycgp import EvParams
from pycgp.gems import MatchByActiveStrategy, GemMultipleGenes
from pycgp.gems import MatchPMStrategy, GemSingleGene
from pycgp.gems import MatchSMStrategy

def test_basic_creation():
    """Test object creation"""
    ev_params = EvParams(lambda x: x)

    assert True

def test_associated_gem_type():
    """Should assign correct gem type to certain match strategy"""
    ev_params = EvParams(lambda x: x, gem_match_strategy=MatchByActiveStrategy)

    assert ev_params.gem_type == GemMultipleGenes

    ev_params = EvParams(lambda x: x, gem_match_strategy=MatchSMStrategy)

    assert ev_params.gem_type == GemMultipleGenes

    ev_params = EvParams(lambda x: x, gem_match_strategy=MatchPMStrategy)

    assert ev_params.gem_type == GemSingleGene
