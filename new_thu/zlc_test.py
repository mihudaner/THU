import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建按钮
        self.button = QPushButton("选择文件", self)
        self.button.setGeometry(20, 20, 100, 30)  # 位置和大小
        self.button.clicked.connect(self.open_file_dialog)

        # 创建显示路径的标签
        self.label = QLabel("未选择文件", self)
        self.label.setGeometry(20, 60, 400, 30)

    def open_file_dialog(self):
        # 创建文件对话框
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("文本文件 (*.txt);;所有文件 (*.*)")

        if file_dialog.exec_():
            # 获取选择的文件路径
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.label.setText(selected_files[0])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 450, 150)
    window.setWindowTitle("文件选择示例")
    window.show()
    sys.exit(app.exec_())
