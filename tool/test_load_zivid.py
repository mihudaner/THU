#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/20 7:13
# @Author  : mihudan~
# @File    : test_load_zivid.py
# @Description :
import time

import zivid
import datetime
import multiprocessing as mp
import threading
from src.src_zivid.capture_frame import Camera
import subprocess


def print_hi():
    while True:
        time.sleep(0.01)
        print(f'Hi, ')


def test_print_hi():
    t1 = threading.Thread(target=zivid.Application().connect_camera)
    t2 = threading.Thread(target=print_hi)
    t2.start()
    time.sleep(3)
    t1.start()
    t2.join()


def run_exe():
    exePath = r"C:\Program Files (x86)\KUKA\WorkVisual 6.0\WorkVisual.exe"
    # exePath = "D:\\soft\\XTranslator\\Xtranslator\\Xtranslator.exe"
    subprocess.Popen(exePath)


if __name__ == '__main__':
    #  run_exe()
    test_print_hi()
