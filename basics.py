#import opencv
import cv2 as cv
#reading image
img=cv.imread('photos/shinchan.jpg')
#displaying image
cv.imshow('Shinchan_cartoon',img)
#waitkey :0 refers here infinite amount of time
cv.waitKey(0)