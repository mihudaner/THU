import sys
import socket
import threading
from PySide2.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QTextBrowser, QLabel
)
from PySide2.QtCore import Qt


class TcpClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TCP调试助手")
        self.resize(500, 400)

        layout = QVBoxLayout()

        ip_port_layout = QHBoxLayout()
        self.ip_input = QLineEdit("192.168.100.147")
        self.port_input = QLineEdit("54600")
        self.connect_button = QPushButton("连接")
        self.connect_button.clicked.connect(self.toggle_connection)

        ip_port_layout.addWidget(QLabel("IP:"))
        ip_port_layout.addWidget(self.ip_input)
        ip_port_layout.addWidget(QLabel("端口:"))
        ip_port_layout.addWidget(self.port_input)
        ip_port_layout.addWidget(self.connect_button)
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

        self.client_socket = None
        self.recv_thread = None
        self.connected = False

    def toggle_connection(self):
        if not self.connected:
            ip = self.ip_input.text()
            port = int(self.port_input.text())

            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((ip, port))
                self.connected = True
                self.output_browser.append(f"已连接到 {ip}:{port}")
                self.log_to_file(f"已连接到 {ip}:{port}")
                self.connect_button.setText("断开")

                self.recv_thread = threading.Thread(target=self.receive_data, daemon=True)
                self.recv_thread.start()

            except Exception as e:
                self.output_browser.append(f"连接失败: {e}")
                self.log_to_file(f"连接失败: {e}")
        else:
            self.disconnect()

    def disconnect(self):
        if self.client_socket:
            self.client_socket.close()
            self.client_socket = None
        self.connected = False
        self.output_browser.append("已断开连接")
        self.log_to_file("已断开连接")
        self.connect_button.setText("连接")

    def send_data(self):
        if self.connected and self.client_socket:
            try:
                message = self.send_input.text()
                self.client_socket.sendall(message.encode('ascii'))
                self.output_browser.append(f"发送: {message}")
                self.log_to_file(f"发送: {message}")
                self.send_input.clear()
            except Exception as e:
                self.output_browser.append(f"发送失败: {e}")
                self.log_to_file(f"发送失败: {e}")
        else:
            self.output_browser.append("未连接，无法发送")
            self.log_to_file("未连接，无法发送")

    def receive_data(self):
        while self.connected:
            try:
                data = self.client_socket.recv(1024)
                if data:
                    message = data.decode('ascii')
                    self.output_browser.append(f"接收: {message}")
                    self.log_to_file(f"接收: {message}")
                else:
                    self.output_browser.append("服务器断开连接")
                    self.log_to_file("服务器断开连接")
                    self.disconnect()
                    break
            except Exception as e:
                self.output_browser.append(f"接收出错: {e}")
                self.log_to_file(f"接收出错: {e}")
                break

    def log_to_file(self, message):
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(message + "\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TcpClient()
    window.show()
    sys.exit(app.exec_())
