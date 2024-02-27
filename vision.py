import numpy as np

import cv2

from watcher import Watcher

class Eyes(Watcher):
    def __init__(self, rows, columns, bounding_box = None):
        super().__init__()
        if bounding_box is not None:
            self.set_bounding_box(bounding_box)

        self.current_image = super().grab_screen(self.bounding_box)
        self.gray_image = None
        self.binary_image = None
        self.rows = rows
        self.columns = columns
        self.centers = np.zeros((rows,columns,2))

    def grab_screen(self):
        self.current_image = super().grab_screen()
        return self.current_image
    
    def gray_image(self):
        self.gray_image = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2GRAY)
        return self.gray_image
    
    def binary_image(self):
        _, self.binary_image = cv2.threshold(self.gray_image, 185, 255,0)
        return self.binary_image
    
    def find_centroid(contour):
        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        return [cX, cY]

    def find_distance(center1, center2):
        return ((center1[0]-center2[0])**2 + (center1[1] - center2[1])**2)**0.5

    def add_value(self, matrix, value, index):
        current_row = index // (self.columns)
        current_column = index % (self.columns)
        matrix[current_row, current_column, :] = value

    def get_centroids(self):
        thresh = cv2.erode(self.binary_image, np.ones((3,3), np.uint8), 1)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        distance = 50
        passed_start = False
        for element in range(self.rows*self.columns+1):
            idx = element + 2
            contour = contours[idx]
            current_center = self.find_centroid(contour)
            if element > 0 :
                distance = self.find_distance(current_center, previous_center)
            
            if distance < 10:
                passed_start = True
                start_point  = (element // (self.columns) ,element % (self.columns))
            if passed_start:
                self.add_value(self.centers, current_center, element-1, self.rows, self.columns)
            else:
                self.add_value(self.centers, current_center, element, self.rows, self.columns)
            previous_center = current_center
            
        return self.centers, start_point
        