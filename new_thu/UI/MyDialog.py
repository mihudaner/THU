import json
import os
import shutil
import sys
import subprocess
import numpy as np
import openpyxl
from os import path as osp
from PySide2.QtGui import QIcon
import pandas as pd
from PySide2.QtCore import Qt
from PySide2.QtGui import QDoubleValidator
from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QAction,
    QComboBox, QTableWidget, QTableWidgetItem, QListWidget, QPushButton, QMenu,
    QFormLayout, QTextEdit, QMessageBox, QTreeWidgetItem, QFileDialog, QSpinBox
)
from openpyxl.utils import get_column_letter
class MaterialDialog(QDialog):
    def __init__(self, pitem, absolute_path=None, note=None):
        super().__init__()
        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")
        self.absolute_path = pitem.data(0, Qt.UserRole)
        self.pitem = pitem
        self.note = note
        self.setWindowTitle("编辑材料")
        self.setFixedSize(700, 800)
        # 主布局
        layout = QVBoxLayout()

        # 名称和类型
        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.type_combo = QLineEdit()
        type = pitem.text(0)
        self.type_combo.setText(type)
        form_layout.addRow(QLabel("名称:"), self.name_input)
        form_layout.addRow(QLabel("类型:"), self.type_combo)
        # 创建 QLabel 并将其文本设置为 QComboBox 的当前值

        # 添加到布局中
        layout.addLayout(form_layout)

        # 材料成分
        self.composition_table = QTableWidget(2, 10)
        self.composition_table.setVerticalHeaderLabels(["元素", "Wt.%"])
        layout.addWidget(QLabel("材料成分"))
        layout.addWidget(self.composition_table)

        # 材料属性列表
        self.property_list = QListWidget()
        self.property_list.addItems([
            "密度", "比热", "热导率", "电阻率", "热膨胀系数", "潜热", "弹性", "塑性"
        ])
        # 属性及其单位
        self.property_units = {
            "密度": "kg/m³",
            "比热": "J/g/K",
            "热导率": "W/m/K",
            "电阻率": "Ω∗m",
            "热膨胀系数": "1/K"
        }
        # 创建一个字典来存储每个属性对应的温度表
        self.temp_tables = {}
        for property_name in self.property_list.findItems("*", Qt.MatchWildcard):
            name = property_name.text()

            if name == "潜热":
                temp_table = QTableWidget(10, 3)
                temp_table.setHorizontalHeaderLabels(["潜热（J/kg）", "固相温度(K)", "液相温度（K）"])
                # Optional: You can populate the table with initial values if needed
                for row in range(10):
                    temp_table.setItem(row, 0, QTableWidgetItem(""))  # 示例潜热
                    temp_table.setItem(row, 1, QTableWidgetItem(""))  # 固相温度
                    temp_table.setItem(row, 2, QTableWidgetItem(""))  # 液相温度
                self.temp_tables[name] = temp_table

            elif name == "弹性":
                temp_table = QTableWidget(10, 2)
                temp_table.setHorizontalHeaderLabels(["弹性模量（MPa）", "泊松比"])
                for row in range(10):
                    temp_table.setItem(row, 0, QTableWidgetItem(""))  # 弹性模量
                    temp_table.setItem(row, 1, QTableWidgetItem(""))  # 泊松比
                self.temp_tables[name] = temp_table

            elif name == "塑性":
                temp_table = QTableWidget(10, 2)
                temp_table.setHorizontalHeaderLabels(["屈服应力（MPa）", "塑形应变"])
                for row in range(10):
                    temp_table.setItem(row, 0, QTableWidgetItem(""))  # 屈服应力
                    temp_table.setItem(row, 1, QTableWidgetItem(""))  # 塑形应变
                self.temp_tables[name] = temp_table
            else:
                unit = self.property_units[name]
                temp_table = QTableWidget(100, 2)
                temp_table.setHorizontalHeaderLabels(["温度 (K)", f"{unit}"])
                for row in range(100):
                    # Create QLineEdit for temperature
                    temp_line_edit = QLineEdit()
                    temp_validator = QDoubleValidator()  # Allow only double values
                    temp_line_edit.setValidator(temp_validator)

                    # Create QLineEdit for other attributes
                    other_line_edit = QLineEdit()

                    # Set QLineEdit as cell widget
                    temp_table.setCellWidget(row, 0, temp_line_edit)  # 温度 (K)
                    temp_table.setCellWidget(row, 1, other_line_edit)  # 其他属性值

                self.temp_tables[name] = temp_table

        # 默认显示第一个属性的温度表
        self.current_property = self.property_list.item(0).text()
        self.temp_table = self.temp_tables[self.current_property]
        if note=="edit":
            self.initdata()

        # 当选择材料属性时，更新对应的温度表
        self.property_list.currentItemChanged.connect(self.update_temp_table)

        layout.addWidget(QLabel("材料属性"))
        layout.addWidget(self.property_list)
        # layout.addLayout(btn_layout)

        # 温度和属性值表
        layout.addWidget(self.temp_table)

        # 确定和取消按钮
        button_layout = QHBoxLayout()
        ok_button = QPushButton("确定")
        cancel_button = QPushButton("取消")

        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        # 连接按钮功能
        ok_button.clicked.connect(lambda: self.accept(pitem))
        cancel_button.clicked.connect(self.reject)

    def accept(self, pitem):
        # 获取材料名称
        material_name = self.name_input.text()
        if not material_name:
            # 弹出提示框
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("请填写材料名称")
            msg_box.setWindowTitle("警告")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()  # 显示弹窗并等待用户点击
            return
        # 保存到 Excel 文件
        file_name = f"{self.absolute_path}/{material_name}.xlsx"
        if self.note == 'edit':
            file_name = self.absolute_path
        # 创建一个 DataFrame 来存储名称和类型
        name_type_df = pd.DataFrame({
            '名称': [material_name],
            '类型': [self.type_combo.text()]
        })

        # 保存 composition_table 到 sheet1
        composition_data = []
        for row in range(self.composition_table.rowCount()):
            row_data = []
            for col in range(self.composition_table.columnCount()):
                item = self.composition_table.item(row, col)
                row_data.append(item.text() if item else "")
            composition_data.append(row_data)

        # 转置数据
        composition_data = np.array(composition_data).T  # 使用 NumPy 进行转置

        # 创建 DataFrame
        composition_df = pd.DataFrame(composition_data, columns=["元素", "Wt.%"])

        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            # 保存名称和类型到 Excel
            name_type_df.to_excel(writer, sheet_name='名称-类型-成分', index=False, header=False)

            # 将 composition_df 的数据写入，从第三行开始
            composition_df.to_excel(writer, sheet_name='名称-类型-成分', index=False, startrow=3)

            # 获取工作表对象
            worksheet = writer.sheets['名称-类型-成分']
            fixed_width = 20  # 设定的列宽值
            # 遍历所有列并设置列宽
            for column in worksheet.columns:
                column_letter = get_column_letter(column[0].column)  # 获取列字母
                worksheet.column_dimensions[column_letter].width = fixed_width

            # 保存 temp_table 到 sheets
            for property_name in self.property_list.findItems("*", Qt.MatchWildcard):
                name = property_name.text()
                temp_data = []
                temp_table = self.temp_tables[name]

                for row in range(temp_table.rowCount()):
                    row_data = []
                    for col in range(temp_table.columnCount()):
                        if name in ["潜热", "弹性", "塑性"]:
                            item = temp_table.item(row, col)
                            row_data.append(item.text() if item else "")
                        else:
                            line_edit = temp_table.cellWidget(row, col)
                            row_data.append(line_edit.text() if line_edit is not None else "")

                    temp_data.append(row_data)

                # 为不同属性创建 DataFrame
                if name == "潜热":
                    temp_df = pd.DataFrame(temp_data, columns=["潜热（J/kg）", "固相温度(K)", "液相温度（K）"])
                elif name == "弹性":
                    temp_df = pd.DataFrame(temp_data, columns=["弹性模量（MPa）", "泊松比"])
                elif name == "塑性":
                    temp_df = pd.DataFrame(temp_data, columns=["屈服应力（MPa）", "塑形应变"])
                else:
                    unit = self.property_units[name]
                    temp_df = pd.DataFrame(temp_data, columns=["温度 (K)", f"{unit}"])

                temp_df.to_excel(writer, sheet_name=name, index=False)

        print(f"数据已保存到 {file_name}")
        message = f"数据已保存到 {file_name}"
        # 创建消息对话框
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("提示")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        # 显示消息对话框
        msg_box.exec_()
        # 新建item
        if self.note=='edit':
            pass
        else:
            new_item = QTreeWidgetItem(pitem)  # 只传入父项
            new_item.setText(0, material_name)
            new_item.setToolTip(0, osp.join(self.absolute_path, f'{material_name}.xlsx'))
            print(f'新建节点absolute_path：{self.absolute_path}')
            new_item.setData(0, Qt.UserRole, osp.join(self.absolute_path, f'{material_name}.xlsx'))
            new_item.setData(0, Qt.UserRole + 1, "具体材料")
            icon_path = osp.join('..', 'resource', 'icon', 'doc.png')
            new_item.setIcon(0, QIcon(icon_path))
        super().accept()  # 调用父类的 accept 方法以关闭对话框

    def initdata(self):

        # 加载 Excel 文件
        self.workbook = openpyxl.load_workbook(self.absolute_path)  # 替换为您的文件路径
        # 选择工作表
        sheet1 = self.workbook['名称-类型-成分']
        name = self.pitem.text(0)
        type = self.pitem.parent().text(0)

        self.name_input.setText(name)
        self.name_input.setReadOnly(True)  # 使材料名只读
        self.type_combo.setText(type)
        self.type_combo.setReadOnly(True)

        # 读取材料类型和成分并填入self.composition_table
        for row in range(5, 15):  # 从 A5 到 A14
            A = sheet1.cell(row=row, column=1).value  # 读取 A 列
            B = sheet1.cell(row=row, column=2).value  # 读取 B 列
            A_value = str(A) if A is not None else ''
            B_value = str(B) if B is not None else ''
            # 将数据填充到 QTableWidget
            self.composition_table.setItem(0, row - 5, QTableWidgetItem(A_value))  # 设置元素
            self.composition_table.setItem(1, row - 5, QTableWidgetItem(B_value))  # 设置 Wt.%

        sheets = {}
        for property_name in self.property_list.findItems("*", Qt.MatchWildcard):
            name = property_name.text()
            sheets[name] = self.workbook[name]  # 正确使用字典

            if name == "潜热":
                self.load_data_to_table(sheets[name], self.temp_tables[name], range(2, 12))
            elif name in ["弹性", "塑性"]:
                self.load_data_to_table(sheets[name], self.temp_tables[name], range(2, 12))
            else:
                for row in range(2, 102):
                    # A = sheets[name].cell(row=row, column=1).value
                    # B = sheets[name].cell(row=row, column=2).value
                    #
                    # self.temp_tables[name].setItem(row - 2, 0, QTableWidgetItem(A))
                    # self.temp_tables[name].setItem(row - 2, 1, QTableWidgetItem(B))

                    A = sheets[name].cell(row=row, column=1).value
                    B = sheets[name].cell(row=row, column=2).value

                    # 获取 QLineEdit 并设置其值
                    temp_line_edit = self.temp_tables[name].cellWidget(row - 2, 0)  # 获取温度的 QLineEdit
                    other_line_edit = self.temp_tables[name].cellWidget(row - 2, 1)  # 获取其他属性的 QLineEdit

                    if A is not None:
                        temp_line_edit.setText(str(A))  # 设置温度 (K)
                    if B is not None:
                        other_line_edit.setText(str(B))  # 设置其他属性值

    def load_data_to_table(self, sheet, temp_table, row_range):  # 添加 self 参数
        for row in row_range:
            A = sheet.cell(row=row, column=1).value
            B = sheet.cell(row=row, column=2).value

            A_value = str(A) if A is not None else ''
            B_value = str(B) if B is not None else ''

            temp_table.setItem(row - 2, 0, QTableWidgetItem(A_value))
            temp_table.setItem(row - 2, 1, QTableWidgetItem(B_value))

            # 对于潜热需要读取第三列
            if temp_table.columnCount() == 3:
                C = sheet.cell(row=row, column=3).value
                C_value = str(C) if C is not None else ''
                temp_table.setItem(row - 2, 2, QTableWidgetItem(C_value))

    def update_temp_table(self, current_item):
        if current_item:
            self.current_property = current_item.text()
            # 更新显示的 temp_table
            self.layout().itemAt(5).widget().setParent(None)  # 移除旧的temp_table
            self.temp_table = self.temp_tables[self.current_property]
            self.layout().insertWidget(5, self.temp_table)  # 在相同位置添加新的temp_table

