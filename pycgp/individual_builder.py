from pycgp.genotype_factory import GenotypeFactory
from pycgp.individual import Individual
from pycgp.utils import max_arity


class IndividualBuilder:
    def __init__(self, params):

        self.arity = max_arity(params['funset'].values())
        params['arity'] = self.arity
        self.gfactory = GenotypeFactory(params['n_inputs'], params['n_outputs'], params['n_cols'], params['n_rows'],
                                        self.arity, params['funset'])
        self.n_inputs = params['n_inputs']
        self.n_outputs = params['n_outputs']
        self.params = params

    def build(self):
        genes, bounds = self.gfactory.create()
        return Individual(genes, bounds, self.params)
