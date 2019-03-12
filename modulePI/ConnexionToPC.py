import socket
from modulePI.Light import Light
from modulePI.Move import Move
from modulePI.Rotate import Rotate
from modulePI.Initialize import Initialize
from modulePI.Stop import Stop

login = "serge"
password = "delacompta"

hote = '192.168.1.24'
port = 12800

principal_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
principal_connexion.bind((hote, port))
principal_connexion.listen(5)
print("The server listen on port {}".format(port))
connexion_to_pc, infos_connexion = principal_connexion.accept()
Light.green_blink()

msg_recu = b""
while msg_recu != b"fin":
    msg_recu = connexion_to_pc.recv(1024)
    print(msg_recu.decode())
    if msg_recu.decode() == login + " " + password:
        Initialize.start_initialisation()
        Light.turn_off_green()
    elif msg_recu.decode() == "walk_forward":
        Move.walk_forward()
    elif msg_recu.decode() == "walk_backward":
        Move.walk_backward()
    elif msg_recu.decode() == "rotate_right":
        Rotate.rotate_right()
    elif msg_recu.decode() == "rotate_left":
        Rotate.rotate_left()
    elif msg_recu.decode() == "turn_on_yellow":
        Light.turn_on_yellow()
    elif msg_recu.decode() == "turn_off_yellow":
        Light.turn_off_yellow()
    else:
        Stop.clear_pos()
    connexion_to_pc.send(b"5 / 5")

print("Close connexion")
connexion_to_pc.close()
principal_connexion.close()
