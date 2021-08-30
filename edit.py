import cv2 as cv
import numpy as np

cap = cv.VideoCapture('sal.mp4')
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('./output.avi', fourcc, 22.0, (1440,  1440))
'''
for i in range(10):
    _, frame = cap.read()
    cv.imshow('frame',frame)
    cv.waitKey(1000)

cv.destroyAllWindows()

'''
i = 0
while(i < 700):

    _, frame = cap.read()
    if(_ == False):
        break
    
    r, g, b = cv.split(frame)

    r = r * 2
    g = g * 5 
    b = b * 10 

    frame = cv.merge((r,g,b))
    
    out.write(frame)
    i += 1

cap.release()
out.release()
cv.destroyAllWindows()
print(i)