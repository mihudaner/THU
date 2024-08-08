# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AIOwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import QTui.CustomWidgets.Cardpage.icon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(885, 476)
        Form.setContextMenuPolicy(Qt.PreventContextMenu)
        Form.setStyleSheet(u"#styleSheet{\n"
"border: none;\n"
"margin: 0px;\n"
"}\n"
"QPushButton {\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"    color: #f8f8f2;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QWidget{\n"
"	color: #333;\n"
"	font: 13pt \"Segoe UI\";\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: #333;\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #9faeda;\n"
"	padding-lef"
                        "t: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #6272a4;\n"
"	max-width: 30px;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {\n"
"	background-color: #6272a4;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"	background-color: #6272a4;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb"
                        "(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    he"
                        "ight: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background-color: #6272a"
                        "4;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* //////////////////////////////////////////////////////////"
                        "///////////////////////////////////////\n"
"CheckBox \n"
"QCheckBox::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"*/\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;\n"
"}\n"
"\n"
"/* /////////////////////////////////////"
                        "////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #6272a4;\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////"
                        "////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	bor"
                        "der-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"\n"
"QTabWidget {\n"
"     border: none;\n"
"}\n"
"\n"
"QTabWidget {\n"
"     border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_7 = QGroupBox(Form)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_waveview_2 = QGroupBox(self.groupBox_7)
        self.groupBox_waveview_2.setObjectName(u"groupBox_waveview_2")
        self.groupBox_waveview_2.setMinimumSize(QSize(100, 100))

        self.verticalLayout_2.addWidget(self.groupBox_waveview_2)

        self.comboBox_plotcannel_2 = QComboBox(self.groupBox_7)
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.addItem("")
        self.comboBox_plotcannel_2.setObjectName(u"comboBox_plotcannel_2")

        self.verticalLayout_2.addWidget(self.comboBox_plotcannel_2)


        self.gridLayout_3.addWidget(self.groupBox_7, 0, 1, 1, 1)

        self.groupBox_10 = QGroupBox(Form)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_waveview_3 = QGroupBox(self.groupBox_10)
        self.groupBox_waveview_3.setObjectName(u"groupBox_waveview_3")
        self.groupBox_waveview_3.setMinimumSize(QSize(100, 100))

        self.verticalLayout_5.addWidget(self.groupBox_waveview_3)

        self.comboBox_plotcannel_3 = QComboBox(self.groupBox_10)
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.addItem("")
        self.comboBox_plotcannel_3.setObjectName(u"comboBox_plotcannel_3")

        self.verticalLayout_5.addWidget(self.comboBox_plotcannel_3)


        self.gridLayout_3.addWidget(self.groupBox_10, 0, 2, 1, 1)

        self.groupBox_8 = QGroupBox(Form)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_waveview_4 = QGroupBox(self.groupBox_8)
        self.groupBox_waveview_4.setObjectName(u"groupBox_waveview_4")
        self.groupBox_waveview_4.setMinimumSize(QSize(100, 100))

        self.verticalLayout_3.addWidget(self.groupBox_waveview_4)

        self.comboBox_plotcannel_4 = QComboBox(self.groupBox_8)
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.addItem("")
        self.comboBox_plotcannel_4.setObjectName(u"comboBox_plotcannel_4")

        self.verticalLayout_3.addWidget(self.comboBox_plotcannel_4)


        self.gridLayout_3.addWidget(self.groupBox_8, 1, 0, 1, 1)

        self.groupBox_9 = QGroupBox(Form)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_waveview_5 = QGroupBox(self.groupBox_9)
        self.groupBox_waveview_5.setObjectName(u"groupBox_waveview_5")
        self.groupBox_waveview_5.setMinimumSize(QSize(100, 100))

        self.verticalLayout_4.addWidget(self.groupBox_waveview_5)

        self.comboBox_plotcannel_5 = QComboBox(self.groupBox_9)
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.addItem("")
        self.comboBox_plotcannel_5.setObjectName(u"comboBox_plotcannel_5")

        self.verticalLayout_4.addWidget(self.comboBox_plotcannel_5)


        self.gridLayout_3.addWidget(self.groupBox_9, 1, 1, 1, 1)

        self.groupBox_11 = QGroupBox(Form)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_waveview_6 = QGroupBox(self.groupBox_11)
        self.groupBox_waveview_6.setObjectName(u"groupBox_waveview_6")
        self.groupBox_waveview_6.setMinimumSize(QSize(100, 100))

        self.verticalLayout_6.addWidget(self.groupBox_waveview_6)

        self.comboBox_plotcannel_6 = QComboBox(self.groupBox_11)
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.addItem("")
        self.comboBox_plotcannel_6.setObjectName(u"comboBox_plotcannel_6")

        self.verticalLayout_6.addWidget(self.comboBox_plotcannel_6)


        self.gridLayout_3.addWidget(self.groupBox_11, 1, 2, 1, 1)

        self.groupBox_6 = QGroupBox(Form)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout = QVBoxLayout(self.groupBox_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_waveview_1 = QGroupBox(self.groupBox_6)
        self.groupBox_waveview_1.setObjectName(u"groupBox_waveview_1")
        self.groupBox_waveview_1.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.groupBox_waveview_1)

        self.comboBox_plotcannel_1 = QComboBox(self.groupBox_6)
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.addItem("")
        self.comboBox_plotcannel_1.setObjectName(u"comboBox_plotcannel_1")

        self.verticalLayout.addWidget(self.comboBox_plotcannel_1)


        self.gridLayout_3.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 1)

        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.textBrowser = QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.textBrowser)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"\u6a21\u62df\u91cf\u8f93\u5165", None))
        self.groupBox_waveview_2.setTitle("")
        self.comboBox_plotcannel_2.setItemText(0, QCoreApplication.translate("Form", u"AD1_\u5b9e\u65f6\u6fc0\u5149\u529f\u7387", None))
        self.comboBox_plotcannel_2.setItemText(1, QCoreApplication.translate("Form", u"AD2_\u6fc0\u5149\u529f\u7387", None))
        self.comboBox_plotcannel_2.setItemText(2, QCoreApplication.translate("Form", u"AD3_\u7c89\u7b521\u9001\u7c89\u7535\u538b", None))
        self.comboBox_plotcannel_2.setItemText(3, QCoreApplication.translate("Form", u"AD4_\u7c89\u7b522\u9001\u7c89\u7535\u538b", None))
        self.comboBox_plotcannel_2.setItemText(4, QCoreApplication.translate("Form", u"AD5_\u5149\u6591\u7535\u538b", None))
        self.comboBox_plotcannel_2.setItemText(5, QCoreApplication.translate("Form", u"AD6_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_2.setItemText(6, QCoreApplication.translate("Form", u"AD7_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_2.setItemText(7, QCoreApplication.translate("Form", u"AD8_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_2.setItemText(8, QCoreApplication.translate("Form", u"AD9_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_2.setItemText(9, QCoreApplication.translate("Form", u"AD10_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_2.setItemText(10, QCoreApplication.translate("Form", u"AD11_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_2.setItemText(11, QCoreApplication.translate("Form", u"AD12_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_2.setItemText(12, QCoreApplication.translate("Form", u"AD13_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_2.setItemText(13, QCoreApplication.translate("Form", u"AD14_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_2.setItemText(14, QCoreApplication.translate("Form", u"AD15_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_2.setItemText(15, QCoreApplication.translate("Form", u"AD16_\u672a\u5b9a\u4e49", None))

        self.groupBox_10.setTitle(QCoreApplication.translate("Form", u"\u6a21\u62df\u91cf\u8f93\u5165", None))
        self.groupBox_waveview_3.setTitle("")
        self.comboBox_plotcannel_3.setItemText(0, QCoreApplication.translate("Form", u"AD1_\u5b9e\u65f6\u6fc0\u5149\u529f\u7387", None))
        self.comboBox_plotcannel_3.setItemText(1, QCoreApplication.translate("Form", u"AD2_\u6fc0\u5149\u529f\u7387", None))
        self.comboBox_plotcannel_3.setItemText(2, QCoreApplication.translate("Form", u"AD3_\u7c89\u7b521\u9001\u7c89\u7535\u538b", None))
        self.comboBox_plotcannel_3.setItemText(3, QCoreApplication.translate("Form", u"AD4_\u7c89\u7b522\u9001\u7c89\u7535\u538b", None))
        self.comboBox_plotcannel_3.setItemText(4, QCoreApplication.translate("Form", u"AD5_\u5149\u6591\u7535\u538b", None))
        self.comboBox_plotcannel_3.setItemText(5, QCoreApplication.translate("Form", u"AD6_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_3.setItemText(6, QCoreApplication.translate("Form", u"AD7_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_3.setItemText(7, QCoreApplication.translate("Form", u"AD8_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_3.setItemText(8, QCoreApplication.translate("Form", u"AD9_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_3.setItemText(9, QCoreApplication.translate("Form", u"AD10_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_3.setItemText(10, QCoreApplication.translate("Form", u"AD11_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_3.setItemText(11, QCoreApplication.translate("Form", u"AD12_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_3.setItemText(12, QCoreApplication.translate("Form", u"AD13_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_3.setItemText(13, QCoreApplication.translate("Form", u"AD14_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_3.setItemText(14, QCoreApplication.translate("Form", u"AD15_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_3.setItemText(15, QCoreApplication.translate("Form", u"AD16_\u672a\u5b9a\u4e49", None))

        self.groupBox_8.setTitle(QCoreApplication.translate("Form", u"\u6a21\u62df\u91cf\u8f93\u5165", None))
        self.groupBox_waveview_4.setTitle("")
        self.comboBox_plotcannel_4.setItemText(0, QCoreApplication.translate("Form", u"AD1_\u5b9e\u65f6\u6fc0\u5149\u529f\u7387", None))
        self.comboBox_plotcannel_4.setItemText(1, QCoreApplication.translate("Form", u"AD2_\u6fc0\u5149\u529f\u7387", None))
        self.comboBox_plotcannel_4.setItemText(2, QCoreApplication.translate("Form", u"AD3_\u7c89\u7b521\u9001\u7c89\u7535\u538b", None))
        self.comboBox_plotcannel_4.setItemText(3, QCoreApplication.translate("Form", u"AD4_\u7c89\u7b522\u9001\u7c89\u7535\u538b", None))
        self.comboBox_plotcannel_4.setItemText(4, QCoreApplication.translate("Form", u"AD5_\u5149\u6591\u7535\u538b", None))
        self.comboBox_plotcannel_4.setItemText(5, QCoreApplication.translate("Form", u"AD6_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_4.setItemText(6, QCoreApplication.translate("Form", u"AD7_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_4.setItemText(7, QCoreApplication.translate("Form", u"AD8_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_4.setItemText(8, QCoreApplication.translate("Form", u"AD9_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_4.setItemText(9, QCoreApplication.translate("Form", u"AD10_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_4.setItemText(10, QCoreApplication.translate("Form", u"AD11_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_4.setItemText(11, QCoreApplication.translate("Form", u"AD12_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_4.setItemText(12, QCoreApplication.translate("Form", u"AD13_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_4.setItemText(13, QCoreApplication.translate("Form", u"AD14_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_4.setItemText(14, QCoreApplication.translate("Form", u"AD15_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_4.setItemText(15, QCoreApplication.translate("Form", u"AD16_\u672a\u5b9a\u4e49", None))

        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"\u6a21\u62df\u91cf\u8f93\u5165", None))
        self.groupBox_waveview_5.setTitle("")
        self.comboBox_plotcannel_5.setItemText(0, QCoreApplication.translate("Form", u"AD1_\u5b9e\u65f6\u6fc0\u5149\u529f\u7387", None))
        self.comboBox_plotcannel_5.setItemText(1, QCoreApplication.translate("Form", u"AD2_\u6fc0\u5149\u529f\u7387", None))
        self.comboBox_plotcannel_5.setItemText(2, QCoreApplication.translate("Form", u"AD3_\u7c89\u7b521\u9001\u7c89\u7535\u538b", None))
        self.comboBox_plotcannel_5.setItemText(3, QCoreApplication.translate("Form", u"AD4_\u7c89\u7b522\u9001\u7c89\u7535\u538b", None))
        self.comboBox_plotcannel_5.setItemText(4, QCoreApplication.translate("Form", u"AD5_\u5149\u6591\u7535\u538b", None))
        self.comboBox_plotcannel_5.setItemText(5, QCoreApplication.translate("Form", u"AD6_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_5.setItemText(6, QCoreApplication.translate("Form", u"AD7_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_5.setItemText(7, QCoreApplication.translate("Form", u"AD8_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_5.setItemText(8, QCoreApplication.translate("Form", u"AD9_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_5.setItemText(9, QCoreApplication.translate("Form", u"AD10_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_5.setItemText(10, QCoreApplication.translate("Form", u"AD11_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_5.setItemText(11, QCoreApplication.translate("Form", u"AD12_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_5.setItemText(12, QCoreApplication.translate("Form", u"AD13_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_5.setItemText(13, QCoreApplication.translate("Form", u"AD14_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_5.setItemText(14, QCoreApplication.translate("Form", u"AD15_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_5.setItemText(15, QCoreApplication.translate("Form", u"AD16_\u672a\u5b9a\u4e49", None))

        self.groupBox_11.setTitle(QCoreApplication.translate("Form", u"\u6a21\u62df\u91cf\u8f93\u5165", None))
        self.groupBox_waveview_6.setTitle("")
        self.comboBox_plotcannel_6.setItemText(0, QCoreApplication.translate("Form", u"AD1_\u5b9e\u65f6\u6fc0\u5149\u529f\u7387", None))
        self.comboBox_plotcannel_6.setItemText(1, QCoreApplication.translate("Form", u"AD2_\u6fc0\u5149\u529f\u7387", None))
        self.comboBox_plotcannel_6.setItemText(2, QCoreApplication.translate("Form", u"AD3_\u7c89\u7b521\u9001\u7c89\u7535\u538b", None))
        self.comboBox_plotcannel_6.setItemText(3, QCoreApplication.translate("Form", u"AD4_\u7c89\u7b522\u9001\u7c89\u7535\u538b", None))
        self.comboBox_plotcannel_6.setItemText(4, QCoreApplication.translate("Form", u"AD5_\u5149\u6591\u7535\u538b", None))
        self.comboBox_plotcannel_6.setItemText(5, QCoreApplication.translate("Form", u"AD6_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_6.setItemText(6, QCoreApplication.translate("Form", u"AD7_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_6.setItemText(7, QCoreApplication.translate("Form", u"AD8_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_6.setItemText(8, QCoreApplication.translate("Form", u"AD9_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_6.setItemText(9, QCoreApplication.translate("Form", u"AD10_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_6.setItemText(10, QCoreApplication.translate("Form", u"AD11_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_6.setItemText(11, QCoreApplication.translate("Form", u"AD12_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_6.setItemText(12, QCoreApplication.translate("Form", u"AD13_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_6.setItemText(13, QCoreApplication.translate("Form", u"AD14_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_6.setItemText(14, QCoreApplication.translate("Form", u"AD15_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_6.setItemText(15, QCoreApplication.translate("Form", u"AD16_\u672a\u5b9a\u4e49", None))

        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"\u6a21\u62df\u91cf\u8f93\u5165", None))
        self.groupBox_waveview_1.setTitle("")
        self.comboBox_plotcannel_1.setItemText(0, QCoreApplication.translate("Form", u"AD1_\u5b9e\u65f6\u6fc0\u5149\u529f\u7387", None))
        self.comboBox_plotcannel_1.setItemText(1, QCoreApplication.translate("Form", u"AD2_\u6fc0\u5149\u529f\u7387", None))
        self.comboBox_plotcannel_1.setItemText(2, QCoreApplication.translate("Form", u"AD3_\u7c89\u7b521\u9001\u7c89\u7535\u538b", None))
        self.comboBox_plotcannel_1.setItemText(3, QCoreApplication.translate("Form", u"AD4_\u7c89\u7b522\u9001\u7c89\u7535\u538b", None))
        self.comboBox_plotcannel_1.setItemText(4, QCoreApplication.translate("Form", u"AD5_\u5149\u6591\u7535\u538b", None))
        self.comboBox_plotcannel_1.setItemText(5, QCoreApplication.translate("Form", u"AD6_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_1.setItemText(6, QCoreApplication.translate("Form", u"AD7_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_1.setItemText(7, QCoreApplication.translate("Form", u"AD8_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_1.setItemText(8, QCoreApplication.translate("Form", u"AD9_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_1.setItemText(9, QCoreApplication.translate("Form", u"AD10_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_1.setItemText(10, QCoreApplication.translate("Form", u"AD11_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_1.setItemText(11, QCoreApplication.translate("Form", u"AD12_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_1.setItemText(12, QCoreApplication.translate("Form", u"AD13_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_1.setItemText(13, QCoreApplication.translate("Form", u"AD14_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_1.setItemText(14, QCoreApplication.translate("Form", u"AD15_\u672a\u5b9a\u4e49", None))
        self.comboBox_plotcannel_1.setItemText(15, QCoreApplication.translate("Form", u"AD16_\u672a\u5b9a\u4e49", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8c03\u8bd5\u4fe1\u606f:", None))
    # retranslateUi

