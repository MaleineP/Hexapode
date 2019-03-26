import socket


class ConnexionToPi:

    def __init__(self):
        self.msg_to_send = b""
        hote = "192.168.43.99"
        port = 12800
        self.connexion_to_pi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connexion_to_pi.connect((hote, port))
        #self.connexion_to_pi.listen(5)
        print("Connexion established with the serveur on the port {}".format(port))
        #self.connexion, self.infos_connexion = self.connexion_to_pi.accept()

    def send_message(self, message):
        if message != "fin":
            print("message " + message)
            msg_to_send = message.encode()
            print("msg_to_send " + str(msg_to_send))
            self.connexion_to_pi.sendall(msg_to_send)
            #msg_recu = self.connexion_to_pi.recv(1024)
            #print(msg_recu.decode())
        else:
            print("Fermeture de la connexion")
            self.connexion_to_pi.close()
            #self.connexion.close()
