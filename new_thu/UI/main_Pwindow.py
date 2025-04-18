from main_viewer import *
from utils import *
from typing import cast
import torch
import torch.nn as nn
from torchvision.models import resnet18
from Cardpage.Two_widget_debug import DIOWidget, AIOWidget_ShowOne
from Cardpage.Signal import g_signals
from CustomWidget.TimeDialog import TimedConfirmDialog
from PySide2.QtCore import QTimer, QPoint, QRect, QObject, Signal, QThread
from PySide2.QtGui import QPixmap, QImage
from src.molten_pool import CCD_Pretor
from src.depositionMorphology import cpltArea, dsfSimuDep, dsfSave, dcgCodegen, dcgSave
import datetime
import cv2
from PIL import Image
import time
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
import threading
from PySide2.QtWidgets import QTableWidget, QComboBox, QHeaderView,QWidget
import queue

#  D:\\soft\\Anaconda\\envs\\py37\\Scripts\\pyside2-uic -o  E:\Work\THU\code\THU_Project_project\QTui\module\ui_main.py E:\Work\THU\code\THU_Project_project\QTui\main.ui
global flag
flag = False
from UI import config


class CCD_Window(MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        print("CCD_Window")


class TabWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        print("PWindow")
        # 初始化数据
        self.DataInit()
        # 初始化UI
        self.InitUI()
        # 初始化连接信号
        self.InitConnect()

    def InitUI(self):
        print("PWindow Load")
        # self.resize(1900, 1100)

        self.ui = cast(Ui_MainWindow, self.ui)

        # 初始化标签页布局
        self.ui.tabLayout = QHBoxLayout()
        self.ui.tab.setLayout(self.ui.tabLayout)
        self.ui.tab2Layout = QHBoxLayout()
        self.ui.tab_2.setLayout(self.ui.tab2Layout)
        self.ui.tab3Layout = QHBoxLayout()
        self.ui.tab_3.setLayout(self.ui.tab3Layout)
        self.ui.tab4Layout = QHBoxLayout()

        # 初始化数字量控制界面-工艺更新
        self.ui.DIOControlWidget = DIOWidget(DEBUG=config.DEBUG)
        # self.ui.DIOControlWidget.hide()
        self.ui.tab4Layout.addWidget(self.ui.DIOControlWidget)
        self.ui.tab_4.setLayout(self.ui.tab4Layout)

        # 隐藏实时反馈，沉积形貌，熔池尺寸....标签
        self.ui.tabWidget_2.tabBar().hide()


        # 初始化模拟量控制界面-实时反馈
        self.ui.AIOControlWidget = AIOWidget_ShowOne(DEBUG=config.DEBUG)
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

        self.ui.center.setMouseTracking(True)  # 开启鼠标追踪
        self.ui.center.mousePressEvent = self.mousePressEvent_centor
        self.ui.center.mouseMoveEvent = self.mouseMoveEvent_centor
        self.ui.center.mouseReleaseEvent = self.mouseReleaseEvent_centor

        # 边缘放缩的尺寸范围
        self._resize_margin = 10
        self._is_resizing = False
        self._resizing_edge = None

        # MP4格式保存CCD数据标志位
        self.mp4_recording = False
        # cvs保存数字量数据标志位
        self.cvs_recording = False

        # 当前选择的项目保存CCD文件的路径
        self.now_select_ccd_save_apppath = "."


        # 设置表格自动调整列宽
        for i in range(self.ui.dsfSimuDepTable.columnCount()):
            self.ui.dsfSimuDepTable.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
        #
        # dcgParaTabel
        # dcgDetTabel
        # dcgScanTabel
        for i in range(self.ui.dcgParaTabel.columnCount()):
            self.ui.dcgParaTabel.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
        for i in range(self.ui.dcgDetTabel.columnCount()):
            self.ui.dcgDetTabel.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
        for i in range(self.ui.dcgScanTabel.columnCount()):
            self.ui.dcgScanTabel.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

        self.dsf()
        self.dcg()


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

            else:
                self.start_recording(save_img=False, save_mp4=False)
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

        # 数字量反馈信号连接
        g_signals.DI1_signal.connect(self.DI1_trigger)
        g_signals.DI2_signal.connect(self.DI2_trigger)

        # 沉积形貌信号连接
        self.cpltAreaAcq()

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

        elif item.data(0, Qt.UserRole + 1) == "沉积监控" and item.text(0) == "沉积形貌":
            self.ui.tabWidget_2.setCurrentIndex(1)
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

    def update_text_browser(self, result_text):
        self.ui.AIOControlWidget.widgets.textBrowser_ccdres.append(result_text)  # 在主线程中更新 UI

    def start_recording(self, save_mp4=False, save_img=False):
        if self.mp4_recording:
            print("Already mp4_recording!")
            return
        self.mp4_recording = True
        # 创建工作线程
        now = datetime.datetime.now()
        create_time = now.strftime("%Y%m%d_%H%M%S")
        self.worker = Worker()
        self.worker.update_text_signal.connect(self.update_text_browser)  # 连接信号
        self.worker.update_error_signal.connect(self.ccd_detect_type_error)  # 连接错误信号

        record_thread = threading.Thread(target=self.worker._record_loop, args=(self, create_time, save_mp4, save_img))
        # record_thread = threading.Thread(target=self._record_loop, args=(create_time,save_mp4,save_img,))
        record_thread.start()

    def _record_loop(self, create_time, save_mp4=False, save_img=False):
        update_text_signal = Signal(str)
        first_frame = True
        self.fps = self.ui.AIOControlWidget.widgets.Slider_fps.value()
        frame_time = 1 / self.fps  # 每帧期望的时间间隔（秒）
        i = 0
        #####
        # 设置中文字体，这里使用系统自带的黑体字体示例，你可以根据实际情况更换为其他支持中文的字体
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        class_mapping = {
            '1': 'normal',
            '2': 'Zero spot voltage',
            '3': 'No powder',
            '4': 'No laser'
        }
        # 定义图像预处理的转换操作
        transform = transforms.Compose([
            transforms.Grayscale(num_output_channels=3),  # 将灰度图转换为3通道图
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        # 初始化模型，这里以ResNet18为例，如果你训练的是其他模型，要做相应替换
        model = resnet18()
        num_ftrs = model.fc.in_features
        # 修改全连接层结构，使其与权重键名对应的结构匹配
        model.fc = nn.Sequential(
            nn.Linear(num_ftrs, 8),  # some_output_size需根据实际情况填写，比如分类的类别数量等
        )

        # 加载训练好的模型权重，替换成你的实际.pth 文件路径
        checkpoint = torch.load(config.CCD_MODEL_PAYH)

        # 处理权重字典的键名，将fc.weight和fc.bias修改为fc.0.weight和fc.0.bias。
        # 训练的时候有权重字典的键名的修改，这里要修改
        new_state_dict = {}
        for key, value in checkpoint['state_dict'].items():
            if key == "fc.weight":
                new_key = "fc.0.weight"
            elif key == "fc.bias":
                new_key = "fc.0.bias"
            else:
                new_key = key
            new_state_dict[new_key] = value

        # 使用修改后的权重字典加载权重到模型
        model.load_state_dict(new_state_dict)
        model.eval()

        while self.mp4_recording:
            start_time = time.time()  # 记录帧处理开始时间
            self.ui.AIOControlWidget.capture(updateshow=True, timedelay=0)
            img = self.ui.AIOControlWidget.cam.get_img()

            # ===========================
            # img送到网络判读模型
            # 应用预处理转换操作
            # 将 NumPy 数组转换为 PIL 图像
            img = Image.fromarray(img)
            img = transform(img).unsqueeze(0)

            # 识别分类
            with torch.no_grad():
                outputs = model(img)
                probabilities = torch.softmax(outputs, dim=1)  # 获取概率分布
                _, predicted = torch.max(outputs, 1)
                predicted_class_index = predicted.item()
                # 因为类别编号从1开始，所以将模型输出的以0为起始的索引值加1
                predicted_class_index_adjusted = predicted_class_index + 1
                # 通过调整后的索引从映射关系中获取类别名称
                predicted_class_name = class_mapping[str(predicted_class_index_adjusted)]
                predicted_probability = probabilities[0][predicted_class_index].item()  # 获取对应类别的概率

            # # 自定义字体和字号，这里示例设置字体为黑体，字号为12，可根据需求调整
            # font_path = font_manager.findfont('SimHei')
            # font_prop = font_manager.FontProperties(fname=font_path, size=12)
            #
            # # 文字显示的纵坐标位置偏移量，用于调节打印内容和图片的距离，可根据实际情况微调
            # text_y_offset = -0.25
            #
            # fig, ax = plt.subplots(figsize=(4, 3))  # 设置图像显示的画布大小，可根据需求调整
            # ax.imshow(img.squeeze(0).permute(1, 2, 0).numpy())
            # ax.axis('off')
            #
            # info_text = f"图像时间: {start_time}\n预测类别: {predicted_class_name}\n该类别的概率: {predicted_probability:.4f}"
            # ax.text(0.5, text_y_offset, info_text, size=12, ha="center", transform=ax.transAxes,
            #         fontproperties=font_prop)
            # 将类别名称和概率转换为字符串
            result_text = f"预测类别: {predicted_class_name}\n预测概率: {predicted_probability:.2f}"  # 保留两位小数
            # 更新显示结果
            # self.ui.AIOControlWidget.widgets.label_ccd_img
            update_text_signal.emit(result_text)  # 发出信号更新 UI
            # self.ui.AIOControlWidget.widgets.textBrowser_ccdres.append(result_text)

            # 将 PIL 图像转换为 NumPy 数组
            img = np.array(img)
            if isinstance(img, np.ndarray):
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y%m%d_%H%M%S")

                if first_frame:
                    self.frame_size = (img.shape[1], img.shape[0])
                    first_frame = False

                    if save_mp4:
                        self.video_save_path = os.path.join(self.now_select_ccd_save_apppath, f"video_{timestamp}.mp4")
                        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                        self.video_writer = cv2.VideoWriter(self.video_save_path, fourcc, self.fps, self.frame_size)
                        print(f"mp4_recording started: {self.video_save_path}")
                    if save_img:
                        dir = os.path.join(self.now_select_ccd_save_apppath, f"{create_time}")
                        if not os.path.exists(dir):
                            os.makedirs(dir)
                        print(f"save_img started: {self.now_select_ccd_save_apppath}")

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
                    path = os.path.join(dir, f"{timestamp}_{i}.jpg")
                    print(f"save to {path}")
                    # 假设 img 是 OpenCV 的 numpy 数组
                    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                    img_pil.save(path)
            i += 1

            # 计算实际处理时间和动态调整休眠
            elapsed_time = time.time() - start_time  # 当前帧的处理时间
            remaining_time = frame_time - elapsed_time  # 剩余时间

            if remaining_time > 0:
                time.sleep(remaining_time)  # 补偿时间，保证帧率
            else:
                print(f"Warning: Frame took {elapsed_time:.3f}s, which exceeds the target frame time {frame_time:.3f}s")

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

    def ccd_detect_type_error(self, error_msg):
        # 在主线程中更新 UI
        self.ui.AIOControlWidget.widgets.textBrowser_ccdres.append(error_msg)
        # 弹窗提示
        # QMessageBox.warning(self, '错误', f'熔覆检测识别状态异常 {error_msg}')

        def stop_process():
            print("⚠️ 用户确认终止处理")
            # 调用终止处理逻辑，比如：
            self.ui.DIOControlWidget.widgets.DO4.setChecked(True)
            # 或调用 self.terminate_deposition() 之类函数

        dialog = TimedConfirmDialog("沉积连续异常\n是否终止？", timeout=3, on_confirm=stop_process, parent=None)
        dialog.exec_()  # 阻塞等待，直到用户操作或倒计时结束

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
        x, y, w, h = pos.x(), pos.y(), self.ui.center.width(), self.ui.center.height()
        print(f"x: {x}, y: {y}", f"w: {w}, h: {h}", f"margin: {self._resize_margin}")
        margin = self._resize_margin

        self._resizing_edge = None
        self.setCursor(Qt.ArrowCursor)

        if x <= margin and y <= margin:
            self._resizing_edge = 'top-left'
            self.setCursor(Qt.SizeFDiagCursor)
        elif x >= w - margin and y <= margin:
            self._resizing_edge = 'top-right'
            self.setCursor(Qt.SizeBDiagCursor)
        elif x <= margin and y >= h - margin:
            self._resizing_edge = 'bottom-left'
            self.setCursor(Qt.SizeBDiagCursor)
        elif x >= w - margin and y >= h - margin:
            self._resizing_edge = 'bottom-right'
            self.setCursor(Qt.SizeFDiagCursor)
        elif x <= margin:
            self._resizing_edge = 'left'
            self.setCursor(Qt.SizeHorCursor)
        elif x >= w - margin:
            self._resizing_edge = 'right'
            self.setCursor(Qt.SizeHorCursor)
        elif y <= margin:
            self._resizing_edge = 'top'
            self.setCursor(Qt.SizeVerCursor)
        elif y >= h - margin:
            self._resizing_edge = 'bottom'
            self.setCursor(Qt.SizeVerCursor)

    def _resize_window(self, global_pos):
        dx = global_pos.x() - self._start_mouse_pos.x()
        dy = global_pos.y() - self._start_mouse_pos.y()
        new_geometry = QRect(self._start_geometry)

        if self._resizing_edge == 'right':
            new_geometry.setRight(self._start_geometry.right() + dx)
        elif self._resizing_edge == 'bottom':
            new_geometry.setBottom(self._start_geometry.bottom() + dy)
        elif self._resizing_edge == 'bottom-right':
            new_geometry.setRight(self._start_geometry.right() + dx)
            new_geometry.setBottom(self._start_geometry.bottom() + dy)
        elif self._resizing_edge == 'left':
            new_geometry.setLeft(self._start_geometry.left() + dx)
        elif self._resizing_edge == 'top':
            new_geometry.setTop(self._start_geometry.top() + dy)
        elif self._resizing_edge == 'top-left':
            new_geometry.setTop(self._start_geometry.top() + dy)
            new_geometry.setLeft(self._start_geometry.left() + dx)
        elif self._resizing_edge == 'top-right':
            new_geometry.setTop(self._start_geometry.top() + dy)
            new_geometry.setRight(self._start_geometry.right() + dx)
        elif self._resizing_edge == 'bottom-left':
            new_geometry.setBottom(self._start_geometry.bottom() + dy)
            new_geometry.setLeft(self._start_geometry.left() + dx)

        self.setGeometry(new_geometry)

        # 方法：切换最大化和还原

    def toggle_maximize_restore(self):
        if self.is_maximized:
            self.showNormal()  # 还原窗口
            self.is_maximized = False
        else:
            self.showMaximized()  # 最大化窗口
            self.is_maximized = True

    ##### 沉积形貌功能 #####
    ### 补形区域获取 ###
    def cpltAreaAcq(self):
        # 绑定文件选择
        self.ui.cpltAreaAcqCFBtn.clicked.connect(self.cpltAreaAcqCF)
        # 绑定文件查看
        self.ui.cpltAreaAcqVFBtn.clicked.connect(self.cpltAreaAcqVF)
        # 绑定截面显示
        self.ui.cpltAreaAcqShowBtn.clicked.connect(self.cpltAreaAcqShow)
        #
        self.ui.cpltAreaAcqSaveBtn.clicked.connect(self.cpltAreaAcqSave)

        self.ui.dcgCodeTransBtn.clicked.connect(self.dcgCodeTrans)

    def thread_error(self, error_msg):
        print("thread_error:", error_msg)

    def dcgCodeTrans(self):
        run_exe(self.apppath["WorkVisual"])

    ## 补形区域获取-浏览按键-选择文件
    def cpltAreaAcqCF(self):
        try:
            # 创建文件对话框
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setNameFilter("点云文件 (*.xyz);;所有文件 (*.*)")

            if file_dialog.exec_():
                # 获取选择的文件路径
                self.cpltAreaAcqF = file_dialog.selectedFiles()
                if self.cpltAreaAcqF:
                    self.ui.cpltAreaAcqFLabel.setText(self.cpltAreaAcqF[0])
                    self.updatecpltArea()
        except:
            print("补形区域获取:文件选择失败")

    ## 补形区域获取-浏览按键-线程加载文件，更新补形区域
    def updatecpltArea(self):
        if self.cpltAreaAcqF:
            self.ui.cpltAreaShowLabel.setText("文件加载中")
            self.ui.cpltAreaAcqCFBtn.setEnabled(False)  # 禁用按钮
            # 创建线程和 Worker
            self.cpltAreathread1 = QThread()
            self.cpltAreaworker1 = cpltAreaFLWorker(self.cpltAreaAcqF[0])

            # 将 Worker 移动到线程
            self.cpltAreaworker1.moveToThread(self.cpltAreathread1)

            # 连接信号与槽
            self.cpltAreathread1.started.connect(self.cpltAreaworker1.run)
            self.cpltAreaworker1.data_loaded.connect(self.setcpltArea)
            self.cpltAreaworker1.error_occurred.connect(self.thread_error)
            self.cpltAreaworker1.finished.connect(self.cpltAreathread1.quit)
            self.cpltAreaworker1.finished.connect(self.cpltAreaworker1.deleteLater)
            self.cpltAreathread1.finished.connect(self.cpltAreathread1.deleteLater)
            # 启动线程
            self.cpltAreathread1.start()

    ## 补形区域获取-浏览按键-更新补形区域-设置补形区域
    def setcpltArea(self, x, y, z):
        self.ui.cpltAreaShowLabel.setText("加载完成")
        self.ui.cpltAreaAcqCFBtn.setEnabled(True)
        self.cpltdf = [x, y, z]
        ymin, ymax = np.nanmin(self.cpltdf[1]), np.nanmax(self.cpltdf[1])
        self.ui.yminDSBox.setValue(ymin)
        self.ui.ymaxDSBox.setValue(ymax)

    ## 补形区域获取-查看按键-查看文件(调用Cloudcompare)
    def cpltAreaAcqVF(self):
        if self.cpltAreaAcqF:
            print("cpltAreaAcqVF:", self.cpltAreaAcqF)
            run_exe(self.apppath["OrangeEdit"])
        else:
            print("cpltAreaAcqF didnt choose a file")

    ## 补形区域获取-截面显示按键-截面显示
    def cpltAreaAcqShow(self):
        self.ui.cpltAreaAcqShowBtn.setEnabled(False)  # 禁用按钮
        try:
            if self.cpltAreaAcqF:
                params = {
                    'x_min': self.ui.xminDSBox.value(),
                    'x_max': self.ui.xmaxDSBox.value(),
                    'y_min': self.ui.yminDSBox.value(),
                    'y_max': self.ui.ymaxDSBox.value()
                }
            if self.cpltdf:
                self.ui.cpltAreaShowLabel.setText("数据计算中")
                self.cpltarea = cpltArea(self.cpltdf, params)
                canvas = self.cpltarea.cpltAreaShow()
                img_array = np.frombuffer(canvas, dtype=np.uint8)
                width, height = 8 * 100, 4 * 100  # 必须与 figsize 一致
                img_array = img_array.reshape((height, width, 4))

                # self.ui.cpltAreaShowLabel.setScaledContents(True)
                pixmap = QPixmap.fromImage(QImage(img_array.data, width, height, QImage.Format_RGBA8888))
                label_size = self.ui.cpltAreaShowLabel.size()  # 获取当前 QLabel 尺寸
                scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.ui.cpltAreaShowLabel.setPixmap(scaled_pixmap)

        except:
            print("cpltAreaAcqShow:", "error")
        self.ui.cpltAreaAcqShowBtn.setEnabled(True)  # 启用按钮

    ## 补形区域获取-数据保存按键
    def cpltAreaAcqSave(self):
        self.ui.cpltAreaAcqSaveBtn.setEnabled(False)
        try:
            if self.cpltAreaAcqF:
                save_dir = os.path.dirname(self.cpltAreaAcqF[0])
                if not os.path.exists(save_dir):
                    print("cpltAreaAcqSave: wrong file path")
                    return -1
                self.cpltarea.saveExcel(save_dir)
        except Exception as e:
            print("补形区域获取:", "保存失败:", e)

        self.ui.cpltAreaAcqSaveBtn.setEnabled(True)

    ### 沉积模拟填充 ###
    def dsf(self):

        self.ui.dsfSimuDepBtn.clicked.connect(self.dsfSimuDep)
        self.ui.dsfSavePthBtn.clicked.connect(self.dsfSavePth)

    ## 模拟沉积
    def dsfSimuDep(self):
        try:
            self.ui.dsfSimuDepBtn.setEnabled(False)
            avgW = self.ui.dsfAvgWBox.value()
            avgH = self.ui.dsfAvgHBox.value()
            params = [avgW, avgH]
            try:
                if self.cpltAreaAcqF:
                    save_dir = os.path.dirname(self.cpltAreaAcqF[0])
                    file_path = os.path.join(save_dir, "表面原位补形.xlsx")
                    # 创建线程和 Worker
                    self.dsfSimuDepthread1 = QThread()
                    self.dsfSimuDepworker1 = dsfSimuDepWorker(file_path, params)
            except:
                # 创建线程和 Worker
                self.dsfSimuDepthread1 = QThread()
                self.dsfSimuDepworker1 = dsfSimuDepWorker("../database/项目库/zlc/沉积形貌/表面原位补形.xlsx", params)

            # 将 Worker 移动到线程
            self.dsfSimuDepworker1.moveToThread(self.dsfSimuDepthread1)

            # 连接信号与槽
            self.dsfSimuDepthread1.started.connect(self.dsfSimuDepworker1.run)
            self.dsfSimuDepworker1.dsfSimuDep_plot.connect(self.dsfSimuDepShowImg)
            self.dsfSimuDepworker1.dsfSimuDep_table.connect(self.dsfSimuDepShowTable)
            self.dsfSimuDepworker1.dsfSimuDep_error.connect(self.thread_error)
            self.dsfSimuDepworker1.finished.connect(self.dsfSimuDepthread1.quit)
            self.dsfSimuDepworker1.finished.connect(self.dsfSimuDepworker1.deleteLater)
            self.dsfSimuDepthread1.finished.connect(self.dsfSimuDepthread1.deleteLater)
            # 启动线程
            self.dsfSimuDepthread1.start()
        except:
            print("模拟沉积线程启动失败")
            self.ui.dsfSimuDepBtn.setEnabled(True)

    ## 模拟沉积-显示
    def dsfSimuDepShowImg(self, canvas):
        self.dsfimg_array = np.frombuffer(canvas, dtype=np.uint8)
        width, height = 8 * 60, 4 * 60  # 必须与 figsize 一致
        self.dsfimg_array = self.dsfimg_array.reshape((height, width, 4))

        pixmap = QPixmap.fromImage(
            QImage(self.dsfimg_array.data, width, height, QImage.Format_RGBA8888)
        )

        label_size = self.ui.dsfSimuDepShowLabel.size()
        scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.ui.dsfSimuDepShowLabel.setPixmap(scaled_pixmap)
        self.ui.dsfSimuDepShowLabel.setAlignment(Qt.AlignCenter)  # 居中可选

    def dsfSimuDepShowTable(self, df):
        # 设置表格的行列数
        self.dsfdf = df
        self.ui.dsfSimuDepTable.setRowCount(self.dsfdf.shape[0])
        self.ui.dsfSimuDepTable.setColumnCount(self.dsfdf.shape[1])

        # 设置表头
        self.ui.dsfSimuDepTable.setHorizontalHeaderLabels(self.dsfdf.columns.tolist())

        # 填充数据
        for row in range(self.dsfdf.shape[0]):
            for col in range(self.dsfdf.shape[1]):
                item = QTableWidgetItem(str(self.dsfdf.iat[row, col]))
                self.ui.dsfSimuDepTable.setItem(row, col, item)
        self.ui.dsfSimuDepBtn.setEnabled(True)

    ## 模拟沉积-从表格更新df
    def dsfTable2Df(self):
        # 获取表格的行数和列数
        rows = self.ui.dsfSimuDepTable.rowCount()
        cols = self.ui.dsfSimuDepTable.columnCount()

        # 检查列数是否与原数据框一致
        if cols != self.dsfdf.shape[1]:
            raise ValueError("表格列数与原数据框不一致")

        # 使用原数据框的列名
        columns = self.dsfdf.columns.tolist()

        # 收集数据
        data = []
        for row in range(rows):
            row_data = []
            for col in range(cols):
                item = self.ui.dsfSimuDepTable.item(row, col)
                cell_value = item.text() if item is not None else ''
                row_data.append(cell_value)
            data.append(row_data)

        # 创建新的DataFrame
        new_df = pd.DataFrame(data, columns=columns)

        # 转换数据类型，处理数值列的空字符串或无效值
        for col in columns:
            dtype = self.dsfdf[col].dtype
            if np.issubdtype(dtype, np.number):
                # 转换为数值类型，无效值转为NaN
                new_df[col] = pd.to_numeric(new_df[col], errors='coerce')
            else:
                # 其他类型直接转换
                new_df[col] = new_df[col].astype(dtype)

        # 更新数据框
        self.dsfdf = new_df

    ## 模拟沉积-保存
    def dsfSavePth(self):
        self.ui.dsfSavePthBtn.setEnabled(False)
        try:
            avgW = self.ui.dsfAvgWBox.value()
            avgH = self.ui.dsfAvgHBox.value()
            params = [avgW, avgH]

            try:
                if self.cpltAreaAcqF:
                    save_dir = os.path.dirname(self.cpltAreaAcqF[0])
                    file_path = os.path.join(save_dir, "表面原位补形.xlsx")
            except:
                file_path = os.path.join("../database/项目库/zlc/沉积形貌/表面原位补形.xlsx")
            self.dsfTable2Df()
            dsfSave(file_path, params, self.dsfdf, self.dsfimg_array)
        except:
            if not hasattr(self, 'dsfdf'):
                print("请先生成沉积模拟")
        self.ui.dsfSavePthBtn.setEnabled(True)

    ### 沉积程序生成
    def dcg(self):
        self.ui.dcgCodeGenBtn.clicked.connect(self.dcgCodeGen)
        self.ui.dcgParaSaveBtn.clicked.connect(self.dcgParaSave)
        self.ui.dcgCodeTransBtn.clicked.connect(self.dcgCodeTrans)
        self.ui.dcgCodeUpdateBtn.clicked.connect(self.dcgCodeUpdate)
        # 以下顺序不可变
        self.dcgTable()
        self.LaserCombo.currentTextChanged.connect(self.update_scan_table_visibility)

    ## 沉积程序生成-初始化表格
    def dcgTable(self):
        powderLocate = [8, 1]
        ccdLocate = [0, 1]
        temperatureLocate = [1, 1]
        GaoSuLocate = [2, 1]
        LaserLocate = [3, 1]
        # 粉桶
        self.powderCombo = QComboBox()
        self.powderCombo.addItems(["1", "2"])
        self.ui.dcgParaTabel.setCellWidget(powderLocate[0], powderLocate[1], self.powderCombo)
        # ccd
        self.ccdCombo = QComboBox()
        self.ccdCombo.addItems(["True", "False"])
        self.ui.dcgDetTabel.setCellWidget(ccdLocate[0], ccdLocate[1], self.ccdCombo)
        # Temperature
        self.temperatureCombo = QComboBox()
        self.temperatureCombo.addItems(["True", "False"])
        self.ui.dcgDetTabel.setCellWidget(temperatureLocate[0], temperatureLocate[1], self.temperatureCombo)
        # GaoSu_Camera
        self.GaoSuCombo = QComboBox()
        self.GaoSuCombo.addItems(["True", "False"])
        self.ui.dcgDetTabel.setCellWidget(GaoSuLocate[0], GaoSuLocate[1], self.GaoSuCombo)
        # Laser_LunKuo
        self.LaserCombo = QComboBox()
        self.LaserCombo.addItems(["True", "False"])
        self.ui.dcgDetTabel.setCellWidget(LaserLocate[0], LaserLocate[1], self.LaserCombo)

    def dcgtabel2Df(self, table: QTableWidget, include_index: bool = True, index_as_column: bool = True):
        try:
            # 获取表格维度
            rows = table.rowCount()
            cols = table.columnCount()

            # 获取列标题
            col_headers = []
            for c in range(cols):
                header = table.horizontalHeaderItem(c)
                col_headers.append(header.text() if header else f"Column_{c + 1}")

            # 获取行标题
            row_headers = []
            for r in range(rows):
                header = table.verticalHeaderItem(r)
                row_headers.append(header.text() if header else f"Row_{r + 1}")

            # 收集数据
            data = []
            for r in range(rows):
                row_data = []
                for c in range(cols):
                    # 处理控件
                    widget = table.cellWidget(r, c)
                    if isinstance(widget, QComboBox):
                        value = widget.currentText()
                    else:
                        item = table.item(r, c)
                        value = item.text() if item else ""
                    row_data.append(value)
                data.append(row_data)

            # 创建DataFrame
            df = pd.DataFrame(data, columns=col_headers)

            # 添加行标题处理
            if include_index:
                if index_as_column:
                    df.insert(0, "参数名称", row_headers)
                else:
                    df.index = row_headers

            return df

        except Exception as e:
            print(f"表格转换错误: {str(e)}")
            return pd.DataFrame()

    ## 沉积程序生成-保存参数
    def dcgParaSave(self):
        try:
            self.ui.dcgParaSaveBtn.setEnabled(False)
            try:
                if self.cpltAreaAcqF:
                    save_dir = os.path.dirname(self.cpltAreaAcqF[0])
                    file_path = os.path.join(save_dir, "表面原位补形.xlsx")
            except:
                file_path = os.path.join("../database/项目库/zlc/沉积形貌/表面原位补形.xlsx")
            df = self.dcgtabel2Df(self.ui.dcgParaTabel, True, True)
            dcgSave(file_path, df, 2, 1)
            df = self.dcgtabel2Df(self.ui.dcgDetTabel, True, True)
            dcgSave(file_path, df, 2, 6)
            if self.LaserCombo.currentText() == "True":
                df = self.dcgtabel2Df(self.ui.dcgScanTabel, True, True)
                dcgSave(file_path, df, 2, 11)
        except:
            print("保存参数失败")
        self.ui.dcgParaSaveBtn.setEnabled(True)

    def update_scan_table_visibility(self):
        """根据激光轮廓选项显示/隐藏扫描表格"""
        if self.LaserCombo.currentText() == "False":
            self.ui.dcgScanGroup.setVisible(False)

            policy = self.ui.dcgScanGroup.sizePolicy()
            policy.setRetainSizeWhenHidden(True)
            self.ui.dcgScanGroup.setSizePolicy(policy)
        else:
            self.ui.dcgScanGroup.setVisible(True)

    ## 沉积程序生成-生成程序
    def dcgCodeGen(self):
        try:
            self.ui.dcgCodeGenBtn.setEnabled(False)
            try:
                if self.cpltAreaAcqF:
                    save_dir = os.path.dirname(self.cpltAreaAcqF[0])
                    file_path = os.path.join(save_dir, "表面原位补形.xlsx")
            except:
                file_path = os.path.join("../database/项目库/zlc/沉积形貌/表面原位补形.xlsx")
            dcgCodegen(file_path)
        except:
            print("生成程序失败")
        self.ui.dcgCodeGenBtn.setEnabled(True)

    def dcgCodeTrans(self):
        run_exe(self.apppath["WorkVisual"])

    def dcgCodeUpdate(self):
        # 创建文件对话框
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("点云文件 (*.py);;所有文件 (*.*)")

        if file_dialog.exec_():
            # 获取选择的文件路径
            self.dcgAcqF = file_dialog.selectedFiles()
            if self.dcgAcqF:
                print("获取到文件：", self.dcgAcqF[0])


### 模拟沉积加载excel并生成图像
class dsfSimuDepWorker(QObject):
    # 定义完成信号（携带图像数据）和错误信号
    dsfSimuDep_plot = Signal(bytes)
    dsfSimuDep_table = Signal(object)
    dsfSimuDep_error = Signal(str)
    finished = Signal()

    def __init__(self, file_path, params):
        super().__init__()
        self.file_path = file_path
        self.params = params

    def run(self):
        try:
            canvas, df = dsfSimuDep(self.file_path, self.params)
            # 发射完成信号（携带图像原始数据）
            self.dsfSimuDep_plot.emit(canvas)
            self.dsfSimuDep_table.emit(df)
        except Exception as e:
            self.dsfSimuDep_error.emit(f"dsfSimuDepWorker错误: {str(e)}")
        finally:
            self.finished.emit()


#### 加载xyz文件的woker
class cpltAreaFLWorker(QObject):
    # 定义信号
    data_loaded = Signal(np.ndarray, np.ndarray, np.ndarray)  # 数据加载完成
    error_occurred = Signal(str)  # 发生错误
    finished = Signal()  # 任务结束

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        try:
            # 使用 pandas 读取，处理 NaN 并优化性能
            data = pd.read_csv(
                self.file_path,
                sep=r'\s+',  # 匹配任意空白字符（空格/tab等）
                header=None,  # 无列标题
                dtype=np.float32,  # 指定数据类型为 float32
                na_values=['nan', 'NaN', ''],  # 识别常见的 NaN 表示
                usecols=[0, 1, 2],  # 只读取前三列
                engine='c',  # 使用 C 引擎加速
                skipinitialspace=True  # 忽略分隔符前的空格
            ).values
            # 提取数据列
            x, y, z = data[:, 0], data[:, 1], data[:, 2]

            # 发射数据加载信号
            self.data_loaded.emit(x, y, z)

        except Exception as e:
            self.error_occurred.emit(f"加载失败：{str(e)}")

        finally:
            self.finished.emit()


class Worker(QObject):
    """
    线程工作类，负责处理CCD图像的异常识别
    """
    # 在类中定义信号
    update_text_signal = Signal(str)
    update_error_signal = Signal(str)
    error_warning_frame = config.ERROR_WARNING_FRAME

    def __init__(self):
        super().__init__()
        self.prediction_queue = queue.Queue(maxsize=5)
        self._start_predict_thread()

    def _start_predict_thread(self):
        self.predict_thread = threading.Thread(target=self._predict_worker, daemon=True)
        self.predict_thread.start()

    def _predict_worker(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        class_mapping = {
            "1": "Normal",
            "2": "No laser",
            "3": "Not enough powder",
            "4": "No powder",
            "5": "Smaller distance",
            "6": "Larger distance",
            "7": "Not enough gas",
            "8": "No gas"
        }

        transform = transforms.Compose([
            transforms.Grayscale(num_output_channels=3),
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        model = resnet18()
        num_ftrs = model.fc.in_features
        model.fc = nn.Sequential(nn.Linear(num_ftrs, 8))

        checkpoint = torch.load(config.CCD_MODEL_PAYH, map_location=device)
        new_state_dict = {}
        for key, value in checkpoint['state_dict'].items():
            if key == "fc.weight":
                new_key = "fc.0.weight"
            elif key == "fc.bias":
                new_key = "fc.0.bias"
            else:
                new_key = key
            new_state_dict[new_key] = value

        model.load_state_dict(new_state_dict)
        model.to(device)
        model.eval()

        while True:
            img = self.prediction_queue.get()
            try:
                pil_img = Image.fromarray(img)
                input_tensor = transform(pil_img).unsqueeze(0).to(device)

                with torch.no_grad():
                    outputs = model(input_tensor)
                    probabilities = torch.softmax(outputs, dim=1)
                    _, predicted = torch.max(outputs, 1)

                    predicted_class_index = predicted.item()
                    predicted_class_index_adjusted = predicted_class_index + 1

                    if predicted_class_index != 0:
                        self.error_warning_frame -= 1
                    else:
                        self.error_warning_frame = config.ERROR_WARNING_FRAME

                    if self.error_warning_frame == 0:
                        self.update_error_signal.emit(f"{predicted_class_index_adjusted}")

                    predicted_class_name = class_mapping[str(predicted_class_index_adjusted)]
                    predicted_probability = probabilities[0][predicted_class_index].item()

                    result_text = f"预测类别: {predicted_class_name}\n预测概率: {predicted_probability:.2f}\n时间: {datetime.datetime.now()}"
                    self.update_text_signal.emit(result_text)

            except Exception as e:
                print(f"[预测错误] {e}")

    def _record_loop(self, self_pwin, create_time, save_mp4=False, save_img=False):
        self_pwin.fps = self_pwin.ui.AIOControlWidget.widgets.Slider_fps.value()
        frame_time = 1 / self_pwin.fps
        first_frame = True
        i = 0

        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        while self_pwin.mp4_recording:
            start_time = time.time()
            self_pwin.ui.AIOControlWidget.capture(updateshow=True, timedelay=0)
            img = self_pwin.ui.AIOControlWidget.cam.get_img()

            # ✅ 异步送入识别线程（每3帧一次）
            if self_pwin.ui.AIOControlWidget.widgets.checkBox_openccd_2.isChecked() and i % 3 == 0:
                try:
                    if not self.prediction_queue.full():
                        self.prediction_queue.put_nowait(img.copy())
                except queue.Full:
                    pass  # 跳帧不等

            # ✅ 图像保存 / 视频写入
            if isinstance(img, np.ndarray):
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y%m%d_%H%M%S")

                if first_frame:
                    self_pwin.frame_size = (img.shape[1], img.shape[0])
                    first_frame = False

                    if save_mp4:
                        self_pwin.video_save_path = os.path.join(self_pwin.now_select_ccd_save_apppath, f"video_{timestamp}.mp4")
                        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                        self_pwin.video_writer = cv2.VideoWriter(self_pwin.video_save_path, fourcc, self_pwin.fps, self_pwin.frame_size)
                        print(f"[视频录制] 开始: {self_pwin.video_save_path}")

                    if save_img:
                        dir = os.path.join(self_pwin.now_select_ccd_save_apppath, f"{create_time}")
                        os.makedirs(dir, exist_ok=True)
                        print(f"[图像保存] 路径: {dir}")

                if save_mp4:
                    self_pwin.video_writer.write(img)

                if save_img:
                    path = os.path.join(self_pwin.now_select_ccd_save_apppath, f"{create_time}/{timestamp}_{i}.jpg")
                    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                    img_pil.save(path)

            i += 1

            # ✅ 保持恒定帧率
            elapsed_time = time.time() - start_time
            remaining_time = frame_time - elapsed_time
            if remaining_time > 0:
                time.sleep(remaining_time)
            else:
                print(f"[警告] 帧处理超时: {elapsed_time:.3f}s (目标: {frame_time:.3f}s)")

        if save_mp4 and self_pwin.video_writer is not None:
            self_pwin.video_writer.release()
            self_pwin.video_writer = None
            print(f"[视频录制] 结束: {self_pwin.video_save_path}")


class PWindow(CCD_Window, TabWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
