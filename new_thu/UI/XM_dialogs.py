import json
import os
import shutil
from datetime import datetime
import sys
import subprocess
import numpy as np
import openpyxl
from os import path as osp
from PySide2.QtGui import QIcon, QFont
import pandas as pd
from PySide2.QtCore import Qt, QDate
from PySide2.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QAction, QDoubleSpinBox,
    QComboBox, QTableWidget, QTableWidgetItem, QListWidget, QPushButton, QMenu, QCheckBox, QSizePolicy,
    QFormLayout, QTextEdit, QMessageBox, QTreeWidgetItem, QFileDialog, QSpinBox, QSpacerItem, QDateEdit
)
from openpyxl.utils import get_column_letter
def get_folder_names(path):
    try:
        # 列出目录中的所有内容
        dir_contents = os.listdir(path)

        # 过滤出文件夹
        folders = [name for name in dir_contents if osp.isdir(osp.join(path, name))]

        return folders
    except FileNotFoundError:
        print(f"路径 {path} 不存在")
        return []
    except Exception as e:
        print(f"遍历路径 {path} 时发生错误: {e}")
        return []
class style_equipment_Dialog(QDialog):
    def __init__(self, mainWindow, item):
        super().__init__()
        self.item = item
        self.path = item.data(0, Qt.UserRole)
        self.json_path = osp.join(self.path, '类型及设备.json')
        self.save_path = osp.join(self.path, '类型及设备.json')
        self.mainWindow = mainWindow
        self.info_dict = mainWindow.info_dict
        self.style = ''
        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")
        # 设置字体大小
        font = QFont()
        font.setPointSize(10)  # 设置字体大小为10
        self.setFont(font)
        self.setFixedSize(360, 400)
        self.setWindowTitle('类型及设备')
        # 创建布局
        layout = QVBoxLayout()

        # 项目日期
        date_layout = QHBoxLayout()
        self.date_label = QLabel("项目日期:")
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())  # 设置默认为当前日期
        self.date_edit.setDisplayFormat("yyyy.MM.dd")  # 设置显示格式
        date_layout.addWidget(self.date_label)
        date_layout.addWidget(self.date_edit)
        layout.addLayout(date_layout)
        # 类型下拉选择
        type_layout = QHBoxLayout()
        self.type_label = QLabel("项目类型:")
        self.type_combo = QComboBox()
        self.type_combo.addItems(["送粉", "送丝", "粉丝同送"])  # 添加选项
        type_layout.addWidget(self.type_label)
        type_layout.addWidget(self.type_combo)
        layout.addLayout(type_layout)

        # 能量设备
        device_layout1 = QHBoxLayout()
        self.device_label1 = QLabel("能量设备:")
        self.device_combo1 = QComboBox()
        self.device_combo1.addItem('')
        self.device_combo1.addItems(self.info_dict['能量'])
        device_layout1.addWidget(self.device_label1)
        device_layout1.addWidget(self.device_combo1)
        layout.addLayout(device_layout1)
        # 质量设备1
        device_layout2 = QHBoxLayout()
        self.device_label2 = QLabel("质量设备1:")
        self.device_combo2 = QComboBox()
        self.device_combo2.addItem('')
        self.device_combo2.addItems(self.info_dict['质量'])
        device_layout2.addWidget(self.device_label2)
        device_layout2.addWidget(self.device_combo2)
        layout.addLayout(device_layout2)
        # 质量设备2
        device_layout3 = QHBoxLayout()
        self.device_label3 = QLabel("质量设备2:")
        self.device_combo3 = QComboBox()
        self.device_combo3.addItem('')
        self.device_combo3.addItems(self.info_dict['质量'])
        device_layout3.addWidget(self.device_label3)
        device_layout3.addWidget(self.device_combo3)
        layout.addLayout(device_layout3)
        # 运动设备
        device_layout4 = QHBoxLayout()
        self.device_label4 = QLabel("运动设备:")
        self.device_combo4 = QComboBox()
        self.device_combo4.addItem('')
        self.device_combo4.addItems(self.info_dict['运动'])
        device_layout4.addWidget(self.device_label4)
        device_layout4.addWidget(self.device_combo4)
        layout.addLayout(device_layout4)
        # 保护气氛
        qf_layout1 = QHBoxLayout()
        self.qf_label1 = QLabel("保护气氛:")
        self.qf_combo1 = QComboBox()
        self.qf_combo1.addItem('')
        self.qf_combo1.addItems(self.info_dict['气氛'])
        qf_layout1.addWidget(self.qf_label1)
        qf_layout1.addWidget(self.qf_combo1)
        layout.addLayout(qf_layout1)
        # 载气气氛
        qf_layout2 = QHBoxLayout()
        self.qf_label2 = QLabel("载气气氛:")
        self.qf_combo2 = QComboBox()
        self.qf_combo2.addItem('')
        self.qf_combo2.addItems(self.info_dict['气氛'])
        qf_layout2.addWidget(self.qf_label2)
        qf_layout2.addWidget(self.qf_combo2)
        layout.addLayout(qf_layout2)
        # 熔池状态
        jk_layout1 = QHBoxLayout()
        self.jk_label1 = QLabel("熔池状态:")
        self.jk_combo1 = QComboBox()
        self.jk_combo1.addItem('')
        self.jk_combo1.addItems(self.info_dict['监控'])
        jk_layout1.addWidget(self.jk_label1)
        jk_layout1.addWidget(self.jk_combo1)
        layout.addLayout(jk_layout1)
        # 熔池温度
        jk_layout2 = QHBoxLayout()
        self.jk_label2 = QLabel("熔池温度:")
        self.jk_combo2 = QComboBox()
        self.jk_combo2.addItem('')
        self.jk_combo2.addItems(self.info_dict['监控'])
        jk_layout2.addWidget(self.jk_label2)
        jk_layout2.addWidget(self.jk_combo2)
        layout.addLayout(jk_layout2)
        # 熔池流动
        jk_layout3 = QHBoxLayout()
        self.jk_label3 = QLabel("熔池流动:")
        self.jk_combo3 = QComboBox()
        self.jk_combo3.addItem('')
        self.jk_combo3.addItems(self.info_dict['监控'])
        jk_layout3.addWidget(self.jk_label3)
        jk_layout3.addWidget(self.jk_combo3)
        layout.addLayout(jk_layout3)
        # 熔覆形貌
        jk_layout4 = QHBoxLayout()
        self.jk_label4 = QLabel("熔覆形貌:")
        self.jk_combo4 = QComboBox()
        self.jk_combo4.addItem('')
        self.jk_combo4.addItems(self.info_dict['监控'])
        jk_layout4.addWidget(self.jk_label4)
        jk_layout4.addWidget(self.jk_combo4)
        layout.addLayout(jk_layout4)

        # 设置所有下拉框的宽度一致
        for combo in [self.date_edit, self.type_combo, self.device_combo1, self.device_combo2, self.device_combo3, self.device_combo4,
                      self.jk_combo1, self.jk_combo2, self.jk_combo3, self.jk_combo4, self.qf_combo1, self.qf_combo2]:
            combo.setFixedWidth(200)  # 设置固定宽度，可以根据需要调整

        # 按钮布局
        button_layout = QHBoxLayout()
        # 项目导入按钮
        self.import_button = QPushButton("项目导入")
        self.ok_button = QPushButton("确认")
        self.cancel_btt = QPushButton("取消")
        button_layout.addWidget(self.import_button)
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_btt)
        self.import_button.clicked.connect(self.import_from_xm)
        self.ok_button.clicked.connect(self.saveto_json)
        self.cancel_btt.clicked.connect(self.reject)

        layout.addLayout(button_layout)
        self.setLayout(layout)
        if osp.exists(self.json_path):
            self.initData()

    def initData(self):
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        json_data = QDate.fromString(data["项目日期"], "yyyy.MM.dd")
        self.date_edit.setDate(json_data)
        self.type_combo.setCurrentText(data["项目类型"])
        self.device_combo1.setCurrentText(data["能量设备"])
        self.device_combo2.setCurrentText(data["质量设备1"])
        self.device_combo3.setCurrentText(data["质量设备2"])
        self.device_combo4.setCurrentText(data["运动设备"])
        self.qf_combo1.setCurrentText(data["保护气氛"])
        self.qf_combo2.setCurrentText(data["载气气氛"])
        self.jk_combo1.setCurrentText(data["熔池状态"])
        self.jk_combo2.setCurrentText(data["熔池温度"])
        self.jk_combo3.setCurrentText(data["熔池流动"])
        self.jk_combo4.setCurrentText(data["熔覆形貌"])

    def import_from_xm(self):
        dialog = ProjectFilterDialog(self.mainWindow, self.item.parent().parent())
        if dialog.exec_() == QDialog.Accepted:
            project_name = dialog.get_selected_text()
            project_path = osp.join(self.mainWindow.projectroot, project_name)
            self.json_path = osp.join(project_path, "类型及设备", "类型及设备.json")
            self.initData()

    def saveto_json(self):
        # 获取用户输入
        data = {
            "项目日期": self.date_edit.date().toString("yyyy.MM.dd"),
            "项目类型": self.type_combo.currentText(),
            "能量设备": self.device_combo1.currentText(),
            "质量设备1": self.device_combo2.currentText(),
            "质量设备2": self.device_combo3.currentText(),
            "运动设备": self.device_combo4.currentText(),
            "保护气氛": self.qf_combo1.currentText(),
            "载气气氛": self.qf_combo2.currentText(),
            "熔池状态": self.jk_combo1.currentText(),
            "熔池温度": self.jk_combo2.currentText(),
            "熔池流动": self.jk_combo3.currentText(),
            "熔覆形貌": self.jk_combo4.currentText()
        }
        print("保存到"+self.save_path)
        self.style = self.type_combo.currentText()
        mod_path = osp.join(self.mainWindow.dataroot, "模型库", self.style)
        mod_names = get_folder_names(mod_path)
        for mod_name in mod_names:
            new_path = osp.join(self.item.parent().data(0, Qt.UserRole), '分析预测', mod_name)
            if not osp.exists(new_path):
                os.mkdir(new_path)
        # 保存为 JSON 文件
        with open(self.save_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        # 重新生成子项
        self.parent = self.item.parent()
        while self.parent.childCount() > 0:
            self.parent.removeChild(self.parent.child(0))
        for obj in os.listdir(self.parent.data(0, Qt.UserRole)):
            tmp_path = osp.join(self.parent.data(0, Qt.UserRole), obj)
            if osp.isdir(tmp_path):
                dir_item = self.mainWindow._generate_item(self.parent, obj, tmp_path, 0)
                self.mainWindow.list_dir(dir_item, tmp_path)  # 递归调用
            else:
                self.mainWindow._generate_item(self.parent, obj, tmp_path, self.parent.NodeFile.value)

        super().accept()
    # def reject(self):
    #     print(1245)

class ProjectFilterDialog(QDialog):
    def __init__(self, mainWindow, item):
        super().__init__()
        self.item = item
        self.path = item.data(0, Qt.UserRole)
        self.info_dict = mainWindow.info_dict
        self.names = get_folder_names(mainWindow.projectroot)
        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")
        # 设置窗口标题和大小
        self.setWindowTitle("模型项目")
        self.resize(1425, 700)

        self.data = []  # 存储所有项目
        xm_names = self.get_folder_names(self.path)
        for xm_name in xm_names:
            path1 = osp.join(self.path, xm_name, "类型及设备", "类型及设备.json")
            path2 = osp.join(self.path, xm_name, "材料及工艺", "材料及工艺.json")
            if osp.exists(path1):  # 先检查文件是否存在
                data1 = self.read_json_file(path1)
                data2 = {"熔覆材料": "", "基板材料": "", "激光功率": 0, "熔覆速度": 0}
                if data1 is not None:  # 确保数据有效
                    # 如果 data 是字典
                    data_with_name = {"项目名称": xm_name}  # 创建新的字典
                    data_with_name.update(data1)
                    if osp.exists(path2):
                        data2 = self.read_json_file(path2)
                    data_with_name.update(data2)
                    # 选择性保存到 data 中
                    data = {
                        "项目名称": data_with_name.get("项目名称"),
                        "项目日期": data_with_name.get("项目日期"),
                        "项目类型": data_with_name.get("项目类型"),
                        "熔覆材料": data_with_name.get("熔覆材料"),
                        "基板材料": data_with_name.get("基板材料"),
                        "激光功率": data_with_name.get("激光功率(W)"),
                        "熔覆速度": data_with_name.get("熔覆速度(mm/s)"),
                        "熔池状态": data_with_name.get("熔池状态"),
                        "熔池温度": data_with_name.get("熔池温度"),
                        "熔池流动": data_with_name.get("熔池流动"),
                        "熔覆形貌": data_with_name.get("熔覆形貌"),
                    }
                    self.data.append(data)
        if not self.data:  # 检查 self.data 是否为空
            QMessageBox.warning(self, '警告', '不存在可筛选信息!', QMessageBox.Ok)
            return
        self.ColumnCount = len(self.data[0])
        self.keys = self.data[0].keys()
        # 创建 UI 组件
        self.table_cx = QTableWidget()
        self.table_cx.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_cx.customContextMenuRequested.connect(self.show_context_menu)
        # 创建筛选器组件
        # self.filter_name = QLineEdit()  # 项目名称
        # self.filter_name.setMaximumWidth(150)
        self.filter_name = QComboBox()
        self.filter_name.setMinimumWidth(120)
        self.filter_name.addItem("全部")
        self.filter_name.addItems(self.names)
        # 项目类型
        self.filter_type = QComboBox()
        self.filter_type.addItem("全部")
        self.filter_type.setMinimumWidth(120)
        self.filter_type.addItems(["送粉", "送丝", "粉丝同送"])
        # 熔覆材料
        self.filter_material = QComboBox()
        self.filter_material.addItem("全部")
        self.filter_material.addItems(self.info_dict["具体材料"])
        # 基板材料
        self.filter_substrate = QComboBox()
        self.filter_substrate.addItem("全部")
        self.filter_substrate.addItems(self.info_dict["具体材料"])
        # 熔池状态
        self.filter_state = QComboBox()
        self.filter_state.setMinimumWidth(100)
        self.filter_state.addItem("全部")
        self.filter_state.addItems(self.info_dict["监控"])
        # 熔池温度
        self.filter_wen = QComboBox()
        self.filter_wen.setMinimumWidth(100)
        self.filter_wen.addItem("全部")
        self.filter_wen.addItems(self.info_dict["监控"])
        # 熔池流动
        self.filter_liu = QComboBox()
        self.filter_liu.setMinimumWidth(120)
        self.filter_liu.addItem("全部")
        self.filter_liu.addItems(self.info_dict["监控"])
        # 熔覆形貌
        self.filter_mao = QComboBox()
        self.filter_mao.setMinimumWidth(120)
        self.filter_mao.addItem("全部")
        self.filter_mao.addItems(self.info_dict["监控"])
        # 项目日期
        self.filter_time_min = QDateEdit()
        self.filter_time_min.setDisplayFormat("yyyy.MM.dd")
        self.filter_time_max = QDateEdit()  # 默认为当前时间
        self.filter_time_max.setDisplayFormat("yyyy.MM.dd")
        self.filter_time_max.setDate(QDate.currentDate())
        # 激光功率
        self.filter_jg_min = QSpinBox()
        self.filter_jg_min.setFixedWidth(100)
        self.filter_jg_min.setRange(0, 10000)
        self.filter_jg_max = QSpinBox()
        self.filter_jg_max.setFixedWidth(100)
        self.filter_jg_max.setRange(0, 10000)
        self.filter_jg_max.setValue(10000)  # 设置默认值为最大值
        # 熔覆速度
        self.filter_speed_min = QSpinBox()
        self.filter_speed_min.setFixedWidth(100)
        self.filter_speed_min.setRange(0, 10000)
        self.filter_speed_max = QSpinBox()
        self.filter_speed_max.setFixedWidth(100)
        self.filter_speed_max.setRange(0, 10000)
        self.filter_speed_max.setValue(10000)  # 设置默认值为最大值

        filter_button = QPushButton("筛选")
        filter_button.setMaximumWidth(120)
        filter_button.clicked.connect(self.apply_filter)

        # 布局设置
        filter_layout1 = QHBoxLayout()
        filter_layout2 = QHBoxLayout()
        filter_layout = QVBoxLayout()
        hl11 = QHBoxLayout()
        hl12 = QHBoxLayout()
        hl13 = QHBoxLayout()
        hl14 = QHBoxLayout()
        hl15 = QHBoxLayout()
        hl21 = QHBoxLayout()
        hl22 = QHBoxLayout()
        hl23 = QHBoxLayout()
        hl24 = QHBoxLayout()
        hl25 = QHBoxLayout()
        hl26 = QHBoxLayout()
        hl11.setContentsMargins(0, 0, 0, 0)  # 消除内边距
        hl11.setSpacing(10)  # 消除间距
        hl12.setSpacing(10)
        hl13.setSpacing(10)
        hl14.setSpacing(10)
        hl15.setSpacing(10)
        hl21.setSpacing(10)
        hl22.setSpacing(10)
        hl23.setSpacing(10)
        hl24.setSpacing(10)
        hl25.setSpacing(10)
        hl26.setSpacing(10)

        hl11.addWidget(QLabel("名称:"))
        hl11.addWidget(self.filter_name)
        hl12.addWidget(QLabel("日期:"))
        hl12.addWidget(self.filter_time_min)
        hl12.addWidget(QLabel("到"))
        hl12.addWidget(self.filter_time_max)
        hl13.addWidget(QLabel("熔覆材料:"))
        hl13.addWidget(self.filter_material)
        hl14.addWidget(QLabel("基板材料:"))
        hl14.addWidget(self.filter_substrate)
        hl15.addWidget(QLabel("激光功率:"))
        hl15.addWidget(self.filter_jg_min)
        hl15.addWidget(QLabel("到"))
        hl15.addWidget(self.filter_jg_max)
        hl21.addWidget(QLabel("类型:"))
        hl21.addWidget(self.filter_type)
        hl22.addWidget(QLabel("熔覆速度:"))
        hl22.addWidget(self.filter_speed_min)
        hl22.addWidget(QLabel("到"))
        hl22.addWidget(self.filter_speed_max)
        hl23.addWidget(QLabel("熔池状态:"))
        hl23.addWidget(self.filter_state)
        hl24.addWidget(QLabel("熔池温度:"))
        hl24.addWidget(self.filter_wen)
        hl25.addWidget(QLabel("熔池流动:"))
        hl25.addWidget(self.filter_liu)
        hl26.addWidget(QLabel("熔覆形貌:"))
        hl26.addWidget(self.filter_mao)

        filter_layout1.addLayout(hl11)
        filter_layout1.addStretch(1)  # 添加弹性空间

        filter_layout1.addLayout(hl12)
        filter_layout1.addStretch(1)
        filter_layout1.addLayout(hl13)
        filter_layout1.addStretch(1)
        filter_layout1.addLayout(hl14)
        filter_layout1.addStretch(1)
        filter_layout1.addLayout(hl15)
        filter_layout1.addStretch(1)
        filter_layout1.addWidget(filter_button)

        filter_layout2.addLayout(hl21)
        filter_layout2.addStretch(1)
        filter_layout2.addLayout(hl22)
        filter_layout2.addStretch(1)
        filter_layout2.addLayout(hl23)
        filter_layout2.addStretch(1)
        filter_layout2.addLayout(hl24)
        filter_layout2.addStretch(1)
        filter_layout2.addLayout(hl25)
        filter_layout2.addStretch(1)
        filter_layout2.addLayout(hl26)

        filter_layout.addLayout(filter_layout1)
        filter_layout.addLayout(filter_layout2)

        # 确定和取消按钮
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("确认")
        self.cancel_button = QPushButton("取消")
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        # 主布局
        main_layout = QVBoxLayout()
        main_layout.addLayout(filter_layout)
        main_layout.addWidget(self.table_cx)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        self.selected_text = None  # 用于存储选中的项文本
        # 初始化表格
        self.populate_table(self.data)

    def accept(self):
        item = self.table_cx.currentItem()
        row = item.row()  # 获取当前项的行索引
        col1_item = self.table_cx.item(row, 0)  # 前第一列
        col1_text = col1_item.text() if col1_item else "null"  # 获取项目名称
        self.selected_text = col1_text
        super().accept()

    def get_selected_text(self):
        return self.selected_text  # 返回选中的项目文本
    def get_folder_names(self, path):
        try:
            # 列出目录中的所有内容
            dir_contents = os.listdir(path)

            # 过滤出文件夹
            folders = [name for name in dir_contents if osp.isdir(osp.join(path, name))]

            return folders
        except FileNotFoundError:
            print(f"路径 {path} 不存在")
            return []
        except Exception as e:
            print(f"遍历路径 {path} 时发生错误: {e}")
            return []
    def read_json_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"文件 {file_path} 不存在")
            return None
        except json.JSONDecodeError as e:
            print(f"解析 JSON 文件 {file_path} 时发生错误: {e}")
            return None
    def populate_table(self, data):
        self.table_cx.setRowCount(len(data))
        self.table_cx.setColumnCount(self.ColumnCount)
        self.table_cx.setHorizontalHeaderLabels(self.keys)
        for row_index, row_data in enumerate(data):
            for col_index, (key, value) in enumerate(row_data.items()):
                # 如果值为 None，则用空字符串或其他默认值替代
                if value is None:
                    display_value = ""
                else:
                    display_value = str(value)
                item = QTableWidgetItem(str(display_value))
                item.setTextAlignment(Qt.AlignCenter)  # 设置文本居中对齐
                self.table_cx.setItem(row_index, col_index, item)
        self.table_cx.horizontalHeader().setStretchLastSection(True)  # 最后一列扩展以占满空间
        # for row_index, row_data in enumerate(data):
        #     for col_index, (key, value) in enumerate(row_data.items()):
        #         # 如果值为 None，则用空字符串或其他默认值替代
        #         if value is None:
        #             display_value = ""
        #         else:
        #             display_value = str(value)
        #         self.table_cx.setItem(row_index, col_index, QTableWidgetItem(display_value))

    def show_context_menu(self, position):
        context_menu = QMenu(self)

        action_open = QAction("打开", self)
        action_open.triggered.connect(self.open_item)
        context_menu.addAction(action_open)

        action_zhan = QAction("展开", self)
        action_zhan.triggered.connect(self.imp_item)
        context_menu.addAction(action_zhan)

        context_menu.exec_(self.table_cx.viewport().mapToGlobal(position))

    def open_item(self):
        item = self.table_cx.currentItem()
        if item:
            row = item.row()  # 获取当前项的行索引
            # 获取该行前两列的内容
            if row >= 0:  # 确保行索引有效
                col1_item = self.table_cx.item(row, 0)  # 前第一列
                col1_text = col1_item.text() if col1_item else "null"
                # 拼接路径
                path = os.path.join(self.path, col1_text)

                # 打开文件
                if os.path.exists(path):  # 检查路径是否存在
                    try:
                        if os.name == 'nt':  # Windows
                            os.startfile(path)
                        elif os.name == 'posix':  # MacOS / Linux
                            subprocess.run(['open', path])  # MacOS
                            # subprocess.run(['xdg-open', path])  # Linux
                    except Exception as e:
                        print(f"打开文件时出错: {e}")
                else:
                    print(f"路径不存在: {path}")

    def imp_item(self):
        item = self.table_cx.currentItem()
        row = item.row()  # 获取当前项的行索引
        col1_item = self.table_cx.item(row, 0)  # 前第一列
        col1_text = col1_item.text() if col1_item else "null"  # 获取项目名称
        self.selected_text = col1_text
        for i in range(self.item.childCount()):
            if self.item.child(i).text(0) == col1_text:
                self.item.child(i).setExpanded(True)  # 展开匹配的项
            else:
                self.item.child(i).setExpanded(False)
        super().accept()

    def apply_filter(self):
        name_filter = self.filter_name.currentText()
        time_min = self.filter_time_min.dateTime().toString("yyyy.MM.dd")
        time_max = self.filter_time_max.dateTime().toString("yyyy.MM.dd")
        type_filter = self.filter_type.currentText()
        material_filter = self.filter_material.currentText()
        substrate_filter = self.filter_substrate.currentText()
        jg_min = self.filter_jg_min.value()
        jg_max = self.filter_jg_max.value()
        speed_min = self.filter_speed_min.value()
        speed_max = self.filter_speed_max.value()

        filter_wen = self.filter_wen.currentText()
        filter_state = self.filter_state.currentText()
        filter_liu = self.filter_liu.currentText()
        filter_mao = self.filter_mao.currentText()

        filtered_data = []

        for item in self.data:
            # 检查时间范围
            time_matches = (time_min <= item["项目日期"] <= time_max)

            # 检查过滤条件
            name_matches = (name_filter == "全部" or name_filter.lower() in item["项目名称"].lower())
            type_matches = (type_filter == "全部" or item["项目类型"] == type_filter)
            material_matches = (material_filter == "全部" or item["熔覆材料"] == material_filter)
            substrate_matches = (substrate_filter == "全部" or item["基板材料"] == substrate_filter)
            if item["激光功率"] is not None:
                jg_matches = (jg_min <= item["激光功率"] <= jg_max)
            else:
                jg_matches = False
            # speed_matches = (speed_min <= item["熔覆速度"] <= speed_max)
            if item["熔覆速度"] is not None:
                speed_matches = (jg_min <= item["激光功率"] <= jg_max)
            else:
                speed_matches = False

            # 检查其他过滤条件
            wen_matches = (filter_wen == "全部" or item["熔池温度"] == filter_wen)
            state_matches = (filter_state == "全部" or item["熔池状态"] == filter_state)
            liu_matches = (filter_liu == "全部" or item["熔池流动"] == filter_liu)
            mao_matches = (filter_mao == "全部" or item["熔覆形貌"] == filter_mao)

            # 如果所有条件都满足，则添加到过滤后的数据中
            if (time_matches and type_matches and material_matches and substrate_matches and
                    jg_matches and speed_matches and wen_matches and state_matches and
                    liu_matches and mao_matches and name_matches):
                filtered_data.append(item)

        self.populate_table(filtered_data)

