#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/18 11:16
# @Author  : mihudan~
# @File    : QTreeWidgetv1
# @Description : 
from PySide2.QtWidgets import *


class MyTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super(MyTreeWidget, self).__init__(parent)

    def mouseDoubleClickEvent(self, event):
        # 获取双击的项
        item = self.itemAt(event.pos())
        if item:
            print(f"双击了: {item.text(0)}")
            # 在这里添加自定义的双击处理逻辑
            # 不调用父类的方法以阻止默认行为
        # 如果不需要进一步处理，可以直接返回
        # 否则，可以选择在特定条件下调用父类方法
        # super(MyTreeWidget, self).mouseDoubleClickEvent(event)
