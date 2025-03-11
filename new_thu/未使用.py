
class cpltAreaShowWorker(QThread):
    # 定义完成信号（携带图像数据）和错误信号
    plot_complete = Signal(bytes)
    plot_error = Signal(str)
    def __init__(self, df, params):
        super().__init__()
        self.df = df  # 原始数据 [x, y, z]
        self.params = params  # 参数字典 {x_min, x_max, y_min, y_max}
    def run(self):
        try:
            # 解包数据
            x, y, z = self.df
            params = self.params
            # 筛选数据
            mask = (x >= params['x_min']) & (x <= params['x_max']) & \
                   (y >= params['y_min']) & (y <= params['y_max'])
            y_filtered = y[mask]
            z_filtered = z[mask]

            # 创建 DataFrame
            df = pd.DataFrame({"Y/mm": y_filtered, "Z/mm": z_filtered})

            # 数据处理流程
            df = df.drop_duplicates(subset=["Y/mm"], keep="first")
            df["Y/mm"] = df["Y/mm"] - df["Y/mm"].min()
            df["Z/mm"] = df["Z/mm"] - df["Z/mm"].min()

            # 生成图表
            fig = Figure(figsize=(8, 4))
            ax = fig.add_subplot(111)
            ax.plot(df["Y/mm"], df["Z/mm"], color='b', linestyle='-', linewidth=2)
            ax.set(xlim=[0, 190], ylim=[0, 12],
                   xlabel='Y/mm', ylabel='Z/mm',
                   title='横截面形状')
            ax.grid(True, linestyle=':', color='gray')
            fig.tight_layout()

            # 渲染图像
            canvas = FigureCanvasAgg(fig)
            canvas.draw()
            img_data = canvas.buffer_rgba()

            # 发射完成信号（携带图像原始数据）
            self.plot_complete.emit(img_data)

        except Exception as e:
            self.plot_error.emit(f"绘图错误: {str(e)}")


    def cpltAreaAcqVF(self):
        if self.cpltAreaAcqF:
            print("cpltAreaAcqVF:", self.cpltAreaAcqF)
        else:
            print("cpltAreaAcqF didnt choose a file")

    ## 补形区域获取-截面显示按键-截面显示
    def cpltAreaAcqShow(self):
        try:
            if self.cpltAreaAcqF:
                params = {
                    'x_min': self.ui.xminDSBox.value(),
                    'x_max': self.ui.xmaxDSBox.value(),
                    'y_min': self.ui.yminDSBox.value(),
                    'y_max': self.ui.ymaxDSBox.value()
                }
            if self.df:
                self.ui.cpltAreaShowLabel.setText("数据计算中")
                self.ui.cpltAreaAcqShowBtn.setEnabled(False)  # 禁用按钮

                # 创建线程和 Worker
                self.cpltAreathread2 = QThread()
                self.cpltAreaworker2 = cpltAreaShowWorker(self.df,params)

                # 将 Worker 移动到线程
                self.cpltAreaworker2.moveToThread(self.cpltAreathread2)

                # 连接信号与槽
                self.cpltAreathread2.started.connect(self.cpltAreaworker2.run)
                self.cpltAreaworker2.plot_complete.connect(self.cpltAreashow)
                self.cpltAreaworker2.plot_error.connect(self.thread_error)
                self.cpltAreaworker2.finished.connect(self.cpltAreathread2.quit)
                self.cpltAreaworker2.finished.connect(self.cpltAreaworker2.deleteLater)
                self.cpltAreathread2.finished.connect(self.cpltAreathread2.deleteLater)
                # 启动线程
                self.cpltAreathread2.start()
        except:
            print("cpltAreaAcqShow:", "请选择点云")


    def cpltAreashow(self, img_data):
        # 将图像数据转换为 QPixmap
        img_array = np.frombuffer(img_data, dtype=np.uint8)
        width, height = 800, 400  # 必须与 figsize 一致
        img_array = img_array.reshape((height, width, 4))

        pixmap = QPixmap.fromImage(
            QImage(img_array.data, width, height, QImage.Format_RGBA8888)
        )

        # 更新 QLabel
        self.ui.cpltAreaShowLabel.setPixmap(pixmap)
        self.ui.cpltAreaShowLabel.setScaledContents(True)
        self.ui.cpltAreaAcqShowBtn.setEnabled(True)
