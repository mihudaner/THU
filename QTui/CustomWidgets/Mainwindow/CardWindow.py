#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/2 1:24
# @Author  : mihudan~
# @File    : ProjectWindow
# @Description : 

from .BasicMainwindow import *
from db.project import ProjectPage
from QTui.CustomWidgets.Cardpage.Two_widget_debug import DIOWidget, AIOWidget
from card.load_csv import QChart_Csv


class CardWindow(MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        global widgets
        widgets = self.ui
        # 采集卡        界面加入，控件太多，分开写的界面
        widgets.diowidget = DIOWidget()
        widgets.aiowidget = AIOWidget()
        widgets.verticalLayout_card_di.addWidget(widgets.diowidget)
        widgets.verticalLayout_card_ai.addWidget(widgets.aiowidget)
        # widgets.qwidget_card.t_in.data_in_sign.connect(self.DIO_operator)

        # CSV控件
        widgets.qchart_csv = QChart_Csv(self)
        widgets.verticalLayout_csv.addWidget(widgets.qchart_csv)

    def DIO_operator(self, up_flag, down_flag):
        """
        任意上升下降都会触发
        写不同上升沿的触发函数
        Parameters
        ----------
        up_flag: 上升沿标志位 【0，0，0，1，0，0，0，0】 就是dio4 上升沿
        down_flag

        Returns
        -------

        """
        # print("IO up_flag:", up_flag)
        # print("IO down_flag:", down_flag)
        # if up_flag[6]:
        #     start_grabbing(self)
        #     print("trigger up  start_grabbing")
        #     widgets.qwidget_card.t_in.card_datas = Card_datas(get_date_time())
        # if down_flag[6]:
        #     stop_grabbing(self)
        #     print("trigger up  stop_grabbing")
        #     widgets.qwidget_card.t_in.card_datas.close()
        #     widgets.qwidget_card.t_in.card_datas = None
        # if up_flag[5] or down_flag[5]:
        #     """开启红外相机"""
        #     pass
        return
        ##########################    PINN   ###############################################
