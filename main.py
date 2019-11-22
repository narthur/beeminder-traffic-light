import RPi.GPIO as GPIO
import time

# Pin Setup:
GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme. This uses the pin numbers that match the pin numbers on the Pi Traffic light.

GPIO.setup(9, GPIO.OUT)   # Red LED pin set as output
GPIO.setup(10, GPIO.OUT)   # Yellow LED pin set as output
GPIO.setup(11, GPIO.OUT)   # Green LED pin set as output

def powerLight(pin, seconds):
    if pin not in [9, 10, 11]:
        return

    GPIO.output(pin, True)
    time.sleep(seconds)
    GPIO.output(pin, False)

def powerRed(seconds):
    powerLight(9, seconds)

def powerYellow(seconds):
    powerLight(10, seconds)

def powerGreen(seconds):
    powerLight(11, seconds)

powerRed(2)
powerYellow(2)
powerGreen(2)

print('done')

GPIO.cleanup()