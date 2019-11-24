import RPi.GPIO as GPIO
import time
from pyminder.beeminder import Beeminder
import os
import yaml
import time

base_dir = os.path.dirname(os.path.realpath(__file__))
config = yaml.load(open(f"{base_dir}/config.yaml", "r"), Loader=yaml.FullLoader)

bm = Beeminder()

bm.set_username(config['beeminder']['user'])
bm.set_token(config['beeminder']['token'])

goals = bm.get_goals()
lose_dates = [g['losedate'] for g in goals]
lose_date = min(lose_dates)
now = time.time()
remaining = lose_date - now

print(f'Now: {now}')
print(f'Lose Date: {lose_date}')
print(f'Remaining: {remaining}')

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