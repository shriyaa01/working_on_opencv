#importing opencv module
import cv2 as cv
#reading videos
video=cv.VideoCapture('videos/video1.mp4')
while True:
    istrue,frame=video.read()
    cv.imshow('Video running right now',frame)
    if cv.waitKey(30) & 0xFF==ord('s'):
        break
video.release()
cv.destroyAllWindows()