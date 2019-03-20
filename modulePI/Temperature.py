import time
from w1thermsensor import W1ThermSensor


class Temperature:
    """Lecture #4 -> GPIO 7"""

    @staticmethod
    def get_temperature():
        sensor = W1ThermSensor()
        while True:
            return sensor.get_temperature()
            #temperature = sensor.get_temperature()
            #print("The temperature is %s celsius" % temperature)
            #time.sleep(1)
