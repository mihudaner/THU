# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectpage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .ProjectScrollArea import ProjectScrollArea


class Ui_ProjectPage(object):
    def setupUi(self, ProjectPage):
        if not ProjectPage.objectName():
            ProjectPage.setObjectName(u"ProjectPage")
        ProjectPage.resize(657, 522)
        ProjectPage.setContextMenuPolicy(Qt.PreventContextMenu)
        ProjectPage.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(ProjectPage)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget = QWidget(ProjectPage)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ProjectScrollArea = ProjectScrollArea(self.widget)
        self.ProjectScrollArea.setObjectName(u"ProjectScrollArea")

        self.verticalLayout_2.addWidget(self.ProjectScrollArea)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.btn_create = QPushButton(self.widget)
        self.btn_create.setObjectName(u"btn_create")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_create.sizePolicy().hasHeightForWidth())
        self.btn_create.setSizePolicy(sizePolicy)

        self.verticalLayout_36.addWidget(self.btn_create)

        self.btn_save = QPushButton(self.widget)
        self.btn_save.setObjectName(u"btn_save")

        self.verticalLayout_36.addWidget(self.btn_save)

        self.btn_open = QPushButton(self.widget)
        self.btn_open.setObjectName(u"btn_open")

        self.verticalLayout_36.addWidget(self.btn_open)

        self.btn_search = QPushButton(self.widget)
        self.btn_search.setObjectName(u"btn_search")

        self.verticalLayout_36.addWidget(self.btn_search)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.verticalLayout_36)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.horizontalLayout_12.addWidget(self.widget)


        self.retranslateUi(ProjectPage)

        QMetaObject.connectSlotsByName(ProjectPage)
    # setupUi

    def retranslateUi(self, ProjectPage):
        ProjectPage.setWindowTitle(QCoreApplication.translate("ProjectPage", u"Form", None))
        self.btn_create.setText(QCoreApplication.translate("ProjectPage", u"\u65b0\u5efa\u9879\u76ee", None))
        self.btn_save.setText(QCoreApplication.translate("ProjectPage", u"\u4fdd\u5b58\u9879\u76ee", None))
        self.btn_open.setText(QCoreApplication.translate("ProjectPage", u"\u6253\u5f00\u9879\u76ee", None))
        self.btn_search.setText(QCoreApplication.translate("ProjectPage", u"\u7b5b\u9009", None))
    # retranslateUi

