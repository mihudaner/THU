
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import os
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl.drawing.image import Image
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from PIL import Image
import numpy as np
import io
from openpyxl.drawing.image import Image as XLImage



# 设置中文字体为SimHei，解决中文显示及负号显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class cpltArea():
    def __init__(self, df, params):
        self.df = df  # 原始数据 [x, y, z]
        self.params = params  # 参数字典 {x_min, x_max, y_min, y_max}
        self.df_processed = None  # 存储处理后的截面数据

    def cpltAreaShow(self):
        """执行绘图并返回图像原始数据"""
        try:
            # 解包数据
            x, y, z = self.df
            params = self.params

            # 筛选数据
            mask = (x >= params['x_min']) & (x <= params['x_max']) & \
                   (y >= params['y_min']) & (y <= params['y_max'])
            y_filtered = y[mask]
            z_filtered = z[mask]

            # 创建并处理 DataFrame
            self.df_processed = pd.DataFrame({
                "Y/mm": y_filtered,
                "Z/mm": z_filtered
            })

            self.df_processed = self.df_processed.drop_duplicates(subset=["Y/mm"], keep="first")
            self.df_processed["Y/mm"] -= self.df_processed["Y/mm"].min()
            self.df_processed["Z/mm"] -= self.df_processed["Z/mm"].min()

            fig = Figure(figsize=(8, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(self.df_processed["Y/mm"], self.df_processed["Z/mm"],
                    color='b', linestyle='-', linewidth=2)
            ax.set(
                xlim=[0, 190],
                ylim=[0, 12],
                xlabel='Y/mm',
                ylabel='Z/mm',
                title='横截面形状'
            )
            ax.grid(True, linestyle=':', color='gray')
            fig.tight_layout()
            # 自定义绘图空白边界
            fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)

            # 渲染图像
            canvas = FigureCanvasAgg(fig)
            canvas.draw()
            return canvas.buffer_rgba()

        except Exception as e:
            raise RuntimeError(f"绘图过程中发生错误: {str(e)}")

    def saveExcel(self, save_dir):
        try:
            if self.df_processed is None:
                raise ValueError("请先调用 cpltAreaShow() 生成数据")

            os.makedirs(save_dir, exist_ok=True)
            file_path = os.path.join(save_dir, "表面原位补形.xlsx")

            # 如果文件已存在，则加载工作簿
            if os.path.exists(file_path):
                book = load_workbook(file_path)
                writer = pd.ExcelWriter(file_path, engine='openpyxl')
                writer.book = book
            else:
                writer = pd.ExcelWriter(file_path, engine='openpyxl')

            # 写入新Sheet（如果已有同名Sheet会被覆盖）
            self.df_processed.to_excel(
                writer,
                sheet_name="Sheet1",
                columns=["Y/mm", "Z/mm"],
                header=["Y/mm", "Z/mm"],
                index=False
            )

            writer.close()
            print("保存成功：", file_path)

        except Exception as e:
            raise RuntimeError(f"保存Excel失败: {str(e)}")


# 判断点是否在多边形内部的函数
def point_in_polygon(x, y, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


# 从Excel文件读取数据形成封闭曲线图形，增加文件名和工作表名参数
def read_curve_from_excel(file_path, sheet_name='Sheet1'):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    curve_points = df[['Y/mm', 'Z/mm']].values.tolist()
    return curve_points


# 用矩形填充封闭曲线图形并进行筛选及相关统计，增加文件名和工作表名参数，同时处理矩形连续性
def fill_and_filter(curve_points, rect_length, rect_width, file_path, sheet_name='Sheet1'):
    rect_centers = []
    rect_count = 0
    rect_layers_info = []  # 用于存储每一层的信息，考虑到可能有多层（不连续部分视为不同层）
    layer_info = {}  # 临时存储每层的信息

    x_min = min(point[0] for point in curve_points)
    x_max = max(point[0] for point in curve_points)
    y_min = min(point[1] for point in curve_points)
    y_max = max(point[1] for point in curve_points)

    # 确定最底一层矩形底边的纵坐标
    bottom_y = y_min

    step_x = rect_length
    step_y = rect_width

    prev_y = None  # 记录上一个矩形所在的纵坐标
    prev_x_center = None  # 记录上一个矩形的中心横坐标，用于判断连续性

    # 先筛选出在多边形内的所有矩形的中心坐标
    all_rect_centers_inside = []
    for x in np.arange(x_min, x_max, step_x):
        for y in np.arange(bottom_y, y_max, step_y):
            rect_corners = [
                (x, y),
                (x + rect_length, y),
                (x + rect_length, y + rect_width),
                (x, y + rect_width)
            ]
            rect_center = ((x + x + rect_length) / 2, (y + y + rect_width) / 2)
            left_bottom_corner = (x, y)
            right_bottom_corner = (x + rect_length, y)

            # 判断是否在多边形内
            if (point_in_polygon(rect_center[0], rect_center[1], curve_points) or
                    point_in_polygon(left_bottom_corner[0], left_bottom_corner[1], curve_points) or
                    point_in_polygon(right_bottom_corner[0], right_bottom_corner[1], curve_points)):
                all_rect_centers_inside.append(rect_center)
                rect_count += 1

    # 对在多边形内的矩形按照优先纵坐标最小，纵坐标相同时横坐标最小的顺序排序
    sorted_rect_centers_inside = sorted(all_rect_centers_inside, key=lambda x: (x[1], x[0]))

    # 基于排序后的矩形来判断是否为新的一层以及进行相关统计
    for rect_center in sorted_rect_centers_inside:
        x, y = rect_center

        # 判断是否为新的一层（按照之前规则判断，综合考虑纵坐标变化以及横坐标间距情况）
        if prev_y is None or (prev_y != y or (
                prev_y == y and prev_x_center is not None and abs(x - prev_x_center[0]) >= 2 * rect_length)):
            if layer_info:
                rect_layers_info.append(layer_info)
            layer_info = {'y': y, 'count': 1, 'rect_centers': [rect_center]}
        else:
            layer_info['count'] += 1
            layer_info['rect_centers'].append(rect_center)

        prev_y = y
        prev_x_center = rect_center

    if layer_info:
        rect_layers_info.append(layer_info)

    return sorted_rect_centers_inside, rect_count, rect_layers_info

# class DSF():
#     def __init__(self):
#         pass
def dsfSimuDep(file_path, params):

    # self.file_path = file_path  # 文件存储路径
    # self.params = params  # 参数[avgW，avgH]
    print(file_path, params)

    # 自定义读取封闭曲线数据的Excel文件及工作表名称
    curve_file_path = file_path
    curve_sheet_name = 'Sheet1'
    rect_length,rect_width = params
    # 自定义坐标轴范围
    x_min_custom = 0  # 这里替换为你想要的横坐标最小值
    x_max_custom = 170  # 这里替换为你想要的横坐标最大值
    y_min_custom = 0  # 这里替换为你想要的纵坐标最小值
    y_max_custom = 12  # 这里替换为你想要的纵坐标最大值

    curve_points = read_curve_from_excel(curve_file_path, sheet_name=curve_sheet_name)
    rect_centers, rect_count, rect_layers_info = fill_and_filter(curve_points, rect_length, rect_width,
                                                                 curve_file_path, curve_sheet_name)
    fig = Figure(figsize=(8, 4), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot([point[0] for point in curve_points] + [curve_points[0][0]],
             [point[1] for point in curve_points] + [curve_points[0][1]], 'b-')

    for center in rect_centers:
        rect = plt.Rectangle((center[0] - rect_length / 2, center[1] - rect_width / 2),
                             rect_length, rect_width, fill=False, edgecolor='r')
        ax.add_patch(rect)

    # 设置坐标轴范围和标签
    ax.set_xlim(x_min_custom, x_max_custom)
    ax.set_ylim(y_min_custom, y_max_custom)
    ax.set_xlabel('Y/mm')
    ax.set_ylabel('Z/mm')

    # 设置刻度
    ax.set_xticks([0, 30, 60, 90, 120, 150])
    y_tick_spacing = 3
    y_ticks = np.arange(y_min_custom, y_max_custom + y_tick_spacing, y_tick_spacing)
    ax.set_yticks(y_ticks)

    # 调整布局
    fig.tight_layout()
    # 渲染图像
    canvas = FigureCanvasAgg(fig)
    canvas.draw()

    print("矩形总个数：", rect_count)

    # 输出每一层的信息并按照一行进行格式化打印输出
    print("每一层信息如下：")
    for layer_info in rect_layers_info:
        y = layer_info['y']
        count = layer_info['count']
        min_x_center = min([center[0] for center in layer_info['rect_centers']])
        max_x_center = max([center[0] for center in layer_info['rect_centers']])
        min_y_center = min([center[1] for center in layer_info['rect_centers']])
        max_y_center = max([center[1] for center in layer_info['rect_centers']])
        print(f"Layer_Number: {rect_layers_info.index(layer_info) + 1}, Y_coordinate: {round(y, 2)}, "
              f"Pass_Number: {count}, X_min: {round(min_x_center, 2)}, Y_min: {round(min_y_center, 2)}, "
              f"X_max: {round(max_x_center, 2)}, Y_max: {round(max_y_center, 2)}")

    # 输出每一层的信息并保存到Excel文件中
    rows_data = []
    layer_number = 1
    for layer_info in rect_layers_info:
        y = layer_info['y']
        count = layer_info['count']
        min_x_center = min([center[0] for center in layer_info['rect_centers']])
        max_x_center = max([center[0] for center in layer_info['rect_centers']])
        min_y_center = min([center[1] for center in layer_info['rect_centers']])
        max_y_center = max([center[1] for center in layer_info['rect_centers']])

        row_data = {
            '层数': layer_number,
            'Y坐标': round(y, 2),
            '道数': count,
            'X_min': round(min_x_center, 2),
            'Y_min': round(min_y_center, 2),
            'X_max': round(max_x_center, 2),
            'Y_max': round(max_y_center, 2)
        }
        rows_data.append(row_data)
        layer_number += 1

    df = pd.DataFrame(rows_data)


    return canvas.buffer_rgba(),df

def dsfSave(file_path:str,params:list,df:object,img:np.ndarray):

    # 自定义保存数据在已存在Excel文件中的工作表名、起始行索引和起始列索引

    sheet_name = 'Sheet2'
    start_row_index = int(1)
    start_column_index = int(1)
    img_cell = 'J10'


    # 转换图像数组为PIL Image并保存到字节流
    img = Image.fromarray(img)
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    paramsdf = ['平均道次宽度(mm)', params[0], '平均熔覆层厚(mm)', params[1]]
    # 加载或创建Excel文件
    try:
        book = load_workbook(file_path)
    except FileNotFoundError:
        print("FileNotFoundError")

    # 创建或获取Sheet2
    if sheet_name in book.sheetnames:
        sheet = book[sheet_name]
    else:
        sheet = book.create_sheet(sheet_name)
        print(f"已创建新工作表: {sheet_name}")
    sheet.cell(start_row_index, start_column_index).value = paramsdf[0]
    sheet.cell(start_row_index, start_column_index + 1).value = paramsdf[1]
    sheet.cell(start_row_index + 1, start_column_index).value = paramsdf[2]
    sheet.cell(start_row_index + 1, start_column_index + 1).value = paramsdf[3]

    df_start_row = start_row_index + 2

    for r_idx, row in enumerate(dataframe_to_rows(df, index=False, header=True), df_start_row):
        for c_idx, value in enumerate(row, start=start_column_index):
            sheet.cell(row=r_idx, column=c_idx, value=value)

    # 插入图片
    try:
        excel_img = XLImage(img_byte_arr)
        sheet.add_image(excel_img, img_cell)
        print(f"图片已插入到位置: {img_cell}")
    except Exception as e:
        print(f"图片插入失败: {str(e)}")

    book.save(file_path)
    print(f"已保存工作表: {sheet_name}")






