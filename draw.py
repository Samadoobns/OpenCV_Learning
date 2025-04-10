import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)
img = cv.imread('pics/cat.jpg')
cv.imshow('Cat',img)
blank[:] = 0,255,0
cv.imshow('green',blank)

#draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=2)# thickness pour remplissage
cv.imshow('rectangle',blank)
#cv.circle()
#cv.line()
#write text
cv.putText(blank,'hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255),2)
cv.imshow('green',blank)
cv.waitKey(0)