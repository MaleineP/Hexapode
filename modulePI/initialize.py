import RPi.GPIO as GPIO

def initialize_led():
    # green LED
    GPIO.setmode(GPIO.BMC)
    GPIO.setup(17, GPIO.OUT)
    # yellow LED
    GPIO.setmode(GPIO.BMC)
    GPIO.setup(5, GPIO.OUT)
    # yellow LED
    GPIO.setmode(GPIO.BMC)
    GPIO.setup(6, GPIO.OUT)
    # yellow LED
    GPIO.setmode(GPIO.BMC)
    GPIO.setup(13, GPIO.OUT)
    # yellow LED
    GPIO.setmode(GPIO.BMC)
    GPIO.setup(19, GPIO.OUT)
    # yellow LED
    GPIO.setmode(GPIO.BMC)
    GPIO.setup(26, GPIO.OUT)
