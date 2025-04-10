import cv2 as cv


# img = cv.imread('pics/cat_large.jpg')#image ==> matrix of pixels
# cv.imshow('Cat',img) # name_of_window, matrix_of_pixels
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF == ord('d'): #if the letter d pressed, destroy the window
        break
capture.release()
cv.destroyAllWindows()
    

#cv.waitKey(0)

