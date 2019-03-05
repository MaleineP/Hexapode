from logging import CRITICAL

import pygame
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QGroupBox, QDialog, QGridLayout, QLabel, \
    QStyleFactory, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot


class Interface(QDialog):
    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def __init__(self):
        super(Interface, self).__init__(None)
        global beginning
        beginning = QDialog()
        beginning.setWindowTitle("Démarrage de l'Hexapode")
        layout = QGridLayout()
        label = QLabel()
        label.setText("Mettre l'hexapode sous tension via le port USB avec la batterie fournie")
        button = QPushButton("Ok")
        button.clicked.connect(self.next)
        layout.addWidget(label)
        layout.addWidget(button)
        beginning.setLayout(layout)
        beginning.show()

    @pyqtSlot()
    def next(self):
        label = QLabel("La lumière verte doit clignoter.\nSi ce n'est pas le cas quitter le logiciel et se référer au manuel utilisateur")
        button = QPushButton("Connexion")
        button.clicked.connect(self.connexionPI)
        self.clearLayout(beginning.layout())
        beginning.layout().addWidget(label)
        beginning.layout().addWidget(button)

    @pyqtSlot()
    def connexionPI(self):
        label = QLabel("Connexion en cours...")
        self.clearLayout(beginning.layout())
        beginning.layout().addWidget(label)
        beginning.show()

    def connexionError(self):
        label = QLabel("Une erreur est survenue, veuillez consulter le manuel utilisateur")
        self.clearLayout(beginning.layout())
        beginning.layout().addWidget(label)
        button = QPushButton("Quitter")
        button.clicked.connect(self.quit)
        beginning.layout().addWidget(button)
        beginning.show()

    @pyqtSlot()
    def quit(self):
        beginning.done()
        exit(0)

    def connexionOK(self):
        self.createInterface()
        self.createVideo()
        self.createLabel()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.label, 0, 1)
        mainLayout.addWidget(self.topRightGroupBox, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        self.setLayout(mainLayout)
        self.setWindowTitle("Hexapode")
        self.setStyle(QStyleFactory.create('Fusion'))
        self.show()
        pygame.init()
        direction = "none"
        stick = pygame.joystick.init()
        x = pygame.joystick.get_count()
        if x == 0:
            message = QMessageBox()
            message.setIcon(CRITICAL)
            message.setText("Veuillez brancher un Joystick")
            message.setWindowTitle("Erreur")
            message.open()
        else:
            events = pygame.event.get(pygame.JOYAXISMOTION)
            for event in events:
                axis = event.axis
                value = event.value
                if (value < 0.005) & (value > -0.005):
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


app = QApplication([])
app.setStyle(QStyleFactory.create('Fusion'))

interface = Interface()

app.exec_()

