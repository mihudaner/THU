#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/27 15:05
# @Author  : mihudan~
# @File    : AC_dll.py
# @Description : 采集卡动态连接调用
# @ c_uint
# nuitka --mingw64 --standalone --show-progress --show-memory --enable-plugin=pyside2 --include-qt-plugins=sensible,styles  --nofollow-imports --output-dir=out  AC_dll.py
# D:\\soft\\Anaconda\\envs\\py37\\Scripts\\pyside2-uic -o  E:\Work\THU\code\THU_Project_暑假前\src\card\AC_widget.py E:\Work\THU\code\THU_Project_暑假前\src\card\AC_widget.ui

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from AC_widget import Ui_Form
from QplotWidget import RealTimePlotWidget
from matplot_embed import QplotWidget
from QCheckCombox import CheckableComboBox

from ctypes import *
import time
import sys
import threading
import numpy as np
import csv
import pandas as pd

DEBUG = False

global dll
# dll = WinDLL("./DLL_LIB_H/MPS-010602_x64.dll")  # 调用了这个dll
dll = WinDLL("./DLL_LIB_H/MPS-010602_x64.dll")  # 调用了这个dll
if not dll:
    print("load MPS-010602_x64.dll default!")
else:
    print(dll)

global timeshift
timeshift = 0
global PlotBuffer
PlotBuffer = np.zeros(5000)
global past_DI_state
past_DI_state = np.array([-1, -1, -1, -1, -1, -1, -1, -1], dtype=np.int)
global Card_widgts


def get_date_time():
    # 获取当前时间戳，并打印输出
    timestamp = time.time()
    timeArray = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d-%H:%M:%S", timeArray) + ":" + str(timestamp).split(".")[1]
    return otherStyleTime


class Card_datas():
    def __init__(self, set_time):
        # 模拟采集的数据
        # new_float_data = [0.17, 0.18, ..., 0.32]  # 新的16个float数据
        # new_int_data = [17, 18, ..., 32]  # 新的16个int数据
        # 保存数据到CSV文件
        header = ['time_stamp', 'DIO1', 'DIO2', 'DIO3', 'DIO4', 'DIO5', 'DIO6', 'DIO7', 'DIO8',
                  'AD1', 'AD2', 'AD3', 'AD4', 'AD5', 'AD6', 'AD7', 'AD8', 'AD9', 'AD10', 'AD11', 'AD12', 'AD13', 'AD14', 'AD15', 'AD16']
        filename = f'./data/csv/{set_time}.csv'.replace(":", "-")
        # filename = f'{set_time}.csv'.replace(":", "-")
        self.f = open(filename, 'a', newline='')
        self.writer = csv.writer(self.f)
        # writer.writerow(new_float_data + new_int_data)
        self.writer.writerow(header)

    def write_oneline(self, time_stamp_str, DI_state, AD_buffer, checkcomboBox):
        global Card_widgts
        for i in range(16):
            if not checkcomboBox.model().item(i).checkState():
                AD_buffer[i][:] = np.ones(len(AD_buffer[0]), dtype=int) * -1
        for i in range(0, len(AD_buffer[0]), 4):
            mul = int(len(DI_state[0]) / len(AD_buffer[0]))
            self.writer.writerow(
                [time_stamp_str[11:], DI_state[0][i * mul], DI_state[1][i * mul], DI_state[2][i * mul], DI_state[3][i * mul],
                 DI_state[4][i * mul], DI_state[5][i * mul], DI_state[6][i * mul], DI_state[7][i * mul],
                 AD_buffer[0][i], AD_buffer[1][i], AD_buffer[2][i], AD_buffer[3][i], AD_buffer[4][i], AD_buffer[5][i], AD_buffer[6][i], AD_buffer[7][i],
                 AD_buffer[8][i], AD_buffer[9][i], AD_buffer[10][i], AD_buffer[11][i], AD_buffer[12][i], AD_buffer[13][i], AD_buffer[14][i], AD_buffer[15][i]])
            # self.writer.writerow(["wk", 1.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def close(self):
        self.f.close()


