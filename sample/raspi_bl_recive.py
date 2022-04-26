import os
import glob
import time
import RPi.GPIO as GPIO
from bluetooth import *

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

#ラズパイのUUID
uuid = "516825d8-c508-11ec-beba-ff7091cc9b2a"

advertise_service( server_sock, "AquaPiServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
#                  protocols = [ OBEX_UUID ]
                    )


client_sock, client_info = server_sock.accept()

while True:
    print("Waiting for connection on RFCOMM channel %d" % port)
    
    #client_sock, client_info = server_sock.accept()

    print("Accepted connection from ", client_info)

    try:
        print("1")
        data = client_sock.recv(1024)
        print("2")
        if len(data) == 0: break
 #       print(str(len(data)))
        print("Received: %s" % data)
        #data = 'Hello!' 
        #client_sock.send(data)
        #print("sending [%s]" % data)

        print("3")
        data = client_sock.recv(1024)
        print("4")
        if len(data) == 0: break
 #       print(str(len(data)))
        print("Received: %s" % data)


    except IOError as e:
        print(e)

    except KeyboardInterrupt:
        print("disconnected")
        client_sock.close()
        server_sock.close()
        print("all done")
        break
print("3")
