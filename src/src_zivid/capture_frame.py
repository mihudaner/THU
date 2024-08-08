#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 19:00
# @Author  : mihudan~
# @File    : capture_frame.py
# @Description : 结构光相机的图像点云，采集，处理，保存
import cv2
import numpy as np
from plyfile import PlyData
import mayavi.mlab
import open3d as o3d
from copy import deepcopy
import os
import pickle
import zivid
import datetime
from Cfgs.cfg import *


class Camera:
    def __init__(self):
        self.app = zivid.Application()
        self.camera = None
        self.settings = zivid.Settings()

        self.settings_2d = zivid.Settings2D()
        self.settings_2d.acquisitions.append(zivid.Settings2D.Acquisition())
        self.settings_2d.acquisitions[0].aperture = 2.83
        self.settings_2d.acquisitions[0].exposure_time = datetime.timedelta(microseconds=10000)

        self.auto_flag = True
        self.settings.processing.filters.noise.removal.enabled = False
        self.settings.processing.filters.outlier.removal.enabled = False
        self.settings.processing.filters.outlier.removal.threshold = 1
        self.settings.processing.filters.reflection.removal.enabled = False
        self.settings.processing.filters.smoothing.gaussian.enabled = True
        self.settings.processing.filters.smoothing.gaussian.threshold = 10
        self.frame = None
        self.datas = None

        ###################  转换矩阵参数 ###################
        self.rvec = None
        self.tvec = None
        self.camera_matrix = None
        self.dist_coeffs = None

        if os.path.exists(RVEC_PATH):
            self.rvec = np.load(RVEC_PATH, allow_pickle=True)
            print("load_rvec:", self.rvec)

        if os.path.exists(TVEC_PATH):
            self.tvec = np.load(TVEC_PATH, allow_pickle=True)
            print("load_tvec:", self.tvec)
        if os.path.exists(CAMERA_MATRIX_PATH):
            self.camera_matrix = np.load(CAMERA_MATRIX_PATH, allow_pickle=True)
            print("load_camera_matrix:", self.camera_matrix)
        if os.path.exists(DIST_COEFFS_PATH):
            self.dist_coeffs = np.load(DIST_COEFFS_PATH, allow_pickle=True)
            print("load_dist_coeffs:", self.dist_coeffs)

    def load_vr(self):
        self.camera = self.app.create_file_camera(FileCameraPATH)

    def load_sql_data(self, roix, roiy, roih, roiw, timestamp):

        rgb = cv2.imread(f"data/zivid_rgb/{timestamp}.jpg")[:, :, ::-1]  # 注释
        self.datas = Datas(rgb,
                           rect_leftupx=int(roix),
                           rect_leftupy=int(roiy),
                           rect_h=int(roih),
                           rect_w=int(roiw),
                           rvec=self.rvec,
                           tvec=self.tvec,
                           camera_matrix=self.camera_matrix,
                           dist_coeffs=self.dist_coeffs,
                           timestamp=timestamp
                           )

        settings_2d = zivid.Settings2D()
        settings_2d.acquisitions.append(zivid.Settings2D.Acquisition())
        settings_2d.acquisitions[0].gain = 16
        settings_2d.acquisitions[0].brightness = 0
        settings_2d.acquisitions[0].aperture = 6.7
        settings_2d.acquisitions[0].exposure_time = datetime.timedelta(microseconds=100000)

        # Get point coordinates as [Height,Width,3] float array
        self.datas.points.xyz = load_ply_vtx(f"data/zivid_points/{timestamp}.ply")  # 注释
        self.datas.normal = cv2.imread(f"data/zivid_normal/{timestamp}.jpg")[:, :, ::-1]  # 注释
        self.datas.ROI_deepmap = cv2.imread(f"data/zivid_deepmap/{timestamp}.jpg")
        self.datas.ROI_normal = cv2.imread(f"data/zivid_normal/{timestamp}.jpg")  # 注释
        self.datas.draw = self.datas.rgb.copy()
        cv2.rectangle(self.datas.draw, (self.datas.rect_leftupx, self.datas.rect_leftupy),
                      (self.datas.rect_leftupx + self.datas.rect_w,
                       self.datas.rect_leftupy + self.datas.rect_h),
                      (255, 0, 0), 2)
        return

    def capture(self,
                roix,
                roiy,
                roih,
                roiw,
                pipe_normal,
                pipe_deep,
                n0x,
                n0y,
                n0z,
                NEED_POINT,
                ratefilterL=0.0,
                ratefilterH=0.3,
                DEBUG=False,
                timestamp="0"
                ):
        """
        采集一帧，包括点云和图像以及检测，结果存在self.datas = Datas()类里，并且会保存在temp文件夹
        Args:
            roix:
            roiy:
            roih:
            roiw:
            pipe_normal:
            pipe_deep:
            n0x:
            n0y:
            n0z:
            ratefilterL:
            ratefilterH:

        Returns:

        """
        if DEBUG:
            rgb = cv2.imread(r"data/zivid_rgb/000053.jpg")[:, :, ::-1]  # 注释
            self.datas = Datas(rgb,
                               rect_leftupx=int(roix),
                               rect_leftupy=int(roiy),
                               rect_h=int(roih),
                               rect_w=int(roiw),
                               rvec=self.rvec,
                               tvec=self.tvec,
                               camera_matrix=self.camera_matrix,
                               dist_coeffs=self.dist_coeffs,
                               timestamp=timestamp
                               )

            settings_2d = zivid.Settings2D()
            settings_2d.acquisitions.append(zivid.Settings2D.Acquisition())
            settings_2d.acquisitions[0].gain = 16
            settings_2d.acquisitions[0].brightness = 0
            settings_2d.acquisitions[0].aperture = 6.7
            settings_2d.acquisitions[0].exposure_time = datetime.timedelta(microseconds=100000)

            # Get point coordinates as [Height,Width,3] float array
            self.datas.points.xyz = load_ply_vtx(INIT_PTS_PATH)  # 注释
            self.datas.normal = cv2.imread(INIT_NORMAL_PATH)[:, :, ::-1]  # 注释
            self.datas.ROI_deepmap = cv2.imread(INIT_ROI_deepmap)
            self.datas.ROI_normal = cv2.imread(INIT_ROI_normal)  # 注释
            self.datas.draw = self.datas.rgb.copy()
            cv2.rectangle(self.datas.draw, (self.datas.rect_leftupx, self.datas.rect_leftupy),
                          (self.datas.rect_leftupx + self.datas.rect_w,
                           self.datas.rect_leftupy + self.datas.rect_h),
                          (255, 0, 0), 2)
        else:

            # 获取2d图像
            rgb = cv2.cvtColor(self.camera.capture(self.settings_2d).image_rgba().copy_data(), cv2.COLOR_RGBA2RGB)  # 这里单独用第一个参数box采集了一次rgb

            self.datas = Datas(rgb,
                               rect_leftupx=int(roix),
                               rect_leftupy=int(roiy),
                               rect_h=int(roih),
                               rect_w=int(roiw),
                               rvec=self.rvec,
                               tvec=self.tvec,
                               camera_matrix=self.camera_matrix,
                               dist_coeffs=self.dist_coeffs,
                               timestamp=timestamp)

            self.datas.draw = self.datas.rgb.copy()
            cv2.rectangle(self.datas.draw, (self.datas.rect_leftupx, self.datas.rect_leftupy), (self.datas.rect_leftupx + self.datas.rect_w, self.datas.rect_leftupy + self.datas.rect_h), (255, 0, 0),
                          2)

            if NEED_POINT:
                # 获取3d点云
                if self.auto_flag == False:
                    self.frame = self.camera.capture(self.settings)
                else:
                    suggest_settings_parameters = zivid.capture_assistant.SuggestSettingsParameters(
                        max_capture_time=datetime.timedelta(milliseconds=1200),
                        ambient_light_frequency=zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.none,
                    )

                    print(f"Running Capture Assistant with parameters: {suggest_settings_parameters}")
                    settings = zivid.capture_assistant.suggest_settings(self.camera, suggest_settings_parameters)

                    print("Settings suggested by Capture Assistant:")
                    for acquisition in settings.acquisitions:
                        print(acquisition)

                    print("Manually configuring processing settings (Capture Assistant only suggests acquisition settings)")
                    """settings.processing.filters.reflection.removal.enabled = True
                    settings.processing.filters.reflection.removal.experimental.mode = "global"
                    settings.processing.filters.smoothing.gaussian.enabled = True
                    settings.processing.filters.smoothing.gaussian.sigma = 1.5"""

                    print("Capturing frame")
                    self.frame = self.camera.capture(settings)

                    point_cloud = self.frame.point_cloud()
                    self.datas.points.xyz = point_cloud.copy_data("xyz").reshape(-1, 3)
                    self.datas.points.rgba = point_cloud.copy_data("rgba").reshape(-1, 4)

                    self.datas.normal = point_cloud.copy_data("normals")
                    self.datas.pre_normal()  # 0-1  0-255 abs

                    self.datas.get_ROI_normal()
                    self.datas.get_roi_deepmap(n0_x=float(n0x), n0_y=float(n0y), n0_z=float(n0z),
                                               rate_filterL=float(ratefilterL), rate_filterH=float(ratefilterH))

    def save_all(self):
        # 对图像进行处理
        self.datas.save_ROI_normal()
        self.datas.save_ply()
        # save temp文件
        self.datas.save_roi_deepmap()
        # self.datas.save_metrix()
        self.datas.save_label()
        idx = self.datas.timestamp
        cv2.imwrite(self.datas.path_rgb + idx + ".jpg", self.datas.rgb)


