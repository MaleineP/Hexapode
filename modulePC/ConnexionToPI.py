import socket

hote = "192.168.1.30"
port = 12800

connexion_to_pi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_to_pi.connect((hote, port))
print("Connexion established with the serveur on the port {}".format(port))

msg_to_send = b""
while msg_to_send != b"fin":
    msg_to_send = input("> ")
    msg_to_send = msg_to_send.encode()
    connexion_to_pi.send(msg_to_send)
    msg_recived = connexion_to_pi.recv(1024)
    print(msg_recived.decode())  # Là encore, peut planter s'il y a des accents

print("Fermeture de la connexion")
connexion_to_pi.close()
