#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 16:01
# @Author  : mihudan~
# @File    : dropout_reflect.py
# @Description :
# 自定义的最上层的QToolBox控件

from PySide2.QtWidgets import *
import sys
from .QToolpage import QToolpage


class MyQToolBox(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(2)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch(1)

        # self.setMinimumSize(400,200)

    def addWidget(self, title, widget):
        page = QToolpage(self)
        page.addWidget(title, widget)
        self.layout.addWidget(page)


class MyQToolBox_raw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.layout = QVBoxLayout(self)
        # self.setMinimumSize(400,200)

        self.widget = QWidget(self)

        self.ContentLayout = QVBoxLayout()
        self.ContentLayout.setSpacing(2)
        self.ContentLayout.setContentsMargins(0, 0, 0, 0)

        self.scrollLayout = QVBoxLayout(self.widget)
        self.scrollLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollLayout.addLayout(self.ContentLayout)
        self.scrollLayout.addStretch(1)

        self.scrollarea = QScrollArea(self)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setWidget(self.widget)
        self.layout.addWidget(self.scrollarea)

    def addWidget(self, title, widget):
        page = QToolpage(self)
        page.addWidget(title, widget)
        self.ContentLayout.addWidget(page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QToolBox()
    window.show()
    sys.exit(app.exec_())
