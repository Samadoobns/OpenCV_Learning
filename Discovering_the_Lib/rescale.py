
import cv2 as cv

def rescaleFrame(frame,scale = 0.75):
    width =  int(frame.shape[1] * scale)
    height =  int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
def changRes(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('0')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.2)
    
    cv.imshow('Video',frame)
    cv.imshow('Video resized',frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'): #if the letter d pressed, destroy the window
        break
capture.release()
cv.destroyAllWindows()

