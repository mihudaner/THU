#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 15:43
# @Author  : mihudan~
# @File    : main.py
# @Description : 主程序
import multiprocessing as mp
import sys
from QTui.QSplashScreen.findwindows import create_loading_window
import os
import time
from src.SAM.SAMDetectorOnnx import sam_run

# set PYTHONIOENCODING=utf-8
# nuitka --mingw64 --standalone --show-progress --show-memory --output-dir=installer --enable-plugin=pyside2 --include-qt-plugins=sensible,styles --nofollow-import-to=QTui,src main.py
# HIK
# 曝光55000
# 增益0

timestamp = time.time()


def print_timestamp():
    """
    打印查看进程启动时间
    Returns
    -------

    """
    global timestamp
    print(time.time() - timestamp)
    timestamp = time.time()


if __name__ == "__main__":
    print("Main.py path：", os.getcwd())
    # 先导入必要的库，先加载等待页面
    if sys.platform == "win32":
        mp.freeze_support()

    # 创建 加载窗口进程
    p_load = mp.Process(target=create_loading_window, name='load')
    p_load.daemon = True
    p_load.start()

    # 把导入慢的库放在加载窗口显示之后
    from src.yolov7.mydetect import img2yolo

    print("Import img2yolo time:")
    print_timestamp()

    # 导入主窗口
    from QTui.boot_mainwindow import window_process, Cfg

    print("Import QTui.boot_mainwindow time:")
    print_timestamp()
    # 双向管道用于在进程间传输图像和检测结果
    pipe_hik = mp.Pipe(duplex=True)
    pipe_sam = mp.Pipe(duplex=True)
    # 启动主界面进程

    p_window = mp.Process(target=window_process, args=(pipe_sam[0], pipe_hik[0]), name='windows')  # 参数传递可以，全局变量不行
    p_window.start()
    print("Create all Process time:")
    print_timestamp()

    # 创建HIK检测的进程
    cfg_hik = Cfg(weights='./src/yolov7/hik_best.pt', imgsz=1280, conf_thres=0.1)
    # 全局变量进程间是独立的，所以只能参数传递
    p_yolo_hik = mp.Process(target=img2yolo, args=(pipe_hik[1], cfg_hik), name='yolo_hik')
    p_yolo_hik.daemon = True
    p_yolo_hik.start()

    p_yolo_sam = mp.Process(target=sam_run, args=(pipe_sam[1],), name='sam')  # 参数传递可以，全局变量不行
    p_yolo_sam.daemon = True
    p_yolo_sam.start()

    p_window.join()
    # window_process(pipe_sam[0], pipe_hik[0])

    print('close all')
