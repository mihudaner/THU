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
from QTui.CustomWidgets.Cardpage.DAM8888_widget import Ui_Form
import DAM8888_dll as dll
import sys
import threading
import numpy as np

DEBUG = True
debug_cnt = 0x00
global PlotBuffer
PlotBuffer = np.zeros((8, 500))
global Card_widgts


class DIDOINThread(threading.Thread):
    def __init__(self, DIDO_updatetime):
        threading.Thread.__init__(self)
        self.threadStop = False
        self.DIDO_updatetime = DIDO_updatetime

    def do_run(self):
        global Card_widgts
        while not self.threadStop:
            time.sleep(self.DIDO_updatetime * 0.001)
            Card_widgts.read_DI_state()


class AIINThread(threading.Thread):
    def __init__(self, AI_updatetime):
        threading.Thread.__init__(self)
        self.threadStop = False
        self.AI_updatetime = AI_updatetime

    def do_run(self):
        global Card_widgts
        while not self.threadStop:
            time.sleep(self.AI_updatetime * 0.001)
            # 索引从 0 开始
            AOshow_channel = Card_widgts.widgets.comboBox_plotcannel.currentIndex()
            Card_widgts.read_AI_state()
            print(f"PlotBuffer[{AOshow_channel}]:{PlotBuffer[AOshow_channel]}")
            Card_widgts.widgets.waveview.update_data(PlotBuffer[AOshow_channel], AOshow_channel)


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
        Card_widgts = self
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
        # self.widgets.doubleSpinBox_DCout1.setToolTip("激光器模拟量")
        # self.widgets.doubleSpinBox_DCout1.setToolTip("送分电压模拟量")

        # self.widgets.pushButton_startin
        # self.widgets.pushButton_startout

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

        # 绘图控件
        self.widgets.waveview = RealTimePlotWidget()
        self.widgets.Layout_wave = QVBoxLayout(self.widgets.groupBox_waveview)
        self.widgets.Layout_wave.addWidget(self.widgets.waveview)

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

        # for i in range(8):
        #     channel = 1 + i
        #     slider = getattr(self.widgets, f"Slider{channel}")
        #     spinBox = getattr(self.widgets, f"spinBox_AO{channel}")
        #     slider.valueChanged[int].connect(lambda: spinBox.setValue(slider.value()))
        #     spinBox.editingFinished.connect(lambda: slider.setValue(spinBox.value()))

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
                # self.widgets.textBrowser.append(f"IP:{self.IP}")
                # self.widgets.textBrowser.append(f"port:{self.port}")
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

        # self.in_thread_DIDO.stop()
        #     self.in_thread_DIDO.quit()
        #     # self.widgets.textBrowser.append("等待in_thread_DIDO线程退出")

        # self.in_thread_AI.stop()
        # self.in_thread_AI.quit()
        # # self.widgets.textBrowser.append("等待in_thread_DIDO线程退出")

        # 开始不间断采集

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
        if DEBUG:
            rev = hex(0xFE041000000000000000000000000000000000712C + debug_cnt)[2:]
            debug_cnt += 0x100000
            if debug_cnt > 0x10000000: debug_cnt = 0x0
        else:
            rev = dll.ReadAI()
        # self.widgets.textBrowser.append(f"查询AI状态{rev}")  # 如果位为1，表示高电平
        bytes = int(rev[4:6], 16)
        global PlotBuffer
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


def boot_windows():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        # 创建并显示第一个窗口
    window1 = QWidget_Card()
    window1.show()

    # 创建并显示第二个窗口
    window2 = QWidget_Card()
    window2.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    boot_windows()
