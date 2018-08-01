import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
a=input()
if a>=50:
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print "Red signal is on"
if a<50:
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(18,GPIO.LOW)
    time.sleep(1)
    print "Green signal is on"
        
       
        
            
