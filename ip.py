#Edge detection for a network enabled camera image input 
import urllib
import cv2
import numpy as np
url='http://192.168.43.1:8080/shot.jpg'
cap = cv2.VideoCapture(0)
fgbg = cv2.BackgroundSubtractorMOG(history=3, nmixtures=5, backgroundRatio=0.0001)
while True:
    cap = cv2.VideoCapture('http://192.168.43.1:8080/shot.avi')
    ret, frame = cap.read()
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    cv2.imshow('Webcam_image',img)
    edges = cv2.Canny(frame,100,200)
    cv2.imshow('Edges',edges)
    gmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    print fgmask.mean()
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    # Close the window
cap.release()
 
# De-allocate any associated memory usage
cv2.destroyAllWindows() 

