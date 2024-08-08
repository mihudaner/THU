import numpy as np
from plyfile import PlyData
import mayavi.mlab
import open3d as o3d
from copy import deepcopy
import os
import pickle
import datetime


def show_point(*points_list):
    '''
    :param points_list:
    :return:
    '''

    fig = mayavi.mlab.figure("point", bgcolor=(0, 0, 0), size=(1650, 1500))

    for i, points in enumerate(points_list):
        x = points[:, 0]  # x position of point
        y = points[:, 1]  # y position of point
        z = points[:, 2] + i * 0.001  # z position of point
        colors = [(1, 1, 1), (0, 1, 0), (1, 1, 1), (0.5, 0, 1), (0, 0.5, 1), (0.5, 0.5, 0.5), (0.5, 0, 0), (0, 0.5, 0), (0.5, 0.5, 0.5)]

        mayavi.mlab.points3d(x, y, z,
                      scale_factor=0.05 - 0.01 * i,
                      # z,
                      color=colors[i % len(colors)],  # Values used for Color
                      mode="point",
                      # mode="sphere",
                      colormap='spectral',  # 'bone', 'copper', 'gnuplot'
                      # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                      figure=fig,
                      )
    mayavi.mlab.show()


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


points = load_ply_vtx(r"E:\Work\THU\code\THU_Project_project\data\zivid_points\2024-04-02-20-42-59.ply")
show_point(points)
