import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)


print("LED on") 
GPIO.output(17,GPIO.HIGH)
time.sleep(3)    
print ("LED off")
GPIO.output(17,GPIO.LOW)
time.sleep(3)    

GPIO.cleanup()
