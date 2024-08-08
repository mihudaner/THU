#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/26 16:29
# @Author  : mihudan~
# @File    : project.py
# @Description :
from PySide2.QtWidgets import *  # 不止这一个外部库，其它的库我在需要用到时单独引入
from PySide2.QtCore import Signal

from .projectpage_ui import Ui_ProjectPage


# D:\\soft\\Anaconda\\envs\\py37\\Scripts\\pyside2-uic -o  projectpage_ui.py projectpage.ui

# from QTui.boot_mainwindow import MainWindow
#
#
# class InitProjectPage(MainWindow):
#
#     def Init(self):
#         print("InitProjectPage")
#         self.ui.projectpage = ProjectPage()
#         self.ui.horizontalLayout_33.addWidget(self.ui.projectpage)
#         pass


class ProjectPage(QWidget):
    def __init__(self):
        super(ProjectPage, self).__init__()

        # 创建一个滚动区域
        self.initUI()  # 初始化窗口
        self.initConnect()
        self.resize(1800, 1000)

    def initConnect(self):
        self.widgets.btn_create.clicked.connect(self.widgets.ProjectScrollArea.add_card)
        self.widgets.btn_save.clicked.connect(self.widgets.ProjectScrollArea.manager.save_project)

    def initUI(self):
        self.ui = Ui_ProjectPage()
        self.ui.setupUi(self)
        self.widgets = self.ui


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = ProjectPage()
    window.show()
    sys.exit(app.exec_())
