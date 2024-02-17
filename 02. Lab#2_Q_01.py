# CE450L/Lab#02/Question-01
# 20099_MD_MANIRUZZAMAN


import RPi.GPIO as GPIO
import time

# select LED pins
led_port_connect = [25, 24, 23, 18, 9, 27, 17, 4]

# GPIO setup
GPIO.setmode(GPIO.BCM)
pwm_info = []

# Set pin and create PWM
for port_num in led_port_connect:
    GPIO.setup(port_num, GPIO.OUT)
    mod_freq = GPIO.PWM(port_num, 100)  # frequency set at 100 Hz
    mod_freq.start(0)  			        # Start with 0% (LED off)
    pwm_info.append(mod_freq)

try:
    print("Press CTRL+C to stop...")
    while True:
        # increase brightness from start to end
        for pwm in pwm_info:
            for dc in range(0, 101, 50):  # duty cycle from 0% to 100%
                pwm.ChangeDutyCycle(dc)
                time.sleep(0.5)       
            pwm.ChangeDutyCycle(0)        # Turn off LED after full brightness

        # decrease brightness from end to start
        for pwm in reversed(pwm_info):
            for dc in range(100, -1, -50): # duty cycle from 100% to 0%
                pwm.ChangeDutyCycle(dc)
                time.sleep(0.5)  
            pwm.ChangeDutyCycle(0)  # LED is off before moving to next

except KeyboardInterrupt:
    print("LED Turn OFF by user.")
finally:
    # Stop PWM and then clean up
    for pwm in pwm_info:
        pwm.stop()
    GPIO.cleanup()
