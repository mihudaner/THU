import sys
import time
from io import BytesIO

import numpy as np
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel
from PySide2.QtCore import QThread, QObject, Signal, Qt
from PySide2.QtGui import QPixmap
import pandas as pd
import matplotlib.pyplot as plt
# 设置中文字体为SimHei，解决中文显示及负号显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ======================================================================
# Worker 类：封装后台任务逻辑
# ======================================================================
class FileLoaderWorker(QObject):
    data_loaded = Signal(bytes)  # 发送PNG图像数据
    error_occurred = Signal(str)
    finished = Signal()

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        try:
            t1=time.time()
            png_data = cpltArea(self.file_path, -0.5, 0.5, 0, 200)
            t2 = time.time()
            print(t2-t1)
            self.data_loaded.emit(png_data)
        except Exception as e:
            self.error_occurred.emit(f"加载失败：{str(e)}")
        finally:
            self.finished.emit()


# ======================================================================
# 主窗口类
# ======================================================================
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.thread = None
        self.worker = None

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel("点击按钮选择 .xyz 文件", alignment=Qt.AlignCenter)
        self.image_label = QLabel()  # 新增用于显示图像的QLabel
        self.btn_load = QPushButton("加载文件")

        layout.addWidget(self.label)
        layout.addWidget(self.image_label)  # 添加图像Label
        layout.addWidget(self.btn_load)
        self.setLayout(layout)

        self.btn_load.clicked.connect(self.open_file_dialog)
        self.setWindowTitle("Matplotlib图表显示示例")
        self.setGeometry(300, 300, 800, 600)  # 调整窗口大小

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择 .xyz 文件", "", "XYZ Files (*.xyz)"
        )
        if file_path:
            self.label.setText("加载中...")
            self.btn_load.setEnabled(False)

            self.thread = QThread()
            self.worker = FileLoaderWorker(file_path)
            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.run)
            self.worker.data_loaded.connect(self.on_data_loaded)
            self.worker.error_occurred.connect(self.on_error)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)

            self.thread.start()

    def on_data_loaded(self, png_data):
        pixmap = QPixmap()
        pixmap.loadFromData(png_data)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.label.setText("加载完成")
        self.btn_load.setEnabled(True)

    def on_error(self, error_msg):
        self.label.setText(error_msg)
        self.btn_load.setEnabled(True)

    def closeEvent(self, event):
        if self.thread and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()
        event.accept()


# ======================================================================
# 修改后的绘图函数
# ======================================================================
def cpltArea(input_file_path, x_min, x_max, y_min, y_max):
    data_list = []
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            values = line.strip().split()
            if len(values) > 0:
                front_value = float(values[0])
                second_value = float(values[1])
                if x_min <= front_value <= x_max and y_min <= second_value <= y_max:
                    data_list.append([float(values[1]), float(values[2])])
    df = pd.DataFrame(data_list, columns=["Y/mm", "Z/mm"])
    df = df.drop_duplicates(subset=["Y/mm"], keep="first")

    if df.empty:
        raise ValueError("没有符合条件的数据")

    min_Y_value = df["Y/mm"].min()
    df["Y/mm"] -= min_Y_value

    min_Z_value = df["Z/mm"].min()
    df["Z/mm"] -= min_Z_value

    # 创建Figure对象
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["Y/mm"], df["Z/mm"], color='b', linestyle='-', linewidth=2)
    ax.set(xlim=[0, 190], ylim=[0, 12],
           xlabel='Y/mm', ylabel='Z/mm',
           title='横截面形状')
    ax.grid(True, linestyle=':', color='gray')

    # 将图像保存到内存缓冲区
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight')
    plt.close(fig)  # 关闭figure释放内存
    buffer.seek(0)

    return buffer.getvalue()


# ======================================================================
# 启动应用
# ======================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
