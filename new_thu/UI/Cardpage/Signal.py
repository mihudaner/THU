#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/16 16:00
# @Author  : mihudan~
# @File    : Signal
# @Description : 

# Signal.py
from PySide2.QtCore import QObject, Signal


# 定义一个继承自 QObject 的类
class Globel_Signals(QObject):
    DI1_signal = Signal(str)  # 在类中定义 Signal
    DI2_signal = Signal(str)  # 在类中定义 Signal

g_signals = Globel_Signals()