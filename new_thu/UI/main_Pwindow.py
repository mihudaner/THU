from main_viewer import *
from utils import *
from typing import cast
from Cardpage.Two_widget_debug import DIOWidget, AIOWidget_ShowOne
from PySide2.QtCore import QTimer, QPoint, QRect
from PySide2.QtGui import QPixmap, QImage
from src.molten_pool import CCD_Pretor
import datetime
import cv2
from PIL import Image
from Cardpage.Signal import g_signals
import time
import threading

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
        self.DataInit()
        self.InitUI()
        self.InitConnect()

    def InitUI(self):
        print("PWindow Load")
        self.resize(1900, 1100)

        self.ui = cast(Ui_MainWindow, self.ui)
        # 使用生成的Python文件作为类型提示
        self.ui.tabLayout = QHBoxLayout()
        self.ui.tab.setLayout(self.ui.tabLayout)

        self.ui.tab2Layout = QHBoxLayout()
        self.ui.tab_2.setLayout(self.ui.tab2Layout)

        # 隐藏标签选择
        self.ui.tabWidget_2.tabBar().hide()

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

        #### 工具栏功能
        # 假设 self.toolbar 是你的工具栏，设置鼠标事件
        self.ui.toolBar.mousePressEvent = self.mousePressEvent_toolbar
        self.ui.toolBar.mouseMoveEvent = self.mouseMoveEvent_toolbar
        self.ui.toolBar.mouseReleaseEvent = self.mouseReleaseEvent_toolbar
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置为可扩展的
        self.ui.toolBar.addWidget(spacer)

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

        self.mp4_recording = False
        self.cvs_recording = False

        self.now_select_ccd_save_apppath = "."

        g_signals.DI1_signal.connect(self.DI1_trigger)
        g_signals.DI2_signal.connect(self.DI2_trigger)

    def DI1_trigger(self, state):
        print(f"D1 state: {state}")
        if state == "UP":
            self.ui.AIOControlWidget.widgets.radioButton.setChecked(True)
            combo_selection = self.ui.AIOControlWidget.widgets.comboBox.currentText()

            if combo_selection == "保存为jpg":
                # self.ui.AIOControlWidget.capture()
                # self.save_ccd_img()
                self.start_recording(save_img=True)
            elif combo_selection == "保存为mp4":
                self.start_recording(save_mp4=True)
            elif combo_selection == "jpg+mp4":
                self.start_recording(save_mp4=True, save_img=True)
        else:  # state == "DOWN"
            self.ui.AIOControlWidget.widgets.radioButton.setChecked(False)
            if self.mp4_recording:
                self.mp4_recording = False

    def DI2_trigger(self, state):
        print(f"D2 state: {state}")
        if state == "UP":
            self.ui.DIOControlWidget.tar1.record_state = 1
            self.ui.DIOControlWidget.tar2.record_state = 1
            self.ui.AIOControlWidget.widgets.radioButton_2.setChecked(True)

        else:  # state == "DOWN"
            self.ui.DIOControlWidget.tar1.record_state = 3
            self.ui.DIOControlWidget.tar2.record_state = 3
            self.ui.AIOControlWidget.widgets.radioButton_2.setChecked(False)

    def InitConnect(self):
        self.ui.action_updateIO.triggered.connect(lambda: self.ui.tabWidget_2.setCurrentIndex(3))
        # 点击预测轮廓
        self.ui.btn_pre.clicked.connect(self.start_pre)
        self.ui.treeWidget.itemClicked.connect(self.on_item_clicked)
        self.ui.AIOControlWidget.widgets.btn_savecddimg.clicked.connect(self.save_ccd_img)

    def DataInit(self):
        self.ccd_pretor = CCD_Pretor(Debug=False)

    def on_item_clicked(self, item):
        if item.data(0, Qt.UserRole + 1) == "沉积监控" and item.text(0) == "实时反馈":
            self.ui.tabWidget_2.setCurrentIndex(0)
            self.now_select_ccd_save_apppath = item.data(0, Qt.UserRole)
            self.ui.DIOControlWidget.now_select_csv_save_apppath = self.now_select_ccd_save_apppath
            pass
        elif item.data(0, Qt.UserRole + 1) == "沉积监控" and item.text(0) == "熔池状态":
            self.ui.tabWidget_2.setCurrentIndex(2)
            pass

    # def open_file_dialog(self):
    #     # 弹出文件对话框，获取选择的 TIFF 文件路径
    #     options = QFileDialog.Options()
    #     file_path, _ = QFileDialog.getOpenFileName(self, "选择 TIFF img", "", "TIFF 文件 (*.tiff *.tif);;所有文件 (*)", options=options)
    #
    #     # 如果用户选择了文件，则显示图片
    #     if file_path:
    #         self.display_image(file_path)

    def save_ccd_img(self):
        img = self.ui.AIOControlWidget.cam.get_img()
        # 获取当前时间
        now = datetime.datetime.now()

        # 格式化时间字符串，可以根据需求调整格式
        timestamp = now.strftime("%Y%m%d_%H%M%S")

        # 创建文件名
        filename = f"\\image_{timestamp}.jpg"
        path = self.now_select_ccd_save_apppath + filename
        # 假设 img 是 OpenCV 的 numpy 数组
        img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        img_pil.save(path)

    def start_recording(self, save_mp4=False, save_img=False):
        if self.mp4_recording:
            print("Already mp4_recording!")
            return
        self.mp4_recording = True
        # 创建线程
        record_thread = threading.Thread(target=self._record_loop, args=(save_mp4,save_img,))
        record_thread.start()

    def _record_loop(self,save_mp4=False, save_img=False):
        first_frame = True
        self.fps = self.ui.AIOControlWidget.Slider_fps.value()
        i = 0
        while self.mp4_recording:
            img = self.ui.AIOControlWidget.capture(updateshow=True, timedelay=1 / self.fps - self.ui.AIOControlWidget.Slider_exposure.value() / 1000)

            if isinstance(img, np.ndarray):
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y%m%d_%H%M%S")

                if first_frame:
                    self.frame_size = (img.shape[1], img.shape[0])
                    first_frame = False

                    self.video_save_path = os.path.join(self.now_select_ccd_save_apppath, f"video_{timestamp}.mp4")
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                    if save_mp4:
                        self.video_writer = cv2.VideoWriter(self.video_save_path, fourcc, self.fps, self.frame_size)
                        print(f"mp4_recording started: {self.video_save_path}")

                resized_img = cv2.resize(img, self.frame_size)
                font = cv2.FONT_HERSHEY_SIMPLEX  # 字体
                font_scale = 0.7  # 字体大小
                font_color = (0, 255, 255)  # 文字颜色（黄色）
                thickness = 2  # 字体粗细
                text_size = cv2.getTextSize(timestamp + f"{i}", font, font_scale, thickness)[0]
                text_x = resized_img.shape[1] - text_size[0] - 10  # 右上角横坐标
                text_y = 30  # 右上角纵坐标
                cv2.putText(resized_img, timestamp + f"{i}", (text_x, text_y), font, font_scale, font_color, thickness)
                if save_mp4:
                    self.video_writer.write(resized_img)
                if save_img:
                    path = os.path.join(self.now_select_ccd_save_apppath, f"{timestamp}_{i}.jpg")
                    print(f"save to {path}")
                    # 假设 img 是 OpenCV 的 numpy 数组
                    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                    img_pil.save(path)
            i += 1
        if save_mp4:
            self.video_writer.release()
            self.video_writer = None
            print(f"mp4_recording stopped. Video saved at: {self.video_save_path}")

    def display_image(self, cv_image, dis):
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
        while (1):
            res_img, dis = self.ccd_pretor.get_next_frame_res()
            if dis is not None:
                break

        self.display_image(res_img, dis)

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
        print(x, y, w, h)
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


class PWindow(CCD_Window, TabWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
