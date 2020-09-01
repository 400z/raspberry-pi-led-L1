import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)


password = input("enter the password: ")

if password == ("raspberry"):
        print("LED on") 
        GPIO.output(17,GPIO.HIGH)
        time.sleep(3)    
        print ("LED off")
        GPIO.output(17,GPIO.LOW)
        time.sleep(3)
        print("the password is correct")
else:
    print("the password is incorrect")




GPIO.cleanup()
