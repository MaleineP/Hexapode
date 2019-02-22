import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def main():
    # down / repos
    # m.pos_down_1()
    # m.pos_down_3()
    # m.pos_down_5()
    # m.pos_down_7()
    # m.pos_down_9()
    # m.pos_down_11()
    # Extérieur
    # m.pos_ext_1()
    # m.pos_ext_3()
    # m.pos_ext_5()
    # m.pos_ext_7()
    # m.pos_ext_9()
    # m.pos_ext_11()
    # Intérieur
    # m.pos_int_1()
    # m.pos_int_3()
    # m.pos_int_5()
    # m.pos_int_7()
    # m.pos_int_9()
    # m.pos_int_11()
    # mid / repos
    # m.pos_mid_0()
    # m.pos_mid_2()
    # m.pos_mid_4()
    # m.pos_mid_6()
    # m.pos_mid_8()
    # m.pos_mid_10()
    # front
    # m.pos_front_0()
    # m.pos_front_2()
    # m.pos_front_4()
    # m.pos_front_6()
    # m.pos_front_8()
    # m.pos_front_10()
    # Arière
    # m.pos_back_0()
    # m.pos_back_2()
    # m.pos_back_4()
    # m.pos_back_6()
    # m.pos_back_8()
    # m.pos_back_10()

if __name__ == "__main__":
    main()

FEET_RIGHT_EXT = 150
FEET_RIGHT_DOWN = 90
FEET_RIGHT_INT = 30

LEG_RIGHT_FRONT = 90
LEG_RIGHT_MIDDLE = 45
LEG_RIGHT_BACK = 0

FEET_LEFT_EXT = 30
FEET_LEFT_DOWN = 90
FEET_LEFT_INT = 150

LEG_LEFT_FRONT = 0
LEG_LEFT_MIDDLE = 45
LEG_LEFT_BACK = 90

def pos_down_1(t):
    kit.servo[1].angle = FEET_RIGHT_DOWN
    time.sleep(t)
def pos_ext_1(t):
    kit.servo[1].angle = FEET_RIGHT_EXT
    time.sleep(t)
def pos_int_1(t):
    kit.servo[1].angle = FEET_RIGHT_INT
    time.sleep(t)

def pos_down_3(t):
    kit.servo[3].angle = FEET_RIGHT_DOWN
    time.sleep(t)
def pos_ext_3(t):
    kit.servo[3].angle = FEET_RIGHT_EXT
    time.sleep(t)
def pos_int_3(t):
    kit.servo[3].angle = FEET_RIGHT_INT
    time.sleep(t)

def pos_down_5(t):
    kit.servo[5].angle = FEET_RIGHT_DOWN
    time.sleep(t)
def pos_ext_5(t):
    kit.servo[5].angle = FEET_RIGHT_EXT
    time.sleep(t)
def pos_int_5(t):
    kit.servo[5].angle = FEET_RIGHT_INT
    time.sleep(t)

def pos_down_7(t):
    kit.servo[7].angle = FEET_LEFT_DOWN
    time.sleep(t)
def pos_ext_7(t):
    kit.servo[7].angle = FEET_LEFT_EXT
    time.sleep(t)
def pos_int_7(t):
    kit.servo[7].angle = FEET_LEFT_INT
    time.sleep(t)

def pos_down_9(t):
    kit.servo[9].angle = FEET_LEFT_DOWN
    time.sleep(t)
def pos_ext_9(t):
    kit.servo[9].angle = FEET_LEFT_EXT
    time.sleep(t)
def pos_int_9(t):
    kit.servo[9].angle = FEET_LEFT_INT
    time.sleep(t)

def pos_down_11(t):
    kit.servo[11].angle = FEET_LEFT_DOWN
    time.sleep(t)
def pos_ext_11(t):
    kit.servo[11].angle = FEET_LEFT_EXT
    time.sleep(t)
def pos_int_11(t):
    kit.servo[11].angle = FEET_LEFT_INT
    time.sleep(t)

def pos_mid_0(t):
    kit.servo[0].angle = LEG_RIGHT_MIDDLE
    time.sleep(t)
def pos_front_0(t):
    kit.servo[0].angle = LEG_RIGHT_FRONT
    time.sleep(t)
def pos_back_0(t):
    kit.servo[0].angle = LEG_RIGHT_BACK
    time.sleep(t)

def pos_mid_2(t):
    kit.servo[2].angle = LEG_RIGHT_MIDDLE
    time.sleep(t)
def pos_front_2(t):
    kit.servo[2].angle = LEG_RIGHT_FRONT
    time.sleep(t)
def pos_back_2(t):
    kit.servo[2].angle = LEG_RIGHT_BACK
    time.sleep(t)

def pos_mid_4(t):
    kit.servo[4].angle = LEG_RIGHT_MIDDLE
    time.sleep(t)
def pos_front_4(t):
    kit.servo[4].angle = LEG_RIGHT_FRONT
    time.sleep(t)
def pos_back_4(t):
    kit.servo[4].angle = LEG_RIGHT_BACK
    time.sleep(t)

def pos_mid_6(t):
    kit.servo[6].angle = LEG_LEFT_MIDDLE
    time.sleep(t)
def pos_front_6(t):
    kit.servo[6].angle = LEG_LEFT_FRONT
    time.sleep(t)
def pos_back_6(t):
    kit.servo[6].angle = LEG_LEFT_BACK
    time.sleep(t)

def pos_mid_8(t):
    kit.servo[8].angle = LEG_LEFT_MIDDLE
    time.sleep(t)
def pos_front_8(t):
    kit.servo[8].angle = LEG_LEFT_FRONT
    time.sleep(t)
def pos_back_8(t):
    kit.servo[8].angle = LEG_LEFT_BACK
    time.sleep(t)

def pos_mid_10(t):
    kit.servo[10].angle = LEG_LEFT_MIDDLE
    time.sleep(t)
def pos_front_10(t):
    kit.servo[10].angle = LEG_LEFT_FRONT
    time.sleep(t)
def pos_back_10(t):
    kit.servo[10].angle = LEG_LEFT_BACK
    time.sleep(t)

