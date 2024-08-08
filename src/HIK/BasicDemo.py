# -- coding: utf-8 --
import sys
import time
import os
import cv2
# sys.path.append(".")
from PySide2.QtCore import Qt
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QMessageBox

from .CamOperation_class import CameraOperation
from .MvCameraControl_class import *
from .MvErrorDefine_const import *
from .CameraParams_header import *
import threading
import numpy as np


# 转为16进制字符串
def To_hex_str(num):
    chaDic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    hexStr = ""
    if num < 0:
        num = num + 2 ** 32
    while num >= 16:
        digit = num % 16
        hexStr = chaDic.get(digit, str(digit)) + hexStr
        num //= 16
    hexStr = chaDic.get(num, str(num)) + hexStr
    return hexStr


# 获取选取设备信息的索引，通过[]之间的字符去解析
def TxtWrapBy(start_str, end, all):
    start = all.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = all.find(end, start)
        if end >= 0:
            return all[start:end].strip()


# 将返回的错误码转换为十六进制显示
def ToHexStr(num):
    chaDic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    hexStr = ""
    if num < 0:
        num = num + 2 ** 32
    while num >= 16:
        digit = num % 16
        hexStr = chaDic.get(digit, str(digit)) + hexStr
        num //= 16
    hexStr = chaDic.get(num, str(num)) + hexStr
    return hexStr


global deviceList
deviceList = MV_CC_DEVICE_INFO_LIST()
global nSelCamIndex
nSelCamIndex = 0
global obj_cam_operation
obj_cam_operation = 0
global isOpen
isOpen = False
global isGrabbing
isGrabbing = False
global isCalibMode  # 是否是标定模式（获取原始图像）
isCalibMode = True


# 绑定下拉列表至设备信息索引
def xFunc(event):
    global nSelCamIndex
    nSelCamIndex = TxtWrapBy("[", "]", ui.ComboDevices.get())


# ch:枚举相机 | en:enum devices
def enum_devices(mainWindow):
    global deviceList
    global obj_cam_operation

    deviceList = MV_CC_DEVICE_INFO_LIST()

    # ret = MvCamera.MV_CC_EnumDevices(MV_GIGE_DEVICE | MV_USB_DEVICE, deviceList)
    ret = MvCamera.MV_CC_EnumDevices(MV_GIGE_DEVICE, deviceList)
    if ret != 0:
        strError = "Enum devices fail! ret = :" + ToHexStr(ret)
        QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)
        return ret

    if deviceList.nDeviceNum == 0:
        QMessageBox.warning(mainWindow, "Info", "Find no device", QMessageBox.Ok)
        return ret
    print("Find %d devices!" % deviceList.nDeviceNum)

    devList = []

    deviceList.nDeviceNum -= 0

    for i in range(0, deviceList.nDeviceNum):
        mvcc_dev_info = cast(deviceList.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
        if mvcc_dev_info.nTLayerType == MV_GIGE_DEVICE:
            print("\ngige device: [%d]" % i)
            chUserDefinedName = ""
            for per in mvcc_dev_info.SpecialInfo.stGigEInfo.chUserDefinedName:
                if 0 == per:
                    break
                chUserDefinedName = chUserDefinedName + chr(per)
            print("device user define name: %s" % chUserDefinedName)

            chModelName = ""
            for per in mvcc_dev_info.SpecialInfo.stGigEInfo.chModelName:
                if 0 == per:
                    break
                chModelName = chModelName + chr(per)

            print("device model name: %s" % chModelName)

            nip1 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0xff000000) >> 24)
            nip2 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x00ff0000) >> 16)
            nip3 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x0000ff00) >> 8)
            nip4 = (mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x000000ff)
            print("current ip: %d.%d.%d.%d\n" % (nip1, nip2, nip3, nip4))
            devList.append(
                "[" + str(i) + "]GigE: " + chUserDefinedName + " " + chModelName + "(" + str(nip1) + "." + str(
                    nip2) + "." + str(nip3) + "." + str(nip4) + ")")

        # USB设备注释掉
        elif mvcc_dev_info.nTLayerType == MV_USB_DEVICE:
            print("\nu3v device: [%d]" % i)
            chUserDefinedName = ""
            for per in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chUserDefinedName:
                if per == 0:
                    break
                chUserDefinedName = chUserDefinedName + chr(per)
            print("device user define name: %s" % chUserDefinedName)

            chModelName = ""
            for per in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chModelName:
                if 0 == per:
                    break
                chModelName = chModelName + chr(per)
            print("device model name: %s" % chModelName)

            strSerialNumber = ""
            for per in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chSerialNumber:
                if per == 0:
                    break
                strSerialNumber = strSerialNumber + chr(per)
            print("user serial number: %s" % strSerialNumber)
            devList.append("[" + str(i) + "]USB: " + chUserDefinedName + " " + chModelName
                           + "(" + str(strSerialNumber) + ")")
    mainWindow.ui.ComboDevices.clear()
    mainWindow.ui.ComboDevices.addItems(devList)
    mainWindow.ui.ComboDevices.setCurrentIndex(0)


def updata_nSelCamIndex(mainWindow):
    """
    更新当前操作的是哪一个相机
    Parameters
    ----------
    mainWindow

    Returns
    -------

    """
    global nSelCamIndex
    nSelCamIndex = mainWindow.ui.ComboDevices.currentIndex()


# ch:打开相机 | en:open device
def open_device(mainWindow):
    global deviceList
    global nSelCamIndex
    global obj_cam_operation
    global isOpen
    if isOpen:
        QMessageBox.warning(mainWindow, "Error", 'Camera is Running!', QMessageBox.Ok)
        return MV_E_CALLORDER

    nSelCamIndex = mainWindow.ui.ComboDevices.currentIndex()
    if nSelCamIndex < 0:
        QMessageBox.warning(mainWindow, "Error", 'Please select a camera!', QMessageBox.Ok)
        return MV_E_CALLORDER

    obj_cam_operation = []
    for i in range(0, deviceList.nDeviceNum):
        cam = MvCamera()
        obj_cam_operation.append(CameraOperation(cam, deviceList, i))
        ret = obj_cam_operation[i].Open_device()

    if 0 != ret:
        strError = "Open device failed ret:" + ToHexStr(ret)
        QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)
        isOpen = False
    else:
        set_continue_mode(mainWindow)
        get_param(mainWindow)  # 起动获得参数
        isOpen = True
        enable_controls(mainWindow)


def updata_show_hik(mainWindow, Event):
    global obj_cam_operation
    global nSelCamIndex
    while True:
        Event.wait()
        mainWindow.hik_img = np.ascontiguousarray(obj_cam_operation[nSelCamIndex].img_np)
        img = mainWindow.hik_img
        img_Qimage = QImage(img, img.shape[1], img.shape[0], QImage.Format_BGR888)
        img_pix = QPixmap.fromImage(img_Qimage)
        mainWindow.ui.label_hikimg.setScaledContents(True)  # 调用setScaledContents将图像比例化显示在QLabel上
        img_pix = img_pix.scaled(mainWindow.ui.label_hikimg.size(), Qt.KeepAspectRatio)
        mainWindow.ui.label_hikimg.clear()
        mainWindow.ui.label_hikimg.setPixmap(img_pix)  # 调用setPixmap函数设置显示Pixmap
        Event.clear()


# ch:开始取流 | en:Start grab image
def start_grabbing(mainWindow):
    global obj_cam_operation
    global isGrabbing
    global nSelCamIndex

    # 创建更新图像线程
    hik_event = threading.Event()
    updata_show_hik_thread = threading.Thread(target=updata_show_hik, args=(mainWindow, hik_event))
    updata_show_hik_thread.daemon = True
    updata_show_hik_thread.start()

    ret = obj_cam_operation[nSelCamIndex].Start_grabbing(mainWindow.ui.widgetDisplay.winId(), hik_event)
    if ret != 0:
        strError = "Start grabbing failed ret:" + ToHexStr(ret)
        QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)
    else:
        # 开启动取流DIO6拉高
        mainWindow.ui.qwidget_card.widgets.DI6.setChecked(True)
        isGrabbing = True
        enable_controls(mainWindow)


