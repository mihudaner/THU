import time
import socket

print(time.localtime(time.time()))

datas = {
    "SetOnOrder": {
        "0": "fe050000ff009835",
        "1": "fe050001ff00c9f5",
        "2": "fe050002ff0039f5",
        "3": "fe050003ff006835",
        "4": "fe050004ff00d9f4",
        "5": "fe050005ff008834",
        "6": "fe050006ff007834",
        "7": "fe050007ff0029f4",
        "8": "fe050008ff0019f7",
        "9": "fe050009ff004837",
        "10": "fe05000aff00b837",
        "11": "fe05000bff00e9f7",
        "12": "fe05000cff005836",
        "13": "fe05000dff0009f6",
        "14": "fe05000eff00f9f6",
        "15": "fe05000fff00a836"

    },
    "SetOffOrder": {
        "0": "fe0500000000d9c5",
        "1": "fe05000100008805",
        "2": "fe05000200007805",
        "3": "fe050003000029c5",
        "4": "fe05000400009804",
        "5": "fe0500050000c9c4",
        "6": "fe050006000039c4",
        "7": "fe05000700006804",
        "8": "fe05000800005807",
        "9": "fe050009000009c7",
        "10": "fe05000a0000f9c7",
        "11": "fe05000b0000a807",
        "12": "fe05000c000019c6",
        "13": "fe05000d00004806",
        "14": "fe05000e0000b806",
        "15": "fe05000f0000e9c6"

    }
}


def callPower(ip, port, order):
    s = socket.socket()
    s.connect((ip, port))
    Modbus_16 = ""
    for x in range(0, len(order), 2):
        Modbus_16 += chr(int(order[x:x + 2], 16))

    s.send(Modbus_16.encode('ISO-8859-1'))
    reply_16 = s.recv(50)

    reply_temp = ""
    for i in reply_16.decode('ISO-8859-1'):
        reply_temp += "0x%02x" % ord(i)
    reply_temp = reply_temp[2:]
    mb = ""
    while reply_temp:
        mb += reply_temp[0:2]
        reply_temp = reply_temp[4:]
    return mb


IP = "192.168.10.1"
port = 10000
roads = 8
for s in range(100):
    for orderSet in datas:
        if orderSet == "SetOnOrder":
            for j in range(roads):
                order = datas["SetOnOrder"][str(j)]
                print("发：", order)
                for i in range(25):
                    mb = callPower(IP, port, order)
                    print("收：", mb)
                    if mb != order:
                        continue
                    break
                print("第" + str(j + 1) + "路打开指令已发送")
                j += 1
        else:
            for k in range(roads):
                order = datas["SetOffOrder"][str(k)]
                print("发：", order)
                for t in range(25):
                    mb = callPower(IP, port, order)
                    print("收：", mb)
                    if mb != order:
                        time.sleep(0.3)
                        continue
                    break
                print("第" + str(k + 1) + "路关闭指令已发送")
                k += 1
    s += 1
    print(time.localtime(time.time()))
    print(f"-------第{s}次循环已完成---------")


print(time.localtime(time.time()))
