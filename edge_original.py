# OpenCV program to perform Edge detection in real time
import cv2 
import numpy as np
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)


 
# capture frames from a camera
cap = cv2.VideoCapture(0)
fgbg = cv2.BackgroundSubtractorMOG(history=3, nmixtures=5, backgroundRatio=0.0001)
 
# loop runs if capturing has been initialized
while(1):
    #reads image from camera
    ret, frame = cap.read()
    
    #conversion credetentials for edge detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #Display original image
    cv2.imshow('Original',frame)

    #Canny edge detection
    edges = cv2.Canny(frame,100,200)
    cv2.imshow('Edges',edges)

    #Background subratction
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    print fgmask.mean()

    #Led glow
    if (fgmask.mean>=50):
        
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(1)
        print "Red signal is on"
    elif (fgmask.mean<50):
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        time.sleep(1)
        print "Green signal is on"
        
    
    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
 
 
# Close the window
cap.release()
 
# De-allocate any associated memory usage
cv2.destroyAllWindows() 