# ch:停止取流 | en:Stop grab image
def stop_grabbing(mainWindow):
    global obj_cam_operation
    global nSelCamIndex
    global isGrabbing
    try:
        ret = obj_cam_operation[nSelCamIndex].Stop_grabbing()
    except TypeError:
        QMessageBox.warning(mainWindow, "Error", "obj_cam_operation=int，可能未打开相机或枚举相机！", QMessageBox.Ok)
    if ret != 0:
        strError = "Stop grabbing failed ret:" + ToHexStr(ret)
        QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)
    else:
        # 关动取流DIO6拉低
        mainWindow.ui.qwidget_card.widgets.DI6.setChecked(False)
        isGrabbing = False
        enable_controls(mainWindow)


# ch:关闭设备 | Close device
def close_device(mainWindow):
    global isOpen
    global isGrabbing
    global obj_cam_operation
    global nSelCamIndex

    if isOpen:
        for i in range(0, deviceList.nDeviceNum):
            obj_cam_operation[i].Close_device()
        isOpen = False

    isGrabbing = False

    enable_controls(mainWindow)


# ch:设置触发模式 | en:set trigger mode
def set_continue_mode(mainWindow):
    global nSelCamIndex
    strError = None

    ret = obj_cam_operation[nSelCamIndex].Set_trigger_mode(False)
    if ret != 0:
        strError = "Set continue mode failed ret:" + ToHexStr(ret)
        QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)
    else:
        mainWindow.ui.radioContinueMode.setChecked(True)
        mainWindow.ui.radioTriggerMode.setChecked(False)
        # mainWindow.ui.bnSoftwareTrigger.setEnabled(False)


# ch:设置软触发模式 | en:set software trigger mode
def set_software_trigger_mode(mainWindow):
    global nSelCamIndex
    ret = obj_cam_operation[nSelCamIndex].Set_trigger_mode(True)
    if ret != 0:
        strError = "Set trigger mode failed ret:" + ToHexStr(ret)
        QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)
    else:
        mainWindow.ui.radioContinueMode.setChecked(False)
        mainWindow.ui.radioTriggerMode.setChecked(True)
        # mainWindow.ui.bnSoftwareTrigger.setEnabled(isGrabbing)


# ch:设置触发命令 | en:set trigger software
def trigger_once(mainWindow):
    global nSelCamIndex
    mainWindow.update_timestamp()
    ret = obj_cam_operation[nSelCamIndex].Trigger_once(mainWindow.timestamp)
    if ret != 0:
        strError = "TriggerSoftware failed ret:" + ToHexStr(ret)
        QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)


# ch:存图 | en:save image
def Save_jpg(mainWindow):
    global nSelCamIndex
    ret = obj_cam_operation[nSelCamIndex].Save_jpg()
    if ret != MV_OK:
        strError = "Save_jpg failed ret:" + ToHexStr(ret)
        QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)
    else:
        print("Save image success")


# ch:存图 | en:save image
def save_bmp(mainWindow):
    global nSelCamIndex
    ret = obj_cam_operation[nSelCamIndex].Save_Bmp()
    if ret != MV_OK:
        strError = "Save BMP failed ret:" + ToHexStr(ret)
        QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)
    else:
        print("Save image success")


# ch: 获取参数 | en:get param
def get_param(mainWindow):
    global nSelCamIndex
    ret = obj_cam_operation[nSelCamIndex].Get_parameter()
    if ret != MV_OK:
        strError = "Get param failed ret:" + ToHexStr(ret)
        QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)
    else:
        mainWindow.ui.edtExposureTime.setText("{0:.2f}".format(obj_cam_operation[nSelCamIndex].exposure_time))
        mainWindow.ui.edtGain.setText("{0:.2f}".format(obj_cam_operation[nSelCamIndex].gain))
        mainWindow.ui.edtFrameRate.setText("{0:.2f}".format(obj_cam_operation[nSelCamIndex].frame_rate))

        # 获得自动曝光状态
        auto_mode = obj_cam_operation[nSelCamIndex].Get_auto_Exposure()

    if auto_mode == 2:
        mainWindow.ui.radioButton_autopara.setChecked(True)
    else:
        mainWindow.ui.radioButton_autopara.setChecked(False)
    # 获得高宽
    get_hw(mainWindow)