class XMProcessDialog(QDialog):
    def __init__(self, mainWindow, item, style):
        super().__init__()
        self.item = item
        self.note = "create"
        self.mainWindow = mainWindow
        self.json_path = osp.join(item.data(0, Qt.UserRole), '材料及工艺.json')
        self.path = item.data(0, Qt.UserRole)
        self.style = style
        if style == "送粉":
            self.setWindowTitle("送粉工艺")
        elif style == "送丝":
            self.setWindowTitle("送丝工艺")
        else:
            self.setWindowTitle("编辑工艺")
        self.setFixedSize(650, 350)
        # 设置窗口图标（可选）
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        # 设置字体大小
        font = QFont()
        font.setPointSize(10)  # 设置字体大小为10
        self.setFont(font)
        # 创建主布局
        layout = QVBoxLayout()
        form = QHBoxLayout()
        form_layout1 = QFormLayout()
        form_layout1.setSpacing(13)  # 设置表单布局中控件间隙
        form_layout2 = QFormLayout()
        form_layout2.setSpacing(13)  # 设置表单布局中控件间隙

        # 创建输入字段
        self.name = QLineEdit()
        self.material_edit = QComboBox()
        self.material_edit.addItems(mainWindow.info_dict["具体材料"])
        form_layout1.addRow("工艺名称", self.name)
        form_layout1.addRow("熔覆材料", self.material_edit)

        self.base_material_edit = QComboBox()
        self.base_material_edit.addItems(mainWindow.info_dict["具体材料"])
        form_layout2.addRow("   ", QLabel("  "))
        form_layout2.addRow("基板材料", self.base_material_edit)

        self.fmd_edit = QLineEdit()
        # self.fmd_edit.setRange(0, 1000)  # 设置范围 粉末粒径(μm)
        self.bansize_edit = QLineEdit()
        # self.bansize_edit.setRange(0, 500)  # 设置范围 基板尺寸(mm)
        self.scd_edit = QDoubleSpinBox()
        self.scd_edit.setRange(0, 10000)  # 设置范围 丝材直径(mm)
        if self.style == "送粉":
            form_layout1.addRow("粉末粒径(μm)", self.fmd_edit)
            form_layout2.addRow("基板尺寸(mm)", self.bansize_edit)
        else:
            form_layout1.addRow("丝材直径(mm)", self.scd_edit)
            form_layout2.addRow("基板尺寸(mm)", self.bansize_edit)

        self.laser_power_edit = QSpinBox()
        self.laser_power_edit.setRange(0, 10000)  # 设置范围 激光功率(W)
        form_layout1.addRow("激光功率(W)", self.laser_power_edit)
        self.welding_speed_edit = QDoubleSpinBox()
        self.welding_speed_edit.setRange(0, 10000)  # 设置范围 熔覆速度(mm/s)
        form_layout2.addRow("熔覆速度(mm/s)", self.welding_speed_edit)

        self.sf_rate_edit = QDoubleSpinBox()
        self.sf_rate_edit.setRange(0, 10000)  # 设置范围 送粉转速(r/min)
        self.ss_rate_edit = QDoubleSpinBox()
        self.ss_rate_edit.setRange(0, 10000)  # 设置范围 送丝速度(m/min)
        if self.style == "送粉":
            form_layout1.addRow("送粉转速(r/min)", self.sf_rate_edit)
        else:
            form_layout1.addRow("送丝速度(m/min)", self.ss_rate_edit)

        self.addition_rate_edit = QDoubleSpinBox()
        self.addition_rate_edit.setRange(0, 10000)  # 设置范围 质量添加(g/min)
        form_layout2.addRow("质量添加(g/min)", self.addition_rate_edit)

        self.spot_voltage_edit = QDoubleSpinBox()
        self.spot_voltage_edit.setRange(0, 10000)  # 设置范围 光斑电压(V)
        self.spot_diameter_edit = QDoubleSpinBox()
        self.spot_diameter_edit.setRange(0, 10000)  # 设置范围 光斑直径(mm)
        self.gap_interval_edit = QDoubleSpinBox()
        self.gap_interval_edit.setRange(0, 10000)  # 设置范围 道间间隔(s)
        self.layer_interval_edit = QDoubleSpinBox()
        self.layer_interval_edit.setRange(0, 10000)  # 设置范围 层间间隔(s)

        if self.style == "送粉":
            form_layout1.addRow("光斑电压(V)", self.spot_voltage_edit)
            form_layout1.addRow("道间间隔(s)", self.gap_interval_edit)
            form_layout2.addRow("光斑直径(mm)", self.spot_diameter_edit)
            form_layout2.addRow("层间间隔(s)", self.layer_interval_edit)

        self.offset_edit = QDoubleSpinBox()
        self.offset_edit.setRange(0, 10000)  # 设置范围 道间偏移(mm)
        form_layout1.addRow("道间偏移(mm)", self.offset_edit)

        self.lift_height_edit = QDoubleSpinBox()
        self.lift_height_edit.setRange(0, 10000)  # 设置范围 层间抬升(mm)
        form_layout2.addRow("层间抬升(mm)", self.lift_height_edit)

        self.protect_gas_flow_edit = QLineEdit()
        # self.protect_gas_flow_edit.setRange(0, 10000)  # 设置范围 保护气及流量(L/min)

        self.carrier_gas_flow_edit = QLineEdit()
        # self.carrier_gas_flow_edit.setRange(0, 10000)  # 设置范围 载气及流量(L/min)

        self.qd_flow_edit = QLineEdit()
        # self.qd_flow_edit.setRange(0, 10000)  # 设置范围 气刀及流量(L/min)

        self.pre_time_edit = QDoubleSpinBox()
        self.pre_time_edit.setRange(0, 10000)  # 设置范围 加工前保护气时长(s)
        self.keep_time_edit = QDoubleSpinBox()
        self.keep_time_edit.setRange(0, 10000)  # 设置范围 保护气保持时间(s)

        if self.style == "送粉":
            form_layout1.addRow("保护气及流量(L/min)", self.protect_gas_flow_edit)
            form_layout2.addRow("载气及流量(L/min)", self.carrier_gas_flow_edit)
        else:
            form_layout1.addRow("保护气及流量(L/min)", self.protect_gas_flow_edit)
            form_layout2.addRow("气刀及流量(L/min)", self.qd_flow_edit)
            form_layout1.addRow("加工前保护气时长(s)", self.pre_time_edit)
            form_layout2.addRow("保护气保持时间(s)", self.keep_time_edit)

        form.addLayout(form_layout1)
        form.addLayout(form_layout2)
        layout.addLayout(form)
        # 确定和取消按钮
        button_layout = QHBoxLayout()
        self.xm_import = QPushButton("项目导入")
        self.gy_import = QPushButton("工艺库导入")
        self.ok_button = QPushButton("确认")
        self.cancel_button = QPushButton("取消")
        button_layout.addWidget(self.xm_import)
        button_layout.addWidget(self.gy_import)
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        # 设置主布局
        self.setLayout(layout)
        # 连接信号
        self.xm_import.clicked.connect(self.import_from_xm)
        self.gy_import.clicked.connect(self.import_from_gy)
        self.ok_button.clicked.connect(self.save_to_json)
        self.cancel_button.clicked.connect(self.accept)

        if osp.exists(self.json_path):
            self.initData()
    def import_from_xm(self):
        dialog = ProjectFilterDialog(self.mainWindow, self.item.parent().parent())
        if dialog.exec_() == QDialog.Accepted:
            project_name = dialog.get_selected_text()
            project_path = osp.join(self.mainWindow.projectroot, project_name)
            self.json_path = osp.join(project_path, "材料及工艺", "材料及工艺.json")
            self.initData()
    def import_from_gy(self):
        gyk_path = osp.join(self.mainWindow.dataroot, "工艺库")
        if self.style == "送粉":
            gyk_path = osp.join(gyk_path, "送粉")
        else:
            gyk_path = osp.join(gyk_path, "送丝")
        names = self.get_file_names(gyk_path)
        dialog = ShowList(names)
        if dialog.exec_() == QDialog.Accepted:  # 显示对话框
            name = dialog.get_selected_item()  # 在对话框关闭后获取选中的项
        gy_path = osp.join(gyk_path, name)
        self.json_path = gy_path
        self.initData()
    def initData(self):
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # 填入控件
        if self.style == "送粉":
            self.name.setText(data.get("工艺名称", ""))
            self.material_edit.setCurrentText(data.get("熔覆材料", ""))
            self.base_material_edit.setCurrentText(data.get("基板材料", ""))
            self.fmd_edit.setText(data.get("粉末粒径(μm)", ""))
            self.bansize_edit.setText(data.get("基板尺寸(mm)", ""))
            self.laser_power_edit.setValue(data.get("激光功率(W)", 0))
            self.welding_speed_edit.setValue(data.get("熔覆速度(mm/s)", 0))
            self.sf_rate_edit.setValue(data.get("送粉转速(r/min)", 0))
            self.addition_rate_edit.setValue(data.get("质量添加(g/min)", 0))
            self.spot_voltage_edit.setValue(data.get("光斑电压(V)", 0))
            self.spot_diameter_edit.setValue(data.get("光斑直径(mm)", 0))
            self.gap_interval_edit.setValue(data.get("道间间隔(s)", 0))
            self.layer_interval_edit.setValue(data.get("层间间隔(s)", 0))
            self.offset_edit.setValue(data.get("道间偏移(mm)", 0))
            self.lift_height_edit.setValue(data.get("层间抬升(mm)", 0))
            self.protect_gas_flow_edit.setText(data.get("保护气及流量(L/min)", ""))
            self.carrier_gas_flow_edit.setText(data.get("载气及流量(L/min)", ""))
        else:
            self.name.setText(data.get("工艺名称", ""))
            self.material_edit.setCurrentText(data.get("熔覆材料", ""))
            self.base_material_edit.setCurrentText(data.get("基板材料", ""))
            self.scd_edit.setValue(data.get("丝材直径(mm)", 0))
            self.bansize_edit.setText(data.get("基板尺寸(mm)", ""))
            self.laser_power_edit.setValue(data.get("激光功率(W)", 0))
            self.welding_speed_edit.setValue(data.get("熔覆速度(mm/s)", 0))
            self.ss_rate_edit.setValue(data.get("送丝速度(m/min)", 0))
            self.addition_rate_edit.setValue(data.get("质量添加(g/min)", 0))
            self.offset_edit.setValue(data.get("道间偏移(mm)", 0))
            self.lift_height_edit.setValue(data.get("层间抬升(mm)", 0))
            self.protect_gas_flow_edit.setText(data.get("保护气及流量(L/min)", ""))
            self.qd_flow_edit.setText(data.get("气刀及流量(L/min)", ""))
            self.pre_time_edit.setValue(data.get("加工前保护气时长(s)", 0))
            self.keep_time_edit.setValue(data.get("保护气保持时间(s)", 0))

    def get_file_names(self, path):
        try:
            # 列出目录中的所有内容
            dir_contents = os.listdir(path)
            # 过滤出文件
            files = [name for name in dir_contents if osp.isfile(osp.join(path, name))]
            return files
        except FileNotFoundError:
            print(f"路径 {path} 不存在")
            return []
        except Exception as e:
            print(f"遍历路径 {path} 时发生错误: {e}")
            return []
    def save_to_json(self):
        file_path = osp.join(self.item.data(0, Qt.UserRole), "材料及工艺.json")
        if self.style == "送粉":
            data = {
                "工艺名称": self.name.text(),
                "熔覆材料": self.material_edit.currentText(),
                "基板材料": self.base_material_edit.currentText(),
                "粉末粒径(μm)": self.fmd_edit.text(),
                "基板尺寸(mm)": self.bansize_edit.text(),
                "激光功率(W)": self.laser_power_edit.value(),
                "熔覆速度(mm/s)": self.welding_speed_edit.value(),
                "送粉转速(r/min)": self.ss_rate_edit.value(),
                "质量添加(g/min)": self.addition_rate_edit.value(),
                "光斑电压(V)": self.spot_voltage_edit.value(),
                "光斑直径(mm)": self.spot_diameter_edit.value(),
                "道间间隔(s)": self.gap_interval_edit.value(),
                "层间间隔(s)": self.layer_interval_edit.value(),
                "道间偏移(mm)": self.offset_edit.value(),
                "层间抬升(mm)": self.lift_height_edit.value(),
                "保护气及流量(L/min)": self.protect_gas_flow_edit.text(),
                "载气及流量(L/min)": self.carrier_gas_flow_edit.text()
            }
        else:
            data = {
                "工艺名称": self.name.text(),
                "熔覆材料": self.material_edit.currentText(),
                "基板材料": self.base_material_edit.currentText(),
                "丝材直径(mm)": self.scd_edit.value(),
                "基板尺寸(mm)": self.bansize_edit.text(),
                "激光功率(W)": self.laser_power_edit.value(),
                "熔覆速度(mm/s)": self.welding_speed_edit.value(),
                "送丝速度(m/min)": self.ss_rate_edit.value(),
                "质量添加(g/min)": self.addition_rate_edit.value(),
                "道间偏移(mm)": self.offset_edit.value(),
                "层间抬升(mm)": self.lift_height_edit.value(),
                "保护气及流量(L/min)": self.protect_gas_flow_edit.text(),
                "气刀及流量(L/min)": self.qd_flow_edit.text(),
                "加工前保护气时长(s)": self.pre_time_edit.value(),
                "保护气保持时间(s)": self.keep_time_edit.value()
            }
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        self.accept()