class EquipmentDialog(QDialog):
    def __init__(self, item):
        super().__init__()
        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")
        self.item = item
        self.path = item.data(0, Qt.UserRole)
        self.setWindowTitle("编辑设备")
        self.setFixedSize(600, 600)

        # 主布局
        layout = QVBoxLayout()

        # 名称和类型
        name_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setText(item.text(0))
        self.name_input.setReadOnly(True)
        self.type_combo = QLineEdit()
        self.type_combo.setText(item.parent().text(0))
        self.type_combo.setReadOnly(True)

        name_layout.addWidget(QLabel("名称:"))
        name_layout.addWidget(self.name_input)
        name_layout.addWidget(QLabel("类型:"))
        name_layout.addWidget(self.type_combo)
        layout.addLayout(name_layout)

        # 设备描述
        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("设备描述")
        layout.addWidget(QLabel("设备描述:"))
        layout.addWidget(self.description_input)

        # 设备照片管理
        layout.addWidget(QLabel("设备照片:"))
        self.image_list = QListWidget()
        layout.addWidget(self.image_list)

        image_button_layout = QHBoxLayout()
        add_image_button = QPushButton("添加")
        remove_image_button = QPushButton("删除")
        image_button_layout.addWidget(add_image_button)
        image_button_layout.addWidget(remove_image_button)
        layout.addLayout(image_button_layout)

        # 设备文件管理
        layout.addWidget(QLabel("设备文件:"))
        self.file_list = QListWidget()
        layout.addWidget(self.file_list)

        file_button_layout = QHBoxLayout()
        add_file_button = QPushButton("添加")
        remove_file_button = QPushButton("删除")
        file_button_layout.addWidget(add_file_button)
        file_button_layout.addWidget(remove_file_button)
        layout.addLayout(file_button_layout)

        # 确定和取消按钮
        button_layout = QHBoxLayout()
        ok_button = QPushButton("确定")
        cancel_button = QPushButton("取消")
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        # 按钮功能（示例）
        add_image_button.clicked.connect(self.add_image)
        remove_image_button.clicked.connect(self.remove_image)
        add_file_button.clicked.connect(self.add_file)
        remove_file_button.clicked.connect(self.remove_file)
        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.initData()

    def initData(self):
        filepath = osp.join(self.item.data(0, Qt.UserRole), self.name_input.text())
        filepath = f"{filepath}.txt"  # 添加文件扩展名
        # 确保文件存在
        if not osp.exists(filepath):
            QMessageBox.warning(self, "警告", f"文件 {filepath} 不存在")
            return
        try:
            # 以读模式打开文件并读取内容
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()  # 读取文件内容
            # 将内容设置到 QTextEdit
            self.description_input.setPlainText(content)  # 使用 setPlainText()方法
        except Exception as e:
            QMessageBox.critical(self, "错误", f"无法读取文件: {e}")
        tu_dir = osp.join(self.item.data(0, Qt.UserRole), '设备图片')
        # 列出目录下的所有文件
        try:
            for filename in os.listdir(tu_dir):
                # 过滤出图片文件（根据扩展名）
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    self.image_list.addItem(filename)  # 添加文件名到 QListWidget
        except Exception as e:
            QMessageBox.critical(self, "错误", f"无法加载图片: {e}")
        wen_dir = osp.join(self.item.data(0, Qt.UserRole), '设备文件')
        # 列出目录下的所有文件
        try:
            for filename in os.listdir(wen_dir):
                # 过滤出pdf文件（根据扩展名）
                if filename.lower().endswith(('.pdf', '.txt', '.doc', '.docx')):
                    self.file_list.addItem(filename)  # 添加文件名到 QListWidget
        except Exception as e:
            QMessageBox.critical(self, "错误", f"无法加载文件: {e}")

    def accept(self):
        description = self.description_input.toPlainText()
        file = osp.join(self.item.data(0, Qt.UserRole), self.name_input.text())
        filepath = f"{file}.txt"  # 添加文件扩展名
        try:
            with open(filepath, 'w', encoding='utf-8') as file:  # 以写入模式打开文件
                file.write(description)  # 将描述写入文件
            QMessageBox.information(self, '成功', f'描述已保存到 {filepath}')
        except Exception as e:
            QMessageBox.critical(self, '错误', f'无法保存文件: {e}')
        tu_dir = osp.join(self.item.data(0, Qt.UserRole), '设备图片')
        wen_dir = osp.join(self.item.data(0, Qt.UserRole), '设备文件')
        # 遍历 QListWidget 中的所有项
        for index in range(self.image_list.count()):
            item = self.image_list.item(index)  # 获取 QListWidget 中的项
            image_filename = item.text()  # 获取文件名
            # 检查文件路径是否为绝对路径
            if not os.path.isabs(image_filename):
                pass
            else:
                try:
                    # 复制文件到目标目录
                    shutil.copy(image_filename, tu_dir)
                except Exception as e:
                    QMessageBox.critical(self, "错误", f"无法复制文件 {image_filename}: {e}")
        # 遍历 QListWidget 中的所有项
        for index in range(self.file_list.count()):
            item = self.file_list.item(index)  # 获取 QListWidget 中的项
            image_filename = item.text()  # 获取文件名
            # 检查文件路径是否为绝对路径
            if not os.path.isabs(image_filename):
                pass
            else:
                try:
                    # 复制文件到目标目录
                    shutil.copy(image_filename, wen_dir)
                except Exception as e:
                    QMessageBox.critical(self, "错误", f"无法复制文件 {image_filename}: {e}")

        super().accept()

    def add_image(self):
        # 打开文件对话框选择图片文件
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "选择图片文件", "",
                                                "Image Files (*.png *.jpg *.jpeg);;All Files (*)",
                                                options=options)
        if files:  # 如果用户选择了文件
            for file in files:
                self.image_list.addItem(file)  # 将文件路径添加到 QListWidget

    def remove_image(self):
        # 获取选中的项并删除
        selected_items = self.image_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "警告", "请先选择要删除的项目")
            return

        for item in selected_items:
            self.image_list.takeItem(self.image_list.row(item))  # 从列表中删除选中的项
    def add_file(self):
        # 打开文件对话框选择文件
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "选择文件", "",
                                                "Image Files (*.pdf *.txt *.doc *.docx);;All Files (*)",
                                                options=options)

        if files:  # 如果用户选择了文件
            for file in files:
                self.file_list.addItem(file)  # 将文件路径添加到 QListWidget

    def remove_file(self):
        # 获取选中的项并删除
        selected_items = self.file_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "警告", "请先选择要删除的项目")
            return

        for item in selected_items:
            self.file_list.takeItem(self.file_list.row(item))  # 从列表中删除选中的项

