#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/31 16:12
# @Author  : mihudan~
# @File    : findwindows.py
# @Description : 
from PySide2.QtWidgets import QApplication, QMainWindow
import cgitb
from QTui.QSplashScreen.GifSplashScreen import GifSplashScreen
import win32gui
import sys


def close_window_by_title(target_title):
    import win32con
    def callback(hwnd, target):
        if win32gui.GetWindowText(hwnd).find(target) != -1:
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

    win32gui.EnumWindows(callback, target_title)


def get_all_window_titles():
    def callback(hwnd, window_titles):
        window_titles.append(win32gui.GetWindowText(hwnd))

    window_titles = []
    win32gui.EnumWindows(callback, window_titles)
    return window_titles


def create_loading_window():
    print("create_loading_window!!!!")
    cgitb.enable(format='text')
    app1 = QApplication.instance()
    if app1 is None:
        app1 = QApplication(sys.argv)
    global splash
    splash = GifSplashScreen()
    splash.show()
    splash.setWindowTitle("GifSplashScreen")
    sys.exit(app1.exec_())


if __name__ == "__main__":
    # window_titles = get_all_window_titles()
    # for title in window_titles:
    #     if title:
    #         print(title)
    create_loading_window()