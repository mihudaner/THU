#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 12:35
# @Author  : mihudan~
# @File    : DAM8888
# @Description :

import time
import socket
import threading
import crcmod

global s
s = socket.socket()
global lock
lock = threading.Lock()

orders = {
    "SetOnRelay": {
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
    "SetOffRelay": {
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
    },
    "SetAO": "fe100190000810",
    "ReadRelay": "fe010000000829c3",
    "ReadDI": "fe02000000086dc3",
    "ReadAI": "fe0400000008e5c3",
}

"""FE 06 01 90 03 20 9D 3C
字段 含义 备注
FE 设备地址
06 06 指令 模拟量输出
01 90 地址 要设置第一路模拟量寄存器地址 400
03 20 数值 要设置的模拟量数值 0x0320 = 800
9D 3C CRC16"""


def callPower(order):
    global s
    # s = socket.socket()
    # s.connect(("192.168.10.1", 10000))
    Modbus_16 = ""
    for x in range(0, len(order), 2):
        Modbus_16 += chr(int(order[x:x + 2], 16))
    print(f"send:{Modbus_16}")
    s.send(Modbus_16.encode('ISO-8859-1'))
    reply_16 = s.recv(50)
    print("reply_16", reply_16)
    reply_temp = ""
    for i in reply_16.decode('ISO-8859-1'):
        reply_temp += "0x%02x" % ord(i)
    reply_temp = reply_temp[2:]
    mb = ""
    while reply_temp:
        mb += reply_temp[0:2]
        reply_temp = reply_temp[4:]
    return mb


# IP = "192.168.10.1"
# port = 10000
# roads = 8

def SetOnRelay(cannel):
    global lock
    lock.acquire()
    order = orders["SetOnRelay"][str(cannel)]
    print("发：", order)
    for i in range(25):
        mb = callPower(order)
        print("收：", mb)
        if mb != order:
            continue
        break
    print("第" + str(cannel + 1) + "路打开指令已发送")
    lock.release()


def SetOffRelay(cannel):
    global lock
    lock.acquire()
    order = orders["SetOffRelay"][str(cannel)]
    print("发：", order)
    for t in range(25):
        mb = callPower(order)
        print("收：", mb)
        if mb != order:
            print("SetOffRelay error")
            time.sleep(0.3)
            continue
        break
    print("第" + str(cannel + 1) + "路关闭指令已发送")
    lock.release()


def ReadRelay():
    global lock
    lock.acquire()
    order = orders["ReadRelay"]
    print("发：", order)
    for t in range(25):
        mb = callPower(order)
        print("收：", mb)
        if mb[0:4] != "fe01":
            print("ReadRelay error")
            time.sleep(0.3)
            continue
        break
    print(f"查询继电器状态{mb}")
    lock.release()
    return mb[6:8]


def ReadDI():
    global lock
    lock.acquire()
    order = orders["ReadDI"]
    print("发：", order)
    for t in range(25):
        mb = callPower(order)
        print("收：", mb)
        if mb[0:4] != "fe02":
            print("ReadDI error")
            time.sleep(0.3)
            continue
        break
    print(f"查询光耦DI状态{mb}")
    lock.release()
    return mb[6:8]


def ReadAI():
    global lock
    lock.acquire()
    order = orders["ReadAI"]
    print("发：", order)
    for t in range(25):
        mb = callPower(order)
        print("收：", mb)
        if mb[0:4] != "fe04":
            print("ReadAI error")
            time.sleep(0.3)
            continue
        break
    print(f"查询AI状态{mb}")
    lock.release()
    return mb


def int2string16(x):
    return str(hex(x))[2:].zfill(4)


def calculate_crc16(s) -> int:
    data = bytes.fromhex(s)
    # 初始化crc为0xFFFF
    crc = 0xFFFF

    # 循环处理每个数据字节
    for byte in data:
        # 将每个数据字节与crc进行异或操作
        crc ^= byte

        # 对crc的每一位进行处理
        for _ in range(8):
            # 如果最低位为1，则右移一位并执行异或0xA001操作(即0x8005按位颠倒后的结果)
            if crc & 0x0001:
                crc = (crc >> 1) ^ 0xA001
            # 如果最低位为0，则仅将crc右移一位
            else:
                crc = crc >> 1

    # 返回最终的crc值
    return f"{crc:04X}"


def add_crc16(s):
    add = calculate_crc16(s)
    s += add[2:4]
    s += add[0:2]
    return s


def SetAO(values):
    global lock
    lock.acquire()
    order = orders["SetAO"]
    for i in range(8):
        value = values[i]
        order += int2string16(value)
    order = add_crc16(order)
    print("发：", order)
    for t in range(25):
        mb = callPower(order)
        print("收：", mb)
        if mb[0:4] != "fe10":
            print("SetAO error")
            time.sleep(0.3)
            continue
        break
    print(f"设置AO值{values}")
    lock.release()
    return mb


if __name__ == "__main__":
    print(str(hex(40))[2:].zfill(4))
    s = "fe10019000081000000000000000000000000000000000"
    s += add_crc16(s)
    # 计算CRC-16校验码
    print(s)
