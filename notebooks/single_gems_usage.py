from pycgp.benchmarks.symbolic import X, y, PARAMS, EV_PARAMS
from pycgp.evolution import evolution
from pycgp import Params, EvParams
from pycgp.counter import Counter
import pandas as pd

params = Params(1, 1, funset=PARAMS['funset'])
ev_params = EvParams(EV_PARAMS['cost_func'], gems_box_size=10, population_size=10)

def get_data(gems):
    data = pd.DataFrame([(
        x.n_uses, 
        x.match_checks, 
        x.match_count, 
        x.gene_possible_values,
        x.match_probability
        ) for x in gems])
    columns = ['n_uses', 'match_checks', 'match_count', 'gene_possible_values', 'match_probability']
    data.columns = columns
    data['empiric'] = data.iloc[:,2]/data.iloc[:,1]
    return data

__all__ = [
    'params',
    'ev_params',
    'get_data',
    'evolution',
    'X',
    'y',
    'Counter'
]