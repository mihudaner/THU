#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 16:01
# @Author  : mihudan~
# @File    : dropout_reflect.py
# @Description :
# 参数盒子，三个滑块和spinbox的信号连接，以及添加自定义的DoubleSlider


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from .parabox_ui import Ui_Form
from .QDoubleSlider import DoubleSlider
import datetime
import sys


class QParaBox(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 曝光时间滑块
        self.ui.horizontalSlider_eps_time.valueChanged[int].connect(
            lambda: self.update_spinbox_eps_time(self.ui.horizontalSlider_eps_time.value()))
        self.ui.spinBox_eps_time.valueChanged.connect(
            lambda: self.update_slider_eps_time(self.ui.spinBox_eps_time.value()))

        # 创建三个浮点数滑块
        self.ui.dbSlider_f = DoubleSlider(min=140, max=3200)
        self.ui.dbSlider_f.setParent(self)
        self.ui.verticalLayout_2.addWidget(self.ui.dbSlider_f)
        self.ui.dbSlider_f.valueChanged[int].connect(
            lambda: self.update_dbspinbox_f(self.ui.dbSlider_f.value()))
        self.ui.doubleSpinBox_f.valueChanged.connect(
            lambda: self.update_dbslider_f(self.ui.doubleSpinBox_f.value()))

        self.ui.dbSlider_bright = DoubleSlider(min=0, max=100)
        self.ui.dbSlider_bright.setParent(self)
        self.ui.verticalLayout_3.addWidget(self.ui.dbSlider_bright)
        self.ui.dbSlider_bright.valueChanged[int].connect(
            lambda: self.update_dbspinbox_bright(self.ui.dbSlider_bright.value()))
        self.ui.doubleSpinBox_bright.valueChanged.connect(
            lambda: self.update_dbslider_bright(self.ui.doubleSpinBox_bright.value()))

        self.ui.dbSlider_eps = DoubleSlider(min=100, max=1600)
        self.ui.dbSlider_eps.setParent(self)
        self.ui.verticalLayout_4.addWidget(self.ui.dbSlider_eps)
        self.ui.dbSlider_eps.valueChanged[int].connect(
            lambda: self.update_dbspinbox_eps(self.ui.dbSlider_eps.value()))
        self.ui.doubleSpinBox_eps.valueChanged.connect(  # 之前用的editingFinished
            lambda: self.update_dbslider_eps(self.ui.doubleSpinBox_eps.value()))

    """
    /*    三个滑块的槽函数  */
    """

    def update_spinbox_eps_time(self, value):
        return

    def update_slider_eps_time(self, value):
        return

    def update_dbspinbox_f(self, value):
        value = float(value) / 100
        self.ui.doubleSpinBox_f.setValue(value)
        return

    def update_dbslider_f(self, value):
        # spinbox_value uses float/ doubles type
        # '*100' is used to convert it into integer as QSlider
        # only register integer type
        value = int(value * 100)
        self.ui.dbSlider_f.setValue(value)
        return

    def update_dbspinbox_bright(self, value):
        value = float(value) / 100
        self.ui.doubleSpinBox_bright.setValue(value)
        return

    def update_dbslider_bright(self, value):
        # spinbox_value uses float/ doubles type
        # '*100' is used to convert it into integer as QSlider
        # only register integer type
        value = int(value * 100)
        self.ui.dbSlider_bright.setValue(value)
        return

    def update_dbspinbox_eps(self, value):
        value = float(value) / 100
        self.ui.doubleSpinBox_eps.setValue(value)
        return

    def update_dbslider_eps(self, value):
        # spinbox_value uses float/ doubles type
        # '*100' is used to convert it into integer as QSlider
        # only register integer type
        value = int(value * 100)
        self.ui.dbSlider_eps.setValue(value)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QParaBox()
    window.show()
    sys.exit(app.exec_())
