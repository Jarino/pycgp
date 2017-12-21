""" Test suite for CGP individual """

from individual import Individual

import numpy as np

class TestIndividual(object):

    def test_creating_nodes(self, individual):
        """ Test the creation of input nodes """

        assert [x.id for x in individual.input_nodes] == [0, 1, 2]


    def test_n_nodes(self, individual):
        """ Test whether individual correctly computes the number of fun nodes """

        assert individual.n_nodes == 4


    def test_evaluation(self, individual):
        """ Test the evaluation of the individual """

        input_data = [10, 8, 4]

        output = individual.execute(input_data)

        assert output[0] == -92

    def test_evaluation_of_multiple_instances(self, individual):
        """ Test the evaluation of multidim input data """

        input_data = [[10,8,4], [8,4,0]]

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
