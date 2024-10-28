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
        self.w_path = QAction(MainWindow)
        self.w_path.setObjectName(u"w_path")
        self.center = QWidget(MainWindow)
        self.center.setObjectName(u"center")
        self.horizontalLayout = QHBoxLayout(self.center)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.treeWidget = QTreeWidget(self.center)
        font = QFont()
        font.setPointSize(8)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QSize(350, 0))
        self.treeWidget.setMaximumSize(QSize(350, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        self.treeWidget.setFont(font1)

        self.horizontalLayout.addWidget(self.treeWidget)

        self.frame = QFrame(self.center)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
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

        MainWindow.setCentralWidget(self.center)
        self.status = QStatusBar(MainWindow)
        self.status.setObjectName(u"status")
        MainWindow.setStatusBar(self.status)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setFont(font1)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.file_menu)
        self.toolBar.addAction(self.cl_open)
        self.toolBar.addAction(self.sb_open)
        self.toolBar.addAction(self.gy_open)
        self.toolBar.addAction(self.cx_open)
        self.toolBar.addAction(self.mx_open)
        self.toolBar.addAction(self.xm_open)
        self.toolBar.addAction(self.action_fresh)

        self.retranslateUi(MainWindow)

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
        self.action_path.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u9009\u62e9", None))
        self.action_fresh.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.action_other.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.file_menu.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.w_path.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u7d22\u5f15", None));
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

