# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 15:43
# @Author  : mihudan~
# @File    : boot_mainwindow.py
# @Description : 界面主程序，内主要功能为UI界面的控件和结构光相机接口以及工业相机接口的信号槽连接


# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide2
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html


# 工具信息
#
# Convert UI
# pyside2-uic main.ui > ui_main.py
#
# Convert QRC
# pyside2-rcc resources.qrc -o resources_rc.py
# D:\\soft\\Anaconda\\envs\\py37\\Scripts\\pyside2-rcc   E:\Work\THU\code\ZIVID_多进程线程测试7-24\QTui\resources.qrc   -o  E:\Work\THU\code\ZIVID_多进程线程测试7-24\QTui\resources_rc.py
# D:\\soft\\Anaconda\\envs\\py37\\Scripts\\pyside2-uic -o  E:\Work\THU\code\THU_Project_project\QTui\module\ui_main.py E:\Work\THU\code\THU_Project_project\QTui\main.ui

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
import os
import sys
from PySide2.QtCore import QThread, Signal, QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QFileDialog, QTableWidgetItem, QApplication, \
    QWidget, QGridLayout, QSizePolicy

# current_dir = os.path.dirname(os.path.abspath(__file__))
# os.chdir(current_dir)
print("boot_mainwindow path:", os.getcwd())
# 获取当前脚本所在的目录
sys.path.append("./src")
sys.path.append("./QTui")

# # 声明QMainWindow
# class MainWindow(QMainWindow):
#     def __init__(self):
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)


import datetime
from Cfgs.cfg import *
import multiprocessing as mp
from QTui.CustomWidgets.RightPara.QToolBox import MyQToolBox
from CustomWidgets.VisualPointWidget import MayaviQWidget
from CustomWidgets.ImgView import ImageBox
from HIK.BasicDemo import *
from calib.point2rgb import run_calib
from src_zivid.capture_frame import Camera
from dde_temp_torch.torch_dde_predict import PINN_predict2

from app.openexe import run_exe
from db import *
from tool.hole_deep_analysis import deep_analysis
from CustomWidgets.Mainwindow import *
from module.connnect_extra_rightbox import ConnnectExtraRightBox

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////

hole_save_idx = 0


class Thread_Load_ZIVID__Camera(QThread):
    """
    !!!!!!!!现在好像会关闭进程这个线程无法推出，加载虚拟相机后关闭界面  进程没有结束
    连接zivid相机线程，避免阻塞，用signal把camera发送回主界面赋值
    """
    signal = Signal(object)

    def __init__(self, camera):
        super().__init__()
        self.camera = camera

    # 处理业务逻辑
    def run(self):
        # camera = Camera()
        # camera.app.connect_camera()
        camera = self.camera.app.connect_camera()
        if camera is not None:
            print("connect zivid success!")
        self.signal.emit(camera)


