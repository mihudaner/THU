#!/usr/bin/env python
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
from onnxruntime.quantization import QuantType
from onnxruntime.quantization.quantize import quantize_dynamic

DEBUG = False


def elipse_compute(cnt_n):
    # 拟合椭圆
    ellipse = cv2.fitEllipse(cnt_n)

    # 获取椭圆参数
    center, axes, angle = ellipse

    # 解构椭圆参数
    center_x, center_y = center
    major_axis, minor_axis = axes

    # 计算椭圆的四个顶点坐标
    angle_rad = math.radians(angle)
    cos_angle = math.cos(angle_rad)
    sin_angle = math.sin(angle_rad)

    # 椭圆的四个顶点相对于中心点的偏移量
    offset_x = major_axis / 2 * cos_angle
    offset_y = major_axis / 2 * sin_angle

    # 计算顶点坐标
    vertex1_x = center_x + offset_x
    vertex1_y = center_y + offset_y
    vertex2_x = center_x - offset_x
    vertex2_y = center_y - offset_y
    # 交换偏移量方向
    offset_x = minor_axis / 2 * sin_angle
    offset_y = minor_axis / 2 * cos_angle

    # # 计算顶点坐标
    # vertex3 = (center_x - offset_x, center_y + offset_y)
    # vertex4 = (center_x + offset_x, center_y - offset_y)
    # 计算顶点坐标
    vertex3_x = center_x - offset_x
    vertex3_y = center_y + offset_y
    vertex4_x = center_x + offset_x
    vertex4_y = center_y - offset_y

    # # 打印顶点坐标
    # print("顶点1坐标:", vertex1)
    # print("顶点2坐标:", vertex2)
    # print("顶点3坐标:", vertex3)
    # print("顶点4坐标:", vertex4)
    return vertex1_x, vertex1_y, vertex2_x, vertex2_y, vertex3_x, vertex3_y, vertex4_x, vertex4_y, major_axis, minor_axis


def show_mask(mask, ax, random_color=False):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30 / 255, 144 / 255, 255 / 255, 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)


def show_points(coords, labels, ax, marker_size=375):
    pos_points = coords[labels == 1]
    neg_points = coords[labels == 0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)


def show_box(box, short, long, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0, 0, 0, 0), lw=2))
    # Display label_10 and label_11 at the top-left corner of the box
    ax.text(x0, y0, f'{short:.2f}, {long:.2f}', fontsize=12, color='white', bbox=dict(facecolor='green', alpha=0.5))


def show_mask_cv(mask, img, random_color=True):
    if random_color:
        color = np.random.randint(100, 150, size=(3,), dtype=np.uint8).tolist()
    else:
        color = [30, 144, 255]

    mask = mask.astype(np.uint8)  # Ensure the mask is of type uint8
    h, w = mask.shape[-2:]
    mask_resized = mask[0]

    cannnel = np.random.randint(0, 2, 1)[0]
    img[:, :, cannnel] = np.where(mask_resized, color[cannnel], img[:, :, cannnel])


def show_box_cv(box, short, long, img):
    x0, y0 = int(box[0]), int(box[1])
    x1, y1 = int(box[2]), int(box[3])
    cv2.rectangle(img, (x0, y0), (x1, y1), (0, 255, 0), 2)

    label = f'{short:.2f}, {long:.2f}'
    font_scale = 0.9
    font_thickness = 2
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size, _ = cv2.getTextSize(label, font, font_scale, font_thickness)
    text_w, text_h = text_size

    # Create a filled rectangle as background for text
    cv2.rectangle(img, (x0, y0 - text_h - 10), (x0 + text_w, y0), (0, 255, 0), -1)

    # Put the text over the rectangle
    cv2.putText(img, label, (x0, y0 - 5), font, font_scale, (255, 0, 0), font_thickness, cv2.LINE_AA)


def process_box_labels(labelpath):
    box_labels = []

    with open(labelpath, "r") as file:
        # 逐行读取数据
        for line in file:
            # 分割每一行的数据
            values = line.split(" ")
            # 获取类别标签
            label = int(values[0])
            # 获取边界框坐标
            box_label = [float(value) for value in values[1:5]]
            box_labels.append(box_label)

    # 将 box_labels 转换为 NumPy 数组
    box_labels = np.array(box_labels)

    # 进行坐标变换
    box_labels[:, 0] *= 2448
    box_labels[:, 2] *= 2448
    box_labels[:, 1] *= 2048
    box_labels[:, 3] *= 2048

    box_labels_copy = box_labels.copy()
    box_labels[:, 0] = box_labels_copy[:, 0] - box_labels_copy[:, 2] / 2
    box_labels[:, 1] = box_labels_copy[:, 1] - box_labels_copy[:, 3] / 2
    box_labels[:, 2] = box_labels_copy[:, 0] + box_labels_copy[:, 2] / 2
    box_labels[:, 3] = box_labels_copy[:, 1] + box_labels_copy[:, 3] / 2

    return box_labels