def checkDI_setoperate(DI_state):
    """
    np.all(DI_state[i] == 1):
            DI_state[i] = 1
    DI口的触发沿是前一次采集为低，后一次采集全为高，才会up_flag

    Parameters
    ----------
    DI_state: numpy
        for i in range(8):
            DI_flag_list.append(DI % 2)
            DI = DI / 2
    Returns
    ------
    """
    up_flag = [False, False, False, False, False, False, False, False]
    down_flag = [False, False, False, False, False, False, False, False]

    global past_DI_state
    for i in range(8):
        if np.all(DI_state[i] == 1):
            DI_state[i] = 1
            if past_DI_state[i] == 0:
                up_flag[i] = True
                print(f"port {i} up_flag!")
        elif np.all(DI_state[i] == 0):
            DI_state[i] = 0
            if past_DI_state[i] == 1:
                down_flag[i] = True
                print(f"port {i} down_flag!")
        else:
            DI_state[i] = past_DI_state[i]
    past_DI_state = DI_state
    print(past_DI_state)
    return up_flag, down_flag


def generate_triangular_wave(samples_per_output, frequency, sample_rate, gain, wave_type, AD_PORT):
    """
    生成不同类型的波形
    Parameters
    ----------
    samples_per_output
    frequency
    sample_rate
    gain
    wave_type
    AD_PORT

    Returns
    -------

    """
    global timeshift
    global Card_widgts

    # 计算每个样点的时间间隔
    time_interval = 1 / sample_rate

    # 生成时间序列
    time = np.arange(samples_per_output) * time_interval + timeshift
    timeshift += samples_per_output * time_interval
    # 计算相位随时间的变化
    phase_shift = (2 * np.pi * frequency * time) % (2 * np.pi)

    # 计算波信号
    if wave_type == 0:
        wave = np.sin(phase_shift) / 2 + 0.5
    elif wave_type == 1:
        wave = np.where(np.sin(phase_shift) >= 0, 1, 0)
    elif wave_type == 2:
        wave = (np.arcsin(np.sin(phase_shift)) / np.pi) + 0.5
    elif wave_type == 3:
        DC = getattr(Card_widgts, f"doubleSpinBox_DCout{AD_PORT}").value()
        wave = np.array([DC] * samples_per_output)

    # 防止最大值大于2.5
    wave = wave * gain
    wave = np.where(wave > 2.5, 2.5, wave)

    return wave


# def update_label_ad(datas, idx):
#     """
#     刷新label_ad要显示的信息值的映射
#     Parameters
#     ----------
#     datas
#     Mainwindows
#
#     Returns
#     -------
#
#     """
#     if idx + 1 == 4:
#         Card_widgts.label_ad.setText(f"distance：{(datas[0] - 2.5) * 14}mm")
#     else:
#         Card_widgts.label_ad.setText(f"AD{idx + 1} out(V)：{datas[0]}"[:15])


