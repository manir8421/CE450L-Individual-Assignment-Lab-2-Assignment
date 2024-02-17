# CE450L/Lab#02/Question-03
# 20099_MD_MANIRUZZAMAN


import RPi.GPIO as GPIO
import time
import threading

# GPIO pins connected to the led_number.
led_number = [25, 24, 23, 18, 9, 27, 17, 4]
ON = GPIO.HIGH
OFF = GPIO.LOW
close_flg = False

# GPIO using BCM numbering.
GPIO.setmode(GPIO.BCM)
for pin_num in led_number:
    GPIO.setup(pin_num, GPIO.OUT)

def input_for_stop():
    global close_flg
    input("LED start. Press Ctrl+C to stop...")
    close_flg = True

def blink_led_number():

    global close_flg
    try:
        while not close_flg:
            # LED start from the center and move to outwards.
            mid = len(led_number) // 2
            for m in range(mid):
                left, right = mid - m - 1, mid + m
                if close_flg:
                    break
                # LED ON the center led_number and go to outwards.
                if left >= 0: GPIO.output(led_number[left], ON)
                if right < len(led_number): GPIO.output(led_number[right], ON)
                time.sleep(1)
                if left >= 0: GPIO.output(led_number[left], OFF)
                if right < len(led_number): GPIO.output(led_number[right], OFF)
                time.sleep(1)

            if close_flg:
                break

            # Move from the ends back to the center.
            for m in range(mid-1, -1, -1):
                left, right = mid - m - 1, mid + m
                if close_flg:
                    break
                # Turn on the led from the ends back towards the center.
                if left >= 0: GPIO.output(led_number[left], ON)
                if right < len(led_number): GPIO.output(led_number[right], ON)
                time.sleep(0.5)
                if left >= 0: GPIO.output(led_number[left], OFF)
                if right < len(led_number): GPIO.output(led_number[right], OFF)
                time.sleep(0.5)
    finally:
        # Clean GPIO.
        GPIO.cleanup()

try:
    # keyboard input to stop the program.
    input_thread = threading.Thread(target=input_for_stop)
    input_thread.start()
    
    # Start blinking the led.
    blink_led_number()

except KeyboardInterrupt:
    print("Keyboard input found to exit...")
finally:
    close_flg = True
    if input_thread.is_alive():
        input_thread.join()
