import time
import socket


def callPower(ip, port, cnt, num):
    s = socket.socket()
    s.connect((ip, port))
    
    
    Modbus_16 = "!"
    for x in range(num-4):
        Modbus_16 += '.'
    Modbus_16+="@"
    Modbus_16+="\r"
    Modbus_16+="\n"

    for a in range(cnt):
        s.send(Modbus_16.encode('ISO-8859-1'))
        time.sleep(0.2)
    


IP = "192.168.1.3"
port = 10000
roads = 8

print(time.localtime(time.time()))
callPower(IP, port,100,30)
print(time.localtime(time.time()))
