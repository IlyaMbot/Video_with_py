import cv2 as cv
import numpy as np
import glob, os
from PIL import Image


filenames = glob.glob('./results/*')
filenames = sorted(filenames, key=os.path.getctime)

fourcc = cv.VideoWriter_fourcc(*'MJPG')
out = cv.VideoWriter('./output.mp4', fourcc, 22.0, (1440,  1440))

for filename in filenames:
    img = cv.imread(filename)
    out.write(img)

out.release()
