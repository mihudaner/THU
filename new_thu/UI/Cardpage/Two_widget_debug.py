# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 13:11
# @Author  : mihudan~
# @File    : DAM8888_dll
# @Description :
import re
import time
import csv
import datetime
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/27 15:05
# @Author  : mihudan~
# @File    : AC_dll.py
# @Description : 采集卡动态连接调用
# @ c_uint
# nuitka --mingw64 --standalone --show-progress --show-memory --enable-plugin=pyside2 --include-qt-plugins=sensible,styles  --nofollow-imports --output-dir=out  AC_dll.py
# D:\\soft\\Anaconda\\envs\\py37\\Scripts\\pyside2-uic -o  .\DAM8888_widget.py .\DAM8888_widget.ui
# pyside2-rcc ./icon/icon.qrc -o icon_rc.py
from PySide2.QtWidgets import *
from PySide2.QtGui import QPixmap, QImage
from PySide2.QtCore import Qt
from .QplotWidget import RealTimePlotWidget
from UI.Cardpage import DIOwidget
from .AIO_CCD_Table import Ui_Form as AIO_CCD_Table
from UI.Cardpage import DAM8888_dll as dll
import sys
import threading
import cv2
import numpy as np
from src.CCDControler import CCD_camera

global PlotBuffer
PlotBuffer = np.zeros((8, 500))
Checked_AI = np.zeros(8)
global DIOWindow_widgts
global AIOWindow_widgts
global DO
from .Signal import g_signals

DO = 0
ai = [0, 500, 10000, 2000, 5000, 8888, 7777, 2222]


def extract_last_hex_string(deviceList):
    """
    提取字符串中最后一个以 '0x' 开头的十六进制字符串及其后面的部分。

    Args:
        input_string (str): 输入的字符串。

    Returns:
        str: 提取出的十六进制字符串及其后面的部分。如果未找到，返回 None。
    """
    res_list = []
    for input_string in deviceList:
        # 使用正则表达式匹配以 '0x' 开头的十六进制字符串
        # 由于要获取最后一个，使用负向查找
        hex_pattern = r'0x[0-9a-fA-F]+.*$'
        match = re.search(hex_pattern, input_string)
        if match:
            res_list.append(match.group())
        else:
            continue

    return res_list
def show_warning(title, message):
    # 创建并显示警告框
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)  # 设置警告图标
    msg.setText(message)  # 设置消息内容
    msg.setWindowTitle(title)  # 设置窗口标题
    msg.exec_()  # 显示消息框并等待用户交互


class DIDOINThread(threading.Thread):
    def __init__(self, DIDO_updatetime, now_select_csv_save_apppath):
        threading.Thread.__init__(self)
        self.threadStop = False
        self.DIDO_updatetime = DIDO_updatetime
        self.now_select_csv_save_apppath = now_select_csv_save_apppath
        self.record_state = 0

    def do_run(self):
        global DIOWindow_widgts
        while not self.threadStop:
            if self.record_state == 1:
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y%m%d_%H%M%S")
                header = ['time_stamp', 'DIO1', 'DIO2', 'DIO3', 'DIO4', 'DIO5', 'DIO6', 'DIO7', 'DIO8']
                filename = f'{self.now_select_csv_save_apppath}/{timestamp}_DI.csv'
                # filename = f'{set_time}.csv'.replace(":", "-")
                self.f = open(filename, 'a', newline='')
                self.writer = csv.writer(self.f)
                # writer.writerow(new_float_data + new_int_data)
                self.writer.writerow(header)
                self.record_state = 2

            time.sleep(self.DIDO_updatetime * 0.001)
            DI8s = DIOWindow_widgts.read_DI_state()
            if self.record_state == 2:
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y%m%d_%H%M%S")
                self.writer.writerow(
                    [timestamp, DI8s[0], DI8s[1], DI8s[2], DI8s[3],
                     DI8s[4], DI8s[5], DI8s[6], DI8s[7]])

            if self.record_state == 3:
                self.f.close()
                self.record_state = 4


