# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_viewer.ui'
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
        MainWindow.resize(1340, 905)
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
        self.action_fresh = QAction(MainWindow)
        self.action_fresh.setObjectName(u"action_fresh")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_other = QAction(MainWindow)
        self.action_other.setObjectName(u"action_other")
        self.file_menu = QAction(MainWindow)
        self.file_menu.setObjectName(u"file_menu")
        self.center = QWidget(MainWindow)
        self.center.setObjectName(u"center")
        self.verticalLayout = QVBoxLayout(self.center)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.center)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeWidget = QTreeWidget(self.page)
        font = QFont()
        font.setPointSize(8)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy1)
        self.treeWidget.setMinimumSize(QSize(350, 0))
        self.treeWidget.setMaximumSize(QSize(350, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        self.treeWidget.setFont(font1)

        self.horizontalLayout.addWidget(self.treeWidget)

        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(500, 0))
        self.frame.setMaximumSize(QSize(10000, 16777215))
        self.frame.setStyleSheet(u"border: 1px solid rgb(150, 150, 150);\n"
"border-color: rgb(150, 150, 150);\n"
"background-color: rgb(232, 232, 232);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_2 = QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.treeWidget_2 = QTreeWidget(self.page_2)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setFont(0, font);
        self.treeWidget_2.setHeaderItem(__qtreewidgetitem1)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        self.treeWidget_2.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.treeWidget_2.sizePolicy().hasHeightForWidth())
        self.treeWidget_2.setSizePolicy(sizePolicy2)
        self.treeWidget_2.setMinimumSize(QSize(300, 0))
        self.treeWidget_2.setMaximumSize(QSize(500, 16777215))
        self.treeWidget_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.treeWidget_2)

        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setMinimumSize(QSize(500, 0))
        self.frame_2.setMaximumSize(QSize(10000, 16777215))
        self.frame_2.setStyleSheet(u"border: 1px solid rgb(150, 150, 150);\n"
"border-left-color: 1px solid rgb(255, 255, 255);\n"
"background-color: rgb(232, 232, 232);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.frame_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy4)
        self.tabWidget_2.setMinimumSize(QSize(0, 500))
        self.tabWidget_2.setFont(font1)
        self.tabWidget_2.setStyleSheet(u"border:0px;")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.table_cx_2 = QTableWidget(self.tab_4)
        self.table_cx_2.setObjectName(u"table_cx_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(10)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.table_cx_2.sizePolicy().hasHeightForWidth())
        self.table_cx_2.setSizePolicy(sizePolicy5)
        self.table_cx_2.setMinimumSize(QSize(500, 400))
        self.table_cx_2.setMaximumSize(QSize(5000, 5000))
        self.table_cx_2.setStyleSheet(u"QHeaderView::section {  \n"
"        background-color: rgb(172, 187, 203); /* \u80cc\u666f\u8272 */     \n"
"		color: rgb(20, 20, 20);/* \u8868\u5934\u6587\u5b57\u989c\u8272 */\n"
"        font-size: 18px; \n"
"		border:0px solid #7B95AF;\n"
"		border-bottom:1px solid #7B95AF;\n"
"		outline:1px;\n"
"    } ")
        self.table_cx_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.gridLayout_4.addWidget(self.table_cx_2, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_5 = QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.table_mx_2 = QTableWidget(self.tab_5)
        self.table_mx_2.setObjectName(u"table_mx_2")
        self.table_mx_2.setStyleSheet(u"QHeaderView::section {  \n"
"        background-color: rgb(172, 187, 203); /* \u80cc\u666f\u8272 */     \n"
"		color: rgb(20, 20, 20);/* \u8868\u5934\u6587\u5b57\u989c\u8272 */\n"
"        font-size: 18px; \n"
"		border:0px solid #7B95AF;\n"
"		border-bottom:1px solid #7B95AF;\n"
"		outline:1px;\n"
"    } ")

        self.gridLayout_5.addWidget(self.table_mx_2, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_6 = QGridLayout(self.tab_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.table_xm_2 = QTableWidget(self.tab_6)
        self.table_xm_2.setObjectName(u"table_xm_2")
        self.table_xm_2.setStyleSheet(u"QHeaderView::section {  \n"
"        background-color: rgb(172, 187, 203); /* \u80cc\u666f\u8272 */     \n"
"		color: rgb(20, 20, 20);/* \u8868\u5934\u6587\u5b57\u989c\u8272 */\n"
"        font-size: 18px; \n"
"		border:0px solid #7B95AF;\n"
"		border-bottom:1px solid #7B95AF;\n"
"		outline:1px;\n"
"    } ")

        self.gridLayout_6.addWidget(self.table_xm_2, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_6, "")

        self.verticalLayout_3.addWidget(self.tabWidget_2)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.center)
        self.status = QStatusBar(MainWindow)
        self.status.setObjectName(u"status")
        MainWindow.setStatusBar(self.status)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setFont(font1)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.file_menu)
        self.toolBar.addAction(self.show_all)
        self.toolBar.addAction(self.cl_open)
        self.toolBar.addAction(self.sb_open)
        self.toolBar.addAction(self.gy_open)
        self.toolBar.addAction(self.cx_open)
        self.toolBar.addAction(self.mx_open)
        self.toolBar.addAction(self.xm_open)
        self.toolBar.addAction(self.action_fresh)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)


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
        self.w_path.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.action_path.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u9009\u62e9", None))
        self.action_fresh.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.action_other.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.file_menu.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u7d22\u5f15", None));
        ___qtreewidgetitem1 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u7d22\u5f15", None));
#if QT_CONFIG(whatsthis)
        self.tabWidget_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u7a0b\u5e8f\u5e93</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u5e93", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u5e93", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u5e93", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

