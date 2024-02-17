import numpy as np

import cv2

from watcher import Watcher

class Eyes(Watcher):
    def __init__(self, bounding_box = None):
        super().__init__()
        if bounding_box is not None:
            self.set_bounding_box(bounding_box)

        self.current_image = super().grab_screen(self.bounding_box)
        self.gray_image = None
        self.edges_image = None

    def grab_screen(self):
        self.current_image = super().grab_screen()
        return self.current_image
    
    def gray_image(self):
        self.gray_image = cv2.cvtColor(self.current_image)
        return self.gray_image
    
    def edges_image(self):
        if self.gray_image is None:
            _ = self.gray_image()
        
        self.edges_image = cv2.Sobel(self.gray_image, 3, 1, 1)
    
    def find_squares(self):
        squares = 2