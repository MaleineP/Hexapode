from Connexion import Connexion
from Initialize import Initialize
from Light import Light
from Move import Move
from Rotate import Rotate
from Stop import Stop
from Temperature import Temperature
import time


class MainClass:

    @staticmethod
    def main():
        Initialize.start_initialisation()
        connexion_to_pc = Connexion().get_instance()
        connexion_to_pc.start()
        # Stop.clear_pos()
        # Rotate.rotate_left()
        # Rotate.rotate_right()
        # Move.walk_forward()
        # Move.walk_backward()
        # Light.green_blink()
        # Light.turn_on_yellow()
        # Light.turn_off_yellow()
        # Temperature.get_temperature()
