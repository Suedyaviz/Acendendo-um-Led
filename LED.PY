import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

def controleled(pin,delay):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(delay)

while True:
        controleled(12,1)
       
