#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/25 22:54
# @Author  : mihudan~
# @File    : QplotWidget
# @Description : 

import sys
import numpy as np
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore


class RealTimePlotWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.data8 = np.zeros((8, 500))  # 初始化数据数组，这里假设波形数组长度为100
        self.data = np.zeros(500)  # 初始化数据数组，这里假设波形数组长度为100
        self.timer_interval = 33  # 定时器间隔，单位为毫秒，可以根据需要调整

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(self.timer_interval)
        self.current_ad_port = None

    def update_data(self, new_data):
        self.data8 = new_data  # 更新波形数据

    def update_plot(self):
        self.update()  # 调用QWidget的update()方法，触发绘图事件

    def paintEvent(self, event):

        for i in range(8):
            self.current_ad_port = i
            self.data = self.data8[i]

            V_MAX = 10
            TOP_MARGIN = 30

            painter = QtGui.QPainter(self)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)

            # 绘制波形
            pen = QtGui.QPen(QtGui.QColor(98, 114, 165))  # 设置画笔颜色为蓝色
            pen.setWidth(2)  # 设置画笔宽度
            painter.setPen(pen)

            width = self.width() - 30
            height = self.height() - TOP_MARGIN
            step = width / len(self.data)

            painter.drawLine(30, 0, 30, self.height())  # 画一条左侧刻度尺线
            h_step = height / V_MAX
            for i in range(0, V_MAX + 1, 1):
                if i % 2 == 0:
                    painter.drawText(QtCore.QPoint(2, TOP_MARGIN + height - i * h_step), str(i))
                    painter.drawLine(0, TOP_MARGIN + i * h_step, 30, TOP_MARGIN + i * h_step)
                else:
                    painter.drawLine(30, TOP_MARGIN + i * h_step, 15, TOP_MARGIN + i * h_step)

            for i in range(len(self.data) - 1):
                x1 = i * step + 30
                y1 = (V_MAX - self.data[i]) * height / V_MAX + TOP_MARGIN
                x2 = (i + 1) * step + + 30
                y2 = (V_MAX - self.data[i + 1]) * height / V_MAX + TOP_MARGIN
                painter.drawLine(x1, y1, x2, y2)

            if self.current_ad_port == 4:
                painter.drawText(QtCore.QPoint(width / 2, 20), str((self.data[0] - 2.5) * 14)[:5] + "mm")
            else:
                painter.drawText(QtCore.QPoint(width / 2, 20), str(self.data[0])[:5] + "V")
            painter.end()


# 这里模拟数据更新过程，实际情况中你可以根据具体应用，实时获取数据并更新波形数组


if __name__ == "__main__":
    class MyMainWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()

            # 设置主窗口标题
            self.setWindowTitle("Tab Widget Example")

            # 创建一个 QTabWidget
            tab_widget = QtWidgets.QTabWidget(self)

            # 创建第一个 QWidget
            widget1 = QtWidgets.QWidget()

            # 创建第二个 QWidget
            widget2 = QtWidgets.QWidget()

            # 将 QWidget 添加到 QTabWidget 的标签页中
            tab_widget.addTab(widget1, "Tab 1")
            tab_widget.addTab(widget2, "Tab 2")

            layout1 = QtWidgets.QVBoxLayout()
            widget1.setLayout(layout1)
            layout2 = QtWidgets.QVBoxLayout()
            widget2.setLayout(layout2)

            self.R1 = RealTimePlotWidget()
            layout1.addWidget(self.R1)
            self.R2 = RealTimePlotWidget()
            layout1.addWidget(self.R2)
            self.setCentralWidget(tab_widget)

            self.timer1 = QtCore.QTimer()
            self.timer1.timeout.connect(lambda: self.update_data_R1())
            self.timer1.start(1000)  # 数据更新间隔，单位为毫秒

            self.timer2 = QtCore.QTimer()
            self.timer2.timeout.connect(lambda: self.update_data_R2())
            self.timer2.start(1000)  # 数据更新间隔，单位为毫秒

        def update_data_R1(self):
            new_data = np.random.rand(100)  # 生成随机数据，假设波形数组长度为100
            self.R1.update_data(new_data, 0)

        def update_data_R2(self):
            new_data = np.random.rand(100)  # 生成随机数据，假设波形数组长度为100
            self.R2.update_data(self.R1.data, 0)


    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.setGeometry(100, 100, 800, 400)

    window.show()

    sys.exit(app.exec_())
