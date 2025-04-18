#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @_time_cfg    : 2025/4/10 22:44
# @Author  : mihudan~
# @File    : 调试以及运行参数设置
# @Description : 

import numpy as np
import matplotlib.pyplot as plt


DEBUG = True
# TEST_CCD_PATH = r'E:\Work\THU\code\DEBUG_DATA\pre5s-normal8s-intervel5s-nopower5s-stop2s.mp4'
TEST_CCD_PATH = r'E:\Work\THU\code\DEBUG_DATA\frame_imgs'
# TEST_CCD_PATH = r'E:\Work\THU\code\THU_Workspace\new_thu\resource\valid\1-3'
# TEST_CCD_PATH = "../src/centor_img.tiff"
CCD_MODEL_PAYH = r'E:\Work\THU\code\DEBUG_DATA\更新的网络及熔池分类\checkpoint8-200.pth'
# CCD_MODEL_PAYH = '../resource/models/checkpoint4.pth'

# 错误连续帧数
ERROR_WARNING_FRAME = 5

# 时间轴（0~30秒，每0.1秒一个点）
_time_cfg = np.arange(0, 25.1, 0.05)
TIMESIZE = _time_cfg.size
# 初始化电压
LASER_POWER_VOLTAGE = np.zeros_like(_time_cfg)
FEEDING_RATE_VOLTAGE = np.zeros_like(_time_cfg)
SPOT_VOLTAGE = np.zeros_like(_time_cfg)
REAL_TIME_SPEED = np.zeros_like(_time_cfg)
# 1.设置激光功率电压
LASER_POWER_VOLTAGE[(_time_cfg >= 5) & (_time_cfg < 13)] = 5
LASER_POWER_VOLTAGE[(_time_cfg >= 18) & (_time_cfg < 23)] = 5
# 2.设置送料速率电压
FEEDING_RATE_VOLTAGE[_time_cfg < 13] = 0.75
# 3.设置实时速度（带波动）
# 第1段上升：5~6s
mask1 = (_time_cfg >= 5) & (_time_cfg < 6)
REAL_TIME_SPEED[mask1] = np.linspace(0, 2.4, mask1.sum())
# 第1段恒定+波动：6~13s
mask_const1 = (_time_cfg >= 6) & (_time_cfg < 13)
REAL_TIME_SPEED[mask_const1] = 2.4 + np.random.normal(0, 0.05, mask_const1.sum())
# 第1段下降：13~14s
mask2 = (_time_cfg >= 13) & (_time_cfg < 14)
REAL_TIME_SPEED[mask2] = np.linspace(2.4, 0, mask2.sum())
# 第2段上升：18~19s
mask3 = (_time_cfg >= 18) & (_time_cfg < 19)
REAL_TIME_SPEED[mask3] = np.linspace(0, 2.4, mask3.sum())
# 第2段恒定+波动：19~25s
mask_const2 = (_time_cfg >= 19) & (_time_cfg < 25)
REAL_TIME_SPEED[mask_const2] = 2.4 + np.random.normal(0, 0.05, mask_const2.sum())
# 第2段下降：25~26s
mask4 = (_time_cfg >= 25) & (_time_cfg < 26)
REAL_TIME_SPEED[mask4] = np.linspace(2.4, 0, mask4.sum())
# 限制最大最小值防止超出范围
REAL_TIME_SPEED = np.clip(REAL_TIME_SPEED, 0, 2.5)
# # ----------------------------
# # 绘图
# plt.figure(figsize=(10, 6))
# plt.plot(_time_cfg, LASER_POWER_VOLTAGE, label='激光功率电压/V', color='blue')
# plt.plot(_time_cfg, FEEDING_RATE_VOLTAGE, label='送料速率电压/V', color='orange')
# plt.plot(_time_cfg, SPOT_VOLTAGE, label='光斑电压/V', color='gold')
# plt.plot(_time_cfg, REAL_TIME_SPEED, label='实时速度/V', color='green')
# plt.xlabel('时间/s')
# plt.ylabel('电压值')
# plt.title('四种电压随时间变化图（含速度波动）')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()


