import time
#      _____
# L1 <[     ]> R1
# L2 <[     ]> R2
# L3 <[_____]> R3
#
#


def leg_forward(side, number):
    print("j'avance " + side + " " + number)
    # soulever la patte
    # avancer la patte
    # reposer la patte


def leg_backward(side, number):
    print("je recule " + side + " " + number)
    # soulever la patte
    # reculer la patte
    # reposer la patte


def initial_position(side, number):
    print("je suis en position initiale " + side + " " + number)
    # ramener la patte sans la soulever
    # ne rien faire si deja en position initiale


def walking_forward():
    leg_forward('g', 1)
    leg_forward('d', 2)
    leg_forward('g', 3)
    initial_position('d', 1)
    initial_position('g', 2)
    initial_position('d', 3)
    time.sleep(1)
    leg_forward('d', 1)
    leg_forward('g', 2)
    leg_forward('d', 3)
    initial_position('g', 1)
    initial_position('d', 2)
    initial_position('g', 3)


def walking_backward():
    leg_backward('g', 1)
    leg_backward('d', 2)
    leg_backward('g', 3)
    initial_position('d', 1)
    initial_position('g', 2)
    initial_position('d', 3)
    time.sleep(1)
    leg_backward('d', 1)
    leg_backward('g', 2)
    leg_backward('d', 3)
    initial_position('g', 1)
    initial_position('d', 2)
    initial_position('g', 3)