class AIINThread(threading.Thread):
    def __init__(self, AI_updatetime, now_select_csv_save_apppath):
        threading.Thread.__init__(self)
        self.threadStop = False
        self.AI_updatetime = AI_updatetime
        self.now_select_csv_save_apppath = now_select_csv_save_apppath
        self.record_state = 0

    def do_run(self):
        global DIOWindow_widgts
        global PlotBuffer
        while not self.threadStop:
            if self.record_state == 1:
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y%m%d_%H%M%S")
                header = ['time_stamp', 'AD1', 'AD2', 'AD3', 'AD4', 'AD5', 'AD6', 'AD7', 'AD8', 'AD9', 'AD10', 'AD11', 'AD12', 'AD13', 'AD14', 'AD15', 'AD16']
                filename = f'{self.now_select_csv_save_apppath}/{timestamp}_AI.csv'
                # filename = f'{set_time}.csv'.replace(":", "-")
                self.f = open(filename, 'a', newline='')
                self.writer = csv.writer(self.f)
                # writer.writerow(new_float_data + new_int_data)
                self.writer.writerow(header)
                self.record_state = 2

            time.sleep(self.AI_updatetime * 0.001)
            # 索引从 0 开始
            waveview = getattr(AIOWindow_widgts.widgets, f"waveview_{1}")
            DIOWindow_widgts.read_AI_state()
            for i in range(8):
                ckbox = getattr(AIOWindow_widgts.widgets, f"checkBox_{i + 1}")
                if ckbox.isChecked():
                    Checked_AI[i] = 1
                else:
                    Checked_AI[i] = 0
            waveview.update_data(PlotBuffer, Checked_AI)
            now = datetime.datetime.now()
            if self.record_state == 2:
                timestamp = now.strftime("%Y%m%d_%H%M%S")
                self.writer.writerow(
                    [timestamp, PlotBuffer[0][-1], PlotBuffer[1][-1], PlotBuffer[2][-1], PlotBuffer[3][-1], PlotBuffer[4][-1], PlotBuffer[5][-1], PlotBuffer[6][-1], PlotBuffer[7][-1], ])
            if self.record_state == 3:
                self.f.close()
                self.record_state = 4


