""" Test suite for CGP individual """

import numpy as np

from pycgp.individual import Individual


class TestIndividual(object):

    def test_creating_nodes(self, individual):
        """ Test the creation of input nodes """

        assert [x.id for x in individual.input_nodes] == [0, 1, 2]

    def test_n_nodes(self, individual):
        """ Test whether individual correctly computes the number of fun nodes """

        assert len(individual.function_nodes) == 4

    def test_evaluation(self, individual):
        """ Test the evaluation of the individual """

        input_data = [10, 8, 4]

        output = individual.execute(input_data)

        assert output[0] == -92

    def test_evaluation_of_multiple_instances(self, individual):
        """ Test the evaluation of multidim input data """

        input_data = [[10, 8, 4], [8, 4, 0]]

        output = individual.execute(input_data)

        assert output == [[-92], [-60]]

        np_input_data = np.array(input_data)

        output = individual.execute(np_input_data)

        assert output == [[-92], [-60]]

    def test_marking_active(self, individual):
        """ Test whether individual correctly marks its nodes as (in)active """

        assert individual.nodes[3].active
        assert not individual.nodes[4].active
        assert not individual.nodes[5].active
        assert individual.nodes[6].active

        assert not individual.is_gene_active(4)
        assert individual.is_gene_active(2)
        assert individual.is_gene_active(12)

        assert individual.active_genes == [
            1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

    def test_print(self, individual):
        """ test printing the individual """

        assert str(individual) == 'fsub(x1,fmul(x0,x0))'

    def test_equality(self, individual):
        """ Test the equality of two individuals """
        # create a new, same individual
        new_same_ind = Individual(
            individual.genes, individual.bounds, individual.params)

        # create individual with modified active gene
        mod_active_genes = individual.genes[:]
        mod_active_genes[2] = 2

        mod_act_ind = Individual(
            mod_active_genes, individual.bounds, individual.params)

        # create individual with modified inactive gene
        mod_inact_genes = individual.genes[:]
        mod_inact_genes[4] = 2

        mod_inact_ind = Individual(
            mod_inact_genes, individual.bounds, individual.params)

        assert individual == new_same_ind
        assert not (individual == mod_act_ind)
        assert individual != mod_act_ind
        assert individual == mod_inact_ind