class Window(ProjectWindow, CardWindow):
    def __init__(self, pipe_sam, pipe_hik, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pipe_sam = pipe_sam
        self.pipe_hik = pipe_hik
        self.DEBUG = True

        # ZIVID相机的API连接信号槽///////////////////////////////////////////////////////////////
        # 创建zivid'相机对象
        global zivid_camera
        global widgets
        widgets = self.ui
        self.zivid_camera = Camera()
        zivid_camera = self.zivid_camera

        # 点云显示控件（注意不要用透明背景）
        mayavi_layout = QGridLayout(widgets.widget_showpoints)
        widgets.mayavi = MayaviQWidget()
        mayavi_layout.addWidget(widgets.mayavi, 2, 2)

        widgets.toolBox2 = MyQToolBox(QWidget(self))
        widgets.verticalLayout_29.addWidget(widgets.toolBox2)
        ConnnectExtraRightBox.init(self)

        # 加载虚拟相机
        widgets.btn_connect_virtual.clicked.connect(self.load_vr)

        # 连接结构光相机
        widgets.btn_connect_camera.clicked.connect(self.load_zivid_camera)
        self.Thread_Load_ZIVID__Camera = Thread_Load_ZIVID__Camera(zivid_camera)
        self.Thread_Load_ZIVID__Camera.signal.connect(lambda camera: setattr(zivid_camera, 'camera', camera))

        # zivid采集线程槽函数连接
        widgets.btn_cupture.clicked.connect(lambda: self.create_capture_thread())

        # 图片缩放控件
        widgets.normalview = ImageBox()
        widgets.horizontalLayout_7.addWidget(widgets.normalview)
        widgets.deepview = ImageBox()
        widgets.horizontalLayout_8.addWidget(widgets.deepview)

        # rgb全屏
        widgets.btn_rgbviewdown.clicked.connect(self.allscreenrgb)
        self.allrgbflag = False

        # 点云显示全屏
        widgets.btn_pointviewdown.clicked.connect(self.allscreenmaya)
        self.allmayaflag = False

        # 点云显示刷新
        widgets.tableWidget_fault.itemClicked.connect(self.show_points)

        widgets.btn_zivid_save.clicked.connect(zivid_camera.save_all)

        # HIK相机的API连接信号槽///////////////////////////////////////////////////////////////
        self.hik_img = self.init_hik_img(INIT_HIK_IMG)
        widgets.bnEnum.clicked.connect(lambda: enum_devices(self))
        widgets.bnOpen.clicked.connect(lambda: open_device(self))
        widgets.bnClose.clicked.connect(lambda: close_device(self))

        widgets.bnStart.clicked.connect(lambda: start_grabbing(self))
        widgets.bnStop.clicked.connect(lambda: stop_grabbing(self))

        widgets.bnSoftwareTrigger.clicked.connect(lambda: trigger_once(self))
        widgets.radioTriggerMode.clicked.connect(lambda: set_software_trigger_mode(self))
        widgets.radioContinueMode.clicked.connect(lambda: set_continue_mode(self))
        widgets.bnGetParam.clicked.connect(lambda: get_param(self))
        widgets.bnSetParam.clicked.connect(lambda: set_param(self))
        widgets.bnSaveImage.clicked.connect(lambda: save_bmp(self))
        widgets.closeAppBtn.clicked.connect(lambda: close_device(self))
        widgets.ComboDevices.currentIndexChanged.connect(lambda: updata_nSelCamIndex(self))

        # 标定矩阵
        widgets.btn_calib.clicked.connect(lambda: self.calib_camera())
        widgets.btn_verificate.clicked.connect(lambda: self.verificate_calib())
        self.H = None

        # 同步采集
        widgets.btn_all_capture.clicked.connect(lambda: self.all_capture_detect(self.pipe_sam, self.pipe_hik))

        widgets.btn_pinn.clicked.connect(self.pinn_predict)

        # 第三方软件调用
        widgets.btn_orangedit.clicked.connect(lambda: run_exe(widgets.lineEdit_orangedit_path.text()))
        widgets.btn_workvisual.clicked.connect(lambda: run_exe(widgets.lineEdit_workvisual_path.text()))

        DEBUG = False
        current_datetime = datetime.datetime.now()
        # Format it as a string with year, month, day, hour, minute, and second
        self.timestamp = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

        # 数据库
        # self.mysqlviewer = MySQLViewer(self)
        # self.mysqlviewer.widgets.tableWidget.itemDoubleClicked.connect(self.mysqlviewer_double_clicked)
        # widgets.verticalLayout_db.addWidget(self.mysqlviewer)
        # self.resize(2300, 1200)

    def all_capture_detect(self, pipe_sam, pipe_hik):
        """
        zivid和hik相机捕捉和检测
        zivid设置为需要电压，hik打开并且调到触发模式
        需要拿到两个相机的img和label然后处理，
                self.hik_img
                zivid_camera.datas.rgb
        Args:
            pipe_sam:
            pipe_hik:

        Returns:

        """
        self.update_timestamp()
        if not self.DEBUG:
            trigger_once(self)
            time.sleep(0.5)
        else:
            self.hik_img = self.init_hik_img(INIT_HIK_IMG)

        self.capture(UPDATA_SHOW=False)

        # 与HIK检测经常通信交互
        pipe_hik.send(self.hik_img)
        pipe_hik.send(self.hik_img)
        pipe_hik.send([0, 0])
        hik_img_pipe_recv = pipe_hik.recv()
        _ = pipe_hik.recv()
        hik_labels = pipe_hik.recv()
        zivid_camera.datas.labels = hik_labels
        _ = pipe_hik.recv()

        # 与SAM进程通信交互
        pipe_sam.send(self.hik_img)
        pipe_sam.send(hik_labels)
        #  vertex1_x, vertex1_y, vertex2_x, vertex2_y, vertex3_x, vertex3_y, vertex4_x, vertex4_y, short, long
        sam_label = pipe_sam.recv()
        sam_img = pipe_sam.recv()

        # 显示hik图像
        # img = hik_img_pipe_recv
        img = sam_img
        img_Qimage = QImage(img, img.shape[1], img.shape[0], QImage.Format_BGR888)
        img_pix = QPixmap.fromImage(img_Qimage)
        widgets.label_hikimg.setScaledContents(True)  # 调用setScaledContents将图像比例化显示在QLabel上
        size_policy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        widgets.label_hikimg.setSizePolicy(size_policy)
        img_pix = img_pix.scaled(widgets.label_hikimg.size(), Qt.KeepAspectRatio)
        widgets.label_hikimg.clear()
        widgets.label_hikimg.setPixmap(img_pix)  # 调用setPixmap函数设置显示Pixmap

        # 刷新deepmap和normal
        self.updata_show_zivid_rgb()
        if widgets.checkBox_needppoints.isChecked():
            self.updata_tablist()
            self.updata_show_normal()

        if not self.DEBUG:













            self.add_mysql_db()

    def calib_camera(self):
        """
        用机构光相机和海康相机的一帧进行标定矩阵
        """
        datas = [[], [], []]
        for i in range(3):
            file_dialog = QFileDialog(self, CALIB_DATA_PATH[i], CALIB_DATA_PATH[i], "All Files (*)")
            file_dialog.setFileMode(QFileDialog.ExistingFiles)
            if file_dialog.exec_():
                datas[i] = file_dialog.selectedFiles()

        updata_show_hik_thread = threading.Thread(target=self.target_calib_camera, args=(datas,))
        updata_show_hik_thread.daemon = True
        updata_show_hik_thread.start()

    def verificate_calib(self):
        """
        验证矩阵转换像素的的准确度
        好像得创建一个进程
        """
        print("verificate_calib")

    def target_calib_camera(self, datas):
        hik_imgs = datas[0]
        zivid_points = datas[1]
        zivid_rgbs = datas[2]
        zivid_camera.rvec, zivid_camera.tvec, zivid_camera.camera_matrix, zivid_camera.dist_coeffs \
            = run_calib(hik_imgs, zivid_points, zivid_rgbs, show=True)

        # np.save("./data/matrix/rvec1.npy", zivid_camera.rvec)
        # print("save_rvec:", zivid_camera.rvec)
        #
        # np.save("./data/matrix/tvec1.npy", zivid_camera.tvec)
        # print("save_tvec:", zivid_camera.tvec)
        #
        # np.save("./data/matrix/camera_matrix1.npy", zivid_camera.camera_matrix)
        # print("save_camera_matrix:", zivid_camera.camera_matrix)
        # np.save("./data/matrix/dist_coeffs1.npy", zivid_camera.dist_coeffs)
        # print("save_dist_coeffs:", zivid_camera.dist_coeffs)

    ######################################     ZIVID   ###############################

    def create_capture_thread(self):
        """
        创建zivid采集线程
        Returns
        -------

        """
        t = threading.Thread(target=self.capture, args=(True,))
        t.daemon = True
        t.start()

    def capture(self, UPDATA_SHOW):
        """
        ZIVID抓取一帧图像
        UPDATA_SHOW: 是否刷新显示deepmap和normal
        """
        # 输出配置信息
        print(f"zivid capture one frame！")

        zivid_camera.capture(widgets.spinBox_ROIX.value(),
                             widgets.spinBox_ROIY.value(),
                             widgets.spinBox_ROIH.value(),
                             widgets.spinBox_ROIW.value(),
                             self.pipe_sam,
                             self.pipe_hik,
                             widgets.horizontalSlider_nx.value(),
                             widgets.horizontalSlider_ny.value(),
                             widgets.horizontalSlider_nz.value(),
                             widgets.checkBox_needppoints.isChecked(),
                             DEBUG=self.DEBUG,
                             timestamp=self.timestamp
                             )
        if UPDATA_SHOW:
            self.updata_show_zivid_rgb()
            if widgets.checkBox_needppoints.isChecked():
                self.updata_tablist()
                self.updata_show_normal()

    def updata_show_zivid_rgb(self):
        """
        显示ZIVID rgb图像
        Returns:

        """

        if self.DEBUG:
            # zivid_camera.datas.draw = zivid_camera.datas.rgb_high_ios
            widgets.label_imgrgba.setMinimumSize(QSize(800, 500))
            widgets.label_imgrgba.setMaximumSize(QSize(800, 500))

        img_Qimage = QImage(zivid_camera.datas.draw, zivid_camera.datas.draw.shape[1], zivid_camera.datas.draw.shape[0], QImage.Format_BGR888)
        img_pix = QPixmap.fromImage(img_Qimage)
        widgets.label_imgrgba.setScaledContents(True)  # 调用setScaledContents将图像比例化显示在QLabel上
        img_pix = img_pix.scaled(widgets.label_imgrgba.size(), Qt.KeepAspectRatio)
        widgets.label_imgrgba.setPixmap(img_pix)  # 调用setPixmap函数设置显示Pixmap

    def updata_tablist(self):
        """
        维护listWidget_labels，点击显示缺陷点云,结果光相机采集一帧后更新缺陷点云列表
        """
        widgets.tableWidget_fault.clear()
        # qtablewidgetitemlist={}
        # qtablewidgetitemlist["00"] = QTableWidgetItem()
        # qtablewidgetitemlist["01"] = QTableWidgetItem()
        # qtablewidgetitemlist["02"] = QTableWidgetItem()
        widgets.tableWidget_fault.setItem(0, 0, QTableWidgetItem())
        widgets.tableWidget_fault.setItem(0, 1, QTableWidgetItem())
        widgets.tableWidget_fault.setItem(0, 2, QTableWidgetItem())
        widgets.tableWidget_fault.item(0, 0).setText(f"点云ID")
        widgets.tableWidget_fault.item(0, 1).setText(f"点云个数")
        widgets.tableWidget_fault.item(0, 2).setText(f"置信度")
        if zivid_camera.datas.labels is not None:
            print(f"detected defaults num : {len(zivid_camera.datas.labels)}")
            for i, label in enumerate(zivid_camera.datas.labels):
                idx = i + 1
                widgets.tableWidget_fault.setItem(idx, 0, QTableWidgetItem())
                widgets.tableWidget_fault.setItem(idx, 1, QTableWidgetItem())
                widgets.tableWidget_fault.setItem(idx, 2, QTableWidgetItem())
                widgets.tableWidget_fault.item(idx, 0).setText(f"{idx}")
                widgets.tableWidget_fault.item(idx, 1).setText(f"{(label[2] - label[0]) * label[3] - label[1]}")
                widgets.tableWidget_fault.item(idx, 2).setText(f"{label[4]}")

    def updata_show_normal(self):
        """
        采集了点云，更新列表显示normal和deepmap
        Returns:

        """
        # normal_Qimage = QImage(zivid_camera.datas.ROI_normal , zivid_camera.datas.ROI_normal .shape[1], zivid_camera.datas.ROI_normal .shape[0], zivid_camera.datas.ROI_normal .shape[1] * 3, QImage.Format_RGB888)
        normal_Qimage = QImage(zivid_camera.datas.ROI_normal, zivid_camera.datas.ROI_normal.shape[1], zivid_camera.datas.ROI_normal.shape[0],
                               zivid_camera.datas.ROI_normal.shape[1] * 3, QImage.Format_BGR888)
        img_pix = QPixmap.fromImage(normal_Qimage)
        widgets.normalview.set_image(img_pix)

        deep_Qimage = QImage(zivid_camera.datas.ROI_deepmap, zivid_camera.datas.ROI_deepmap.shape[1], zivid_camera.datas.ROI_deepmap.shape[0], zivid_camera.datas.ROI_deepmap.shape[1] * 3,
                             QImage.Format_BGR888)
        img_pix = QPixmap.fromImage(deep_Qimage)
        widgets.deepview.set_image(img_pix)

    def show_points(self, Item):
        """
        根据当前listWidget_labels选择的内容显示不同的点云
        """
        try:
            if Item is None or Item.text() == "":
                return
            else:
                print(Item.row())
                idx = Item.row()
                if 1 <= idx <= len(zivid_camera.datas.labels):
                    self.show_points_inbox(idx - 1)
                else:
                    self.show_points_inroi()
        except Exception as e:
            print("Error:", e)
            print("no points!")

    def show_points_inroi(self):
        """
        显示ROI点云
        """
        points = zivid_camera.datas.get_points_inroi()
        # 显示深度点云
        x = points[:, 0]  # x position of point
        y = points[:, 1]  # y position of point
        z = points[:, 2]  # z position of point
        print(f"points in roi nums:{x.shape[0]}")

        # N scalars
        widgets.mayavi.visualization.scene.mlab.clf()
        points_mlab = widgets.mayavi.visualization.scene.mlab.points3d(x, y, z,
                                                                       # z,
                                                                       scale_factor=0.1,
                                                                       # color=(r, g, b),  # Values used for Color
                                                                       colormap='spectral',
                                                                       # 'bone', 'copper', 'gnuplot'
                                                                       mode="point",

                                                                       # color=(0, 1, 0),   # Used a fixed (r,g,b) instead

                                                                       )
        # 加载所有检测到的点云并且和ROI进行同样的flip
        points_inbox = zivid_camera.datas.get_points_inbox_all()
        if len(points_inbox) != 0:
            x_inbox = points_inbox[:, 0]  # x position of point
            y_inbox = points_inbox[:, 1]  # y position of point
            z_inbox = points_inbox[:, 2]  # z position of point
        widgets.mayavi.visualization.scene.mlab.points3d(x_inbox, y_inbox, z_inbox,
                                                         scale_factor=0.2,
                                                         # scale_mode="none",
                                                         color=(0.8, 0.8, 0.8),  # Values used for Color
                                                         # mode="point",
                                                         mode="sphere",
                                                         colormap='copper',  # 'bone', 'copper', 'gnuplot'
                                                         # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                                                         )

        widgets.mayavi.visualization.scene.mlab.points3d(0, 0, 0,
                                                         scale_factor=0.5,
                                                         # scale_mode="none",
                                                         color=(0, 1, 0),  # Values used for Color
                                                         # mode="point",
                                                         mode="sphere",
                                                         colormap='copper',  # 'bone', 'copper', 'gnuplot'
                                                         # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                                                         )

    def show_points_inbox(self, idx):
        """
        显示点击列表选择的缺陷idx的点云
        Args:
            idx(int): 索引

        Returns:

        """

        points = zivid_camera.datas.get_points_inbox(idx)

        deep_analysis(points)
        # np.save(f"./data/points/points_{hole_save_idx}.npy", points)

        widgets.mayavi.visualization.scene.mlab.clf()
        x = points[:, 0]  # x position of point
        y = points[:, 1]  # y position of point
        z = points[:, 2]  # z position of point

        widgets.mayavi.visualization.scene.mlab.clf()
        points_mlab = widgets.mayavi.visualization.scene.mlab.points3d(x, y, z,
                                                                       # z,
                                                                       scale_factor=0.2,
                                                                       # color=(r, g, b),  # Values used for Color
                                                                       colormap='spectral',
                                                                       # 'bone', 'copper', 'gnuplot'
                                                                       mode="sphere",
                                                                       # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                                                                       )

    def allscreenrgb(self):
        """
        rgb图像全屏显示
        """
        if self.allrgbflag is False:
            widgets.verticalLayout.setStretch(0, 1)
            widgets.verticalLayout.setStretch(2, 0)
            widgets.label_imgrgba.setMaximumSize(QSize(9999, 9999))
            widgets.widget.hide()
            widgets.widget_2.hide()
            # 显示图像
            try:
                img_Qimage = QImage(zivid_camera.datas.draw, zivid_camera.datas.draw.shape[1], zivid_camera.datas.draw.shape[0], QImage.Format_BGR888)
                img_pix = QPixmap.fromImage(img_Qimage)
                widgets.label_imgrgba.setScaledContents(True)  # 调用setScaledContents将图像比例化显示在QLabel上
                img_pix = img_pix.scaled(widgets.label_imgrgba.size(), Qt.KeepAspectRatio)
                widgets.label_imgrgba.setPixmap(img_pix)  # 调用setPixmap函数设置显示Pixmap
            except:
                pass
            self.allrgbflag = True
        else:
            widgets.verticalLayout.setStretch(0, 3)
            widgets.verticalLayout.setStretch(2, 2)
            widgets.label_imgrgba.setMaximumSize(QSize(800, 500))
            if self.DEBUG:
                widgets.label_imgrgba.setMaximumSize(QSize(800, 500))
            widgets.widget.show()
            widgets.widget_2.show()
            self.allrgbflag = False

    def allscreenmaya(self):
        """
        点云显示控件全屏
        """
        if self.allrgbflag is False:
            widgets.verticalLayout_16.setStretch(0, 999)
            widgets.verticalLayout_16.setStretch(2, 1)
            widgets.tableWidget_fault.hide()
            self.allrgbflag = True
        else:
            widgets.verticalLayout_16.setStretch(0, 0)
            widgets.verticalLayout_16.setStretch(2, 0)
            widgets.tableWidget_fault.show()
            self.allrgbflag = False

    def load_zivid_camera(self):
        """
        连接结构光相机

        """
        self.Thread_Load_ZIVID__Camera.start()
        DEBUG = False

    def load_vr(self):
        """
        加载结构光虚拟相机

        """
        zivid_camera.load_vr()  # 非常奇怪，这里load.zdf文件无法释放进程
        if zivid_camera.camera is not None:
            print("connect virtual zivid success!")
            DEBUG = True

    def init_hik_img(self, path):
        return cv2.imread(path)

    def pinn_predict(self):
        """
        注意Qthread还必须得 self.pinn_thread ，不能 pinn_thread
        PINN预测，显示
        Returns:
        """
        # self.pinn_thread.start()
        p = mp.Process(target=PINN_predict2, name='PInn process')  # 参数传递可以，全局变量不行
        p.daemon = True
        p.start()

    def add_mysql_db(self):
        if zivid_camera.datas.labels is None:
            defect_num = 0
        else:
            defect_num = len(zivid_camera.datas.labels)
        self.mysqlviewer.add_frame(["./data/", self.timestamp,
                                    int(float(widgets.edtExposureTime.text())),
                                    int(float(widgets.edtGain.text())),
                                    widgets.spinBox_ROIH.value(),
                                    widgets.spinBox_ROIW.value(),
                                    len(zivid_camera.datas.points.xyz),
                                    defect_num,
                                    widgets.horizontalSlider_nx.value(),
                                    widgets.horizontalSlider_ny.value(),
                                    widgets.horizontalSlider_nz.value()])

    def mysqlviewer_double_clicked(self, item):
        """
        双击mysql数据库表格的一行，显示对应的点云
        """
        row = item.row()
        data = [self.mysqlviewer.widgets.tableWidget.item(row, c).text() for c in range(self.mysqlviewer.widgets.tableWidget.columnCount())]
        timestamp = data[2]

        characters_to_remove = " :"
        for char in characters_to_remove:
            timestamp = timestamp.replace(char, '-')
        print(timestamp)

        pipe_hik = self.pipe_hik
        zivid_camera.load_sql_data(widgets.spinBox_ROIX.value(),
                                   widgets.spinBox_ROIY.value(),
                                   widgets.spinBox_ROIH.value(),
                                   widgets.spinBox_ROIW.value(),
                                   timestamp)

        self.hik_img = self.init_hik_img(f"data/hik_img/{timestamp}.jpg")
        pipe_hik.send(self.hik_img)
        pipe_hik.send(self.hik_img)
        pipe_hik.send([0, 0])
        hik_img_pipe_recv = pipe_hik.recv()
        _ = pipe_hik.recv()
        hik_labels = pipe_hik.recv()
        zivid_camera.datas.labels = hik_labels
        _ = pipe_hik.recv()

        # 显示hik图像
        img = hik_img_pipe_recv
        img_Qimage = QImage(img, img.shape[1], img.shape[0], QImage.Format_BGR888)
        img_pix = QPixmap.fromImage(img_Qimage)
        widgets.label_hikimg.setScaledContents(True)  # 调用setScaledContents将图像比例化显示在QLabel上
        img_pix = img_pix.scaled(widgets.label_hikimg.size(), Qt.KeepAspectRatio)
        widgets.label_hikimg.clear()
        widgets.label_hikimg.setPixmap(img_pix)  # 调用setPixmap函数设置显示Pixmap

        # 刷新deepmap和normal
        self.updata_show_zivid_rgb()
        if widgets.checkBox_needppoints.isChecked():
            self.updata_tablist()
            self.updata_show_normal()

    def update_timestamp(self):
        # Get the current date and time
        current_datetime = datetime.datetime.now()
        # Format it as a string with year, month, day, hour, minute, and second
        self.timestamp = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

        print(self.timestamp)


def close_window_by_title(target_title):
    """
    通过窗口名称关闭加载显示界面
    Parameters
    ----------
    target_title

    Returns
    -------

    """
    import win32gui
    import win32con
    def callback(hwnd, target):
        if win32gui.GetWindowText(hwnd).find(target) != -1:
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

    win32gui.EnumWindows(callback, target_title)


def window_process(pipe_sam: tuple, pipe_hik: tuple):
    """
    QT界面启动入口
    Parameters
    ----------
    pipe_sam
    pipe_hik

    Returns
    -------

    """
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    icon = QIcon("./QTui/icon.ico")
    print(f"icon:{icon}")
    app.setWindowIcon(icon)
    window = Window(pipe_sam, pipe_hik)
    window.show()

    # 关闭加载页面
    close_window_by_title("GifSplashScreen")

    # QMainWindow内如果不用QThread而是python的线程，如果不手动释放，就会无法结束界面进程！！
    sys.exit(app.exec_())
    print("window_process closed!")


class Cfg:
    def __init__(self, weights, imgsz, conf_thres):
        self.weights = weights  # 训练好的模型路径   （必改）
        self.imgsz = imgsz  # 训练模型设置的尺寸 （必改）
        self.conf_thres = conf_thres
