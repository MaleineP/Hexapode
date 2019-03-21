import socket


class ConnexionToPi:

    def __init__(self):
        self.msg_to_send = b""
        hote = "192.168.1.30"
        port = 12800
        self.connexion_to_pi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connexion_to_pi.connect((hote, port))
        print("Connexion established with the serveur on the port {}".format(port))

    def send_message(self, message):
        if message != "fin":
            msg_to_send = message.encode()
            self.connexion_to_pi.send(msg_to_send)
            msg_recived = self.connexion_to_pi.recv(1024)
            print(msg_recived.decode())  # Là encore, peut planter s'il y a des accents
        else:
            print("Fermeture de la connexion")
            self.connexion_to_pi.close()
