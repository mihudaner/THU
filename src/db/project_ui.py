# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(596, 404)
        Form.setContextMenuPolicy(Qt.PreventContextMenu)
        Form.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(Form)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_13 = QHBoxLayout(self.widget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_4.addWidget(self.comboBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_13.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontalLayout_5.addWidget(self.doubleSpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.horizontalLayout_7.addWidget(self.doubleSpinBox_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")

        self.horizontalLayout_8.addWidget(self.doubleSpinBox_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")

        self.horizontalLayout_9.addWidget(self.doubleSpinBox_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")

        self.horizontalLayout_10.addWidget(self.doubleSpinBox_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")

        self.horizontalLayout_11.addWidget(self.doubleSpinBox_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_13.addWidget(self.groupBox_2)


        self.horizontalLayout_12.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u9879\u76ee\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u65e5\u671f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7c89\u672b\u6750\u6599", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"T15", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"TC11", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u6750\u6599", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"43CrMo", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"TC4", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\u7c7b\u578b", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"\u5355\u9053", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"\u5355\u5c42\u591a\u9053", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"\u5355\u9053\u591a\u5c42", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form", u"\u591a\u5c42\u591a\u9053", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u5de5\u827a\u53c2\u6570", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6fc0\u5149\u529f\u7387", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u7194\u8986\u901f\u5ea6", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u9001\u7c89\u901f\u5ea6", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u5149\u6591\u76f4\u5f84", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u504f\u79fb\u8ddd\u79bb", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u9053\u95f4\u95f4\u9694", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u5c42\u95f4\u95f4\u9694", None))
    # retranslateUi

