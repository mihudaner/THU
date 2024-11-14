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
from scipy import interpolate


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
    return  result

def find_biggest_Contours(binary_image):
    """
    查找最大轮廓
           """
    # _, contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找到面积最大的轮廓
    max_contour = max(contours, key=cv2.contourArea)
    return max_contour


def get_out_ellipse(max_contour, original_image,dis_axis=0,DEBUG=False):
    """
    边缘拟合椭圆

    """
    # 椭圆拟合，只对至少包含5个点的轮廓进行椭圆拟合
    if max_contour is None or len(max_contour) < 5:
        return None # 椭圆拟合至少需要5个点

    ellipse = cv2.fitEllipse(max_contour)
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
    adjusted_angle = 90

    # 绘制调整后的椭圆
    ellipse = (center, axes, adjusted_angle)
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

class Ellipse_Detector():
    """
    通过椭圆拟合检测焊缝
    """
    img = None
    gray = None
    calib_obg = None

    def __init__(self,calib_obg, Debug=True):
        self.Debug = Debug
        self.calib_obg = calib_obg

    def read_img(self, img_path=r'.\1021-CCD-left\left-50du-ps.jpg'):
        self.img = cv2.imread(img_path)


    def draw_contours_filled(self, max_contour, original_image):
        # 创建与原图尺寸相同的空白掩码
        random_color = np.random.randint(0, 256, size=(3,)).tolist()

        mask = np.zeros_like(original_image[:, :, 0])  # 单通道掩码
        # 在原始图像上绘制这个轮廓
        cv2.drawContours(self.img, [max_contour], -1, random_color, 2)  # 使用绿色绘制轮廓

        random_color = np.random.randint(0, 256, size=(3,)).tolist()

        # 在掩码上绘制最大轮廓的填充区域
        cv2.drawContours(mask, [max_contour], -1, 255, thickness=cv2.FILLED)

        # 将原图像分离为 B、G、R 三个通道
        b_channel, g_channel, r_channel = cv2.split(original_image)

        # 对轮廓内区域的 R 通道值加 30，确保不超过255
        # r_channel[mask == 255] = np.clip(255, 0, 255)
        # 在 mask == 255 的区域填充随机颜色
        # 生成随机颜色(R, G, B)

        # r_channel[mask == 255] = random_color[2]
        self.img[mask == 255] = random_color
        # 合并回 B、G、R 通道
        # modified_image = cv2.merge([b_channel, g_channel, r_channel])

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
        cv2.drawContours(original_image, contours, -1, 255, thickness=cv2.FILLED)
        if self.Debug:
            cv2.imshow('contours', original_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # 遍历所有轮廓，找到符合红色弧形特征的轮廓
        contour= max(contours, key=cv2.contourArea)
        right_arc_points = None
        if len(contour) >= 5:
            # # 创建字典存储每个y值对应的最小x值点
            # rightmost_points = {}
            rightmost_points = []
            #
            # 遍历轮廓中的所有点
            max_x = 0
            for point in contour:
                x, y = point[0]  # 获取轮廓点的x, y坐标
                # idx = int(y/5)
                # # 如果y坐标还没有存储，或者该y对应的x更小，则更新为更小的x
                # if idx not in leftmost_points or x > leftmost_points[idx][0]:
                #     leftmost_points[idx] = (x, y)

                # 获得point中x的最大值
                if x > max_x:
                    max_x = x


            for point in contour:


                x, y = point[0]  # 获取轮廓点的x, y坐标
                # 并且和上一个距离小于一定值
                if x > max_x-250:
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



    def cal_binary(self, gray, thre,kernel = np.ones((30, 30), np.uint8)):
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
        if self.Debug :
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


    def get_major_axis(self, ellipse,original_image,put_text=False):
        # 获取椭圆的短轴和边界的两个交点
        center, axes, angle = ellipse
        major_axis, minor_axis = axes

        angle = np.deg2rad(angle)
        # 计算椭圆的短轴端点
        x1 = int(center[0] + major_axis / 2 * np.cos(angle))
        y1 = int(center[1] - major_axis / 2 * np.sin(angle))
        x2 = int(center[0] - major_axis / 2 * np.cos(angle))
        y2 = int(center[1] + major_axis / 2 * np.sin(angle))
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

        # cv2.imshow('draw major_axis', original_image)
        # cv2.waitKey(500)
        # cv2.waitKey(0)
        return dis

    def pre_centor(self):
        # 灰度
        gray = cv2.cvtColor(self.img.copy(), cv2.COLOR_BGR2GRAY)
        if self.Debug:
            cv2.imshow('gray', gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        binary_out = self.cal_binary(gray, 150,np.ones((5, 5), np.uint8))
        img = self.img.copy()
        max_contour1 = self.find_first_Contour_right(binary_out, img)

        if max_contour1 is None:
            return False
        ellipse = get_out_ellipse(max_contour1,img,100.0,self.Debug)
        if ellipse is None:
            return False
        # self.get_major_axis(ellipse,img)

        img = self.img.copy()
        # img = draw_ellipse_with_black_background(img, ellipse)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        binary_out = self.cal_binary(gray, 90, np.ones((5, 5), np.uint8))

        max_contour2 = self.find_first_Contour_right(binary_out, self.img.copy())
        img = self.img.copy()
        ellipse1 = get_out_ellipse(max_contour1, img,False)
        ellipse2 = get_out_ellipse(max_contour2, img,False)
        if ellipse1 is None or ellipse2 is None:
            return False
        # self.get_major_axis(ellipse1, img)
        dis = self.get_major_axis(ellipse2, img,True)

        return img,dis



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


    def cal_distance(self,p1,p2):
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
            return None,None

        self.d.read_img(r'..\..\src\molten\1021-CCD-left\left\Basler_acA1600-60gm__21553543__20241021_102120526_0239.tiff')
        self.d.pre_left()

        self.d.read_img(file_path)
        plotimg,dis = self.d.pre_centor()
        print(f"{plotimg.shape}{dis}")
        return  plotimg,dis


if __name__ == "__main__":

    cam = CCD_Pretor(True)
    # 循环读取所有 TIFF 文件
    i =0
    while(1):
        cam.get_next_frame_res()
