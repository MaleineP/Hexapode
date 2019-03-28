import socket
import time
from Light import Light
from Move import Move
from Rotate import Rotate
from Temperature import Temperature
from Stop import Stop

hote = '192.168.43.99'
port = 12800

principal_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
principal_connexion.bind((hote, port))
principal_connexion.listen(5)
print("The server listen on port {}".format(port))
Light.turn_on_green()
time.sleep(0.5)
Light.turn_off_green()
Light.green_blink()
connexion_to_pc, infos_connexion = principal_connexion.accept()
print("infos : " + str(infos_connexion))
light_auto = False
msg_recu = b""
while msg_recu != b"fin":
    print("light_auto : " + str(light_auto))
    temp = Temperature.get_temperature()
    print("temp : " + str(temp))
    msg_recu = connexion_to_pc.recv(1024)
    print("msg_recieved : " + msg_recu.decode())
    if msg_recu.decode() == "walkforward":
        Move.walk_forward()
    elif msg_recu.decode() == "walkbackward":
        Move.walk_backward()
    elif msg_recu.decode() == "rotateright":
        Rotate.rotate_right()
    elif msg_recu.decode() == "rotateleft":
        Rotate.rotate_left()
    elif msg_recu.decode() == "turnonyellow":
        Light.turn_on_yellow()
    elif msg_recu.decode() == "turnoffyellow":
        Light.turn_off_yellow()
    elif msg_recu.decode() == "lightautoon":
        light_auto = True
    elif msg_recu.decode() == "lightautooff":
        light_auto = False
    else:
        print("Clear position")
        #Stop.clear_pos()

    if temp >= 21 and light_auto:
        Light.turn_on_yellow()
    elif temp < 21 and light_auto:
        Light.turn_off_yellow()

principal_connexion.close()
