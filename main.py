import RPi.GPIO as GPIO
import time
from pyminder.beeminder import Beeminder
import os
import yaml
import time
import datetime

base_dir = os.path.dirname(os.path.realpath(__file__))
config = yaml.load(open(f"{base_dir}/config.yaml", "r"), Loader=yaml.FullLoader)

bm = Beeminder()

bm.set_username(config['beeminder']['user'])
bm.set_token(config['beeminder']['token'])

def tick():
    lose_date = get_lose_date()
    pin = get_pin(lose_date)
    interval = get_interval(lose_date)

    power_light(pin, interval)

def get_lose_date():
    goals = bm.get_goals()
    lose_dates = {g['slug']: g['losedate'] for g in goals}
    key = min(lose_dates, key=lose_dates.get)
    print(key)
    return lose_dates[key]

def get_pin(lose_date):
    today = datetime.datetime.today()
    tomorrow = today + datetime.timedelta(days=1)
    red_bound = today.replace(hour=23, minute=59, second=59).timestamp()
    yellow_bound = tomorrow.replace(hour=23, minute=59, second=59).timestamp()

    if lose_date <= red_bound:
        # red
        return 9
    elif lose_date <= yellow_bound:
        # yellow
        return 10
    else:
        # green
        return 11

def get_interval(lose_date):
    now = time.time()
    remaining = lose_date - now
    interval = lose_date / 2

    return min(interval, 60 * 10)

def power_light(pin, seconds):
    if pin not in [9, 10, 11]:
        return

    for x in range(0, int(seconds / 2)):
        GPIO.output(pin, True)
        time.sleep(1)
        GPIO.output(pin, False)
        time.sleep(1)

# Pin Setup:
GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme. This uses the pin numbers that match the pin numbers on the Pi Traffic light.
GPIO.setup(9, GPIO.OUT)   # Red LED pin set as output
GPIO.setup(10, GPIO.OUT)   # Yellow LED pin set as output
GPIO.setup(11, GPIO.OUT)   # Green LED pin set as output

try:
    while True:
        tick()
except KeyboardInterrupt:
    print('Interrupted')
finally:
    GPIO.cleanup()