class Datas:

    def __init__(self,
                 rgb,
                 rect_leftupx,
                 rect_leftupy,
                 rect_h,
                 rect_w,
                 rvec,
                 tvec,
                 camera_matrix,
                 dist_coeffs,
                 timestamp,
                 ):
        # self.rect_leftupx = 700  # ROI左上角坐标
        # self.rect_leftupy = 150  # ROI左上角坐标
        self.rect_leftupx = rect_leftupx  # ROI左上角坐标
        self.rect_leftupy = rect_leftupy  # ROI左上角坐标
        self.rect_h = rect_h  # 待检测高度
        self.rect_w = rect_w  # 待检测宽度

        self.rgb = rgb  # 全视野原始rgb图像
        self.normal = None  # 全视野法向量贴图
        self.draw = None  # 画框显示的rgb图
        self.snr = None  # 全视野snr

        self.ROI_deepmap = None  # ROI内的深度图
        self.ROI_normal = None  # ROI内的法向量贴图
        self.ROI_rgb = None  # ROI内的法向量贴图
        self.transform_normal = None

        self.h = self.rgb.shape[0]  # 原图高
        self.w = self.rgb.shape[1]  # 原图宽
        self.names = None
        self.labels = None
        self.points = Points()  # 全视野点云
        self.roi_flipx = 0  # roi flip时候的值，get_points_inbox_all用到
        self.roi_flipy = 0
        self.roi_flipz = 0

        self.path_normal = "./data/zivid_normal/"
        self.path_rgb = "./data/zivid_rgb/"
        self.path_ROI_rgb = "./data/zivid_ROI_rgb/"
        self.path_points = "./data/zivid_points/"
        self.path_labels = "./data/zivid_labels/"
        self.path_ROI_deepmap = "./data/zivid_deepmap/"
        self.path_matrix = "./Cfgs/matrix/"

        characters_to_remove = " :"
        for char in characters_to_remove:
            timestamp = timestamp.replace(char, '-')
        self.timestamp = timestamp  # 下一次会存为的文件名idx

        self.check_exist(self.path_normal)
        self.check_exist(self.path_ROI_rgb)
        self.check_exist(self.path_points)
        self.check_exist(self.path_labels)
        self.check_exist(self.path_ROI_deepmap)
        self.check_exist(self.path_rgb)
        self.check_exist(self.path_matrix)

        self.rvec = rvec
        self.tvec = tvec
        self.camera_matrix = camera_matrix
        self.dist_coeffs = dist_coeffs

    def check_exist(self, path):
        """
        计算当前帧应该保存的文件名
        Args:
            path:

        Returns:

        """
        if not os.path.exists(path):
            os.makedirs(path)

    def get_ROI_normal(self):
        """
        生成self.draw和 self.ROI_normal， self.ROI_rgb， self.ROI_normal并且保存，以及保存RIO点云
        """
        self.ROI_normal = self.normal[self.rect_leftupy:self.rect_leftupy + self.rect_h, self.rect_leftupx:self.rect_leftupx + self.rect_w].copy()
        self.ROI_rgb = self.rgb[self.rect_leftupy:self.rect_leftupy + self.rect_h, self.rect_leftupx:self.rect_leftupx + self.rect_w].copy()
        self.ROI_normal = cv2.cvtColor(self.ROI_normal, cv2.COLOR_RGB2BGR)

    def save_ROI_normal(self):
        idx = self.timestamp
        cv2.imwrite(self.path_normal + idx + ".jpg", self.normal)
        cv2.imwrite(self.path_ROI_rgb + idx + ".jpg", self.ROI_rgb)

    def pre_normal(self):
        """
        法向量贴图数值处理和标准化
        Returns:

        """

        def enhance_image(image, alpha=1.5, beta=-100):
            enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
            return enhanced_image

        """
        self.normal映射[0,1]->[0,255]
        """
        # self.normal = np.abs(self.normal)
        self.normal = 0.5 * (1 - self.normal)
        self.normal = self.normal * 255.  # [0,1]->[0,255]
        self.normal = np.uint8(self.normal)
        self.normal = enhance_image(self.normal)

    def get_points_inroi(self):
        """
        获得ROI范围内的点云，flip_xyz去除了一定数量为0的点
        """
        try:

            points = self.points.xyz.reshape(self.h, self.w, 3)
            points_inroi = points[self.rect_leftupy:self.rect_leftupy + self.rect_h, self.rect_leftupx:self.rect_leftupx + self.rect_w]
            points_inroi = points_inroi.reshape(-1, 3)
            points_inroi, self.roi_flipx, self.roi_flipy, self.roi_flipz, _ = flip_xyz(points_inroi)
            return points_inroi
        except IndexError:
            print("out of box range!")

    def get_points_inroi_no_deal(self):
        pts = self.points.xyz.reshape(self.h, self.w, 3)
        self.points_inroi_no_deal = pts[self.rect_leftupy:self.rect_leftupy + self.rect_h, self.rect_leftupx:self.rect_leftupx + self.rect_w]
        self.points_inroi_no_deal = self.points_inroi_no_deal.reshape(-1, 3)

    def get_project_pts(self):
        self.get_points_inroi_no_deal()
        self.projected_points, _ = cv2.projectPoints(self.points_inroi_no_deal, self.rvec, self.tvec, self.camera_matrix, self.dist_coeffs)
        self.projected_points = np.reshape(self.projected_points, (-1, 2))

    def get_points_inbox(self, idx, flip=True):
        """
            第idx个label内的点云
        Args:
            idx(int): 返回的box索引
            flip(bool): 是否需要平移

        Returns:
            box内的点
        """
        try:
            self.get_project_pts()

            box = self.labels[idx]

            # 这里//2是应为标定的时候HIK图像是缩小为1/2的，这里的// 2的值应该和标定的down_rate倍率一样
            mask1 = self.projected_points[:, 0] > (box[0] - 80) // 2
            mask2 = self.projected_points[:, 0] < (box[2] + 80) // 2
            mask3 = self.projected_points[:, 1] > (box[1] - 80) // 2
            mask4 = self.projected_points[:, 1] < (box[3] + 80) // 2
            mask = mask1 & mask2 & mask3 & mask4

            return self.points_inroi_no_deal[mask]

        except IndexError:
            print("out of box range!")

    def get_points_inbox_all(self):
        """
        获得所有box内的点云，并且和ROI同样的flip

        """
        points_inbox = []
        for i in range(len(self.labels)):
            if len(points_inbox) == 0:
                points_inbox = self.get_points_inbox(i, flip=False)
            else:
                points_inbox = np.concatenate((points_inbox, self.get_points_inbox(i, flip=False)), axis=0)
        if len(self.labels) != 0:
            points_inbox = points_inbox - np.array([self.roi_flipx, self.roi_flipy, self.roi_flipz])
        return points_inbox

    def save_roi_deepmap(self):
        idx = self.timestamp
        cv2.imwrite(self.path_ROI_deepmap + idx + ".jpg", self.ROI_deepmap)

    def save_matrix(self):
        idx = self.timestamp
        result_obj = {
            'rvec': self.rvec,
            'tvec': self.tvec,
            'camera_matrix': self.camera_matrix,
            'self.dist_coeffs': self.self.dist_coeffs,
        }
        np.save(self.path_matrix + idx + ".txt", result_obj)

    def save_ply(self):
        """
        保存ROI点云
        Returns:

        """

        idx = self.timestamp
        path = self.path_points + idx + ".ply"
        source = o3d.geometry.PointCloud()
        source.points = o3d.utility.Vector3dVector(self.points.xyz)
        o3d.io.write_point_cloud(path, source)

    def save_label(self):
        idx = self.timestamp
        path = self.path_labels + idx + ".pkl"
        with open(path, 'wb') as file:
            pickle.dump(self.labels, file)

    def get_roi_deepmap(self, n0_x=-6.41562717, n0_y=2.2990275, n0_z=28.68353056, rate_filterL=0.2, rate_filterH=1):
        """
        保存矫正的深度图
        Args:
            n0_x: deepmap生成时候，ROI点云需要旋转的法向量x分量
            n0_y: deepmap生成时候，ROI点云需要旋转的法向量y分量
            n0_z: deepmap生成时候，ROI点云需要旋转的法向量z分量
            rate_filter: 离顶部最近的百分之多少进行深度显示

        Returns:

        """
        points = self.points.xyz.reshape(self.h, self.w, 3)
        points_inroi = points[self.rect_leftupy:self.rect_leftupy + self.rect_h, self.rect_leftupx:self.rect_leftupx + self.rect_w]
        points_inroi = points_inroi.reshape(-1, 3)

        points_inroi, _, _, _, mask = flip_xyz(points_inroi, fliter=False)

        # 旋转点云
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points_inroi)
        pcd = pcd_rotate_normal(pcd, n0=np.array([n0_x, n0_y, n0_z]), n1=np.array([0, 0, 1]))
        points_inroi = np.array(pcd.points)
        points_inroi, _, _, _, _ = flip_xyz(points_inroi, fliter=False)

        points_inroi[mask] = np.array([0, 0, 0])  # 旋转后不要的点赋值再0

        img = points_inroi.reshape(self.rect_h, self.rect_w, 3)

        img[:, :, 0:2] = 0
        _range = np.max(img[:, :, 2]) - np.min(img[:, :, 2])
        img[:, :, 2] = (img[:, :, 2] - np.min(img[:, :, 2])) / _range

        maskL = img[:, :, 2] < rate_filterL
        maskH = img[:, :, 2] > rate_filterH
        img[maskL] = np.array([0, 0, 0])
        img[maskH] = np.array([0, 0, 0])

        img[:, :, 2] = (img[:, :, 2] - rate_filterL) / (rate_filterH - rate_filterL)

        img[:, :, 2] = 255 - (img[:, :, 2] * 255).astype(np.int)
        img[maskL] = np.array([0, 0, 0])
        img[maskH] = np.array([0, 0, 0])

        img[:, :, 1] = img[:, :, 2]
        img[:, :, 2] = 0
        self.ROI_deepmap = img