class ProcessDialog(QDialog):
    def __init__(self, item):
        super().__init__()
        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")
        self.setWindowTitle("编辑工艺")
        self.path = item.data(0, Qt.UserRole)

        # 创建布局
        main_layout = QVBoxLayout()

        # 创建左侧表单布局
        self.left_form_layout = QFormLayout()
        self.fuel_material_combo = QComboBox()
        self.fuel_material_combo.addItems(["材料1", "材料2", "材料3"])

        # 添加左侧表单项
        self.power_input = QLineEdit()
        self.power_input.setObjectName("激光功率 (W):")

        self.left_form_layout.addRow(QLabel("燃料材料:"), self.fuel_material_combo)
        self.left_form_layout.addRow(QLabel("激光功率 (W):"), self.power_input)
        self.left_form_layout.addRow(QLabel("送粉转速 (r/min):"), self.create_line_edit("送粉转速 (r/min):"))
        self.left_form_layout.addRow(QLabel("光束电压 (V):"), self.create_line_edit("光束电压 (V):"))
        self.left_form_layout.addRow(QLabel("道间隔 (s):"), self.create_line_edit("道间隔 (s):"))
        self.left_form_layout.addRow(QLabel("道间偏移 (mm):"), self.create_line_edit("道间偏移 (mm):"))
        self.left_form_layout.addRow(QLabel("保护气及流量 (L/min):"), self.create_line_edit("保护气及流量 (L/min):"))

        # 创建右侧表单布局
        self.right_form_layout = QFormLayout()
        self.base_material_combo = QComboBox()
        self.base_material_combo.addItems(["基板1", "基板2", "基板3"])

        # 添加右侧表单项
        self.right_form_layout.addRow(QLabel("基板材料:"), self.base_material_combo)
        self.right_form_layout.addRow(QLabel("熔覆速度 (mm/s):"), self.create_line_edit("熔覆速度 (mm/s):"))
        self.right_form_layout.addRow(QLabel("质量添加 (g/min):"), self.create_line_edit("质量添加 (g/min):"))
        self.right_form_layout.addRow(QLabel("光斑直径 (mm):"), self.create_line_edit("光斑直径 (mm):"))
        self.right_form_layout.addRow(QLabel("层间隔 (s):"), self.create_line_edit("层间隔 (s):"))
        self.right_form_layout.addRow(QLabel("层间提升 (mm):"), self.create_line_edit("层间提升 (mm):"))
        self.right_form_layout.addRow(QLabel("载气及流量 (L/min):"), self.create_line_edit("载气及流量 (L/min):"))

        # 将左右表单布局放入一个水平布局中
        central_layout = QHBoxLayout()
        central_layout.addLayout(self.left_form_layout)
        central_layout.addLayout(self.right_form_layout)

        main_layout.addLayout(central_layout)

        # 添加确认和取消按钮
        button_layout = QHBoxLayout()
        confirm_button = QPushButton("确认")
        cancel_button = QPushButton("取消")

        button_layout.addWidget(confirm_button)
        button_layout.addWidget(cancel_button)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # 连接信号
        confirm_button.clicked.connect(self.save_to_excel)
        cancel_button.clicked.connect(self.reject)
        self.initData()

    def create_line_edit(self, placeholder):
        line_edit = QLineEdit()
        line_edit.setObjectName(placeholder)
        return line_edit

    def initData(self):
        # 读取 Excel 文件
        df = pd.read_excel(self.path, sheet_name='Sheet')

        # 删除空行
        df = df.dropna(how='all')

        # 检查行数
        if df.shape[0] >= 3:  # 确保有足够的行
            row_2 = df.iloc[0].tolist()  # A2-G2
            row_4 = df.iloc[2].tolist()  # A4-G4

            # 填充左侧表单
            self.fuel_material_combo.setCurrentText(row_2[0])  # 燃料材料
            self.power_input.setText(str(row_2[1]))  # 激光功率
            self.left_form_layout.itemAt(5).widget().setText(str(row_2[2]))  # 送粉转速
            self.left_form_layout.itemAt(7).widget().setText(str(row_2[3]))  # 光束电压
            self.left_form_layout.itemAt(9).widget().setText(str(row_2[4]))  # 道间隔
            self.left_form_layout.itemAt(11).widget().setText(str(row_2[5]))  # 道间偏移
            self.left_form_layout.itemAt(13).widget().setText(str(row_2[6]))  # 保护气及流量

            # 填充右侧表单
            self.base_material_combo.setCurrentText(row_4[0])  # 基板材料
            self.right_form_layout.itemAt(3).widget().setText(str(row_4[1]))  # 熔覆速度
            self.right_form_layout.itemAt(5).widget().setText(str(row_4[2]))  # 质量添加
            self.right_form_layout.itemAt(7).widget().setText(str(row_4[3]))  # 光斑直径
            self.right_form_layout.itemAt(9).widget().setText(str(row_4[4]))  # 层间隔
            self.right_form_layout.itemAt(11).widget().setText(str(row_4[5]))  # 层间提升
            self.right_form_layout.itemAt(13).widget().setText(str(row_4[6]))  # 载气及流量
        else:
            print("数据行数不足，无法填充表单。")
    def save_to_excel(self):
        data1 = {
            "燃料材料": [self.fuel_material_combo.currentText()],
            "激光功率（W）": [self.findChild(QLineEdit, "激光功率 (W):").text()],
            "送粉转速（r/min）": [self.findChild(QLineEdit, "送粉转速 (r/min):").text()],
            "光束电压（V）": [self.findChild(QLineEdit, "光束电压 (V):").text()],
            "道间隔（s）": [self.findChild(QLineEdit, "道间隔 (s):").text()],
            "道间偏移（mm）": [self.findChild(QLineEdit, "道间偏移 (mm):").text()],
            "保护气及流量（L/min）": [self.findChild(QLineEdit, "保护气及流量 (L/min):").text()],
        }
        data2 = {
            "基板材料": [self.base_material_combo.currentText()],
            "熔覆速度（mm/s）": [self.findChild(QLineEdit, "熔覆速度 (mm/s):").text()],
            "质量添加（g/min）": [self.findChild(QLineEdit, "质量添加 (g/min):").text()],
            "光斑直径（mm）": [self.findChild(QLineEdit, "光斑直径 (mm):").text()],
            "层间隔（s）": [self.findChild(QLineEdit, "层间隔 (s):").text()],
            "层间提升（mm）": [self.findChild(QLineEdit, "层间提升 (mm):").text()],
            "载气及流量（L/min）": [self.findChild(QLineEdit, "载气及流量 (L/min):").text()],
        }

        # 创建ExcelWriter对象
        with pd.ExcelWriter(self.path, engine='openpyxl') as writer:
            df1 = pd.DataFrame(data1)
            df1.to_excel(writer, index=False, sheet_name='Sheet')
            df2 = pd.DataFrame(data2)
            # 写入第二个数据框，从第一个数据框的行数开始
            df2.to_excel(writer, index=False, header=True, startrow=len(df1) + 1, sheet_name='Sheet')
            # 获取工作表对象,调整列宽以适应内容
            worksheet = writer.sheets['Sheet']
            # 假设您要设置的列宽
            fixed_width = 25  # 设定的列宽值
            # 遍历所有列并设置列宽
            for column in worksheet.columns:
                column_letter = get_column_letter(column[0].column)  # 获取列字母
                worksheet.column_dimensions[column_letter].width = fixed_width
        self.accept()

class EditDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")
        self.setWindowTitle("编辑程序")
        self.setGeometry(100, 100, 400, 600)

        # 创建控件
        self.type_label = QtWidgets.QLabel("类型")
        self.type_combobox = QtWidgets.QComboBox()
        self.type_combobox.addItems(["选项1", "选项2"])  # 示例选项

        self.path_count_label = QtWidgets.QLabel("道数")
        self.path_count_input = QtWidgets.QLineEdit()

        self.layer_count_label = QtWidgets.QLabel("层数")
        self.layer_count_input = QtWidgets.QLineEdit()

        self.laser_power_label = QtWidgets.QLabel("激光功率")
        self.laser_power_input = QtWidgets.QLineEdit()

        self.overlay_speed_label = QtWidgets.QLabel("熔覆速度")
        self.overlay_speed_input = QtWidgets.QLineEdit()

        self.voltage_label = QtWidgets.QLabel("光斑电压")
        self.voltage_input = QtWidgets.QLineEdit()

        self.sampling_speed_label = QtWidgets.QLabel("送粉转速")
        self.sampling_speed_input = QtWidgets.QLineEdit()

        self.offset_distance_label = QtWidgets.QLabel("偏移距离")
        self.offset_distance_input = QtWidgets.QLineEdit()

        self.program_files_label = QtWidgets.QLabel("程序文件")
        self.program_files_list = QtWidgets.QListWidget()

        self.add_button = QtWidgets.QPushButton("添加")
        self.add_button.clicked.connect(self.add_file)

        self.remove_button = QtWidgets.QPushButton("删除")
        self.remove_button.clicked.connect(self.remove_file)

        self.ok_button = QtWidgets.QPushButton("确定")
        self.cancel_button = QtWidgets.QPushButton("取消")

        # 布局
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.type_label, 0, 0)
        layout.addWidget(self.type_combobox, 0, 1)

        layout.addWidget(self.path_count_label, 1, 0)
        layout.addWidget(self.path_count_input, 1, 1)

        layout.addWidget(self.layer_count_label, 2, 0)
        layout.addWidget(self.layer_count_input, 2, 1)

        layout.addWidget(self.laser_power_label, 3, 0)
        layout.addWidget(self.laser_power_input, 3, 1)

        layout.addWidget(self.overlay_speed_label, 4, 0)
        layout.addWidget(self.overlay_speed_input, 4, 1)

        layout.addWidget(self.voltage_label, 5, 0)
        layout.addWidget(self.voltage_input, 5, 1)

        layout.addWidget(self.sampling_speed_label, 6, 0)
        layout.addWidget(self.sampling_speed_input, 6, 1)

        layout.addWidget(self.offset_distance_label, 7, 0)
        layout.addWidget(self.offset_distance_input, 7, 1)

        layout.addWidget(self.program_files_label, 8, 0, 1, 2)
        layout.addWidget(self.program_files_list, 9, 0, 1, 2)

        layout.addWidget(self.add_button, 10, 0)
        layout.addWidget(self.remove_button, 10, 1)

        layout.addWidget(self.ok_button, 11, 0)
        layout.addWidget(self.cancel_button, 11, 1)

        self.setLayout(layout)

    def add_file(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", "", "所有文件 (*)")
        if filename:
            self.program_files_list.addItem(filename)

    def remove_file(self):
        selected_items = self.program_files_list.selectedItems()
        for item in selected_items:
            self.program_files_list.takeItem(self.program_files_list.row(item))

class EditProgramDialog(QDialog):
    def __init__(self, item):
        super().__init__()
        self.setWindowTitle("编辑程序")
        # 设置对话框的固定宽度和高度
        self.setFixedSize(600, 600)  # 设置宽度为400，高度为300
        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")

        self.item = item
        self.path = item.data(0, Qt.UserRole)

        # 创建布局
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # 输入字段
        self.name = QLineEdit()
        form_layout.addRow("名称", self.name)
        self.type_combo = QLineEdit()
        self.type_combo.setText(item.text(0))
        # 设置为只读，防止修改
        self.type_combo.setReadOnly(True)
        form_layout.addRow("类型", self.type_combo)

        self.path_count_edit = QLineEdit()
        form_layout.addRow("道数", self.path_count_edit)

        self.layer_count_edit = QLineEdit()
        form_layout.addRow("层数", self.layer_count_edit)

        self.laser_power_edit = QLineEdit()
        form_layout.addRow("激光功率(W)", self.laser_power_edit)

        self.melting_speed_edit = QLineEdit()
        form_layout.addRow("熔融速度(mm/s)", self.melting_speed_edit)

        self.light_press_edit = QLineEdit()
        form_layout.addRow("光斑电压(V)", self.light_press_edit)

        self.convey_speed_edit = QLineEdit()
        form_layout.addRow("送粉转速(r/min)", self.convey_speed_edit)

        self.offset_height_edit = QLineEdit()
        form_layout.addRow("偏移高度", self.offset_height_edit)

        layout.addLayout(form_layout)

        # 程序文件列表
        self.file_list = QListWidget()
        layout.addWidget(self.file_list)

        # 添加和删除按钮
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("添加")
        self.remove_button = QPushButton("删除")
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.remove_button)
        layout.addLayout(button_layout)

        # 确定和取消按钮
        self.ok_button = QPushButton("确定")
        self.cancel_button = QPushButton("取消")
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        # 设置主布局
        self.setLayout(layout)

        # 连接信号
        self.add_button.clicked.connect(self.add_file)
        self.remove_button.clicked.connect(self.remove_file)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def add_file(self):
        # 打开文件对话框选择文件
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "选择文件", "",
                                                "Image Files (*.src *.txt *.json);;All Files (*)",
                                                options=options)

        if files:  # 如果用户选择了文件
            for file in files:
                self.file_list.addItem(file)  # 将文件路径添加到 QListWidget

    def remove_file(self):
        # 在这里处理删除文件逻辑
        selected_items = self.file_list.selectedItems()
        for item in selected_items:
            self.file_list.takeItem(self.file_list.row(item))
    def accept(self):
        description = self.description_input.toPlainText()
        file = osp.join(self.item.data(0, Qt.UserRole), self.name_input.text())
        filepath = f"{file}.txt"  # 添加文件扩展名
        try:
            with open(filepath, 'w', encoding='utf-8') as file:  # 以写入模式打开文件
                file.write(description)  # 将描述写入文件
            QMessageBox.information(self, '成功', f'描述已保存到 {filepath}')
        except Exception as e:
            QMessageBox.critical(self, '错误', f'无法保存文件: {e}')
        tu_dir = osp.join(self.item.data(0, Qt.UserRole), '设备图片')
        wen_dir = osp.join(self.item.data(0, Qt.UserRole), '设备文件')
        # 遍历 QListWidget 中的所有项
        for index in range(self.image_list.count()):
            item = self.image_list.item(index)  # 获取 QListWidget 中的项
            image_filename = item.text()  # 获取文件名
            # 检查文件路径是否为绝对路径
            if not os.path.isabs(image_filename):
                pass
            else:
                try:
                    # 复制文件到目标目录
                    shutil.copy(image_filename, tu_dir)
                except Exception as e:
                    QMessageBox.critical(self, "错误", f"无法复制文件 {image_filename}: {e}")
        # 遍历 QListWidget 中的所有项
        for index in range(self.file_list.count()):
            item = self.file_list.item(index)  # 获取 QListWidget 中的项
            image_filename = item.text()  # 获取文件名
            # 检查文件路径是否为绝对路径
            if not os.path.isabs(image_filename):
                pass
            else:
                try:
                    # 复制文件到目标目录
                    shutil.copy(image_filename, wen_dir)
                except Exception as e:
                    QMessageBox.critical(self, "错误", f"无法复制文件 {image_filename}: {e}")

        super().accept()
