#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/11/6 15:14
# @Author  : mihudan~
# @File    : CCDControler
# @Description :

import pypylon.pylon as py
import numpy as np
import cv2
from collections import namedtuple

# this sample has been tested with a Basler acA1920-155uc
# type 'q' or 'ESC' in the window to close it

# the camera is configured to run at high framerate with only two lines hight
# the acquired rows are concatenated as a virtual frame and this frame is displayed


class CCD_camera:
    Debug = True
    def __init__(self):
        self.H = 800
        self.W = 1200
        self.Hoffset = 0
        self.Woffset = 0
        self.deviceList = []
        self.img = None
        self.tlf = None
        self.cams = dict()
        self.IsOpen = dict()

    def enum(self):

        if self.Debug:
            self.deviceList = ["device1","device2"]
        else:
            self.tlf = py.TlFactory.GetInstance()
            print(self.tlf.EnumerateDevices())
            self.deviceList = self.tlf.EnumerateDevices()
        for dv in self.deviceList:
            dv = f"{dv}"
            self.IsOpen[dv] = False
        return [f"[{element}]" for element in self.deviceList]

    def get_state(self, idx):
        if self.Debug: pass
        name =  f"{self.deviceList[idx]}"
        return self.IsOpen[name]

    def change_select(self, idx):
        if self.Debug:
            print(f"change_select {idx}")
            pass
        else:
            name = f"{self.deviceList[idx]}"
            if self.IsOpen[name]:
                self.cam = self.cams[name]
            else:
                self.cam = None

    def open(self, idx):
        name = f"{self.deviceList[idx]}"
        if self.Debug:
            print(f"open {idx}")
            pass
        elif self.cam is None:
                div = self.deviceList[idx]
                self.cam = py.InstantCamera(self.tlf.CreateDevice(div))
                self.cams[name] = self.cam
                self.cam.Open()
                self.cam.Height = self.cam.Height.Max
                self.cam.Width = self.cam.Width.Max
                self.cam.CenterX = True
                self.cam.CenterY = True
                self.cam.StartGrabbing()

        self.IsOpen[name] = True

    def close(self,idx):
        name = f"{self.deviceList[idx]}"
        if self.Debug:
            print(f"close {idx}")
            pass
        elif self.cam is not None:
            self.cam.StopGrabbing()
            self.cam.Close()

            self.cams[name] = None

        self.IsOpen[name] = False

    def set_hw(self,h,w):
        self.H = h
        self.W = w

    def set_offset(self,h,w):
        self.Hoffset = h
        self.Woffset = w

    def get_img(self):
        # 确保图像已经被加载
        if self.img is None:
            raise ValueError("图像未被加载，请检查图像加载过程。")

        # 获取图像的高度和宽度
        img_height, img_width = self.img.shape[:2]

        # 计算中心点
        center_y = img_height // 2
        center_x = img_width // 2

        # 计算裁剪区域的起始和结束坐标
        start_y = center_y - (self.H // 2) + self.Hoffset
        start_x = center_x - (self.W // 2) + self.Woffset
        end_y = start_y + self.H
        end_x = start_x + self.W

        # 创建一个全黑的图像
        result_img = np.zeros((self.H, self.W, 3), dtype=np.uint8)

        # 计算裁剪区域在黑色图像中的位置
        # 确保坐标在合法范围内
        src_start_y = max(0, start_y)
        src_start_x = max(0, start_x)
        src_end_y = min(img_height, end_y)
        src_end_x = min(img_width, end_x)

        # 计算在结果图像中的位置
        dest_start_y = max(0, -start_y)
        dest_start_x = max(0, -start_x)
        dest_end_y = dest_start_y + (src_end_y - src_start_y)
        dest_end_x = dest_start_x + (src_end_x - src_start_x)

        # 将裁剪区域复制到黑色图像中
        result_img[dest_start_y:dest_end_y, dest_start_x:dest_end_x] = self.img[src_start_y:src_end_y, src_start_x:src_end_x]

        return result_img

    def capture(self):
        if self.Debug:
            self.img = cv2.imread("../src/centor_img.tiff")
            return
        with self.cam.RetrieveResult(5000) as result:
            if result.GrabSucceeded():
                self.img = result.Array
                self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2BGR)
            else:
                pass
        return self.img

    def setpara(self,gain,extime):
        self.cam.GainRaw.SetValue(gain)
        self.cam.ExposureTimeRaw.SetValue(extime)

def first_test():
    tlf = py.TlFactory.GetInstance()
    print(tlf.EnumerateDevices())

    # cam = py.InstantCamera(tlf.CreateFirstDevice())
    cam = py.InstantCamera(tlf.CreateDevice(tlf.EnumerateDevices()[1]))
    cam.Open()

    # setup center scan line
    cam.Height = cam.Height.Max
    cam.Width = cam.Width.Max
    cam.CenterX = True
    cam.CenterY = True

    # setup for
    cam.PixelFormat = "Mono8"
    # cam.GainSelector.SetValue()

    cam.GainRaw.SetValue(360)
    # cam.GainAuto = "Continuous"
    # cam.ExposureAuto = "Continuous"
    cam.ExposureAuto.SetValue("Off")
    # cam.ExposureTimeRaw.SetValue(550000)


    # print("Resulting framerate:", cam.ResultingFrameRate.Value)

    cam.StartGrabbing()


    missing_line = np.ones(
        (cam.Height.Value, cam.Width.Value), dtype=np.uint8)*255
    image_idx = 0
    while True:
        # for idx in range(VIRTUAL_FRAME_HEIGHT // SCANLINE_HEIGHT):
        #     with cam.RetrieveResult(2000) as result:
        #         if result.GrabSucceeded():
        #             with result.GetArrayZeroCopy() as out_array:
        #                 img[idx * SCANLINE_HEIGHT:idx *
        #                     SCANLINE_HEIGHT + SCANLINE_HEIGHT] = out_array
        #         else:
        #             img[idx * SCANLINE_HEIGHT:idx * SCANLINE_HEIGHT +
        #                 SCANLINE_HEIGHT] = missing_line
        #             print(idx)
        with cam.RetrieveResult(5000) as result:
            if result.GrabSucceeded():
                img_rgb = result.Array
            else:
                continue

        # Display the resulting frame
        show_img = cv2.resize(img_rgb, (img_rgb.shape[0], img_rgb.shape[1]))
        cv2.imshow('Linescan View', img_rgb)
        cv2.imwrite("1.png",img_rgb)

        image_idx += 1
        if cv2.waitKey(1) & 0xFF in (ord('q'), 27):
            break

    # When everything done, release the capture
    cam.StopGrabbing()
    cv2.destroyAllWindows()

    cam.Close()