class DIOWidget(QWidget):

    def __init__(self,DEBUG):
        super().__init__()
        self.DEBUG = DEBUG
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        # self.ui = QUiLoader().load('windows.ui')
        self.SampleNumber = None
        self.AD_channe_number = None

        self.ui = DIOwidget.Ui_Form()
        self.ui.setupUi(self)
        self.widgets = self.ui
        global DIOWindow_widgts
        DIOWindow_widgts = self
        self.show()

        self.widgets.DO0.clicked.connect(lambda: self.change_DO(0))
        self.widgets.DO1.clicked.connect(lambda: self.change_DO(1))
        self.widgets.DO2.clicked.connect(lambda: self.change_DO(2))
        self.widgets.DO3.clicked.connect(lambda: self.change_DO(3))
        self.widgets.DO4.clicked.connect(lambda: self.change_DO(4))
        self.widgets.DO5.clicked.connect(lambda: self.change_DO(5))
        self.widgets.DO6.clicked.connect(lambda: self.change_DO(6))
        self.widgets.DO7.clicked.connect(lambda: self.change_DO(7))
        self.IP = None
        self.port = None

        self.widgets.checkBox_openport.stateChanged.connect(self.open_port)
        self.widgets.btn_readDO.clicked.connect(self.read_DO_state)
        self.widgets.btn_readDI.clicked.connect(self.read_DI_state)
        self.widgets.btn_readAI.clicked.connect(self.read_AI_state)

        self.is_startin = False
        self.connected = False
        self.connect_AO_slider_spinbox()
        self.widgets.btn_setAO.clicked.connect(lambda: self.set_AI())

        self.now_select_csv_save_apppath = '.'

    def connect_AO_slider_spinbox(self):
        self.widgets.Slider1.valueChanged[int].connect(
            lambda: self.widgets.spinBox_AO1.setValue(self.widgets.Slider1.value()))
        self.widgets.spinBox_AO1.editingFinished.connect(
            lambda: self.widgets.Slider1.setValue(self.widgets.spinBox_AO1.value()))

        self.widgets.Slider2.valueChanged[int].connect(
            lambda: self.widgets.spinBox_AO2.setValue(self.widgets.Slider2.value()))
        self.widgets.spinBox_AO2.editingFinished.connect(
            lambda: self.widgets.Slider2.setValue(self.widgets.spinBox_AO2.value()))

        self.widgets.Slider3.valueChanged[int].connect(
            lambda: self.widgets.spinBox_AO3.setValue(self.widgets.Slider3.value()))
        self.widgets.spinBox_AO3.editingFinished.connect(
            lambda: self.widgets.Slider3.setValue(self.widgets.spinBox_AO3.value()))

        self.widgets.Slider4.valueChanged[int].connect(
            lambda: self.widgets.spinBox_AO4.setValue(self.widgets.Slider4.value()))
        self.widgets.spinBox_AO4.editingFinished.connect(
            lambda: self.widgets.Slider4.setValue(self.widgets.spinBox_AO4.value()))

        self.widgets.Slider5.valueChanged[int].connect(
            lambda: self.widgets.spinBox_AO5.setValue(self.widgets.Slider5.value()))
        self.widgets.spinBox_AO5.editingFinished.connect(
            lambda: self.widgets.Slider5.setValue(self.widgets.spinBox_AO5.value()))

        self.widgets.Slider6.valueChanged[int].connect(
            lambda: self.widgets.spinBox_AO6.setValue(self.widgets.Slider6.value()))
        self.widgets.spinBox_AO6.editingFinished.connect(
            lambda: self.widgets.Slider6.setValue(self.widgets.spinBox_AO6.value()))

        self.widgets.Slider7.valueChanged[int].connect(
            lambda: self.widgets.spinBox_AO7.setValue(self.widgets.Slider7.value()))
        self.widgets.spinBox_AO7.editingFinished.connect(
            lambda: self.widgets.Slider7.setValue(self.widgets.spinBox_AO7.value()))

        self.widgets.Slider8.valueChanged[int].connect(
            lambda: self.widgets.spinBox_AO8.setValue(self.widgets.Slider8.value()))
        self.widgets.spinBox_AO8.editingFinished.connect(
            lambda: self.widgets.Slider8.setValue(self.widgets.spinBox_AO8.value()))

    def startin(self):
        """
        开始读取数据，修改读线程的falg
        :return:
        """
        if not self.is_startin:
            self.is_startin = True
            self.t_in.start()
        else:
            self.is_startin = False
            self.t_in.stop()

    def open_port(self):
        if self.widgets.checkBox_openport.isChecked():

            if not self.DEBUG:
                self.IP = self.widgets.lineEdit_IP.text()
                self.port = self.widgets.spinBox_port.value()
                if not self.connected:
                    dll.s.connect((self.IP, self.port))
                    self.connected = True

            self.tar1 = DIDOINThread(self.widgets.spinBox_DIDO_updatetime.value(), self.now_select_csv_save_apppath)
            t1 = threading.Thread(target=self.tar1.do_run, name='in_thread_DIDO')
            t1.start()
            self.tar2 = AIINThread(self.widgets.spinBox_AI_updatetime.value(), self.now_select_csv_save_apppath)
            t2 = threading.Thread(target=self.tar2.do_run, name='in_thread_AI')
            t2.start()
        else:
            self.tar1.threadStop = True
            self.tar2.threadStop = True

    def change_DO(self, channel):
        global DO
        DOcheckbtn = getattr(self.widgets, f"DO{channel}")
        if DOcheckbtn.isChecked():
            if self.DEBUG:
                DO = DO | (1 << channel)
            else:
                dll.SetOnRelay(channel)
            # self.widgets.textBrowser.append(f"DO{channel} open!")
        else:
            if self.DEBUG:
                DO = DO & ~(1 << channel)
            else:
                dll.SetOffRelay(channel)
            # self.widgets.textBrowser.append(f"DO{channel} close!")

    def read_DO_state(self):
        """
        查询继电器状态fe 01 01 21 a184
        21
        高位2   L8L7L6L5第二个灯亮就是L6
        低位1   L4L3L2L1第一个灯亮就是L1
        :return:
        """
        rev = dll.ReadRelay()
        # self.widgets.textBrowser.append(f"查询继电器状态{rev}")
        rev = int(rev, 16)
        for i in range(8):  # 因为 "fe" 表示16个电平，所以有8位
            radio_btn = getattr(self.widgets, f"DO{i}")
            if (rev >> i) & 1:
                radio_btn.setChecked(True)
            else:
                radio_btn.setChecked(False)

    def read_DI_state(self):
        """
        查询DI状态
        :return:
        """
        res = [0, 0, 0, 0, 0, 0, 0, 0]
        global DO
        if self.DEBUG:
            rev = DO
        else:
            rev = dll.ReadDI()
            rev = int(rev, 16)
        for i in range(8):  # 因为 "fe" 表示16个电平，所以有8位
            radio_btn = getattr(self.widgets, f"DI{i}")
            if (rev >> i) & 1:
                res[i] = 1
                if not radio_btn.isChecked():
                    radio_btn.setChecked(True)
                    if i is 0:
                        # 发出信号，传递一个字符串参数
                        g_signals.DI1_signal.emit("UP")
                    if i is 1:
                        # 发出信号，传递一个字符串参数
                        g_signals.DI2_signal.emit("UP")

            elif not (rev >> i) & 1 and radio_btn.isChecked():
                radio_btn.setChecked(False)
                if i is 0:
                    # 发出信号，传递一个字符串参数
                    g_signals.DI1_signal.emit("Down")
                if i is 1:
                    # 发出信号，传递一个字符串参数
                    g_signals.DI2_signal.emit("Down")
        return res

    def read_AI_state(self):
        global debug_cnt
        global PlotBuffer
        global ai
        if self.DEBUG:
            # rev = hex(0xFE041000000000000000000000000000000000712C + debug_cnt)[2:]
            # debug_cnt += 0x0011001100110000
            # if debug_cnt > 0x1000000000000000000: debug_cnt = 0x0
            for i in range(8):
                if ai[i] >= 10000:
                    ai[i] = 0
                ai[i] += 10
                PlotBuffer[i] = np.append(PlotBuffer[i], ai[i] / 1000)[1:]
        else:
            rev = dll.ReadAI()
            # self.widgets.textBrowser.append(f"查询AI状态{rev}")  # 如果位为1，表示高电平
            bytes = int(rev[4:6], 16)
            for i in range(int(bytes / 2)):
                l = 6 + i * 4
                r = 6 + i * 4 + 4
                ai = int(rev[l: r], 16)
                PlotBuffer[i] = np.append(PlotBuffer[i], ai / 1000)[1:]

    def set_AI(self):
        values = []
        for channel in range(8):
            slider = getattr(self.widgets, f"Slider{channel + 1}")
            values.append(slider.value())
        dll.SetAO(values)


