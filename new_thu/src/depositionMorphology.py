import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import os
import matplotlib.pyplot as plt

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

            fig = Figure(figsize=(8, 4))
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

            # 确保目录存在
            os.makedirs(save_dir, exist_ok=True)

            # 构造文件路径
            file_path = os.path.join(save_dir, "表面原位补形.xlsx")

            # 保存数据（重命名列标题）
            self.df_processed.to_excel(
                file_path,
                sheet_name="Sheet1",
                columns=["Y/mm", "Z/mm"],
                header=["Y(mm)", "Z(mm)"],
                index=False
            )
            print("保存成功：",file_path,"表面原位补形.xlsx")

        except Exception as e:
            raise RuntimeError(f"保存Excel失败: {str(e)}")
