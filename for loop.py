import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

repeats = int(input("enter the number of times the led should blink: "))

for i in range (0,repeats):
    print("LED on") 
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.2)    
    print ("LED off")
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.2)
    
print("the led blinked",repeats,"times")

