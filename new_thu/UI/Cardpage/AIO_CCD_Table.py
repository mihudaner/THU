# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AIO_CCD_TableioGzPO.ui'
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
        Form.resize(894, 640)
        Form.setContextMenuPolicy(Qt.PreventContextMenu)
        Form.setStyleSheet(u"#styleSheet{\n"
"border: none;\n"
"margin: 0px;\n"
"}\n"
"\n"
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
"	padding-left: 5px;\n"
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
"QTableWidg"
                        "et::horizontalHeader {\n"
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
"	selection-background-color: rgb(255, 121, 198);\n"
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
"QPlainTex"
                        "tEdit {\n"
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
"    height: 8px;\n"
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
""
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
"    background-color: #6272a4;\n"
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
"     height:"
                        " 20px;\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
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
"QCheckBox::indica"
                        "tor:checked {\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(43, 87, 154);\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
""
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
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
"    background-co"
                        "lor: rgb(189, 147, 249);\n"
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
"	border-radius: 5px;\n"
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
""
                        "\n"
"QTabBar::tab {\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QGroupBox{\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	background-color: rgb(43, 87, 154);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_6 = QGroupBox(Form)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.groupBox_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.groupBox_6)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.groupBox_waveview_1 = QGroupBox(self.groupBox_6)
        self.groupBox_waveview_1.setObjectName(u"groupBox_waveview_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_waveview_1.sizePolicy().hasHeightForWidth())
        self.groupBox_waveview_1.setSizePolicy(sizePolicy1)
        self.groupBox_waveview_1.setMinimumSize(QSize(0, 0))
        self.groupBox_waveview_1.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.verticalLayout.addWidget(self.groupBox_waveview_1)

        self.groupBox_2 = QGroupBox(self.groupBox_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label_9)

        self.label_ccd_img = QLabel(self.groupBox_2)
        self.label_ccd_img.setObjectName(u"label_ccd_img")
        self.label_ccd_img.setStyleSheet(u"background-color: rgb(230, 230, 230);")

        self.verticalLayout_3.addWidget(self.label_ccd_img)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)

        self.gridLayout_3.addWidget(self.groupBox_6, 0, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_5 = QCheckBox(Form)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"    background-color: rgb(75, 0, 130); /* \u9009\u4e2d\u72b6\u6001\u80cc\u666f\u8272 */\n"
"}")
        self.checkBox_5.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_5, 4, 0, 1, 1)

        self.checkBox_1 = QCheckBox(Form)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"    background-color: rgb(98, 114, 165); /* \u9009\u4e2d\u72b6\u6001\u80cc\u666f\u8272 */\n"
"}")
        self.checkBox_1.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_1, 0, 0, 1, 1)

        self.checkBox_4 = QCheckBox(Form)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"    background-color: rgb(255, 215, 0); /* \u9009\u4e2d\u72b6\u6001\u80cc\u666f\u8272 */\n"
"}")
        self.checkBox_4.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_4, 3, 0, 1, 1)

        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"    background-color: rgb(50, 50, 50); /* \u9009\u4e2d\u72b6\u6001\u80cc\u666f\u8272 */\n"
"}")
        self.checkBox_2.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.checkBox_7 = QCheckBox(Form)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"    background-color: rgb(0, 191, 255); /* \u9009\u4e2d\u72b6\u6001\u80cc\u666f\u8272 */\n"
"}")
        self.checkBox_7.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_7, 6, 0, 1, 1)

        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"    background-color: rgb(60, 179, 113); /* \u9009\u4e2d\u72b6\u6001\u80cc\u666f\u8272 */\n"
"}")
        self.checkBox_3.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)

        self.checkBox_6 = QCheckBox(Form)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"    background-color: rgb(255, 105, 180); /* \u9009\u4e2d\u72b6\u6001\u80cc\u666f\u8272 */\n"
"}")
        self.checkBox_6.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_6, 5, 0, 1, 1)

        self.checkBox_8 = QCheckBox(Form)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"    background-color: rgb(255, 69, 0); /* \u9009\u4e2d\u72b6\u6001\u80cc\u666f\u8272 */\n"
"}")
        self.checkBox_8.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_8, 7, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"QRadioButton::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(255, 70, 46);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(50, 255,70 );\n"
"	border: 3px solid #bd93f9;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_enum = QPushButton(self.groupBox)
        self.btn_enum.setObjectName(u"btn_enum")

        self.horizontalLayout_5.addWidget(self.btn_enum)

        self.checkBox_openccd = QCheckBox(self.groupBox)
        self.checkBox_openccd.setObjectName(u"checkBox_openccd")
        self.checkBox_openccd.setStyleSheet(u"\n"
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
"url(:/icon/check_off.png)")

        self.horizontalLayout_5.addWidget(self.checkBox_openccd)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.comboBox_ccd_device = QComboBox(self.groupBox)
        self.comboBox_ccd_device.setObjectName(u"comboBox_ccd_device")

        self.verticalLayout_2.addWidget(self.comboBox_ccd_device)

        self.btn_ccd_capture = QPushButton(self.groupBox)
        self.btn_ccd_capture.setObjectName(u"btn_ccd_capture")

        self.verticalLayout_2.addWidget(self.btn_ccd_capture)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.Slider_exposure = QSlider(self.groupBox)
        self.Slider_exposure.setObjectName(u"Slider_exposure")
        self.Slider_exposure.setMaximum(10000)
        self.Slider_exposure.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.Slider_exposure)

        self.spinBox_exposure = QSpinBox(self.groupBox)
        self.spinBox_exposure.setObjectName(u"spinBox_exposure")
        self.spinBox_exposure.setMaximum(10000)
        self.spinBox_exposure.setSingleStep(1)
        self.spinBox_exposure.setValue(0)

        self.horizontalLayout_2.addWidget(self.spinBox_exposure)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.Slider1_gain = QSlider(self.groupBox)
        self.Slider1_gain.setObjectName(u"Slider1_gain")
        self.Slider1_gain.setMaximum(10000)
        self.Slider1_gain.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.Slider1_gain)

        self.spinBox_gain = QSpinBox(self.groupBox)
        self.spinBox_gain.setObjectName(u"spinBox_gain")
        self.spinBox_gain.setMaximum(10000)
        self.spinBox_gain.setSingleStep(1)
        self.spinBox_gain.setValue(0)

        self.horizontalLayout_3.addWidget(self.spinBox_gain)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.Slider_fps = QSlider(self.groupBox)
        self.Slider_fps.setObjectName(u"Slider_fps")
        self.Slider_fps.setMaximum(60)
        self.Slider_fps.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.Slider_fps)

        self.spinBox_fps = QSpinBox(self.groupBox)
        self.spinBox_fps.setObjectName(u"spinBox_fps")
        self.spinBox_fps.setMaximum(60)
        self.spinBox_fps.setSingleStep(1)
        self.spinBox_fps.setValue(0)

        self.horizontalLayout_4.addWidget(self.spinBox_fps)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.Slider_h = QSlider(self.groupBox)
        self.Slider_h.setObjectName(u"Slider_h")
        self.Slider_h.setMaximum(3000)
        self.Slider_h.setValue(800)
        self.Slider_h.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.Slider_h)

        self.spinBox_ccdh = QSpinBox(self.groupBox)
        self.spinBox_ccdh.setObjectName(u"spinBox_ccdh")
        self.spinBox_ccdh.setMaximum(3000)
        self.spinBox_ccdh.setValue(600)

        self.horizontalLayout_6.addWidget(self.spinBox_ccdh)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.Slider_w = QSlider(self.groupBox)
        self.Slider_w.setObjectName(u"Slider_w")
        self.Slider_w.setMaximum(3000)
        self.Slider_w.setValue(800)
        self.Slider_w.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.Slider_w)

        self.spinBox_ccdw = QSpinBox(self.groupBox)
        self.spinBox_ccdw.setObjectName(u"spinBox_ccdw")
        self.spinBox_ccdw.setMaximum(3000)
        self.spinBox_ccdw.setValue(600)

        self.horizontalLayout_8.addWidget(self.spinBox_ccdw)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.Slider_hoffset = QSlider(self.groupBox)
        self.Slider_hoffset.setObjectName(u"Slider_hoffset")
        self.Slider_hoffset.setMaximum(3000)
        self.Slider_hoffset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.Slider_hoffset)

        self.spinBox_ccd_hoffset = QSpinBox(self.groupBox)
        self.spinBox_ccd_hoffset.setObjectName(u"spinBox_ccd_hoffset")
        self.spinBox_ccd_hoffset.setMaximum(3000)

        self.horizontalLayout_10.addWidget(self.spinBox_ccd_hoffset)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.Slider_woffset = QSlider(self.groupBox)
        self.Slider_woffset.setObjectName(u"Slider_woffset")
        self.Slider_woffset.setMaximum(3000)
        self.Slider_woffset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.Slider_woffset)

        self.spinBox_ccd_woffset = QSpinBox(self.groupBox)
        self.spinBox_ccd_woffset.setObjectName(u"spinBox_ccd_woffset")
        self.spinBox_ccd_woffset.setMaximum(3000)

        self.horizontalLayout_9.addWidget(self.spinBox_ccd_woffset)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.btn_setpara = QPushButton(self.groupBox)
        self.btn_setpara.setObjectName(u"btn_setpara")

        self.verticalLayout_2.addWidget(self.btn_setpara)

        self.btn_savecddimg = QPushButton(self.groupBox)
        self.btn_savecddimg.setObjectName(u"btn_savecddimg")

        self.verticalLayout_2.addWidget(self.btn_savecddimg)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_7.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(Form)
        self.Slider_exposure.valueChanged.connect(self.spinBox_exposure.setValue)
        self.spinBox_exposure.valueChanged.connect(self.Slider_exposure.setValue)
        self.Slider1_gain.valueChanged.connect(self.spinBox_gain.setValue)
        self.spinBox_gain.valueChanged.connect(self.Slider1_gain.setValue)
        self.Slider_fps.valueChanged.connect(self.spinBox_fps.setValue)
        self.spinBox_fps.valueChanged.connect(self.Slider_fps.setValue)
        self.Slider_h.valueChanged.connect(self.spinBox_ccdh.setValue)
        self.Slider_w.valueChanged.connect(self.spinBox_ccdw.setValue)
        self.Slider_hoffset.valueChanged.connect(self.spinBox_ccd_hoffset.setValue)
        self.Slider_woffset.valueChanged.connect(self.spinBox_ccd_woffset.setValue)
        self.spinBox_ccdh.valueChanged.connect(self.Slider_h.setValue)
        self.spinBox_ccdw.valueChanged.connect(self.Slider_w.setValue)
        self.spinBox_ccd_hoffset.valueChanged.connect(self.Slider_hoffset.setValue)
        self.spinBox_ccd_woffset.valueChanged.connect(self.Slider_woffset.setValue)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"\u6a21\u62df\u91cf\u8f93\u5165", None))
        self.label_2.setText("")
        self.groupBox_waveview_1.setTitle("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"CCD\u56fe\u50cf:", None))
        self.label_9.setText("")
        self.label_ccd_img.setText("")
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"AI5", None))
        self.checkBox_1.setText(QCoreApplication.translate("Form", u"AI1", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"AI4", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"AI2", None))
        self.checkBox_7.setText(QCoreApplication.translate("Form", u"AI7", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"AI3", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"AI6", None))
        self.checkBox_8.setText(QCoreApplication.translate("Form", u"AI8", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"CCD\u53c2\u6570", None))
        self.label_10.setText("")
        self.radioButton.setText(QCoreApplication.translate("Form", u"DI1\u6307\u793a", None))
        self.btn_enum.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4b\u8bbe\u5907", None))
        self.checkBox_openccd.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u76f8\u673a", None))
        self.btn_ccd_capture.setText(QCoreApplication.translate("Form", u"\u62cd\u6444\u4e00\u5e27", None))
        self.label.setText(QCoreApplication.translate("Form", u"Exposure:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Gain:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"FPS", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"H", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"W", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Hoffset", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Woffset", None))
        self.btn_setpara.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u53c2\u6570", None))
        self.btn_savecddimg.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u56fe\u50cf", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"DI\u89e6\u53d1\u4fdd\u5b58\u683c\u5f0f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u4e0d\u4fdd\u5b58", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u4fdd\u5b58\u4e3ajpg", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u4fdd\u5b58\u4e3amp4", None))
        self.comboBox.setItemText(3, "")

    # retranslateUi

