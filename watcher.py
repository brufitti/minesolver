import numpy as np
import cv2
from mss import mss
from PIL import Image

class Watcher():
    def __init__(self):
        self.bounding_box = {'top': 164, 'left': 491, 'width': 1139, 'height': 869} # 164, 491, 1136, 869
        self.sct = mss()

    def set_bounding_box(self, bounding_box):
        self.bounding_box = bounding_box

    def grab_screen(self):
        return self.sct.grab(self.bounding_box)

    def show_screen(self):
        while True:
            screen = self.grab_screen()
            cv2.imshow('screen', np.array(screen))
            if (cv2.waitKey(1) & 0xFF) == ord('q'):
                cv2.destroyAllWindows()
                break

def main():
    watcher = Watcher()
    screen = watcher.grab_screen()
    cv2.imwrite("Screen_shot.png", np.array(screen))
    # watcher.show_screen()

if __name__ == '__main__':
    main()