#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/8 14:36
# @Author  : mihudan~
# @File    : QLabelEditable
# @Description : 

import sys
from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget
class EditableLabel(QWidget):
     def __init__(self,parent):
         super().__init__(parent)
         self.label = QLabel("Hello, World!")
         self.edit = QLineEdit()
         layout = QVBoxLayout()
         layout.addWidget(self.label)
         layout.addWidget(self.edit)
         self.setLayout(layout)
         self.edit.setHidden(True)
         self.label.mouseDoubleClickEvent = self.editLabel
         self.edit.returnPressed.connect(self.finish_edit)

     def editLabel(self, event):
         self.label.setHidden(True)
         self.edit.setText(self.label.text())
         self.edit.setHidden(False)
         self.edit.setFocus()

     def finish_edit(self):
         """编辑完成后回车确认"""

         self.label.setHidden(False)
         self.label.setText(self.edit.text())
         self.edit.setHidden(True)

     def setAlignment(self,arg):
         self.label.setAlignment(arg)
         self.edit.setAlignment(arg)

     def setText(self,arg):
         self.label.setText(arg)
         self.edit.setText(arg)

if __name__ == '__main__':
 app = QApplication(sys.argv)
 window = EditableLabel()
 window.show()
 sys.exit(app.exec_())

