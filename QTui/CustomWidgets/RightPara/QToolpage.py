#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 16:01
# @Author  : mihudan~
# @File    : dropout_reflect.py
# @Description :
# QToolPage，没有滑动区域，实现了一些添加控件和点击隐藏

import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from .toolpage_ui import Ui_Form


class QToolpage(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(
            """
            background-color: black;
            """
        )
        self.is_expand = False
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.pushButtonFlod.clicked.connect(self.btn_clicked)
        self.ui.widgetContent.hide()
        self.ui.widgetContent.setAttribute(Qt.WA_StyledBackground)
        self.ContentLayout = QVBoxLayout(self.ui.widgetContent)
        self.ContentLayout.setSpacing(2)
        self.ContentLayout.setContentsMargins(0, 0, 0, 0)
        self.ContentLayout.addStretch(1)

    def btn_clicked(self):
        if self.is_expand:
            self.ui.widgetContent.hide()
            self.is_expand = False
        else:
            self.ui.widgetContent.show()
            """self.anim = QPropertyAnimation(self.ui.widgetContent)
            self.anim.setTargetObject(self.ui.widgetContent)
            self.anim.setPropertyName(b"geometry")
            self.anim.setStartValue(QRect(0, 44, self.ui.pushButtonFlod.width(), 0))
            self.anim.setEndValue((QRect(0, 44, self.ui.pushButtonFlod.width(), self.ui.widgetContent.height())))
            self.anim.setDuration(150)
            self.anim.start()"""

            self.is_expand = True

    def addWidget(self, title, widget):
        self.ui.pushButtonFlod.setText(title)
        # self.ui.pushButtonFlod.setStyleSheet('text-align:center')
        self.ContentLayout.addWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QToolpage()
    window.show()
    sys.exit(app.exec_())