class AIOWidget(QWidget):

    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        # self.ui = QUiLoader().load('windows.ui')
        self.SampleNumber = None
        self.AD_channe_number = None

        self.ui = AIOwidget.Ui_Form()
        self.ui.setupUi(self)
        self.widgets = self.ui
        global AIOWindow_widgts
        AIOWindow_widgts = self
        self.show()

        # 绘图控件
        self.widgets.waveview_1 = RealTimePlotWidget()
        self.widgets.Layout_wave_1 = QVBoxLayout(self.widgets.groupBox_waveview_1)
        self.widgets.Layout_wave_1.addWidget(self.widgets.waveview_1)

        # 绘图控件
        self.widgets.waveview_2 = RealTimePlotWidget()
        self.widgets.Layout_wave_2 = QVBoxLayout(self.widgets.groupBox_waveview_2)
        self.widgets.Layout_wave_2.addWidget(self.widgets.waveview_2)

        # 绘图控件
        self.widgets.waveview_3 = RealTimePlotWidget()
        self.widgets.Layout_wave_3 = QVBoxLayout(self.widgets.groupBox_waveview_3)
        self.widgets.Layout_wave_3.addWidget(self.widgets.waveview_3)

        # 绘图控件
        self.widgets.waveview_4 = RealTimePlotWidget()
        self.widgets.Layout_wave_4 = QVBoxLayout(self.widgets.groupBox_waveview_4)
        self.widgets.Layout_wave_4.addWidget(self.widgets.waveview_4)

        # 绘图控件
        self.widgets.waveview_5 = RealTimePlotWidget()
        self.widgets.Layout_wave_5 = QVBoxLayout(self.widgets.groupBox_waveview_5)
        self.widgets.Layout_wave_5.addWidget(self.widgets.waveview_5)

        # 绘图控件
        self.widgets.waveview_6 = RealTimePlotWidget()
        self.widgets.Layout_wave_6 = QVBoxLayout(self.widgets.groupBox_waveview_6)
        self.widgets.Layout_wave_6.addWidget(self.widgets.waveview_6)


