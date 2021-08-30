import cv2 as cv
import numpy as np
import glob, os
from PIL import Image
import time

step = 10

filenames = glob.glob('./frames/*')
filenames = sorted(filenames, key=os.path.basename)

frames = len(filenames) - 144

for k in range(1):
    
    img = np.zeros(shape = (1440, 1440, 3), dtype = np.uint8)
    t1 = time.time_ns()
    
    for i in range(0, 144, 1):
    
        img[i*10 : i*10 + step] = cv.imread(filenames[i + k])[i*10 : i*10 + 10]
        
    t2 = time.time_ns()
    print("crop =", (t2 - t1) / 10**9)
    
    img = Image.fromarray(img)
    img.save("./results/rframe" + "{}".format(k).zfill(4) + ".jpg")
    

'''
# the last worked version without modifications

for k in range(frames):

    img = np.zeros(shape = (1440, 1440, 3), dtype = np.uint8)
    
    for i in range(0, 144, 1):
        img[i*10 : i*10 + step] = Image.open(filenames[i + k]).crop((0, i*10, 1440, i*10 + 10))
    
    img = Image.fromarray(img)
    img.save("./results/rframe" + "{}".format(k).zfill(4) + ".jpg")
    
'''