sys.path.append("./src/SAM/")

if DEBUG:
    from segment_anything import sam_model_registry, SamPredictor

    path = "./sam_vit_b_01ec64.pth"
    onnx_model_path = "./sam_onnx_example.onnx"
    device = "cpu"
else:
    from .segment_anything import sam_model_registry, SamPredictor

    path = "./src/SAM//sam_vit_b_01ec64.pth"
    onnx_model_path = "./src/SAM//sam_onnx_example.onnx"
    device = "cpu"


class SAMDetector:
    def __init__(self, modelpath):
        if os.path.exists(modelpath):
            sam_checkpoint = modelpath
            model_type = "vit_b"
            sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
            sam.to(device=device)
            self.predictor = SamPredictor(sam)
            self.img = None
            self.res = None
            self.boxs = None
            if DEBUG:
                self.h = np.load('./homography_matrix.npy')
            else:
                self.h = np.load('./src/SAM/homography_matrix.npy')

            self.ort_session = onnxruntime.InferenceSession(onnx_model_path)

    def detect(self, image, input_boxes):
        """

        :param image: 输入图像
        :param input_boxes: 输入boxs
        :return: 每个boxs内主体的整个图像的masks
        """

        self.predictor.set_image(image)
        transformed_boxes = self.predictor.transform.apply_boxes_torch(input_boxes, image.shape[:2])
        masks, _, _ = self.predictor.predict_torch(
            point_coords=None,
            point_labels=None,
            boxes=transformed_boxes,
            multimask_output=False,
        )
        self.img = image
        self.res = masks

        return masks

    def det(self, image, input_boxes):
        self.predictor.set_image(image)
        self.boxs = input_boxes
        image_embedding = self.predictor.get_image_embedding().cpu().numpy()
        # 创建一个空的np数组
        resmask = np.empty((0, 1, image.shape[0], image.shape[1]), dtype=bool)

        for box in input_boxes:
            input_box = box
            input_point = np.array([[(box[0] + box[2]) // 2, (box[1] + box[3]) // 2]])
            input_label = np.array([1])

            onnx_box_coords = input_box.reshape(2, 2)
            onnx_box_labels = np.array([2, 3])

            onnx_coord = np.concatenate([input_point, onnx_box_coords], axis=0)[None, :, :]
            onnx_label = np.concatenate([input_label, onnx_box_labels], axis=0)[None, :].astype(np.float32)

            onnx_coord = self.predictor.transform.apply_coords(onnx_coord, image.shape[:2]).astype(np.float32)

            onnx_mask_input = np.zeros((1, 1, 256, 256), dtype=np.float32)
            onnx_has_mask_input = np.zeros(1, dtype=np.float32)

            ort_inputs = {
                "image_embeddings": image_embedding,
                "point_coords": onnx_coord,
                "point_labels": onnx_label,
                "mask_input": onnx_mask_input,
                "has_mask_input": onnx_has_mask_input,
                "orig_im_size": np.array(image.shape[:2], dtype=np.float32)
            }

            masks, _, _ = self.ort_session.run(None, ort_inputs)
            masks = masks > self.predictor.model.mask_threshold
            resmask = np.append(resmask, masks, axis=0)

        resmask = torch.tensor(resmask)
        self.img = image
        self.res = resmask
        return resmask

    def get_bimg(self):
        h, w = self.res.shape[-2:]
        result_img = np.zeros_like(self.img[:, :, 0])
        # 遍历所有掩膜
        for i in range(self.res.shape[0]):
            # 获取当前掩膜
            mask = self.res[i, :, :, :]
            mask_image = mask.squeeze()
            binary_mask = mask_image.to(torch.uint8) * 255
            binary_m = binary_mask.cpu().numpy()
            # 二值化掩膜
            ret, threshold_mask = cv2.threshold(binary_m, 0.5, 255, cv2.THRESH_BINARY)

            # 将二值化后的掩膜图像与结果图像进行按位或操作
            result_img = cv2.bitwise_or(result_img, threshold_mask)

        # 将原始图像与结果图像进行按位与操作
        res = cv2.bitwise_and(self.img, self.img, mask=result_img)
        # cv2.imshow('Thresholded Image', res)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return res

    def get_shape_img(self):
        if self.img is None:
            print("SAMDetector no set img!")
            return False
        gray_image = cv2.cvtColor(self.get_bimg(), cv2.COLOR_BGR2GRAY)
        # # 对灰度图像进行 Sobel 锐化操作
        laplacian_image = cv2.Laplacian(gray_image, cv2.CV_64F)

        return cv2.convertScaleAbs(laplacian_image)

    def cal_distance(self, x1, y1, x2, y2):
        # 点击图像上两个点
        # （这里用简单的手动输入坐标代替点击，实际情况可能需要用图形界面来实现）
        point1 = np.array([x1, y1]).astype(int)  # 像素坐标点1
        point2 = np.array([x2, y2]).astype(int)  # 像素坐标点2

        # 将像素坐标转换为实际距离
        point1_hom = np.dot(self.h, np.array([point1[0], point1[1], 1]))
        point2_hom = np.dot(self.h, np.array([point2[0], point2[1], 1]))

        # 计算欧式距离
        pixel_distance = np.linalg.norm(point2 - point1)
        real_distance = np.linalg.norm(point2_hom[:2] / point2_hom[2] - point1_hom[:2] / point1_hom[2])

        cv2.circle(self.img, tuple(point1), 5, (255, 0, 0), -1)  # 参数：图像、中心点坐标、半径、颜色、线宽度（-1表示填充）
        cv2.circle(self.img, tuple(point2), 5, (255, 0, 0), -1)  # 参数：图像、中心点坐标、半径、颜色、线宽度（-1表示填充）

        print("Pixel distance:", pixel_distance)
        print("Real distance:", real_distance)

        # # 显示长短轴端点的图像
        # cv2.imshow('Points', cv2.resize(self.img, (0, 0), fx=0.5, fy=0.5))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return real_distance

    def compute_pos(self):
        if self.img is None:
            print("SAMDetector no set img!")
            return False
        gray = self.get_shape_img()
        # 应用阈值将灰度图像转换为二进制图像
        ret, thresh = cv2.threshold(gray, 0.5, 255, 0)

        # 显示二值化后的图像
        # cv2.imshow('Thresholded Image', thresh)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # 查找轮廓
        ref_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print("检测到的轮廓数:", len(contours))
        contours_len = len(contours)
        # 创建一个空的NumPy数组
        data = np.empty((0, 12), dtype=float)
        if contours_len != self.res.size():
            print("warning contours_len != res.size()")
        # 选择轮廓
        for i in range(contours_len):
            cnt = contours[i]
            vertex1_x, vertex1_y, vertex2_x, vertex2_y, vertex3_x, vertex3_y, vertex4_x, vertex4_y, short, long = elipse_compute(cnt)
            if long < 5:
                print("warning long < 5")
                continue
            print(f"顶点1坐标为 {vertex1_x, vertex1_y}, 顶点2坐标为 {vertex2_x, vertex2_y},顶点3坐标为{vertex3_x, vertex3_y}, 顶点4坐标为 {vertex4_x, vertex4_y}, 长轴为 {long}, 短轴为 {short}\n")

            real_distance_short = self.cal_distance(vertex1_x, vertex1_y, vertex2_x, vertex2_y)
            real_distance_long = self.cal_distance(vertex3_x, vertex3_y, vertex4_x, vertex4_y)
            # 将新的变量添加到NumPy数组
            new_row = np.array([[vertex1_x, vertex1_y, vertex2_x, vertex2_y, vertex3_x, vertex3_y, vertex4_x, vertex4_y, short, long, real_distance_short, real_distance_long]])
            data = np.append(data, new_row, axis=0)
        return data

    def show_result(self, res_label):
        if self.res is None:
            print("SAMDetector no res!")
            return False
        masks = self.res
        fig, ax = plt.subplots(figsize=(100, 100))
        ax.imshow(self.img)
        for mask in masks:
            show_mask(mask.cpu().numpy(), plt.gca(), random_color=True)
        for i, box in enumerate(self.boxs):
            short = res_label[i][10]
            long = res_label[i][11]
            show_box(box, short, long, plt.gca())
        ax.axis('off')

        # Convert the plot to a NumPy array
        fig.canvas.draw()  # Draw the canvas to update the renderer
        image_np = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        image_np = image_np.reshape(fig.canvas.get_width_height()[::-1] + (3,))

        # plt.show()

        return image_np

    def cv2_plot_result(self, res_label):
        if self.res is None:
            print("SAMDetector no res!")
            return False

        masks = self.res
        img = self.img.copy()

        for mask in masks:
            mask_np = mask.cpu().numpy()
            show_mask_cv(mask_np, img, random_color=True)

        for i, box in enumerate(self.boxs):
            short = res_label[i][10]
            long = res_label[i][11]
            show_box_cv(box, short, long, img)

        return img

    def detect2(self, imgs, input_boxes):
        """
        废弃的self.predictor.set_image(局部图像)但是结果不对，整个局部图像都是true，
        而且没有节省什么现存
        :param imgs:
        :param input_boxes:
        :return:
        """
        for box in input_boxes.int():
            img = imgs[box[1]:box[3], box[0]:box[2]]

            box = np.array([0, 0, img.shape[1], img.shape[0]])
            self.predictor.set_image(img)
            # transformed_boxes = self.predictor.transform.apply_boxes_torch(input_boxes, image.shape[:2])
            masks, _, _ = self.predictor.predict(
                point_coords=None,
                point_labels=None,
                box=box[None, :],
                multimask_output=False,
            )

            plt.figure(figsize=(10, 10))
            plt.imshow(img)
            for mask in masks:
                show_mask(mask, plt.gca(), random_color=True)
            plt.axis('off')
            # plt.savefig('/mnt/data02/LYF/THU seg/result/4.png')
            plt.show()

        return masks


def sam_run(pipe):
    while True:
        detector = SAMDetector(path)
        width = 2448 // 1
        height = 2048 // 1

        image = pipe.recv()
        box_labels = pipe.recv()

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (width, height))
        box_labels = np.array(box_labels)[:, :4]
        # box_labels[:, 0] *= width
        # box_labels[:, 2] *= width
        # box_labels[:, 1] *= height
        # box_labels[:, 3] *= height
        # box_labels_copy = box_labels.copy()
        # box_labels[:, 0] = box_labels_copy[:, 0] - box_labels_copy[:, 2] / 2
        # box_labels[:, 1] = box_labels_copy[:, 1] - box_labels_copy[:, 3] / 2
        # box_labels[:, 2] = box_labels_copy[:, 0] + box_labels_copy[:, 2] / 2
        # box_labels[:, 3] = box_labels_copy[:, 1] + box_labels_copy[:, 3] / 2

        input_boxes = torch.tensor(box_labels, device=device)
        detector.det(image, input_boxes)
        res_label = detector.compute_pos()
        # res_img = detector.show_result(res_label)
        res_img = detector.cv2_plot_result(res_label)
        # cv2.imshow('res_img', res_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # vertex1_x, vertex1_y, vertex2_x, vertex2_y, vertex3_x, vertex3_y, vertex4_x, vertex4_y, short, long
        pipe.send(res_label)
        pipe.send(res_img)


def test_run(pipe):
    detector = SAMDetector(path)
    width = 2448 // 1
    height = 2048 // 1
    image = cv2.imread('./000074_2.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (width, height))
    ### 读取一张图片
    box_labels = []
    labelpath = './000074_2.txt'
    with open(labelpath, "r") as file:
        # 逐行读取数据
        for line in file:
            # 分割每一行的数据
            values = line.split(" ")
            # 获取类别标签
            label = int(values[0])
            # 获取边界框坐标
            box_label = [float(value) for value in values[1:5]]
            box_labels.append(box_label)
    box_labels = np.array(box_labels)
    box_labels[:, 0] *= width
    box_labels[:, 2] *= width
    box_labels[:, 1] *= height
    box_labels[:, 3] *= height
    box_labels_copy = box_labels.copy()
    box_labels[:, 0] = box_labels_copy[:, 0] - box_labels_copy[:, 2] / 2
    box_labels[:, 1] = box_labels_copy[:, 1] - box_labels_copy[:, 3] / 2
    box_labels[:, 2] = box_labels_copy[:, 0] + box_labels_copy[:, 2] / 2
    box_labels[:, 3] = box_labels_copy[:, 1] + box_labels_copy[:, 3] / 2

    input_boxes = torch.tensor(box_labels, device=device)

    detector.detect(image, input_boxes)
    detector.det(image, input_boxes)
    res_label = detector.compute_pos()
    # res_img = detector.show_result(res_label)
    res_img = detector.cv2_plot_result(res_label)
    cv2.imshow('res_img', res_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # vertex1_x, vertex1_y, vertex2_x, vertex2_y, vertex3_x, vertex3_y, vertex4_x, vertex4_y, short, long
    pipe.send(res_label)
    pipe.send(res_img)


if __name__ == "__main__":
    import multiprocessing as mp

    pipe_hik = mp.Pipe(duplex=True)
    test_run(pipe_hik[0])
