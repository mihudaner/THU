import time
import os
import torch
import numpy as np
import sys
from os import getcwd

print("yolo.mydetect.py path：", getcwd())
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages, letterbox
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel

# python detect.py --weights yolov7.pt --conf 0.25 --img-size 640 --source inference/images/2.mp4

# --------------------这里更改配置--------------------
# ---------------------------------------------------
'''
weights='./yolov7/yolov7.pt'   #训练好的模型路径   （必改）
imgsz=640           #训练模型设置的尺寸 （必改）
cap = 0             #摄像头
conf_thres=0.25     #置信度
iou_thres=0.45      #NMS IOU 阈值
max_det=1000        #最大侦测的目标数
device='0'          #设备
crop=True           #显示预测框
classes=None        #种类
agnostic_nms=False  #class-agnostic NMS
augment=False       #是否扩充推理
half=False          #使用FP16半精度推理
hide_labels=False   #是否隐藏标签
hide_conf=False     #是否隐藏置信度
line_thickness=3     #预测框的线宽
'''


def img2yolo(pipe_img, cfg):
    @torch.no_grad()
    def detect(  # --------------------这里更改配置--------------------
            # ---------------------------------------------------
            weights=cfg.weights,  # 训练好的模型路径   （必改）
            # weights='../yolov7/yolov7.pt',  # 训练好的模型路径   （必改）
            imgsz=cfg.imgsz,  # 训练模型设置的尺寸 （必改）
            cap=0,  # 摄像头
            conf_thres=cfg.conf_thres,  # 置信度
            iou_thres=0.45,  # NMS IOU 阈值
            max_det=100,  # 最大侦测的目标数
            device='0',  # 设备
            # device='cpu',  # 设备'cpu'
            crop=True,  # 显示预测框
            classes=None,  # 种类
            agnostic_nms=False,  # class-agnostic NMS
            augment=False,  # 是否扩充推理
            half=False,  # 使用FP16半精度推理
            hide_labels=False,  # 是否隐藏标签
            hide_conf=False,  # 是否隐藏置信度
            line_thickness=1,  # 预测框的线宽

    ):

        # cap = cv2.VideoCapture(r'D:\Desktop\pythonwork\data\big.mp4')
        # ref,img0 = cap.read()

        # Initialize
        set_logging()
        device = select_device(device)
        half = device.type != 'cpu'  # half precision only supported on CUDA
        half = False
        # Load model

        model = attempt_load(weights, map_location=device)  # load FP32 model
        stride = int(model.stride.max())  # model stride
        imgsz = check_img_size(imgsz, s=stride)  # check img_size

        if half:
            model.half()  # to FP16

        # Get names and colors
        names = model.module.names if hasattr(model, 'module') else model.names
        colors = [[np.random.randint(0, 255) for _ in range(3)] for _ in names]

        # Run inference
        if device.type != 'cpu':
            model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once

        while True:  #############################***here
            labels = []
            centers = []
            img0 = pipe_img.recv()
            raw_img = pipe_img.recv()
            roi_x, roi_y = pipe_img.recv()

            t0 = time.time()
            img = letterbox(img0, imgsz, stride=stride)[0]
            # 转换
            img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416

            img = np.ascontiguousarray(img)

            img = torch.from_numpy(img).to(device)
            img = img.half() if half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Inference
            # t1 = time_synchronized()
            pred = model(img, augment=augment)[0]

            # Apply NMS
            pred = non_max_suppression(pred, conf_thres, iou_thres, classes=classes, agnostic=agnostic_nms)
            # t2 = time_synchronized()

            # Apply Classifier
            # if classify:
            #    pred = apply_classifier(pred, modelc, img, im0s)

            # Process detections

            for i, det in enumerate(pred):  # detections per image
                s, im0 = '', img0.copy()
                # 输出字符串
                s += '%gx%g ' % img.shape[2:]
                # 归一化增益
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]
                if len(det):
                    # 将框从img_大小重新缩放为im0大小
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
                    # 输出结果
                    for c in det[:, -1].unique():
                        # 每类检测数
                        n = (det[:, -1] == c).sum()
                        # 添加到字符串
                        s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "
                        # 结果输出
                    id = 0
                    for *xyxy, conf, cls in reversed(det):
                        id += 1
                        # 归一化xywh
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()
                        # 标签格式
                        line = (cls, *xywh, conf)
                        # 整数类
                        c = int(cls)
                        # if names[int(cls)] == 'bottle':
                        # 建立标签
                        label = None if hide_labels else (names[c] if hide_conf else f'{names[c]}_{id} {conf:.2f}')
                        # 绘画预测框
                        if crop:
                            centerx = int((xyxy[0] + xyxy[2]) / 2)
                            centery = int((xyxy[1] + xyxy[3]) / 2)
                            plot_one_box(xyxy, im0, label=label, color=(57, 79, 234), line_thickness=line_thickness * 2)
                            # cv2.rectangle(im0, (centerx+4,centery+4) ,(centerx-4,centery-4), colors[c])  # 自己添加的中心画的小矩形
                        # 记录标签/概率/位置
                        labels.append([names[c], conf, xyxy])
                        centers.append([int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3]), float(conf.item()), int(cls.item())])  # tensor类型数据不能用pipe传输，不知为啥会变成0

                    for *xyxy, conf, cls in reversed(det):
                        # 归一化xywh
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()
                        # 标签格式
                        line = (cls, *xywh, conf)
                        # 整数类
                        c = int(cls)
                        # if names[int(cls)] == 'bottle':
                        # 建立标签
                        label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
                        # 绘画预测框
                        if crop:
                            xyxy[0], xyxy[1], xyxy[2], xyxy[3] = xyxy[0] + roi_x, xyxy[1] + roi_y, xyxy[2] + roi_x, xyxy[3] + roi_y
                            plot_one_box(xyxy, raw_img, label=label, color=(57, 79, 234), line_thickness=line_thickness)
            pipe_img.send(im0)
            pipe_img.send(raw_img)
            pipe_img.send(centers)
            pipe_img.send(names)
            # --------------------这里写/修改代码--------------------
            # -------------------------------------------------
            '''
            labels里面有该图片的标签/概率/坐标(列表)
            labels = [ [列表0] , [列表1] , [列表3] ,......]
                其中 列表 = [标签,概率,坐标]
            例如获取第一个预测框的概率值：print( float( labels[0][1])  )
            '''

            # 输出计算时间
            t1 = time.time()
            print(f'处理时间: ({t1 - t0:.3f}s)')
            '''
            # 显示图片
            #cv2.imshow("666",im0)
            
            key = cv2.waitKey(20)  

            #这里设置ESC退出
            if key == 27:
                break
            #--------------------END--------------------
            #-------------------------------------------------'''

    detect()


def draw_label(
        img,
        labels,
        names,
        crop=True,  # 显示预测框
        hide_labels=False,  # 是否隐藏标签
        hide_conf=False,  # 是否隐藏置信度
        line_thickness=4,  # 预测框的线宽

):
    """
    绘制检测框
    """
    for *xyxy, conf, cls in reversed(labels):

        # 整数类
        c = int(cls)

        label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
        # 绘画预测框
        if crop:
            xyxy[0], xyxy[1], xyxy[2], xyxy[3] = xyxy[0], xyxy[1], xyxy[2], xyxy[3]
            plot_one_box(xyxy, img, label=label, color=(57, 79, 234), line_thickness=line_thickness)
    return img
