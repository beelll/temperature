import socket
from contextlib import closing
import sys


TCP_HOST_ADDR = '192.168.0.18'
TCP_HOST_PORT = 5000

# Run TCP-IP Socket transfer
def recSocketvData(command):
    s = socket.socket()

    #with closing(s):
    s.connect((TCP_HOST_ADDR, TCP_HOST_PORT))
    s.send(command)
    #while True:
    ret = s.recv(4096)
    return ret


# Receive temprature data by TCP-IP Socket
def getTemp():
    data = recSocketvData("getTemperature")
    print(data)


# Call getTemperature() only when it is executed directry
if __name__ == '__main__':
    getTemp()