class AIOWidget_ShowOne(QWidget):

    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        # self.ui = QUiLoader().load('windows.ui')
        self.SampleNumber = None
        self.AD_channe_number = None

        self.ui = AIOwidget.Ui_Form()
        self.ui.setupUi(self)
        self.widgets = self.ui
        global AIOWindow_widgts
        AIOWindow_widgts = self
        self.show()

        # 绘图控件
        self.widgets.waveview_1 = RealTimePlotWidget()
        self.widgets.Layout_wave_1 = QVBoxLayout(self.widgets.groupBox_waveview_1)
        self.widgets.Layout_wave_1.addWidget(self.widgets.waveview_1)

        # 绘图控件
        self.widgets.waveview_2 = RealTimePlotWidget()
        self.widgets.Layout_wave_2 = QVBoxLayout(self.widgets.groupBox_waveview_2)
        self.widgets.Layout_wave_2.addWidget(self.widgets.waveview_2)

        # 绘图控件
        self.widgets.waveview_3 = RealTimePlotWidget()
        self.widgets.Layout_wave_3 = QVBoxLayout(self.widgets.groupBox_waveview_3)
        self.widgets.Layout_wave_3.addWidget(self.widgets.waveview_3)

        # 绘图控件
        self.widgets.waveview_4 = RealTimePlotWidget()
        self.widgets.Layout_wave_4 = QVBoxLayout(self.widgets.groupBox_waveview_4)
        self.widgets.Layout_wave_4.addWidget(self.widgets.waveview_4)

        # 绘图控件
        self.widgets.waveview_5 = RealTimePlotWidget()
        self.widgets.Layout_wave_5 = QVBoxLayout(self.widgets.groupBox_waveview_5)
        self.widgets.Layout_wave_5.addWidget(self.widgets.waveview_5)

        # 绘图控件
        self.widgets.waveview_6 = RealTimePlotWidget()
        self.widgets.Layout_wave_6 = QVBoxLayout(self.widgets.groupBox_waveview_6)
        self.widgets.Layout_wave_6.addWidget(self.widgets.waveview_6)