class DATAINThread(QThread):
    """

    """
    data_in_sign = Signal(list, list)

    def __init__(self, Mainwindows):
        super().__init__()
        self.Mainwindows = Mainwindows
        self.is_running = False
        self.card_datas = None
        self.data_inbuffer = None

    def run(self):
        # 在这里实现视频流读取和图像刷新逻辑
        # 将每帧图像转换为QImage，并发送信号通知更新
        self.is_running = True
        global PlotBuffer
        c_num = int(2 ** (self.Mainwindows.widgets.comboBox_AD_channe_number.currentIndex() + 1))  # 通道个数
        buffer_num = int(self.Mainwindows.SampleNumber / (c_num / 2))  # 每个通道数据的个数
        self.data_inbuffer = [[0.0] * buffer_num] * 16  # 创建一共16个数据的通道buffer

        while self.is_running:
            t1 = time.time()
            if DEBUG:
                time.sleep(0.010)

            VoltageIn1, VoltageIn2, DI_buffer = DataIn(self.Mainwindows.SampleNumber, self.Mainwindows.DeviceNumber)  # 读到的数据是ctype类型
            if DEBUG:
                VoltageIn1, VoltageIn2 = np.arange(self.Mainwindows.SampleNumber), np.arange(self.Mainwindows.SampleNumber) + 100

            # 分解收到的ctype为每一个通道的数据np数据
            for i in range(int(c_num / 2)):
                self.data_inbuffer[i] = VoltageIn1[i::int(c_num / 2)]
                self.data_inbuffer[i + 8] = VoltageIn2[i::int(c_num / 2)]

            # -------模拟量
            # 显示选中的模拟通道数据
            # idx = int(self.Mainwindows.widgets.buttonGroup.checkedButton().objectName()[-1])
            # + (10 if len(self.Mainwindows.widgets.buttonGroup.checkedButton().text()) == 4 else 0)
            idx = self.Mainwindows.widgets.comboBox_plotcannel.currentIndex()
            if self.Mainwindows.select_in != idx:
                PlotBuffer = np.zeros(5000)
            self.Mainwindows.select_in = idx

            # update_label_ad(data_inbuffer[idx], self.Mainwindows.widgets.comboBox_plotcannel.currentIndex())
            # PlotBuffer = np.append(PlotBuffer, self.data_inbuffer[self.Mainwindows.select_in])[len(self.data_inbuffer[self.Mainwindows.select_in]):]
            # self.Mainwindows.widgets.waveview.update_data(PlotBuffer, self.Mainwindows.widgets.comboBox_plotcannel.currentIndex())

            # -------数字量
            DI = []
            DI_state = []
            for i in range(self.Mainwindows.SampleNumber):
                DI.append(DI_buffer[i])  # 迭代次数多
            DI = np.array(DI, dtype=np.int)
            for i in range(8):
                DI_state.append(DI % 2)
                DI = DI // 2

            # 保存cvs
            if self.card_datas is not None:
                try:
                    self.card_datas.write_oneline(get_date_time(), DI_state, self.data_inbuffer, self.Mainwindows.widgets.checkableComboBox)
                except ValueError as e:
                    print(e)

            # DI = np.frombuffer(DI_buffer, dtype=np.int64)

            # print(f"DI[0] = {DI[0]}")  # 类型未知
            # print(f"Data in t tiem:{time.time() - t1}")

            # DI_buff检测触发沿 ,operator_flag应该是一个字典
            up_flag, down_flag = checkDI_setoperate(DI_state)
            if any(up_flag) or any(down_flag):
                self.data_in_sign.emit(up_flag, down_flag)

    def stop(self):
        self.is_running = False



class DATAPLOTThread(QThread):

    def __init__(self, Mainwindows):
        super().__init__()
        self.Mainwindows = Mainwindows
        self.is_running = False

    def run(self):
        self.is_running = True
        while self.is_running:
            global PlotBuffer
            global past_DI_state
            check_state = past_DI_state
            t1 = time.time()
            self.Mainwindows.widgets.waveview.plot(PlotBuffer)
            for i in range(8):
                # time.sleep(0.1)
                if check_state[i] == 1:
                    getattr(self.Mainwindows.widgets, f"DI{i}").setChecked(True)
                    continue
                if check_state[i] == 0:
                    getattr(self.Mainwindows.widgets, f"DI{i}").setChecked(False)
                    continue
            print(f"wave palot tiem:{time.time() - t1}")

    def stop(self):
        self.is_running = False


