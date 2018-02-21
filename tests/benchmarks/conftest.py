import pytest

from pycgp.benchmarks.santafe import AntSimulator, parse_matrix

@pytest.fixture
def ant_simulator():
    with open('tests/benchmarks/matrix.txt') as f:
        matrix, start_position = parse_matrix(f)
        print(start_position)
        return AntSimulator(matrix, start_position, 0)



