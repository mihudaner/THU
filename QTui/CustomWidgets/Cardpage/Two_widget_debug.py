# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 13:11
# @Author  : mihudan~
# @File    : DAM8888_dll
# @Description :
import time

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
from QTui.CustomWidgets.Cardpage.QplotWidget import RealTimePlotWidget
from QTui.CustomWidgets.Cardpage import DIOwidget, AIOwidget
import card.DAM8888_dll as dll
import sys
import threading
import numpy as np

DEBUG = True
global PlotBuffer
PlotBuffer = np.zeros((8, 500))
global DIOWindow_widgts
global AIOWindow_widgts
ai = [0, 500, 10000, 2000, 5000, 8888, 7777, 2222]


class DIDOINThread(threading.Thread):
    def __init__(self, DIDO_updatetime):
        threading.Thread.__init__(self)
        self.threadStop = False
        self.DIDO_updatetime = DIDO_updatetime

    def do_run(self):
        global DIOWindow_widgts
        while not self.threadStop:
            time.sleep(self.DIDO_updatetime * 0.001)
            DIOWindow_widgts.read_DI_state()


class AIINThread(threading.Thread):
    def __init__(self, AI_updatetime):
        threading.Thread.__init__(self)
        self.threadStop = False
        self.AI_updatetime = AI_updatetime

    def do_run(self):
        global DIOWindow_widgts
        while not self.threadStop:
            time.sleep(self.AI_updatetime * 0.001)
            # 索引从 0 开始
            for widgetid in range(1, 7):
                combox_cannel = getattr(AIOWindow_widgts.widgets, f"comboBox_plotcannel_{widgetid}")
                waveview = getattr(AIOWindow_widgts.widgets, f"waveview_{widgetid}")
                AOshow_channel = combox_cannel.currentIndex() % 8
                DIOWindow_widgts.read_AI_state()
                waveview.update_data(PlotBuffer[AOshow_channel], AOshow_channel)

    # 老采集卡的保存csv的代码
    # def write_oneline(self, time_stamp_str, DI_state, AD_buffer, checkcomboBox):
    #     global Card_widgts
    #     for i in range(16):
    #         if not checkcomboBox.model().item(i).checkState():
    #             AD_buffer[i][:] = np.ones(len(AD_buffer[0]), dtype=int) * -1
    #     for i in range(0, len(AD_buffer[0]), 4):
    #         mul = int(len(DI_state[0]) / len(AD_buffer[0]))
    #         self.writer.writerow(
    #             [time_stamp_str[11:], DI_state[0][i * mul], DI_state[1][i * mul], DI_state[2][i * mul], DI_state[3][i * mul],
    #              DI_state[4][i * mul], DI_state[5][i * mul], DI_state[6][i * mul], DI_state[7][i * mul],
    #              AD_buffer[0][i], AD_buffer[1][i], AD_buffer[2][i], AD_buffer[3][i], AD_buffer[4][i], AD_buffer[5][i], AD_buffer[6][i], AD_buffer[7][i],
    #              AD_buffer[8][i], AD_buffer[9][i], AD_buffer[10][i], AD_buffer[11][i], AD_buffer[12][i], AD_buffer[13][i], AD_buffer[14][i], AD_buffer[15][i]])
    #         # self.writer.writerow(["wk", 1.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    # def close(self):
    #     self.f.close()


class DIOWidget(QWidget):

    def __init__(self):
        super().__init__()
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

            if not DEBUG:
                self.IP = self.widgets.lineEdit_IP.text()
                self.port = self.widgets.spinBox_port.value()
                if not self.connected:
                    dll.s.connect((self.IP, self.port))
                    self.connected = True

            self.tar1 = DIDOINThread(self.widgets.spinBox_DIDO_updatetime.value())
            t1 = threading.Thread(target=self.tar1.do_run, name='in_thread_DIDO')
            t1.start()
            self.tar2 = AIINThread(self.widgets.spinBox_AI_updatetime.value())
            t2 = threading.Thread(target=self.tar2.do_run, name='in_thread_AI')
            t2.start()
        else:
            self.tar1.threadStop = True
            self.tar2.threadStop = True

    def change_DO(self, channel):
        DO = getattr(self.widgets, f"DO{channel}")
        if DO.isChecked():
            dll.SetOnRelay(channel)
            # self.widgets.textBrowser.append(f"DO{channel} open!")
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
        if DEBUG:
            rev = 7
        else:
            rev = dll.ReadDI()
            rev = int(rev, 16)
        for i in range(8):  # 因为 "fe" 表示16个电平，所以有8位
            radio_btn = getattr(self.widgets, f"DI{i}")
            if (rev >> i) & 1:
                radio_btn.setChecked(True)
            else:
                radio_btn.setChecked(False)

    def read_AI_state(self):
        global debug_cnt
        global PlotBuffer
        global ai
        if DEBUG:
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


def boot_windows():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        # 创建并显示第一个窗口
    window1 = DIOWidget()
    window1.show()

    # 创建并显示第二个窗口
    window2 = DIOWidget()
    window2.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    boot_windows()
