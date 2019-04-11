import socket
from contextlib import closing
import sys
import time
import datetime
import requests


TCP_HOST_ADDR = '192.168.0.18'
TCP_HOST_PORT = 5000

temperature = 0
humidity = 0

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
def getTempBySocket():
    data = recSocketvData("getTemperature")
    # set global
    global temperature
    temperature = data.split(',')[0]
    global humidity
    humidity = data.split(',')[1]
    #print(temperature + ' ' + humidity)
    return data


def getTemperature():
    return temperature

def getHumidity():
    return humidity


def loop():
    # get temperature at first
    getTempBySocket()

    while True:
        now = datetime.datetime.now()
        if ((now.minute % 20)  == 0):     # every 20 minutes
            getTempBySocket()

            # Send data to IFTTT
            headers = {
                'Content-Type': 'application/json',
            }
            #data = '{"value1":"2018/01/06 0:03:03","value2":"24","value3":"33"}'
            data = '{"value1":"' + str(now) + '","value2":"' + str(temperature) + '","value3":"' + str(humidity) + '"}'
            response = requests.post('https://maker.ifttt.com/trigger/temperature/with/key/dZoUaA3eWWF2H0HmNNfDtb', headers=headers, data=data)

            #print(temperature + ' ' + humidity)
            #print(data)
            time.sleep(60)

        time.sleep(1)


# Call getTemperature() only when it is executed directry
if __name__ == '__main__':
    loop()


