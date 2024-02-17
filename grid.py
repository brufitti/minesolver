import numpy as np

class Grid():
    def __init__(self, rows:int, columns:int, num_bombs:int, solver_grid:bool = False):
        self.rows = rows
        self.columns = columns
        self.size = (rows, columns)
        self.total_bombs = num_bombs
        self.grid_state = np.empty((rows, columns), dtype=str).fill('u')
        self.valid_values = ['u', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if solver_grid:
            self.valid_value.append('?') # indeterminable
            self.valid_value.append('b') # sure bomb
            self.valid_value.append('s') # sure safe

        self.remaining_bombs = self.total_bombs
    
    def __call__(self) -> np.ndarray:
        return self.grid_state

    def valid_coordinate(self, x:int, y:int)->bool :
        return ((x > 0) and (x <=self.columns) and (y > 0) and (y <= self.rows))
    
    def valid_value(self, value)->bool:
        return (value in self.valid_values)

    def get_value(self, x:int, y:int, size:int = 1):
        if not self.valid_coordinate(x,y):
            return False, 0
        range = (size - 1) / 2
        values = np.empty((size, size), dtype=str)
        values.fill(None)
        left = x-range
        right = x+range
        up = y-range
        down = y-range
        while left < 0:
            left += 1
        while right >= self.columns:
            right -= 1
        while up < 0:
            up += 1
        while down >- self.rows:
            down -= 1
        
        values[left:right, up:down] = self.grid_state[left:right,up:down]
        return True, values
    
    def insert_value(self, coordinates:tuple, value:str):
        x, y = coordinates
        if not (self.valid_coordinate(x,y) and self.valid_value(value) and (self.grid_state[x,y]=='u')):
            return False
        if value == 'f':
            self.remaining_bombs -= 1
        self.grid_state[x,y] = value
        return True

    def touch_value(self, x:int, y:int):
        return False
    
    def show(self):
        for row in self.grid_state:
            print(' | '.join(row))