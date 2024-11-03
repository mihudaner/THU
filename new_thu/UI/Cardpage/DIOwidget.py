# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DIOwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import UI.Cardpage.icon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1083, 647)
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
"	font: 10pt \"Segoe UI\";\n"
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
"    background: 3px solid #F72121;\n"
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
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.groupBox_7 = QGroupBox(Form)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMaximumSize(QSize(16777215, 300))
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.DI0 = QRadioButton(self.groupBox_7)
        self.DI0.setObjectName(u"DI0")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DI0.sizePolicy().hasHeightForWidth())
        self.DI0.setSizePolicy(sizePolicy)
        self.DI0.setLayoutDirection(Qt.LeftToRight)
        self.DI0.setIconSize(QSize(25, 25))
        self.DI0.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.DI0)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_6.addWidget(self.label_14)

        self.label_15 = QLabel(self.groupBox_7)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_6.addWidget(self.label_15)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_15)

        self.DI1 = QRadioButton(self.groupBox_7)
        self.DI1.setObjectName(u"DI1")
        self.DI1.setAutoExclusive(False)

        self.horizontalLayout_21.addWidget(self.DI1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_16)


        self.verticalLayout_10.addLayout(self.horizontalLayout_21)

        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_16)

        self.label_17 = QLabel(self.groupBox_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_17)


        self.horizontalLayout_9.addLayout(self.verticalLayout_10)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.DI2 = QRadioButton(self.groupBox_7)
        self.DI2.setObjectName(u"DI2")
        self.DI2.setAutoExclusive(False)

        self.horizontalLayout_13.addWidget(self.DI2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)

        self.label_18 = QLabel(self.groupBox_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_18)

        self.label_19 = QLabel(self.groupBox_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_19)


        self.horizontalLayout_9.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.DI3 = QRadioButton(self.groupBox_7)
        self.DI3.setObjectName(u"DI3")
        self.DI3.setAutoExclusive(False)

        self.horizontalLayout_14.addWidget(self.DI3)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)


        self.verticalLayout_14.addLayout(self.horizontalLayout_14)

        self.label_20 = QLabel(self.groupBox_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_20)

        self.label_21 = QLabel(self.groupBox_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_21)


        self.horizontalLayout_9.addLayout(self.verticalLayout_14)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.DI4 = QRadioButton(self.groupBox_7)
        self.DI4.setObjectName(u"DI4")
        self.DI4.setAutoExclusive(False)

        self.horizontalLayout_12.addWidget(self.DI4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.verticalLayout_18.addLayout(self.horizontalLayout_12)

        self.label_28 = QLabel(self.groupBox_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_28)

        self.label_29 = QLabel(self.groupBox_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_29)


        self.horizontalLayout_9.addLayout(self.verticalLayout_18)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_11)

        self.DI5 = QRadioButton(self.groupBox_7)
        self.DI5.setObjectName(u"DI5")
        self.DI5.setAutoExclusive(False)

        self.horizontalLayout_19.addWidget(self.DI5)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_12)


        self.verticalLayout_15.addLayout(self.horizontalLayout_19)

        self.label_22 = QLabel(self.groupBox_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_22)

        self.label_23 = QLabel(self.groupBox_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_23)


        self.horizontalLayout_9.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_13)

        self.DI6 = QRadioButton(self.groupBox_7)
        self.DI6.setObjectName(u"DI6")
        self.DI6.setAutoExclusive(False)

        self.horizontalLayout_20.addWidget(self.DI6)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_14)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)

        self.label_24 = QLabel(self.groupBox_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_24)

        self.label_25 = QLabel(self.groupBox_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_25)


        self.horizontalLayout_9.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_9)

        self.DI7 = QRadioButton(self.groupBox_7)
        self.DI7.setObjectName(u"DI7")
        self.DI7.setAutoExclusive(False)

        self.horizontalLayout_18.addWidget(self.DI7)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_10)


        self.verticalLayout_17.addLayout(self.horizontalLayout_18)

        self.label_26 = QLabel(self.groupBox_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_26)

        self.label_27 = QLabel(self.groupBox_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_27)


        self.horizontalLayout_9.addLayout(self.verticalLayout_17)


        self.verticalLayout_30.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_30.addItem(self.verticalSpacer_5)


        self.verticalLayout_11.addWidget(self.groupBox_7)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMaximumSize(QSize(16777215, 300))
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_19)

        self.DO0 = QRadioButton(self.groupBox_3)
        self.DO0.setObjectName(u"DO0")
        self.DO0.setAutoExclusive(False)

        self.horizontalLayout_23.addWidget(self.DO0)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_20)


        self.verticalLayout_21.addLayout(self.horizontalLayout_23)

        self.label_32 = QLabel(self.groupBox_3)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_21.addWidget(self.label_32)

        self.label_33 = QLabel(self.groupBox_3)
        self.label_33.setObjectName(u"label_33")
        sizePolicy1.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy1)
        self.label_33.setMaximumSize(QSize(16777215, 200))
        self.label_33.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_33)


        self.horizontalLayout_7.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_21)

        self.DO1 = QRadioButton(self.groupBox_3)
        self.DO1.setObjectName(u"DO1")
        self.DO1.setAutoExclusive(False)

        self.horizontalLayout_24.addWidget(self.DO1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_22)


        self.verticalLayout_22.addLayout(self.horizontalLayout_24)

        self.label_34 = QLabel(self.groupBox_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_34)

        self.label_35 = QLabel(self.groupBox_3)
        self.label_35.setObjectName(u"label_35")
        sizePolicy1.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy1)
        self.label_35.setMaximumSize(QSize(16777215, 200))
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_35)


        self.horizontalLayout_7.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_23)

        self.DO2 = QRadioButton(self.groupBox_3)
        self.DO2.setObjectName(u"DO2")
        self.DO2.setAutoExclusive(False)

        self.horizontalLayout_25.addWidget(self.DO2)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_24)


        self.verticalLayout_23.addLayout(self.horizontalLayout_25)

        self.label_36 = QLabel(self.groupBox_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_36)

        self.label_37 = QLabel(self.groupBox_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 200))
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_37)


        self.horizontalLayout_7.addLayout(self.verticalLayout_23)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_25)

        self.DO3 = QRadioButton(self.groupBox_3)
        self.DO3.setObjectName(u"DO3")
        self.DO3.setAutoExclusive(False)

        self.horizontalLayout_26.addWidget(self.DO3)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_26)


        self.verticalLayout_24.addLayout(self.horizontalLayout_26)

        self.label_38 = QLabel(self.groupBox_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_38)

        self.label_39 = QLabel(self.groupBox_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 200))
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_39)


        self.horizontalLayout_7.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_27)

        self.DO4 = QRadioButton(self.groupBox_3)
        self.DO4.setObjectName(u"DO4")
        self.DO4.setAutoExclusive(False)

        self.horizontalLayout_27.addWidget(self.DO4)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_28)


        self.verticalLayout_25.addLayout(self.horizontalLayout_27)

        self.label_40 = QLabel(self.groupBox_3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_40)

        self.label_41 = QLabel(self.groupBox_3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_41)


        self.horizontalLayout_7.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_29)

        self.DO5 = QRadioButton(self.groupBox_3)
        self.DO5.setObjectName(u"DO5")
        self.DO5.setAutoExclusive(False)

        self.horizontalLayout_28.addWidget(self.DO5)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_30)


        self.verticalLayout_26.addLayout(self.horizontalLayout_28)

        self.label_42 = QLabel(self.groupBox_3)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_42)

        self.label_43 = QLabel(self.groupBox_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_43)


        self.horizontalLayout_7.addLayout(self.verticalLayout_26)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_31)

        self.DO6 = QRadioButton(self.groupBox_3)
        self.DO6.setObjectName(u"DO6")
        self.DO6.setAutoExclusive(False)

        self.horizontalLayout_29.addWidget(self.DO6)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_32)


        self.verticalLayout_27.addLayout(self.horizontalLayout_29)

        self.label_44 = QLabel(self.groupBox_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_44)

        self.label_45 = QLabel(self.groupBox_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_45)


        self.horizontalLayout_7.addLayout(self.verticalLayout_27)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_33)

        self.DO7 = QRadioButton(self.groupBox_3)
        self.DO7.setObjectName(u"DO7")
        self.DO7.setAutoExclusive(False)

        self.horizontalLayout_30.addWidget(self.DO7)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_34)


        self.verticalLayout_28.addLayout(self.horizontalLayout_30)

        self.label_46 = QLabel(self.groupBox_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_46)

        self.label_47 = QLabel(self.groupBox_3)
        self.label_47.setObjectName(u"label_47")
        sizePolicy1.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy1)
        self.label_47.setMinimumSize(QSize(0, 0))
        self.label_47.setMaximumSize(QSize(16777215, 100))
        self.label_47.setAlignment(Qt.AlignCenter)
        self.label_47.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.label_47)


        self.horizontalLayout_7.addLayout(self.verticalLayout_28)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 1)
        self.horizontalLayout_7.setStretch(3, 1)
        self.horizontalLayout_7.setStretch(4, 1)
        self.horizontalLayout_7.setStretch(5, 1)
        self.horizontalLayout_7.setStretch(6, 1)
        self.horizontalLayout_7.setStretch(7, 1)

        self.verticalLayout_31.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_31.addItem(self.verticalSpacer_6)


        self.verticalLayout_11.addWidget(self.groupBox_3)


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
        self.label_30 = QLabel(self.groupBox_ADsets)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 1, 0, 1, 1)

        self.label_51 = QLabel(self.groupBox_ADsets)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout.addWidget(self.label_51, 5, 1, 1, 1)

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

        self.label_31 = QLabel(self.groupBox_ADsets)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 1, 1, 1, 1)

        self.label_50 = QLabel(self.groupBox_ADsets)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout.addWidget(self.label_50, 5, 0, 1, 1)

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


        self.gridLayout.addLayout(self.horizontalLayout_17, 6, 1, 1, 1)

        self.label_49 = QLabel(self.groupBox_ADsets)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout.addWidget(self.label_49, 3, 1, 1, 1)

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


        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 0, 1, 1)

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


        self.gridLayout.addLayout(self.horizontalLayout_16, 6, 0, 1, 1)

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


        self.gridLayout.addLayout(self.horizontalLayout_15, 4, 1, 1, 1)

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


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

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


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)

        self.label_48 = QLabel(self.groupBox_ADsets)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout.addWidget(self.label_48, 3, 0, 1, 1)

        self.label_52 = QLabel(self.groupBox_ADsets)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout.addWidget(self.label_52, 7, 0, 1, 1)

        self.label_53 = QLabel(self.groupBox_ADsets)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout.addWidget(self.label_53, 7, 1, 1, 1)


        self.verticalLayout_19.addWidget(self.groupBox_ADsets)

        self.btn_setAO = QPushButton(self.groupBox)
        self.btn_setAO.setObjectName(u"btn_setAO")

        self.verticalLayout_19.addWidget(self.btn_setAO)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.verticalLayout_12.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_readDO = QPushButton(Form)
        self.btn_readDO.setObjectName(u"btn_readDO")
        sizePolicy.setHeightForWidth(self.btn_readDO.sizePolicy().hasHeightForWidth())
        self.btn_readDO.setSizePolicy(sizePolicy)
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
        self.verticalLayout_12.setStretch(3, 1)

        self.horizontalLayout_11.addLayout(self.verticalLayout_12)

        self.horizontalLayout_11.setStretch(0, 2)
        self.horizontalLayout_11.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"\u6570\u5b57\u91cf\u8bfb\u5165", None))
        self.DI0.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"DI1", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u5f85\u5b9a\u4e49", None))
        self.DI1.setText("")
        self.label_16.setText(QCoreApplication.translate("Form", u"DI2", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u7ed3\u6784\u5149\u76f8\u673a", None))
        self.DI2.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"DI3", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u5f85\u5b9a\u4e49", None))
        self.DI3.setText("")
        self.label_20.setText(QCoreApplication.translate("Form", u"DI4", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u5b9e\u65f6\u529f\u7387\u4fdd\u5b58", None))
        self.DI4.setText("")
        self.label_28.setText(QCoreApplication.translate("Form", u"DI5", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"\u4f4d\u79fb\u4fdd\u5b58", None))
        self.DI5.setText("")
        self.label_22.setText(QCoreApplication.translate("Form", u"DI6", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"CCD\u5f00\u5173", None))
        self.DI6.setText("")
        self.label_24.setText(QCoreApplication.translate("Form", u"DI7", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"\u5f85\u5b9a\u4e49", None))
        self.DI7.setText("")
        self.label_26.setText(QCoreApplication.translate("Form", u"DI8", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"\u7ea2\u5916\u70b9\u6e29\u5f00\u5173", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u7ee7\u7535\u5668", None))
        self.DO0.setText("")
        self.label_32.setText(QCoreApplication.translate("Form", u"DO1", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u6fc0\u5149\u529f\u7387", None))
        self.DO1.setText("")
        self.label_34.setText(QCoreApplication.translate("Form", u"DO2", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u9001\u5206\u7535\u538b1", None))
        self.DO2.setText("")
        self.label_36.setText(QCoreApplication.translate("Form", u"DO3", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u9001\u5206\u7535\u538b2", None))
        self.DO3.setText("")
        self.label_38.setText(QCoreApplication.translate("Form", u"DO4", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u6fc0\u5149\u5149\u6591", None))
        self.DO4.setText("")
        self.label_40.setText(QCoreApplication.translate("Form", u"DO5", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"\u5f85\u5b9a\u4e49", None))
        self.DO5.setText("")
        self.label_42.setText(QCoreApplication.translate("Form", u"DO6", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"\u5f85\u5b9a\u4e49", None))
        self.DO6.setText("")
        self.label_44.setText(QCoreApplication.translate("Form", u"DO7", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"\u5f85\u5b9a\u4e49", None))
        self.DO7.setText("")
        self.label_46.setText(QCoreApplication.translate("Form", u"DO8", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"\u5f85\u5b9a\u4e49", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u53c2\u6570\u8bbe\u7f6e:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"IP\u5730\u5740", None))
        self.lineEdit_IP.setText(QCoreApplication.translate("Form", u"192.168.10.1", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"DIDO\u66f4\u65b0\u65f6\u95f4ms", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"AI\u66f4\u65b0\u65f6\u95f4ms", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3\u53f7", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u901a\u4fe1\u8d85\u65f6ms", None))
        self.checkBox_openport.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u7aef\u53e3", None))
        self.groupBox_ADsets.setTitle(QCoreApplication.translate("Form", u"\u6a21\u62df\u91cf\u8bbe\u7f6e", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"\u65b0\u6fc0\u5149\u529f\u7387", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"\u672a\u5b9a\u4e49", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"AO2", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"\u65b0\u9001\u7c89\u7535\u538b1", None))
        self.label_50.setText(QCoreApplication.translate("Form", u"\u672a\u5b9a\u4e49", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"AO8", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"\u65b0\u6fc0\u5149\u5149\u6591", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"AO5", None))
        self.label.setText(QCoreApplication.translate("Form", u"AO1", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"AO7", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"AO6", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"AO3", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"AO4", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"\u65b0\u9001\u7c89\u7535\u538b1", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"\u672a\u5b9a\u4e49", None))
        self.label_53.setText(QCoreApplication.translate("Form", u"\u672a\u5b9a\u4e49", None))
        self.btn_setAO.setText(QCoreApplication.translate("Form", u"\u591a\u901a\u9053\u8bbe\u7f6eAO", None))
        self.btn_readDO.setText(QCoreApplication.translate("Form", u"\u8bfb\u53d6\u7ee7\u7535\u5668\u72b6\u6001", None))
        self.btn_readDI.setText(QCoreApplication.translate("Form", u"\u8bfb\u53d6DI\u72b6\u6001", None))
        self.btn_readAI.setText(QCoreApplication.translate("Form", u"\u8bfb\u53d6AI\u72b6\u6001", None))
    # retranslateUi

