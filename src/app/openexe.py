#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 11:17
# @Author  : mihudan~
# @File    : openexe.py
# @Description : 
import subprocess


def run_exe(exePath):
    # exePath = r"C:\Program Files (x86)\KUKA\WorkVisual 6.0\WorkVisual.exe"
    # # exePath = "D:\\soft\\XTranslator\\Xtranslator\\Xtranslator.exe"
    subprocess.Popen(exePath)
