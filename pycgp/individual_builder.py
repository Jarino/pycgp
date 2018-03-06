from pycgp.genotype_factory import GenotypeFactory
from pycgp.individual import Individual


class IndividualBuilder:
    def __init__(self, params):
        self.gfactory = GenotypeFactory(
            params.n_inputs, params.n_outputs, params.n_columns, params.n_rows,
            params.arity, params.funset)
        self.params = params

    def build(self):
        genes, bounds = self.gfactory.create()
        return Individual(genes, bounds, self.params)