class EditModelDialog(QDialog):
    def __init__(self, item):
        super().__init__()
        self.setWindowTitle("编辑程序")
        # 设置对话框的固定宽度和高度
        self.setFixedSize(600, 600)  # 设置宽度为400，高度为300
        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")
        self.setWindowTitle("编辑模型")

        # 创建主布局
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # 创建输入字段
        self.name_edit = QLineEdit()
        form_layout.addRow("名称", self.name_edit)

        self.type_combo = QLineEdit()
        self.type_combo.setText(item.text(0))
        # 设置为只读，防止修改
        self.type_combo.setReadOnly(True)
        form_layout.addRow("类型", self.type_combo)

        self.material_edit = QLineEdit()
        form_layout.addRow("熔覆材料", self.material_edit)

        self.base_material_combo = QComboBox()
        self.base_material_combo.addItems(["基板材料1", "基板材料2"])
        form_layout.addRow("基板材料", self.base_material_combo)

        self.laser_efficiency_edit = QLineEdit()
        form_layout.addRow("激光功率(W)", self.laser_efficiency_edit)

        self.melting_speed_edit = QLineEdit()
        form_layout.addRow("熔覆速度(mm/s)", self.melting_speed_edit)

        self.melting_shape_edit = QLineEdit()
        form_layout.addRow("熔覆形式", self.melting_shape_edit)

        self.initial_condition_edit = QLineEdit()
        form_layout.addRow("初始条件", self.initial_condition_edit)

        self.boundary_condition_edit = QLineEdit()
        form_layout.addRow("边界条件", self.boundary_condition_edit)

        layout.addLayout(form_layout)

        # 模型文件列表
        self.file_list = QListWidget()
        layout.addWidget(QLabel("模型文件"))
        layout.addWidget(self.file_list)

        # 添加和删除按钮
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("添加")
        self.remove_button = QPushButton("删除")
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.remove_button)
        layout.addLayout(button_layout)

        # 确定和取消按钮
        self.ok_button = QPushButton("确定")
        self.cancel_button = QPushButton("取消")
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        # 设置主布局
        self.setLayout(layout)

        # 连接信号
        self.add_button.clicked.connect(self.add_file)
        self.remove_button.clicked.connect(self.remove_file)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    # 在这里处理添加文件逻辑
    def add_file(self):
        # 打开文件对话框选择文件
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "选择文件", "",
                                                "Image Files (*.src *.txt *.json);;All Files (*)",
                                                options=options)

        if files:  # 如果用户选择了文件
            for file in files:
                self.file_list.addItem(file)  # 将文件路径添加到 QListWidget

    def remove_file(self):
        # 在这里处理删除文件逻辑
        selected_items = self.file_list.selectedItems()
        for item in selected_items:
            self.file_list.takeItem(self.file_list.row(item))

