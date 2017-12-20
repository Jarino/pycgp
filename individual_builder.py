from genotype_factory import GenotypeFactory
from utils import max_arity
from individual import Individual

class IndividualBuilder:
    
    def __init__(self, n_inputs, n_outputs, n_cols, n_rows, funset):
        self.arity = max_arity(funset.values()) 
        self.gfactory = GenotypeFactory(n_inputs, n_outputs, n_cols, n_rows, self.arity, funset)
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        

    def build(self):
        return Individual(self.gfactory.create(), self.arity, self.n_inputs, self.n_outputs)



