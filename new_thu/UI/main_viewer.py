import json

from main_viewer_ui import Ui_MainWindow
from PySide2.QtWidgets import *
from enum import Enum, unique
from functools import partial
import subprocess
from pathlib import Path
from MyDialog import *
from PySide2.QtGui import QIcon
from openpyxl import Workbook
from utils import *
@unique
class NodeType(Enum):
    """节点类型，文件还是文件夹"""
    NodeDir = 0
    NodeFile = 1
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Main Window')

        # 设置窗口图标
        icon_path = os.path.join('..', 'resource', 'icon', 'PyDracula.png')

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")
        self.initUI()  # 初始化窗口

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #文件
        self.ui.w_quit.triggered.connect(QApplication.quit)
        self.ui.w_path.triggered.connect(self.select_database)

        self.model = QFileSystemModel()
        self.treeWidget = self.ui.treeWidget
        self.root = "../database"
        self.dataroot = osp.join(self.root, "数据库")
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

        # Enable custom context menu
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 右击显示菜单
        self.treeWidget.customContextMenuRequested.connect(partial(show_context_menu, self))

        self.initTable()
    def initTable(self):
        cx = osp.join(self.dataroot, "程序库/程序目录.json")
        mx = osp.join(self.dataroot, "模型库/模型目录.json")
        with open(cx, 'r', encoding='utf-8') as file:
            data = json.load(file)
        # 设置表格行数和列数
        self.ui.table_cx.setRowCount(len(data))
        self.ui.table_cx.setColumnCount(len(data[0]))  # 假设每个字典都有相同的键
        # 设置表头
        self.ui.table_cx.setHorizontalHeaderLabels(data[0].keys())
        # 填充数据
        for row_index, row_data in enumerate(data):
            for col_index, (key, value) in enumerate(row_data.items()):
                self.ui.table_cx.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        with open(mx, 'r', encoding='utf-8') as file:
            data = json.load(file)
        # 设置表格行数和列数
        self.ui.table_mx.setRowCount(len(data))
        self.ui.table_mx.setColumnCount(len(data[0]))  # 假设每个字典都有相同的键
        # 设置表头
        self.ui.table_mx.setHorizontalHeaderLabels(data[0].keys())
        # 填充数据
        for row_index, row_data in enumerate(data):
            for col_index, (key, value) in enumerate(row_data.items()):
                self.ui.table_mx.setItem(row_index, col_index, QTableWidgetItem(str(value)))

    def filter(self, item):
        if item.text(0)=='程序库':
            dialog = FilterCX(item)
        elif item.text(0)=='模型库':
            dialog = FilterMX(item)
        else:
            dialog = FilterMX(item)
        dialog.exec_()

    def updateTable(self):
        cx = osp.join(self.dataroot, "程序库/程序目录.json")
        mx = osp.join(self.dataroot, "模型库/模型目录.json")
        with open(cx, 'r', encoding='utf-8') as file:
            data = json.load(file)
        # 设置表格行数和列数
        self.ui.table_cx.setRowCount(len(data))
        self.ui.table_cx.setColumnCount(len(data[0]))  # 假设每个字典都有相同的键
        # 设置表头
        self.ui.table_cx.setHorizontalHeaderLabels(data[0].keys())
        # 填充数据
        for row_index, row_data in enumerate(data):
            for col_index, (key, value) in enumerate(row_data.items()):
                self.ui.table_cx.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        with open(mx, 'r', encoding='utf-8') as file:
            data = json.load(file)
        # 设置表格行数和列数
        self.ui.table_mx.setRowCount(len(data))
        self.ui.table_mx.setColumnCount(len(data[0]))  # 假设每个字典都有相同的键
        # 设置表头
        self.ui.table_mx.setHorizontalHeaderLabels(data[0].keys())
        # 填充数据
        for row_index, row_data in enumerate(data):
            for col_index, (key, value) in enumerate(row_data.items()):
                self.ui.table_mx.setItem(row_index, col_index, QTableWidgetItem(str(value)))


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
        else:
            return

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


        else:
            for obj in os.listdir(directory):
                tmp_path = osp.join(directory, obj)
                if osp.isdir(tmp_path):
                    dir_item = self._generate_item(parent, obj, tmp_path, NodeType.NodeDir.value)
                    self.list_dir(dir_item, tmp_path)
                else:
                    self._generate_item(parent, obj, tmp_path, NodeType.NodeFile.value)

    def _generate_item(self, parent, name, path, node_type):
        item = QTreeWidgetItem(parent)
        if name.endswith('bak'):
            item.setHidden(True)
        if name.endswith('xlsx') or name.endswith('json'):
            name = name.rstrip('.xlsx')
            name = name.rstrip('.json')

        item.setText(0, name)
        item.setToolTip(0, path)
        item.setData(0, Qt.UserRole, path)

        if item.parent() is None: # 父节点为database
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

        else:
            if item.parent().text(0)=="材料库":
                item.setData(0, Qt.UserRole+1, "材料类型")
            elif item.parent().text(0)=="设备库":
                item.setData(0, Qt.UserRole+1, "设备类型")
                item.setExpanded(True)
            elif item.parent().text(0)=="程序库":
                item.setData(0, Qt.UserRole+1, "程序类型")
                item.setExpanded(True)
                if "目录" in item.text(0):
                    item.setData(0, Qt.UserRole + 1, "程序目录")
            elif item.parent().text(0)=="模型库":
                item.setData(0, Qt.UserRole+1, "模型类型")
                item.setExpanded(True)
            elif item.parent().text(0)=="工艺库":
                item.setData(0, Qt.UserRole+1, "具体工艺")
            elif item.parent().data(0, Qt.UserRole + 1) == "材料类型":
                item.setData(0, Qt.UserRole + 1, "具体材料")
            elif item.parent().data(0, Qt.UserRole + 1) == "设备类型":
                item.setData(0, Qt.UserRole + 1, "具体设备")
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
        project_path = item.data(0, Qt.UserRole)
        if osp.isdir(project_path):
            self.open_type_library(item)
        elif item.data(0, Qt.UserRole + 1) == "具体材料":
            self.edit(item)
        elif item.data(0, Qt.UserRole + 1) == "具体工艺":
            self.edit(item)

    #编辑
    def edit(self, item):
        project_path = item.data(0, Qt.UserRole)
        print(project_path)
        if item.data(0, Qt.UserRole + 1) == "具体材料":
            dialog = MaterialDialog(item, project_path, note="edit")
            dialog.exec_()
        elif item.data(0, Qt.UserRole + 1) == "具体工艺":
            dialog = ProcessDialog(item)
            dialog.exec_()
        elif item.data(0, Qt.UserRole + 1) == "具体设备":
            dialog = EquipmentDialog(item)
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

    def delete(self,item):
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
                        QMessageBox.information(self, '提示', f'文件夹已删除: {project_path}')
                    else:
                        os.remove(project_path)  # 删除文件
                        QMessageBox.information(self, '提示', f'文件已删除: {project_path}')
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
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