class Points:

    def __init__(self):
        self.xyz = None
        self.rgba = None


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


def view_points(points):
    """
    显示点云
    """
    # 添加坐标轴

    x_input = points[:, 0]
    y_input = points[:, 1]
    z_input = points[:, 2]

    fig = mayavi.mlab.figure("point", bgcolor=(1, 1, 1), size=(650, 500))

    mayavi.mlab.points3d(x_input, y_input, z_input,
                         # z_input,
                         scale_factor=0.05,
                         scale_mode="none",
                         color=(1, 0, 0),  # Values used for Color
                         # mode="point",
                         mode="sphere",
                         colormap='copper',  # 'bone', 'copper', 'gnuplot'
                         # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                         figure=fig,
                         )

    mayavi.mlab.points3d(0, 0, 0,
                         scale_factor=0.3,
                         # scale_mode="none",
                         color=(0, 1, 0),  # Values used for Color
                         # mode="point",
                         mode="sphere",
                         colormap='copper',  # 'bone', 'copper', 'gnuplot'
                         # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                         figure=fig,
                         )
    # mayavi.mlab.plot3d([0, 10], [0, 0], [0, 0], color=(0, 0, 0), tube_radius=1)
    # mayavi.mlab.plot3d([0, 0], [0, 15], [0, 0], color=(0, 0, 0), tube_radius=1)
    # mayavi.mlab.plot3d([0, 0], [0, 0], [0, 15], color=(0, 0, 0), tube_radius=1)
    # mayavi.mlab.text3d(10, -0.5, +0.5, 'X', color=(0, 0, 0), scale=1.)
    # mayavi.mlab.text3d(0, 0.15, +0.5, 'Y', color=(0, 0, 0), scale=1.)
    # mayavi.mlab.text3d(0, -0.5, 15, 'Z', color=(0, 0, 0), scale=1.)

    mayavi.mlab.show()


