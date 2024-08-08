#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/3 17:16
# @Author  : mihudan~
# @File    : get_hole_pts
# @Description :
import cv2
from plyfile import PlyData
import os
import pickle

import numpy as np
from mayavi import mlab

if os.path.exists("../Cfgs/matrix/rvec1.npy"):
    rvec = np.load("../Cfgs/matrix/rvec1.npy", allow_pickle=True)
    print("load_rvec:", rvec)

if os.path.exists("../Cfgs/matrix/tvec1.npy"):
    tvec = np.load("../Cfgs/matrix/tvec1.npy", allow_pickle=True)
    print("load_tvec:", tvec)
if os.path.exists("../Cfgs/matrix/camera_matrix1.npy"):
    camera_matrix = np.load("../Cfgs/matrix/camera_matrix1.npy", allow_pickle=True)
    print("load_camera_matrix:", camera_matrix)
if os.path.exists("../Cfgs/matrix/dist_coeffs1.npy"):
    dist_coeffs = np.load("../Cfgs/matrix/dist_coeffs1.npy", allow_pickle=True)
    print("load_dist_coeffs:", dist_coeffs)


def load_ply_vtx(pth):
    """
    加载ply点云文件
    Args:
        pth(str):加载的ply文件路径

    Returns:
        ply点云
    """
    # ply就是得到的对象
    ply = PlyData.read(pth)
    # vtx相当于得到的所有的点的信息，每个点有10个属性
    vtx = ply['vertex']
    # 只要有用的3个属性，stack得到的列表是一堆x，一堆y，一堆z,
    # 我们要对其进行转换，axis=-1是在列的维度拼接，
    # 变成一个x，一个y，一个z这种的格式，
    pts = np.stack([vtx['x'], vtx['y'], vtx['z']], axis=-1)
    return pts


points = load_ply_vtx(r"E:\Work\THU\code\THU_Project_project\data\zivid_points\2024-04-03-13-06-43.ply")
with open('E:\Work\THU\code\THU_Project_project\data\zivid_labels/2024-04-03-13-06-43.pkl', 'rb') as f:
    # 使用pickle.load()函数加载数据
    labels = pickle.load(f)


def get_points_inroi_no_deal():
    global points
    h = 1200
    w = 1920
    rect_leftupy = 300
    rect_h = 800
    rect_leftupx = 800
    rect_w = 800
    pts = points.reshape(h, w, 3)
    points_inroi_no_deal = pts[rect_leftupy:rect_leftupy + rect_h, rect_leftupx:rect_leftupx + rect_w]
    points_inroi_no_deal = points_inroi_no_deal.reshape(-1, 3)
    return points_inroi_no_deal


def get_project_pts():
    points_inroi_no_deal = get_points_inroi_no_deal()
    projected_points, _ = cv2.projectPoints(points_inroi_no_deal, rvec, tvec, camera_matrix, dist_coeffs)
    projected_points = np.reshape(projected_points, (-1, 2))
    return projected_points, points_inroi_no_deal


def get_points_inbox(idx, flip=True):
    """
        第idx个label内的点云
    Args:
        idx(int): 返回的box索引
        flip(bool): 是否需要平移

    Returns:
        box内的点
    """
    try:
        projected_points, points_inroi_no_deal = get_project_pts()
        box = labels[idx]
        mask1 = projected_points[:, 0] > (box[0] - 60 - 40) // 2
        mask2 = projected_points[:, 0] < (box[2] - 60 + 40) // 2
        mask3 = projected_points[:, 1] > (box[1] + 30 - 40) // 2
        mask4 = projected_points[:, 1] < (box[3] + 30 + 40) // 2
        mask = mask1 & mask2 & mask3 & mask4
        return points_inroi_no_deal[mask]

    except IndexError:
        print("out of box range!")


def show_point(*points_list):
    fig = mlab.figure("point", bgcolor=(0, 0, 0), size=(1650, 1500))

    for i, points in enumerate(points_list):
        x = points[:, 0]  # x position of point
        y = points[:, 1]  # y position of point
        z = points[:, 2] + i * 0.01  # z position of point
        colors = [(0, 1, 0), (0, 1, 0), (1, 1, 1)]

        mlab.points3d(x, y, z,
                      scale_factor=0.05 - 0.01 * i,
                      # z,
                      color=colors[i],  # Values used for Color
                      # mode="point",
                      mode="sphere",
                      colormap='spectral',  # 'bone', 'copper', 'gnuplot'
                      # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                      figure=fig,
                      )

    mlab.show()


if __name__ == '__main__':
    for (i, label) in enumerate(labels):
        pts = get_points_inbox(i)
        show_point(pts)
