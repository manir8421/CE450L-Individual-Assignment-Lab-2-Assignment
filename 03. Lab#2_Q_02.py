# CE450L/Lab#02/Question-02
# 20099_MD_MANIRUZZAMAN


import RPi.GPIO as GPIO
import time

# GPIO ports for the LEDs
led_port_num = [25, 24, 23, 18, 9, 27, 17, 4]

def setup():
    """GPIO settings and PWM for LED."""
    GPIO.setmode(GPIO.BCM)
    for port_num in led_port_num:
        GPIO.setup(port_num, GPIO.OUT, initial=GPIO.LOW)

def main():
    print("Starting the LED. Press Ctrl+C to stop...")
    while True:
        for m in range(len(led_port_num)):
            GPIO.output(led_port_num[m], GPIO.HIGH)
            if m != len(led_port_num) - m - 1:  
                GPIO.output(led_port_num[-(m + 1)], GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led_port_num[m], GPIO.LOW)
            if m != len(led_port_num) - m - 1:
                GPIO.output(led_port_num[-(m + 1)], GPIO.LOW)

def cleanup():
    GPIO.output(led_port_num, GPIO.LOW)
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        main()
    except KeyboardInterrupt:
        print("Program stop by the user.")
        cleanup()
