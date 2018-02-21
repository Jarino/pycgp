""" Test suite for santa fe benchmark """
from io import StringIO
from pycgp.benchmarks.santafe import parse_matrix
from pycgp.benchmarks.santafe import AntSimulator

def test_parsing_matrix():
    with open('tests/benchmarks/matrix.txt') as f:
        matrix, (x, y) = parse_matrix(f)

        assert matrix == [
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [0, 0, 0, 0]
        ]
        assert x == 2
        assert y == 1

def test_simulation_move(ant_simulator: AntSimulator):
    """ test the move forward """

    ant_simulator.move() # default direction = 0 (north)

    assert (ant_simulator.pos_columns, ant_simulator.pos_rows) == (2, 0)

    ant_simulator.direction = 1
    ant_simulator.move()

    assert (ant_simulator.pos_columns, ant_simulator.pos_rows) == (3, 0)

    ant_simulator.direction = 2
    ant_simulator.move()
    
    assert (ant_simulator.pos_columns, ant_simulator.pos_rows) == (3, 1)

    ant_simulator.direction = 3
    ant_simulator.move()
    
    assert (ant_simulator.pos_columns, ant_simulator.pos_rows) == (2, 1)

    assert ant_simulator.eaten == 1
