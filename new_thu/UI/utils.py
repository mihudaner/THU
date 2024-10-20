from main_viewer_ui import Ui_MainWindow
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from enum import Enum, unique
from functools import partial
import subprocess
from pathlib import Path
from MyDialog import *
from PySide2.QtGui import QIcon
from openpyxl import Workbook

@unique
class NodeType(Enum):
    """节点类型，文件还是文件夹"""
    NodeDir = 0
    NodeFile = 1
# 实现新建功能的槽函数
def new_type(self, item):
    #待探究Qt.UserRole和路径的关系
    project_path = item.data(0, Qt.UserRole)
    print(project_path)
    # 将相对路径转换为绝对路径
    absolute_path = os.path.abspath(project_path)
    print(absolute_path)
    if item and item.data(0, Qt.UserRole + 1) == "材料库":
        text, ok = QInputDialog.getText(self, '新建材料类型', '输入材料类型名称:')
        if ok and text:
            new_item = QTreeWidgetItem(item)
            new_item.setText(0, text)
            new_item.setData(0, Qt.UserRole, osp.join(absolute_path, text))
            # 设置窗口图标
            icon_path = os.path.join('..', 'resource', 'icon', 'dir.png')
            if os.path.exists(icon_path):
                new_item.setIcon(0, QIcon(icon_path))
            else:
                print(f"Icon file not found: {icon_path}")
            new_item.setData(0, Qt.UserRole + 1, "材料类型")
            item.addChild(new_item)
            item.setExpanded(True)  # 展开项目以显示新添加的内容
            # 定义要创建的目录路径
            dir_path = osp.join(absolute_path, text)
            path_obj = Path(dir_path)
            # 使用 Path.mkdir 创建目录，parents=True 表示递归创建，exist_ok=True 表示如果目录已存在，不会引发异常
            path_obj.mkdir(parents=True, exist_ok=True)

    elif item and item.data(0, Qt.UserRole + 1) == "设备库":
        text, ok = QInputDialog.getText(self, '新建设备类型', '输入设备类型名称:')
        if ok and text:
            new_item = QTreeWidgetItem(item)
            new_item.setText(0, text)
            new_item.setData(0, Qt.UserRole, osp.join(absolute_path, text))
            # 设置窗口图标
            icon_path = os.path.join('..', 'resource', 'icon', 'dir.png')
            if os.path.exists(icon_path):
                new_item.setIcon(0, QIcon(icon_path))
            else:
                print(f"Icon file not found: {icon_path}")
            new_item.setData(0, Qt.UserRole + 1, "设备类型")
            item.addChild(new_item)
            item.setExpanded(True)  # 展开项目以显示新添加的内容
            dir_path = osp.join(absolute_path, text)
            path_obj = Path(dir_path)
            path_obj.mkdir(parents=True, exist_ok=True)
    elif item and item.data(0, Qt.UserRole + 1) == "程序库":
        text, ok = QInputDialog.getText(self, '新建程序类型', '输入程序类型名称:')
        if ok and text:
            new_item = QTreeWidgetItem(item)
            new_item.setText(0, text)
            new_item.setData(0, Qt.UserRole, osp.join(absolute_path, text))
            # 设置窗口图标
            icon_path = os.path.join('..', 'resource', 'icon', 'dir.png')
            if os.path.exists(icon_path):
                new_item.setIcon(0, QIcon(icon_path))
            else:
                print(f"Icon file not found: {icon_path}")
            new_item.setData(0, Qt.UserRole + 1, "程序类型")
            item.addChild(new_item)
            item.setExpanded(True)  # 展开项目以显示新添加的内容
            dir_path = osp.join(absolute_path, text)
            path_obj = Path(dir_path)
            path_obj.mkdir(parents=True, exist_ok=True)
    elif item and item.data(0, Qt.UserRole + 1) == "模型库":
        text, ok = QInputDialog.getText(self, '新建模型类型', '输入模型类型名称:')
        if ok and text:
            new_item = QTreeWidgetItem(item)
            new_item.setText(0, text)
            new_item.setData(0, Qt.UserRole, osp.join(absolute_path, text))
            # 设置窗口图标
            icon_path = os.path.join('..', 'resource', 'icon', 'dir.png')
            if os.path.exists(icon_path):
                new_item.setIcon(0, QIcon(icon_path))
            else:
                print(f"Icon file not found: {icon_path}")
            new_item.setData(0, Qt.UserRole + 1, "模型类型")
            item.addChild(new_item)
            item.setExpanded(True)  # 展开项目以显示新添加的内容
            dir_path = osp.join(absolute_path, text)
            path_obj = Path(dir_path)
            path_obj.mkdir(parents=True, exist_ok=True)
    elif item and item.data(0, Qt.UserRole + 1) == "工艺库":
        text, ok = QInputDialog.getText(self, '新建工艺', '输入工艺名称:')
        if ok and text:
            new_item = QTreeWidgetItem(item)
            new_item.setText(0, text)
            new_item.setData(0, Qt.UserRole, osp.join(absolute_path, f"{text}.xlsx"))
            new_item.setData(0, Qt.UserRole + 1, "具体工艺")
            # 设置窗口图标
            icon_path = os.path.join('..', 'resource', 'icon', 'doc.png')
            new_item.setIcon(0, QIcon(icon_path))
            item.addChild(new_item)
            item.setExpanded(True)  # 展开项目以显示新添加的内容
            # 定义要创建的文件路径
            file_path = osp.join(absolute_path, f"{text}.xlsx")
            # 创建一个 Workbook 对象
            workbook = Workbook()
            # 保存到指定路径
            workbook.save(file_path)
            print(f"Excel 文件已创建: {file_path}")
    elif item and item.data(0, Qt.UserRole + 1) == "材料类型":
        dialog = MaterialDialog(item)
        dialog.exec_()

    elif item and item.data(0, Qt.UserRole + 1) == "设备类型":
        text, ok = QInputDialog.getText(self, '新建设备', '输入设备名称:')
        if ok and text:
            new_item = QTreeWidgetItem(item)
            new_item.setText(0, text)
            new_item.setData(0, Qt.UserRole, osp.join(absolute_path, text))
            # 设置窗口图标
            icon_path = os.path.join('..', 'resource', 'icon', 'dir.png')
            if os.path.exists(icon_path):
                new_item.setIcon(0, QIcon(icon_path))
            else:
                print(f"Icon file not found: {icon_path}")
            new_item.setData(0, Qt.UserRole + 1, "具体设备")
            item.addChild(new_item)
            item.setExpanded(True)  # 展开项目以显示新添加的内容
            dir_path = osp.join(absolute_path, text)
            path_obj = Path(dir_path)
            path_obj.mkdir(parents=True, exist_ok=True)
            #新建图片和文件dir
            miaoshu = osp.join(dir_path, text)
            miaoshu = f'{miaoshu}.txt'
            tu_dir = osp.join(dir_path, '设备图片')
            wen_dir = osp.join(dir_path, '设备文件')
            try:
                # 创建设备图片和设备文件的文件夹
                os.makedirs(tu_dir, exist_ok=True)  # exist_ok=True表示如果文件夹已存在，不会抛出异常
                os.makedirs(wen_dir, exist_ok=True)
                # 创建一个空的文本文件
                with open(miaoshu, 'w', encoding='utf-8') as file:
                    file.write('')  # 可以在文件中写入一些初始内容，如果需要的话
            except Exception as e:
                print(f'创建文件夹或文件时出错: {e}')
            for obj in os.listdir(new_item.data(0, Qt.UserRole)):
                tmp_path = osp.join(new_item.data(0, Qt.UserRole), obj)
                if osp.isdir(tmp_path):
                    dir_item = self._generate_item(new_item, obj, tmp_path, NodeType.NodeDir.value)
                    self.list_dir(dir_item, tmp_path)
                else:
                    self._generate_item(new_item, obj, tmp_path, NodeType.NodeFile.value)

    elif item and item.data(0, Qt.UserRole + 1) == "具体设备":
        dialog2 = EquipmentDialog(item)
        dialog2.exec_()
    elif item and item.data(0, Qt.UserRole + 1) == "程序类型":
        dialog = EditProgramDialog(item)
        dialog.exec_()
    elif item and item.data(0, Qt.UserRole + 1) == "模型类型":
        dialog = EditModelDialog(item)
        dialog.exec_()

