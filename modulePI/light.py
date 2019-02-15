import RPi.GPIO as GPIO
import time

# Yellow 5 -> GPIO 29
# Yellow 6 -> GPIO 31
# Yellow 13 -> GPIO 33
# Yellow 19 -> GPIO 35
# Yellow 26 -> GPIO 37
# Green 17 -> GPIO 11

def green_blink():
    while True:
        GPIO.output(17, False)
        time.sleep(0.5)
        GPIO.output(17, True)
        time.sleep(0.5)

def turn_on_green():
    GPIO.output(17, True)

def turn_off_green():
    GPIO.output(17, False)

def turn_on_yellow():
    GPIO.output(5, True)
    GPIO.output(6, True)
    GPIO.output(13, True)
    GPIO.output(19, True)
    GPIO.output(26, True)

def turn_off_yellow():
    GPIO.output(5, False)
    GPIO.output(6, False)
    GPIO.output(13, False)
    GPIO.output(19, False)
    GPIO.output(26, False)
