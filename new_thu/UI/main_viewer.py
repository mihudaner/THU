from utils import *
from openpyxl import load_workbook
from main_Pwindow import *
@unique
class NodeType(Enum):
    """节点类型，文件还是文件夹"""
    NodeDir = 0
    NodeFile = 1
class MainWindow(QMainWindow):
    info_dict = {"具体材料": [], "材料类型": [], "工艺类型": [], "具体设备": [], "模型类型": [], "模型工艺类型": []}
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Main Window')

        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")
        self.jt_cls = []
        self.jt_sb = []
        self.cl_styles = []
        self.gy_styles = []
        self.cx_styles = []
        self.mxgy_styles = []
        self.mx_styles = []

        self.initUI()  # 初始化窗口

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #文件
        dropdown_menu = QMenu()
        dropdown_menu.addAction(self.ui.w_path)
        dropdown_menu.addAction(self.ui.w_save)
        dropdown_menu.addAction(self.ui.w_save_as)
        dropdown_menu.addAction(self.ui.w_quit)

        # self.ui.file_menu.setMenu(dropdown_menu)
        # 连接 QAction 的触发信号到菜单
        self.ui.file_menu.triggered.connect(lambda: dropdown_menu.exec_(self.ui.toolBar.mapToGlobal(self.ui.toolBar.rect().bottomLeft())))
        self.ui.w_quit.triggered.connect(QApplication.quit)
        self.ui.w_path.triggered.connect(self.select_database)
        self.ui.w_save.triggered.connect(self.saveAll)
        # 另存为
        self.ui.w_save_as.triggered.connect(self.save_as)

        self.model = QFileSystemModel()
        self.treeWidget = self.ui.treeWidget
        self.root = "../database"
        self.dataroot = osp.join(self.root, "数据库")
        self.projectroot = osp.join(self.root, "项目库")
        self.choosed_project = osp.join(self.projectroot, "项目一")
        self.kupath = None
        self.treeWidget.itemClicked.connect(self.on_item_clicked)  # Connect the itemClicked signal to a slot function
        self.treeWidget.itemDoubleClicked.connect(self.on_item_double_clicked)  # 双击信号
        # 全部
        self.ui.show_all.triggered.connect(partial(self.select_database, note="fresh"))
        # 材料
        self.ui.cl_open.triggered.connect(partial(self.select_data, note="材料"))
        # 设备
        self.ui.sb_open.triggered.connect(partial(self.select_data, note="设备"))
        # 工艺
        self.ui.gy_open.triggered.connect(partial(self.select_data, note="工艺"))
        # 程序
        self.ui.cx_open.triggered.connect(partial(self.select_data, note="程序"))
        # 模型
        self.ui.mx_open.triggered.connect(partial(self.select_data, note="模型"))
        # 项目
        self.ui.xm_open.triggered.connect(partial(self.select_data, note="项目"))

        # Enable custom context menu
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 右击显示菜单
        self.treeWidget.customContextMenuRequested.connect(partial(show_context_menu, self))
        self.initData()
    def initData(self):
        path1 = osp.join(self.dataroot, '材料库')
        self.cl_styles = self.get_folder_names(path1)
        self.jt_cls = []
        for cl_style in self.cl_styles:
            path = osp.join(path1, cl_style)
            xlsx_files = self.get_xlsx_files(path)
            # 将 xlsx_files 包含的文件名添加到 self.jt_cls
            for xlsx_file in xlsx_files:
                self.jt_cls.append(xlsx_file)

        path2 = osp.join(self.dataroot, '工艺库')
        self.gy_styles = self.get_folder_names(path2)

        path3 = osp.join(self.dataroot, '程序库')
        self.cx_styles = self.get_folder_names(path3)

        path4 = osp.join(self.dataroot, '模型库')
        self.mxgy_styles = self.get_folder_names(path4)
        mx_styles_set = set()
        for i in range(len(self.mxgy_styles)):
            path4_1 = osp.join(path4, self.mxgy_styles[i])  # 使用 i 而不是 0
            mx_styles = self.get_folder_names(path4_1)
            for j in range(len(mx_styles)):
                mx_styles_set.add(mx_styles[j])  # 将获取的文件夹名称添加到集合中
        self.mx_styles = list(mx_styles_set)  # 转换为列表（可选）

        path5 = osp.join(self.dataroot, '设备库')
        styles_sb = self.get_folder_names(path5)
        for style_sb in styles_sb:
            path = osp.join(path5, style_sb)
            sb_files = self.get_folder_names(path)
            for sb_file in sb_files:
                self.jt_sb.append(sb_file)

        MainWindow.info_dict["材料类型"] = self.cl_styles
        MainWindow.info_dict["具体材料"] = self.jt_cls
        MainWindow.info_dict["具体设备"] = self.jt_sb
        MainWindow.info_dict["工艺类型"] = self.gy_styles
        MainWindow.info_dict["程序类型"] = self.cx_styles
        MainWindow.info_dict["模型工艺类型"] = self.mxgy_styles
        MainWindow.info_dict["模型类型"] = self.mx_styles

    def get_xlsx_files(self, path):
        try:
            # 列出目录中的所有内容
            dir_contents = os.listdir(path)

            # 过滤出 .xlsx 文件
            xlsx_files = [osp.splitext(name)[0] for name in dir_contents if name.endswith('.xlsx') and osp.isfile(osp.join(path, name))]

            return xlsx_files
        except FileNotFoundError:
            print(f"路径 {path} 不存在")
            return []
        except Exception as e:
            print(f"遍历路径 {path} 时发生错误: {e}")
            return []
    def get_folder_names(self, path):
        try:
            # 列出目录中的所有内容
            dir_contents = os.listdir(path)

            # 过滤出文件夹
            folders = [name for name in dir_contents if osp.isdir(osp.join(path, name))]

            return folders
        except FileNotFoundError:
            print(f"路径 {path} 不存在")
            return []
        except Exception as e:
            print(f"遍历路径 {path} 时发生错误: {e}")
            return []

    def saveAll(self):
        target_directory = QFileDialog.getExistingDirectory(self, "选择目标文件夹")
        # 确保目标目录存在
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        # 定义源目录
        dir_path = self.root
        # 确保源目录存在
        if not os.path.exists(dir_path):
            print(f"源目录 {dir_path} 不存在。")
            return
        # 复制文件夹
        try:
            # 计算目标路径
            target_path = os.path.join(target_directory, os.path.basename(dir_path))
            shutil.copytree(dir_path, target_path)
            print(f"成功将 {dir_path} 复制到 {target_path}")
        except Exception as e:
            print(f"复制过程中发生错误: {e}")

    def save_as(self):
        dialog = SaveAsDialog(self)
        dialog.exec_()
    def filter(self, item):
        if item.text(0)=='程序库':
            dialog = FilterCX(self, item)
        elif item.text(0)=='模型库':
            dialog = FilterMX(self, item)
        elif item.text(0)=='项目库':
            dialog = FilterMX(self, item)
        else:
            dialog = FilterMX(self, item)
        dialog.exec_()

    #选择总库
    def select_database(self, note=None):
        self.treeWidget.clear()
        if note != "fresh":
            #新的database路径
            dataroot = QFileDialog.getExistingDirectory(self, "选择工程目录", ".",
                            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
            if dataroot:
                self.dataroot = dataroot
        if self.dataroot:
            # top_item = self.create_top_item(self.root, value='all')  # 创建topitem
            self.list_dir(None, self.dataroot)  # 递归遍历

        else:
            # 创建一个警告对话框
            warning_box = QMessageBox(self)
            warning_box.setIcon(QMessageBox.Warning)  # 设置图标为警告图标
            warning_box.setText("数据库未选择！")  # 警告文本
            warning_box.setWindowTitle("警告")  # 对话框标题
            warning_box.setStandardButtons(QMessageBox.Ok)  # 添加按钮
            # 显示对话框并获取用户选择
            warning_box.exec_()
    #选择数据库
    def select_data(self, note=None):
        self.treeWidget.clear()
        if note == "材料" or note == "cl_fresh":
            self.kupath = osp.join(self.dataroot, "材料库")
            top_item = self.create_top_item(self.kupath, "材料")  # 创建topitem
            top_item.setExpanded(True)  # 固定展开 top_item
            self.list_dir(top_item, self.kupath, "材料")  # 递归遍历
        elif note == "设备" or note == "sb_fresh":
            self.kupath = osp.join(self.dataroot, "设备库")
            top_item = self.create_top_item(self.kupath, "设备")  # 创建topitem
            top_item.setExpanded(True)  # 固定展开 top_item
            self.list_dir(top_item, self.kupath, "设备")  # 递归遍历
        elif note == "工艺" or note == "gy_fresh":
            self.kupath = osp.join(self.dataroot, "工艺库")
            top_item = self.create_top_item(self.kupath, "工艺")  # 创建topitem
            top_item.setExpanded(True)  # 固定展开 top_item
            self.list_dir(top_item, self.kupath, "工艺")  # 递归遍历
        elif note == "程序" or note == "cx_open":
            self.kupath = osp.join(self.dataroot, "程序库")
            top_item = self.create_top_item(self.kupath, "程序")  # 创建topitem
            top_item.setExpanded(True)  # 固定展开 top_item
            self.list_dir(top_item, self.kupath, "程序")  # 递归遍历
        elif note == "模型" or note == "mx_fresh":
            self.kupath = osp.join(self.dataroot, "模型库")
            top_item = self.create_top_item(self.kupath, "模型")  # 创建topitem
            top_item.setExpanded(True)  # 固定展开 top_item
            self.list_dir(top_item, self.kupath, "模型")  # 递归遍历
        elif note == "项目" or note == "xm_fresh":
            top_item = self.create_top_item(self.projectroot, "项目")  # 创建topitem
            top_item.setExpanded(True)  # 固定展开 top_item
            self.list_dir(top_item, self.projectroot, "项目")  # 递归遍历
        else:
            return
        self.initData()

    #实现打开功能的槽函数
    def open_type_library(self, item):
        project_path = item.data(0, Qt.UserRole)
        print(project_path)
        if project_path:
            # 将相对路径转换为绝对路径
            absolute_path = os.path.abspath(project_path)
            # 打开文件浏览器显示该路径，以下代码适用于Windows系统
            subprocess.Popen(f'explorer "{absolute_path}"')

    # 实现刷新的槽函数
    def refresh_type_library(self):
        self.updateShow()

    def list_project_dir(self, parent, directory):
        for obj in os.listdir(directory):
            tmp_path = osp.join(directory, obj)
            if osp.isdir(tmp_path):
                dir_item = self._generate_item(parent, obj, tmp_path, NodeType.NodeDir.value)
                self.list_dir(dir_item, tmp_path)
            else:
                self._generate_item(parent, obj, tmp_path, NodeType.NodeFile.value)

    def list_dir(self, parent, directory, value=None):
        if parent==None:
            # 首先处理 "材料库"
            if "材料库" in os.listdir(directory):
                cl_item = self._generate_item(None, "材料库", osp.join(directory, "材料库"), NodeType.NodeDir.value)
                self.ui.treeWidget.addTopLevelItem(cl_item)
                self.list_dir(cl_item, osp.join(directory, "材料库"))
            if "设备库" in os.listdir(directory):
                cl_item = self._generate_item(None, "设备库", osp.join(directory, "设备库"), NodeType.NodeDir.value)
                self.ui.treeWidget.addTopLevelItem(cl_item)
                self.list_dir(cl_item, osp.join(directory, "设备库"))
            if "工艺库" in os.listdir(directory):
                cl_item = self._generate_item(None, "工艺库", osp.join(directory, "工艺库"), NodeType.NodeDir.value)
                self.ui.treeWidget.addTopLevelItem(cl_item)
                self.list_dir(cl_item, osp.join(directory, "工艺库"))
            if "程序库" in os.listdir(directory):
                cl_item = self._generate_item(None, "程序库", osp.join(directory, "程序库"), NodeType.NodeDir.value)
                self.ui.treeWidget.addTopLevelItem(cl_item)
                self.list_dir(cl_item, osp.join(directory, "程序库"))
            if "模型库" in os.listdir(directory):
                cl_item = self._generate_item(None, "模型库", osp.join(directory, "模型库"), NodeType.NodeDir.value)
                self.ui.treeWidget.addTopLevelItem(cl_item)
                self.list_dir(cl_item, osp.join(directory, "模型库"))
            if "项目库" in os.listdir(directory):
                cl_item = self._generate_item(None, "项目库", osp.join(directory, "项目库"), NodeType.NodeDir.value)
                self.ui.treeWidget.addTopLevelItem(cl_item)
                self.list_dir(cl_item, osp.join(directory, "项目库"))
        # elif parent.data(0, Qt.UserRole + 1) in ["具体模型", "具体项目"]:
        #     pass
        else:
            for obj in os.listdir(directory):
                tmp_path = osp.join(directory, obj)
                if osp.isdir(tmp_path):
                    dir_item = self._generate_item(parent, obj, tmp_path, NodeType.NodeDir.value)
                    self.list_dir(dir_item, tmp_path)
                else:
                    self._generate_item(parent, obj, tmp_path, NodeType.NodeFile.value)

    def _generate_item(self, parent, name, path, node_type):
        item = QTreeWidgetItem()
        if name.endswith('json'):
            name = name.rstrip('.json')
        elif name.endswith('xlsx'):
            name = name.rstrip('.xlsx')
        if name.endswith('bak'):
            item.setHidden(True)

        item.setText(0, name)
        item.setToolTip(0, path)
        item.setData(0, Qt.UserRole, path)

        # 设置列表展示顺序
        if parent is not None:
            if parent.data(0, Qt.UserRole + 1) == "具体项目":
                # 设置插入顺序的优先级
                order = {
                    '类型及设备': 0,
                    '材料及工艺': 1,
                    '项目程序': 2,
                    '熔覆监控': 3,
                    '分析预测': 4,
                }
                insert_priority = order.get(name, None)
                if insert_priority is not None:
                    # 确定插入位置
                    current_count = parent.childCount()
                    inserted = False
                    for i in range(current_count):
                        current_child = parent.child(i)
                        current_name = current_child.text(0)
                        current_priority = order.get(current_name, float('inf'))

                        if insert_priority < current_priority:
                            parent.insertChild(i, item)
                            inserted = True
                            break
                    if not inserted:
                        parent.addChild(item)  # 如果没有合适的位置，添加到最后
                else:
                    parent.addChild(item)
            elif parent.data(0, Qt.UserRole + 1) == "项目包含项" and parent.text(0) == "熔覆监控":
                # 设置插入顺序的优先级
                order = {
                    '实时反馈': 0,
                    '熔池状态': 1,
                    '熔池温度': 2,
                    '熔池流动': 3,
                    '熔池尺寸': 4,
                    '熔覆形貌': 5,
                }
                insert_priority = order.get(name, None)
                if insert_priority is not None:
                    # 确定插入位置
                    current_count = parent.childCount()
                    inserted = False
                    for i in range(current_count):
                        current_child = parent.child(i)
                        current_name = current_child.text(0)
                        current_priority = order.get(current_name, float('inf'))
                        if insert_priority < current_priority:
                            parent.insertChild(i, item)
                            inserted = True
                            break
                    if not inserted:
                        parent.addChild(item)  # 如果没有合适的位置，添加到最后
                else:
                    parent.addChild(item)
            elif parent.data(0, Qt.UserRole + 1) == "项目包含项" and parent.text(0) == "分析预测":
                # 设置插入顺序的优先级
                order = {
                    '熔池多相流': 0,
                    '热力耦合': 1,
                    'PINN': 2,
                    'LBM': 3,
                }
                insert_priority = order.get(name, None)
                if insert_priority is not None:
                    # 确定插入位置
                    current_count = parent.childCount()
                    inserted = False
                    for i in range(current_count):
                        current_child = parent.child(i)
                        current_name = current_child.text(0)
                        current_priority = order.get(current_name, float('inf'))
                        if insert_priority < current_priority:
                            parent.insertChild(i, item)
                            inserted = True
                            break
                    if not inserted:
                        parent.addChild(item)  # 如果没有合适的位置，添加到最后
                else:
                    parent.addChild(item)
            elif parent.data(0, Qt.UserRole + 1) == "设备库":
                # 设置插入顺序的优先级
                order = {
                    '能量': 0,
                    '质量': 1,
                    '运动': 2,
                    '激光头': 3,
                    '气氛': 4,
                    '冷却': 5,
                    '监控': 6,
                    '其他': 7,
                }
                insert_priority = order.get(name, None)
                if insert_priority is not None:
                    # 确定插入位置
                    current_count = parent.childCount()
                    inserted = False
                    for i in range(current_count):
                        current_child = parent.child(i)
                        current_name = current_child.text(0)
                        current_priority = order.get(current_name, float('inf'))
                        if insert_priority < current_priority:
                            parent.insertChild(i, item)
                            inserted = True
                            break
                    if not inserted:
                        parent.addChild(item)  # 如果没有合适的位置，添加到最后
                else:
                    parent.addChild(item)
            elif parent.data(0, Qt.UserRole + 1) == "具体设备":
                if item.text(0) == "设备文件":
                    parent.insertChild(0, item)
                else:
                    parent.addChild(item)
            else:
                parent.addChild(item)  # 如果不是以上，默认添加到最后
        else:
            if item.text(0) == "材料库":
                item.setData(0, Qt.UserRole + 1, "材料库")
            elif item.text(0) == "设备库":
                item.setData(0, Qt.UserRole + 1, "设备库")
            elif item.text(0) == "工艺库":
                item.setData(0, Qt.UserRole + 1, "工艺库")
            elif item.text(0) == "程序库":
                item.setData(0, Qt.UserRole + 1, "程序库")
            elif item.text(0) == "模型库":
                item.setData(0, Qt.UserRole + 1, "模型库")
            elif item.text(0) == "项目库":
                item.setData(0, Qt.UserRole + 1, "项目库")
            self.treeWidget.addTopLevelItem(item)

        if name.endswith('bak'):
            item.setHidden(True)

        if item.parent() is not None:  # 父节点为database
            if item.parent().data(0, Qt.UserRole + 1) == "材料库":
                item.setData(0, Qt.UserRole+1, "材料类型")
            elif item.parent().data(0, Qt.UserRole + 1) == "材料类型":
                item.setData(0, Qt.UserRole + 1, "具体材料")
            elif item.parent().data(0, Qt.UserRole + 1) == "设备库":
                item.setData(0, Qt.UserRole+1, "设备类型")
                item.setExpanded(True)
            elif item.parent().data(0, Qt.UserRole + 1) == "设备类型":
                item.setData(0, Qt.UserRole + 1, "具体设备")
            elif item.parent().data(0, Qt.UserRole + 1) == "具体设备":
                if item.text(0) == "设备文件":
                    item.setData(0, Qt.UserRole + 1, "设备文件")
                elif item.text(0) == "设备图片":
                    item.setData(0, Qt.UserRole + 1, "设备图片")
            elif item.parent().data(0, Qt.UserRole + 1) == "工艺库":
                item.setData(0, Qt.UserRole+1, "工艺类型")
            elif item.parent().data(0, Qt.UserRole + 1)=="工艺类型":
                item.setData(0, Qt.UserRole+1, "具体工艺")
            elif item.parent().data(0, Qt.UserRole + 1) == "程序库":
                item.setData(0, Qt.UserRole+1, "程序类型")
                item.setExpanded(True)
            elif item.parent().data(0, Qt.UserRole + 1)=="程序类型":
                item.setData(0, Qt.UserRole+1, "具体程序")
                # item.setExpanded(True)
            elif item.parent().data(0, Qt.UserRole + 1) == "模型库":
                item.setData(0, Qt.UserRole+1, "模型工艺类型")
                item.setExpanded(True)
            elif item.parent().data(0, Qt.UserRole + 1) == "模型工艺类型":
                item.setData(0, Qt.UserRole+1, "模型类型")
                item.setExpanded(True)
            elif item.parent().data(0, Qt.UserRole + 1) == "模型类型":
                item.setData(0, Qt.UserRole+1, "具体模型")
            elif item.parent().data(0, Qt.UserRole + 1) == "项目库":
                item.setData(0, Qt.UserRole + 1, "具体项目")
                item.setExpanded(True)
            elif item.parent().data(0, Qt.UserRole + 1) == "具体项目":
                item.setData(0, Qt.UserRole + 1, "项目包含项")
                if item.text(0) in ["分析预测", "熔覆监控"]:
                    item.setExpanded(True)
            elif item.parent().data(0, Qt.UserRole + 1) == "项目包含项" and item.parent().text(0) == "熔覆监控":
                item.setData(0, Qt.UserRole + 1, "熔覆监控")
            elif item.parent().data(0, Qt.UserRole + 1) == "项目包含项" and item.parent().text(0) == "分析预测":
                item.setData(0, Qt.UserRole + 1, "分析预测")

        # 设置图标路径
        if node_type == NodeType.NodeDir.value:
            icon_path = os.path.join('..', 'resource', 'icon', 'dir.png')
        else:
            icon_path = os.path.join('..', 'resource', 'icon', 'doc.png')

        # 检查文件是否存在
        if os.path.exists(icon_path):
            item.setIcon(0, QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")
        return item

    def create_top_item(self, project_path, value=None):
        # 如果 value 为 "all"，则不添加这个 item
        if value == "all":
            return None  # 不显示顶级节点
        # 根节点
        project_name = osp.basename(project_path)
        top_item = QTreeWidgetItem(self.ui.treeWidget, NodeType.NodeDir.value)
        top_item.setText(0, project_name)
        top_item.setToolTip(0, project_path)
        top_item.setData(0, Qt.UserRole, project_path)

        # 设置图标
        icon_path = os.path.join('..', 'resource', 'icon', 'dir.png')
        top_item.setIcon(0, QIcon(icon_path))
        # 设置节选数据标记
        if value == "材料":
            top_item.setData(0, Qt.UserRole + 1, "材料库")
        elif value == "设备":
            top_item.setData(0, Qt.UserRole + 1, "设备库")
        elif value == "工艺":
            top_item.setData(0, Qt.UserRole + 1, "工艺库")
        elif value == "程序":
            top_item.setData(0, Qt.UserRole + 1, "程序库")
        elif value == "模型":
            top_item.setData(0, Qt.UserRole + 1, "模型库")
        elif value == "项目":
            top_item.setData(0, Qt.UserRole + 1, "项目库")
        elif value == "所选项目":
            top_item.setData(0, Qt.UserRole + 1, "所选项目")
        # 将顶级项添加到树形控件中
        self.ui.treeWidget.addTopLevelItem(top_item)

        return top_item

    #单击在状态栏显示路径
    def on_item_clicked(self, item):
        project_path = item.data(0, Qt.UserRole)
        if project_path:
            self.ui.status.showMessage(
                f"Path: {project_path}")

    #设置双击事件
    def on_item_double_clicked(self, item):
        # 防止双击节点展开/收起
        if item.isExpanded():
            item.setExpanded(False)
        else:
            item.setExpanded(True)
        project_path = item.data(0, Qt.UserRole)
        if osp.isdir(project_path):
            self.open_type_library(item)
        elif item.data(0, Qt.UserRole + 1) == "具体材料":
            self.edit(item)
        elif item.data(0, Qt.UserRole + 1) == "具体工艺":
            self.edit(item)
        elif item.parent().data(0, Qt.UserRole + 1) in ["设备文件", "设备图片"]:
            path = item.data(0, Qt.UserRole)
            subprocess.run(['start', '', path], shell=True)
        elif item.data(0, Qt.UserRole + 1) == "熔覆监控" and item.text(0) == "实时反馈":
            # item.data(0, Qt.UserRole)是当前节点的实际路径，设计函数时把item传进去来获得保存路径
            # 你也可以设计函数，在里面根据item.text(0)来选择操作逻辑
            pass
        elif item.data(0, Qt.UserRole + 1) == "熔覆监控" and item.text(0) == "熔池状态":
            pass
        elif item.data(0, Qt.UserRole + 1) == "熔覆监控" and item.text(0) == "熔池温度":
            pass
        elif item.data(0, Qt.UserRole + 1) == "熔覆监控" and item.text(0) == "熔池流动":
            pass
        elif item.data(0, Qt.UserRole + 1) == "熔覆监控" and item.text(0) == "熔池尺寸":
            pass
        elif item.data(0, Qt.UserRole + 1) == "熔覆监控" and item.text(0) == "熔覆形貌":
            pass
        elif item.data(0, Qt.UserRole + 1) == "分析预测":
            # 可以设计函数，在里面根据item.text(0)来选择操作逻辑 ['PINN','LBM',...]
            pass

    #编辑
    def edit(self, item):
        project_path = item.data(0, Qt.UserRole)
        print(project_path)
        if item.data(0, Qt.UserRole + 1) == "具体材料":
            dialog = MaterialDialog(item)
            dialog.exec_()
        elif item.data(0, Qt.UserRole + 1) == "具体工艺":
            dialog = ProcessDialog(self, item)
            dialog.exec_()
        elif item.data(0, Qt.UserRole + 1) == "具体设备":
            dialog = EquipmentDialog(self, item)
            dialog.exec_()
            while item.childCount() > 0:
                item.removeChild(item.child(0))
            # 重新生成子项
            for obj in os.listdir(item.data(0, Qt.UserRole)):
                tmp_path = osp.join(item.data(0, Qt.UserRole), obj)
                if osp.isdir(tmp_path):
                    dir_item = self._generate_item(item, obj, tmp_path, NodeType.NodeDir.value)
                    self.list_dir(dir_item, tmp_path)  # 递归调用
                else:
                    self._generate_item(item, obj, tmp_path, NodeType.NodeFile.value)
        elif item.data(0, Qt.UserRole + 1) == "具体模型":
            dialog = ModelDialog(self, item)
            dialog.exec_()
            while item.childCount() > 0:
                item.removeChild(item.child(0))
            # 重新生成子项
            for obj in os.listdir(item.data(0, Qt.UserRole)):
                tmp_path = osp.join(item.data(0, Qt.UserRole), obj)
                if osp.isdir(tmp_path):
                    dir_item = self._generate_item(item, obj, tmp_path, NodeType.NodeDir.value)
                    self.list_dir(dir_item, tmp_path)  # 递归调用
                else:
                    self._generate_item(item, obj, tmp_path, NodeType.NodeFile.value)
        elif item.data(0, Qt.UserRole + 1) == "具体程序":
            dialog = ProgramDialog(self, item)
            dialog.exec_()
            while item.childCount() > 0:
                item.removeChild(item.child(0))
            # 重新生成子项
            for obj in os.listdir(item.data(0, Qt.UserRole)):
                tmp_path = osp.join(item.data(0, Qt.UserRole), obj)
                if osp.isdir(tmp_path):
                    dir_item = self._generate_item(item, obj, tmp_path, NodeType.NodeDir.value)
                    self.list_dir(dir_item, tmp_path)  # 递归调用
                else:
                    self._generate_item(item, obj, tmp_path, NodeType.NodeFile.value)

    def delete(self, item):
        project_path = item.data(0, Qt.UserRole)
        print("delete")
        print(project_path)
        # 弹出提示，询问是否确认删除文件project_path
        reply = QMessageBox.question(
            self,
            '确认删除',
            f'您确认要删除文件: {project_path} 吗？',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            if os.path.exists(project_path):
                try:
                    if os.path.isdir(project_path):
                        shutil.rmtree(project_path)  # 删除文件夹及其中的内容
                        # QMessageBox.information(self, '提示', f'文件夹已删除: {project_path}')
                    else:
                        os.remove(project_path)  # 删除文件
                        # QMessageBox.information(self, '提示', f'文件已删除: {project_path}')
                    # 从树中删除该项，因为是子项，使用父项来删除
                    parent_item = item.parent()
                    index = parent_item.indexOfChild(item)
                    parent_item.takeChild(index)
                except Exception as e:
                    QMessageBox.critical(self, '错误', f'无法删除文件: {e}')
            else:
                QMessageBox.warning(self, '警告', f'文件不存在: {project_path}')
        else:
            QMessageBox.information(self, '提示', '已取消删除操作')

    def updateShow(self):
        # 清空树形控件的所有内容
        self.treeWidget.clear()
        self.ui.status.showMessage("Tree content cleared")

    def rename(self, item):
        project_path = item.data(0, Qt.UserRole)
        item_style = item.data(0, Qt.UserRole + 1)
        name = item.text(0)
        parent = item.parent()
        text, ok = QInputDialog.getText(self, '重命名', '输入新名称:', text=name)
        text0 = text
        if ok and text:
            # 获取父目录路径
            parent_dir = parent.data(0, Qt.UserRole)
            # 给文件重命名
            if item_style == "具体工艺":
                text = f"{text}.json"
            elif item_style == "具体材料":
                text = f"{text}.xlsx"
            new_path = os.path.join(parent_dir, text)
            try:
                # 重命名文件/文件夹
                os.rename(project_path, new_path)
                # 更新 item 显示的名称
                item.setText(0, text0)
                # 更新 item 中存储的路径
                item.setData(0, Qt.UserRole, new_path)
                print(f"Successfully renamed {project_path} to {new_path}")
            except OSError as e:
                print(f"Error renaming {project_path} to {new_path}: {e}")
            # 修改文件记录中的名称信息
            if item_style == "具体材料":
                # 加载 Excel 文件
                workbook = load_workbook(new_path)
                sheet = workbook['名称-类型-成分']  # 或 workbook['SheetName']
                # 修改 A1 单元格的值
                sheet['A1'] = text0  # 替换为你想要输入的值
                workbook.save(new_path)  # 保存修改
            elif item_style == "具体程序":
                new_path = os.path.join(new_path, '程序描述.json')
                # 加载 JSON 文件
                with open(new_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                data["名称"] = text0  # 替换为你想要的新值
                with open(new_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
    def copy(self, item):
        parent = item.parent()
        target_path = parent.data(0, Qt.UserRole)
        project_path = item.data(0, Qt.UserRole)
        item_style = item.data(0, Qt.UserRole + 1)
        text, ok = QInputDialog.getText(self, '复制', '输入新名称:')
        text0 = text
        if ok and text:  # 如果用户确认并输入了名称
            # 计算目标目录路径
            if item_style == "具体工艺":
                text = f"{text}.json"
            elif item_style == "具体材料":
                text = f"{text}.xlsx"
            new_project_path = os.path.join(target_path, text)
            print(project_path)
            print(new_project_path)
            # 确保目标路径不存在
            if os.path.exists(new_project_path):
                QMessageBox.warning(self, '错误', f'目标 {new_project_path} 已存在，请选择其他名称。')
                return
            try:
                # 复制项目到新路径
                new_item = QTreeWidgetItem(parent)
                new_item.setText(0, text0)
                new_item.setData(0, Qt.UserRole, new_project_path)
                if item_style == "具体工艺":
                    shutil.copy(project_path, new_project_path)
                    # 设置窗口图标
                    icon_path = os.path.join('..', 'resource', 'icon', 'doc.png')
                    new_item.setIcon(0, QIcon(icon_path))
                    new_item.setData(0, Qt.UserRole + 1, "具体工艺")
                elif item_style == "具体材料":
                    shutil.copy(project_path, new_project_path)
                    # 设置窗口图标
                    icon_path = os.path.join('..', 'resource', 'icon', 'doc.png')
                    new_item.setIcon(0, QIcon(icon_path))
                    new_item.setData(0, Qt.UserRole + 1, "具体材料")
                else:
                    shutil.copytree(project_path, new_project_path)
                    # 设置窗口图标
                    icon_path = os.path.join('..', 'resource', 'icon', 'dir.png')
                    new_item.setIcon(0, QIcon(icon_path))
                    new_item.setData(0, Qt.UserRole + 1, item_style)
                QMessageBox.information(self, '成功', f'项目已成功复制到 {new_project_path}')
            except Exception as e:
                QMessageBox.critical(self, '错误', f'复制过程中发生错误: {e}')

    def unfolder(self, item):
        # 展开当前项
        item.setExpanded(True)

        # 遍历所有子项并递归展开
        for index in range(item.childCount()):
            child_item = item.child(index)
            self.unfolder(child_item)  # 递归调用

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = PWindow()
    MainWindow.show()
    sys.exit(app.exec_())
