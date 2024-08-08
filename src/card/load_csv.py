#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017年12月23日
@author: Irony
@site: https://pyqt.site , https://github.com/PyQt5
@email: 892768447@qq.com
@file: ToolTip
@description: 是一个QChartView结合了一个自定义写出的悬停提示控件
# 把鼠标位置所在点转换为对应的xy值
        x = self._chart.mapToValue(event.pos()).x()
"""
import sys
import time
import numpy as np
import pandas as pd

try:
    from PyQt5.QtChart import QChartView, QChart, QLineSeries
    from PyQt5.QtCore import Qt, QRectF, QPoint, QPointF
    from PyQt5.QtGui import QPainter, QCursor
    from PyQt5.QtWidgets import QApplication, QGraphicsProxyWidget, QLabel, \
        QWidget, QHBoxLayout, QVBoxLayout, QToolTip, QGraphicsLineItem, QPushButton
except ImportError:
    from PySide2.QtCore import Qt, QRectF, QPoint, QPointF
    from PySide2.QtGui import QPainter, QCursor
    from PySide2.QtWidgets import *
    from PySide2.QtCharts import QtCharts

    QChartView = QtCharts.QChartView
    QChart = QtCharts.QChart
    QLineSeries = QtCharts.QLineSeries

"""
class CircleWidget(QGraphicsProxyWidget):

    def __init__(self, color, *args, **kwargs):
        super(CircleWidget, self).__init__(*args, **kwargs)
        label = QLabel()
        label.setMinimumSize(12, 12)
        label.setMaximumSize(12, 12)
        label.setStyleSheet(
            "border:1px solid green;border-radius:6px;background: %s;" % color)
        self.setWidget(label)


class TextWidget(QGraphicsProxyWidget):

    def __init__(self, text, *args, **kwargs):
        super(TextWidget, self).__init__(*args, **kwargs)
        self.setWidget(QLabel(text, styleSheet="color:white;"))


class GraphicsWidget(QGraphicsWidget):

    def __init__(self, *args, **kwargs):
        super(GraphicsWidget, self).__init__(*args, **kwargs)
#         self.setFlags(self.ItemClipsChildrenToShape)
        self.setZValue(999)
        layout = QGraphicsGridLayout(self)
        for row in range(6):
            layout.addItem(CircleWidget("red"), row, 0)
            layout.addItem(TextWidget("red"), row, 1)
        self.hide()

    def show(self, pos):
        self.setGeometry(pos.x(), pos.y(), self.size().width(),
                         self.size().height())
        super(GraphicsWidget, self).show()
