import cv2 as cv
import numpy as np
from PIL import Image

cap = cv.VideoCapture('car.mp4')

step = 10

k = 0
while(1):
    _, frame = cap.read()  
    if(_ == False):
        break
    
    cv.imwrite("./frames/frame" + "{}".format(k).zfill(4) + ".jpg" , frame)
    k += 1

cap.release()