#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/14 14:26
# @Author  : mihudan~
# @File    : server.py
# @Description : 

import sys
import socket
import threading
from PySide2.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QTextBrowser, QLabel
)
from PySide2.QtCore import Qt


class TcpServer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TCP服务器测试界面")
        self.resize(500, 400)

        # UI布局
        layout = QVBoxLayout()

        ip_port_layout = QHBoxLayout()
        self.port_input = QLineEdit("12345")
        self.start_button = QPushButton("启动服务器")
        self.start_button.clicked.connect(self.start_server)

        ip_port_layout.addWidget(QLabel("端口:"))
        ip_port_layout.addWidget(self.port_input)
        ip_port_layout.addWidget(self.start_button)
        layout.addLayout(ip_port_layout)

        self.output_browser = QTextBrowser()
        layout.addWidget(self.output_browser)

        send_layout = QHBoxLayout()
        self.send_input = QLineEdit()
        self.send_button = QPushButton("发送")
        self.send_button.clicked.connect(self.send_data)
        send_layout.addWidget(self.send_input)
        send_layout.addWidget(self.send_button)
        layout.addLayout(send_layout)

        self.setLayout(layout)

        # TCP相关
        self.server_socket = None
        self.client_socket = None
        self.addr = None
        self.listen_thread = None
        self.recv_thread = None
        self.running = False

    def start_server(self):
        if self.running:
            self.output_browser.append("服务器已在运行")
            return

        port = int(self.port_input.text())

        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind(("127.0.0.1", port))
            self.server_socket.listen(1)
            self.output_browser.append(f"服务器已启动，监听 127.0.0.1:{port}")
            self.running = True

            # 等待客户端连接线程
            self.listen_thread = threading.Thread(target=self.wait_for_client, daemon=True)
            self.listen_thread.start()
        except Exception as e:
            self.output_browser.append(f"服务器启动失败: {e}")

    def wait_for_client(self):
        try:
            self.client_socket, self.addr = self.server_socket.accept()
            self.output_browser.append(f"客户端连接：{self.addr}")
            self.recv_thread = threading.Thread(target=self.receive_data, daemon=True)
            self.recv_thread.start()
        except Exception as e:
            self.output_browser.append(f"等待客户端失败: {e}")

    def receive_data(self):
        while self.running:
            try:
                data = self.client_socket.recv(1024)
                if data:
                    msg = data.decode('utf-8')
                    self.output_browser.append(f"收到: {msg}")
                else:
                    self.output_browser.append("客户端断开连接")
                    break
            except Exception as e:
                self.output_browser.append(f"接收失败: {e}")
                break

    def send_data(self):
        if self.client_socket:
            try:
                message = self.send_input.text()
                self.client_socket.sendall(message.encode('utf-8'))
                self.output_browser.append(f"发送: {message}")
                self.send_input.clear()
            except Exception as e:
                self.output_browser.append(f"发送失败: {e}")
        else:
            self.output_browser.append("无客户端连接，无法发送")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    server = TcpServer()
    server.show()
    sys.exit(app.exec_())
