# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DAM8888_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1426, 789)
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
        self.horizontalLayout_11 = QHBoxLayout(Form)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_waveview = QGroupBox(Form)
        self.groupBox_waveview.setObjectName(u"groupBox_waveview")
        self.groupBox_waveview.setMinimumSize(QSize(700, 500))

        self.verticalLayout_11.addWidget(self.groupBox_waveview)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox_6 = QGroupBox(Form)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.comboBox_plotcannel = QComboBox(self.groupBox_6)
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.addItem("")
        self.comboBox_plotcannel.setObjectName(u"comboBox_plotcannel")

        self.horizontalLayout_12.addWidget(self.comboBox_plotcannel)


        self.horizontalLayout_9.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(Form)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.DI0 = QRadioButton(self.groupBox_7)
        self.DI0.setObjectName(u"DI0")
        self.DI0.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.DI0)

        self.DI1 = QRadioButton(self.groupBox_7)
        self.DI1.setObjectName(u"DI1")
        self.DI1.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.DI1)

        self.DI2 = QRadioButton(self.groupBox_7)
        self.DI2.setObjectName(u"DI2")
        self.DI2.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.DI2)

        self.DI3 = QRadioButton(self.groupBox_7)
        self.DI3.setObjectName(u"DI3")
        self.DI3.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.DI3)

        self.DI4 = QRadioButton(self.groupBox_7)
        self.DI4.setObjectName(u"DI4")
        self.DI4.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.DI4)

        self.DI5 = QRadioButton(self.groupBox_7)
        self.DI5.setObjectName(u"DI5")
        self.DI5.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.DI5)

        self.DI6 = QRadioButton(self.groupBox_7)
        self.DI6.setObjectName(u"DI6")
        self.DI6.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.DI6)

        self.DI7 = QRadioButton(self.groupBox_7)
        self.DI7.setObjectName(u"DI7")
        self.DI7.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.DI7)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_9.addWidget(self.groupBox_7)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_11.addLayout(self.horizontalLayout)

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


        self.verticalLayout_11.addWidget(self.groupBox_2)

        self.verticalLayout_11.setStretch(0, 3)
        self.verticalLayout_11.setStretch(3, 1)

        self.horizontalLayout_11.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.lineEdit_IP = QLineEdit(self.groupBox)
        self.lineEdit_IP.setObjectName(u"lineEdit_IP")

        self.verticalLayout_4.addWidget(self.lineEdit_IP)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setTextFormat(Qt.PlainText)

        self.verticalLayout_5.addWidget(self.label_4)

        self.spinBox_DIDO_updatetime = QSpinBox(self.groupBox)
        self.spinBox_DIDO_updatetime.setObjectName(u"spinBox_DIDO_updatetime")
        self.spinBox_DIDO_updatetime.setMinimum(100)
        self.spinBox_DIDO_updatetime.setMaximum(100000)
        self.spinBox_DIDO_updatetime.setValue(2000)

        self.verticalLayout_5.addWidget(self.spinBox_DIDO_updatetime)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 3, 1, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_9.addWidget(self.label_2)

        self.spinBox_AI_updatetime = QSpinBox(self.groupBox)
        self.spinBox_AI_updatetime.setObjectName(u"spinBox_AI_updatetime")
        self.spinBox_AI_updatetime.setMinimum(100)
        self.spinBox_AI_updatetime.setMaximum(100000)
        self.spinBox_AI_updatetime.setValue(2000)

        self.verticalLayout_9.addWidget(self.spinBox_AI_updatetime)


        self.gridLayout_2.addLayout(self.verticalLayout_9, 3, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.spinBox_port = QSpinBox(self.groupBox)
        self.spinBox_port.setObjectName(u"spinBox_port")
        self.spinBox_port.setMinimum(5000)
        self.spinBox_port.setMaximum(80000)
        self.spinBox_port.setValue(10000)

        self.verticalLayout_8.addWidget(self.spinBox_port)


        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_7.addWidget(self.label_5)

        self.spinBox_PWM1 = QSpinBox(self.groupBox)
        self.spinBox_PWM1.setObjectName(u"spinBox_PWM1")
        self.spinBox_PWM1.setMaximum(65535)

        self.verticalLayout_7.addWidget(self.spinBox_PWM1)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 3, 2, 1, 1)

        self.checkBox_openport = QCheckBox(self.groupBox)
        self.checkBox_openport.setObjectName(u"checkBox_openport")
        self.checkBox_openport.setMinimumSize(QSize(120, 50))
        self.checkBox_openport.setLayoutDirection(Qt.RightToLeft)
        self.checkBox_openport.setStyleSheet(u" QCheckBox {\n"
"            /*font-size: 20px;*/\n"
"			font: 13pt \"Segoe UI\";\n"
"        }\n"
"\n"
"        QCheckBox::indicator {\n"
"            padding-top: 1px;\n"
"            width: 40px;\n"
"            height: 30px;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked {\n"
"            image: url(:/icon/check_on.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked {\n"
"            image: url(:/icon/check_off.png);\n"
"        }\n"
"")

        self.gridLayout_2.addWidget(self.checkBox_openport, 0, 2, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_2)

        self.groupBox_ADsets = QGroupBox(self.groupBox)
        self.groupBox_ADsets.setObjectName(u"groupBox_ADsets")
        self.gridLayout = QGridLayout(self.groupBox_ADsets)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.groupBox_ADsets)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.Slider3 = QSlider(self.groupBox_ADsets)
        self.Slider3.setObjectName(u"Slider3")
        self.Slider3.setMaximum(10000)
        self.Slider3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.Slider3)

        self.spinBox_AO3 = QSpinBox(self.groupBox_ADsets)
        self.spinBox_AO3.setObjectName(u"spinBox_AO3")
        self.spinBox_AO3.setMaximum(10000)
        self.spinBox_AO3.setSingleStep(1)
        self.spinBox_AO3.setValue(0)

        self.horizontalLayout_4.addWidget(self.spinBox_AO3)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.groupBox_ADsets)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.Slider4 = QSlider(self.groupBox_ADsets)
        self.Slider4.setObjectName(u"Slider4")
        self.Slider4.setMaximum(10000)
        self.Slider4.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.Slider4)

        self.spinBox_AO4 = QSpinBox(self.groupBox_ADsets)
        self.spinBox_AO4.setObjectName(u"spinBox_AO4")
        self.spinBox_AO4.setMaximum(10000)
        self.spinBox_AO4.setSingleStep(1)
        self.spinBox_AO4.setValue(0)

        self.horizontalLayout_5.addWidget(self.spinBox_AO4)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_ADsets)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.Slider1 = QSlider(self.groupBox_ADsets)
        self.Slider1.setObjectName(u"Slider1")
        self.Slider1.setMaximum(10000)
        self.Slider1.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.Slider1)

        self.spinBox_AO1 = QSpinBox(self.groupBox_ADsets)
        self.spinBox_AO1.setObjectName(u"spinBox_AO1")
        self.spinBox_AO1.setMaximum(10000)
        self.spinBox_AO1.setSingleStep(1)
        self.spinBox_AO1.setValue(0)

        self.horizontalLayout_2.addWidget(self.spinBox_AO1)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_13 = QLabel(self.groupBox_ADsets)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_17.addWidget(self.label_13)

        self.Slider8 = QSlider(self.groupBox_ADsets)
        self.Slider8.setObjectName(u"Slider8")
        self.Slider8.setMaximum(10000)
        self.Slider8.setOrientation(Qt.Horizontal)

        self.horizontalLayout_17.addWidget(self.Slider8)

        self.spinBox_AO8 = QSpinBox(self.groupBox_ADsets)
        self.spinBox_AO8.setObjectName(u"spinBox_AO8")
        self.spinBox_AO8.setMaximum(10000)
        self.spinBox_AO8.setSingleStep(1)
        self.spinBox_AO8.setValue(0)

        self.horizontalLayout_17.addWidget(self.spinBox_AO8)


        self.gridLayout.addLayout(self.horizontalLayout_17, 3, 1, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_11 = QLabel(self.groupBox_ADsets)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_15.addWidget(self.label_11)

        self.Slider6 = QSlider(self.groupBox_ADsets)
        self.Slider6.setObjectName(u"Slider6")
        self.Slider6.setMaximum(10000)
        self.Slider6.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.Slider6)

        self.spinBox_AO6 = QSpinBox(self.groupBox_ADsets)
        self.spinBox_AO6.setObjectName(u"spinBox_AO6")
        self.spinBox_AO6.setMaximum(10000)
        self.spinBox_AO6.setSingleStep(1)
        self.spinBox_AO6.setValue(0)

        self.horizontalLayout_15.addWidget(self.spinBox_AO6)


        self.gridLayout.addLayout(self.horizontalLayout_15, 2, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.groupBox_ADsets)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.Slider5 = QSlider(self.groupBox_ADsets)
        self.Slider5.setObjectName(u"Slider5")
        self.Slider5.setMaximum(10000)
        self.Slider5.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.Slider5)

        self.spinBox_AO5 = QSpinBox(self.groupBox_ADsets)
        self.spinBox_AO5.setObjectName(u"spinBox_AO5")
        self.spinBox_AO5.setMaximum(10000)
        self.spinBox_AO5.setSingleStep(1)
        self.spinBox_AO5.setValue(0)

        self.horizontalLayout_8.addWidget(self.spinBox_AO5)


        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.groupBox_ADsets)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.Slider7 = QSlider(self.groupBox_ADsets)
        self.Slider7.setObjectName(u"Slider7")
        self.Slider7.setMaximum(10000)
        self.Slider7.setOrientation(Qt.Horizontal)

        self.horizontalLayout_16.addWidget(self.Slider7)

        self.spinBox_AO7 = QSpinBox(self.groupBox_ADsets)
        self.spinBox_AO7.setObjectName(u"spinBox_AO7")
        self.spinBox_AO7.setMaximum(10000)
        self.spinBox_AO7.setSingleStep(1)
        self.spinBox_AO7.setValue(0)

        self.horizontalLayout_16.addWidget(self.spinBox_AO7)


        self.gridLayout.addLayout(self.horizontalLayout_16, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.groupBox_ADsets)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.Slider2 = QSlider(self.groupBox_ADsets)
        self.Slider2.setObjectName(u"Slider2")
        self.Slider2.setMaximum(10000)
        self.Slider2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.Slider2)

        self.spinBox_AO2 = QSpinBox(self.groupBox_ADsets)
        self.spinBox_AO2.setObjectName(u"spinBox_AO2")
        self.spinBox_AO2.setMaximum(10000)
        self.spinBox_AO2.setSingleStep(1)
        self.spinBox_AO2.setValue(0)

        self.horizontalLayout_3.addWidget(self.spinBox_AO2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)


        self.verticalLayout_19.addWidget(self.groupBox_ADsets)

        self.btn_setAO = QPushButton(self.groupBox)
        self.btn_setAO.setObjectName(u"btn_setAO")

        self.verticalLayout_19.addWidget(self.btn_setAO)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.verticalLayout_12.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.DO0 = QRadioButton(self.groupBox_3)
        self.DO0.setObjectName(u"DO0")
        self.DO0.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.DO0)

        self.DO1 = QRadioButton(self.groupBox_3)
        self.DO1.setObjectName(u"DO1")
        self.DO1.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.DO1)

        self.DO2 = QRadioButton(self.groupBox_3)
        self.DO2.setObjectName(u"DO2")
        self.DO2.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.DO2)

        self.DO3 = QRadioButton(self.groupBox_3)
        self.DO3.setObjectName(u"DO3")
        self.DO3.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.DO3)

        self.DO4 = QRadioButton(self.groupBox_3)
        self.DO4.setObjectName(u"DO4")
        self.DO4.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.DO4)

        self.DO5 = QRadioButton(self.groupBox_3)
        self.DO5.setObjectName(u"DO5")
        self.DO5.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.DO5)

        self.DO6 = QRadioButton(self.groupBox_3)
        self.DO6.setObjectName(u"DO6")
        self.DO6.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.DO6)

        self.DO7 = QRadioButton(self.groupBox_3)
        self.DO7.setObjectName(u"DO7")
        self.DO7.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.DO7)


        self.verticalLayout_12.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_readDO = QPushButton(Form)
        self.btn_readDO.setObjectName(u"btn_readDO")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_readDO.sizePolicy().hasHeightForWidth())
        self.btn_readDO.setSizePolicy(sizePolicy1)
        self.btn_readDO.setMinimumSize(QSize(0, 0))
        self.btn_readDO.setContextMenuPolicy(Qt.NoContextMenu)
        self.btn_readDO.setLayoutDirection(Qt.LeftToRight)
        self.btn_readDO.setIconSize(QSize(16, 16))
        self.btn_readDO.setAutoRepeatDelay(300)
        self.btn_readDO.setAutoRepeatInterval(100)

        self.verticalLayout.addWidget(self.btn_readDO)

        self.btn_readDI = QPushButton(Form)
        self.btn_readDI.setObjectName(u"btn_readDI")

        self.verticalLayout.addWidget(self.btn_readDI)

        self.btn_readAI = QPushButton(Form)
        self.btn_readAI.setObjectName(u"btn_readAI")

        self.verticalLayout.addWidget(self.btn_readAI)


        self.verticalLayout_12.addLayout(self.verticalLayout)

        self.verticalLayout_12.setStretch(0, 3)
        self.verticalLayout_12.setStretch(4, 1)

        self.horizontalLayout_11.addLayout(self.verticalLayout_12)

        self.horizontalLayout_11.setStretch(0, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_waveview.setTitle("")
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"\u6a21\u62df\u91cf\u8f93\u5165", None))
        self.comboBox_plotcannel.setItemText(0, QCoreApplication.translate("Form", u"AD1", None))
        self.comboBox_plotcannel.setItemText(1, QCoreApplication.translate("Form", u"AD2", None))
        self.comboBox_plotcannel.setItemText(2, QCoreApplication.translate("Form", u"AD3", None))
        self.comboBox_plotcannel.setItemText(3, QCoreApplication.translate("Form", u"AD4", None))
        self.comboBox_plotcannel.setItemText(4, QCoreApplication.translate("Form", u"AD5", None))
        self.comboBox_plotcannel.setItemText(5, QCoreApplication.translate("Form", u"AD6", None))
        self.comboBox_plotcannel.setItemText(6, QCoreApplication.translate("Form", u"AD7", None))
        self.comboBox_plotcannel.setItemText(7, QCoreApplication.translate("Form", u"AD8", None))
        self.comboBox_plotcannel.setItemText(8, QCoreApplication.translate("Form", u"AD9", None))
        self.comboBox_plotcannel.setItemText(9, QCoreApplication.translate("Form", u"AD10", None))
        self.comboBox_plotcannel.setItemText(10, QCoreApplication.translate("Form", u"AD11", None))
        self.comboBox_plotcannel.setItemText(11, QCoreApplication.translate("Form", u"AD12", None))
        self.comboBox_plotcannel.setItemText(12, QCoreApplication.translate("Form", u"AD13", None))
        self.comboBox_plotcannel.setItemText(13, QCoreApplication.translate("Form", u"AD14", None))
        self.comboBox_plotcannel.setItemText(14, QCoreApplication.translate("Form", u"AD15", None))
        self.comboBox_plotcannel.setItemText(15, QCoreApplication.translate("Form", u"AD16", None))

        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"\u6570\u5b57\u91cf\u8bfb\u5165", None))
        self.DI0.setText("")
        self.DI1.setText("")
        self.DI2.setText("")
        self.DI3.setText("")
        self.DI4.setText("")
        self.DI5.setText("")
        self.DI6.setText("")
        self.DI7.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8c03\u8bd5\u4fe1\u606f:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u53c2\u6570\u8bbe\u7f6e:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"IP\u5730\u5740", None))
        self.lineEdit_IP.setText(QCoreApplication.translate("Form", u"192.168.10.1", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"DIDO\u66f4\u65b0\u65f6\u95f4ms", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"AI\u66f4\u65b0\u65f6\u95f4ms", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3\u53f7", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u901a\u4fe1\u8d85\u65f6ms", None))
        self.checkBox_openport.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u7aef\u53e3", None))
        self.groupBox_ADsets.setTitle(QCoreApplication.translate("Form", u"\u6a21\u62df\u91cf\u8bbe\u7f6e", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"AO3", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"AO4", None))
        self.label.setText(QCoreApplication.translate("Form", u"AO1", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"AO8", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"AO6", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"AO5", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"AO7", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"AO2", None))
        self.btn_setAO.setText(QCoreApplication.translate("Form", u"\u591a\u901a\u9053\u8bbe\u7f6eAO", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u7ee7\u7535\u5668", None))
        self.DO0.setText("")
        self.DO1.setText("")
        self.DO2.setText("")
        self.DO3.setText("")
        self.DO4.setText("")
        self.DO5.setText("")
        self.DO6.setText("")
        self.DO7.setText("")
        self.btn_readDO.setText(QCoreApplication.translate("Form", u"\u8bfb\u53d6\u7ee7\u7535\u5668\u72b6\u6001", None))
        self.btn_readDI.setText(QCoreApplication.translate("Form", u"\u8bfb\u53d6DI\u72b6\u6001", None))
        self.btn_readAI.setText(QCoreApplication.translate("Form", u"\u8bfb\u53d6AI\u72b6\u6001", None))
    # retranslateUi

