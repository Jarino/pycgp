""" Factory class for generating the genotypes of given parameters """

from random import randint

class GenotypeFactory():

    def __init__(self, n_inputs, n_outputs, n_cols, n_rows, arity, funset):
        self.n_ins = n_inputs
        self.n_outs = n_outputs
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.arity = arity
        self.funset = funset
        self.n_fun_nodes = n_cols * n_rows
        self.n_funs = len(funset)

    def create(self):
        genes = []
        bounds = []
        for i in range(self.n_ins, self.n_ins + self.n_fun_nodes):
            function_gene = randint(0, self.n_funs - 1)

            genes.append(function_gene)
            bounds.append(self.n_funs - 1)

            current_column = (i - self.n_ins) // self.n_rows

            upper_bound = self.n_ins + current_column * self.n_rows - 1

            for _ in range(self.arity):
                genes.append(randint(0, upper_bound))
                bounds.append(upper_bound)

        output_gene_upper_bound = self.n_ins + self.n_fun_nodes - 1
        for i in range(self.n_outs):
            genes.append(randint(0, output_gene_upper_bound))
            bounds.append(output_gene_upper_bound)

        return genes, bounds