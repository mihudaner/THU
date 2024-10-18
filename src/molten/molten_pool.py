#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/10 2:49
# @Author  : mihudan~
# @File    : molten_pool
# @Description : 

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/15 3:16
# @Author  : mihudan~
# @File    : SAMDetector
# @Description :

import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
import os
import sys
import math
import io
import onnxruntime
kernel=np.ones((5,5),np.uint8)

class Cal_H():
    img = None
    pattern_size = None
    gray = None

    def __init__(self, size=(6, 6)):
        self.pattern_size = size  # 标定板内角点数

    def read_img(self, img_path=r'E:\Work\THU\code\THU_Project_project\src\molten\molten_img\bdb.jpg'):
        self.img = cv2.imread(img_path)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        ret, thre = cv2.threshold(self.img, 200, 255, cv2.THRESH_BINARY)
        self.gray = cv2.morphologyEx(thre, cv2.MORPH_OPEN, kernel)
        cv2.imshow('img', self.gray)  # 黑色部分会变粗
        cv2.waitKey(0)
        cv2.imshow("img", thre)
        cv2.waitKey(0)

    def get_h(self):

        # 定义标定板参数

        # 查找棋盘格角点
        found, corners = cv2.findChessboardCorners(self.gray, self.pattern_size, None)

        if found:

            # 定义点的坐标列表
            points = [corners[0, 0], corners[10, 0], corners[77, 0], corners[87, 0]]

            # 寻找单应性矩阵
            h, _ = cv2.findHomography(np.asarray(points), np.array([[40, 50], [40, 0], [0, 50], [0, 0]]))

            # 保存单应性矩阵为 .npy 文件
            np.save('homography_matrix.npy', h)

            # 点击图像上两个点
            # （这里用简单的手动输入坐标代替点击，实际情况可能需要用图形界面来实现）
            point1 = np.array([1051, 1190])  # 像素坐标点1
            # point1 = np.array([964, 1133])
            cv2.circle(self.img, tuple(point1), 5, (255, 255, 0), -1)  # 参数：图像、中心点坐标、半径、颜色、线宽度（-1表示填充）

            point2 = np.array([1394, 1380])
            #  point2 = np.array([941, 1082])# 像素坐标点2
            cv2.circle(self.img, tuple(point2), 5, (255, 255, 0), -1)  # 参数：图像、中心点坐标、半径、颜色、线宽度（-1表示填充）
            # 显示图像
            cv2.imshow('Points', cv2.resize(self.img, (0, 0), fx=0.5, fy=0.5))
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            # 将像素坐标转换为实际距离
            point1_hom = np.dot(h, np.array([point1[0], point1[1], 1]))
            point2_hom = np.dot(h, np.array([point2[0], point2[1], 1]))

            # 计算欧式距离
            pixel_distance = np.linalg.norm(point2 - point1)
            real_distance = np.linalg.norm(point2_hom[:2] / point2_hom[2] - point1_hom[:2] / point1_hom[2])

            print("Pixel distance:", pixel_distance)
            print("Real distance:", real_distance)
        else:
            print("Chessboard not found.")


if __name__ == "__main__":
    # 读取标定板图像

    obg = Cal_H()
    obg.read_img()
    obg.get_h()
