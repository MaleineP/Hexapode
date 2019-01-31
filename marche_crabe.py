import time
#      _____
# L1 <[     ]> R1
# L2 <[     ]> R2
# L3 <[_____]> R3
#
#


def unfold_leg(side, number):
    print(side+number+" depliee")
    # soulever la patte
    # déplier la patte (différent selon gauche ou droite ?)
    # reposer la patte


def fold_leg(side, number):
    print(side+number+" repliee")
    # soulever la patte
    # replier la patte (différent selon gauche ou droite ?)
    # reposer la patte


def crab_right():
    fold_leg('g', 1)
    fold_leg('g', 3)
    fold_leg('d', 2)
    unfold_leg('d', 1)
    unfold_leg('d', 3)
    unfold_leg('g', 2)
    time.sleep(1)
    fold_leg('d', 1)
    fold_leg('d', 3)
    fold_leg('g', 2)
    unfold_leg('g', 1)
    unfold_leg('g', 3)
    unfold_leg('d', 2)


def crab_left():
    fold_leg('d', 1)
    fold_leg('d', 3)
    fold_leg('g', 2)
    unfold_leg('g', 1)
    unfold_leg('g', 3)
    unfold_leg('d', 2)
    time.sleep(1)
    fold_leg('g', 1)
    fold_leg('g', 3)
    fold_leg('d', 2)
    unfold_leg('d', 1)
    unfold_leg('d', 3)
    unfold_leg('g', 2)
