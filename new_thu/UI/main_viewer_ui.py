# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_viewerYmJjDL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# from CustomWidget.QTreeWidgetv1 import MyTreeWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1203, 912)
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
"	background-position: left center;\n"
""
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
"	selection-color: rgb"
                        "(255, 255, 255);\n"
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
"    subcontrol-position: right;\n"
""
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
"     subcontrol-positio"
                        "n: bottom;\n"
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
"	background-image: url("
                        ":/icons/images/icons/cil-check-alt.png);\n"
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
""
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
"    margin: 0px;\n"
"	borde"
                        "r-radius: 5px;\n"
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
"/***https://github.com/gnibuoz/QRibbon/blob/master/QRib"
                        "bon/qribbon.ui***/\n"
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
"  border-bottom: none;\n"
"}"
                        "\n"
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
"		color:#fff;\n"
""
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
"     width: 24px;\n"
"	 height:24"
                        "px;\n"
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
"QToolButton:hover,QToolButton:checked{\n"
""
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy1)
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

        self.tabWidget_2.setCurrentIndex(0)


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
        self.action_updateIO.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u53cd\u9988", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u7194\u6c60\u72b6\u6001", None))
        self.label_showpre.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u663e\u793a", None))
        self.label_pre_w.setText(QCoreApplication.translate("MainWindow", u"\u7194\u6c60\u5bbd\u5ea6\uff1a   mm", None))
        self.btn_pre.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u9884\u6d4b", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u7194\u6c60\u5c3a\u5bf8", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u5de5\u827a\u66f4\u65b0", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem3 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