class QWidget_Card(QWidget):

    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        # self.ui = QUiLoader().load('windows.ui')
        self.SampleNumber = None
        self.AD_channe_number = None

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.widgets = self.ui
        global Card_widgts
        Card_widgts = self.widgets
        self.widgets
        self.show()

        # 悬浮显示提醒
        self.widgets.DO0.setToolTip("采集卡D1，<b>送粉电压确认输出</b>")
        self.widgets.DO1.setToolTip("采集卡D2，<b>激光器电压确认输出</b>")
        self.widgets.DO2.setToolTip("采集卡D3，<b>NULL</b>")
        self.widgets.DO3.setToolTip("采集卡D4，<b>NULL</b>")
        self.widgets.DO4.setToolTip("采集卡D5，<b>NULL</b>")
        self.widgets.DO5.setToolTip("采集卡D6，<b>开始停止取流的ACK信号，发送给kuka</b>")
        self.widgets.DO6.setToolTip("采集卡D7，<b>该信号需要kuka给出，拉高开始取流，拉低停止取流！开始停止取流的ACK信号是D6端</b>")
        self.widgets.DO7.setToolTip("采集卡D8，<b>NULL</b>")
        self.widgets.doubleSpinBox_DCout1.setToolTip("激光器模拟量")
        self.widgets.doubleSpinBox_DCout1.setToolTip("送分电压模拟量")

        self.widgets.pushButton_startin.clicked.connect(lambda: self.startin())
        self.widgets.pushButton_startout.clicked.connect(lambda: self.startout())

        self.widgets.waveview = QplotWidget(QWidget(self))
        # pyqt绘图控件
        # self.widgets.waveview = RealTimePlotWidget()

        self.widgets.Layout_wave = QVBoxLayout(self.widgets.groupBox_waveview)
        self.widgets.Layout_wave.addWidget(self.widgets.waveview)

        # AD口选通CheckableComboBox
        self.widgets.checkableComboBox = CheckableComboBox()
        self.widgets.horizontalLayout_ADcheckcombox.addWidget(self.widgets.checkableComboBox)
        self.widgets.checkableComboBox.addItems(["AD1", "AD2", "AD3", "AD4", "AD5", "AD6", "AD7", "AD8",
                                                 "AD9", "AD10", "AD11", "AD12", "AD13", "AD14", "AD15", "AD16"])
        self.widgets.checkableComboBox.setToolTip("勾选则该AD口从buff读取，否则直接置0！")

        self.is_startin = False
        self.is_startout = False

        self.select_in = None  # 选择的输入idx


        # 输入输出线程
        self.t_out = threading.Thread(target=self.Data_out, args=(), name='Data_out')
        self.t_out.daemon = True
        self.t_out.start()
        self.t_in = DATAINThread(self)
        self.t_plot = DATAPLOTThread(self)

        # 数字量输入边沿显示的触发更改checkbottons
        self.t_in.data_in_sign.connect(self.update_checkbottons)

        # DIO口1，2设置拉高1s后自动拉低
        self.widgets.DO0.toggled.connect(self.set_radiobutton_1s)
        self.D0_timer = QTimer()
        self.D0_timer.timeout.connect(lambda: self.widgets.DO0.setChecked(False))
        self.widgets.DO1.toggled.connect(self.set_radiobutton_1s)
        self.D1_timer = QTimer()
        self.D1_timer.timeout.connect(lambda: self.widgets.DO1.setChecked(False))

    def set_radiobutton_1s(self, checked):
        if checked:
            print("D0 set 1s")
            self.D0_timer.start(1000)  # Start timer for 1 second

    def update_checkbottons(self, up_flag, down_flag):
        print(up_flag, down_flag)
        for i in range(len(up_flag)):
            if up_flag[i]:
                getattr(self.widgets, f"DI{i}").setChecked(True)
                continue
            if down_flag[i]:
                getattr(self.widgets, f"DI{i}").setChecked(False)
                continue

    def setpara(self):
        sample_rate = self.widgets.spinBox_clock.value()
        self.AD_channe_number = (self.widgets.comboBox_AD_channe_number.currentIndex() + 1) * 2  # AD端口是2，4，8，16
        ADGPA_channels = [self.widgets.spinBox_gain.value()] * 16  # 16个模拟端口的增益大小
        DIOmodal = self.widgets.comboBox_DIOmodal.currentIndex()  # 数字段输入还是输出模式
        PWM1 = self.widgets.spinBox_PWM1.value()
        PWM2 = self.widgets.spinBox_PWM2.value()
        ComparaporEnable = 0  # 比较器禁止
        ExtTringger = 0  # 使用内部时钟
        self.DeviceNumber = self.widgets.spinBox_device_id.value()  # 一般默认0
        self.SampleNumber = self.widgets.spinBox_SampleNumber.value()  # 一次采样个数

        setpara(sample_rate, self.AD_channe_number, ADGPA_channels, DIOmodal, PWM1, PWM2, ComparaporEnable, ExtTringger, self.DeviceNumber)
        self.widgets.textBrowser.setText("sample_rate:" + f"{sample_rate}" + "\nAD_channe_number:" + f"{self.AD_channe_number}" + "\nADGPA_channels:" + f"{ADGPA_channels}" +
                                         "\nDIOmodal:" + f"{DIOmodal}" + "\nPWM1:" + f"{PWM1}" + "\nPWM2:" + f"{PWM2}" + "\nComparaporEnable:" + f"{ComparaporEnable}" + "\nExtTringger:" +
                                         f"{ExtTringger}" + "\nDeviceNumber:" + f"{self.DeviceNumber}" + "\nSampleNumber:" + f"{self.SampleNumber}")

    def startin(self):
        """
        开始读取数据，修改读线程的falg
        :return:
        """
        if not self.is_startin:
            self.setpara()
            self.is_startin = True
            self.widgets.pushButton_startin.setText("停止输入")
            self.widgets.pushButton_startin.setStyleSheet("background-color: red;")
            self.t_in.start()
            self.t_plot.start()

        else:
            self.is_startin = False
            self.widgets.pushButton_startin.setText("开始输入")
            self.widgets.pushButton_startin.setStyleSheet("background-color: transparent;")
            self.t_in.stop()
            self.t_plot.stop()

    def startout(self):
        """
        开始输出数据，输出读线程的falg
        :return:
        """
        if not self.is_startout:
            self.setpara()
            self.is_startout = True
            self.widgets.pushButton_startout.setText("停止输出")
            self.widgets.pushButton_startout.setStyleSheet("background-color: red;")

        else:
            # 清除模拟和数字电平状态
            VoltageOut1 = np.zeros(self.SampleNumber)
            VoltageOut2 = np.zeros(self.SampleNumber)
            VoltageOut3 = np.zeros(self.SampleNumber)
            VoltageOut4 = np.zeros(self.SampleNumber)
            DO = []
            value = 0x00
            for i in range(self.SampleNumber):
                DO.append(value)

            DataOut(VoltageOut1.tolist(), VoltageOut2.tolist(), VoltageOut3.tolist(), VoltageOut4.tolist(), DO, self.SampleNumber, self.DeviceNumber)

            self.widgets.pushButton_startout.setText("开始输出")
            self.widgets.pushButton_startout.setStyleSheet("background-color: transparent;")
            self.is_startout = False
            return

    def Data_out(self):
        """
        输出线程函数，并且绘制
        :return:
        """
        while True:
            t1 = time.time()
            if self.is_startout:

                VoltageOut1 = np.zeros(self.SampleNumber)
                VoltageOut2 = np.zeros(self.SampleNumber)
                VoltageOut3 = np.zeros(self.SampleNumber)
                VoltageOut4 = np.zeros(self.SampleNumber)
                if self.widgets.radioButton_1.isChecked():
                    wave_type = self.widgets.comboBox_out1.currentIndex()
                    VoltageOut1 = generate_triangular_wave(self.SampleNumber, self.widgets.spinBox_fps1.value(), self.widgets.spinBox_clock.value(),
                                                           self.widgets.spinBox_gain.value(), wave_type, 1)
                if self.widgets.radioButton_2.isChecked():
                    wave_type = self.widgets.comboBox_out2.currentIndex()
                    VoltageOut2 = generate_triangular_wave(self.SampleNumber, self.widgets.spinBox_fps2.value(), self.widgets.spinBox_clock.value(),
                                                           self.widgets.spinBox_gain.value(), wave_type, 2)
                if self.widgets.radioButton_3.isChecked():
                    wave_type = self.widgets.comboBox_out3.currentIndex()
                    VoltageOut3 = generate_triangular_wave(self.SampleNumber, self.widgets.spinBox_fps3.value(), self.widgets.spinBox_clock.value(),
                                                           self.widgets.spinBox_gain.value(), wave_type, 3)
                if self.widgets.radioButton_4.isChecked():
                    # wave_type = self.widgets.comboBox_out4.currentIndex()
                    # VoltageOut4 = generate_triangular_wave(self.SampleNumber, self.widgets.spinBox_fps4.value(), self.widgets.spinBox_clock.value(),
                    #                                        self.widgets.spinBox_gain.value(), wave_type)
                    # VoltageOut4 = np.array([float()] * self.SampleNumber)
                    wave_type = self.widgets.comboBox_out4.currentIndex()
                    VoltageOut4 = generate_triangular_wave(self.SampleNumber, self.widgets.spinBox_fps3.value(), self.widgets.spinBox_clock.value(),
                                                           self.widgets.spinBox_gain.value(), wave_type, 4)
                # 输出的数字量初始化
                DO = []
                value = 0x00
                if self.widgets.DO0.isChecked(): value += 1
                if self.widgets.DO1.isChecked(): value += 2
                if self.widgets.DO2.isChecked(): value += 4
                if self.widgets.DO3.isChecked(): value += 8
                if self.widgets.DO4.isChecked(): value += 16
                if self.widgets.DO5.isChecked(): value += 32
                if self.widgets.DO6.isChecked(): value += 64
                if self.widgets.DO7.isChecked(): value += 128

                for i in range(self.SampleNumber):
                    DO.append(value)
                DataOut(VoltageOut1.tolist(), VoltageOut2.tolist(), VoltageOut3.tolist(), VoltageOut4.tolist(), DO, self.SampleNumber, self.DeviceNumber)

                # # 测试输出才开
                global PlotBuffer
                PlotBuffer = np.append(PlotBuffer, VoltageOut1)[len(VoltageOut1.tolist()):]
            else:
                time.sleep(0.5)
            # print(f"Card OUTTIME:{time.time() - t1}")