def pcd_rotate_normal(pointcloud, n0, n1):
    """
    点云法向量旋转
    Args:
        pointcloud: 输入点云
        n0(array): 1x3, 原始法向量
        n1(array): 1x3, 目标法向量

    Returns:
        pcd : open3d PointCloud, 旋转后点云
    """

    pcd = deepcopy(pointcloud)
    n0_norm2 = np.sqrt(sum(n0 ** 2))
    n1_norm2 = np.sqrt(sum(n1 ** 2))
    theta = np.arccos(sum(n0 * n1) / n0_norm2 / n1_norm2)
    r_axis = np.array([n1[2] * n0[1] - n0[2] * n1[1], n0[2] * n1[0] - n1[2] * n0[0], n0[0] * n1[1] - n1[0] * n0[1]])
    r_axis = r_axis * theta / np.sqrt(sum(r_axis ** 2))
    R = pcd.get_rotation_matrix_from_axis_angle(r_axis.T)
    pcd.rotate(R)
    return pcd


def flip_xyz(p, fliter=True):
    """
    点云平移（fliter: 是否会过滤值为0点，False的话返回的点z为0，true删除）
    Args:
        p: 输入点云
        fliter: 是否会过滤值为0点，False的话返回的点z为0，true删除

    Returns:
        p:平移后的点云
        x: 平移后的点云
        y: 平移后的点云
        z: 平移后的点云
        mask: 平移后的点云

    """

    mask = np.isnan(p[:, 2])
    p[mask] = np.array([0, 0, 0])

    if fliter:
        mask = p[:, 2] != 0
        p = p[mask]

    x = np.sort(p[:, 0])
    y = np.sort(p[:, 1])
    z = np.sort(p[:, 2])

    x = x[int(len(x) / 2)]
    y = y[int(len(y) / 2)]
    z = z[int(len(z) / 2)]

    if not fliter:
        mask = p[:, 2] == 0
        p[mask] = z

    p = p - np.array([x, y, z])

    return p, x, y, z, mask


if __name__ == '__main__':
    imgs = Datas(cv2.imread(r"C:\Users\33567\Desktop\1.png"))

    imgs.draw_rectangle()
    cv2.imshow("wk", imgs.draw)
    cv2.waitKey(0)
    cv2.destroyWindow("wk")
    cv2.imshow("wk", imgs.ROI)
    cv2.waitKey(0)
    cv2.destroyWindow("wk")
