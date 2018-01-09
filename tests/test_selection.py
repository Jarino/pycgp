""" Test suite for selection operators """

from pycgp.selection import truncation_selection

def truncation_selection(population):
    
    best = truncation_selection(population, 1)

    assert True 