def setpara(sample_rate, AD_channe_number, ADGPA_channels, DIOmodal, PWM1, PWM2, ComparaporEnable, ExtTringger, DeviceNumber):
    '''

    :param sample_rate: 采样率、刷新率等工作时钟频率。此参数为内部时钟频率设定。参数取值范围为 5000-80000
    :param AD_channe_number: 模拟输入通道数。ADChannelNumber = 2， AD1 与 AD9 分别被配置为两路模拟信号输入，并且为同步采集，其余 ADx 口无效
    :param ADGPA_channels: 模拟输入增益设置。ADPGAofChannels 为一维 16 元素数组，数组元素依次代表模拟输入 1-16 通道的增益系数
    :param DIOmodal: 数字输入/输出端口模式设置
    :param PWM1: PWM1 输出占空比设置
    :param PWM2: PWM2 输出占空比设置
    :param ComparaporEnable: 比较器使能。ComparatorEnable = 0，比较器结果输出端被禁止，比较器无效；
    :param ExtTringger:外部时钟触发使能。ExtTrigger = 0，使用内部时钟触发采集和输出；ExtTrigger 为其他值时使用外部时钟触发。一般情况下建议使用内部时钟
    :param DeviceNumber: 操作所针对的设备号
    :return:
    '''
    dllFunc = dll.SetPara
    dllFunc.restype = c_int
    ret = dllFunc(c_int(sample_rate), c_int(AD_channe_number), (c_int * 16)(*ADGPA_channels),
                  c_int(DIOmodal), c_short(PWM1), c_short(PWM2), c_int(ComparaporEnable), c_int(ExtTringger), c_int(DeviceNumber))
    if ret is None:
        print("find no card func！")
    elif ret == 0:
        print("Please check card  hardware!")