# 右键菜单功能
def show_context_menu(self, position):
    # 获取被点击的项目
    item = self.treeWidget.itemAt(position)
    print(item.data(0, Qt.UserRole + 1))
    if item.data(0, Qt.UserRole + 1) == "材料库":
        menu = QMenu()
        unfolder = menu.addAction("展开全部")
        open_action = menu.addAction("打开材料库")
        refresh_action = menu.addAction("刷新材料库")
        new_type_action = menu.addAction("新建材料类型")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        refresh_action.triggered.connect(partial(self.select_data, note="cl_fresh"))
        new_type_action.triggered.connect(lambda: new_type(self, item))
        unfolder.triggered.connect(lambda: self.unfolder(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item.data(0, Qt.UserRole + 1) == "设备库":
        menu = QMenu()
        unfolder = menu.addAction("展开全部")
        open_action = menu.addAction("打开设备库")
        refresh_action = menu.addAction("刷新设备库")
        new_type_action = menu.addAction("新建设备类型")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        refresh_action.triggered.connect(partial(self.select_data, note="sb_fresh"))
        new_type_action.triggered.connect(lambda: new_type(self, item))
        unfolder.triggered.connect(lambda: self.unfolder(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "工艺库":
        menu = QMenu()
        open_action = menu.addAction("打开工艺库")
        refresh_action = menu.addAction("刷新工艺库")
        new_type_action = menu.addAction("新建工艺")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        refresh_action.triggered.connect(partial(self.select_data, note="gy_fresh"))
        new_type_action.triggered.connect(lambda: new_type(self, item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "程序库":
        menu = QMenu()
        unfolder = menu.addAction("展开全部")
        open_action = menu.addAction("打开程序库")
        new_type_action = menu.addAction("新建程序类型")
        filter_action = menu.addAction("筛选程序")
        unfolder.triggered.connect(lambda: self.unfolder(item))
        open_action.triggered.connect(lambda: self.open_type_library(item))
        new_type_action.triggered.connect(lambda: new_type(self, item))
        filter_action.triggered.connect(lambda: self.filter(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "模型库":
        menu = QMenu()
        unfolder = menu.addAction("展开全部")
        open_action = menu.addAction("打开模型库")
        new_type_action = menu.addAction("新建模型类型")
        filter_action = menu.addAction("筛选模型")
        unfolder.triggered.connect(lambda: self.unfolder(item))
        open_action.triggered.connect(lambda: self.open_type_library(item))
        new_type_action.triggered.connect(lambda: new_type(self, item))
        filter_action.triggered.connect(lambda: self.filter(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "材料类型":
        menu = QMenu()
        open_action = menu.addAction("打开")
        rename_action = menu.addAction("重命名")
        new_file_action = menu.addAction("新建材料")
        del_action = menu.addAction("删除")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        rename_action.triggered.connect(partial(self.select_data, note="gy_fresh"))
        new_file_action.triggered.connect(lambda: new_type(self, item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item.data(0, Qt.UserRole + 1) == "设备类型":
        menu = QMenu()
        open_action = menu.addAction("打开")
        rename_action = menu.addAction("重命名")
        new_file_action = menu.addAction("新建设备")
        del_action = menu.addAction("删除")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        rename_action.triggered.connect(partial(self.select_data, note="sb_fresh"))
        new_file_action.triggered.connect(lambda: new_type(self, item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item.data(0, Qt.UserRole + 1) == "程序类型":
        menu = QMenu()
        open_action = menu.addAction("打开")
        rename_action = menu.addAction("重命名")
        new_file_action = menu.addAction("新建程序")
        del_action = menu.addAction("删除")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        rename_action.triggered.connect(partial(self.select_data, note="cx_fresh"))
        new_file_action.triggered.connect(lambda: new_type(self, item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item.data(0, Qt.UserRole + 1) == "程序目录":
        menu = QMenu()
        open_action = menu.addAction("打开")
        del_action = menu.addAction("刷新")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item.data(0, Qt.UserRole + 1) == "模型类型":
        menu = QMenu()
        open_action = menu.addAction("打开")
        rename_action = menu.addAction("重命名")
        new_file_action = menu.addAction("新建模型")
        del_action = menu.addAction("删除")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        rename_action.triggered.connect(partial(self.select_data, note="mx_fresh"))
        new_file_action.triggered.connect(lambda: new_type(self, item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "具体工艺":
        menu = QMenu()
        edit_action = menu.addAction("编辑")
        rename_action = menu.addAction("重命名")
        copy_action = menu.addAction("复制")
        del_file_action = menu.addAction("删除")
        edit_action.triggered.connect(lambda: self.edit(item))
        rename_action.triggered.connect(partial(self.select_data, note="sb_fresh"))
        copy_action.triggered.connect(lambda: self.open_type_library(item))
        del_file_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "具体材料":
        print("具体材料")
        menu = QMenu()
        edit_action = menu.addAction("编辑")
        copy_action = menu.addAction("复制")
        rename_action = menu.addAction("重命名")
        del_action = menu.addAction("删除")
        edit_action.triggered.connect(lambda: self.edit(item))
        copy_action.triggered.connect(partial(self.select_data, note="sb_fresh"))
        rename_action.triggered.connect(lambda: new_type(self, item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "具体设备":
        print("具体设备")
        menu = QMenu()
        edit_action = menu.addAction("编辑")
        copy_action = menu.addAction("复制")
        rename_action = menu.addAction("重命名")
        del_action = menu.addAction("删除")
        edit_action.triggered.connect(lambda: self.edit(item))
        copy_action.triggered.connect(partial(self.select_data, note="sb_fresh"))
        rename_action.triggered.connect(lambda: new_type(self, item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
