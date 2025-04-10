import cv2 as cv
img = cv.imread('pics/park.jpg')
cv.imshow('cat', img)


#converting to grayscale:
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('cat_gray', gray)

#Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
#cv.imshow('blur', blur)

#Edges Cascade:
canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

#Dilation 
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('dilated', dilated)
#eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('resized', resized)

#CROPPING
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)  