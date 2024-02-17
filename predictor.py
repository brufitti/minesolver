import numpy as np

from grid import Grid

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class Predictor():
    def __init__(self, grid: Grid, first_move_safe :bool=False):
        self.is_first_move = True
        self.first_move_safe = first_move_safe
        self.game_grid = grid
        self.solution_grid = Grid(rows=self.game_grid.rows, 
                                  columns=self.game_grid.columns, 
                                  num_bombs=self.game_grid.total_bombs, 
                                  solver_grid=True)
        self.numbers = []
        self.probability_grid = np.zeros(self.game_grid.size)
        # if not first_move_safe:
        #     update_probabilities()

    def find_numbers(self):
        self.numbers = []
        for y, row in enumerate(self.game_grid):
            for x, column in enumerate(row):
                if column in numbers:
                    self.numbers.append((x,y))
        return self.numbers
    
    def find_near_unknowns(self):
        # Gera uma lista de variáveis validas, contém elementos unknown com vizinhos númerados
        # Gera uma lista de
        for (x,y) in self.unknowns:
            kernel = self.game_grid.get_value(x,y,3)
            numbers = []
            variables = []
            flags = []
            for yi, row in enumerate(kernel):
                for xi, column in enumerate(row): 
                    if (column == 'u') and not ((x,y) in numbers):
                        numbers.append((x,y))
                        if not (x+column-1, y+row-1) in variables:
                            variables.append(x+column-1, y+row-1)
                        



    # def update_probabilities(self):
    #     for y in self.rows:
    #         for x in self.columns:
                # self.probability_grid[x,y] = get_probability(x,y)
        
    # def get_probability(self, x, y):
    #     return 20.00

def main():
    grid = Grid(rows=9,columns=9)
    
    # take all unknown values