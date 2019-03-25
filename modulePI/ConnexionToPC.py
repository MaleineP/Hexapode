import socket
from Light import Light
from Move import Move
from Rotate import Rotate
from Temperature import Temperature
from Stop import Stop

hote = '192.168.1.30'
port = 12800

principal_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
principal_connexion.bind((hote, port))
principal_connexion.listen(5)
print("The server listen on port {}".format(port))
connexion_to_pc, infos_connexion = principal_connexion.accept()
Light.green_blink()
light_auto = True
msg_recu = b""
while msg_recu != b"fin":
    msg_recu = connexion_to_pc.recv(1024)
    print(msg_recu.decode())
    if msg_recu.decode() == "walk_forward":
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
    elif msg_recu.decode() == "light_auto_on":
        light_auto = True
    elif msg_recu.decode() == "light_auto_off":
        light_auto = False
    elif Temperature.get_temperature() < 19 and light_auto:
        Light.turn_on_yellow()
    elif Temperature.get_temperature() >= 19 and light_auto:
        Light.turn_off_yellow()
    else:
        Stop.clear_pos()
    connexion_to_pc.send(b"5 / 5")

print("Close connexion")
connexion_to_pc.close()
principal_connexion.close()
