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


    def test_mutating_the_output_gene(self, individual):
        # lets pretend this is a random mutation
        new_individual = individual.copy()
        new_individual.genes[len(new_individual.genes) - 1] = 5

        assert new_individual.output_genes != individual.output_genes


    def test_print(self, individual):
        """ test printing the individual """

        assert str(individual) == 'fsub(x1,fmul(x0,x0))'


