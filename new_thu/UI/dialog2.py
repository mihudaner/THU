import sys
from PySide2.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMainWindow, \
    QHBoxLayout
from PySide2.QtGui import QIcon


class CustomInputDialog(QDialog):
    def __init__(self, parent, title, label, text=''):
        super().__init__(parent)

        # 设置窗口标题和图标
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('../resource/icon/main.png'))  # 设置窗口图标

        # 设置对话框宽度
        self.setFixedWidth(260)  # 设置固定宽度为 400 像素

        # 设置布局
        layout = QVBoxLayout()

        # 添加标签
        self.label = QLabel(label)
        layout.addWidget(self.label)

        # 添加文本输入框
        self.input_line = QLineEdit()
        layout.addWidget(self.input_line)

        # 创建按钮布局
        button_layout = QHBoxLayout()

        # 添加确定按钮
        self.ok_button = QPushButton("确定")
        self.ok_button.clicked.connect(self.accept)  # 点击按钮关闭对话框
        button_layout.addWidget(self.ok_button)

        # 添加取消按钮
        self.cancel_button = QPushButton("取消")
        self.cancel_button.clicked.connect(self.reject)  # 点击按钮关闭对话框
        button_layout.addWidget(self.cancel_button)

        # 将按钮布局添加到主布局
        layout.addLayout(button_layout)

        # # 设置样式表
        # self.setStyleSheet("""
        #     QDialog {
        #         background-color: #f0f0f0; /* 对话框背景颜色 */
        #     }
        #     QLabel {
        #         font-size: 16px;
        #     }
        #     QLineEdit {
        #         background-color: lightgray; /* 输入框背景颜色 */
        #         padding: 5px;
        #     }
        #     QPushButton {
        #         border: none;
        #         padding: 10px;
        #     }
        # """)

        # 设置布局
        self.setLayout(layout)

    def get_input(self):
        return self.input_line.text()

    @staticmethod
    def getText(parent, title, label, text=''):
        dialog = CustomInputDialog(parent, title, label, text='')
        result = dialog.exec_()  # 显示对话框并等待用户输入
        text = dialog.get_input() if result == QDialog.Accepted else None  # 获取输入
        return text, result == QDialog.Accepted  # 返回输入和状态