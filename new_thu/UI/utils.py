from pathlib import Path

from main_viewer_ui import Ui_MainWindow
from PySide2.QtWidgets import *
from enum import Enum, unique
from functools import partial
from XM_dialogs import *
from MyDialog import *
from PySide2.QtGui import QIcon
import json
import subprocess
from dialog2 import *

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
        # 调用输入对话框，获取用户输入
        text, ok = CustomInputDialog.getText(None, '新建材料类型', '输入材料类型名称:')
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
        text, ok = CustomInputDialog.getText(None, '新建设备类型', '输入设备类型名称:')
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
        text, ok = CustomInputDialog.getText(None, '新建程序类型', '输入程序类型名称:')
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
        text, ok = CustomInputDialog.getText(None, '新建模型工艺类型', '输入工艺类型名称:')
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
            new_item.setData(0, Qt.UserRole + 1, "模型工艺类型")
            item.addChild(new_item)
            item.setExpanded(True)  # 展开项目以显示新添加的内容
            dir_path = osp.join(absolute_path, text)
            path_obj = Path(dir_path)
            path_obj.mkdir(parents=True, exist_ok=True)
    elif item and item.data(0, Qt.UserRole + 1) == "模型工艺类型":
        text, ok = CustomInputDialog.getText(None, '新建模型类型', '输入模型类型名称:')
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
    elif item and item.data(0, Qt.UserRole + 1) == "项目库":
        text, ok = CustomInputDialog.getText(None, '新建项目', '输入项目名称:')
        if ok and text:
            file_path = osp.join(absolute_path, text)
            # 检查 file_path 是否已经存在
            if os.path.exists(file_path):
                QMessageBox.warning(self, '警告', f'项目 "{text}" 已经存在!', QMessageBox.Ok)
            else:
                new_item = QTreeWidgetItem()
                new_item.setText(0, text)
                new_item.setData(0, Qt.UserRole, file_path)
                # 设置窗口图标
                icon_path = os.path.join('..', 'resource', 'icon', 'dir.png')
                if os.path.exists(icon_path):
                    new_item.setIcon(0, QIcon(icon_path))
                else:
                    print(f"Icon file not found: {icon_path}")

                new_item.setData(0, Qt.UserRole + 1, "具体项目")
                os.makedirs(file_path, exist_ok=True)
                project_list = ["类型及设备", "材料及工艺", "项目程序", "熔覆监控", "分析预测"]
                for type in project_list:
                    new_file = osp.join(file_path, type)
                    os.makedirs(new_file, exist_ok=True)
                jk_list = ["熔池温度", "熔池状态", "实时反馈", "熔池流动", "熔池尺寸", "熔覆形貌"]
                jk_path = osp.join(file_path, "熔覆监控")
                for type in jk_list:
                    new_file = osp.join(jk_path, type)
                    os.makedirs(new_file, exist_ok=True)
                yc_list = ["LBM", "PINN", "热力耦合", "熔池多相流"]
                yc_path = osp.join(file_path, "分析预测")
                for type in yc_list:
                    new_file = osp.join(yc_path, type)
                    os.makedirs(new_file, exist_ok=True)
                # item.addChild(new_item)
                # 重新生成子项
                while item.childCount() > 0:
                    item.removeChild(item.child(0))
                for obj in os.listdir(item.data(0, Qt.UserRole)):
                    tmp_path = osp.join(item.data(0, Qt.UserRole), obj)
                    if osp.isdir(tmp_path):
                        dir_item = self._generate_item(item, obj, tmp_path, NodeType.NodeDir.value)
                        self.list_dir(dir_item, tmp_path)  # 递归调用
                    else:
                        self._generate_item(item, obj, tmp_path, NodeType.NodeFile.value)
    elif item and item.data(0, Qt.UserRole + 1) == "工艺库":
        text, ok = CustomInputDialog.getText(None, '新建工艺', '输入工艺类型名称:')
        if ok and text:
            new_item = QTreeWidgetItem(item)
            new_item.setText(0, text)
            new_item.setData(0, Qt.UserRole, osp.join(absolute_path, text))
            new_item.setData(0, Qt.UserRole + 1, "工艺类型")
            # 设置窗口图标
            icon_path = os.path.join('..', 'resource', 'icon', 'dir.png')
            new_item.setIcon(0, QIcon(icon_path))
            item.addChild(new_item)
            item.setExpanded(True)  # 展开项目以显示新添加的内容
            # 定义要创建的文件路径
            file_path = osp.join(absolute_path, text)
            os.makedirs(file_path, exist_ok=True)
    elif item and item.data(0, Qt.UserRole + 1) == "工艺类型":
        if item.text(0) == "粉丝同送":
            dialog = ProcessDialog2(self, item)
        else:
            dialog = ProcessDialog(self, item)
        dialog.exec_()
    elif item and item.data(0, Qt.UserRole + 1) == "材料类型":
        dialog = MaterialDialog1(item)
        dialog.exec_()
    elif item and item.data(0, Qt.UserRole + 1) == "设备类型":
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
    elif item and item.data(0, Qt.UserRole + 1) == "程序类型":
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
    elif item and item.data(0, Qt.UserRole + 1) == "模型类型":
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
    elif item and item.data(0, Qt.UserRole + 1) == "材料类型":
        menu = QMenu()
        open_action = menu.addAction("打开")
        rename_action = menu.addAction("重命名")
        new_file_action = menu.addAction("新建材料")
        del_action = menu.addAction("删除")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        new_file_action.triggered.connect(lambda: new_type(self, item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "具体材料":
        print("具体材料")
        menu = QMenu()
        edit_action = menu.addAction("编辑")
        copy_action = menu.addAction("复制")
        rename_action = menu.addAction("重命名")
        del_action = menu.addAction("删除")
        edit_action.triggered.connect(lambda: self.edit(item))
        copy_action.triggered.connect(lambda: self.copy(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        del_action.triggered.connect(lambda: self.delete(item))
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
    elif item.data(0, Qt.UserRole + 1) == "设备类型":
        menu = QMenu()
        open_action = menu.addAction("打开")
        rename_action = menu.addAction("重命名")
        new_file_action = menu.addAction("新建设备")
        del_action = menu.addAction("删除")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        new_file_action.triggered.connect(lambda: new_type(self, item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "具体设备":
        menu = QMenu()
        edit_action = menu.addAction("编辑")
        copy_action = menu.addAction("复制")
        rename_action = menu.addAction("重命名")
        del_action = menu.addAction("删除")
        edit_action.triggered.connect(lambda: self.edit(item))
        copy_action.triggered.connect(lambda: self.copy(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "工艺库":
        menu = QMenu()
        unfolder = menu.addAction("展开全部")
        open_action = menu.addAction("打开工艺库")
        refresh_action = menu.addAction("刷新工艺库")
        new_type_action = menu.addAction("新建工艺类型")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        refresh_action.triggered.connect(partial(self.select_data, note="gy_fresh"))
        new_type_action.triggered.connect(lambda: new_type(self, item))
        unfolder.triggered.connect(lambda: self.unfolder(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "工艺类型":
        menu = QMenu()
        open_action = menu.addAction("打开")
        rename_action = menu.addAction("重命名")
        new_file_action = menu.addAction("新建工艺")
        del_action = menu.addAction("删除")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        new_file_action.triggered.connect(lambda: new_type(self, item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "具体工艺":
        menu = QMenu()
        edit_action = menu.addAction("编辑")
        copy_action = menu.addAction("复制")
        rename_action = menu.addAction("重命名")
        del_file_action = menu.addAction("删除")
        edit_action.triggered.connect(lambda: self.edit(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        copy_action.triggered.connect(lambda: self.copy(item))
        del_file_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "程序库":
        menu = QMenu()
        unfolder = menu.addAction("展开全部")
        open_action = menu.addAction("打开程序库")
        refresh_action = menu.addAction("刷新程序库")
        new_type_action = menu.addAction("新建程序类型")
        filter_action = menu.addAction("筛选程序")
        unfolder.triggered.connect(lambda: self.unfolder(item))
        open_action.triggered.connect(lambda: self.open_type_library(item))
        refresh_action.triggered.connect(partial(self.select_data, note="cx_fresh"))
        new_type_action.triggered.connect(lambda: new_type(self, item))
        filter_action.triggered.connect(lambda: self.filter(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item.data(0, Qt.UserRole + 1) == "程序类型":
        menu = QMenu()
        open_action = menu.addAction("打开")
        rename_action = menu.addAction("重命名")
        new_file_action = menu.addAction("新建程序")
        del_action = menu.addAction("删除")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        new_file_action.triggered.connect(lambda: new_type(self, item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "具体程序":
        menu = QMenu()
        edit_action = menu.addAction("编辑")
        copy_action = menu.addAction("复制")
        rename_action = menu.addAction("重命名")
        del_file_action = menu.addAction("删除")
        edit_action.triggered.connect(lambda: self.edit(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        copy_action.triggered.connect(lambda: self.copy(item))
        del_file_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "模型库":
        menu = QMenu()
        unfolder = menu.addAction("展开全部")
        open_action = menu.addAction("打开模型库")
        refresh_action = menu.addAction("刷新模型库")
        new_type_action = menu.addAction("新建工艺类型")
        filter_action = menu.addAction("筛选模型")
        unfolder.triggered.connect(lambda: self.unfolder(item))
        open_action.triggered.connect(lambda: self.open_type_library(item))
        refresh_action.triggered.connect(partial(self.select_data, note="mx_fresh"))
        new_type_action.triggered.connect(lambda: new_type(self, item))
        filter_action.triggered.connect(lambda: self.filter(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "模型工艺类型":
        menu = QMenu()
        open_action = menu.addAction("打开")
        rename_action = menu.addAction("重命名")
        new_type_action = menu.addAction("新建模型类型")
        delete = menu.addAction("删除")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        delete.triggered.connect(lambda: self.delete(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        new_type_action.triggered.connect(lambda: new_type(self, item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item.data(0, Qt.UserRole + 1) == "模型类型":
        menu = QMenu()
        open_action = menu.addAction("打开")
        rename_action = menu.addAction("重命名")
        new_file_action = menu.addAction("新建模型")
        delete = menu.addAction("删除")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        new_file_action.triggered.connect(lambda: new_type(self, item))
        delete.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item.data(0, Qt.UserRole + 1) == "具体模型":
        menu = QMenu()
        edit_action = menu.addAction("编辑")
        open_action = menu.addAction("打开")
        copy_action = menu.addAction("复制")
        rename_action = menu.addAction("重命名")
        del_action = menu.addAction("删除")
        edit_action.triggered.connect(lambda: self.edit(item))
        open_action.triggered.connect(lambda: self.open_type_library(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        copy_action.triggered.connect(lambda: self.copy(item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "项目库":
        print("项目库")
        menu = QMenu()
        open_action = menu.addAction("打开项目库")
        refresh = menu.addAction("刷新项目库")
        new_type_action = menu.addAction("新建项目")
        filter_action = menu.addAction("筛选项目")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        refresh.triggered.connect(partial(self.select_data, note="项目"))
        new_type_action.triggered.connect(lambda: new_type(self, item))
        filter_action.triggered.connect(lambda: self.filter(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "具体项目":
        print("具体项目")
        menu = QMenu()
        # choose = menu.addAction("选择")
        rename_action = menu.addAction("重命名")
        copy_action = menu.addAction("复制")
        del_action = menu.addAction("删除")
        unfolder = menu.addAction("展开")
        # choose.triggered.connect(lambda: choose_project(self, item))
        copy_action.triggered.connect(lambda: self.copy(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        del_action.triggered.connect(lambda: self.delete(item))
        unfolder.triggered.connect(lambda: self.unfolder(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item.data(0, Qt.UserRole + 1) == "项目包含项" and item.text(0) == "项目程序":
        menu = QMenu()
        # choose = menu.addAction("选择")
        xmimport_action = menu.addAction("项目导入")
        cxkimport_action = menu.addAction("程序库导入")
        new_type_action = menu.addAction("新建程序")
        open_action = menu.addAction("打开目录")
        trans_action = menu.addAction("传输程序")
        set_codepath1 = menu.addAction("OrangeEdit路径")
        set_codepath2 = menu.addAction("WorkVisual路径")

        # choose.triggered.connect(lambda: choose_project(self, item))
        xmimport_action.triggered.connect(lambda: xm_program_import(self, item))
        cxkimport_action.triggered.connect(lambda: cx_program_import(self, item))
        new_type_action.triggered.connect(lambda: run_exe(self.apppath[item.text(0) + "OrangeEdit"])) # pass
        open_action.triggered.connect(lambda: self.open_type_library(item))
        trans_action.triggered.connect(lambda: run_exe(self.apppath[item.text(0)+"WorkVisual"]))
        set_codepath1.triggered.connect(lambda: self.open_file_dialog(item.text(0)+"OrangeEdit"))
        set_codepath2.triggered.connect(lambda: self.open_file_dialog(item.text(0)+"WorkVisual"))

        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item.data(0, Qt.UserRole + 1) == "分析预测":
        menu = QMenu()
        xmimport_action = menu.addAction("项目导入")
        mxkimport_action = menu.addAction("模型库导入")
        open_action = menu.addAction("打开目录")
        del_action = menu.addAction("删除")
        xmimport_action.triggered.connect(lambda: xm_model_import(self, item))
        mxkimport_action.triggered.connect(lambda: mx_model_import(self, item))
        open_action.triggered.connect(lambda: self.open_type_library(item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))
    elif item and item.data(0, Qt.UserRole + 1) == "熔覆监控":
        menu = QMenu()
        setapppath = menu.addAction("设置路径")
        exeapppath = menu.addAction("运行应用")
        setapppath.triggered.connect(lambda: self.open_file_dialog(item.text(0)))
        exeapppath.triggered.connect(lambda: run_exe(self.apppath[item.text(0)]))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))


def choose_project(self, item):
    project_name = item.text(0)
    self.treeWidget.clear()
    self.choosed_project = osp.join(self.projectroot, project_name)
    top_item = self.create_top_item(self.choosed_project, "所选项目")  # 创建topitem
    top_item.setExpanded(True)  # 固定展开 top_item
    self.list_project_dir(top_item, self.choosed_project)  # 递归遍历

def xm_program_import(self, item):
    current_path = item.data(0, Qt.UserRole)
    dialog = ProjectFilterDialog(self, item.parent().parent())
    if dialog.exec_() == QDialog.Accepted:
        selected_text = dialog.get_selected_text()
        path = osp.join(self.projectroot, selected_text, "项目程序")
        if osp.exists(path):
            shutil.copytree(path, current_path, dirs_exist_ok=True)
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

def cx_program_import(self, item):
    current_path = item.data(0, Qt.UserRole)
    new_item = QTreeWidgetItem()
    new_item.setText(0, "程序库")
    new_item.setData(0, Qt.UserRole, osp.join(self.dataroot, "程序库"))
    new_item.setData(0, Qt.UserRole + 1, "程序库")
    dialog = FilterCX(self, new_item)
    if dialog.exec_() == QDialog.Accepted:
        selected_text = dialog.get_selected_text()
        path = osp.join(self.dataroot, "程序库", selected_text)
        if osp.exists(path):
            shutil.copytree(path, current_path, dirs_exist_ok=True)
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

def xm_model_import(self, item):
    current_path = item.data(0, Qt.UserRole)
    type = item.text(0)
    dialog = ProjectFilterDialog(self, item.parent().parent().parent())
    if dialog.exec_() == QDialog.Accepted:
        selected_text = dialog.get_selected_text()
        path = osp.join(self.projectroot, selected_text, "分析预测", type)
        if osp.exists(path):
            shutil.copytree(path, current_path, dirs_exist_ok=True)
    item = item.parent()
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

def mx_model_import(self, item):
    current_path = item.parent().data(0, Qt.UserRole)
    new_item = QTreeWidgetItem()
    new_item.setText(0, "模型库")
    new_item.setData(0, Qt.UserRole, osp.join(self.dataroot, "模型库"))
    new_item.setData(0, Qt.UserRole + 1, "模型库")
    dialog = FilterMX(self, new_item)
    if dialog.exec_() == QDialog.Accepted:
        selected_text = dialog.get_selected_text()
        name = selected_text[0]
        gy = selected_text[1]
        mx = selected_text[2]
        path = osp.join(self.dataroot, "模型库", gy, mx, name)
        if osp.exists(path):
            shutil.copytree(path, osp.join(current_path, mx), dirs_exist_ok=True)
    item = item.parent()
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
def load_apppath():

    # 要存储的配置数据
    config = {
        "path1": "/path/to/file1",
        "path2": "/path/to/file2",
        "path3": "/path/to/file3"
    }
    # 读取 JSON 文件
    with open('../resource/config.json', 'r') as json_file:
        loaded_config = json.load(json_file)

    print(loaded_config)
    return loaded_config

def save_apppath(config):
    # 写入 JSON 文件
    with open('../resource/config.json', 'w') as json_file:
        json.dump(config, json_file, indent=4)

def run_exe(exePath):
    # exePath = r"C:\Program Files (x86)\KUKA\WorkVisual 6.0\WorkVisual.exe"
    # # exePath = "D:\\soft\\XTranslator\\Xtranslator\\Xtranslator.exe"
    subprocess.Popen(exePath)
