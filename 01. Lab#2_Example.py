# CE450L/Lab#02/Example
# 20099_MD_MANIRUZZAMAN

import RPi.GPIO as GPIO
import time
import sys

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)     # Pin No 17 connect to LED

# LED will blink until get any input from keyboard.
def blink():
    while True:
        GPIO.output(17, GPIO.HIGH)
        time.sleep(1)               # LED glowing for 1 second
        GPIO.output(17, GPIO.LOW)
        time.sleep(0.5)             # LED will off for 0.5 second
        if keyboard_input():
            break

def keyboard_input():
    # Check any keyboard input is available
    return input_ready()

def input_ready():
    # Check any keyboard input is available
    import select
    return select.select([sys.stdin,],[],[],0.0)[0]

try:
    setup()
    blink()
finally:
    GPIO.cleanup()



