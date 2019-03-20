import basicMove as m
import time


class Move:

    @staticmethod
    def walk_forward():
        # on lève à gauche
        m.pos_ext_11(0)
        m.pos_ext_3(0)
        m.pos_ext_7(0)
        # on avance à gauche
        m.pos_front_10(0)
        m.pos_front_2(0)
        m.pos_front_6(0)

        time.sleep(0.5)

        # on baisse à gauche
        m.pos_down_11(0)
        m.pos_down_3(0)
        m.pos_down_7(0)

        time.sleep(0.5)

        # on lève à droite
        m.pos_ext_1(0)
        m.pos_ext_9(0)
        m.pos_ext_5(0)

        # on revient au centre à gauche
        m.pos_mid_10(0)
        m.pos_mid_2(0)
        m.pos_mid_6(0)

        # on avance à droite
        m.pos_front_0(0)
        m.pos_front_8(0)
        m.pos_front_4(0)

        time.sleep(0.5)

        # on baisse à droite
        m.pos_down_1(0)
        m.pos_down_9(0)
        m.pos_down_5(0)

        time.sleep(0.5)

        # on lève à gauche
        m.pos_ext_11(0)
        m.pos_ext_3(0)
        m.pos_ext_7(0)

        # on revient au centre à droite
        m.pos_mid_0(0)
        m.pos_mid_8(0)
        m.pos_mid_4(0)

        # on baisse à gauche
        m.pos_down_3(0)
        m.pos_down_7(0)
        m.pos_down_11(0)


    # changer 0 en 0.5 ?
    @staticmethod
    def walk_backward():
        # on lève à gauche
        m.pos_ext_11(0)
        m.pos_ext_3(0)
        m.pos_ext_7(0)
        # on recule à gauche
        m.pos_back_10(0)
        m.pos_back_2(0)
        m.pos_back_6(0)

        time.sleep(0.5)

        # on baisse à gauche
        m.pos_down_11(0)
        m.pos_down_3(0)
        m.pos_down_7(0)

        time.sleep(0.5)

        # on lève à droite
        m.pos_ext_1(0)
        m.pos_ext_9(0)
        m.pos_ext_5(0)

        # on revient au centre à gauche
        m.pos_mid_10(0)
        m.pos_mid_2(0)
        m.pos_mid_6(0)

        # on recule à droite
        m.pos_back_0(0)
        m.pos_back_8(0)
        m.pos_back_4(0)

        time.sleep(0.5)

        # on baisse à droite
        m.pos_down_1(0)
        m.pos_down_9(0)
        m.pos_down_5(0)

        time.sleep(0.5)

        # on lève à gauche
        m.pos_ext_11(0)
        m.pos_ext_3(0)
        m.pos_ext_7(0)

        # on revient au centre à droite
        m.pos_mid_0(0)
        m.pos_mid_8(0)
        m.pos_mid_4(0)

        time.sleep(0.5)

        # on baisse à gauche
        m.pos_down_11(0)
        m.pos_down_3(0)
        m.pos_down_7(0)
