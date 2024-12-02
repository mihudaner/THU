from main_viewer import  *
from utils import *
from typing import cast
from Cardpage.Two_widget_debug import DIOWidget,AIOWidget_ShowOne
from PySide2.QtCore import QTimer,QPoint, QRect
from PySide2.QtGui import QPixmap,QImage
from src.molten_pool import CCD_Pretor
import cv2

#  D:\\soft\\Anaconda\\envs\\py37\\Scripts\\pyside2-uic -o  E:\Work\THU\code\THU_Project_project\QTui\module\ui_main.py E:\Work\THU\code\THU_Project_project\QTui\main.ui
global flag
flag = False



class CCD_Window(MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        print("CCD_Window")


class TabWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        print("PWindow")
        self.InitUI()
        self.PInit()

<<<<<<< HEAD
# <<<<<<< HEAD
#         # self.ccd_cam = CCD_Camera(False)
# =======
# >>>>>>> origin/addProject



=======
>>>>>>> origin/addProject
    def InitUI(self):
        print("PWindow Load")
        self.resize(1900, 900)

        self.ui = cast(Ui_MainWindow, self.ui)
        # 使用生成的Python文件作为类型提示
        self.ui.tabLayout = QHBoxLayout()
        self.ui.tab.setLayout(self.ui.tabLayout)

        self.ui.tab2Layout = QHBoxLayout()
        self.ui.tab_2.setLayout(self.ui.tab2Layout)

        self.ui.tab3Layout = QHBoxLayout()
        self.ui.tab_3.setLayout(self.ui.tab3Layout)

        self.ui.tab4Layout = QHBoxLayout()
        # 添加DIO TAB
        self.ui.DIOControlWidget = DIOWidget()
        self.ui.tab4Layout.addWidget(self.ui.DIOControlWidget)
        self.ui.tab_4.setLayout(self.ui.tab4Layout)

        # 添加AIO TAB
        self.ui.AIOControlWidget = AIOWidget_ShowOne()
        self.ui.tabLayout.addWidget(self.ui.AIOControlWidget)


        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置工具栏拖拽
        self._is_dragging = False
        self._drag_start_pos = QPoint()

        # 假设 self.toolbar 是你的工具栏，设置鼠标事件
        self.ui.toolBar.mousePressEvent = self.mousePressEvent_toolbar
        self.ui.toolBar.mouseMoveEvent = self.mouseMoveEvent_toolbar
        self.ui.toolBar.mouseReleaseEvent = self.mouseReleaseEvent_toolbar
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置为可扩展的
        self.ui.toolBar.addWidget(spacer)

        # 创建最小化按钮
        minimize_button = QPushButton("-")
        minimize_button.setFixedSize(30, 30)
        minimize_button.setStyleSheet("QPushButton { color: white; }")
        minimize_button.clicked.connect(self.showMinimized)  # 连接最小化信号

        # 创建最大化/还原按钮
        self.is_maximized = False
        maximize_button = QPushButton("□")
        maximize_button.setFixedSize(30, 30)
        maximize_button.setStyleSheet("QPushButton { color: white; }")
        maximize_button.clicked.connect(self.toggle_maximize_restore)  # 连接最大化/还原信号

        # 创建关闭按钮
        close_button = QPushButton("X")
        close_button.setFixedSize(30, 30)
        close_button.setStyleSheet("QPushButton { color: white; }")
        close_button.clicked.connect(self.close)  # 连接关闭信号

        # 将按钮添加到工具栏
        self.ui.toolBar.addWidget(minimize_button)
        self.ui.toolBar.addWidget(maximize_button)
        self.ui.toolBar.addWidget(close_button)

        self.ui.toolBar.setMouseTracking(True)  # 启用鼠标跟踪

        self.ui.center.mousePressEvent = self.mousePressEvent_centor
        self.ui.center.mouseMoveEvent = self.mouseMoveEvent_centor
        self.ui.center.mouseReleaseEvent = self.mouseReleaseEvent_centor

        # 边缘放缩的尺寸范围
        self._resize_margin = 10
        self._is_resizing = False
        self._resizing_edge = None

    def PInit(self):
<<<<<<< HEAD
        # self.ccd_cam = CCD_Camera(False)
=======
        self.ccd_pretor = CCD_Pretor(False)
>>>>>>> origin/addProject
        self.ui.btn_pre.clicked.connect(self.start_pre)


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
            res_img, dis = self.ccd_pretor.get_next_frame_res()
            if dis is not None:
                break

        self.display_image(res_img,dis)


    # 无标题栏窗口补充的基本功能

    def mousePressEvent_toolbar(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            self._drag_start_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()


    def mouseMoveEvent_toolbar(self, event):
        if self._is_dragging and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._drag_start_pos)
            event.accept()


    def mouseReleaseEvent_toolbar(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = False
            event.accept()


    def mouseMoveEvent_centor(self, event):
        if not self._is_resizing:
            self._update_cursor_shape(event.pos())
        else:
            self._resize_window(event.globalPos())
        event.accept()

    def mousePressEvent_centor(self, event):
        if event.button() == Qt.LeftButton:
            self._start_geometry = self.geometry()
            self._start_mouse_pos = event.globalPos()
            if self._resizing_edge:
                self._is_resizing = True
            event.accept()

    def mouseReleaseEvent_centor(self, event):
        if event.button() == Qt.LeftButton:
            self._is_resizing = False
            self._resizing_edge = None
            event.accept()

    def _update_cursor_shape(self, pos):
        # 确定鼠标是否靠近窗口边缘，并相应地改变光标形状
        x, y, w, h = pos.x(), pos.y(), self.ui.center.width(), self.ui.center.height()
        margin = self._resize_margin
        print( x ,y , w,h)
        if x > w - margin and y > h - margin:  # 右下角
            self._resizing_edge = 'bottom-right'
            self.setCursor(Qt.SizeFDiagCursor)
        else:
            self._resizing_edge = None
            self.setCursor(Qt.ArrowCursor)

    def _resize_window(self, global_pos):
        # 根据鼠标位置调整窗口大小
        dx = global_pos.x() - self._start_mouse_pos.x()
        dy = global_pos.y() - self._start_mouse_pos.y()
        new_geometry = QRect(self._start_geometry)

        if self._resizing_edge in ['bottom-left', 'bottom', 'bottom-right']:
            new_geometry.setBottom(self._start_geometry.bottom() + dy)

        self.setGeometry(new_geometry)

        # 方法：切换最大化和还原

    def toggle_maximize_restore(self):
        if self.is_maximized:
            self.showNormal()  # 还原窗口
            self.is_maximized = False
        else:
            self.showMaximized()  # 最大化窗口
            self.is_maximized = True




class PWindow(CCD_Window,TabWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass