# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUutnlV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from CustomWidgets.RightPara.QDoubleSlider import DoubleSlider

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1507, 1040)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setStyleSheet(u"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"# BY: WANDERSON M.PIMENTA\n"
"# PROJECT MADE WITH: Qt Designer and PySide6\n"
"# V: 1.0.0\n"
"#\n"
"# This project can be used freely for all uses, as long as they maintain the\n"
"# respective credits only in the Python scripts, any information in the visual\n"
"# interface (GUI) can be modified without any implication.\n"
"#\n"
"# There are limitations on Qt licenses if you want to use your products\n"
"# commercially, I recommend reading them on the official website:\n"
"# https://doc.qt.io/qtforpython/licenses.html\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"#styleSheet{\n"
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
"\n"
"#extraRightBox QWidget {\n"
"    color: #f"
                        "8f8f2;\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"#extraRightBox QLineEdit{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"    color: #44475a;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {\n"
"	background-color: #6272a4;\n"
"}\n"
"#topLogo {\n"
"	background-color: #62"
                        "72a4;\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; color: #f8f8f2; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #bd93f9; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#topMenu .QPushButton:pressed {\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
""
                        "    color: #f8f8f2;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid #6a7cb1;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: #5b6996;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: #f8f8f2;\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {\n"
"	background-color: #495474;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"\n"
""
                        "\n"
"#extraTopBg{\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid #6272a4;\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: lef"
                        "t;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{\n"
"	background-color: #6272a4;\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid #bd93f9;\n"
"}\n"
"#titleRightInfo{\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: #bd93f9; border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #ff79c6; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: #495474; }\n"
"#themeSettingsTopDetail { "
                        "background-color: #6272a4; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: #495474 }\n"
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"\n"
"#contentSettings .QPushButton{\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border:2px solid #5d6c99;\n"
"	color: #f8f8f2;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	background-color: transparent;\n"
"	border-top-left-radius:5px;\n"
"	border-bottom-right-radius:5px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#contentSettings .QPushButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"#contentSettings QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-backg"
                        "round-color: rgb(255, 121, 198);\n"
"    color: #000000;\n"
"}\n"
"\n"
"#contentSettings QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"#contentSettings QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"#contentSettings QSpinBox {\n"
" 	background-color: #FFFFFF;\n"
"	color: rgb(0,0,0);\n"
"    border-width: 3;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
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
""
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
"PlainTextEdit "
                        "*/\n"
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
"    "
                        "width: 20px;\n"
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
"    background: #6272a4;"
                        "\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #FFFFFF;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
""
                        "QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #FFFFFF;\n"
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
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b"
                        "9;\n"
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
"	color: rgb(255, 121, 198);\n"
"	background-color: #6272a4;\n"
"	padding: 10px;\n"
"	selection-background-color: #6272a4;\n"
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
"    background-color:"
                        " rgb(189, 147, 249);\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
""
                        "CommandLinkButton */\n"
"#pagesContainer QCommandLinkButton {\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"    border: 2px solid #ff79c6;\n"
"    color: #ff79c6;\n"
"}\n"
"#pagesContainer QCommandLinkButton:hover {\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: #6272a4;\n"
"}\n"
"#pagesContainer QCommandLinkButton:pressed {\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: #586796;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	background-color: rgb(98, 114, 164);\n"
"    color: #f8f8f2;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(98, 114, 164);\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Butto"
                        "n */\n"
"\n"
"QLabel#label_imgrgba {\n"
"    background-color: rgba(98, 114, 164, 50);\n"
"}\n"
"QLabel#label_hikimg {\n"
"    background-color: rgba(98, 114, 164, 50);\n"
"}\n"
"\n"
"\n"
"QWidget#widget {\n"
"    border: 2px solid #6272a4;\n"
"}\n"
"\n"
"QWidget#widget_2 {\n"
"    border: 2px solid #6272a4;\n"
"}\n"
"\n"
"QWidget#widget_2 {\n"
"    border: 2px solid #6272a4;\n"
"}\n"
"\n"
"\n"
"QTabWidget {\n"
"     border: none;\n"
"}\n"
"\n"
"\n"
"QTabWidget {\n"
"     border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#home QLineEdit {\n"
"background: transparent;\n"
"}\n"
"\n"
"\n"
"#edtExposureTime QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"#edtFrameRate QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid "
                        "#6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: rgb(10, 10, 10);\n"
"}\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuBg.sizePolicy().hasHeightForWidth())
        self.leftMenuBg.setSizePolicy(sizePolicy)
        self.leftMenuBg.setMinimumSize(QSize(200, 0))
        self.leftMenuBg.setMaximumSize(QSize(0, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(7)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.toggleBox)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_7)

        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/para.png);")

        self.horizontalLayout_32.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setAutoFillBackground(False)
        self.btn_home.setStyleSheet(u"background-image:url(:/myicons/images/Myicons/camera3.png);")
        self.btn_home.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy1.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy1)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/picture.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy1.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy1)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/point.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy1.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy1)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/cvs.png);")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_card_di = QPushButton(self.topMenu)
        self.btn_card_di.setObjectName(u"btn_card_di")
        sizePolicy1.setHeightForWidth(self.btn_card_di.sizePolicy().hasHeightForWidth())
        self.btn_card_di.setSizePolicy(sizePolicy1)
        self.btn_card_di.setMinimumSize(QSize(0, 45))
        self.btn_card_di.setFont(font)
        self.btn_card_di.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_card_di.setLayoutDirection(Qt.LeftToRight)
        self.btn_card_di.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/chip.png);")

        self.verticalLayout_8.addWidget(self.btn_card_di)

        self.btn_card_ai = QPushButton(self.topMenu)
        self.btn_card_ai.setObjectName(u"btn_card_ai")
        sizePolicy1.setHeightForWidth(self.btn_card_ai.sizePolicy().hasHeightForWidth())
        self.btn_card_ai.setSizePolicy(sizePolicy1)
        self.btn_card_ai.setMinimumSize(QSize(0, 45))
        self.btn_card_ai.setFont(font)
        self.btn_card_ai.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_card_ai.setLayoutDirection(Qt.LeftToRight)
        self.btn_card_ai.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/chip.png);")

        self.verticalLayout_8.addWidget(self.btn_card_ai)

        self.btn_db = QPushButton(self.topMenu)
        self.btn_db.setObjectName(u"btn_db")
        self.btn_db.setMinimumSize(QSize(0, 45))
        self.btn_db.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_db.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/db.png);")

        self.verticalLayout_8.addWidget(self.btn_db)

        self.btn_project = QPushButton(self.topMenu)
        self.btn_project.setObjectName(u"btn_project")
        self.btn_project.setMinimumSize(QSize(0, 45))
        self.btn_project.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/save.png);")

        self.verticalLayout_8.addWidget(self.btn_project)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraContent)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setTabletTracking(False)
        self.stackedWidget.setStyleSheet(u"")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"/*background-image: url(:/images/images/images/PyDracula_vertical.png);*/\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.verticalLayout_30 = QVBoxLayout(self.home)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.widgetDisplay = QWidget(self.home)
        self.widgetDisplay.setObjectName(u"widgetDisplay")
        sizePolicy.setHeightForWidth(self.widgetDisplay.sizePolicy().hasHeightForWidth())
        self.widgetDisplay.setSizePolicy(sizePolicy)
        self.horizontalLayout_24 = QHBoxLayout(self.widgetDisplay)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.groupBox_11 = QGroupBox(self.widgetDisplay)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.groupBox_11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_hikimg = QLabel(self.groupBox_11)
        self.label_hikimg.setObjectName(u"label_hikimg")
        self.label_hikimg.setMinimumSize(QSize(1000, 800))
        self.label_hikimg.setMaximumSize(QSize(1000, 800))
        self.label_hikimg.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_hikimg, 0, 0, 1, 1)


        self.horizontalLayout_24.addWidget(self.groupBox_11)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(1)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.radioButton_hik_isopen = QRadioButton(self.widgetDisplay)
        self.radioButton_hik_isopen.setObjectName(u"radioButton_hik_isopen")
        self.radioButton_hik_isopen.setMaximumSize(QSize(25, 25))

        self.verticalLayout_34.addWidget(self.radioButton_hik_isopen)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer)


        self.horizontalLayout_24.addLayout(self.verticalLayout_34)

        self.horizontalLayout_24.setStretch(0, 99)
        self.horizontalLayout_24.setStretch(1, 1)

        self.horizontalLayout_19.addWidget(self.widgetDisplay)


        self.verticalLayout_30.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_3)

        self.groupBox = QGroupBox(self.home)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(400, 0))
        self.groupBox.setMaximumSize(QSize(16777215, 400))
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.btn_calib = QPushButton(self.groupBox)
        self.btn_calib.setObjectName(u"btn_calib")
        self.btn_calib.setMinimumSize(QSize(0, 45))
        self.btn_calib.setMaximumSize(QSize(100, 16777215))
        self.btn_calib.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.btn_calib)

        self.btn_verificate = QPushButton(self.groupBox)
        self.btn_verificate.setObjectName(u"btn_verificate")
        self.btn_verificate.setMinimumSize(QSize(0, 45))
        self.btn_verificate.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_23.addWidget(self.btn_verificate)


        self.verticalLayout_21.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_20.addWidget(self.label_9)

        self.spinBox_shiftH = QSpinBox(self.groupBox)
        self.spinBox_shiftH.setObjectName(u"spinBox_shiftH")

        self.horizontalLayout_20.addWidget(self.spinBox_shiftH)


        self.verticalLayout_21.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_21.addWidget(self.label_10)

        self.spinBox_shiftW = QSpinBox(self.groupBox)
        self.spinBox_shiftW.setObjectName(u"spinBox_shiftW")

        self.horizontalLayout_21.addWidget(self.spinBox_shiftW)


        self.verticalLayout_21.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_22.addWidget(self.groupBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_4)


        self.verticalLayout_30.addLayout(self.horizontalLayout_22)

        self.stackedWidget.addWidget(self.home)
        self.page_zivid_img = QWidget()
        self.page_zivid_img.setObjectName(u"page_zivid_img")
        self.verticalLayout = QVBoxLayout(self.page_zivid_img)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_4 = QWidget(self.page_zivid_img)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.groupBox_10 = QGroupBox(self.widget_4)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_4 = QGridLayout(self.groupBox_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, -1, -1)
        self.label_imgrgba = QLabel(self.groupBox_10)
        self.label_imgrgba.setObjectName(u"label_imgrgba")
        self.label_imgrgba.setMinimumSize(QSize(800, 500))
        self.label_imgrgba.setMaximumSize(QSize(800, 500))

        self.gridLayout_4.addWidget(self.label_imgrgba, 0, 0, 1, 1)


        self.horizontalLayout_13.addWidget(self.groupBox_10)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget_4)

        self.btn_rgbviewdown = QPushButton(self.page_zivid_img)
        self.btn_rgbviewdown.setObjectName(u"btn_rgbviewdown")
        self.btn_rgbviewdown.setMaximumSize(QSize(999999, 10))
        self.btn_rgbviewdown.setLayoutDirection(Qt.RightToLeft)
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-arrow-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rgbviewdown.setIcon(icon4)

        self.verticalLayout.addWidget(self.btn_rgbviewdown)

        self.widget_3 = QWidget(self.page_zivid_img)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_8 = QGroupBox(self.widget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_2 = QGridLayout(self.groupBox_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.groupBox_8)


        self.horizontalLayout_10.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox_9 = QGroupBox(self.widget_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_3 = QGridLayout(self.groupBox_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.gridLayout_3.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.groupBox_9)


        self.horizontalLayout_10.addWidget(self.widget_2)


        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(2, 4)
        self.stackedWidget.addWidget(self.page_zivid_img)
        self.page_showpts = QWidget()
        self.page_showpts.setObjectName(u"page_showpts")
        self.verticalLayout_16 = QVBoxLayout(self.page_showpts)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_showpoints = QWidget(self.page_showpts)
        self.widget_showpoints.setObjectName(u"widget_showpoints")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(80)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_showpoints.sizePolicy().hasHeightForWidth())
        self.widget_showpoints.setSizePolicy(sizePolicy4)
        self.widget_showpoints.setMinimumSize(QSize(800, 500))
        self.widget_showpoints.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_16.addWidget(self.widget_showpoints)

        self.btn_pointviewdown = QPushButton(self.page_showpts)
        self.btn_pointviewdown.setObjectName(u"btn_pointviewdown")
        self.btn_pointviewdown.setMaximumSize(QSize(16777215, 10))
        self.btn_pointviewdown.setIcon(icon4)

        self.verticalLayout_16.addWidget(self.btn_pointviewdown)

        self.tableWidget_fault = QTableWidget(self.page_showpts)
        if (self.tableWidget_fault.columnCount() < 3):
            self.tableWidget_fault.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_fault.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_fault.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_fault.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget_fault.rowCount() < 40):
            self.tableWidget_fault.setRowCount(40)
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidget_fault.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(11, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(12, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(13, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(14, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(15, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(16, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(17, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(18, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(19, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(20, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(21, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(22, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(23, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(24, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(25, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(26, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(27, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(28, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(29, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(30, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(31, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(32, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(33, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(34, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(35, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(36, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_fault.setVerticalHeaderItem(37, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_fault.setItem(0, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_fault.setItem(0, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_fault.setItem(0, 2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_fault.setItem(1, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_fault.setItem(1, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_fault.setItem(1, 2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_fault.setItem(2, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_fault.setItem(2, 1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_fault.setItem(2, 2, __qtablewidgetitem49)
        self.tableWidget_fault.setObjectName(u"tableWidget_fault")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tableWidget_fault.sizePolicy().hasHeightForWidth())
        self.tableWidget_fault.setSizePolicy(sizePolicy5)
        palette = QPalette()
        brush = QBrush(QColor(51, 51, 51, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 255))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget_fault.setPalette(palette)
        self.tableWidget_fault.setFrameShape(QFrame.NoFrame)
        self.tableWidget_fault.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_fault.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_fault.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_fault.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_fault.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_fault.setShowGrid(True)
        self.tableWidget_fault.setGridStyle(Qt.SolidLine)
        self.tableWidget_fault.setSortingEnabled(False)
        self.tableWidget_fault.setRowCount(40)
        self.tableWidget_fault.horizontalHeader().setVisible(False)
        self.tableWidget_fault.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_fault.horizontalHeader().setDefaultSectionSize(400)
        self.tableWidget_fault.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_fault.verticalHeader().setVisible(False)
        self.tableWidget_fault.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_fault.verticalHeader().setHighlightSections(False)
        self.tableWidget_fault.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_16.addWidget(self.tableWidget_fault)

        self.stackedWidget.addWidget(self.page_showpts)
        self.page_csv = QWidget()
        self.page_csv.setObjectName(u"page_csv")
        self.verticalLayout_32 = QVBoxLayout(self.page_csv)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_csv = QVBoxLayout()
        self.verticalLayout_csv.setObjectName(u"verticalLayout_csv")

        self.verticalLayout_32.addLayout(self.verticalLayout_csv)

        self.groupBox_2 = QGroupBox(self.page_csv)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 400))
        self.horizontalLayout_31 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_5 = QSpacerItem(361, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_5)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.lineEdit_orangedit_path = QLineEdit(self.groupBox_2)
        self.lineEdit_orangedit_path.setObjectName(u"lineEdit_orangedit_path")
        self.lineEdit_orangedit_path.setMinimumSize(QSize(400, 0))
        self.lineEdit_orangedit_path.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_29.addWidget(self.lineEdit_orangedit_path)

        self.btn_orangedit = QPushButton(self.groupBox_2)
        self.btn_orangedit.setObjectName(u"btn_orangedit")
        self.btn_orangedit.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_29.addWidget(self.btn_orangedit)


        self.verticalLayout_33.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lineEdit_workvisual_path = QLineEdit(self.groupBox_2)
        self.lineEdit_workvisual_path.setObjectName(u"lineEdit_workvisual_path")
        self.lineEdit_workvisual_path.setMinimumSize(QSize(400, 0))
        self.lineEdit_workvisual_path.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_30.addWidget(self.lineEdit_workvisual_path)

        self.btn_workvisual = QPushButton(self.groupBox_2)
        self.btn_workvisual.setObjectName(u"btn_workvisual")
        self.btn_workvisual.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_30.addWidget(self.btn_workvisual)


        self.verticalLayout_33.addLayout(self.horizontalLayout_30)

        self.btn_pinn = QPushButton(self.groupBox_2)
        self.btn_pinn.setObjectName(u"btn_pinn")

        self.verticalLayout_33.addWidget(self.btn_pinn)


        self.horizontalLayout_31.addLayout(self.verticalLayout_33)

        self.horizontalSpacer_6 = QSpacerItem(361, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_6)


        self.verticalLayout_32.addWidget(self.groupBox_2)

        self.verticalLayout_32.setStretch(0, 99)
        self.verticalLayout_32.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_csv)
        self.page_card_di = QWidget()
        self.page_card_di.setObjectName(u"page_card_di")
        self.verticalLayout_31 = QVBoxLayout(self.page_card_di)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_card_di = QVBoxLayout()
        self.verticalLayout_card_di.setObjectName(u"verticalLayout_card_di")

        self.verticalLayout_31.addLayout(self.verticalLayout_card_di)

        self.stackedWidget.addWidget(self.page_card_di)
        self.page_card_ai = QWidget()
        self.page_card_ai.setObjectName(u"page_card_ai")
        self.verticalLayout_38 = QVBoxLayout(self.page_card_ai)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_card_ai = QVBoxLayout()
        self.verticalLayout_card_ai.setObjectName(u"verticalLayout_card_ai")

        self.verticalLayout_38.addLayout(self.verticalLayout_card_ai)

        self.stackedWidget.addWidget(self.page_card_ai)
        self.page_db = QWidget()
        self.page_db.setObjectName(u"page_db")
        self.verticalLayout_37 = QVBoxLayout(self.page_db)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_db = QVBoxLayout()
        self.verticalLayout_db.setObjectName(u"verticalLayout_db")

        self.verticalLayout_37.addLayout(self.verticalLayout_db)

        self.stackedWidget.addWidget(self.page_db)
        self.page_project = QWidget()
        self.page_project.setObjectName(u"page_project")
        self.horizontalLayout_33 = QHBoxLayout(self.page_project)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.stackedWidget.addWidget(self.page_project)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        sizePolicy.setHeightForWidth(self.extraRightBox.sizePolicy().hasHeightForWidth())
        self.extraRightBox.setSizePolicy(sizePolicy)
        self.extraRightBox.setMinimumSize(QSize(300, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setStyleSheet(u"")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setMaximumSize(QSize(16777215, 16777215))
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.tabWidget = QTabWidget(self.topMenus)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setDocumentMode(True)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_35 = QVBoxLayout(self.tab_2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.extraTopMenu = QFrame(self.tab_2)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_5 = QGroupBox(self.extraTopMenu)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.btn_connect_virtual = QPushButton(self.groupBox_5)
        self.btn_connect_virtual.setObjectName(u"btn_connect_virtual")
        sizePolicy1.setHeightForWidth(self.btn_connect_virtual.sizePolicy().hasHeightForWidth())
        self.btn_connect_virtual.setSizePolicy(sizePolicy1)
        self.btn_connect_virtual.setMinimumSize(QSize(0, 45))
        self.btn_connect_virtual.setFont(font)
        self.btn_connect_virtual.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_connect_virtual.setLayoutDirection(Qt.LeftToRight)
        self.btn_connect_virtual.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/connect.png);")

        self.verticalLayout_24.addWidget(self.btn_connect_virtual)

        self.btn_connect_camera = QPushButton(self.groupBox_5)
        self.btn_connect_camera.setObjectName(u"btn_connect_camera")
        sizePolicy1.setHeightForWidth(self.btn_connect_camera.sizePolicy().hasHeightForWidth())
        self.btn_connect_camera.setSizePolicy(sizePolicy1)
        self.btn_connect_camera.setMinimumSize(QSize(0, 45))
        self.btn_connect_camera.setFont(font)
        self.btn_connect_camera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_connect_camera.setLayoutDirection(Qt.LeftToRight)
        self.btn_connect_camera.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/open.png);")

        self.verticalLayout_24.addWidget(self.btn_connect_camera)

        self.btn_print_para = QPushButton(self.groupBox_5)
        self.btn_print_para.setObjectName(u"btn_print_para")
        sizePolicy1.setHeightForWidth(self.btn_print_para.sizePolicy().hasHeightForWidth())
        self.btn_print_para.setSizePolicy(sizePolicy1)
        self.btn_print_para.setMinimumSize(QSize(0, 45))
        self.btn_print_para.setFont(font)
        self.btn_print_para.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print_para.setLayoutDirection(Qt.LeftToRight)
        self.btn_print_para.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/para.png);")

        self.verticalLayout_24.addWidget(self.btn_print_para)


        self.verticalLayout_11.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.extraTopMenu)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(0, 45))
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.ComboDevices = QComboBox(self.groupBox_6)
        self.ComboDevices.setObjectName(u"ComboDevices")
        self.ComboDevices.setEnabled(True)

        self.verticalLayout_12.addWidget(self.ComboDevices)

        self.bnEnum = QPushButton(self.groupBox_6)
        self.bnEnum.setObjectName(u"bnEnum")
        sizePolicy1.setHeightForWidth(self.bnEnum.sizePolicy().hasHeightForWidth())
        self.bnEnum.setSizePolicy(sizePolicy1)
        self.bnEnum.setMinimumSize(QSize(0, 45))
        self.bnEnum.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/find.png);")

        self.verticalLayout_12.addWidget(self.bnEnum)

        self.bnOpen = QPushButton(self.groupBox_6)
        self.bnOpen.setObjectName(u"bnOpen")
        sizePolicy1.setHeightForWidth(self.bnOpen.sizePolicy().hasHeightForWidth())
        self.bnOpen.setSizePolicy(sizePolicy1)
        self.bnOpen.setMinimumSize(QSize(0, 45))
        self.bnOpen.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/open.png);")

        self.verticalLayout_12.addWidget(self.bnOpen)

        self.bnClose = QPushButton(self.groupBox_6)
        self.bnClose.setObjectName(u"bnClose")
        sizePolicy1.setHeightForWidth(self.bnClose.sizePolicy().hasHeightForWidth())
        self.bnClose.setSizePolicy(sizePolicy1)
        self.bnClose.setMinimumSize(QSize(0, 45))
        self.bnClose.setStyleSheet(u"\n"
"background-image: url(:/myicons/images/Myicons/stop.png);")

        self.verticalLayout_12.addWidget(self.bnClose)


        self.verticalLayout_11.addWidget(self.groupBox_6)


        self.verticalLayout_35.addWidget(self.extraTopMenu)

        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_25 = QVBoxLayout(self.tab)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy6)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 277, 487))
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy7)
        self.verticalLayout_29 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_29.setSpacing(15)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 10, -1, 10)
        self.radioButton = QRadioButton(self.groupBox_7)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(0, 20))
        self.radioButton.setChecked(True)

        self.horizontalLayout_14.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_7)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_14.addWidget(self.radioButton_2)

        self.checkBox_needppoints = QCheckBox(self.groupBox_7)
        self.checkBox_needppoints.setObjectName(u"checkBox_needppoints")
        self.checkBox_needppoints.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_14.addWidget(self.checkBox_needppoints)


        self.verticalLayout_20.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.btn_cupture = QPushButton(self.groupBox_7)
        self.btn_cupture.setObjectName(u"btn_cupture")
        sizePolicy1.setHeightForWidth(self.btn_cupture.sizePolicy().hasHeightForWidth())
        self.btn_cupture.setSizePolicy(sizePolicy1)
        self.btn_cupture.setMinimumSize(QSize(0, 40))
        self.btn_cupture.setFont(font)
        self.btn_cupture.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cupture.setLayoutDirection(Qt.LeftToRight)
        self.btn_cupture.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/start.png);")
        self.btn_cupture.setIconSize(QSize(0, 0))

        self.horizontalLayout_26.addWidget(self.btn_cupture)


        self.verticalLayout_20.addLayout(self.horizontalLayout_26)

        self.btn_show_colorpoints = QPushButton(self.groupBox_7)
        self.btn_show_colorpoints.setObjectName(u"btn_show_colorpoints")
        sizePolicy1.setHeightForWidth(self.btn_show_colorpoints.sizePolicy().hasHeightForWidth())
        self.btn_show_colorpoints.setSizePolicy(sizePolicy1)
        self.btn_show_colorpoints.setMinimumSize(QSize(0, 40))
        self.btn_show_colorpoints.setFont(font)
        self.btn_show_colorpoints.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_show_colorpoints.setLayoutDirection(Qt.LeftToRight)
        self.btn_show_colorpoints.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/color-filling.png);")

        self.verticalLayout_20.addWidget(self.btn_show_colorpoints)

        self.btn_zivid_save = QPushButton(self.groupBox_7)
        self.btn_zivid_save.setObjectName(u"btn_zivid_save")
        self.btn_zivid_save.setMinimumSize(QSize(0, 40))
        self.btn_zivid_save.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/save.png);")

        self.verticalLayout_20.addWidget(self.btn_zivid_save)


        self.verticalLayout_29.addWidget(self.groupBox_7)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_2)

        self.spinBox_ROIX = QSpinBox(self.groupBox_3)
        self.spinBox_ROIX.setObjectName(u"spinBox_ROIX")
        self.spinBox_ROIX.setMinimumSize(QSize(80, 0))
        self.spinBox_ROIX.setMaximum(9999)
        self.spinBox_ROIX.setValue(800)

        self.horizontalLayout_11.addWidget(self.spinBox_ROIX)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label)

        self.spinBox_ROIY = QSpinBox(self.groupBox_3)
        self.spinBox_ROIY.setObjectName(u"spinBox_ROIY")
        self.spinBox_ROIY.setMinimumSize(QSize(80, 0))
        self.spinBox_ROIY.setMinimum(0)
        self.spinBox_ROIY.setMaximum(9999)
        self.spinBox_ROIY.setSingleStep(1)
        self.spinBox_ROIY.setValue(300)

        self.horizontalLayout_11.addWidget(self.spinBox_ROIY)


        self.verticalLayout_22.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_4)

        self.spinBox_ROIH = QSpinBox(self.groupBox_3)
        self.spinBox_ROIH.setObjectName(u"spinBox_ROIH")
        self.spinBox_ROIH.setMinimumSize(QSize(80, 0))
        self.spinBox_ROIH.setMaximum(99999)
        self.spinBox_ROIH.setValue(800)

        self.horizontalLayout_12.addWidget(self.spinBox_ROIH)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_3)

        self.spinBox_ROIW = QSpinBox(self.groupBox_3)
        self.spinBox_ROIW.setObjectName(u"spinBox_ROIW")
        self.spinBox_ROIW.setMinimumSize(QSize(80, 0))
        self.spinBox_ROIW.setMaximum(9999)
        self.spinBox_ROIW.setSingleStep(1)
        self.spinBox_ROIW.setValue(800)

        self.horizontalLayout_12.addWidget(self.spinBox_ROIW)


        self.verticalLayout_22.addLayout(self.horizontalLayout_12)


        self.verticalLayout_29.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_nx = QLabel(self.groupBox_4)
        self.label_nx.setObjectName(u"label_nx")
        self.label_nx.setMinimumSize(QSize(0, 0))
        self.label_nx.setMaximumSize(QSize(16777215, 20))
        self.label_nx.setLayoutDirection(Qt.LeftToRight)
        self.label_nx.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_17.addWidget(self.label_nx)

        self.horizontalSlider_nx = DoubleSlider(self.groupBox_4)
        self.horizontalSlider_nx.setObjectName(u"horizontalSlider_nx")
        self.horizontalSlider_nx.setMinimum(-9999)
        self.horizontalSlider_nx.setMaximum(9999)
        self.horizontalSlider_nx.setOrientation(Qt.Horizontal)

        self.verticalLayout_17.addWidget(self.horizontalSlider_nx)


        self.verticalLayout_23.addLayout(self.verticalLayout_17)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_nz = QLabel(self.groupBox_4)
        self.label_nz.setObjectName(u"label_nz")
        self.label_nz.setMinimumSize(QSize(0, 0))
        self.label_nz.setMaximumSize(QSize(16777215, 20))
        self.label_nz.setLayoutDirection(Qt.LeftToRight)
        self.label_nz.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.label_nz)

        self.horizontalSlider_nz = DoubleSlider(self.groupBox_4)
        self.horizontalSlider_nz.setObjectName(u"horizontalSlider_nz")
        self.horizontalSlider_nz.setMinimum(-9999)
        self.horizontalSlider_nz.setMaximum(9999)
        self.horizontalSlider_nz.setOrientation(Qt.Horizontal)

        self.verticalLayout_19.addWidget(self.horizontalSlider_nz)


        self.verticalLayout_23.addLayout(self.verticalLayout_19)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_ny = QLabel(self.groupBox_4)
        self.label_ny.setObjectName(u"label_ny")
        self.label_ny.setMinimumSize(QSize(0, 0))
        self.label_ny.setMaximumSize(QSize(16777215, 20))
        self.label_ny.setLayoutDirection(Qt.LeftToRight)
        self.label_ny.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_18.addWidget(self.label_ny)

        self.horizontalSlider_ny = DoubleSlider(self.groupBox_4)
        self.horizontalSlider_ny.setObjectName(u"horizontalSlider_ny")
        self.horizontalSlider_ny.setMinimum(-9999)
        self.horizontalSlider_ny.setMaximum(9999)
        self.horizontalSlider_ny.setOrientation(Qt.Horizontal)

        self.verticalLayout_18.addWidget(self.horizontalSlider_ny)


        self.verticalLayout_23.addLayout(self.verticalLayout_18)


        self.verticalLayout_29.addWidget(self.groupBox_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_25.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_28 = QVBoxLayout(self.tab_3)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.groupGrab = QGroupBox(self.tab_3)
        self.groupGrab.setObjectName(u"groupGrab")
        self.verticalLayout_26 = QVBoxLayout(self.groupGrab)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.radioContinueMode = QRadioButton(self.groupGrab)
        self.radioContinueMode.setObjectName(u"radioContinueMode")

        self.horizontalLayout_15.addWidget(self.radioContinueMode)

        self.radioTriggerMode = QRadioButton(self.groupGrab)
        self.radioTriggerMode.setObjectName(u"radioTriggerMode")
        self.radioTriggerMode.setChecked(True)

        self.horizontalLayout_15.addWidget(self.radioTriggerMode)


        self.verticalLayout_26.addLayout(self.horizontalLayout_15)

        self.bnStart = QPushButton(self.groupGrab)
        self.bnStart.setObjectName(u"bnStart")
        self.bnStart.setMinimumSize(QSize(0, 45))
        self.bnStart.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/start.png);")

        self.verticalLayout_26.addWidget(self.bnStart)

        self.bnStop = QPushButton(self.groupGrab)
        self.bnStop.setObjectName(u"bnStop")
        self.bnStop.setMinimumSize(QSize(0, 45))
        self.bnStop.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/stop.png);")

        self.verticalLayout_26.addWidget(self.bnStop)

        self.bnSoftwareTrigger = QPushButton(self.groupGrab)
        self.bnSoftwareTrigger.setObjectName(u"bnSoftwareTrigger")
        self.bnSoftwareTrigger.setMinimumSize(QSize(0, 45))
        self.bnSoftwareTrigger.setLayoutDirection(Qt.LeftToRight)
        self.bnSoftwareTrigger.setAutoFillBackground(False)
        self.bnSoftwareTrigger.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/trigger.png);")

        self.verticalLayout_26.addWidget(self.bnSoftwareTrigger)

        self.bnSaveImage = QPushButton(self.groupGrab)
        self.bnSaveImage.setObjectName(u"bnSaveImage")
        self.bnSaveImage.setMinimumSize(QSize(0, 45))
        self.bnSaveImage.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/save.png);")

        self.verticalLayout_26.addWidget(self.bnSaveImage)


        self.verticalLayout_28.addWidget(self.groupGrab)

        self.groupParam = QGroupBox(self.tab_3)
        self.groupParam.setObjectName(u"groupParam")
        self.verticalLayout_27 = QVBoxLayout(self.groupParam)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.edtExposureTime = QLineEdit(self.groupParam)
        self.edtExposureTime.setObjectName(u"edtExposureTime")
        self.edtExposureTime.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_16.addWidget(self.edtExposureTime)

        self.label_5 = QLabel(self.groupParam)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_16.addWidget(self.label_5)


        self.verticalLayout_27.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.edtGain = QLineEdit(self.groupParam)
        self.edtGain.setObjectName(u"edtGain")
        self.edtGain.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_17.addWidget(self.edtGain)

        self.label_6 = QLabel(self.groupParam)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_17.addWidget(self.label_6)


        self.verticalLayout_27.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.edtFrameRate = QLineEdit(self.groupParam)
        self.edtFrameRate.setObjectName(u"edtFrameRate")
        self.edtFrameRate.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_18.addWidget(self.edtFrameRate)

        self.label_7 = QLabel(self.groupParam)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_18.addWidget(self.label_7)


        self.verticalLayout_27.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.lineEdit_hik_H = QLineEdit(self.groupParam)
        self.lineEdit_hik_H.setObjectName(u"lineEdit_hik_H")
        self.lineEdit_hik_H.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_27.addWidget(self.lineEdit_hik_H)

        self.label_8 = QLabel(self.groupParam)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_27.addWidget(self.label_8)


        self.verticalLayout_27.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.lineEdit_hik_W = QLineEdit(self.groupParam)
        self.lineEdit_hik_W.setObjectName(u"lineEdit_hik_W")
        self.lineEdit_hik_W.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_28.addWidget(self.lineEdit_hik_W)

        self.label_11 = QLabel(self.groupParam)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_28.addWidget(self.label_11)


        self.verticalLayout_27.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.radioButton_autopara = QRadioButton(self.groupParam)
        self.radioButton_autopara.setObjectName(u"radioButton_autopara")
        self.radioButton_autopara.setLayoutDirection(Qt.LeftToRight)
        self.radioButton_autopara.setChecked(True)

        self.horizontalLayout_25.addWidget(self.radioButton_autopara)


        self.verticalLayout_27.addLayout(self.horizontalLayout_25)

        self.bnGetParam = QPushButton(self.groupParam)
        self.bnGetParam.setObjectName(u"bnGetParam")
        self.bnGetParam.setMinimumSize(QSize(0, 45))
        self.bnGetParam.setLayoutDirection(Qt.LeftToRight)
        self.bnGetParam.setStyleSheet(u"background-image: url(:/myicons/images/Myicons/para.png);")
        self.bnGetParam.setIconSize(QSize(16, 16))

        self.verticalLayout_27.addWidget(self.bnGetParam)

        self.bnSetParam = QPushButton(self.groupParam)
        self.bnSetParam.setObjectName(u"bnSetParam")
        self.bnSetParam.setMinimumSize(QSize(0, 45))
        self.bnSetParam.setStyleSheet(u"background-image:url(:/myicons/images/Myicons/setpara.png)")

        self.verticalLayout_27.addWidget(self.bnSetParam)


        self.verticalLayout_28.addWidget(self.groupParam)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_14.addWidget(self.tabWidget)

        self.btn_all_capture = QPushButton(self.topMenus)
        self.btn_all_capture.setObjectName(u"btn_all_capture")

        self.verticalLayout_14.addWidget(self.btn_all_capture)


        self.verticalLayout_13.addWidget(self.topMenus)


        self.verticalLayout_7.addWidget(self.contentSettings)

        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"  \u9690\u85cf\u5de6\u83dc\u5355", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u754c\u9762", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u663e\u793a", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u4e91\u6570\u636e", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"IO\u6570\u636e", None))
        self.btn_card_di.setText(QCoreApplication.translate("MainWindow", u"\u6570\u5b57\u91cf", None))
        self.btn_card_ai.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u62df\u91cf", None))
        self.btn_db.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93", None))
        self.btn_project.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u83dc\u5355", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u83dc\u5355", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic; vertical-align:sub;\"/><span style=\" font-size:14pt; font-weight:600; font-style:italic; vertical-align:sub;\"/><span style=\" font-size:14pt;\">\u7ed3\u6784\u5149\u548c\u56fe\u50cf\u7684\u5b54\u6d1e\u7f3a\u9677\u68c0\u6d4b</span></p><p align=\"center\"><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u6d77\u5eb7RGB", None))
        self.label_hikimg.setText("")
        self.radioButton_hik_isopen.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5355\u5e94\u6027\u77e9\u9635\u89c6\u5dee\u50cf\u7d20\u8865\u507f", None))
        self.btn_calib.setText(QCoreApplication.translate("MainWindow", u"\u6807\u5b9a\u8f6c\u6362\u77e9\u9635", None))
        self.btn_verificate.setText(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1\u77e9\u9635\u8bef\u5dee", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u6784\u5149RGB", None))
        self.label_imgrgba.setText("")
        self.btn_rgbviewdown.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u6cd5\u5411\u91cf\u8d34\u56fe", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u6df1\u5ea6\u56fe", None))
        self.btn_pointviewdown.setText("")
        ___qtablewidgetitem = self.tableWidget_fault.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget_fault.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget_fault.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget_fault.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.tableWidget_fault.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget_fault.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget_fault.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.tableWidget_fault.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget_fault.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget_fault.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.tableWidget_fault.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.tableWidget_fault.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem12 = self.tableWidget_fault.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem13 = self.tableWidget_fault.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem14 = self.tableWidget_fault.verticalHeaderItem(11)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem15 = self.tableWidget_fault.verticalHeaderItem(12)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem16 = self.tableWidget_fault.verticalHeaderItem(13)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem17 = self.tableWidget_fault.verticalHeaderItem(14)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem18 = self.tableWidget_fault.verticalHeaderItem(15)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem19 = self.tableWidget_fault.verticalHeaderItem(16)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem20 = self.tableWidget_fault.verticalHeaderItem(17)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem21 = self.tableWidget_fault.verticalHeaderItem(18)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem22 = self.tableWidget_fault.verticalHeaderItem(19)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem23 = self.tableWidget_fault.verticalHeaderItem(20)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem24 = self.tableWidget_fault.verticalHeaderItem(21)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem25 = self.tableWidget_fault.verticalHeaderItem(22)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem26 = self.tableWidget_fault.verticalHeaderItem(23)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem27 = self.tableWidget_fault.verticalHeaderItem(24)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem28 = self.tableWidget_fault.verticalHeaderItem(25)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem29 = self.tableWidget_fault.verticalHeaderItem(26)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem30 = self.tableWidget_fault.verticalHeaderItem(27)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem31 = self.tableWidget_fault.verticalHeaderItem(28)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem32 = self.tableWidget_fault.verticalHeaderItem(29)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem33 = self.tableWidget_fault.verticalHeaderItem(30)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem34 = self.tableWidget_fault.verticalHeaderItem(31)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem35 = self.tableWidget_fault.verticalHeaderItem(32)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem36 = self.tableWidget_fault.verticalHeaderItem(33)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem37 = self.tableWidget_fault.verticalHeaderItem(34)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem38 = self.tableWidget_fault.verticalHeaderItem(35)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem39 = self.tableWidget_fault.verticalHeaderItem(36)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem40 = self.tableWidget_fault.verticalHeaderItem(37)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled = self.tableWidget_fault.isSortingEnabled()
        self.tableWidget_fault.setSortingEnabled(False)
        ___qtablewidgetitem41 = self.tableWidget_fault.item(0, 0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u4e91ID", None));
        ___qtablewidgetitem42 = self.tableWidget_fault.item(0, 1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u7684\u4e2a\u6570", None));
        ___qtablewidgetitem43 = self.tableWidget_fault.item(0, 2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u4fe1\u5ea6", None));
        self.tableWidget_fault.setSortingEnabled(__sortingEnabled)

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.lineEdit_orangedit_path.setText(QCoreApplication.translate("MainWindow", u"E:\\soft\\OrangeEdit\\OrangeEdit.exe", None))
        self.btn_orangedit.setText(QCoreApplication.translate("MainWindow", u"OrangeEdit", None))
        self.lineEdit_workvisual_path.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files (x86)\\KUKA\\WorkVisual 6.0\\WorkVisual.exe", None))
        self.btn_workvisual.setText(QCoreApplication.translate("MainWindow", u"WorkVisual", None))
        self.btn_pinn.setText(QCoreApplication.translate("MainWindow", u"PINN\u6a21\u578b\u9884\u6d4b\u9884\u6d4b", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"ZIVID", None))
        self.btn_connect_virtual.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u865a\u62df\u76f8\u673a", None))
        self.btn_connect_camera.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u76f8\u673a", None))
        self.btn_print_para.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u6355\u83b7\u53c2\u6570\u4fe1\u606f", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"HIK", None))
        self.bnEnum.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u627e\u8bbe\u5907", None))
        self.bnOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8bbe\u5907", None))
        self.bnClose.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u8bbe\u5907", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u8bbe\u5907", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u63a7\u5236", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u53c2\u6570", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u53c2\u6570", None))
        self.checkBox_needppoints.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u96c6\u70b9\u4e91", None))
        self.btn_cupture.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u96c6\u4e00\u5e27", None))
        self.btn_show_colorpoints.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5f69\u8272\u70b9\u4e91", None))
        self.btn_zivid_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"ROI", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_nx.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u9762\u6cd5\u5411\u91cfx: 0", None))
        self.label_nz.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u9762\u6cd5\u5411\u91cfz: 0", None))
        self.label_ny.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u9762\u6cd5\u5411\u91cfy: 0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u7ed3\u6784\u5149\u53c2\u6570", None))
        self.groupGrab.setTitle(QCoreApplication.translate("MainWindow", u"\u91c7\u96c6", None))
        self.radioContinueMode.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u7eed", None))
        self.radioTriggerMode.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u89e6\u53d1", None))
        self.bnStart.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u91c7\u96c6", None))
        self.bnStop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u91c7\u96c6", None))
        self.bnSoftwareTrigger.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u89e6\u53d1\u4e00\u6b21", None))
        self.bnSaveImage.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u56fe\u50cf", None))
        self.groupParam.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.edtExposureTime.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u66dd\u5149", None))
        self.edtGain.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u589e\u76ca", None))
        self.edtFrameRate.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5e27\u7387", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"RIO\u9ad8\u5ea6", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ROI\u5bbd\u5ea6", None))
        self.radioButton_autopara.setText(QCoreApplication.translate("MainWindow", u"           \u81ea\u52a8\u66dd\u5149 ", None))
        self.bnGetParam.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u53c2\u6570", None))
        self.bnSetParam.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u53c2\u6570", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u5de5\u4e1a\u76f8\u673a\u53c2\u6570", None))
        self.btn_all_capture.setText(QCoreApplication.translate("MainWindow", u"\u540c\u6b65\u91c7\u96c6", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Wang Kai", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

