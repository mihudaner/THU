#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 16:01
# @Author  : mihudan~
# @File    : dropout_reflect.py
# @Description :
# 由parabox的ui文件生成的py文件,含有曝光时间，增益，亮度曝光，的基本控件
# 在parabox_correct.py文件中添加自定义双浮点滑块

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(202, 145)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_1 = QVBoxLayout()
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.label_eps_time = QLabel(Form)
        self.label_eps_time.setObjectName(u"label_eps_time")

        self.horizontalLayout_1.addWidget(self.label_eps_time)

        self.spinBox_eps_time = QSpinBox(Form)
        self.spinBox_eps_time.setObjectName(u"spinBox_eps_time")
        self.spinBox_eps_time.setMinimum(1677)
        self.spinBox_eps_time.setMaximum(100000)

        self.horizontalLayout_1.addWidget(self.spinBox_eps_time)

        self.verticalLayout_1.addLayout(self.horizontalLayout_1)

        self.horizontalSlider_eps_time = QSlider(Form)
        self.horizontalSlider_eps_time.setObjectName(u"horizontalSlider_eps_time")
        self.horizontalSlider_eps_time.setMinimum(1677)
        self.horizontalSlider_eps_time.setMaximum(100000)
        self.horizontalSlider_eps_time.setOrientation(Qt.Horizontal)

        self.verticalLayout_1.addWidget(self.horizontalSlider_eps_time)

        self.verticalLayout.addLayout(self.verticalLayout_1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_f = QLabel(Form)
        self.label_f.setObjectName(u"label_f")

        self.horizontalLayout_2.addWidget(self.label_f)

        self.doubleSpinBox_f = QDoubleSpinBox(Form)
        self.doubleSpinBox_f.setObjectName(u"doubleSpinBox_f")
        self.doubleSpinBox_f.setMinimum(1.400000000000000)
        self.doubleSpinBox_f.setMaximum(32.000000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_f)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_bright_2 = QLabel(Form)
        self.label_bright_2.setObjectName(u"label_bright_2")

        self.horizontalLayout_3.addWidget(self.label_bright_2)

        self.doubleSpinBox_bright = QDoubleSpinBox(Form)
        self.doubleSpinBox_bright.setObjectName(u"doubleSpinBox_bright")
        self.doubleSpinBox_bright.setMaximum(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_bright)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_eps = QLabel(Form)
        self.label_eps.setObjectName(u"label_eps")

        self.horizontalLayout_5.addWidget(self.label_eps)

        self.doubleSpinBox_eps = QDoubleSpinBox(Form)
        self.doubleSpinBox_eps.setObjectName(u"doubleSpinBox_eps")
        self.doubleSpinBox_eps.setMinimum(1.000000000000000)
        self.doubleSpinBox_eps.setMaximum(16.000000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_eps)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        self.spinBox_eps_time.valueChanged.connect(self.horizontalSlider_eps_time.setValue)
        self.horizontalSlider_eps_time.valueChanged.connect(self.spinBox_eps_time.setValue)

        QMetaObject.connectSlotsByName(Form)

    # setupUi
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_eps_time.setText(QCoreApplication.translate("Form", u"\u66dd\u5149\u65f6\u95f4\uff08us\uff09", None))
        self.label_f.setText(QCoreApplication.translate("Form", u"\u5149\u5708\u5927\u5c0f\uff08f-number\uff09", None))
        self.label_bright_2.setText(QCoreApplication.translate("Form", u"\u4eae\u5ea6", None))
        self.label_eps.setText(QCoreApplication.translate("Form", u"\u66dd\u5149", None))
    # retranslateUi