# ch: 设置参数 | en:set param
def set_param(mainWindow):
    global nSelCamIndex
    if mainWindow.ui.radioButton_autopara.isChecked():
        obj_cam_operation[nSelCamIndex].Set_auto_Exposure("Continuous")
    else:
        obj_cam_operation[nSelCamIndex].Set_auto_Exposure("Off")
        # obj_cam_operation.Merge_Down()  # 下采样两倍
        set_hw(mainWindow)  # 设置ROI
        frame_rate = mainWindow.ui.edtFrameRate.text()
        exposure = mainWindow.ui.edtExposureTime.text()
        gain = mainWindow.ui.edtGain.text()
        ret = obj_cam_operation[nSelCamIndex].Set_parameter(frame_rate, exposure, gain)
        if ret != MV_OK:
            strError = "Set param failed ret:" + ToHexStr(ret)
            QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)
    return MV_OK


# 设置参数
def Set_FloatValue(para_name, value):
    global obj_cam_operation
    if obj_cam_operation.b_open_device:
        ret = obj_cam_operation.obj_cam.MV_CC_SetFloatValue(para_name, float(value))
        if ret != 0:
            print('show error', 'Set_FloatValue fail! ret = ' + To_hex_str(ret))
            return ret
        print('show info', 'set parameter success!')
        return ret


# ch: 设置控件状态 | en:set enable status
def enable_controls(mainWindow):
    global isGrabbing
    global isOpen
    return
    # 先设置group的状态，再单独设置各控件状态
    mainWindow.ui.groupGrab.setEnabled(isOpen)
    mainWindow.ui.groupParam.setEnabled(isOpen)

    mainWindow.ui.bnOpen.setEnabled(not isOpen)
    mainWindow.ui.bnClose.setEnabled(isOpen)

    mainWindow.ui.bnStart.setEnabled(isOpen and (not isGrabbing))
    mainWindow.ui.bnStop.setEnabled(isOpen and isGrabbing)
    mainWindow.ui.bnSoftwareTrigger.setEnabled(isGrabbing and mainWindow.ui.radioTriggerMode.isChecked())

    mainWindow.ui.bnSaveImage.setEnabled(isOpen and isGrabbing)


def set_hw(mainWindow):
    """
    设置采集的高度和宽度
    Args:
        mainWindow:
    Returns:

    """
    global obj_cam_operation
    global nSelCamIndex
    height = int(mainWindow.ui.lineEdit_hik_H.text())
    width = int(mainWindow.ui.lineEdit_hik_W.text())
    # height =  height.rstrip("\n")
    # width =  width.rstrip("\n")

    ret = obj_cam_operation[nSelCamIndex].obj_cam.MV_CC_SetIntValueEx("Width", width)
    ret = obj_cam_operation[nSelCamIndex].obj_cam.MV_CC_SetIntValueEx("Height", height)
    if ret != MV_OK:
        strError = "Set HW failed ret:" + ToHexStr(ret)
        QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)


def get_hw(mainWindow):
    """
    设置采集的高度和宽度
    Args:
        mainWindow:
    Returns:

    """
    global obj_cam_operation
    global nSelCamIndex
    H = MVCC_INTVALUE()
    memset(byref(H), 0, sizeof(MVCC_INTVALUE))
    ret = obj_cam_operation[nSelCamIndex].obj_cam.MV_CC_GetIntValue("Height", H)
    W = MVCC_INTVALUE()
    memset(byref(W), 0, sizeof(MVCC_INTVALUE))
    ret = obj_cam_operation[nSelCamIndex].obj_cam.MV_CC_GetIntValue("Width", W)

    if ret != MV_OK:
        strError = "Set HW failed ret:" + ToHexStr(ret)
        QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)

    mainWindow.ui.lineEdit_hik_H.setText(f"{int(H.nCurValue)}")
    mainWindow.ui.lineEdit_hik_W.setText(f"{int(W.nCurValue)}")