def DataOut(VoltageOut1, VoltageOut2, VoltageOut3, VoltageOut4, DO, SampleNumber, DeviceNumber):
    """

    :param VoltageOut1: 模拟输出通道 DA1 将输出的数据
    :param VoltageOut2: Out1类推
    :param VoltageOut3: Out1类推
    :param VoltageOut4: Out1类推
    :param DO: DO 为一个一维数组，其每个元素为一个 unsigned char 型数据，8 个数据，分别代表同一时刻输出的 8路数字端口电平状态。
    :param SampleNumber: 采样点的个数
    :param DeviceNumber: 操作所针对的设备号
    :return:
    """
    dllFunc = dll.DataOut
    dllFunc.restype = c_int
    ret = dllFunc((c_float * SampleNumber)(*VoltageOut1), (c_float * SampleNumber)(*VoltageOut2), (c_float * SampleNumber)(*VoltageOut3),
                  (c_float * SampleNumber)(*VoltageOut4), (c_ubyte * SampleNumber)(*DO), SampleNumber, DeviceNumber)
    if ret is None:
        print("find no card func！")
    elif ret == 0:
        print("Please check card  hardware!")


def DataIn(SampleNumber, DeviceNumber):
    """

    :param VoltageIn1: 第一组模拟信号输入（AD1-AD8）的数据,VoltageIn1所指向的数组大小应大于 SampleNumber 的大小。
    :param VoltageIn2: 第二组模拟信号输入（AD9-AD16）的数据
    :param DI: 数字信号采集得到的数据。DI 为一个一维数组，其每个元素为 8 位 unsigned char 型数据，8 个数据位分别代表同一时刻采样得到的 8 路数字端口电平状态
    无论数字输入/输出端口工作在输入模式还是输出模式，都可以获得当前 Dx 端口的电平状态
    :param SampleNumber: 采样点的个数
    :param DeviceNumber: 操作所针对的设备号
    :return:
    """
    FLOATARRAY = c_float * SampleNumber
    databuffer1 = FLOATARRAY()
    databuffer2 = FLOATARRAY()

    CHARARRAY = c_ubyte * SampleNumber
    DI = CHARARRAY()

    # for i in range(0, SampleNumber): databuffer1[i] = 0
    # for i in range(0, SampleNumber): databuffer2[i] = 0
    dllFunc = dll.DataIn
    dllFunc.restype = c_int
    ret = dllFunc(databuffer1, databuffer2, DI, SampleNumber, DeviceNumber)
    if ret is None:
        print("find no card func！")
    elif ret == 0:
        print("Please check card  hardware!")

    # VoltageIn1 = []
    # VoltageIn2 = []
    # for i in range(SampleNumber): VoltageIn1.append(databuffer1[i])
    # for i in range(SampleNumber): VoltageIn2.append(databuffer2[i])
    VoltageIn1 = np.frombuffer(databuffer1, dtype=np.float32)
    VoltageIn2 = np.frombuffer(databuffer2, dtype=np.float32)

    # print("VoltageIn1:", VoltageIn1, "\n")
    # print("VoltageIn2:", VoltageIn2, "\n")\
    return VoltageIn1, VoltageIn2, DI