class XMProcessDialog2(QDialog):
    def __init__(self, mainWindow, item):
        super().__init__()
        self.item = item
        self.mainWindow = mainWindow
        self.json_path = osp.join(item.data(0, Qt.UserRole), '材料及工艺.json')
        self.note = "create"
        if self.item.data(0, Qt.UserRole + 1) == "具体工艺":
            self.note = "edit"
        self.path = item.data(0, Qt.UserRole)
        self.setWindowTitle("粉丝同送")
        self.setFixedSize(670, 380)
        # 设置窗口图标（可选）
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        # 设置字体大小
        font = QFont()
        font.setPointSize(10)  # 设置字体大小为10
        self.setFont(font)
        # 创建主布局
        layout = QVBoxLayout()
        form = QHBoxLayout()
        form_layout1 = QFormLayout()
        form_layout1.setSpacing(13)  # 设置表单布局中控件间隙
        form_layout2 = QFormLayout()
        form_layout2.setSpacing(13)  # 设置表单布局中控件间隙

        # 创建输入字段
        self.name = QLineEdit()  # 工艺名称
        self.material_edit = QComboBox()  # 粉末材料
        self.material_edit.addItems(mainWindow.info_dict["具体材料"])
        self.material_edit2 = QComboBox()  # 送丝材料
        self.material_edit2.addItems(mainWindow.info_dict["具体材料"])

        self.base_material_edit = QComboBox()  # 基板材料
        self.base_material_edit.addItems(mainWindow.info_dict["具体材料"])

        self.sf_rate_edit = QDoubleSpinBox()
        self.sf_rate_edit.setRange(0, 10000)  # 设置范围 送粉转速(r/min)
        self.ss_rate_edit = QDoubleSpinBox()
        self.ss_rate_edit.setRange(0, 10000)  # 设置范围 送丝速度(m/min)
        self.fmd_edit = QLineEdit()  # 粉末粒径
        self.bansize_edit = QLineEdit()  # 基板尺寸
        self.scd_edit = QDoubleSpinBox()  # 丝材直径
        self.scd_edit.setRange(0, 10000)  # 设置范围 丝材直径(mm)
        self.addition_rate_edit = QDoubleSpinBox()
        self.addition_rate_edit.setRange(0, 10000)  # 设置范围 质量添加(g/min)
        self.addition_rate_edit2 = QDoubleSpinBox()
        self.addition_rate_edit2.setRange(0, 10000)  # 设置范围 质量添加(g/min)

        self.spot_voltage_edit = QDoubleSpinBox()
        self.spot_voltage_edit.setRange(0, 10000)  # 设置范围 光斑电压(V)
        self.spot_diameter_edit = QDoubleSpinBox()
        self.spot_diameter_edit.setRange(0, 10000)  # 设置范围 光斑直径(mm)
        self.gap_interval_edit = QDoubleSpinBox()
        self.gap_interval_edit.setRange(0, 10000)  # 设置范围 道间间隔(s)
        self.layer_interval_edit = QDoubleSpinBox()
        self.layer_interval_edit.setRange(0, 10000)  # 设置范围 层间间隔(s)

        self.laser_power_edit = QSpinBox()
        self.laser_power_edit.setRange(0, 10000)  # 设置范围 激光功率(W)
        self.welding_speed_edit = QDoubleSpinBox()
        self.welding_speed_edit.setRange(0, 10000)  # 设置范围 熔覆速度(mm/s)

        self.protect_gas_flow_edit = QLineEdit()
        # self.protect_gas_flow_edit.setRange(0, 10000)  # 设置范围 保护气及流量(L/min)
        self.carrier_gas_flow_edit = QLineEdit()
        # self.carrier_gas_flow_edit.setRange(0, 10000)  # 设置范围 载气及流量(L/min)
        self.qd_flow_edit = QLineEdit()
        # self.qd_flow_edit.setRange(0, 10000)  # 设置范围 气刀及流量(L/min)
        self.pre_time_edit = QDoubleSpinBox()
        self.pre_time_edit.setRange(0, 10000)  # 设置范围 加工前保护气时长(s)
        self.keep_time_edit = QDoubleSpinBox()
        self.keep_time_edit.setRange(0, 10000)  # 设置范围 保护气保持时间(s)
        self.offset_edit = QDoubleSpinBox()
        self.offset_edit.setRange(0, 10000)  # 设置范围 道间偏移(mm)
        self.lift_height_edit = QDoubleSpinBox()
        self.lift_height_edit.setRange(0, 10000)  # 设置范围 层间抬升(mm)
        form_layout1.addRow("工艺名称", self.name)
        form_layout1.addRow("粉末材料", self.material_edit)
        form_layout1.addRow("粉末粒径(μm)", self.fmd_edit)
        form_layout1.addRow("送粉转速(r/min)", self.sf_rate_edit)
        form_layout1.addRow("粉末质量添加(g/min)", self.addition_rate_edit)
        form_layout1.addRow("粉末载气及流量(L/min)", self.carrier_gas_flow_edit)
        form_layout1.addRow("送丝材料", self.material_edit2)
        form_layout1.addRow("丝材直径(mm)", self.scd_edit)
        form_layout1.addRow("送丝速度(m/min)", self.ss_rate_edit)
        form_layout1.addRow("丝质量添加(g/min)", self.addition_rate_edit2)

        form_layout2.addRow("基板材料", self.base_material_edit)
        form_layout2.addRow("基板尺寸(mm)", self.bansize_edit)
        form_layout2.addRow("激光功率(W)", self.laser_power_edit)
        form_layout2.addRow("熔覆速度(mm/s)", self.welding_speed_edit)
        form_layout2.addRow("道间偏移(mm)", self.offset_edit)
        form_layout2.addRow("层间抬升(mm)", self.lift_height_edit)
        form_layout2.addRow("保护气及流量(L/min)", self.protect_gas_flow_edit)
        form_layout2.addRow("保护气保持时间(s)", self.keep_time_edit)
        form_layout2.addRow("气刀及流量(L/min)", self.qd_flow_edit)
        form_layout2.addRow("加工前保护气时长(s)", self.pre_time_edit)

        form.addLayout(form_layout1)
        form.addLayout(form_layout2)
        layout.addLayout(form)
        # 确定和取消按钮
        button_layout = QHBoxLayout()
        self.xm_import = QPushButton("项目导入")
        self.gy_import = QPushButton("工艺库导入")
        self.ok_button = QPushButton("确认")
        self.cancel_button = QPushButton("取消")
        button_layout.addWidget(self.xm_import)
        button_layout.addWidget(self.gy_import)
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        # 设置主布局
        self.setLayout(layout)
        # 连接信号
        self.xm_import.clicked.connect(self.import_from_xm)
        self.gy_import.clicked.connect(self.import_from_gy)
        self.ok_button.clicked.connect(self.save_to_json)
        self.cancel_button.clicked.connect(self.reject)

        if osp.exists(self.json_path):
            self.initData()

    def import_from_xm(self):
        dialog = ProjectFilterDialog(self.mainWindow, self.item.parent().parent())
        if dialog.exec_() == QDialog.Accepted:
            project_name = dialog.get_selected_text()
            project_path = osp.join(self.mainWindow.projectroot, project_name)
            self.json_path = osp.join(project_path, "材料及工艺", "材料及工艺.json")
            self.initData()

    def import_from_gy(self):
        gyk_path = osp.join(self.mainWindow.dataroot, "工艺库")
        gyk_path = osp.join(gyk_path, "粉丝同送")
        names = self.get_file_names(gyk_path)
        dialog = ShowList(names)
        if dialog.exec_() == QDialog.Accepted:  # 显示对话框
            name = dialog.get_selected_item()  # 在对话框关闭后获取选中的项
        gy_path = osp.join(gyk_path, name)
        self.json_path = gy_path
        self.initData()
    def initData(self):
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # 填入控件
        self.name.setText(data.get("工艺名称", ""))
        self.material_edit.setCurrentText(data.get("粉末材料", ""))
        self.fmd_edit.setText(data.get("粉末粒径(μm)", ""))
        self.sf_rate_edit.setValue(data.get("送粉转速(r/min)", 0))
        self.addition_rate_edit.setValue(data.get("粉末质量添加(g/min)", 0))
        self.carrier_gas_flow_edit.setText(data.get("粉末载气及流量(L/min)", ""))
        self.material_edit2.setCurrentText(data.get("送丝材料", ""))
        self.scd_edit.setValue(data.get("丝材直径(mm)", 0))
        self.ss_rate_edit.setValue(data.get("送丝速度(m/min)", 0))
        self.addition_rate_edit.setValue(data.get("丝质量添加(g/min)", 0))

        self.base_material_edit.setCurrentText(data.get("基板材料", ""))
        self.bansize_edit.setText(data.get("基板尺寸(mm)", ""))
        self.laser_power_edit.setValue(data.get("激光功率(W)", 0))
        self.welding_speed_edit.setValue(data.get("熔覆速度(mm/s)", 0))
        self.offset_edit.setValue(data.get("道间偏移(mm)", 0))
        self.lift_height_edit.setValue(data.get("层间抬升(mm)", 0))
        self.protect_gas_flow_edit.setText(data.get("保护气及流量(L/min)", ""))
        self.keep_time_edit.setValue(data.get("保护气保持时间(s)", 0))
        self.qd_flow_edit.setText(data.get("气刀及流量(L/min)", ""))
        self.pre_time_edit.setValue(data.get("加工前保护气时长(s)", 0))

    def get_file_names(self, path):
        try:
            # 列出目录中的所有内容
            dir_contents = os.listdir(path)
            # 过滤出文件
            files = [name for name in dir_contents if osp.isfile(osp.join(path, name))]
            return files
        except FileNotFoundError:
            print(f"路径 {path} 不存在")
            return []
        except Exception as e:
            print(f"遍历路径 {path} 时发生错误: {e}")
            return []
    def save_to_json(self):
        file_path = osp.join(self.item.data(0, Qt.UserRole), "材料及工艺.json")
        data = {
            "工艺名称": self.name.text(),
            "粉末粒径(μm)": self.fmd_edit.text(),
            "送粉转速(r/min)": self.ss_rate_edit.value(),
            "粉末质量添加(g/min)": self.addition_rate_edit.value(),
            "粉末载气及流量(L/min)": self.carrier_gas_flow_edit.text(),
            "送丝材料": self.material_edit2.currentText(),
            "丝材直径(mm)": self.scd_edit.value(),
            "送丝速度(m/min)": self.ss_rate_edit.value(),
            "丝质量添加(g/min)": self.addition_rate_edit.value(),
            "基板材料": self.base_material_edit.currentText(),
            "基板尺寸(mm)": self.bansize_edit.text(),
            "激光功率(W)": self.laser_power_edit.value(),
            "熔覆速度(mm/s)": self.welding_speed_edit.value(),
            "道间偏移(mm)": self.offset_edit.value(),
            "层间抬升(mm)": self.lift_height_edit.value(),
            "保护气及流量(L/min)": self.protect_gas_flow_edit.text(),
            "保护气保持时间(s)": self.keep_time_edit.value(),
            "气刀及流量(L/min)": self.qd_flow_edit.text(),
            "加工前保护气时长(s)": self.pre_time_edit.value(),
        }
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        self.accept()

class ShowList(QDialog):
    def __init__(self, names):
        super().__init__()
        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")

        self.name_list = names
        self.selected_item_text = None  # 用于存储选中的项文本
        self.setFixedSize(400, 300)  # 设置窗口大小
        self.setStyleSheet("font-size: 11pt; background-color: rgb(240, 240, 240);")  # 设置字体大小和背景色

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        self.list_widget.addItems(self.name_list)
        self.list_widget.setSelectionMode(QListWidget.SingleSelection)  # 单选模式

        layout.addWidget(self.list_widget)

        self.button = QPushButton("确定")
        self.button.clicked.connect(self.accept)  # 连接到 accept 方法
        layout.addWidget(self.button)

        self.setLayout(layout)

    def accept(self):
        selected_items = self.list_widget.selectedItems()  # 获取所有选中的项目
        if selected_items:  # 确保至少有一个项目被选中
            self.selected_item_text = selected_items[0].text()  # 获取第一个选中的项目文本
        super().accept()  # 调用父类的 accept 方法以关闭对话框

    def get_selected_item(self):
        return self.selected_item_text  # 返回选中的项目文本

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = style_equipment_Dialog(1, 1)
    dialog.exec_()
    sys.exit(app.exec_())