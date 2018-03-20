# coding: utf-8
import single_gems_usage
from pycgp.counter import Counter
Counter.get().dict
gems = Counter.get().dict['gems']
import pandas as pd
data = pd.DataFrame([(x.n_uses, x.match_checks, x.match_count, x.match_probability) for x in gems])
columns = ['n_uses', 'match_checks', 'match_count', 'match_probability']
data.columns = columns
data['empiric'] = data.iloc[:,2]/data.iloc[:,1]
data