def Counter(DeviceNumber):
    """
    :param Count1:
    :param Count2:
    :param DeviceNumber:
    :return:
    """
    INT32ARRAY = c_int
    Count1 = INT32ARRAY()
    Count2 = INT32ARRAY()

    dllFunc = dll.Counter
    dllFunc.restype = c_int
    ret = dllFunc(byref(Count1), byref(Count2), DeviceNumber)
    if ret is None:
        print("find no card func！")
    elif ret == 0:
        print("Please check card  hardware!")
    print("Count1:", Count1.value, "Count2:", Count2.value)


def test():
    """
    第一组模拟信号输入（AD1-AD8）的数据
    第二组模拟信号输入（AD9-AD16）的数据
    模拟输出通道DA1-4
    数字输入/输出通道 D1-D8
    :return:
    """
    sample_rate = 5000  # 采用频率
    AD_channe_number = 2  # AD输入通道数
    ADGPA_channels = [1] * 16  # 模拟输入增益设置
    DIOmodal = 0  # 数字输入/输出端口模式设置 DIOModal = 0，D1-D8 全部为输入模式
    PWM1 = 0  # PWM输出占空比
    PWM2 = 0  # PWM输出占空比
    ComparaporEnable = 0  # 比较器禁止
    ExtTringger = 0  # 使用内部时钟
    DeviceNumber = 0

    SampleNumber = 128

    VoltageOut1 = [0.0] * SampleNumber
    VoltageOut2 = [0.0] * SampleNumber
    VoltageOut3 = [0.0] * SampleNumber
    VoltageOut4 = [0.0] * SampleNumber
    DO = (c_ubyte * SampleNumber)()

    for i in range(SampleNumber):
        VoltageOut1[i] = i / SampleNumber
        VoltageOut2[i] = i / SampleNumber
        if i < SampleNumber / 2:
            VoltageOut3[i] = (i / SampleNumber) * 4
        else:
            VoltageOut3[i] = ((SampleNumber - i) / SampleNumber) * 4
        VoltageOut4[i] = 1
    print("VoltageOut1:", VoltageOut1, "\n")
    print("VoltageOut2:", VoltageOut2, "\n")
    print("VoltageOut3:", VoltageOut3, "\n")
    print("VoltageOut4:", VoltageOut4, "\n")

    setpara(sample_rate, AD_channe_number, ADGPA_channels, DIOmodal, PWM1, PWM2, ComparaporEnable, ExtTringger, DeviceNumber)
    for i in range(10000):
        a = time.time()
        DataIn(SampleNumber, DeviceNumber)
        Counter(DeviceNumber)
        print("times:", time.time() - a)


def boot_windows():
    # test()
    # time.sleep(1000)
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = QWidget_Card()
    # window.t_in.card_datas = Card_datas(time.time())
    sys.exit(app.exec_())


if __name__ == "__main__":
    for i in range(0, 128, 20):
        print(i)
    boot_windows()
    # c = Card_datas(0)
    # c.write_oneline(0, 0, 0)
    # c.close()
    # # 加载CSV文件
    # data = pd.read_csv('0.csv', header=None)  # 如果CSV文件没有表头，可以使用header=None
    # # 现在data是一个Pandas的DataFrame，包含了CSV文件中的所有数据
    # print(data)
    print(get_date_time())
