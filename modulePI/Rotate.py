import time
import basicMove as m


class Rotate:

    @staticmethod
    def rotate_left():
        # on leve à droite
        m.pos_ext_1(0.5)
        m.pos_ext_9(0.5)
        m.pos_ext_5(0.5)
        # on avance à droite
        m.pos_front_0(0.5)
        m.pos_front_4(0.5)
        # on recule la gauche
        m.pos_back_8(0.5)

        # on baisse à droite
        m.pos_down_1(0.5)
        m.pos_down_9(0.5)
        m.pos_down_5(0.5)

        # on leve à gauche
        m.pos_ext_11(0.5)
        m.pos_ext_3(0.5)
        m.pos_ext_7(0.5)
        # on recule à gauche
        m.pos_back_10(0)
        m.pos_back_6(0)
        # on avance la droite
        m.pos_front_2(0)

        time.sleep(1)

        # on baisse à gauche
        m.pos_down_11(0.5)
        m.pos_down_3(0.5)
        m.pos_down_7(0.5)

        # on recentre tout
        m.pos_mid_0(0)
        m.pos_mid_2(0)
        m.pos_mid_4(0)
        m.pos_mid_6(0)
        m.pos_mid_8(0)
        m.pos_mid_10(0)

    @staticmethod
    def rotate_right():
        # on leve à droite
        m.pos_ext_1(0.5)
        m.pos_ext_9(0.5)
        m.pos_ext_5(0.5)
        # on recule à droite
        m.pos_back_0(0.5)
        m.pos_back_4(0.5)
        # on avance la gauche
        m.pos_front_8(0.5)

        # on baisse à droite
        m.pos_down_1(0.5)
        m.pos_down_9(0.5)
        m.pos_down_5(0.5)

        # on leve à gauche
        m.pos_ext_11(0.5)
        m.pos_ext_3(0.5)
        m.pos_ext_7(0.5)
        # on avance à gauche
        m.pos_front_10(0.5)
        m.pos_front_6(0.5)
        # on recule la droite
        m.pos_back_2(0.5)

        # on baisse à gauche
        m.pos_down_11(0.5)
        m.pos_down_3(0.5)
        m.pos_down_7(0.5)

        time.sleep(1)

        # on recentre tout
        m.pos_mid_0(0)
        m.pos_mid_2(0)
        m.pos_mid_4(0)
        m.pos_mid_6(0)
        m.pos_mid_8(0)
        m.pos_mid_10(0)

        time.sleep(1)
