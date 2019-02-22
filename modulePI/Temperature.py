import os
import glob
import time


class Temperature:
    """Lecture #4 -> GPIO 7"""

    @staticmethod
    def initialize_temperature():
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        device_file = device_folder + '/w1_slave'

    @staticmethod
    def read_temperature_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    @staticmethod
    def read_temperature():
        lines = Temperature.read_temperature_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = Temperature.read_temperature_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f

    @staticmethod
    def get_temperature():
        Temperature.initialize_temperature()
        try:
            while True:
                print(Temperature.read_temperature())
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stop")


# peut remplacer read_temp_raw()
"""import subprocess

def read_temperature_raw():
    catdata = subprocess.Popen(['cat',device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = catdata.communicate()
    out_decode = out.decode('utf-8')
    lines = out_decode.split('\n')
    return lines"""
