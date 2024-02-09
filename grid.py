import numpy as np

class Grid():
    def __init__(self, rows:int, columns:int, num_bombs:int):
        self.rows = rows
        self.columns = columns
        self.total_bombs = num_bombs
        self.grid_state = np.empty((rows, columns), dtype=str).fill('u')
        self.valid_values = ['u', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.remaining_bombs = self.total_bombs
    
    def valid_coordinate(self, x:int, y:int)->bool :
        return ((x > 0) and (x <=self.columns) and (y > 0) and (y <= self.rows))
    
    def valid_value(self, value)->bool:
        return (value in self.valid_values)

    def get_value(self, x:int, y:int, size:int = 1):
        if not self.valid_coordinate(x,y):
            return False, 0
        
        values = np.empty((size, size), dtype=str)
        range = (size - 1) / 2
        values = self.grid_state[x-range:x+range,y-range:y+range]
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