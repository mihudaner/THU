import requests
import time
import datetime

# http://{{host}}/mb?opr=open&io=1&addr=254
oenparams = {
    "opr": "open",
    "io": 1,
    "addr": 254
}

closeparams = {
    "opr": "close",
    "io": 1,
    "addr": 254
}

rcvopen="rcv:FE050000FF009835."
rcvclose="rcv:FE0500000000D9C5."


for i in range(100):
    
    start = datetime.datetime.now()    
    r = requests.get(url="http://192.168.3.220/mb", params=oenparams).text
    end = datetime.datetime.now()
    print(end - start)
    if r==rcvopen : 
        print(str(i)+ " openOK:")
    else : 
        print(str(i)+ " openErr:")
        

    start = datetime.datetime.now()
    r = requests.get(url="http://192.168.3.220/mb", params=closeparams).text
    end = datetime.datetime.now()
    print(end - start)
    if r==rcvclose :   
        print(str(i)+ " closeOK:")
    else : 
        print(str(i)+ " closeErr:")
