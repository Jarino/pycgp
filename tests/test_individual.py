""" Test suite for CGP individual """
from copy import deepcopy

import numpy as np

from pycgp.individual import Individual
from pycgp import Params
from pycgp.individual_builder import IndividualBuilder

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

        assert output[0] == 100 




    def test_evaluation_of_multiple_instances(self, individual):
        """ Test the evaluation of multidim input data """

        input_data = [[10, 8, 4], [8, 4, 0]]

        output = individual.execute(input_data)

        assert output == [[100], [64]]

        np_input_data = np.array(input_data)

        output = individual.execute(np_input_data)

        assert output == [[100], [64]]

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

        assert str(individual) == 'fsin(fmul(x0,x0))'

    def test_print_of_multiple_outputs(self, mo_individual):
        """ test printing the individual with multiple outputs """
        
        assert str(mo_individual) == 'fsin(fmul(x0,x0))|fmul(x0,x0)' 


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

    def test_number_of_output_nodes(self):
        """Test whether the number of output nodes is correct"""
        ib4outputs = IndividualBuilder(Params(n_inputs=4, n_outputs=4))

        individual = ib4outputs.build()

        assert len(individual.output_nodes) == 4

    def test_getting_a_node_of_gene(self, individual):

        node = individual.node_of_gene(1) 
        assert node.genes == [1, 0, 0]

        node = individual.node_of_gene(0)
        assert node.genes == [1, 0, 0]

        node = individual.node_of_gene(6)
        assert node.genes == [0, 4, 2]

        node = individual.node_of_gene(11) 
        assert node.genes == [2, 3, 1]

        node = individual.node_of_gene(12)
        assert node.genes == [6] 

