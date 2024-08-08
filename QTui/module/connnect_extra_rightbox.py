#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 10:32
# @Author  : mihudan~
# @File    : ConnnectExtraRightBox
# @Description :
from CustomWidgets.RightPara.ZividParabox import QParaBox
from PySide2.QtWidgets import QWidget
import datetime
import zivid
from Cfgs.cfg import *

class ConnnectExtraRightBox():

    def init(self):
        global widgets, zivid_camera
        widgets = self.ui
        zivid_camera = self.zivid_camera
        # 添加zivid相机ParaBox
        self.paras_num = 0
        self.INIT_PARA_NUM = 5
        widgets.parasboxs_list = []
        # 打印参数槽函数连接
        widgets.btn_print_para.clicked.connect(lambda: ConnnectExtraRightBox.print_para(self))

        zivid_camera = self.zivid_camera
        for parasboxs_idx in range(self.INIT_PARA_NUM):
            ConnnectExtraRightBox.add_parabox(self)
            # 使得初始化的参数同步到控件
        ConnnectExtraRightBox.init_para(self)

        # 法向量slider
        widgets.horizontalSlider_nx.valueChanged[int].connect(
            lambda: widgets.label_nx.setText(f"平面法向量x: {widgets.horizontalSlider_nx.value()}"))
        widgets.horizontalSlider_ny.valueChanged[int].connect(
            lambda: widgets.label_ny.setText(f"平面法向量y: {widgets.horizontalSlider_ny.value()}"))
        widgets.horizontalSlider_nz.valueChanged[int].connect(
            lambda: widgets.label_nz.setText(f"平面法向量z: {widgets.horizontalSlider_nz.value()}"))
        nx = NX
        ny = NY
        nz = NZ
        widgets.horizontalSlider_nx.setValue(nx)
        widgets.horizontalSlider_ny.setValue(ny)
        widgets.horizontalSlider_nz.setValue(nz)
        widgets.label_nz.setText(f"平面法向量x: {nx}")
        widgets.label_nz.setText(f"平面法向量y: {ny}")
        widgets.label_nz.setText(f"平面法向量z: {nz}")

    def print_para(self):
        """
        打印结构光所有参数组的参数值

        """
        for i in range(self.paras_num):
            print(f"para:Acquisition{i}")
            print(f"eps_time:{zivid_camera.settings.acquisitions[i].exposure_time}")
            print(f"f:{zivid_camera.settings.acquisitions[i].aperture}")
            print(f"bright:{zivid_camera.settings.acquisitions[i].brightness}")
            print(f"eps:{zivid_camera.settings.acquisitions[i].gain}")

    def add_parabox(self):
        """
        添加结构光参数box

        """
        parasboxs_idx = len(widgets.parasboxs_list)
        widget2 = QWidget()
        widgets.parasboxs_list.append(QParaBox(widget2))
        widgets.toolBox2.addWidget(f"     采集参数{parasboxs_idx}", widgets.parasboxs_list[parasboxs_idx])
        ConnnectExtraRightBox.setpara_connect(self, parasboxs_idx)  # 单独一个函数连接信号和槽
        # 初值
        zivid_camera.settings.acquisitions.append(zivid.Settings.Acquisition())
        self.paras_num += 1

    def setpara_connect(self, parasboxs_idx):
        """
        设置结构光ParaBox的控件信号槽连接
        把每一个parabox的控件值的变化连接到设置参数槽函数,doubleslider的connect写在parabox_correct.py

        Args:
            parasboxs_idx(int): box索引

        """
        widgets.parasboxs_list[parasboxs_idx].ui.spinBox_eps_time.valueChanged.connect(
            lambda: ConnnectExtraRightBox.setpara_eps_time(self, parasboxs_idx))
        widgets.parasboxs_list[parasboxs_idx].ui.doubleSpinBox_f.valueChanged.connect(
            lambda: ConnnectExtraRightBox.setpara_f(self, parasboxs_idx))
        widgets.parasboxs_list[parasboxs_idx].ui.doubleSpinBox_bright.valueChanged.connect(
            lambda: ConnnectExtraRightBox.setpara_bright(self, parasboxs_idx))
        widgets.parasboxs_list[parasboxs_idx].ui.doubleSpinBox_eps.valueChanged.connect(
            lambda: ConnnectExtraRightBox.setpara_eps(self, parasboxs_idx))

    def setpara_eps_time(self, parasboxs_idx):
        """
        注意：settings_2d只能有一组参数
        这个和下面几个函数都是实现滑块和spinbox变化参数更新
        zivid_camera.settings.acquisitions[parasboxs_idx].exposure_time
        Args:
            parasboxs_idx(int): box索引s
        """

        value = widgets.parasboxs_list[parasboxs_idx].ui.spinBox_eps_time.value()
        zivid_camera.settings.acquisitions[parasboxs_idx].exposure_time = datetime.timedelta(microseconds=value)
        if parasboxs_idx == 0:  # settings_2d只能有一组参数
            zivid_camera.settings_2d.acquisitions[parasboxs_idx].exposure_time = datetime.timedelta(microseconds=value)

    def setpara_f(self, parasboxs_idx):
        value = widgets.parasboxs_list[parasboxs_idx].ui.doubleSpinBox_f.value()
        zivid_camera.settings.acquisitions[parasboxs_idx].aperture = value
        if parasboxs_idx == 0:
            zivid_camera.settings_2d.acquisitions[parasboxs_idx].aperture = value

    def setpara_bright(self, parasboxs_idx):
        value = widgets.parasboxs_list[parasboxs_idx].ui.doubleSpinBox_bright.value()
        zivid_camera.settings.acquisitions[parasboxs_idx].brightness = value
        if parasboxs_idx == 0:
            zivid_camera.settings_2d.acquisitions[parasboxs_idx].brightness = value

    def setpara_eps(self, parasboxs_idx):
        value = widgets.parasboxs_list[parasboxs_idx].ui.doubleSpinBox_eps.value()
        zivid_camera.settings.acquisitions[parasboxs_idx].gain = value
        if parasboxs_idx == 0:
            zivid_camera.settings_2d.acquisitions[parasboxs_idx].gain = value

    def init_para(self):
        """
        初始化结构光相机的ParaBox
        Returns:

        """
        widgets.parasboxs_list[0].ui.spinBox_eps_time.setValue(10333)
        widgets.parasboxs_list[0].ui.doubleSpinBox_eps.setValue(2)
        widgets.parasboxs_list[0].ui.doubleSpinBox_bright.setValue(0.2)
        widgets.parasboxs_list[0].ui.doubleSpinBox_f.setValue(5.72)
        widgets.parasboxs_list[1].ui.spinBox_eps_time.setValue(8333)
        widgets.parasboxs_list[1].ui.doubleSpinBox_eps.setValue(8)
        widgets.parasboxs_list[1].ui.doubleSpinBox_bright.setValue(1.8)
        widgets.parasboxs_list[1].ui.doubleSpinBox_f.setValue(1)
        widgets.parasboxs_list[2].ui.spinBox_eps_time.setValue(8333)
        widgets.parasboxs_list[2].ui.doubleSpinBox_eps.setValue(8)
        widgets.parasboxs_list[2].ui.doubleSpinBox_bright.setValue(1.8)
        widgets.parasboxs_list[2].ui.doubleSpinBox_f.setValue(2)
        widgets.parasboxs_list[3].ui.spinBox_eps_time.setValue(8333)
        widgets.parasboxs_list[3].ui.doubleSpinBox_eps.setValue(8)
        widgets.parasboxs_list[3].ui.doubleSpinBox_bright.setValue(1.8)
        widgets.parasboxs_list[3].ui.doubleSpinBox_f.setValue(3)
        widgets.parasboxs_list[4].ui.spinBox_eps_time.setValue(8333)
        widgets.parasboxs_list[4].ui.doubleSpinBox_eps.setValue(8)
        widgets.parasboxs_list[4].ui.doubleSpinBox_bright.setValue(1.8)
        widgets.parasboxs_list[4].ui.doubleSpinBox_f.setValue(4)
