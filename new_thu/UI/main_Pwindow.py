from main_viewer import  *
from utils import *
from typing import cast
from Cardpage.Two_widget_debug import DIOWidget,AIOWidget_ShowOne
from PySide2.QtCore import QTimer
from PySide2.QtGui import QPixmap,QImage
from src.molten_pool import CCD_Camera
import cv2
#  D:\\soft\\Anaconda\\envs\\py37\\Scripts\\pyside2-uic -o  E:\Work\THU\code\THU_Project_project\QTui\module\ui_main.py E:\Work\THU\code\THU_Project_project\QTui\main.ui
global flag
flag = False

class PWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        print("PWindow")
        # self.ui = parent.ui
        self.Load()
        # 改变自己显示的大小
        self.resize(1400, 900)
        self.PInit()

        # self.ccd_cam = CCD_Camera(False)

    def PInit(self):
        self.ui.btn_pre.clicked.connect(self.start_pre)

    def Load(self):
        print("PWindow Load")
        self.ui = cast(Ui_MainWindow, self.ui)
        # 使用生成的Python文件作为类型提示
        self.ui.tabLayout = QVBoxLayout()
        self.ui.tab.setLayout(self.ui.tabLayout)

        self.ui.tab2Layout = QVBoxLayout()
        self.ui.tab_2.setLayout(self.ui.tab2Layout)

        self.ui.tab3Layout = QVBoxLayout()
        self.ui.tab_3.setLayout(self.ui.tab3Layout)

        self.ui.tab4Layout = QVBoxLayout()
        self.ui.tab_4.setLayout(self.ui.tab4Layout)


        # 添加DIO TAB
        self.ui.DIOControlWidget = DIOWidget()
        self.ui.tab4Layout.addWidget(self.ui.DIOControlWidget)
        # 添加AIO TAB
        self.ui.AIOControlWidget = AIOWidget_ShowOne()
        self.ui.tabLayout.addWidget(self.ui.AIOControlWidget)

    # def open_file_dialog(self):
    #     # 弹出文件对话框，获取选择的 TIFF 文件路径
    #     options = QFileDialog.Options()
    #     file_path, _ = QFileDialog.getOpenFileName(self, "选择 TIFF 图片", "", "TIFF 文件 (*.tiff *.tif);;所有文件 (*)", options=options)
    #
    #     # 如果用户选择了文件，则显示图片
    #     if file_path:
    #         self.display_image(file_path)

    def display_image(self, cv_image,dis):
        # 确保图像为 BGR 格式（OpenCV 默认格式）
        # 转换为 RGB 格式
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

        # 将图像转换为 QImage
        height, width, channel = rgb_image.shape
        bytes_per_line = 3 * width
        q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # 计算缩放比例
        label_width = self.ui.label_showpre.width()
        label_height = self.ui.label_showpre.height()

        # 保持长宽比，缩放 QImage
        scaled_pixmap = QPixmap.fromImage(q_image).scaled(label_width, label_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 设置缩放后的图片到 QLabel
        self.ui.label_showpre.clear()
        self.ui.label_showpre.setPixmap(scaled_pixmap)
        self.ui.label_pre_w.setText(f"熔池宽度： {dis}  mm")


    def start_pre(self):
        global flag
        if flag == False:
            # 创建一个线程一直读取一个文件夹下的tiff图片并显示，延时免=0.5s后再显示下一张图片
            self.ui.timer = QTimer()
            self.ui.timer.timeout.connect(self.show_pre_ccd)
            self.ui.timer.start(500)
            self.ui.btn_pre.setText("停止预测")
            flag = True
        else:
            self.ui.timer.stop()
            self.ui.btn_pre.setText("启动预测")
            flag = False

    def show_pre_ccd(self):
        # self.ui.label_showpre.
        print("show_pre_ccd")
        # 循环读取所有 TIFF 文件
        while(1):
            res_img, dis = self.ccd_cam.get_next_frame_res()
            if dis is not None:
                break

        self.display_image(res_img,dis)