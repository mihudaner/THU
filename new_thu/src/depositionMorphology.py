
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
from openpyxl.utils import get_column_letter
import sys
import textwrap

from openpyxl import load_workbook

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

            sheet_name = 'Sheet1'

            if os.path.exists(file_path):
                # 文件存在，追加并替换Sheet1
                with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                    self.df_processed.to_excel(writer, sheet_name=sheet_name, index=False, header=True)
            else:
                # 文件不存在，新建文件
                with pd.ExcelWriter(file_path, engine='openpyxl', mode='w',if_sheet_exists='replace') as writer:
                    self.df_processed.to_excel(writer, sheet_name=sheet_name, index=False, header=True)

            print("保存成功：", file_path)

        except Exception as e:
            raise RuntimeError(f"saveExcel:保存Excel失败 {str(e)}")


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
    try:
        sheet_name = 'Sheet2'
        start_row_index = int(26)
        start_column_index = int(1)
        img_row_index = int(1)

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

        df_start_row = start_row_index + 3

        for r_idx, row in enumerate(dataframe_to_rows(df, index=False, header=True), df_start_row):
            for c_idx, value in enumerate(row, start=start_column_index):
                sheet.cell(row=r_idx, column=c_idx, value=value)
            img_row_index = r_idx


        # 插入图片
        try:
            excel_img = XLImage(img_byte_arr)
            sheet._images = []
            img_cell = f"{get_column_letter(start_column_index+5)}{img_row_index+5}"
            sheet.add_image(excel_img, img_cell)
            print(f"图片已插入到位置: {img_cell}")
        except Exception as e:
            print(f"图片插入失败: {str(e)}")

        book.save(file_path)
        print(f"已保存工作表: {sheet_name}")
    except:
        print("保存失败，请检查文件是否被占用")
def dcgSave(file_path:str,df:object,start_row_index:int,start_column_index:int):
    try:
        sheet_name = 'Sheet2'
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

        for r_idx, row in enumerate(dataframe_to_rows(df, index=False, header=True), start_row_index):
            for c_idx, value in enumerate(row, start=start_column_index):
                sheet.cell(row=r_idx, column=c_idx, value=value)
        book.save(file_path)
        print(f"已保存工作表: {sheet_name}")
    except:
        print("保存失败，请检查文件是否被占用")