"""


class ToolTipItem(QWidget):

    def __init__(self, color, text, parent=None):
        super(ToolTipItem, self).__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        clabel = QLabel(self)
        clabel.setMinimumSize(12, 12)
        clabel.setMaximumSize(12, 12)
        clabel.setStyleSheet("border-radius:6px;background: rgba(%s,%s,%s,%s);" % (
            color.red(), color.green(), color.blue(), color.alpha()))
        layout.addWidget(clabel)
        self.textLabel = QLabel(text, self, styleSheet="color:white;")
        layout.addWidget(self.textLabel)

    def setText(self, text):
        self.textLabel.setText(text)


class ToolTipWidget(QWidget):
    Cache = {}

    def __init__(self, *args, **kwargs):
        super(ToolTipWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "ToolTipWidget{background: rgba(50,50,50,70);}")
        layout = QVBoxLayout(self)
        self.titleLabel = QLabel(self, styleSheet="color:white;")
        layout.addWidget(self.titleLabel)

    def updateUi(self, title, points):
        self.titleLabel.setText(title)
        for serie, point in points:
            if serie not in self.Cache:
                item = ToolTipItem(
                    serie.color(),
                    (serie.name() or "-") + ":" + str(point.y()), self)
                self.layout().addWidget(item)
                self.Cache[serie] = item
            else:
                self.Cache[serie].setText(
                    (serie.name() or "-") + ":" + str(point.y()))


class GraphicsProxyWidget(QGraphicsProxyWidget):

    def __init__(self, *args, **kwargs):
        super(GraphicsProxyWidget, self).__init__(*args, **kwargs)
        self.setZValue(999)
        self.tipWidget = ToolTipWidget()
        self.setWidget(self.tipWidget)
        self.hide()

    def show(self, title, points, pos):
        self.setGeometry(QRectF(pos, self.size()))
        self.tipWidget.updateUi(title, points)
        super(GraphicsProxyWidget, self).show()


class ChartView(QChartView):

    def __init__(self, dataTable, *args, **kwargs):
        super(ChartView, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.initChart(dataTable)

        self.toolTipWidget = GraphicsProxyWidget(self._chart)

        # line
        self.lineItem = QGraphicsLineItem(self._chart)
        self.lineItem.setZValue(998)
        self.lineItem.hide()
        self.init_shape_para()

    def init_shape_para(self):
        # 一些固定计算，减少mouseMoveEvent中的计算量
        # 获取x和y轴的最小最大值
        axisX, axisY = self._chart.axisX(), self._chart.axisY()
        self.min_x, self.max_x = axisX.min(), axisX.max()
        self.min_y, self.max_y = axisY.min(), axisY.max()
        # 坐标系中左上角顶点
        self.point_top = self._chart.mapToPosition(
            QPointF(self.min_x, self.max_y))
        # 坐标原点坐标
        self.point_bottom = self._chart.mapToPosition(
            QPointF(self.min_x, self.min_y))
        self.step_x = (self.max_x - self.min_x) / (axisX.tickCount() - 1)

    #         self.step_y = (self.max_y - self.min_y) / (axisY.tickCount() - 1)
    def mouseMoveEvent(self, event):
        super(ChartView, self).mouseMoveEvent(event)
        # 把鼠标位置所在点转换为对应的xy值
        x = self._chart.mapToValue(event.pos()).x()
        y = self._chart.mapToValue(event.pos()).y()
        index = round((x - self.min_x) / self.step_x)
        pos_x = self._chart.mapToPosition(
            QPointF(index * self.step_x + self.min_x, self.min_y))
        #         print(x, pos_x, index, index * self.step_x + self.min_x)
        # 得到在坐标系中的所有series的类型和点
        points = [(serie, serie.at(index))
                  for serie in self._chart.series() if
                  self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y]
        if points:
            self.point_top = self._chart.mapToPosition(
                QPointF(self.min_x, self.max_y))
            # 坐标原点坐标
            self.point_bottom = self._chart.mapToPosition(
                QPointF(self.min_x, self.min_y))
            # 永远在轴上的黑线条
            self.lineItem.setLine(pos_x.x(), self.point_top.y(),
                                  pos_x.x(), self.point_bottom.y())
            self.lineItem.show()
            self.toolTipWidget.show("", points, event.pos() + QPoint(20, 20))
        else:
            self.toolTipWidget.hide()
            self.lineItem.hide()

    def onSeriesHoverd(self, point, state):
        if state:
            try:
                name = self.sender().name()
            except:
                name = ""
            QToolTip.showText(QCursor.pos(), "%s\nx: %s\ny: %s" %
                              (name, point.x(), point.y()))

    def initChart(self, dataTable):
        self._chart = QChart(title="Line Chart")
        self._chart.setAcceptHoverEvents(True)

        for i, data_list in enumerate(dataTable):
            series = QLineSeries(self._chart)
            for j, v in enumerate(data_list):
                series.append(j, v)
            series.setName("AD " + str(i + 1))
            series.setPointsVisible(True)  # 显示原点
            series.hovered.connect(self.onSeriesHoverd)
            self._chart.addSeries(series)
        self._chart.createDefaultAxes()  # 创建默认的轴
        self._chart.axisX().setTickCount(len(dataTable[0]))  # x轴设置7个刻度
        self._chart.axisY().setTickCount(10)  # y轴设置7个刻度
        self._chart.axisY().setRange(0, 3)  # 设置y轴范围
        self.setChart(self._chart)


class QChart_Csv(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dataTable = [
            [120, 132, 101, 134, 90, 230, 210],
            [220, 182, 191, 234, 290, 330, 310],
            [150, 232, 201, 154, 190, 330, 410],
            [320, 332, 301, 334, 390, 330, 320],
            [820, 932, 901, 934, 1290, 1330, 1320]
        ]

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.chartview = ChartView(self.dataTable)
        self.layout.addWidget(self.chartview)

        self.button = QPushButton('导入CSV数据')
        self.button.setToolTip("从第10列开始加载AD数据")
        self.layout.addWidget(self.button)

        self.button.clicked.connect(lambda: self.change_cvs())

    def load_csv_data(self):
        # fileName = QFileDialog.getOpenFileName(self, "Open Image", ".")
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(
            self, 'Open CSV File', './data/csv', 'CSV Files (*.csv);;All Files (*)', options=options)
        if file_name.endswith('.csv'):
            data = pd.read_csv(file_name, header=None)  # 如果CSV文件没有表头，可以使用header=None
            # 现在data是一个Pandas的DataFrame，包含了CSV文件中的所有数据
            print(data)
            return data.iloc[1:, 9:].values.astype(float).T
        else:
            QMessageBox.critical(self, 'Error', 'Selected file is not a CSV file.')
            return -1

    def change_cvs(self):
        # dataTable = [
        #     [120, 12, 101, 14, 90, 230, 210],
        #     [220, 182, 191, 24, 290, 330, 310],
        #     [150, 232, 201, 14, 190, 330, 410],
        #     [320, 32, 301, 334, 30, 330, 320],
        #     [820, 932, 901, 934, 190, 330, 1320]
        # ]
        data = self.load_csv_data()
        if len(data) == 1:
            return
        self.layout.removeWidget(self.chartview)
        self.chartview.deleteLater()
        self.chartview = ChartView(data)
        self.layout.insertWidget(0, self.chartview)
        self.update()  # 重新绘制界面


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""QToolTip {
    border: none;
    padding: 5px;
    color: white;
    background: rgb(50,50,50);
    opacity: 100;
}""")

    windows = QChart_Csv()
    windows.show()

    sys.exit(app.exec_())
