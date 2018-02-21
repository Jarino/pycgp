""" Dev script for santa fe trail problem """
from abc import ABC
from random import choice
from functools import partial
from copy import deepcopy

def parse_matrix(f):
    matrix = []
    start_x = 0
    start_y = 0
    for i, line in enumerate(f):
        matrix.append([])
        for j, column in enumerate(line):
            if column == '.':
                matrix[-1].append(0)
            if column == '#':
                matrix[-1].append(1)
            if column == 'S':
                matrix[-1].append(0)
                start_x = j
                start_y = i
    return matrix, (start_x, start_y)

def check_number_of_moves(method):
    def inner(simulator, *args):
        if simulator.moves >= simulator.max_moves:
            raise ValueError
        else:
            method(simulator, *args)
    return inner

class AntSimulator():
    def __init__(self,matrix, start_position, direction=0, max_moves=600):
        self.matrix = matrix[:][:]
        self.matrix_original = deepcopy(matrix)
        self.start_position = start_position
        self.pos_columns = start_position[0]
        self.pos_rows = start_position[1]
        self.direction = direction
        self.direction_columns = [0, 1, 0, -1]
        self.direction_rows = [-1, 0, 1, 0]
        self.width = len(matrix[0])
        self.height = len(matrix)
        # 0 - north
        # 1 - east
        # 2 - south
        # 3 - west
        self.moves = 0
        self.max_moves = max_moves
        self.eaten = 0
        self.start_direction = direction
    
#    @check_number_of_moves
    def move(self):
        self.moves += 1
        self.pos_columns = (
                self.pos_columns + self.direction_columns[self.direction]
                ) % self.width
        self.pos_rows = (
                self.pos_rows + self.direction_rows[self.direction]
                ) % self.height
        if self.matrix[self.pos_rows][self.pos_columns] == 1:
            self.eaten += 1
            self.matrix[self.pos_rows][self.pos_columns] = 0

#    @check_number_of_moves
    def turn_left(self):
        self.moves += 1
        self.direction = (self.direction - 1) % 4

#    @check_number_of_moves
    def turn_right(self):
        self.moves += 1
        self.direction = (self.direction + 1) % 4

    def sense_food(self):
        ahead_row = (
                self.pos_rows + self.direction_rows[self.direction]
                ) % self.height
        ahead_col = (
                self.pos_rows + self.direction_rows[self.direction]
                ) % self.height

        return self.matrix[ahead_row][ahead_col] == 1

#    @check_number_of_moves
    def if_food_ahead(self, opt1, opt2, _):
        if self.sense_food():
            return opt1
        else:
            return opt2

    def reset(self):
        self.eaten = 0
        self.pos_columns = self.start_position[0]
        self.pos_rows = self.start_position[1]
        self.moves = 0
        self.direction = self.start_direction
        self.matrix = deepcopy(self.matrix_original)

def progn(*args):
    for arg in args:
        arg()

def prog2(opt1, opt2, _):
    return partial(progn, opt1, opt2)

def prog3(opt1, opt2, opt3):
    return partial(progn, opt1, opt2, opt3)

with open('pycgp/benchmarks/santafe_trail.txt') as f:
    matrix, position = parse_matrix(f)
simulator = AntSimulator(matrix, position, 1)

FUNSET = {}
FUNSET[0] = simulator.if_food_ahead
FUNSET[1] = prog2
FUNSET[2] = prog3

PARAMS = {
    'n_inputs': 3,
    'n_outputs': 1,
    'n_rows': 1,
    'n_cols': 10,
    'funset': FUNSET
}


X = [[simulator.move, simulator.turn_left, simulator.turn_right]]

def santafe_cost_function(_, machine):
    simulator.reset()
    if machine[0][0] is None:
        return 0

    machine[0][0]()
    return -simulator.eaten

EV_PARAMS = {
    'cost_func': santafe_cost_function,
    'target_fitness': -89
}
        

# example usage

from pycgp.individual_builder import IndividualBuilder

ib = IndividualBuilder(PARAMS)

# individual = ib.build()

# machine = individual.execute([X])[0][0]

#machine()



