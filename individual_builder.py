from genotype_factory import GenotypeFactory
from utils import max_arity
from individual import Individual


class IndividualBuilder:
    def __init__(self, params):
        

        self.arity = max_arity(params['funset'].values())
        self.gfactory = GenotypeFactory(params['n_inputs'], params['n_outputs'], params['n_cols'], params['n_rows'],
                                        self.arity, params['funset'])
        self.n_inputs = params['n_inputs']
        self.n_outputs = params['n_outputs']

    def build(self):
        return Individual(self.gfactory.create(), self.arity, self.n_inputs,
                          self.n_outputs)
