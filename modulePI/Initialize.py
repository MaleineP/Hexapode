import RPi.GPIO as GPIO


class Initialize:

    @staticmethod
    def start_initialisation():
        Initialize.initialize_led()
        Initialize.initialize_i2c()

    @staticmethod
    def initialize_led():
        print("Initialisation of LEDs")
        # green LED
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        # yellow LED
        GPIO.setup(5, GPIO.OUT)

    @staticmethod
    def initialize_i2c():
        print("Initialisation of I2C bus")
