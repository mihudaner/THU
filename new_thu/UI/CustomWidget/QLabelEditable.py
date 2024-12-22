#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/8 14:36
# @Author  : mihudan~
# @File    : QLabelEditable
# @Description : 
from PySide2.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget
from PySide2.QtCore import Qt
import configparser

class EditableLabel(QLabel):
    def __init__(self, parent=None):
        """
        初始化 EditableLabel，自动根据 objectName 作为配置文件的 key 进行存储和读取
        :param parent: 父控件
        """
        super().__init__(parent)  # 初始化 QLabel

        self.edit = QLineEdit(self)
        self.edit.hide()
        self.edit.setAlignment(Qt.AlignCenter)

        # 监听编辑器完成事件
        self.edit.returnPressed.connect(self.finish_edit)

        # 设置 objectName，如果没有设置则自动为其设置一个默认值
        if not self.objectName():
            self.setObjectName(f"label_{id(self)}")  # 使用控件的唯一 ID 作为 objectName

        # 从配置文件加载文本
        self.load_text()

    def setText(self,text):
        text = self.load_text()
        super(EditableLabel, self).setText(text)

    def load_text(self):
        """从配置文件加载文本"""
        config = configparser.ConfigParser()
        config.read("config.ini")

        # 获取配置文件中的文本，如果没有则使用默认文本
        text = config.get("settings", self.objectName(), fallback=self.objectName())
        return text

    def save_text(self):
        """保存文本到配置文件"""
        config = configparser.ConfigParser()
        config.read("config.ini")

        # 如果 section 不存在，则创建
        if "settings" not in config.sections():
            config.add_section("settings")

        # 将文本保存到配置文件，使用 objectName 作为 key
        config.set("settings", self.objectName(), self.text())

        # 保存配置到文件
        with open("config.ini", 'w') as configfile:
            config.write(configfile)

    def mouseDoubleClickEvent(self, event):
        """双击事件切换到编辑模式"""
        self.edit.setText(self.text())  # 将 QLabel 的文本设置到 QLineEdit

        # 设置 QLineEdit 的大小和位置
        self.edit.setGeometry(self.rect())  # 与 QLabel 同大小
        self.edit.show()  # 显示 QLineEdit
        self.edit.setFocus()  # 聚焦到 QLineEdit

    def finish_edit(self):
        """完成编辑后更新 QLabel 的文本，并保存"""
        super(EditableLabel, self).setText(self.edit.text())  # 更新 QLabel 的文本
        self.edit.hide()  # 隐藏 QLineEdit
        self.save_text()  # 保存文本到配置文件


# 测试主窗口
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 创建自定义 QLabel
        self.label = EditableLabel("双击编辑我")
        self.label.setAlignment(Qt.AlignCenter)  # 可以使用 QLabel 的方法
        self.label.setStyleSheet("font-size: 18px; color: blue;")

        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setWindowTitle("可编辑 QLabel 示例")
        self.resize(3000, 1500)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

