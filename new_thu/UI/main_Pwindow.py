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