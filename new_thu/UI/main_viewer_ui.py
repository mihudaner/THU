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
# -*- coding: utf-8 -*-

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1234, 910)
        MainWindow.setMaximumSize(QSize(1234, 16777215))
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
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_6 = QVBoxLayout(self.tab_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox = QGroupBox(self.tab_5)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.textBrowser = QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_4.addWidget(self.textBrowser)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(200, 100))

        self.horizontalLayout_16.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setMaximumSize(QSize(200, 100))
        self.pushButton_4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_16.addWidget(self.pushButton_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")

        self.horizontalLayout_8.addWidget(self.doubleSpinBox_6)


        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 2, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")

        self.horizontalLayout_9.addWidget(self.doubleSpinBox_7)


        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")

        self.horizontalLayout_7.addWidget(self.doubleSpinBox_5)


        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 2, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.groupBox_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.textBrowser_2 = QTextBrowser(self.tab_5)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_6.addWidget(self.textBrowser_2)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_2 = QPushButton(self.tab_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_17.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.tab_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_17.addWidget(self.pushButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.groupBox_3 = QGroupBox(self.tab_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_11.addWidget(self.label_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_2)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")

        self.horizontalLayout_11.addWidget(self.doubleSpinBox_9)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 60))

        self.verticalLayout_11.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 60))

        self.verticalLayout_11.addWidget(self.pushButton_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)


        self.horizontalLayout_13.addWidget(self.groupBox_3)

        self.textBrowser_3 = QTextBrowser(self.tab_6)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.horizontalLayout_13.addWidget(self.textBrowser_3)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)

        self.tableWidget = QTableWidget(self.tab_6)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_13.addWidget(self.tableWidget)


        self.horizontalLayout_12.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_15 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.groupBox_4 = QGroupBox(self.tab_7)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.label_6)

        self.tableWidget_2 = QTableWidget(self.groupBox_4)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        if (self.tableWidget_2.rowCount() < 19):
            self.tableWidget_2.setRowCount(19)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(16, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(17, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(18, __qtablewidgetitem32)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_5.addWidget(self.tableWidget_2)


        self.horizontalLayout_15.addWidget(self.groupBox_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_6 = QGroupBox(self.tab_7)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy1.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy1)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_10.addWidget(self.label_14)

        self.tableWidget_4 = QTableWidget(self.groupBox_6)
        if (self.tableWidget_4.columnCount() < 2):
            self.tableWidget_4.setColumnCount(2)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        if (self.tableWidget_4.rowCount() < 4):
            self.tableWidget_4.setRowCount(4)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, __qtablewidgetitem38)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tableWidget_4.sizePolicy().hasHeightForWidth())
        self.tableWidget_4.setSizePolicy(sizePolicy5)

        self.verticalLayout_10.addWidget(self.tableWidget_4)

        self.groupBox_5 = QGroupBox(self.groupBox_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy6)
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_9.addWidget(self.label_13)

        self.tableWidget_3 = QTableWidget(self.groupBox_5)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        if (self.tableWidget_3.rowCount() < 9):
            self.tableWidget_3.setRowCount(9)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, __qtablewidgetitem49)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        sizePolicy5.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy5)
        self.tableWidget_3.setMinimumSize(QSize(0, 350))

        self.verticalLayout_9.addWidget(self.tableWidget_3)


        self.verticalLayout_10.addWidget(self.groupBox_5)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 2)
        self.verticalLayout_10.setStretch(2, 1)

        self.verticalLayout_8.addWidget(self.groupBox_6)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_10 = QPushButton(self.tab_7)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.tab_7)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.tab_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.tab_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.pushButton_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_15.addLayout(self.verticalLayout_8)

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
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy7)
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
        self.tabWidget.setCurrentIndex(2)


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
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8865\u5f62\u533a\u57df", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Xmin", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ymax", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Xmax", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ymin", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4fdd\u5b58", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u622a\u9762\u663e\u793a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u8865\u5f62\u533a\u57df\u83b7\u53d6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6c89\u79ef\u7279\u5f81", None))
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u9053\u5bbd", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u5c42\u9ad8", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u62df\u6c89\u79ef", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u4fdd\u5b58", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5c42\u6570", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Y\u5750\u6807", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u9053\u6570", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Xmin", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ymin", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Xmax", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Ymax", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u6c89\u79ef\u6a21\u62df\u586b\u5145", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u6c89\u79ef\u53c2\u6570", None))
        self.label_6.setText("")
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u503c", None));
        ___qtablewidgetitem14 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"KUKA\u7a0b\u5e8f\u540d\u79f0", None));
        ___qtablewidgetitem15 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u65f6\u524d\u79fb\u52a8\u8ddd\u79bbX", None));
        ___qtablewidgetitem16 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u65f6\u524d\u79fb\u52a8\u8ddd\u79bbY", None));
        ___qtablewidgetitem17 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u65f6\u524d\u79fb\u52a8\u8ddd\u79bbZ", None));
        ___qtablewidgetitem18 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u5149\u6591\u7535\u538b", None));
        ___qtablewidgetitem19 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u524d\u4fdd\u62a4\u6c14\u65f6\u95f4", None));
        ___qtablewidgetitem20 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u540e\u4fdd\u62a4\u6c14\u65f6\u95f4", None));
        ___qtablewidgetitem21 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u901f\u5ea6", None));
        ___qtablewidgetitem22 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u7c89\u6876\u9009\u62e9", None));
        ___qtablewidgetitem23 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u7c89\u6876\u8f6c\u901f", None));
        ___qtablewidgetitem24 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u6fc0\u5149\u529f\u7387", None));
        ___qtablewidgetitem25 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u5c42\u603b\u6570", None));
        ___qtablewidgetitem26 = self.tableWidget_2.verticalHeaderItem(12)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u9053\u6b21\u6570", None));
        ___qtablewidgetitem27 = self.tableWidget_2.verticalHeaderItem(13)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u9053\u6b21\u957f\u5ea6", None));
        ___qtablewidgetitem28 = self.tableWidget_2.verticalHeaderItem(14)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u504f\u79fb\u8ddd\u79bb", None));
        ___qtablewidgetitem29 = self.tableWidget_2.verticalHeaderItem(15)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u540e\u79fb\u52a8\u8ddd\u79bbX", None));
        ___qtablewidgetitem30 = self.tableWidget_2.verticalHeaderItem(16)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem31 = self.tableWidget_2.verticalHeaderItem(17)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u7194\u8986\u540e\u79fb\u52a8\u8ddd\u79bbZ", None));
        ___qtablewidgetitem32 = self.tableWidget_2.verticalHeaderItem(18)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u5c42\u95f4\u505c\u7559\u65f6\u95f4", None));
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u76d1\u63a7\u9009\u7528", None))
        self.label_14.setText("")
        ___qtablewidgetitem33 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf", None));
        ___qtablewidgetitem34 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u503c", None));
        ___qtablewidgetitem35 = self.tableWidget_4.verticalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"CCD\u76f8\u673a", None));
        ___qtablewidgetitem36 = self.tableWidget_4.verticalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u6e29\u4eea", None));
        ___qtablewidgetitem37 = self.tableWidget_4.verticalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u901f\u76f8\u673a", None));
        ___qtablewidgetitem38 = self.tableWidget_4.verticalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u6fc0\u5149\u8f6e\u5ed3\u4eea", None));
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u5f62\u8c8c\u626b\u63cf", None))
        self.label_13.setText("")
        ___qtablewidgetitem39 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf", None));
        ___qtablewidgetitem40 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u503c", None));
        ___qtablewidgetitem41 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u524d\u7b49\u5f85\u65f6\u95f4", None));
        ___qtablewidgetitem42 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u524d\u79fb\u52a8\u65f6\u95f4X", None));
        ___qtablewidgetitem43 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u524d\u79fb\u52a8\u65f6\u95f4Y", None));
        ___qtablewidgetitem44 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u524d\u79fb\u52a8\u65f6\u95f4Z", None));
        ___qtablewidgetitem45 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u901f\u5ea6", None));
        ___qtablewidgetitem46 = self.tableWidget_3.verticalHeaderItem(5)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"X\u5411\u626b\u63cf\u79fb\u52a8\u8ddd\u79bb", None));
        ___qtablewidgetitem47 = self.tableWidget_3.verticalHeaderItem(6)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u540e\u79fb\u52a8\u65f6\u95f4X", None));
        ___qtablewidgetitem48 = self.tableWidget_3.verticalHeaderItem(7)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u540e\u79fb\u52a8\u65f6\u95f4Y", None));
        ___qtablewidgetitem49 = self.tableWidget_3.verticalHeaderItem(8)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u540e\u79fb\u52a8\u65f6\u95f4Z", None));
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u4fdd\u5b58", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u811a\u672c\u66f4\u65b0", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u751f\u6210", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u4f20\u8f93", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u6c89\u79ef\u7a0b\u5e8f\u751f\u6210", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6c89\u79ef\u5f62\u8c8c", None))
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

