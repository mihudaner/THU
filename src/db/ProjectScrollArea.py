#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/26 16:29
# @Author  : mihudan~
# @File    : project.py
# @Description :
from PySide2.QtWidgets import *  # 不止这一个外部库，其它的库我在需要用到时单独引入
from PySide2.QtCore import Signal

from .project_ui import Ui_Form
import os
import datetime
import json


# D:\\soft\\Anaconda\\envs\\py37\\Scripts\\pyside2-uic -o  project_ui.py project.ui


class ProjectCard(QWidget):
    card_clicked = Signal(object)  # 定义一个信号

    def __init__(self, pdata=None):
        super(ProjectCard, self).__init__()
        self.initUI()  # 初始化窗口
        self.resize(400, 1000)

        if pdata is not None:
            self.load_data(pdata)

    def load_data(self, pdata):
        self.ui.lineEdit.setText(pdata.pinfo.time)
        index = self.ui.comboBox.findText(pdata.pinfo.PowderMaterial)
        # 如果找到匹配的索引，设置当前索引
        if index != -1:  # 如果 findText 没有找到匹配项，会返回 -1
            self.ui.comboBox.setCurrentIndex(index)

        index = self.ui.comboBox_2.findText(pdata.pinfo.SubstrateMaterial)
        # 如果找到匹配的索引，设置当前索引
        if index != -1:  # 如果 findText 没有找到匹配项，会返回 -1
            self.ui.comboBox_2.setCurrentIndex(index)

        index = self.ui.comboBox_3.findText(pdata.pinfo.Type)
        # 如果找到匹配的索引，设置当前索引
        if index != -1:  # 如果 findText 没有找到匹配项，会返回 -1
            self.ui.comboBox_3.setCurrentIndex(index)

        self.ui.doubleSpinBox.setValue(pdata.ppara.LaserPower)
        self.ui.doubleSpinBox_2.setValue(pdata.ppara.CladdingSpeed)
        self.ui.doubleSpinBox_3.setValue(pdata.ppara.PowderFeedRate)
        self.ui.doubleSpinBox_4.setValue(pdata.ppara.SpotDiameter)
        self.ui.doubleSpinBox_5.setValue(pdata.ppara.OffsetDistance)
        self.ui.doubleSpinBox_6.setValue(pdata.ppara.TrackSpacing)
        self.ui.doubleSpinBox_7.setValue(pdata.ppara.LayerSpacing)

    def initUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.widgets = self.ui

    def mousePressEvent(self, event):
        self.card_clicked.emit(self)  # 发射信号，传递当前的card对象
        super(ProjectCard, self).mousePressEvent(event)

    def theme(self, file):
        str = open(file, 'r').read()
        self.ui.widget.setStyleSheet(str)


class ProjectINFO:
    def __init__(self, widgets=None):
        self.time = None
        self.PowderMaterial = None
        self.SubstrateMaterial = None
        self.Type = None

        if widgets is not None:
            self.set_info_from_widgets(widgets)

    def set_info_from_widgets(self, widgets):
        """从UI控件中提取信息并设置属性"""
        self.time = widgets.ui.lineEdit.text()
        self.PowderMaterial = widgets.ui.comboBox.currentText()
        self.SubstrateMaterial = widgets.ui.comboBox_2.currentText()
        self.Type = widgets.ui.comboBox_3.currentText()


class ProcessParameters:
    def __init__(self, widgets):
        self.PowderMaterial = None
        self.SubstrateMaterial = None
        self.Type = None
        self.LaserPower = None
        self.CladdingSpeed = None
        self.PowderFeedRate = None
        self.SpotDiameter = None
        self.OffsetDistance = None
        self.TrackSpacing = None
        self.LayerSpacing = None
        if widgets is not None:
            self.set_info_from_widgets(widgets)

    def set_info_from_widgets(self, widgets):
        self.PowderMaterial = widgets.ui.comboBox.currentText()
        self.SubstrateMaterial = widgets.ui.comboBox_2.currentText()
        self.Type = widgets.ui.comboBox_3.currentText()
        self.LaserPower = widgets.ui.doubleSpinBox.value()
        self.CladdingSpeed = widgets.ui.doubleSpinBox_2.value()
        self.PowderFeedRate = widgets.ui.doubleSpinBox_3.value()
        self.SpotDiameter = widgets.ui.doubleSpinBox_4.value()
        self.OffsetDistance = widgets.ui.doubleSpinBox_5.value()
        self.TrackSpacing = widgets.ui.doubleSpinBox_6.value()
        self.LayerSpacing = widgets.ui.doubleSpinBox_7.value()


class ProjectData:
    def __init__(self, widgets=None):
        self.pinfo = ProjectINFO(widgets)
        self.ppara = ProcessParameters(widgets)


