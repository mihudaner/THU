from main_viewer import  *
from utils import *
from typing import cast
from Cardpage.Two_widget_debug import DIOWidget,AIOWidget_ShowOne
#  D:\\soft\\Anaconda\\envs\\py37\\Scripts\\pyside2-uic -o  E:\Work\THU\code\THU_Project_project\QTui\module\ui_main.py E:\Work\THU\code\THU_Project_project\QTui\main.ui
class PWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        print("PWindow")
        # self.ui = parent.ui
        self.Load()
        # 改变自己显示的大小
        self.resize(1400, 900)


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

    def open_file_dialog(self):
        # 弹出文件对话框，获取选择的 TIFF 文件路径
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "选择 TIFF 图片", "", "TIFF 文件 (*.tiff *.tif);;所有文件 (*)", options=options)

        # 如果用户选择了文件，则显示图片
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        # 加载图片
        pixmap = QPixmap(file_path)

        # 计算缩放比例
        label_width = self.image_label.width()
        label_height = self.image_label.height()

        # 保持长宽比
        scaled_pixmap = pixmap.scaled(label_width, label_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 设置缩放后的图片到 QLabel
        self.image_label.setPixmap(scaled_pixmap)

    def show_pre_ccd(self):
        self.ui.label_showpre.