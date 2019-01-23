import time
#      _____
# G1 <[     ]> D1
# G2 <[     ]> D2
# G3 <[_____]> D3
#
#


def avancer_patte(cote, numero):
    print("j'avance " + cote + " " + numero)
    # soulever la patte
    # avancer la patte
    # reposer la patte


def reculer_patte(cote, numero):
    print("je recule " + cote + " " + numero)
    # soulever la patte
    # reculer la patte
    # reposer la patte


def avancer():
    avancer_patte('g', 1)
    avancer_patte('d', 2)
    avancer_patte('g', 3)
    time.sleep(1)
    avancer_patte('d', 1)
    avancer_patte('g', 2)
    avancer_patte('d', 3)


def reculer():
    reculer_patte('g', 1)
    reculer_patte('d', 2)
    reculer_patte('g', 3)
    time.sleep(1)
    reculer_patte('d', 1)
    reculer_patte('g', 2)
    reculer_patte('d', 3)


