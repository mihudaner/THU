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

from numpy import ndarray
from scipy import interpolate
import pandas as pd
from scipy.signal import savgol_filter
from scipy.optimize import minimize
from scipy.optimize import least_squares
global img_name
img_name = "None"

# 定义椭圆拟合误差函数
def ellipse_error(params, points):
    h, k, a, b = params
    # 计算拟合误差：根据椭圆方程，计算每个点是否满足 (x - h)^2 / a^2 + (y - k)^2 / b^2 = 1
    error = ((points[:, 0] - h)**2 / a**2 + (points[:, 1] - k)**2 / b**2) - 1
    return error

def img_argue(image,mask,DEBUG=False):
    # 直方图均衡化
    equalized_image = cv2.equalizeHist(image)
    # 增加对比度
    alpha = 2 # 对比度控制
    beta = 0  # 亮度控制

    sharpening_kernel = np.array([[0, -1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]])
    # 高斯模糊
    # equalized_image = cv2.GaussianBlur(equalized_image, (5, 5), 0)

    # 定义结构元素
    # 形态学操作
    # kernel = np.ones((25, 25), np.uint8)
    # equalized_image = cv2.morphologyEx(equalized_image, cv2.MORPH_OPEN, kernel)
    # equalized_image = cv2.morphologyEx(equalized_image, cv2.MORPH_CLOSE, kernel)

    scharrx = cv2.Scharr(equalized_image, cv2.CV_64F, 0, 1)  # soblex内含有负数，要绝对值一下
    scharrx = cv2.convertScaleAbs(scharrx)
    scharry = cv2.Scharr(equalized_image, cv2.CV_64F, 1, 0)
    scharry = cv2.convertScaleAbs(scharry)
    scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)  # 用权值相加效果好一些
    scharrxy = cv2.convertScaleAbs(scharrxy)

    #scharrxy亮度小于100的像素点设为0
    scharrxy[scharrxy < 80] = 0
    scharrxy[~mask] = 0  # Black for false areas



    # # 高斯模糊
    # scharrxy = cv2.GaussianBlur(scharrxy, (5, 5), 0)
    #
    kernel = np.ones((3, 3), np.uint8)
    scharrxy = cv2.morphologyEx(scharrxy, cv2.MORPH_OPEN, kernel)
    # 闭操作是先进行膨胀后进行腐蚀的过程。它通常用于填补物体中的小孔和连接断开的部分
    kernel = np.ones((10, 10), np.uint8)
    scharrxy = cv2.morphologyEx(scharrxy, cv2.MORPH_CLOSE, kernel)

    # 应用锐化滤波器
    # sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
    # 显示结果
    # # Canny 边缘检测
    edges = cv2.Canny(scharrxy, 150, 200)

    if DEBUG:
        cv2.imshow('Equalized Image', equalized_image)
        # cv2.imshow('sharpened_image', sharpened_image)
        cv2.imshow('scharrxy', scharrxy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    global img_name
    cv2.imwrite(os.path.join(save_path, os.path.splitext(img_name)[0] + "-edges.jpg"), edges)
    cv2.imwrite(os.path.join(save_path, os.path.splitext(img_name)[0] + "-scharrxy.jpg"), scharrxy)

    return scharrxy

def pre_elipse(points):
    # 假设已知的右侧轮廓点
    # 右端点坐标 (即椭圆的半长轴右端点)
    # 找到最右侧的点
    x_right,y_right = points[np.argmax(points[:, 0])]
    x_r, y_r = (x_right, y_right)

    # 定义椭圆方程：(x - h)^2 / a^2 + (y - k)^2 / b^2 = 1
    # 目标是通过最小二乘法拟合椭圆的中心 (h, k) 和半长轴 a、半短轴 b

    # 初始猜测：右端点给出a的初始猜测，假设椭圆中心接近右端点的水平位置
    # 假设初始椭圆中心 (h, k) 为 (x_r, y_r)，a为右端点的横坐标，b可以估算为垂直方向上的一个较小值
    initial_guess = [x_r, y_r, x_r, 1]  # 初始中心(h, k)为右端点坐标(x_r, y_r)，a为右端点的横坐标，b取1

    # 使用最小二乘法拟合椭圆参数
    result = least_squares(ellipse_error, initial_guess, args=(points,))
    h_fitted, k_fitted, a_fitted, b_fitted = result.x

    # 输出拟合得到的椭圆参数
    print(f"Fitted center (h, k): ({h_fitted}, {k_fitted})")
    print(f"Fitted a (semi-major axis): {a_fitted}")
    print(f"Fitted b (semi-minor axis): {b_fitted}")

    # 绘制拟合结果
    theta = np.linspace(0, 2 * np.pi, 100)
    x_ellipse = h_fitted + a_fitted * np.cos(theta)
    y_ellipse = k_fitted + b_fitted * np.sin(theta)

    plt.figure(figsize=(6,6))
    plt.plot(x_ellipse, y_ellipse, label="Fitted Ellipse")
    plt.scatter(points[:, 0], points[:, 1], color='red', label="Right-side points")
    plt.scatter(x_r, y_r, color='blue', label="Right endpoint")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title("Ellipse Fitting with Arbitrary Center")
    plt.show()


def draw_smooth_contours(max_contour, original_image):
    """
    绘制平滑的轮廓
    """
    # 提取轮廓的点
    contour_points = max_contour.squeeze()  # 删除多余维度
    # 准备 X 和 Y 坐标数组
    x = contour_points[:, 0]
    y = contour_points[:, 1]

    # 使用 scipy 拟合 B 样条曲线
    tck, u = interpolate.splprep([x, y], s=200.0, per=True)

    # 生成更多点来获得平滑的曲线
    u_fine = np.linspace(0, 1, num=1000)
    x_fine, y_fine = interpolate.splev(u_fine, tck)

    # 将平滑曲线坐标转换为整数，用于绘图
    smooth_contour = np.array([x_fine, y_fine], dtype=np.int32).T

    # 绘制平滑曲线到原图上
    random_color = tuple(np.random.randint(0, 256, size=3).tolist())
    for i in range(len(smooth_contour) - 1):
        cv2.line(original_image, tuple(smooth_contour[i]), tuple(smooth_contour[i + 1]), random_color, 2)


def draw_ellipse_with_black_background(original_image, ellipse):
    """
    在图像中绘制椭圆区域，将椭圆外的部分置为黑色。

    参数:
    original_image: 输入的彩色图像或灰度图像
    ellipse: 包含椭圆参数的元组 (center, axes, angle)
             - center: 椭圆中心 (x, y)
             - axes: 长轴和短轴 (major_axis, minor_axis)
             - angle: 椭圆的旋转角度
    """
    # 创建一个与输入图像大小相同的黑色掩码
    mask = np.zeros_like(original_image, dtype=np.uint8)

    # 在掩码上绘制白色的椭圆
    cv2.ellipse(mask, ellipse, (255, 255, 255), -1)

    # 将原图和掩码结合，椭圆外的区域变为黑色
    result = cv2.bitwise_and(original_image, mask)

    # # 显示结果
    # cv2.imshow('Result', result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return result


def find_biggest_Contours(binary_image):
    """
    查找最大轮廓
           """
    # _, contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找到面积最大的轮廓
    max_contour = max(contours, key=cv2.contourArea)
    return max_contour


def get_out_ellipse(max_contour, original_image, dis_axis=0, DEBUG=False):
    """
    边缘拟合椭圆

    """
    # 椭圆拟合，只对至少包含5个点的轮廓进行椭圆拟合
    if max_contour is None or len(max_contour) < 5:
        return None  # 椭圆拟合至少需要5个点

    ellipse = cv2.fitEllipse(max_contour)
    # ellipse = pre_elipse(max_contour)
    # 将椭圆的角度调整为垂直
    # 获取拟合椭圆的参数
    center, axes, angle = ellipse
    # 将 axes 转换为列表进行修改
    axes_list = list(axes)
    axes_list[0] += dis_axis  # 增加第一个轴的长度
    axes_list[1] += dis_axis  # 增加第一个轴的长度
    # 转换回元组
    axes = tuple(axes_list)
    # 将角度设置为 90 度
    if abs(angle - 90) > 20 and abs(angle - 270) > 20:
        return None

    # 绘制调整后的椭圆
    # ellipse = (center, axes, adjusted_angle)
    cv2.ellipse(original_image, ellipse, (0, 255, 0), 2)  # 绿色椭圆线，线条宽度为2
    # 在原图上绘制椭圆
    if DEBUG:
        cv2.imshow('Sobel Combined', original_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return ellipse


def cal_sobel(img):
    # 计算 Sobel X 方向的梯度
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # dx=1, dy=0 表示只计算 X 方向
    # 计算 Sobel Y 方向的梯度
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # dx=0, dy=1 表示只计算 Y 方向
    # 计算梯度的绝对值
    sobel_x_abs = cv2.convertScaleAbs(sobel_x)
    sobel_y_abs = cv2.convertScaleAbs(sobel_y)
    # 合并 X 和 Y 方向的梯度
    sobel_combined = cv2.addWeighted(sobel_x_abs, 0.5, sobel_y_abs, 0.5, 0)
    cv2.imshow('Sobel Combined', sobel_combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def mirror_contour(contour, img_h=415*2):
    """
    将轮廓分为上下部分，比较两部分最左点坐标，
    根据条件镜像上半部分到下半部分或下半部分到上半部分。

    参数：
    contour: numpy.ndarray，轮廓点集合，形状为 (n, 2)。
    img_h: int，图像高度，用于分割上下部分。

    返回：
    mirrored_contour: numpy.ndarray，处理后的轮廓。
    """
    # 按图像高度分为上下两部分
    upper_contour = contour[contour[:, 1] < img_h // 2]
    lower_contour = contour[contour[:, 1] >= img_h // 2]

    # 找到上半部分和下半部分最左侧点


    if len(upper_contour) == 0:
        left_most_upper = 0
    else:
        left_most_upper = upper_contour[:, 0].min()

    if len(lower_contour) == 0:
        left_most_lower = 0
    else:
        left_most_lower = lower_contour[:, 0].min()

    if left_most_upper < left_most_lower:
        # 上半部分更靠左，镜像上半部分到下半部分
        mirrored_upper = upper_contour.copy()
        mirrored_upper[:, 1] = img_h - mirrored_upper[:, 1]  # 镜像 Y 轴坐标
        mirrored_contour = np.vstack((upper_contour, mirrored_upper))
    else:
        # 下半部分更靠左，镜像下半部分到上半部分
        mirrored_lower = lower_contour.copy()
        mirrored_lower[:, 1] = img_h - mirrored_lower[:, 1]  # 镜像 Y 轴坐标
        mirrored_contour = np.vstack((mirrored_lower, lower_contour))

    return mirrored_contour

class Ellipse_Detector():
    """
    通过椭圆拟合检测焊缝
    """
    img = None
    gray = None
    calib_obg = None

    def __init__(self, calib_obg, Debug=True):
        self.Debug = Debug
        self.calib_obg = calib_obg
        self.mask = self.load_mask(r'./molten_mask.png')

    def read_img(self, img_path=r'.\1021-CCD-left\left-50du-ps.jpg'):
        self.img = cv2.imread(img_path)

    def load_mask(self, mask_path):
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
        # 创建布尔型 mask：大于 125 的位置为 True，小于等于 125 为 False
        bool_mask = mask > 125
        return bool_mask

    def draw_contours_filled(self, max_contour, original_image):
        # 创建与原图尺寸相同的空白掩码
        random_color = np.random.randint(0, 256, size=(3,)).tolist()
        mask = np.zeros_like(original_image[:, :, 0])  # 单通道掩码

        # 在原始图像上绘制这个轮廓
        cv2.drawContours(self.img, [max_contour], -1, random_color, 2)  # 使用绿色绘制轮廓
        random_color = np.random.randint(0, 256, size=(3,)).tolist()

        # 在掩码上绘制最大轮廓的填充区域
        cv2.drawContours(mask, [max_contour], -1, 255, thickness=cv2.FILLED)
        self.img[mask == 255] = random_color

        # 显示结果
        if self.Debug:
            cv2.imshow('draw_contours_filled', original_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def find_first_Contour_right(self, binary_image, original_image):
        # 查找二值化图像中的所有轮廓
        _, contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 寻找所有轮廓
        # contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # 在掩码上绘制最大轮廓的填充区域
        cv2.drawContours(original_image, contours, -1, 255)
        if self.Debug:
            cv2.imshow('contours', original_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # 遍历所有轮廓，找到符合红色弧形特征的轮廓
        if len(contours) is 0:
            return None
        contour = max(contours, key=cv2.contourArea)
        # contour = contour[:, 0, :]
        #
        # # 检查点数是否足够平滑
        # if contour.shape[0] < 3:
        #     raise ValueError("Not enough points to perform smoothing.")
        #
        # # 平滑处理
        # window_length = min(len(contour), 11)
        # if window_length % 2 == 0:
        #     window_length -= 1  # 确保是奇数
        #
        # x_smooth = savgol_filter(contour[:, 0], window_length, 3)  # 平滑 X 坐标
        # y_smooth = savgol_filter(contour[:, 1], window_length, 3)  # 平滑 Y 坐标
        #
        # # 合成平滑后的点 (n, 2)
        # smoothed_coords = np.column_stack((x_smooth, y_smooth))
        #
        # # 恢复到 OpenCV 的格式 (n, 1, 2)
        # contour = smoothed_coords[:, np.newaxis, :].astype(int)

        right_arc_points = None
        if len(contour) >= 5:
            # # 创建字典存储每个y值对应的最小x值点
            rightmost_points = []
            # 遍历轮廓中的所有点
            max_x = 0
            for point in contour:
                # 获取轮廓点的x, y坐标
                x, y = point[0]
                # 获得point中x的最大值
                if x > max_x:
                    max_x = x

            for point in contour:

                x, y = point[0]  # 获取轮廓点的x, y坐标
                # 并且和上一个距离小于一定值
                if x > max_x - 300:
                    rightmost_points.append((x, y))

            # 提取所有左侧的点
            right_arc_points = np.array(rightmost_points)
            # 绘制左侧弧
            if len(right_arc_points) > 0:
                cv2.polylines(original_image, [right_arc_points], isClosed=False, color=(255, 0, 255), thickness=2)

        # 显示结果
        if self.Debug:
            cv2.imshow("Left Arc", original_image)
            # 等待按键关闭窗口
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        # 找到面积最大的轮廓
        return right_arc_points

    def cal_binary(self, gray, thre, kernel=np.ones((30, 30), np.uint8)):
        # 对图像先中值滤波再腐蚀和膨胀操作

        # 二值化处理
        _, binary = cv2.threshold(gray, thre, 255, cv2.THRESH_BINARY)  # 版本问题
        if self.Debug:
            cv2.imshow('binary', binary)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # self.gray = cv2.medianBlur(self.gray, 5)

        binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        # cv2.imshow('MORPH_OPEN', binary)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        if self.Debug:
            cv2.imshow('MORPH_CLOSE', binary)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return binary

    def pre_left(self):
        # 灰度
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray', gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        binary_out = self.cal_binary(gray, 30)
        max_contour1 = find_biggest_Contours(binary_out)
        self.draw_contours_filled(max_contour1, self.img)

        binary_in = self.cal_binary(gray, 200)
        max_contour2 = find_biggest_Contours(binary_in)
        self.draw_contours_filled(max_contour2, self.img)

    def get_major_axis(self, ellipse, original_image,Draw=True, put_text=False,Debug=False):
        # 获取椭圆的短轴和边界的两个交点
        center, axes, angle = ellipse
        major_axis, minor_axis = axes

        angle = np.deg2rad(angle)
        # 计算椭圆的短轴端点
        x1 = int(center[0] + major_axis / 2 * np.cos(angle))
        y1 = int(center[1] - major_axis / 2 * np.sin(angle))
        x2 = int(center[0] - major_axis / 2 * np.cos(angle))
        y2 = int(center[1] + major_axis / 2 * np.sin(angle))
        if Draw:
            # 绘制端点
            cv2.circle(original_image, (x1, y1), 5, (0, 255, 0), -1)
            cv2.circle(original_image, (x2, y2), 5, (0, 255, 0), -1)
            # 绘制长轴
            cv2.line(original_image, (x1, y1), (x2, y2), (255, 255, 0), 2)

        # 计算焊缝宽度
        dis = self.calib_obg.cal_distance((x1, y1), (x2, y2))
        if put_text:
            # 在图像右上角显示焊缝宽度
            text = f'Width: {dis:.2f}'  # 格式化焊缝宽度为小数点后两位
            position = (10, 30)  # 文本的起始位置（距离左上角10px，30px向下）
            font = cv2.FONT_HERSHEY_SIMPLEX  # 字体类型
            font_scale = 1  # 字体大小
            color = (255, 255, 0)  # 文本颜色 (B, G, R) (黄色)
            thickness = 2  # 文本线条宽度
            # 在图像上写入文本
            cv2.putText(original_image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
        if Debug:
            cv2.imshow('draw major_axis', original_image)
            cv2.waitKey(500)
            cv2.waitKey(0)
        return dis

    def pre_centor(self):
        # 灰度
        # diff = cv2.imread(r"F:\1106-molten-108-group\centor\centor-4\Basler_acA1920-40gm__24964907__20241107_214745647_0177.tiff")
        gray = cv2.cvtColor(self.img.copy(), cv2.COLOR_BGR2GRAY) # - cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)


        if self.Debug:
            cv2.imshow('gray', gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        gray = img_argue(gray,self.mask,self.Debug)
        # 应用 mask，false 区域设为黑色

        # binary_out = self.cal_binary(gray, 150, np.ones((5, 5), np.uint8))
        img = self.img.copy()
        max_contour2 = self.find_first_Contour_right(gray, img)
        if max_contour2 is None or len(max_contour2) is 0:
            return False, False, False

        max_contour2 = mirror_contour(max_contour2)

        ellipse2 = get_out_ellipse(max_contour2, img, DEBUG=self.Debug)
        if ellipse2 is None:
            return False, False, False
        dis = self.get_major_axis(ellipse2, img,True, True)

        return img, dis, ellipse2


class Caliber():
    """
    通过棋盘格标定相机，获取单应性矩阵
    """
    img = None
    gray = None
    H = None

    def __init__(self, Debug=True):
        self.Debug = Debug

    def read_img(self, img_path):
        self.img = cv2.imread(img_path)
        # cv2.imshow('img', self.img)  # 黑色部分会变粗
        # cv2.waitKey(0)

        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('img', self.gray)
        # cv2.waitKey(0)

        # ret, thre = cv2.threshold(self.img, 200, 255, cv2.THRESH_BINARY)
        # self.openimg = cv2.morphologyEx(thre, cv2.MORPH_OPEN, kernel)
        # cv2.imshow("img", openimg)
        # cv2.waitKey(0)

    def findHomography(self):
        kernel = np.ones((5, 5), np.uint8)
        pattern_size = (6, 5)
        square_size = 0.8  # 每个棋盘格的实际大小

        # 准备棋盘格的真实物理世界坐标
        objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
        objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)
        objp *= square_size  # 物理坐标的缩放

        # 查找图像中的棋盘格角点
        found, corners = cv2.findChessboardCorners(self.img, pattern_size, None)

        if found:
            # 计算单应性矩阵
            self.H, status = cv2.findHomography(corners, objp[:, :2])
            if not self.Debug:
                return
            # 显示图像并绘制角点
            cv2.drawChessboardCorners(self.img, pattern_size, corners, True)
            cv2.imshow('Chessboard', self.img)
            self.test_Homography()

        else:
            print("未找到棋盘格角点。")

    def cal_distance(self, p1, p2):
        # 将双击的两个点转换为物理世界坐标
        p1 = np.array([p1[0], p1[1], 1])
        p2 = np.array([p2[0], p2[1], 1])

        # 使用单应性矩阵将图像坐标转换为物理坐标
        world_p1 = np.dot(self.H, p1)
        world_p1 /= world_p1[2]

        world_p2 = np.dot(self.H, p2)
        world_p2 /= world_p2[2]

        # 计算实际距离
        distance = np.linalg.norm(world_p1[:2] - world_p2[:2])
        print(f"实际物理距离: {distance:.2f} mm")
        return distance

    def test_Homography(self):

        # 选择两个点
        points = []

        def measure(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDBLCLK:
                cv2.circle(self.img, (x, y), 5, (0, 255, 0), -1)
                points.append((x, y))
                if len(points) == 2:
                    self.cal_distance(points[0], points[1])
                    # 重置点列表
                    points.clear()

        cv2.setMouseCallback('Chessboard', measure)

        while True:
            cv2.imshow('Chessboard', self.img)
            if cv2.waitKey(1) & 0xFF == 27:  # 按 ESC 退出
                break

        cv2.destroyAllWindows()

    def calibrateCamera(self):
        """
        获取单应性矩阵
        Returns
        -------

        """
        kernel = np.ones((5, 5), np.uint8)
        pattern_size = (6, 6)
        square_size = 2

        # 准备标定板的真实世界坐标
        objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
        objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)
        objp *= square_size  # 转换为实际尺寸
        # 存储世界坐标和图像坐标
        obj_points = []  # 3D 点
        img_points = []  # 2D 图像点

        # 定义标定板参数

        # 查找棋盘格角点
        found, corners = cv2.findChessboardCorners(self.img, pattern_size, None)

        if found:
            # 添加对象点和图像点
            obj_points.append(objp)
            img_points.append(corners)

            # 精确化角点
            corners2 = cv2.cornerSubPix(self.gray, corners, (11, 11), (-1, -1),
                                        criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))

            # 相机标定
            ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points,
                                                                                self.gray.shape[::-1], None, None)

            # 打印相机标定结果
            print("Camera Matrix:\n", camera_matrix)
            print("Distortion Coefficients:\n", dist_coeffs)

            if self.Debug:

                # 显示图像并绘制角点
                cv2.drawChessboardCorners(self.img, pattern_size, corners2, True)
                cv2.imshow('Chessboard', self.img)

                # 测距
                def measure(event, x, y, flags, param):
                    if event == cv2.EVENT_LBUTTONDBLCLK:
                        cv2.circle(self.img, (x, y), 5, (0, 255, 0), -1)
                        points.append((x, y))
                        if len(points) == 2:
                            # 将双击的两个点转换为数组形式
                            p1 = np.array(points[0], dtype=np.float32)
                            p2 = np.array(points[1], dtype=np.float32)

                            # 计算像素距离
                            pixel_distance = np.linalg.norm(p1 - p2)

                            # 棋盘格的实际物理宽度（单位为毫米）
                            # 假设棋盘格角点之间的距离为基准（例如：棋盘格长宽均为5x5格子，物理尺寸为5mm x 5mm）
                            # 将每个像素距离转换为实际距离
                            # 假设棋盘宽度在图像中对应的像素距离为棋盘格角点行之间的像素距离
                            real_distance_per_pixel = (pattern_size[0] * square_size) / np.linalg.norm(
                                corners[0] - corners[-1])

                            # 计算实际距离
                            actual_distance = pixel_distance * real_distance_per_pixel

                            print(f"实际距离: {actual_distance:.2f} mm")

                            # 重置
                            points.clear()

                points = []
                cv2.setMouseCallback('Chessboard', measure, None)

                while True:
                    cv2.imshow('Chessboard', self.img)
                    if cv2.waitKey(1) & 0xFF == 27:  # 按 'ESC' 键退出
                        break

                cv2.destroyAllWindows()
        else:
            print("未找到棋盘格角点。")


class CCD_Pretor():
    """
    通过椭圆拟合检测焊缝
    """
    img = None
    gray = None
    path = None
    directory = r'..\\..\src\molten\1021-CCD-left\centor'

    def __init__(self, Debug=True):
        self.Debug = Debug
        self.image_files = self.load_image_files()
        self.current_index = 0

        calib_obg = Caliber(Debug)
        # calib_obg.read_img(r'.\1021-CCD-left\left-50du-ps.jpg')
        calib_obg.read_img(r'..\src\centor-ps.jpg')
        calib_obg.findHomography()
        # 替换为您的文件夹路径
        self.d = Ellipse_Detector(calib_obg, Debug)

    def load_image_files(self):
        # 获取目录下所有的 TIFF 文件并排序
        files = [f for f in os.listdir(self.directory) if f.lower().endswith(('.tiff', '.tif'))]
        files.sort()  # 按文件名排序
        return files

    def get_next_frame(self):
        # 检查是否有可用图像文件
        if not self.image_files:
            raise Exception("没有找到任何 TIFF 图像文件。")

        # 获取下一个图像文件的路径
        file_name = self.image_files[self.current_index]
        self.path = os.path.join(self.directory, file_name)

        # 更新当前索引，以便下次调用时获取下一个图像
        self.current_index += 1

        # 如果到达最后一个文件，则重置索引
        if self.current_index >= len(self.image_files):
            self.current_index = 0

        return self.path

    def get_next_frame_res(self):
        file_path = self.get_next_frame()
        if self.current_index < 117:
            return None, None

        self.d.read_img(r'..\..\src\molten\1021-CCD-left\left\Basler_acA1600-60gm__21553543__20241021_102120526_0239.tiff')
        self.d.pre_left()

        self.d.read_img(file_path)
        plotimg, dis, elip = self.d.pre_centor()
        print(f"{plotimg.shape}{dis}")
        return plotimg, dis

    def get_dir_tiff_res(self, dir_path, save_path):
        # 获取目录中的所有 TIFF 图像文件
        img_files = [f for f in os.listdir(dir_path) if f.lower().endswith(('.tiff', '.tif'))]

        # 初始化存储长轴和短轴的列表
        long_axes = []
        short_axes = []

        # 跳过前 1/4 和后 1/4，仅处理中间的 2/4 数据
        total_files = len(img_files)
        quarter = total_files // 4
        process_files = img_files[quarter: -quarter]  # 中间 2/4 数据

        # 分别获取第 2/4 和第 3/4 的数据
        second_quarter_files = process_files[:len(process_files) // 2]
        third_quarter_files = process_files[len(process_files) // 2:]

        # 处理第 2/4 数据，计算均值
        for img_file in second_quarter_files:
            img_path = os.path.join(dir_path, img_file)

            # 读取图像
            self.d.read_img(img_path)

            # 获取处理结果
            plotimg, dis, elip = self.d.pre_centor()

            if dis is False:
                print(f"False  {img_file}")
                continue

            # 从 elip 解包中心、轴长和角度
            (center_x, center_y), (major_axis, minor_axis), angle = elip
            long_axis = max(major_axis, minor_axis)
            short_axis = min(major_axis, minor_axis)

            # 收集长短轴信息
            long_axes.append(long_axis)
            short_axes.append(short_axis)

        # 计算长轴和短轴的均值
        mean_long = np.mean(long_axes)
        mean_short = np.mean(short_axes)

        # 处理第 3/4 数据，筛选离群值
        filtered_data = []
        third_long_axes = []
        third_short_axes = []
        global img_name
        for img_file in third_quarter_files:
            img_name = img_file
            img_path = os.path.join(dir_path, img_file)

            # 读取图像
            self.d.read_img(img_path)

            # 获取处理结果
            plotimg, dis, elip = self.d.pre_centor()
            if dis is False:
                continue

            # 从 elip 解包中心、轴长和角度
            (center_x, center_y), (major_axis, minor_axis), angle = elip
            long_axis = max(major_axis, minor_axis)
            short_axis = min(major_axis, minor_axis)


            outlier_threshold = 0.2
            # 筛选正常值（基于均值和阈值）并保存 dis 信息
            if abs(long_axis - mean_long) <= outlier_threshold * mean_long and \
                    abs(short_axis - mean_short) <= outlier_threshold * mean_short:
                filtered_data.append({
                    "File": img_file,
                    "LongAxis": long_axis,
                    "ShortAxis": short_axis,
                    "Dis": dis
                })
                save_img = self.d.img.copy()
                self.d.get_major_axis(elip, save_img, True)
                cv2.imwrite(os.path.join(save_path, os.path.splitext(img_file)[0] + ".jpg"), plotimg)
                # 保存长短轴和 dis 信息
                third_long_axes.append(long_axis)
                third_short_axes.append(short_axis)

            # 计算第 3/4 部分的长短轴均值
            final_mean_long = np.mean(third_long_axes)
            final_mean_short = np.mean(third_short_axes)
            final_mean_dis = np.mean([data["Dis"] for data in filtered_data])

            filtered_data.append({
                "File": "Mean",
                "LongAxis": final_mean_long,
                "ShortAxis": final_mean_short,
                "Dis": final_mean_dis
            })

            # 将筛选后的数据保存到 CSV 文件
            df = pd.DataFrame(filtered_data)
            output_csv = os.path.join(save_path, "static.csv")
            # 添加均值作为最后一行

            df.to_csv(output_csv, index=False)

            # 绘制长轴和短轴分布图
            plt.figure(figsize=(10, 6))
            plt.hist(third_long_axes, bins=15, alpha=0.6, label="Long Axis")
            plt.hist(third_short_axes, bins=15, alpha=0.6, label="Short Axis")

            # 添加均值标线
            plt.axvline(final_mean_long, color="blue", linestyle="--", label=f"Mean Long: {final_mean_long:.2f}")
            plt.axvline(final_mean_short, color="red", linestyle="--", label=f"Mean Short: {final_mean_short:.2f}")

            plt.xlabel("Axis Length")
            plt.ylabel("Frequency")
            plt.title("Axis Length Distribution (3/4 Data)")
            plt.legend()

            # 保存长短轴分布图
            output_plot_axes = os.path.join(save_path, "axis_statistics.png")
            plt.savefig(output_plot_axes)
            plt.close()

            # 绘制 dis 分布图
            plt.figure(figsize=(10, 6))
            dis_values = [data["Dis"] for data in filtered_data]
            plt.hist(dis_values, bins=15, alpha=0.7, color="purple", label="Dis")

            # 添加 dis 均值标线
            plt.axvline(final_mean_dis, color="green", linestyle="--", label=f"Mean Dis: {final_mean_dis:.2f}")

            plt.xlabel("Dis Value")
            plt.ylabel("Frequency")
            plt.title("Dis Value Distribution (3/4 Data)")
            plt.legend()

            # 保存 dis 分布图
            output_plot_dis = os.path.join(save_path, "dis_statistics.png")
            plt.savefig(output_plot_dis)
            plt.close()

            print(f"Filtered data saved to {output_csv}")
            print(f"Axis statistics plot saved to {output_plot_axes}")
            print(f"Dis statistics plot saved to {output_plot_dis}")

import os


def rename_folders(dir_path):
    # 遍历目录中的所有文件夹
    for folder_name in os.listdir(dir_path):
        # 检查是否以“旁轴-”开头
        if folder_name.startswith("同轴-"):
            # 构建新的文件夹名称
            new_name = folder_name.replace("同轴-", "centor-")
            # 获取旧的完整路径和新的完整路径
            old_path = os.path.join(dir_path, folder_name)
            new_path = os.path.join(dir_path, new_name)
            # 重命名文件夹
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")

def merge_last_lines(output_file="./merged_last_lines.csv"):
    # 存储最后一行的数据
    last_lines = []

    # 遍历给定目录中的所有文件
    for i in range(1, 11):
        path = f"F:\\1106-molten-108-group\\centor\\centor-{i}"
        file_path = path + "-res\\static.csv"
        try:
            # 读取 CSV 文件
            df = pd.read_csv(file_path)
            # 获取最后一行
            last_row = df.iloc[-1]  # 或者使用 df.tail(1)
            last_row_with_index = last_row.to_dict()  # 转换为字典以便添加索引

            # 在字典中添加索引信息
            last_row_with_index['index'] = i  # 添加索引

            # 将字典添加到列表中
            last_lines.append(last_row_with_index)
        except Exception as e:
            print(f"无法读取文件 {file_path}: {e}")

    # 合并所有最后一行数据为一个 DataFrame
    if last_lines:
        merged_df = pd.DataFrame(last_lines)
        # 保存为新的 CSV 文件
        merged_df.to_csv(output_file, index=False)
        print(f"合并的数据已保存到 {output_file}")
    else:
        print("没有找到有效的 static.csv 文件或没有读取到任何数据。")




if __name__ == "__main__":

    cam = CCD_Pretor(False)
    # 循环读取所有 TIFF 文件

    # for i in range(1, 20):
    #     cam.get_next_frame_res()
    #
    #     path = f"F:\\1106-molten-108-group\\centor\\centor-{i}"
    #     save_path = path + "-res"
    #
    #     if not os.path.exists(save_path):
    #         os.mkdir(save_path)
    #     #清除文件夹
    #     for file in os.listdir(save_path):
    #         os.remove(os.path.join(save_path, file))
    #
    #     cam.get_dir_tiff_res(path,save_path)
    merge_last_lines()

    # while(1):
    #     cam.get_next_frame_res()

    # 指定目标文件夹路径
    # target_dir = r"F:\1106-molten-108-group\centor"
    # rename_folders(target_dir)
