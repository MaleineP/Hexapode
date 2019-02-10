from logging import CRITICAL

import pygame
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QGroupBox, QDialog, QGridLayout, QLabel, \
    QStyleFactory, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot


class Interface(QDialog):
    def __init__(self):
        super(Interface, self).__init__(None)

        self.createInterface()
        self.createVideo()
        self.createLabel()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.label, 0, 1)
        mainLayout.addWidget(self.topRightGroupBox, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        self.setLayout(mainLayout)
        self.setWindowTitle("Hexapode")


    def createLabel(self):
        label = QLabel("Hexapode")
        label.setAlignment(Qt.AlignCenter)
        myFont=QtGui.QFont()
        myFont.setBold(True)
        label.setFont(myFont)
        self.label = label


    def paintEvent(self, event = None):
        paint = QPainter()
        paint.begin(self)
        paint.setPen(Qt.darkGreen)
        paint.setBrush(Qt.green)
        paint.drawEllipse(1, 1, 20, 20)
        paint.setPen(Qt.black)
        paint.setBrush(Qt.gray)
        paint.drawEllipse(25, 1, 20, 20)
        paint.end()

    def createInterface(self):
        self.topLeftGroupBox = QGroupBox("Interface")
        layout = QVBoxLayout()

        label1 = QLabel("Hexapode, avance")
        label2 = QLabel("Hexapode, recule")
        label3 = QLabel("Hexapode, bouge à droite")
        label4 = QLabel("Hexapode, bouge à gauche")
        label5 = QLabel("Hexapode, tourne à droite")
        label6 = QLabel("Hexapode, tourne à gauche")
        label7 = QLabel("Hexapode, lumière")
        label8 = QLabel("Hexapode, distance")
        label9 = QLabel("Hexapode, saute")
        label10 = QLabel("Hexapode, stop")
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)
        layout.addWidget(label6)
        layout.addWidget(label7)
        layout.addWidget(label8)
        layout.addWidget(label9)
        layout.addWidget(label10)

        light = QCheckBox("Lumières")
        layout.addWidget(light)

        captor = QCheckBox("Capteur de distance")
        layout.addWidget(captor)

        rest = QPushButton("Repos")
        layout.addWidget(rest)

        self.topLeftGroupBox.setLayout(layout)

    def createVideo(self):
        self.topRightGroupBox = QGroupBox("Retour Vidéo")


@pyqtSlot()
def onClick():
    exit(0)


last_axis = 3
direction = "none"
app = QApplication([])
app.setStyle(QStyleFactory.create('Fusion'))
interface = Interface()
interface.setStyle(QStyleFactory.create('Fusion'))
interface.show()


pygame.init()
stick = pygame.joystick.init()
x = pygame.joystick.get_count()
if x == 0:
    message = QMessageBox()
    message.setIcon(CRITICAL)
    message.setText("Veuillez brancher un Joystick")
    message.setWindowTitle("Erreur")
    message.open()
else:
    app.exec_()
    events = pygame.event.get()
    for event in events:
        if event == pygame.JOYAXISMOTION:
            axis = event.axis
            value = event.value
            if last_axis == axis:
                print("J'arrête de bouger")
                direction = "none"
            else:
                if axis == 0:
                    if value < 0:
                        print("Je vais à gauche")
                        direction = "left"
                    if value > 0:
                        print("Je vais à droite")
                        direction = "right"
                if axis == 1:
                    if value < 0:
                        print("J'avance")
                        direction = "forward"
                    if value > 0:
                        print("Je recule")
                        direction = "backward"

