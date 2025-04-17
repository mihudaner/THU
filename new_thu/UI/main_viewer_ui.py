# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_viewerhtRAXn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1214, 798)
        MainWindow.setMaximumSize(QSize(2500, 16777215))
        MainWindow.setStyleSheet(u"#styleSheet{\n"
"border: none;\n"
"margin: 0px;\n"
"}\n"
"\n"
"\n"
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
"\n"
"\n"
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
"QWidget{\n"
"	color: #333;\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"QToolTip {\n"
"	color: #333;\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"	background-image: none;\n"
"	background-position:"
                        " left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"\n"
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
"QPlainTextEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	se"
                        "lection-color: rgb(255, 255, 255);\n"
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
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-"
                        "position: right;\n"
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
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"  "
                        "   subcontrol-position: bottom;\n"
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
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;\n"
"	b"
                        "ackground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: #1272a4;\n"
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
""
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
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margi"
                        "n: 0px;\n"
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
"\n"
"QTabBar::tab {\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/***https://github.com/gnibuoz/QRibbo"
                        "n/blob/master/QRibbon/qribbon.ui***/\n"
"\n"
"QToolTip {\n"
"  border: 1px solid rgb(255,255,255);\n"
"  background: white;\n"
"  color: rgb(51, 51, 51);\n"
"}\n"
"\n"
"/**********\u83dc\u5355\u680f**********/\n"
"QMenuBar {\n"
"  background: rgb(255,255,255);\n"
"  border: 1px solid rgb(255,255,255);\n"
"  border-left: none;\n"
"  border-right: none;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  border: 1px solid transparent;\n"
"  padding: 5px 10px 5px 10px;\n"
"  background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:enabled {\n"
"  color: rgb(2, 65, 132);\n"
"}\n"
"\n"
"QMenuBar::item:!enabled {\n"
"  color: rgb(155, 155, 155);\n"
"}\n"
"\n"
"QMenuBar::item:enabled:selected {\n"
"  border-top-color: rgb(255,255,255);\n"
"  border-bottom-color: rgb(255,255,255);\n"
"  background: rgb(255,255,255);\n"
"}\n"
"\n"
"\n"
"/**********\u72b6\u6001\u680f**********/\n"
"QStatusBar {\n"
"  background: rgb(255,255,255);\n"
"  border: 1px solid rgb(255,255,255);\n"
"  border-left: none;\n"
"  border-right: none;\n"
"  border-b"
                        "ottom: none;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"  border: none;\n"
"  border-right: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"\n"
"\n"
"QTreeView::item,QTreeWidget::item {\n"
"    height: 25px;\n"
"    border: none;\n"
"    background-color: rgba(43,87,154,0);\n"
"}\n"
"\n"
"QTreeView::item:hover, QTreeView::branch:hover,\n"
"QTreeWidget::item:hover, QTreeWidget::branch:hover { \n"
"    background-color: rgba(43,87,154, 40);\n"
"}\n"
"\n"
"QTreeWidget::item:hover{ \n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgb(43,87,154);\n"
"}\n"
"\n"
"QTreeView::item:selected { \n"
"    background-color: rgba(200, 200, 200, 50);\n"
"	font-weight:bold;\n"
"	color: rgb(43, 87, 154);\n"
"}\n"
"\n"
"\n"
"QTabBar{\n"
"	background:rgb(43,87,154);\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected {\n"
"	  \n"
"       background:rgb(43,87,154);\n"
"      padding: 2px;\n"
"	  height:24px;\n"
"	  padding:2px 12px;\n"
"	  color:#fff;\n"
"  }\n"
"\n"
"\n"
"QTabBar::tab:hover:!selected {\n"
"     background:rgba(0,0,0,40);\n"
""
                        "		color:#fff;\n"
"  }\n"
"\n"
"\n"
"QTabBar::tab {\n"
"	background: rgb(243,243,243);\n"
"	  color: rgb(10, 10, 10);\n"
"color: rgb(10, 10, 10);\n"
"color: rgb(43,87,154);\n"
"\n"
"  }\n"
"\n"
"\n"
"QTabBar::tab:selected {\n"
"      border-color: #9B9B9B;\n"
"      border-bottom-color: #C2C7CB; /* same as pane color */\n"
"  }\n"
"\n"
"\n"
" QDockWidget::title {\n"
"     text-align: left; /* align the text to the left */\n"
"     background: rgb(230,230,230);\n"
"    background:rgb(43,87,154);\n"
"	 padding:6px 4px;\n"
"	 font-size:30pt;\n"
"\n"
"\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"     border: 1px solid rgb(255,0,255);\n"
"	 margin:0px;\n"
"	 color:rgb(240,240,240);\n"
"     background: #fff;\n"
"	color:rgb(10,10,10);\n"
"color:#eee;\n"
"	titlebar-close-icon: url(:/Resources/icon/dockwidget-close.png);\n"
"     titlebar-normal-icon: url(:/Resources/icon/dockwidget-float.png);\n"
" }\n"
"\n"
" QDockWidget::close-button, QDockWidget::float-button {\n"
"     border: 1px solid transparent;\n"
"     width: 24p"
                        "x;\n"
"	 height:24px;\n"
" }\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"      background: rgb(177,177,177);\n"
"	background:rgba(0,0,0,40);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"     padding: 1px -1px -1px 1px;\n"
"background:rgba(0,0,0,80);\n"
" }\n"
"\n"
" QDockWidget::close-button {\n"
"      subcontrol-position: top right;\n"
"      subcontrol-origin: margin;\n"
"	top:-1px;\n"
"	right:4px;\n"
"      position: absolute;\n"
"  }\n"
"\n"
" QDockWidget::float-button {\n"
"      subcontrol-position: top right;\n"
"      subcontrol-origin: margin;\n"
"	top:-1px;\n"
"      position: absolute;\n"
"	right:26px;\n"
"  }\n"
"\n"
"\n"
"QToolBar{\n"
"	background:transparent;\n"
"	background:rgb(43,87,154);\n"
"}\n"
"\n"
"\n"
"QToolButton{\n"
"	background:transparent;\n"
"	border:0px solid gray;\n"
"	color: rgb(255, 255, 255);\n"
"	margin:0;\n"
"}\n"
"\n"
"QToolButton{\n"
"	padding-bottom:10px;\n"
"}\n"
"\n"
"QToolButton:hover,QTool"
                        "Button:checked{\n"
"	border:1px solid rgba(100,100,100,100);\n"
"	border-radius:2px;\n"
"	background:rgb(255,255,255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"    \n"
"      /* 16px width + 4px for border = 20px allocated above */\n"
"      width: 16px;\n"
"	subcontrol-origin:margin;\n"
"subcontrol-position: bottom center;\n"
"	bottom:0px;\n"
"	left:0px;\n"
"	height:10px;\n"
"	width:100%\n"
" }\n"
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
"}\n"
"\n"
"")
        self.w_save = QAction(MainWindow)
        self.w_save.setObjectName(u"w_save")
        self.w_save_as = QAction(MainWindow)
        self.w_save_as.setObjectName(u"w_save_as")
        self.w_quit = QAction(MainWindow)
        self.w_quit.setObjectName(u"w_quit")
        self.cl_open = QAction(MainWindow)
        self.cl_open.setObjectName(u"cl_open")
        self.sb_open = QAction(MainWindow)
        self.sb_open.setObjectName(u"sb_open")
        self.gy_open = QAction(MainWindow)
        self.gy_open.setObjectName(u"gy_open")
        self.ku_all = QAction(MainWindow)
        self.ku_all.setObjectName(u"ku_all")
        self.ku_cl = QAction(MainWindow)
        self.ku_cl.setObjectName(u"ku_cl")
        self.ku_sb = QAction(MainWindow)
        self.ku_sb.setObjectName(u"ku_sb")
        self.show_all = QAction(MainWindow)
        self.show_all.setObjectName(u"show_all")
        self.cx_open = QAction(MainWindow)
        self.cx_open.setObjectName(u"cx_open")
        self.mx_open = QAction(MainWindow)
        self.mx_open.setObjectName(u"mx_open")
        self.help = QAction(MainWindow)
        self.help.setObjectName(u"help")
        self.xm_open = QAction(MainWindow)
        self.xm_open.setObjectName(u"xm_open")
        self.xm_filter = QAction(MainWindow)
        self.xm_filter.setObjectName(u"xm_filter")
        self.ku_gy = QAction(MainWindow)
        self.ku_gy.setObjectName(u"ku_gy")
        self.ku_cx = QAction(MainWindow)
        self.ku_cx.setObjectName(u"ku_cx")
        self.ku_mx = QAction(MainWindow)
        self.ku_mx.setObjectName(u"ku_mx")
        self.w_path = QAction(MainWindow)
        self.w_path.setObjectName(u"w_path")
        self.action_path = QAction(MainWindow)
        self.action_path.setObjectName(u"action_path")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_other = QAction(MainWindow)
        self.action_other.setObjectName(u"action_other")
        self.file_menu = QAction(MainWindow)
        self.file_menu.setObjectName(u"file_menu")
        self.action_updateIO = QAction(MainWindow)
        self.action_updateIO.setObjectName(u"action_updateIO")
        self.center = QWidget(MainWindow)
        self.center.setObjectName(u"center")
        self.horizontalLayout = QHBoxLayout(self.center)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.widget = QWidget(self.center)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border:1px solid rgb(86, 86, 86);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 0, 2, 2)
        self.tabWidget_2 = QTabWidget(self.widget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setMinimumSize(QSize(0, 0))
        self.tabWidget_2.setStyleSheet(u"border:0px solid rgb(86, 86, 86);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.tab_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QGroupBox{\n"
"border: 2px solid #6272a4;\n"
"}")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_18 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.groupBox = QGroupBox(self.tab_5)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.cpltAreaAcqFLabel = QLabel(self.groupBox)
        self.cpltAreaAcqFLabel.setObjectName(u"cpltAreaAcqFLabel")
        self.cpltAreaAcqFLabel.setStyleSheet(u"background-color: rgb(223, 223, 223);")

        self.verticalLayout_4.addWidget(self.cpltAreaAcqFLabel)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.cpltAreaAcqCFBtn = QPushButton(self.groupBox)
        self.cpltAreaAcqCFBtn.setObjectName(u"cpltAreaAcqCFBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cpltAreaAcqCFBtn.sizePolicy().hasHeightForWidth())
        self.cpltAreaAcqCFBtn.setSizePolicy(sizePolicy2)
        self.cpltAreaAcqCFBtn.setMaximumSize(QSize(200, 100))
        self.cpltAreaAcqCFBtn.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_16.addWidget(self.cpltAreaAcqCFBtn)

        self.cpltAreaAcqVFBtn = QPushButton(self.groupBox)
        self.cpltAreaAcqVFBtn.setObjectName(u"cpltAreaAcqVFBtn")
        self.cpltAreaAcqVFBtn.setMaximumSize(QSize(200, 100))

        self.horizontalLayout_16.addWidget(self.cpltAreaAcqVFBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.groupBox_2.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.xminDSBox = QDoubleSpinBox(self.groupBox_2)
        self.xminDSBox.setObjectName(u"xminDSBox")
        self.xminDSBox.setMinimum(-99.000000000000000)
        self.xminDSBox.setSingleStep(0.100000000000000)
        self.xminDSBox.setValue(-0.500000000000000)

        self.horizontalLayout_3.addWidget(self.xminDSBox)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.ymaxDSBox = QDoubleSpinBox(self.groupBox_2)
        self.ymaxDSBox.setObjectName(u"ymaxDSBox")
        self.ymaxDSBox.setMinimum(-1000.000000000000000)
        self.ymaxDSBox.setMaximum(1000.000000000000000)
        self.ymaxDSBox.setValue(200.000000000000000)

        self.horizontalLayout_8.addWidget(self.ymaxDSBox)


        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 2, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.xmaxDSBox = QDoubleSpinBox(self.groupBox_2)
        self.xmaxDSBox.setObjectName(u"xmaxDSBox")
        self.xmaxDSBox.setMinimum(-99.000000000000000)
        self.xmaxDSBox.setSingleStep(0.100000000000000)
        self.xmaxDSBox.setValue(0.500000000000000)

        self.horizontalLayout_9.addWidget(self.xmaxDSBox)


        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.yminDSBox = QDoubleSpinBox(self.groupBox_2)
        self.yminDSBox.setObjectName(u"yminDSBox")
        self.yminDSBox.setMinimum(-1000.000000000000000)
        self.yminDSBox.setMaximum(1000.000000000000000)
        self.yminDSBox.setSingleStep(1.000000000000000)
        self.yminDSBox.setValue(0.000000000000000)

        self.horizontalLayout_7.addWidget(self.yminDSBox)


        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 2, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.groupBox_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_5)

        self.cpltAreaShowLabel = QLabel(self.tab_5)
        self.cpltAreaShowLabel.setObjectName(u"cpltAreaShowLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cpltAreaShowLabel.sizePolicy().hasHeightForWidth())
        self.cpltAreaShowLabel.setSizePolicy(sizePolicy4)
        self.cpltAreaShowLabel.setStyleSheet(u"\n"
"border: 2px solid #6272a4;\n"
"")
        self.cpltAreaShowLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.cpltAreaShowLabel)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.cpltAreaAcqSaveBtn = QPushButton(self.tab_5)
        self.cpltAreaAcqSaveBtn.setObjectName(u"cpltAreaAcqSaveBtn")
        self.cpltAreaAcqSaveBtn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_17.addWidget(self.cpltAreaAcqSaveBtn)

        self.cpltAreaAcqShowBtn = QPushButton(self.tab_5)
        self.cpltAreaAcqShowBtn.setObjectName(u"cpltAreaAcqShowBtn")
        self.cpltAreaAcqShowBtn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_17.addWidget(self.cpltAreaAcqShowBtn)


        self.verticalLayout_14.addLayout(self.horizontalLayout_17)

        self.verticalLayout_14.setStretch(1, 1)

        self.horizontalLayout_18.addLayout(self.verticalLayout_14)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.groupBox_3 = QGroupBox(self.tab_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.groupBox_3.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_11.addWidget(self.label_5)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.dsfAvgWBox = QDoubleSpinBox(self.groupBox_3)
        self.dsfAvgWBox.setObjectName(u"dsfAvgWBox")
        self.dsfAvgWBox.setMinimum(-99.000000000000000)
        self.dsfAvgWBox.setValue(3.210000000000000)

        self.horizontalLayout_6.addWidget(self.dsfAvgWBox)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.dsfAvgHBox = QDoubleSpinBox(self.groupBox_3)
        self.dsfAvgHBox.setObjectName(u"dsfAvgHBox")
        self.dsfAvgHBox.setMinimum(-99.000000000000000)
        self.dsfAvgHBox.setValue(1.580000000000000)

        self.horizontalLayout_11.addWidget(self.dsfAvgHBox)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.dsfSimuDepBtn = QPushButton(self.groupBox_3)
        self.dsfSimuDepBtn.setObjectName(u"dsfSimuDepBtn")
        self.dsfSimuDepBtn.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_4.addWidget(self.dsfSimuDepBtn)

        self.dsfSavePthBtn = QPushButton(self.groupBox_3)
        self.dsfSavePthBtn.setObjectName(u"dsfSavePthBtn")
        self.dsfSavePthBtn.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_4.addWidget(self.dsfSavePthBtn)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)


        self.verticalLayout_6.addWidget(self.groupBox_3)


        self.horizontalLayout_13.addLayout(self.verticalLayout_6)

        self.dsfSimuDepShowLabel = QLabel(self.tab_6)
        self.dsfSimuDepShowLabel.setObjectName(u"dsfSimuDepShowLabel")
        self.dsfSimuDepShowLabel.setStyleSheet(u"\n"
"border: 2px solid #6272a4;\n"
"")
        self.dsfSimuDepShowLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.dsfSimuDepShowLabel)

        self.horizontalLayout_13.setStretch(1, 8)

        self.verticalLayout_13.addLayout(self.horizontalLayout_13)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.dsfSimuDepTable = QTableWidget(self.tab_6)
        if (self.dsfSimuDepTable.columnCount() < 7):
            self.dsfSimuDepTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.dsfSimuDepTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dsfSimuDepTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dsfSimuDepTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.dsfSimuDepTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.dsfSimuDepTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.dsfSimuDepTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.dsfSimuDepTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.dsfSimuDepTable.rowCount() < 7):
            self.dsfSimuDepTable.setRowCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.dsfSimuDepTable.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.dsfSimuDepTable.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.dsfSimuDepTable.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.dsfSimuDepTable.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.dsfSimuDepTable.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.dsfSimuDepTable.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.dsfSimuDepTable.setVerticalHeaderItem(6, __qtablewidgetitem13)
        self.dsfSimuDepTable.setObjectName(u"dsfSimuDepTable")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.dsfSimuDepTable.sizePolicy().hasHeightForWidth())
        self.dsfSimuDepTable.setSizePolicy(sizePolicy5)
        self.dsfSimuDepTable.setTabKeyNavigation(True)
        self.dsfSimuDepTable.setProperty("showDropIndicator", True)
        self.dsfSimuDepTable.horizontalHeader().setDefaultSectionSize(100)
        self.dsfSimuDepTable.verticalHeader().setVisible(False)
        self.dsfSimuDepTable.verticalHeader().setHighlightSections(True)

        self.verticalLayout_7.addWidget(self.dsfSimuDepTable)


        self.verticalLayout_13.addLayout(self.verticalLayout_7)

        self.verticalLayout_13.setStretch(0, 6)
        self.verticalLayout_13.setStretch(1, 5)

        self.horizontalLayout_12.addLayout(self.verticalLayout_13)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_15 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.scrollArea = QScrollArea(self.tab_7)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 762, 696))
        self.horizontalLayout_10 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.label_6)

        self.dcgParaTabel = QTableWidget(self.groupBox_4)
        if (self.dcgParaTabel.columnCount() < 2):
            self.dcgParaTabel.setColumnCount(2)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.dcgParaTabel.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.dcgParaTabel.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        if (self.dcgParaTabel.rowCount() < 19):
            self.dcgParaTabel.setRowCount(19)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(6, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(7, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(8, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(9, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(10, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(11, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(12, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(13, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(14, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(15, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(16, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(17, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.dcgParaTabel.setVerticalHeaderItem(18, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.dcgParaTabel.setItem(0, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.dcgParaTabel.setItem(0, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.dcgParaTabel.setItem(1, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.dcgParaTabel.setItem(1, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.dcgParaTabel.setItem(2, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.dcgParaTabel.setItem(2, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.dcgParaTabel.setItem(3, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.dcgParaTabel.setItem(3, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.dcgParaTabel.setItem(4, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.dcgParaTabel.setItem(4, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.dcgParaTabel.setItem(5, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.dcgParaTabel.setItem(5, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.dcgParaTabel.setItem(6, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.dcgParaTabel.setItem(6, 1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.dcgParaTabel.setItem(7, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.dcgParaTabel.setItem(7, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.dcgParaTabel.setItem(8, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.dcgParaTabel.setItem(8, 1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.dcgParaTabel.setItem(9, 0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.dcgParaTabel.setItem(9, 1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.dcgParaTabel.setItem(10, 0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.dcgParaTabel.setItem(10, 1, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.dcgParaTabel.setItem(11, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.dcgParaTabel.setItem(11, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.dcgParaTabel.setItem(12, 0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.dcgParaTabel.setItem(12, 1, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.dcgParaTabel.setItem(13, 0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.dcgParaTabel.setItem(13, 1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.dcgParaTabel.setItem(14, 0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.dcgParaTabel.setItem(14, 1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.dcgParaTabel.setItem(15, 0, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.dcgParaTabel.setItem(15, 1, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.dcgParaTabel.setItem(16, 0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.dcgParaTabel.setItem(16, 1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.dcgParaTabel.setItem(17, 0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.dcgParaTabel.setItem(17, 1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.dcgParaTabel.setItem(18, 0, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.dcgParaTabel.setItem(18, 1, __qtablewidgetitem72)
        self.dcgParaTabel.setObjectName(u"dcgParaTabel")
        sizePolicy5.setHeightForWidth(self.dcgParaTabel.sizePolicy().hasHeightForWidth())
        self.dcgParaTabel.setSizePolicy(sizePolicy5)
        self.dcgParaTabel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dcgParaTabel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dcgParaTabel.horizontalHeader().setDefaultSectionSize(80)

        self.verticalLayout_5.addWidget(self.dcgParaTabel)


        self.horizontalLayout_10.addWidget(self.groupBox_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy1.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy1)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_10.addWidget(self.label_14)

        self.dcgDetTabel = QTableWidget(self.groupBox_6)
        if (self.dcgDetTabel.columnCount() < 2):
            self.dcgDetTabel.setColumnCount(2)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.dcgDetTabel.setHorizontalHeaderItem(0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.dcgDetTabel.setHorizontalHeaderItem(1, __qtablewidgetitem74)
        if (self.dcgDetTabel.rowCount() < 4):
            self.dcgDetTabel.setRowCount(4)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.dcgDetTabel.setVerticalHeaderItem(0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.dcgDetTabel.setVerticalHeaderItem(1, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.dcgDetTabel.setVerticalHeaderItem(2, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.dcgDetTabel.setVerticalHeaderItem(3, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.dcgDetTabel.setItem(0, 0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.dcgDetTabel.setItem(0, 1, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.dcgDetTabel.setItem(1, 0, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.dcgDetTabel.setItem(1, 1, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.dcgDetTabel.setItem(2, 0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.dcgDetTabel.setItem(2, 1, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.dcgDetTabel.setItem(3, 0, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.dcgDetTabel.setItem(3, 1, __qtablewidgetitem86)
        self.dcgDetTabel.setObjectName(u"dcgDetTabel")
        sizePolicy5.setHeightForWidth(self.dcgDetTabel.sizePolicy().hasHeightForWidth())
        self.dcgDetTabel.setSizePolicy(sizePolicy5)
        self.dcgDetTabel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dcgDetTabel.horizontalHeader().setMinimumSectionSize(90)
        self.dcgDetTabel.horizontalHeader().setDefaultSectionSize(90)
        self.dcgDetTabel.verticalHeader().setMinimumSectionSize(20)

        self.verticalLayout_10.addWidget(self.dcgDetTabel)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 2)

        self.verticalLayout_8.addWidget(self.groupBox_6)

        self.dcgScanGroup = QGroupBox(self.scrollAreaWidgetContents)
        self.dcgScanGroup.setObjectName(u"dcgScanGroup")
        sizePolicy5.setHeightForWidth(self.dcgScanGroup.sizePolicy().hasHeightForWidth())
        self.dcgScanGroup.setSizePolicy(sizePolicy5)
        self.dcgScanGroup.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.dcgScanGroup)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_13 = QLabel(self.dcgScanGroup)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_9.addWidget(self.label_13)

        self.dcgScanTabel = QTableWidget(self.dcgScanGroup)
        if (self.dcgScanTabel.columnCount() < 2):
            self.dcgScanTabel.setColumnCount(2)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.dcgScanTabel.setHorizontalHeaderItem(0, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.dcgScanTabel.setHorizontalHeaderItem(1, __qtablewidgetitem88)
        if (self.dcgScanTabel.rowCount() < 9):
            self.dcgScanTabel.setRowCount(9)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.dcgScanTabel.setVerticalHeaderItem(0, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.dcgScanTabel.setVerticalHeaderItem(1, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.dcgScanTabel.setVerticalHeaderItem(2, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.dcgScanTabel.setVerticalHeaderItem(3, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.dcgScanTabel.setVerticalHeaderItem(4, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.dcgScanTabel.setVerticalHeaderItem(5, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.dcgScanTabel.setVerticalHeaderItem(6, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.dcgScanTabel.setVerticalHeaderItem(7, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.dcgScanTabel.setVerticalHeaderItem(8, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.dcgScanTabel.setItem(0, 0, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.dcgScanTabel.setItem(0, 1, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.dcgScanTabel.setItem(1, 0, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.dcgScanTabel.setItem(1, 1, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.dcgScanTabel.setItem(2, 0, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.dcgScanTabel.setItem(2, 1, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.dcgScanTabel.setItem(3, 0, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.dcgScanTabel.setItem(3, 1, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.dcgScanTabel.setItem(4, 0, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.dcgScanTabel.setItem(4, 1, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.dcgScanTabel.setItem(5, 0, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.dcgScanTabel.setItem(5, 1, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.dcgScanTabel.setItem(6, 0, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.dcgScanTabel.setItem(6, 1, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.dcgScanTabel.setItem(7, 0, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.dcgScanTabel.setItem(7, 1, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.dcgScanTabel.setItem(8, 0, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.dcgScanTabel.setItem(8, 1, __qtablewidgetitem115)
        self.dcgScanTabel.setObjectName(u"dcgScanTabel")
        sizePolicy5.setHeightForWidth(self.dcgScanTabel.sizePolicy().hasHeightForWidth())
        self.dcgScanTabel.setSizePolicy(sizePolicy5)
        self.dcgScanTabel.setMinimumSize(QSize(0, 350))
        self.dcgScanTabel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dcgScanTabel.horizontalHeader().setMinimumSectionSize(90)
        self.dcgScanTabel.horizontalHeader().setDefaultSectionSize(90)
        self.dcgScanTabel.verticalHeader().setMinimumSectionSize(20)
        self.dcgScanTabel.verticalHeader().setDefaultSectionSize(37)

        self.verticalLayout_9.addWidget(self.dcgScanTabel)


        self.verticalLayout_8.addWidget(self.dcgScanGroup)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.dcgParaSaveBtn = QPushButton(self.scrollAreaWidgetContents)
        self.dcgParaSaveBtn.setObjectName(u"dcgParaSaveBtn")
        self.dcgParaSaveBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.dcgParaSaveBtn)

        self.dcgCodeUpdateBtn = QPushButton(self.scrollAreaWidgetContents)
        self.dcgCodeUpdateBtn.setObjectName(u"dcgCodeUpdateBtn")
        self.dcgCodeUpdateBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.dcgCodeUpdateBtn)

        self.dcgCodeGenBtn = QPushButton(self.scrollAreaWidgetContents)
        self.dcgCodeGenBtn.setObjectName(u"dcgCodeGenBtn")
        self.dcgCodeGenBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.dcgCodeGenBtn)

        self.dcgCodeTransBtn = QPushButton(self.scrollAreaWidgetContents)
        self.dcgCodeTransBtn.setObjectName(u"dcgCodeTransBtn")
        self.dcgCodeTransBtn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.dcgCodeTransBtn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_10.addLayout(self.verticalLayout_8)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_15.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_7, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout = QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_showpre = QLabel(self.tab_3)
        self.label_showpre.setObjectName(u"label_showpre")
        self.label_showpre.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_showpre)

        self.label_pre_w = QLabel(self.tab_3)
        self.label_pre_w.setObjectName(u"label_pre_w")
        self.label_pre_w.setMaximumSize(QSize(16777215, 50))
        self.label_pre_w.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_pre_w)

        self.btn_pre = QPushButton(self.tab_3)
        self.btn_pre.setObjectName(u"btn_pre")

        self.verticalLayout.addWidget(self.btn_pre)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")

        self.horizontalLayout_2.addWidget(self.tabWidget_2)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.center)
        self.status = QStatusBar(MainWindow)
        self.status.setObjectName(u"status")
        MainWindow.setStatusBar(self.status)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.toolBar.setFont(font)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setEnabled(True)
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeWidget = QTreeWidget(self.dockWidgetContents)
        font1 = QFont()
        font1.setPointSize(8)
        self.treeWidget.headerItem().setText(0, "")
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font1);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy6)
        self.treeWidget.setMinimumSize(QSize(360, 0))
        self.treeWidget.setMaximumSize(QSize(16777215, 16777215))
        self.treeWidget.setFont(font)
        self.treeWidget.setAnimated(True)

        self.verticalLayout_2.addWidget(self.treeWidget)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)

        self.toolBar.addAction(self.file_menu)
        self.toolBar.addAction(self.show_all)
        self.toolBar.addAction(self.cl_open)
        self.toolBar.addAction(self.sb_open)
        self.toolBar.addAction(self.gy_open)
        self.toolBar.addAction(self.cx_open)
        self.toolBar.addAction(self.mx_open)
        self.toolBar.addAction(self.xm_open)
        self.toolBar.addAction(self.action_updateIO)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.w_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.w_save_as.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.w_quit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.cl_open.setText(QCoreApplication.translate("MainWindow", u"\u6750\u6599", None))
#if QT_CONFIG(tooltip)
        self.cl_open.setToolTip(QCoreApplication.translate("MainWindow", u"\u5c55\u793a\u6750\u6599\u5e93", None))
#endif // QT_CONFIG(tooltip)
        self.sb_open.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907", None))
#if QT_CONFIG(tooltip)
        self.sb_open.setToolTip(QCoreApplication.translate("MainWindow", u"\u5c55\u793a\u8bbe\u5907\u5e93", None))
#endif // QT_CONFIG(tooltip)
        self.gy_open.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u827a", None))
#if QT_CONFIG(tooltip)
        self.gy_open.setToolTip(QCoreApplication.translate("MainWindow", u"\u5c55\u793a\u5de5\u827a\u5e93", None))
#endif // QT_CONFIG(tooltip)
        self.ku_all.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8", None))
        self.ku_all.setIconText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8", None))
        self.ku_cl.setText(QCoreApplication.translate("MainWindow", u"\u6750\u6599", None))
        self.ku_sb.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907", None))
        self.show_all.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8", None))
#if QT_CONFIG(tooltip)
        self.show_all.setToolTip(QCoreApplication.translate("MainWindow", u"\u5c55\u793a\u6570\u636e\u5e93", None))
#endif // QT_CONFIG(tooltip)
        self.cx_open.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f", None))
        self.mx_open.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u6587\u6863", None))
        self.xm_open.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee", None))
#if QT_CONFIG(tooltip)
        self.xm_open.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#endif // QT_CONFIG(tooltip)
        self.xm_filter.setText(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009", None))
        self.ku_gy.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u827a", None))
        self.ku_cx.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f", None))
        self.ku_mx.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
        self.w_path.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u8def\u5f84", None))
        self.action_path.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u9009\u62e9", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.action_other.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.file_menu.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.action_updateIO.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u827a", None))
#if QT_CONFIG(tooltip)
        self.action_updateIO.setToolTip(QCoreApplication.translate("MainWindow", u"\u5de5\u827a", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u53cd\u9988", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5f62\u8c8c\u70b9\u4e91", None))
        self.label_2.setText("")
        self.cpltAreaAcqFLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6587\u4ef6", None))
        self.cpltAreaAcqCFBtn.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.cpltAreaAcqVFBtn.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8865\u5f62\u533a\u57df", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Xmin", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ymax", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Xmax", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ymin", None))
        self.label.setText("")
        self.cpltAreaShowLabel.setText(QCoreApplication.translate("MainWindow", u"\u672a\u9009\u62e9\u6587\u4ef6", None))
        self.cpltAreaAcqSaveBtn.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4fdd\u5b58", None))
        self.cpltAreaAcqShowBtn.setText(QCoreApplication.translate("MainWindow", u"\u622a\u9762\u663e\u793a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u8865\u5f62\u533a\u57df\u83b7\u53d6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6c89\u79ef\u7279\u5f81", None))
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u9053\u5bbd", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u5c42\u9ad8", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.dsfSimuDepBtn.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u62df\u6c89\u79ef", None))
        self.dsfSavePthBtn.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u4fdd\u5b58", None))
        self.dsfSimuDepShowLabel.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u6a21\u62df\u6c89\u79ef\u751f\u6210", None))
        ___qtablewidgetitem = self.dsfSimuDepTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5c42\u6570", None));
        ___qtablewidgetitem1 = self.dsfSimuDepTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Y\u5750\u6807", None));
        ___qtablewidgetitem2 = self.dsfSimuDepTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u9053\u6570", None));
        ___qtablewidgetitem3 = self.dsfSimuDepTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Xmin", None));
        ___qtablewidgetitem4 = self.dsfSimuDepTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ymin", None));
        ___qtablewidgetitem5 = self.dsfSimuDepTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Xmax", None));
        ___qtablewidgetitem6 = self.dsfSimuDepTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Ymax", None));
        ___qtablewidgetitem7 = self.dsfSimuDepTable.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.dsfSimuDepTable.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.dsfSimuDepTable.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.dsfSimuDepTable.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.dsfSimuDepTable.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem12 = self.dsfSimuDepTable.verticalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem13 = self.dsfSimuDepTable.verticalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u6c89\u79ef\u6a21\u62df\u586b\u5145", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u6c89\u79ef\u53c2\u6570", None))
        self.label_6.setText("")
        ___qtablewidgetitem14 = self.dcgParaTabel.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf", None));
        ___qtablewidgetitem15 = self.dcgParaTabel.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u503c", None));
        ___qtablewidgetitem16 = self.dcgParaTabel.verticalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"KUKA\u7a0b\u5e8f\u540d\u79f0", None));
        ___qtablewidgetitem17 = self.dcgParaTabel.verticalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u65f6\u524d\u79fb\u52a8\u8ddd\u79bbX", None));
        ___qtablewidgetitem18 = self.dcgParaTabel.verticalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u65f6\u524d\u79fb\u52a8\u8ddd\u79bbY", None));
        ___qtablewidgetitem19 = self.dcgParaTabel.verticalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u65f6\u524d\u79fb\u52a8\u8ddd\u79bbZ", None));
        ___qtablewidgetitem20 = self.dcgParaTabel.verticalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u5149\u6591\u7535\u538b", None));
        ___qtablewidgetitem21 = self.dcgParaTabel.verticalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u524d\u4fdd\u62a4\u6c14\u65f6\u95f4", None));
        ___qtablewidgetitem22 = self.dcgParaTabel.verticalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u540e\u4fdd\u62a4\u6c14\u65f6\u95f4", None));
        ___qtablewidgetitem23 = self.dcgParaTabel.verticalHeaderItem(7)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u901f\u5ea6", None));
        ___qtablewidgetitem24 = self.dcgParaTabel.verticalHeaderItem(8)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u7c89\u6876\u9009\u62e9", None));
        ___qtablewidgetitem25 = self.dcgParaTabel.verticalHeaderItem(9)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u7c89\u6876\u8f6c\u901f", None));
        ___qtablewidgetitem26 = self.dcgParaTabel.verticalHeaderItem(10)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u6fc0\u5149\u529f\u7387", None));
        ___qtablewidgetitem27 = self.dcgParaTabel.verticalHeaderItem(11)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u5c42\u603b\u6570", None));
        ___qtablewidgetitem28 = self.dcgParaTabel.verticalHeaderItem(12)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u9053\u6b21\u6570", None));
        ___qtablewidgetitem29 = self.dcgParaTabel.verticalHeaderItem(13)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u9053\u6b21\u957f\u5ea6", None));
        ___qtablewidgetitem30 = self.dcgParaTabel.verticalHeaderItem(14)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u504f\u79fb\u8ddd\u79bb", None));
        ___qtablewidgetitem31 = self.dcgParaTabel.verticalHeaderItem(15)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u540e\u79fb\u52a8\u8ddd\u79bbX", None));
        ___qtablewidgetitem32 = self.dcgParaTabel.verticalHeaderItem(16)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u540e\u79fb\u52a8\u8ddd\u79bbY", None));
        ___qtablewidgetitem33 = self.dcgParaTabel.verticalHeaderItem(17)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u540e\u79fb\u52a8\u8ddd\u79bbZ", None));
        ___qtablewidgetitem34 = self.dcgParaTabel.verticalHeaderItem(18)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u5c42\u95f4\u505c\u7559\u65f6\u95f4", None));

        __sortingEnabled = self.dcgParaTabel.isSortingEnabled()
        self.dcgParaTabel.setSortingEnabled(False)
        ___qtablewidgetitem35 = self.dcgParaTabel.item(0, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Program_Name", None));
        ___qtablewidgetitem36 = self.dcgParaTabel.item(0, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"L7_160_10", None));
        ___qtablewidgetitem37 = self.dcgParaTabel.item(1, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Before_Deposition_X", None));
        ___qtablewidgetitem38 = self.dcgParaTabel.item(1, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"59.38", None));
        ___qtablewidgetitem39 = self.dcgParaTabel.item(2, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Before_Deposition_Y", None));
        ___qtablewidgetitem40 = self.dcgParaTabel.item(2, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem41 = self.dcgParaTabel.item(3, 0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Before_Deposition_Z", None));
        ___qtablewidgetitem42 = self.dcgParaTabel.item(3, 1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"-10", None));
        ___qtablewidgetitem43 = self.dcgParaTabel.item(4, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Laser_Spot", None));
        ___qtablewidgetitem44 = self.dcgParaTabel.item(4, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"0.3", None));
        ___qtablewidgetitem45 = self.dcgParaTabel.item(5, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Protection_Gas_Before_Deposition", None));
        ___qtablewidgetitem46 = self.dcgParaTabel.item(5, 1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem47 = self.dcgParaTabel.item(6, 0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Protection_Gas_After_Deposition", None));
        ___qtablewidgetitem48 = self.dcgParaTabel.item(6, 1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem49 = self.dcgParaTabel.item(7, 0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Deposition_Speed", None));
        ___qtablewidgetitem50 = self.dcgParaTabel.item(7, 1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"0.005", None));
        ___qtablewidgetitem51 = self.dcgParaTabel.item(8, 0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Choose_Powder", None));
        ___qtablewidgetitem52 = self.dcgParaTabel.item(9, 0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Powder_Delivery_Speed", None));
        ___qtablewidgetitem53 = self.dcgParaTabel.item(9, 1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"0.075", None));
        ___qtablewidgetitem54 = self.dcgParaTabel.item(10, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Laser_Power", None));
        ___qtablewidgetitem55 = self.dcgParaTabel.item(10, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"0.625", None));
        ___qtablewidgetitem56 = self.dcgParaTabel.item(11, 0)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Layer_Sum", None));
        ___qtablewidgetitem57 = self.dcgParaTabel.item(11, 1)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem58 = self.dcgParaTabel.item(12, 0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Pass_Number", None));
        ___qtablewidgetitem59 = self.dcgParaTabel.item(12, 1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem60 = self.dcgParaTabel.item(13, 0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Pass_Distance", None));
        ___qtablewidgetitem61 = self.dcgParaTabel.item(13, 1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"30", None));
        ___qtablewidgetitem62 = self.dcgParaTabel.item(14, 0)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Offset_Distance ", None));
        ___qtablewidgetitem63 = self.dcgParaTabel.item(14, 1)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem64 = self.dcgParaTabel.item(15, 0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"After_Deposition_X", None));
        ___qtablewidgetitem65 = self.dcgParaTabel.item(15, 1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem66 = self.dcgParaTabel.item(16, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"After_Deposition_Y", None));
        ___qtablewidgetitem67 = self.dcgParaTabel.item(16, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem68 = self.dcgParaTabel.item(17, 0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"After_Deposition_Z", None));
        ___qtablewidgetitem69 = self.dcgParaTabel.item(17, 1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"1.58", None));
        ___qtablewidgetitem70 = self.dcgParaTabel.item(18, 0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Wait_ between_Layers", None));
        ___qtablewidgetitem71 = self.dcgParaTabel.item(18, 1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"120", None));
        self.dcgParaTabel.setSortingEnabled(__sortingEnabled)

        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u76d1\u63a7\u9009\u7528", None))
        self.label_14.setText("")
        ___qtablewidgetitem72 = self.dcgDetTabel.horizontalHeaderItem(0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf", None));
        ___qtablewidgetitem73 = self.dcgDetTabel.horizontalHeaderItem(1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"\u503c", None));
        ___qtablewidgetitem74 = self.dcgDetTabel.verticalHeaderItem(0)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"CCD\u76f8\u673a", None));
        ___qtablewidgetitem75 = self.dcgDetTabel.verticalHeaderItem(1)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u6e29\u4eea", None));
        ___qtablewidgetitem76 = self.dcgDetTabel.verticalHeaderItem(2)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u901f\u76f8\u673a", None));
        ___qtablewidgetitem77 = self.dcgDetTabel.verticalHeaderItem(3)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"\u6fc0\u5149\u8f6e\u5ed3\u4eea", None));

        __sortingEnabled1 = self.dcgDetTabel.isSortingEnabled()
        self.dcgDetTabel.setSortingEnabled(False)
        ___qtablewidgetitem78 = self.dcgDetTabel.item(0, 0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"GongYe_CCD", None));
        ___qtablewidgetitem79 = self.dcgDetTabel.item(0, 1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"TRUE", None));
        ___qtablewidgetitem80 = self.dcgDetTabel.item(1, 0)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Dian_Temperature", None));
        ___qtablewidgetitem81 = self.dcgDetTabel.item(1, 1)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"TRUE", None));
        ___qtablewidgetitem82 = self.dcgDetTabel.item(2, 0)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"GaoSu_Camera", None));
        ___qtablewidgetitem83 = self.dcgDetTabel.item(2, 1)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"TRUE", None));
        ___qtablewidgetitem84 = self.dcgDetTabel.item(3, 0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Laser_LunKuo", None));
        ___qtablewidgetitem85 = self.dcgDetTabel.item(3, 1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"TRUE", None));
        self.dcgDetTabel.setSortingEnabled(__sortingEnabled1)

        self.dcgScanGroup.setTitle(QCoreApplication.translate("MainWindow", u"\u5f62\u8c8c\u626b\u63cf", None))
        self.label_13.setText("")
        ___qtablewidgetitem86 = self.dcgScanTabel.horizontalHeaderItem(0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf", None));
        ___qtablewidgetitem87 = self.dcgScanTabel.horizontalHeaderItem(1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"\u503c", None));
        ___qtablewidgetitem88 = self.dcgScanTabel.verticalHeaderItem(0)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u524d\u79fb\u52a8\u8ddd\u79bbX", None));
        ___qtablewidgetitem89 = self.dcgScanTabel.verticalHeaderItem(1)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u524d\u79fb\u52a8\u8ddd\u79bbY", None));
        ___qtablewidgetitem90 = self.dcgScanTabel.verticalHeaderItem(2)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u524d\u79fb\u52a8\u8ddd\u79bbZ", None));
        ___qtablewidgetitem91 = self.dcgScanTabel.verticalHeaderItem(3)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u524d\u7b49\u5f85\u65f6\u95f4", None));
        ___qtablewidgetitem92 = self.dcgScanTabel.verticalHeaderItem(4)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u901f\u5ea6", None));
        ___qtablewidgetitem93 = self.dcgScanTabel.verticalHeaderItem(5)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Y\u5411\u626b\u63cf\u79fb\u52a8\u8ddd\u79bb", None));
        ___qtablewidgetitem94 = self.dcgScanTabel.verticalHeaderItem(6)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u540e\u79fb\u52a8\u8ddd\u79bbX", None));
        ___qtablewidgetitem95 = self.dcgScanTabel.verticalHeaderItem(7)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u540e\u79fb\u52a8\u8ddd\u79bbY", None));
        ___qtablewidgetitem96 = self.dcgScanTabel.verticalHeaderItem(8)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u540e\u79fb\u52a8\u8ddd\u79bbZ", None));

        __sortingEnabled2 = self.dcgScanTabel.isSortingEnabled()
        self.dcgScanTabel.setSortingEnabled(False)
        ___qtablewidgetitem97 = self.dcgScanTabel.item(0, 0)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Before_Scanning_Y", None));
        ___qtablewidgetitem98 = self.dcgScanTabel.item(0, 1)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"-200", None));
        ___qtablewidgetitem99 = self.dcgScanTabel.item(1, 0)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Before_Scanning_Y", None));
        ___qtablewidgetitem100 = self.dcgScanTabel.item(1, 1)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"-15", None));
        ___qtablewidgetitem101 = self.dcgScanTabel.item(2, 0)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Before_Scanning_Z", None));
        ___qtablewidgetitem102 = self.dcgScanTabel.item(2, 1)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem103 = self.dcgScanTabel.item(3, 0)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"Wait_Before_Scanning", None));
        ___qtablewidgetitem104 = self.dcgScanTabel.item(3, 1)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"55", None));
        ___qtablewidgetitem105 = self.dcgScanTabel.item(4, 0)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"Scanning_Speed", None));
        ___qtablewidgetitem106 = self.dcgScanTabel.item(4, 1)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"0.005", None));
        ___qtablewidgetitem107 = self.dcgScanTabel.item(5, 0)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"Scanning_Y_Distacne", None));
        ___qtablewidgetitem108 = self.dcgScanTabel.item(5, 1)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"-200", None));
        ___qtablewidgetitem109 = self.dcgScanTabel.item(6, 0)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"After_Scanning_X", None));
        ___qtablewidgetitem110 = self.dcgScanTabel.item(6, 1)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem111 = self.dcgScanTabel.item(7, 0)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"After_Scanning_Y", None));
        ___qtablewidgetitem112 = self.dcgScanTabel.item(7, 1)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"30", None));
        ___qtablewidgetitem113 = self.dcgScanTabel.item(8, 0)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"After_Scanning_Z", None));
        ___qtablewidgetitem114 = self.dcgScanTabel.item(8, 1)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"40", None));
        self.dcgScanTabel.setSortingEnabled(__sortingEnabled2)

        self.dcgParaSaveBtn.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u4fdd\u5b58", None))
        self.dcgCodeUpdateBtn.setText(QCoreApplication.translate("MainWindow", u"\u811a\u672c\u66f4\u65b0", None))
        self.dcgCodeGenBtn.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u751f\u6210", None))
        self.dcgCodeTransBtn.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u4f20\u8f93", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u6c89\u79ef\u7a0b\u5e8f\u751f\u6210", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6c89\u79ef\u5f62\u8c8c", None))
        self.label_showpre.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u663e\u793a", None))
        self.label_pre_w.setText(QCoreApplication.translate("MainWindow", u"\u7194\u6c60\u5bbd\u5ea6\uff1a   mm", None))
        self.btn_pre.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u9884\u6d4b", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u7194\u6c60\u5c3a\u5bf8", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u5de5\u827a\u66f4\u65b0", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))

        __sortingEnabled3 = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem3 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled3)

    # retranslateUi

