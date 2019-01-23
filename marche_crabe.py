import time
#      _____
# G1 <[     ]> D1
# G2 <[     ]> D2
# G3 <[_____]> D3
#


def deplier_patte(cote, numero):
    print(cote+numero+" depliee")
    # soulever la patte
    # déplier la patte (différent selon gauche ou droite ?)
    # reposer la patte


def replier_patte(cote, numero):
    print(cote+numero+" repliee")
    # soulever la patte
    # replier la patte (différent selon gauche ou droite ?)
    # reposer la patte


def crabe_a_droite():
    replier_patte('g', 1)
    replier_patte('g', 3)
    replier_patte('d', 2)
    deplier_patte('d', 1)
    deplier_patte('d', 3)
    deplier_patte('g', 2)
    time.sleep(1)
    replier_patte('d', 1)
    replier_patte('d', 3)
    replier_patte('g', 2)
    deplier_patte('g', 1)
    deplier_patte('g', 3)
    deplier_patte('d', 2)


def crabe_a_gauche():
    replier_patte('d', 1)
    replier_patte('d', 3)
    replier_patte('g', 2)
    deplier_patte('g', 1)
    deplier_patte('g', 3)
    deplier_patte('d', 2)
    time.sleep(1)
    replier_patte('g', 1)
    replier_patte('g', 3)
    replier_patte('d', 2)
    deplier_patte('d', 1)
    deplier_patte('d', 3)
    deplier_patte('g', 2)