class FilterCX(QDialog):
    def __init__(self, item):
        super().__init__()

        self.data = self.load_data_from_json('E:\\xiangmu\\qinghua\\THU_S\\database\\数据库\\程序库\\程序目录.json')  # 假设您的 JSON 文件名为 data.json
        self.path = item.data(0, Qt.UserRole)
        # 创建 UI 组件
        self.table_cx = QTableWidget()
        self.table_cx.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_cx.customContextMenuRequested.connect(self.show_context_menu)
        #类型
        self.filter_type = QComboBox()
        self.filter_type.addItems(["全部", "单层", "单道", "多层"])
        #道数
        self.filter_dao_min = QSpinBox()
        self.filter_dao_min.setRange(1, 10)
        self.filter_dao_max = QSpinBox()
        self.filter_dao_max.setRange(1, 10)
        #层数
        self.filter_layer_min = QSpinBox()
        self.filter_layer_min.setRange(1, 10)
        self.filter_layer_max = QSpinBox()
        self.filter_layer_max.setRange(1, 10)
        #功率
        self.filter_power_min = QSpinBox()
        self.filter_power_min.setRange(0, 10000)
        self.filter_power_max = QSpinBox()
        self.filter_power_max.setRange(0, 10000)
        #熔覆速度
        self.filter_rfsd_min = QSpinBox()
        self.filter_rfsd_min.setRange(0, 1000)
        self.filter_rfsd_max = QSpinBox()
        self.filter_rfsd_max.setRange(0, 1000)

        filter_button = QPushButton("筛选")
        filter_button.clicked.connect(self.apply_filter)

        # 布局设置
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("类型:"))
        filter_layout.addWidget(self.filter_type)

        filter_layout.addWidget(QLabel("道数:"))
        filter_layout.addWidget(self.filter_dao_min)
        filter_layout.addWidget(QLabel("到"))
        filter_layout.addWidget(self.filter_dao_max)

        filter_layout.addWidget(QLabel("层数:"))
        filter_layout.addWidget(self.filter_layer_min)
        filter_layout.addWidget(QLabel("到"))
        filter_layout.addWidget(self.filter_layer_max)

        filter_layout.addWidget(QLabel("激光功率:"))
        filter_layout.addWidget(self.filter_power_min)
        filter_layout.addWidget(QLabel("到"))
        filter_layout.addWidget(self.filter_power_max)

        filter_layout.addWidget(QLabel("熔覆速度:"))
        filter_layout.addWidget(self.filter_rfsd_min)
        filter_layout.addWidget(QLabel("到"))
        filter_layout.addWidget(self.filter_rfsd_max)


        filter_layout.addWidget(filter_button)

        layout = QVBoxLayout()
        layout.addLayout(filter_layout)
        layout.addWidget(self.table_cx)
        self.setLayout(layout)

        # 初始化表格
        self.populate_table(self.data)

        # 设置窗口标题和大小
        self.setWindowTitle("数据筛选程序")
        self.resize(800, 600)

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

    def load_data_from_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def populate_table(self, data):
        self.table_cx.setRowCount(len(data))
        self.table_cx.setColumnCount(len(data[0]))
        self.table_cx.setHorizontalHeaderLabels(data[0].keys())

        for row_index, row_data in enumerate(data):
            for col_index, (key, value) in enumerate(row_data.items()):
                self.table_cx.setItem(row_index, col_index, QTableWidgetItem(str(value)))

    def apply_filter(self):

        type_filter = self.filter_type.currentText()
        layer_min = self.filter_layer_min.value()
        layer_max = self.filter_layer_max.value()

        dao_min = self.filter_dao_min.value()
        dao_max = self.filter_dao_max.value()

        power_min = self.filter_power_min.value()
        power_max = self.filter_power_max.value()

        rfsd_min = self.filter_rfsd_min.value()
        rfsd_max = self.filter_rfsd_max.value()

        filtered_data = []

        for item in self.data:
            type_matches = (type_filter == "全部" or item["类型"] == type_filter)
            dao_matches = (dao_min <= item["道数"] <= dao_max)
            layer_matches = (layer_min <= item["层数"] <= layer_max)
            power_matches = (power_min <= item["激光功率(W)"] <= power_max)
            rfsd_matches = (rfsd_min <= item["熔覆速度(mm/s)"] <= rfsd_max)

            if dao_matches and type_matches and layer_matches and power_matches and rfsd_matches:
                filtered_data.append(item)

        self.populate_table(filtered_data)