def save_pdata_txt(pdata, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write("粉末材料：" + pdata.pinfo.PowderMaterial + '\n')
        f.write("基体材料：" + pdata.pinfo.SubstrateMaterial + '\n')
        f.write("类型：" + pdata.pinfo.Type + '\n')
        f.write("激光功率：" + str(pdata.ppara.LaserPower) + '\n')
        f.write("堆焊速度：" + str(pdata.ppara.CladdingSpeed) + '\n')
        f.write("粉末喷射速率：" + str(pdata.ppara.PowderFeedRate) + '\n')
        f.write("斑点直径：" + str(pdata.ppara.SpotDiameter) + '\n')
        f.write("偏移距离：" + str(pdata.ppara.OffsetDistance) + '\n')
        f.write("轨迹间距：" + str(pdata.ppara.TrackSpacing) + '\n')
        f.write("层间距：" + str(pdata.ppara.LayerSpacing) + '\n')
        f.write('\n')


def save_pdata_json(pdata, filename):
    data = {
        "时间": pdata.pinfo.time,
        "粉末材料": pdata.pinfo.PowderMaterial,
        "基体材料": pdata.pinfo.SubstrateMaterial,
        "类型": pdata.pinfo.Type,
        "激光功率": pdata.ppara.LaserPower,
        "堆焊速度": pdata.ppara.CladdingSpeed,
        "粉末喷射速率": pdata.ppara.PowderFeedRate,
        "斑点直径": pdata.ppara.SpotDiameter,
        "偏移距离": pdata.ppara.OffsetDistance,
        "轨迹间距": pdata.ppara.TrackSpacing,
        "层间距": pdata.ppara.LayerSpacing
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_pdata_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 构建 pdata 对象
    pdata = ProjectData()
    pdata.pinfo.time = data["时间"]
    pdata.pinfo.PowderMaterial = data["粉末材料"]
    pdata.pinfo.SubstrateMaterial = data["基体材料"]
    pdata.pinfo.Type = data["类型"]
    pdata.ppara.LaserPower = data["激光功率"]
    pdata.ppara.CladdingSpeed = data["堆焊速度"]
    pdata.ppara.PowderFeedRate = data["粉末喷射速率"]
    pdata.ppara.SpotDiameter = data["斑点直径"]
    pdata.ppara.OffsetDistance = data["偏移距离"]
    pdata.ppara.TrackSpacing = data["轨迹间距"]
    pdata.ppara.LayerSpacing = data["层间距"]

    return pdata


class ProjectManager():
    def __init__(self, parentwidget):
        self.pdatas = dict()
        self.rootpath = "./ProjectData/"
        self.parentwidget = parentwidget
        self.load_all_projects_pdata()

    def save_project(self):
        print("保存成功")
        pdata = ProjectData(self.parentwidget.curr_card)
        projectpath = os.path.join(self.rootpath, pdata.pinfo.time)
        self.check_dir(projectpath)
        filepath = os.path.join(self.rootpath, pdata.pinfo.time, pdata.pinfo.time + ".json")
        if os.path.exists(filepath):
            reply = QMessageBox.question(self.parentwidget, '提示', '文件已存在，是否覆盖？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                return

        save_pdata_json(pdata, filepath)

    def load_all_projects_pdata(self):
        # 将rootpath目录下的所有加载为pdata
        for root, dirs, files in os.walk(self.rootpath):
            for dir in dirs:
                dir = os.path.join(root, dir)
                for filename in os.listdir(dir):
                    if filename.endswith('.json'):
                        pdata = load_pdata_json(os.path.join(dir, filename))
                        self.pdatas[filename] = pdata

    def check_dir(self, projectpath):
        if not os.path.exists(self.rootpath):
            os.mkdir(self.rootpath)
        if not os.path.exists(projectpath):
            os.mkdir(projectpath)
        code_dir_path = os.path.join(projectpath, "src")
        if not os.path.exists(code_dir_path):
            os.mkdir(code_dir_path)


class ProjectScrollArea(QWidget):
    def __init__(self, parent=None):
        super(ProjectScrollArea, self).__init__()

        # 垂直布局
        self.layout = QVBoxLayout(self)
        # 创建一个滚动区域
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        # 滚动区域内部的 widget 和布局
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        self.manager = ProjectManager(self)
        self.manager.load_all_projects_pdata()

        self.curr_card = None
        self.initData()

    def initData(self):
        for filename in self.manager.pdatas:
            pdata = self.manager.pdatas[filename]
            self.load_card(pdata)

    def load_card(self, pdata):
        card = ProjectCard(pdata)
        card.card_clicked.connect(self.change_current_card)  # 连接信号到槽函数
        card.theme("./QTui/themes/white_border.qss")
        self.scroll_layout.addWidget(card)

    def add_card(self):
        if self.curr_card is not None:
            self.set_curr_card_theme("./QTui/themes/white_border.qss")
        # 创建一个 ProjectCard 并添加到滚动区域的布局中
        card = ProjectCard()
        card.card_clicked.connect(self.change_current_card)  # 连接信号到槽函数
        self.scroll_layout.addWidget(card)
        self.set_current_card(card)
        # 设置为lineEdit当前时间戳
        current_datetime = datetime.datetime.now()
        self.curr_card.ui.lineEdit.setText(current_datetime.strftime('%Y-%m-%d-%H-%M-%S'))
        self.set_curr_card_theme("./QTui/themes/white_border.qss")

    def set_current_card(self, card):
        self.curr_card = card
        print("当前卡片已设置为:", card)

    def set_curr_card_theme(self, theme):
        self.curr_card.theme(theme)

    def change_current_card(self, card):
        # 如果有之前选中的卡片，重置其边框颜色
        if self.curr_card is not None:
            self.set_curr_card_theme("./QTui/themes/white_border.qss")

        self.set_current_card(card)
        self.set_curr_card_theme("./QTui/themes/purple_border.qss")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = ProjectScrollArea()
    window.show()
    sys.exit(app.exec_())
