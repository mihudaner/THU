#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/18 15:26
# @Author  : mihudan~
# @File    : TimeDialog
# @Description : 
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer

class TimedConfirmDialog(QDialog):
    def __init__(self, message, timeout=3, on_confirm=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("警示⚠️")
        self.timeout = timeout
        self.remaining_time = timeout
        self.on_confirm = on_confirm

        self.label = QLabel(f"{message}\n{self.remaining_time}s")
        self.btn_yes = QPushButton("是")
        self.btn_no = QPushButton("否")

        self.btn_yes.clicked.connect(self.confirm)
        self.btn_no.clicked.connect(self.reject)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_yes)
        btn_layout.addWidget(self.btn_no)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def update_timer(self):
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.timer.stop()
            self.reject()  # 超时未操作，自动关闭
        else:
            self.label.setText(f"沉积连续异常\n是否终止？\n{self.remaining_time}s")

    def confirm(self):
        if self.on_confirm:
            self.on_confirm()
        self.accept()