class AIOWidget_ShowOne(QWidget):
    select_idx = 0

    def __init__(self,DEBUG):
        super().__init__()
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        # self.ui = QUiLoader().load('windows.ui')

        self.DEBUG = DEBUG
        self.SampleNumber = None
        self.AD_channe_number = None

        self.ui = AIO_CCD_Table()
        self.ui.setupUi(self)
        self.widgets = self.ui
        global AIOWindow_widgts
        AIOWindow_widgts = self
        self.show()

        # 绘图控件
        self.widgets.waveview_1 = RealTimePlotWidget()
        self.widgets.Layout_wave_1 = QVBoxLayout(self.widgets.groupBox_waveview_1)
        self.widgets.Layout_wave_1.addWidget(self.widgets.waveview_1)

        self.cam = CCD_camera(self.DEBUG)
        self.ui.btn_enum.clicked.connect(self.enum)
        self.ui.checkBox_openccd.clicked.connect(self.change_state)
        self.ui.comboBox_ccd_device.currentIndexChanged.connect(self.change_select)
        self.ui.btn_ccd_capture.clicked.connect(self.capture)
        self.ui.btn_ccd_capture.hide()
        self.ui.btn_setpara.clicked.connect(self.setpara2)

        self.widgets.spinBox_ccd_hoffset.editingFinished.connect(self.setpara)
        self.widgets.spinBox_ccd_woffset.editingFinished.connect(self.setpara)
        self.widgets.Slider_hoffset.valueChanged.connect(self.setpara)
        self.widgets.Slider_woffset.valueChanged.connect(self.setpara)
        self.widgets.spinBox_ccdw.editingFinished.connect(self.setpara)
        self.widgets.spinBox_ccdh.editingFinished.connect(self.setpara)
        self.widgets.Slider_h.valueChanged.connect(self.setpara)
        self.widgets.Slider_w.valueChanged.connect(self.setpara)
        self.setpara()

    def setpara2(self):
        if not self.DEBUG:
            ret = self.cam.setpara(self.ui.spinBox_gain.value(), self.ui.spinBox_exposure.value(), self.select_idx)
            if not ret:
                show_warning("设置失败", "设置失败，请检查设备是否连接。")
                return
        self.capture()

    def setpara(self):
        self.cam.H = self.ui.spinBox_ccdh.value()
        self.cam.W = self.ui.spinBox_ccdw.value()
        self.cam.Hoffset = self.ui.spinBox_ccd_hoffset.value()
        self.cam.Woffset = self.ui.spinBox_ccd_woffset.value()
        if self.cam.img is not None:
            self.updateshow(self.cam.get_img())

    def capture(self, updateshow=True, timedelay=0):
        img = self.cam.capture(self.select_idx)
        if not isinstance(img, np.ndarray):
            show_warning("拍照失败", "拍照失败，请检查设备是否连接。")
            return
        rgb_image = cv2.cvtColor(self.cam.get_img(), cv2.COLOR_BGR2RGB)
        if updateshow: self.updateshow(rgb_image)
        if timedelay > 0:
            time.sleep(timedelay*0.001)
        return img

    def updateshow(self, rgb_image):
        # 将图像转换为 QImage
        height, width, channel = rgb_image.shape
        bytes_per_line = 3 * width
        q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # 计算缩放比例
        label_width = self.ui.label_ccd_img.width()
        label_height = self.ui.label_ccd_img.height()

        # 保持长宽比，缩放 QImage
        scaled_pixmap = QPixmap.fromImage(q_image).scaled(label_width, label_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.label_ccd_img.setPixmap(scaled_pixmap)

    def change_select(self):
        self.select_idx = self.ui.comboBox_ccd_device.currentIndex()
        self.cam.change_select(self.select_idx)
        if self.cam.get_state(self.select_idx):
            self.ui.checkBox_openccd.setChecked(True)
        else:
            self.ui.checkBox_openccd.setChecked(False)

    def change_state(self):
        if self.ui.checkBox_openccd.isChecked():
            ret = self.cam.open(self.select_idx)
            if not ret:
                self.ui.checkBox_openccd.setChecked(False)
                show_warning("打开失败", "打开失败，请检查设备是否连接。")
        else:
            ret = self.cam.close(self.select_idx)
            if not ret:
                self.ui.checkBox_openccd.setChecked(True)
                show_warning("关闭失败", "关闭失败")

    def enum(self):

        deviceList = self.cam.enum()
        self.ui.comboBox_ccd_device.clear()
        self.ui.comboBox_ccd_device.addItems(extract_last_hex_string(deviceList))


def boot_windows():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        # 创建并显示第一个窗口
    window1 = DIOWidget()
    window1.show()

    # 创建并显示第二个窗口
    window2 = AIOWidget_ShowOne()
    window2.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    boot_windows()