class FilterMX(QDialog):
    def __init__(self, item):
        super().__init__()

        self.data = self.load_data_from_json('E:\\xiangmu\\qinghua\\THU_S\\database\\数据库\\模型库\\模型目录.json')  # 假设您的 JSON 文件名为 data.json
        # 创建 UI 组件
        self.table_cx = QTableWidget()

        # 创建筛选器组件
        self.filter_type = QComboBox()
        self.filter_type.addItem("全部")
        self.filter_type.addItem("单道")  # 其他类型可以根据需要添加

        self.filter_material = QLineEdit()
        self.filter_substrate = QLineEdit()
        self.filter_speed_min = QSpinBox()
        self.filter_speed_min.setRange(0, 100)
        self.filter_speed_max = QSpinBox()
        self.filter_speed_max.setRange(0, 100)

        filter_button = QPushButton("筛选")
        filter_button.clicked.connect(self.apply_filter)

        # 布局设置
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("类型:"))
        filter_layout.addWidget(self.filter_type)
        filter_layout.addWidget(QLabel("熔覆材料:"))
        filter_layout.addWidget(self.filter_material)
        filter_layout.addWidget(QLabel("基板材料:"))
        filter_layout.addWidget(self.filter_substrate)
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

    def load_data_from_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def populate_table(self, data):
        self.table_cx.setRowCount(len(data))
        self.table_cx.setColumnCount(len(data[0]))
        self.table_cx.setHorizontalHeaderLabels(data[0].keys())

        for row_index, row_data in enumerate(data):
            for col_index, (key, value) in enumerate(row_data.items()):
                self.table_cx.setItem(row_index, col_index, QTableWidgetItem(str(value)))

    def apply_filter(self):
        type_filter = self.filter_type.currentText()
        material_filter = self.filter_material.text().strip().lower()
        substrate_filter = self.filter_substrate.text().strip().lower()
        speed_min = self.filter_speed_min.value()
        speed_max = self.filter_speed_max.value()

        filtered_data = []

        for item in self.data:
            type_matches = (type_filter == "全部" or item["类型"] == type_filter)
            material_matches = material_filter in item["熔覆材料"].lower()
            substrate_matches = substrate_filter in item["基板材料"].lower()
            speed_matches = (speed_min <= item["熔覆速度(mm/s)"] <= speed_max)

            if type_matches and material_matches and substrate_matches and speed_matches:
                filtered_data.append(item)

        self.populate_table(filtered_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = FilterMX('55')
    if dialog.exec_() == QDialog.Accepted:
        # 处理确认后的逻辑
        print("对话框确认")
    sys.exit(app.exec_())