#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/17 12:30
# @Author  : mihudan~
# @File    : calib
# @Description :

import cv2
import numpy as np

# 读取标定板图像
image = cv2.imread(r'E:\Work\THU\code\THU_Project_project\data\hik_img\2024-04-02-20-56-39.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 定义标定板参数
pattern_size = (11, 8)  # 标定板内角点数

# 查找棋盘格角点
found, corners = cv2.findChessboardCorners(gray, pattern_size, None)

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
    cv2.circle(image, tuple(point1), 5, (255, 255, 0), -1)  # 参数：图像、中心点坐标、半径、颜色、线宽度（-1表示填充）

    point2 = np.array([1394, 1380])
   #  point2 = np.array([941, 1082])# 像素坐标点2
    cv2.circle(image, tuple(point2), 5, (255, 255, 0), -1)  # 参数：图像、中心点坐标、半径、颜色、线宽度（-1表示填充）
    # 显示图像
    cv2.imshow('Points', cv2.resize(image, (0, 0), fx=0.5, fy=0.5))
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
