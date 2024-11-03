import json
import os
import shutil
import sys
import subprocess
import numpy as np
import openpyxl
from os import path as osp
from PySide2.QtGui import QIcon, QFont
import pandas as pd
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QAction, QDoubleSpinBox,
    QComboBox, QTableWidget, QTableWidgetItem, QListWidget, QPushButton, QMenu, QCheckBox, QSizePolicy,
    QFormLayout, QTextEdit, QMessageBox, QTreeWidgetItem, QFileDialog, QSpinBox, QSpacerItem
)
from openpyxl.utils import get_column_letter

class FilterMX(QDialog):
    def __init__(self, mainWindow, item):
        super().__init__()
        self.path = item.data(0, Qt.UserRole)
        self.info_dict = mainWindow.info_dict
        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")
        # self.data = self.load_data_from_json(osp.join(self.path, "模型目录.json"))
        self.data = []
        gy_styles = self.get_folder_names(self.path)
        for gy_style in gy_styles:
            path = osp.join(self.path, gy_style)
            mx_styles = self.get_folder_names(path)
            for mx_style in mx_styles:
                mx_style_path = osp.join(path, mx_style)
                jt_mxs = self.get_folder_names(mx_style_path)
                for jt_mx in jt_mxs:
                    mx_path = osp.join(mx_style_path, jt_mx, f"{jt_mx}.json")
                    if osp.exists(mx_path):  # 先检查文件是否存在
                        data = self.read_json_file(mx_path)
                        if data:
                            self.data.append(data)
                    else:
                        print(f"文件 {mx_path} 不存在")

        self.ColumnCount = len(self.data[0])
        self.keys = self.data[0].keys()
        # 创建 UI 组件
        self.table_cx = QTableWidget()
        self.table_cx.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_cx.customContextMenuRequested.connect(self.show_context_menu)
        # 创建筛选器组件
        self.filter_type = QComboBox()
        self.filter_type.addItem("全部")
        self.filter_type.addItems(self.info_dict["模型工艺类型"])

        self.filter_type2 = QComboBox()
        self.filter_type2.addItem("全部")
        self.filter_type2.addItems(self.info_dict["模型类型"])

        self.filter_material = QComboBox()  # 熔覆材料
        self.filter_material.addItem("全部")
        self.filter_material.addItems(self.info_dict["具体材料"])
        self.filter_substrate = QComboBox()  # 基板材料
        self.filter_substrate.addItem("全部")
        self.filter_substrate.addItems(self.info_dict["具体材料"])
        # 激光功率
        self.filter_jg_min = QSpinBox()
        self.filter_jg_min.setRange(0, 10000)
        self.filter_jg_max = QSpinBox()
        self.filter_jg_max.setRange(0, 10000)
        self.filter_jg_max.setValue(10000)  # 设置默认值为最大值
        # 熔覆速度
        self.filter_speed_min = QSpinBox()
        self.filter_speed_min.setRange(0, 100)
        self.filter_speed_max = QSpinBox()
        self.filter_speed_max.setRange(0, 100)
        self.filter_speed_max.setValue(10000)  # 设置默认值为最大值

        filter_button = QPushButton("筛选")
        filter_button.clicked.connect(self.apply_filter)

        # 布局设置
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("工艺类型:"))
        filter_layout.addWidget(self.filter_type)
        filter_layout.addWidget(QLabel("模型类型:"))
        filter_layout.addWidget(self.filter_type2)
        filter_layout.addWidget(QLabel("熔覆材料:"))
        filter_layout.addWidget(self.filter_material)
        filter_layout.addWidget(QLabel("基板材料:"))
        filter_layout.addWidget(self.filter_substrate)
        filter_layout.addWidget(QLabel("激光功率:"))
        filter_layout.addWidget(self.filter_jg_min)
        filter_layout.addWidget(QLabel("到"))
        filter_layout.addWidget(self.filter_jg_max)
        filter_layout.addWidget(QLabel("熔覆速度:"))
        filter_layout.addWidget(self.filter_speed_min)
        filter_layout.addWidget(QLabel("到"))
        filter_layout.addWidget(self.filter_speed_max)
        filter_layout.addWidget(filter_button)

        # 主布局
        main_layout = QVBoxLayout()
        main_layout.addLayout(filter_layout)
        main_layout.addWidget(self.table_cx)
        self.setLayout(main_layout)

        # 初始化表格
        self.populate_table(self.data)

        # 设置窗口标题和大小
        self.setWindowTitle("模型筛选")
        self.resize(800, 600)

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
                self.table_cx.setItem(row_index, col_index, QTableWidgetItem(str(value)))

    def show_context_menu(self, position):
        context_menu = QMenu(self)

        action_edit = QAction("打开", self)
        action_edit.triggered.connect(self.open_item)
        context_menu.addAction(action_edit)

        action_delete = QAction("导入", self)
        action_delete.triggered.connect(self.imp_item)
        context_menu.addAction(action_delete)

        context_menu.exec_(self.table_cx.viewport().mapToGlobal(position))

    def open_item(self):
        item = self.table_cx.currentItem()
        if item:
            row = item.row()  # 获取当前项的行索引
            # 获取该行前两列的内容
            if row >= 0:  # 确保行索引有效
                col1_item = self.table_cx.item(row, 0)  # 前第一列
                col2_item = self.table_cx.item(row, 1)  # 前第二列

                col1_text = col1_item.text() if col1_item else "null"
                col2_text = col2_item.text() if col2_item else "null"
                # 拼接路径
                path = os.path.join(self.path, col2_text, col1_text)

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
        if item:
            row = item.row()
            self.table_cx.removeRow(row)
            print(f"删除项: {item.text()}")

    def apply_filter(self):
        type_filter = self.filter_type.currentText()
        type2_filter = self.filter_type2.currentText()
        material_filter = self.filter_material.currentText()
        substrate_filter = self.filter_substrate.currentText()
        jg_min = self.filter_jg_min.value()
        jg_max = self.filter_jg_max.value()
        speed_min = self.filter_speed_min.value()
        speed_max = self.filter_speed_max.value()

        filtered_data = []

        for item in self.data:
            type_matches = (type_filter == "全部" or item["工艺类型"] == type_filter)
            type2_matches = (type2_filter == "全部" or item["模型类型"] == type2_filter)
            material_matches = (material_filter == "全部" or item["熔覆材料"] == material_filter)
            substrate_matches = (substrate_filter == "全部" or item["基板材料"] == substrate_filter)
            jg_matches = (jg_min <= item["激光功率(W)"] <= jg_max)
            speed_matches = (speed_min <= item["熔覆速度(mm/s)"] <= speed_max)

            if type_matches and type2_matches and material_matches and substrate_matches and jg_matches and speed_matches:
                filtered_data.append(item)

        self.populate_table(filtered_data)

class CustomDialog(QDialog):
    def __init__(self, mainWindow, item):
        super().__init__()
        self.path = item.data(0, Qt.UserRole)
        self.info_dict = mainWindow.info_dict
        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")

        # 创建布局
        layout = QVBoxLayout()

        # 添加标签
        self.label = QLabel("请输入信息:")
        layout.addWidget(self.label)

        # 添加第一个文本框
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("第一个输入框")  # 设置占位符文本
        layout.addWidget(self.input1)

        # 添加第二个文本框
        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("第二个输入框")  # 设置占位符文本
        layout.addWidget(self.input2)

        # 创建按钮布局
        button_layout = QHBoxLayout()

        # 添加确定按钮
        self.ok_button = QPushButton("确定")
        self.ok_button.clicked.connect(self.accept)  # 点击时接受
        button_layout.addWidget(self.ok_button)

        # 添加取消按钮
        self.cancel_button = QPushButton("取消")
        self.cancel_button.clicked.connect(self.reject)  # 点击时拒绝
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = CustomDialog()
    if dialog.exec_() == QDialog.Accepted:
        print("确定被点击")
    else:
        print("取消被点击")
    sys.exit(app.exec_())