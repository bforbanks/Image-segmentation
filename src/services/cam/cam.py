import cv2
from matplotlib.pyplot import imshow


class cam:
    vc: cv2.VideoCapture

    def __init__(self):
        self.vc = cv2.VideoCapture(0)

    def getCurrentImage(self):
        rval, frame = self.vc.read()
        return frame
