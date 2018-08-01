import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
def callback(channel):
    if GPIO.input(channel):
        print "Ambulance sound detected"
    else:
        print "Ambulance Sound not detected"
GPIO.add_event_detect(17,GPIO.BOTH,bouncetime=300)
GPIO.add_event_callback(17,callback)
while(True):
    time.sleep(1)

                                    
        
