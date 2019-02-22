import RPi.GPIO as GPIO
import time


class Light:
    """Yellow 5 -> GPIO 29
    Green 17 -> GPIO 11"""

    @staticmethod
    def green_blink():
        while True:
            GPIO.output(17, False)
            time.sleep(0.5)
            GPIO.output(17, True)
            time.sleep(0.5)

    @staticmethod
    def turn_on_green():
        GPIO.output(17, True)

    @staticmethod
    def turn_off_green():
        GPIO.output(17, False)

    @staticmethod
    def turn_on_yellow():
        GPIO.output(5, True)

    @staticmethod
    def turn_off_yellow():
        GPIO.output(5, False)