def dcgCodegen(file_path:str):
    workbook = load_workbook(file_path)  # 加载Excel文件
    worksheet = workbook['Sheet2']  # 选择指定的工作表，可根据实际修改
    # 激光沉积实验参数
    savedir =  os.path.dirname(file_path)
    Program_Name = str(worksheet['C3'].value)  # KUKA程序名称
    Program_Name = os.path.join(savedir, Program_Name)

    Before_Cladding_X = str(worksheet['C4'].value)  # 熔覆前移动距离(X)
    Before_Cladding_Y = str(worksheet['C5'].value)  # 熔覆前移动距离(Y)
    Before_Cladding_Z = str(worksheet['C6'].value)  # 熔覆前移动距离(Z)
    Laser_Spot = str(worksheet['C7'].value)  # 光斑电压调节，以调节光斑直径
    Protection_Gas_Before_Cladding = str(worksheet['C8'].value)  # 熔覆前保护气时间(s)
    Protection_Gas_After_Cladding = str(worksheet['C9'].value)  # 熔覆后保护气时间(s)
    Cladding_Speed = str(worksheet['C10'].value)  # 熔覆速度(m/s)
    Choose_Powder = str(worksheet['C11'].value)  # 粉桶选择
    Powder_Delivery_Speed = str(worksheet['C12'].value)  # 送粉转速(0.5:10r/min)
    Laser_Power = str(worksheet['C13'].value)  # 激光功率(1:4000W)
    Layers_Sum = int(worksheet['C14'].value)  # 层数
    # Pass_Number = str(worksheet['C15'].value)  # 道次数
    Pass_Distance = str(worksheet['C16'].value)  # 道次长度(mm)，熔覆方向为Y+
    Offset_Distance = str(worksheet['C17'].value)  # 偏移距离(mm)，偏移方向为X+
    # Opposite_Pass_Distance = str(-1 * int(Pass_Distance))  # 反向道次长度，熔覆方向为Y-
    Opposite_Offset_Distance = str(-1 * int(Offset_Distance))  # 反向偏移距离(mm)，偏移方向为X-
    After_Cladding_X = str(worksheet['C18'].value)  # 熔覆后移动距离(X)
    After_Cladding_Y = str(worksheet['C19'].value)  # 熔覆后移动距离(Y)
    After_Cladding_Z = str(worksheet['C20'].value)  # 熔覆后移动距离(Z)
    Wait_between_Layers = str(worksheet['C21'].value)  # 层间停留时间(s)

    # 监控设备是否选用；TRUE表示选用该监控设备；FALSE表示不选用
    GongYe_CCD = str(worksheet['H3'].value)  # CCD相机选用
    Dian_Temperature = str(worksheet['H4'].value)  # 点温仪选用
    GaoSu_Camera = str(worksheet['H5'].value)  # 高速相机选用
    Laser_LunKuo = str(worksheet['H6'].value)  # 激光轮廓仪选用

    # 激光轮廓仪扫描部分参数
    Before_Scanning_X = str(worksheet['M3'].value)  # 扫描前移动距离(X)
    Before_Scanning_Y = str(worksheet['M4'].value)  # 扫描前移动距离(Y)
    Before_Scanning_Z = str(worksheet['M5'].value)  # 扫描前移动距离(Z)
    Wait_Before_Scanning = str(worksheet['M6'].value)  # 扫描前等待时间(s)
    Scanning_Speed = str(worksheet['M7'].value)  # 扫描速度(m/s)
    Scanning_Y_Distance = str(worksheet['M8'].value)  # Y向扫描移动距离
    After_Scanning_X = str(worksheet['M9'].value)  # 扫描后移动距离(X)
    After_Scanning_Y = str(worksheet['M10'].value)  # 扫描后移动距离(Y)
    After_Scanning_Z = str(worksheet['M11'].value)  # 扫描后移动距离(Z)

    # 打开文件，使用 'w' 模式表示写入，如果文件不存在则创建，如果存在则覆盖原有内容
    file_name = Program_Name + ".src"
    original_stdout = sys.stdout
    try:
        with open(file_name, 'w') as f:
            sys.stdout = f
            # 定义KUKA程序名称
            print('DEF ' + Program_Name + '( )', end="")  # end=""用于消除后面的空行
            content_1 = """
            DECL INT i
            ;FOLD INI;%{PE}
              ;FOLD BASISTECH INI
                GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
                INTERRUPT ON 3 
                BAS (#INITMOV,0 )
              ;ENDFOLD (BASISTECH INI)
              ;FOLD USER INI
                ;Make your modifications here

              ;ENDFOLD (USER INI)
            ;ENDFOLD (INI)
            $VEL.CP = 0.010
            $ACC.CP = 10
            ptp $pos_act

            """
            content_1 = textwrap.dedent(content_1)
            print(content_1, end="")

            # 调节激光光斑电压
            print(
                ';FOLD ANOUT Laser_Spot=' + Laser_Spot + ' ;%{PE}%R 8.3.44,%MKUKATPBASIS,%CANA,%VANOUT_STAT,%P 2:CHANNEL_6, 4:' + Laser_Spot)
            print('$ANOUT[6]=' + Laser_Spot)
            print(';ENDFOLD')
            print()

            # 沉积前移动到沉积开始位置
            print('lin_rel {X ' + Before_Cladding_X + '} C_VEL')
            print('lin_rel {Y ' + Before_Cladding_Y + '} C_VEL')
            print('lin_rel {Z ' + Before_Cladding_Z + '} C_VEL')

            Layer_Number_List = [cell.value for row in
                                 worksheet.iter_rows(min_row=30, max_row=30 + Layers_Sum - 1, min_col=1, max_col=1) for
                                 cell
                                 in row]  # 层数列表，从第一层到最后一层

            for i in range(1, len(Layer_Number_List) + 1):

                # 读入每行的道次数和X方向坐标最小值和最大值
                # wb = load_workbook('Multi_Layers_Parameters.xlsx')
                # sheet = wb['Sheet1']
                Y_coordinate_List = [cell.value for row in
                                     worksheet.iter_rows(min_row=30, max_row=30 + len(Layer_Number_List) + 1, min_col=2,
                                                         max_col=2) for cell in row]
                Y_coordinate = Y_coordinate_List[i - 1]

                Pass_Number_List = [cell.value for row in
                                    worksheet.iter_rows(min_row=30, max_row=30 + len(Layer_Number_List) + 1, min_col=3,
                                                        max_col=3) for cell in row]
                Pass_Number = Pass_Number_List[i - 1]

                X_min_List = [cell.value for row in
                              worksheet.iter_rows(min_row=30, max_row=30 + len(Layer_Number_List) + 1, min_col=4,
                                                  max_col=4) for cell in row]
                X_min = X_min_List[i - 1]

                X_max_List = [cell.value for row in
                              worksheet.iter_rows(min_row=30, max_row=30 + len(Layer_Number_List) + 1, min_col=6,
                                                  max_col=6) for cell in row]
                X_max = X_max_List[i - 1]

                # Pass_Distance_List = [cell.value for row in  worksheet.iter_rows(min_row=30, max_row=30 + len(Layer_Number_List) + 1, min_col=8, max_col=8) for cell in row]
                # Pass_Distance = str(Pass_Distance_List[i - 1])

                # After_Cladding_Y_List = [cell.value for row in worksheet.iter_rows(min_row=30, max_row=30 + len(Layer_Number_List) + 1, min_col=9, max_col=9) for cell in row]
                # After_Cladding_Y = str(After_Cladding_Y_List[i - 1])

                # 开启保护气
                content_1_1 = """
                ;FOLD OUT 2 'Ar_ON' State=TRUE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:2, 3:Ar_ON, 5:TRUE, 6:
                $OUT[2]=TRUE
                ;ENDFOLD
                """
                content_1_1 = textwrap.dedent(content_1_1)
                print(content_1_1, end="")

                # 自定义前置保护气时间,时间最少为5s
                print('FOR i = 1 to ' + Protection_Gas_Before_Cladding, end="")
                content_2 = """
                ;FOLD WAIT Time= 1 sec;%{PE}%R 8.3.22,%MKUKATPBASIS,%CWAIT,%VWAIT,%P 2:1
                WAIT SEC 1
                ;ENDFOLD
                ENDFOR
                """
                content_2 = textwrap.dedent(content_2)
                print(content_2)

                # 自定义熔覆速度
                print('$VEL.CP = ' + Cladding_Speed, end="\n")
                print()

                # 自定义送粉桶和送粉转速，并等待三秒，保证送粉稳定
                if int(Choose_Powder) == 1:
                    print(
                        ';FOLD ANOUT PD_V1=' + Powder_Delivery_Speed + ' ;%{PE}%R 8.3.44,%MKUKATPBASIS,%CANA,%VANOUT_STAT,%P 2:CHANNEL_4, 4:' + Powder_Delivery_Speed)
                    print('$ANOUT[4]=' + Powder_Delivery_Speed, end="\n")
                    print(';ENDFOLD', end="")
                    content_3 = """
                    ;FOLD OUT 4 'PD1' State=TRUE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:4, 3:PD1, 5:TRUE, 6:
                    $OUT[4]=TRUE
                    ;ENDFOLD
                    ;FOLD WAIT Time= 3 sec;%{PE}%R 8.3.22,%MKUKATPBASIS,%CWAIT,%VWAIT,%P 2:3
                    WAIT SEC 3
                    ;ENDFOLD            
                    """
                else:
                    print(
                        ';FOLD ANOUT PD_V2=' + Powder_Delivery_Speed + ' ;%{PE}%R 8.3.44,%MKUKATPBASIS,%CANA,%VANOUT_STAT,%P 2:CHANNEL_4, 4:' + Powder_Delivery_Speed)
                    print('$ANOUT[5]=' + Powder_Delivery_Speed, end="\n")
                    print(';ENDFOLD', end="")
                    content_3 = """
                    ;FOLD OUT 5 'PD2' State=TRUE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:5, 3:PD2, 5:TRUE, 6:
                    $OUT[5]=TRUE
                    ;ENDFOLD
                    ;FOLD WAIT Time= 3 sec;%{PE}%R 8.3.22,%MKUKATPBASIS,%CWAIT,%VWAIT,%P 2:3
                    WAIT SEC 3
                    ;ENDFOLD
                    """
                content_3 = textwrap.dedent(content_3)
                print(content_3)

                # 自定义是否选用CCD相机
                if len(GongYe_CCD) == 4:
                    content_3_1 = """
                    ;FOLD OUT 6 'CCD_Camera' State=TRUE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:6, 3:CCD_Camera, 5:TRUE, 6:
                    $OUT[6]=TRUE
                    ;ENDFOLD
                    """
                    content_3_1 = textwrap.dedent(content_3_1)
                    print(content_3_1, end='')

                # 自定义是否选用点温仪
                if len(Dian_Temperature) == 4:
                    content_3_2 = """;FOLD OUT 7 'Point_Temperature' State=TRUE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:7, 3:Point_Temperature, 5:TRUE, 6:
                    $OUT[7]=TRUE
                    ;ENDFOLD
                    """
                    content_3_2 = textwrap.dedent(content_3_2)
                    print(content_3_2, end='')

                # 自定义是否选用高速相机
                if len(GaoSu_Camera) == 4:
                    content_3_3 = """;FOLD OUT 9 'High_Speed_Camera' State=TRUE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:9, 3:High_Speed_Camera, 5:TRUE, 6:
                    $OUT[9]=TRUE
                    ;ENDFOLD
                    """
                    content_3_3 = textwrap.dedent(content_3_3)
                    print(content_3_3, end="")

                # 自定义激光功率
                print()
                print(
                    ';FOLD ANOUT Laser_Power=' + Laser_Power + ' ;%{PE}%R 8.3.44,%MKUKATPBASIS,%CANA,%VANOUT_STAT,%P 2:CHANNEL_1, 4:' + Laser_Power)
                print('$ANOUT[1]=' + Laser_Power, end="\n")
                print(';ENDFOLD', end="")

                # 等待0.1s后开启激光
                content_4 = """
                ;FOLD WAIT Time= 0.1 sec;%{PE}%R 8.3.22,%MKUKATPBASIS,%CWAIT,%VWAIT,%P 2:0.1
                WAIT SEC 0.1
                ;ENDFOLD
                ;FOLD OUT 1 'Laser_ON' State=TRUE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:1, 3:Laser_ON, 5:TRUE, 6:
                $OUT[1]=TRUE
                ;ENDFOLD
                """
                content_4 = textwrap.dedent(content_4)
                print(content_4, end="")

                count = 1
                Pass_Number_Sum = 0  # 已经熔覆的道次数
                while count < i:
                    Pass_Number_Sum += Pass_Number_List[count - 1]
                    count += 1
                # print(i)
                # print('前'+str(i-1)+'层总道次数为：'+str(Pass_Number_Sum))

                if i == 1:
                    Pass_Number = Pass_Number_List[i - 1]
                    if int(Pass_Number) % 2 == 0:
                        Loop_Number = int(int(Pass_Number) / 2 - 1)
                        print('FOR i = 1 to ' + str(Loop_Number))
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('ENDFOR')
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL', end='')

                    else:
                        Loop_Number = (int(Pass_Number) - 1) / 2
                        Loop_Number = int(Loop_Number)
                        print('FOR i = 1 to ' + str(Loop_Number))
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('ENDFOR')
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL', end='')
                elif i >= 2 and i % 2 == 0 and Pass_Number_Sum % 2 == 0:
                    Pass_Number = Pass_Number_List[i - 1]
                    Offset_Distance = str(-1 * abs(float(Offset_Distance)))  # 第2层及其后面偶数层向X-偏移
                    Pass_Distance = str(abs(float(Pass_Distance)))  # 已经熔覆的总道次数为偶数，则该层第一道熔覆方向为Y+
                    if int(Pass_Number) % 2 == 0:
                        Loop_Number = int(Pass_Number) / 2 - 1
                        Loop_Number = int(Loop_Number)
                        print('FOR i = 1 to ' + str(Loop_Number))
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('ENDFOR')
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL', end='')

                    else:
                        Loop_Number = (int(Pass_Number) - 1) / 2
                        Loop_Number = int(Loop_Number)
                        print('FOR i = 1 to ' + str(Loop_Number))
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('ENDFOR')
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL', end='')
                elif i >= 2 and i % 2 != 0 and Pass_Number_Sum % 2 == 0:
                    Pass_Number = Pass_Number_List[i - 1]
                    Offset_Distance = str(abs(float(Offset_Distance)))  # 第3层及其之后的奇数层向X+偏移
                    Pass_Distance = str(abs(float(Pass_Distance)))  # 已经熔覆的总道次数为偶数，则该层第一道熔覆方向为Y+
                    if int(Pass_Number) % 2 == 0:
                        Loop_Number = int(Pass_Number) / 2 - 1
                        Loop_Number = int(Loop_Number)
                        print('FOR i = 1 to ' + str(Loop_Number))
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('ENDFOR')
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL', end='')

                    else:
                        Loop_Number = (int(Pass_Number) - 1) / 2
                        Loop_Number = int(Loop_Number)
                        print('FOR i = 1 to ' + str(Loop_Number))
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('ENDFOR')
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL', end='')
                elif i >= 2 and i % 2 == 0 and Pass_Number_Sum % 2 != 0:
                    Pass_Number = Pass_Number_List[i - 1]
                    Offset_Distance = str(-1 * abs(float(Offset_Distance)))  # 第2层及其后面偶数层向X-偏移
                    Pass_Distance = str(-1 * abs(float(Pass_Distance)))  # 已经熔覆的总道次数为奇数，则该层第一道熔覆方向为Y-
                    if int(Pass_Number) % 2 == 0:
                        Loop_Number = int(Pass_Number) / 2 - 1
                        Loop_Number = int(Loop_Number)
                        print('FOR i = 1 to ' + str(Loop_Number))
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('ENDFOR')
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL', end='')

                    else:
                        Loop_Number = (int(Pass_Number) - 1) / 2
                        Loop_Number = int(Loop_Number)
                        print('FOR i = 1 to ' + str(Loop_Number))
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('ENDFOR')
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL', end='')
                elif i >= 2 and i % 2 != 0 and Pass_Number_Sum % 2 != 0:
                    Pass_Number = Pass_Number_List[i - 1]
                    Offset_Distance = str(abs(float(Offset_Distance)))  # 第3层及其后面奇数层向X+偏移
                    Pass_Distance = str(-1 * abs(float(Pass_Distance)))  # 已经熔覆的总道次数为奇数，则该层第一道熔覆方向为Y-
                    if int(Pass_Number) % 2 == 0:
                        Loop_Number = int(Pass_Number) / 2 - 1
                        Loop_Number = int(Loop_Number)
                        print('FOR i = 1 to ' + str(Loop_Number))
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('ENDFOR')
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL', end='')

                    else:
                        Loop_Number = (int(Pass_Number) - 1) / 2
                        Loop_Number = int(Loop_Number)
                        print('FOR i = 1 to ' + str(Loop_Number))
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('lin_rel {Y ' + str(-1 * float(Pass_Distance)) + '} C_VEL')
                        print('lin_rel {X ' + Offset_Distance + '} C_VEL')
                        print('ENDFOR')
                        print('lin_rel {Y ' + Pass_Distance + '} C_VEL', end='')

                # 关闭激光
                content_5 = """
                ;FOLD OUT 1 'Laser_ON' State=FALSE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:1, 3:Laser_ON, 5:FALSE, 6:
                $OUT[1]=FALSE
                ;ENDFOLD
                """
                content_5 = textwrap.dedent(content_5)
                print(content_5, end="")

                # 激光功率归零
                print(';FOLD ANOUT Laser_Power=0 ;%{PE}%R 8.3.44,%MKUKATPBASIS,%CANA,%VANOUT_STAT,%P 2:CHANNEL_1, 4:0',
                      end='\n')
                print('$ANOUT[1]=0', end='\n')
                print(';ENDFOLD', end='\n')

                # 关闭送粉
                if int(Choose_Powder) == 1:
                    content_6 = """
                    ;FOLD OUT 4 'PD1' State=FALSE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:4, 3:PD1, 5:FALSE, 6:
                    $OUT[4]=FALSE
                    ;ENDFOLD

                    ;FOLD ANOUT PD_V1=0 ;%{PE}%R 8.3.44,%MKUKATPBASIS,%CANA,%VANOUT_STAT,%P 2:CHANNEL_4, 4:0
                    $ANOUT[4]=0
                    ;ENDFOLD
                    """
                    content_6 = textwrap.dedent(content_6)
                    print(content_6, end="")

                else:
                    content_6 = """
                    ;FOLD OUT 5 'PD2' State=FALSE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:5, 3:PD2, 5:FALSE, 6:
                    $OUT[5]=FALSE
                    ;ENDFOLD
                    ;FOLD ANOUT PD_V2=0 ;%{PE}%R 8.3.44,%MKUKATPBASIS,%CANA,%VANOUT_STAT,%P 2:CHANNEL_5, 4:0
                    $ANOUT[5]=0
                    ;ENDFOLD
                    """
                    content_6 = textwrap.dedent(content_6)
                    print(content_6, end="")

                # 等待0.5s，关闭高速相机
                if len(GaoSu_Camera) == 4:
                    content_6_1 = """;FOLD WAIT Time= 0.5 sec;%{PE}%R 8.3.22,%MKUKATPBASIS,%CWAIT,%VWAIT,%P 2:0.5
                    WAIT SEC 0.5
                    ;ENDFOLD
                    ;FOLD OUT 9 'High_Speed_Camera' State=FALSE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:9, 3:High_Speed_Camera, 5:FALSE, 6:
                    $OUT[9]=FALSE
                    ;ENDFOLD
                    """
                    content_6_1 = textwrap.dedent(content_6_1)
                    print(content_6_1, end="")

                # 等待0.5s，关闭CCD相机
                if len(GongYe_CCD) == 4:
                    content_6_2 = """;FOLD WAIT Time= 0.5 sec;%{PE}%R 8.3.22,%MKUKATPBASIS,%CWAIT,%VWAIT,%P 2:0.5
                    WAIT SEC 0.5
                    ;ENDFOLD
                    ;FOLD OUT 6 'CCD_Camera' State=FALSE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:6, 3:CCD_Camera, 5:FALSE, 6:
                    $OUT[6]=FALSE
                    ;ENDFOLD
                    """
                    content_6_2 = textwrap.dedent(content_6_2)
                    print(content_6_2, end="")

                # 沉积结束后5s后关闭点温仪
                if len(Dian_Temperature) == 4:
                    content_6_3 = """
                    ;FOLD WAIT Time= 5 sec;%{PE}%R 8.3.22,%MKUKATPBASIS,%CWAIT,%VWAIT,%P 2:5
                    WAIT SEC 5
                    ;ENDFOLD
                    ;FOLD OUT 7 'Point_Temperature' State=FALSE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:7, 3:Point_Temperature, 5:FALSE, 6:
                    $OUT[7]=FALSE
                    ;ENDFOLD
                    """
                    content_6_3 = textwrap.dedent(content_6_3)
                    print(content_6_3, end="")
                print()

                # 自定义后置保护气时间
                print('FOR i = 1 to ' + Protection_Gas_After_Cladding, end="")
                content_7 = """
                ;FOLD WAIT Time= 1 sec;%{PE}%R 8.3.22,%MKUKATPBASIS,%CWAIT,%VWAIT,%P 2:1
                WAIT SEC 1
                ;ENDFOLD
                ENDFOR
                """
                content_7 = textwrap.dedent(content_7)
                print(content_7, end="")

                # 关闭保护气
                '''
                content_8 = """;FOLD OUT 2 'Ar_ON' State=FALSE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:2, 3:Ar_ON, 5:FALSE, 6:
                $OUT[2]=FALSE
                ;ENDFOLD
                """
                content_8 = textwrap.dedent(content_8)
                print(content_8, end='')
                print()
                '''
                print(
                    ";FOLD OUT 2 'Ar_ON' State=FALSE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:2, 3:Ar_ON, 5:FALSE, 6:")
                print('$OUT[2]=FALSE')
                print(';ENDFOLD')

                # 自定义后置移动距离
                if i < len(Layer_Number_List) and Y_coordinate_List[i] != Y_coordinate_List[i - 1]:
                    X_min = float(X_min_List[i - 1])
                    X_min2 = float(X_min_List[i])

                    X_max = float(X_max_List[i - 1])
                    X_max2 = float(X_max_List[i])

                    if i % 2 == 0 and i < len(Layer_Number_List):
                        After_Cladding_X = X_min2 - X_min
                        # print(round(After_Cladding_X, 2))
                        print('lin_rel {X ' + str(round(After_Cladding_X, 2)) + '} C_VEL')
                        print('lin_rel {Y ' + After_Cladding_Y + '} C_VEL')
                        print('lin_rel {Z ' + After_Cladding_Z + '} C_VEL')
                        print()
                    elif i % 2 != 0 and i < len(Layer_Number_List):
                        After_Cladding_X = X_max2 - X_max
                        # print(round(After_Cladding_X, 2))
                        print('lin_rel {X ' + str(round(After_Cladding_X, 2)) + '} C_VEL')
                        print('lin_rel {Y ' + After_Cladding_Y + '} C_VEL')
                        print('lin_rel {Z ' + After_Cladding_Z + '} C_VEL')

                elif i < len(Layer_Number_List) and Y_coordinate_List[i] == Y_coordinate_List[i - 1]:
                    After_Cladding_X = float(X_min_List[i]) - float(X_max_List[i - 1])
                    print('lin_rel {X ' + str(round(After_Cladding_X, 2)) + '} C_VEL')
                    print('lin_rel {Y ' + After_Cladding_Y + '} C_VEL')
                    print('lin_rel {Z ' + After_Cladding_Z + '} C_VEL')
                    print()

                # 设置层间等待时间
                if i < len(Layer_Number_List):
                    if len(GaoSu_Camera) == 4 and len(GongYe_CCD) == 4 and len(Dian_Temperature) == 4:
                        Wait_between_Layers = int(worksheet['C21'].value) - 6 - int(
                            Protection_Gas_After_Cladding) - int(
                            Protection_Gas_Before_Cladding)
                    elif len(GongYe_CCD) == 4 and len(Dian_Temperature) == 4:
                        Wait_between_Layers = int(worksheet['C21'].value) - 5.5 - int(
                            Protection_Gas_After_Cladding) - int(
                            Protection_Gas_Before_Cladding)
                    elif len(GaoSu_Camera) == 4 and len(Dian_Temperature) == 4:
                        Wait_between_Layers = int(worksheet['C21'].value) - 5.5 - int(
                            Protection_Gas_After_Cladding) - int(
                            Protection_Gas_Before_Cladding)
                    elif len(GaoSu_Camera) == 4 and len(GongYe_CCD) == 4:
                        Wait_between_Layers = int(worksheet['C21'].value) - 1 - int(
                            Protection_Gas_After_Cladding) - int(
                            Protection_Gas_Before_Cladding)
                    elif len(GaoSu_Camera) == 4 or len(GongYe_CCD) == 4:
                        Wait_between_Layers = int(worksheet['C21'].value) - 0.5 - int(
                            Protection_Gas_After_Cladding) - int(
                            Protection_Gas_Before_Cladding)
                    elif len(Dian_Temperature) == 4:
                        Wait_between_Layers = int(worksheet['C21'].value) - 5 - int(
                            Protection_Gas_After_Cladding) - int(
                            Protection_Gas_Before_Cladding)
                    else:
                        Wait_between_Layers = int(worksheet['C21'].value) - int(Protection_Gas_After_Cladding) - int(
                            Protection_Gas_Before_Cladding)
                    Wait_Number = int(Wait_between_Layers + 30) // 30
                    Wait_Remainder = Wait_between_Layers % 30

                    for j in range(1, Wait_Number):
                        content_8_9 = """;FOLD WAIT Time= 30 sec;%{PE}%R 8.3.22,%MKUKATPBASIS,%CWAIT,%VWAIT,%P 2:30
                            WAIT SEC 30
                            ;ENDFOLD
                            """
                        content_8_9 = textwrap.dedent(content_8_9)
                        print(content_8_9, end="")
                    if Wait_Remainder != 0:
                        print(';FOLD WAIT Time= ' + str(
                            Wait_Remainder) + ' sec;%{PE}%R 8.3.22,%MKUKATPBASIS,%CWAIT,%VWAIT,%P 2:' + str(
                            Wait_Remainder))
                        print('WAIT SEC ' + str(Wait_Remainder))
                        print(';ENDFOLD')
                    else:
                        print()

                elif i == Layer_Number_List[-1]:
                    content_8_9_5 = """;FOLD WAIT Time= 15 sec;%{PE}%R 8.3.22,%MKUKATPBASIS,%CWAIT,%VWAIT,%P 2:15
                                    WAIT SEC 15
                                    ;ENDFOLD
                                    """
                    content_8_9_5 = textwrap.dedent(content_8_9_5)
                    print(content_8_9_5, end="")

            if len(Laser_LunKuo) != 4:
                print('END')

            # 如果选用激光轮廓仪进行表面形貌扫描
            elif len(Laser_LunKuo) == 4:
                # 自定义扫描前等待时间(s)
                print('FOR i = 1 to ' + Wait_Before_Scanning, end="")
                content_9 = """
                        ;FOLD WAIT Time= 1 sec;%{PE}%R 8.3.22,%MKUKATPBASIS,%CWAIT,%VWAIT,%P 2:1
                        WAIT SEC 1
                        ;ENDFOLD
                        ENDFOR
                        """
                content_9 = textwrap.dedent(content_9)
                print(content_9, end="")
                print()

                print('lin_rel {X ' + str(round(float(Before_Scanning_X), 1)) + '} C_VEL')
                print('lin_rel {Y ' + str(round(float(Before_Scanning_Y), 1)) + '} C_VEL')
                print('lin_rel {Z ' + str(round(float(Before_Scanning_Z), 1)) + '} C_VEL')

                # 自定义扫描速度(m/s)
                print('$VEL.CP = ' + Scanning_Speed, end="\n")

                # 开启激光轮廓仪
                content_10 = """
                ;FOLD OUT 8 'Laser_Profiler' State=TRUE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:8, 3:Laser_Profiler, 5:TRUE, 6:
                $OUT[8]=TRUE
                ;ENDFOLD
                 """
                content_10 = textwrap.dedent(content_10)
                print(content_10, end="")

                # X向扫描移动距离，正数表示向X+扫描
                print('lin_rel {Y ' + Scanning_Y_Distance + '} C_VEL', end="")

                # 关闭激光轮廓仪
                content_11 = """
                ;FOLD OUT 8 'Laser_Profiler' State=FALSE ;%{PE}%R 8.3.44,%MKUKATPBASIS,%COUT,%VOUTX,%P 2:8, 3:Laser_Profiler, 5:FALSE, 6:
                $OUT[8]=FALSE
                ;ENDFOLD
                """
                content_11 = textwrap.dedent(content_11)
                print(content_11)

                # 扫描后移动距离
                print('lin_rel {X ' + str(round(float(After_Scanning_X), 1)) + '} C_VEL')
                print('lin_rel {Y ' + str(round(float(After_Scanning_Y), 1)) + '} C_VEL')
                print('lin_rel {Z ' + str(round(float(After_Scanning_Z), 1)) + '} C_VEL')
                print()
                print('END', end="")

    except:
        pass
    finally:
        sys.stdout = original_stdout





