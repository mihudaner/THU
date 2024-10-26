#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/2 1:24
# @Author  : mihudan~
# @File    : ProjectWindow
# @Description :

from .BasicMainwindow import *
from db.project import ProjectPage


class HIKWindow(MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("InitProjectPage")
        self.ui.projectpage = ProjectPage()
        self.ui.horizontalLayout_33.addWidget(self.ui.projectpage)
