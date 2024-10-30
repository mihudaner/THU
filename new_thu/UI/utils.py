from main_viewer_ui import Ui_MainWindow
from PySide2.QtWidgets import *
from enum import Enum, unique
from functools import partial
import subprocess
from pathlib import Path
from MyDialog import *
from PySide2.QtGui import QIcon

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
        text, ok = QInputDialog.getText(self, '新建模型工艺类型', '输入工艺类型名称:')
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
    elif item and item.data(0, Qt.UserRole + 1) == "项目库":
        text, ok = QInputDialog.getText(self, '新建项目', '输入项目名称:')
        if ok and text:
            file_path = osp.join(absolute_path, text)
            # 检查 file_path 是否已经存在
            if os.path.exists(file_path):
                QMessageBox.warning(self, '警告', f'项目 "{text}" 已经存在!', QMessageBox.Ok)
            else:
                new_item = QTreeWidgetItem(item)
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
                jk_list = ["尺寸计算", "熔池监控", "实时反馈", "温度监控", "形貌监控"]
                jk_path = osp.join(file_path, "熔覆监控")
                for type in jk_list:
                    new_file = osp.join(jk_path, type)
                    os.makedirs(new_file, exist_ok=True)
                yc_list = ["LBM", "PINN", "热力耦合", "熔池多相流"]
                yc_path = osp.join(file_path, "分析预测")
                for type in yc_list:
                    new_file = osp.join(yc_path, type)
                    os.makedirs(new_file, exist_ok=True)
                item.addChild(new_item)
    elif item and item.data(0, Qt.UserRole + 1) == "工艺库":
        text, ok = QInputDialog.getText(self, '新建工艺', '输入工艺类型名称:')
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
        text, ok = QInputDialog.getText(self, '新建工艺', '输入工艺名称:')
        if ok and text:
            new_item = QTreeWidgetItem(item)
            new_item.setText(0, text)
            new_item.setData(0, Qt.UserRole, osp.join(absolute_path, f"{text}.json"))
            new_item.setData(0, Qt.UserRole + 1, "具体工艺")
            # 设置窗口图标
            icon_path = os.path.join('..', 'resource', 'icon', 'doc.png')
            new_item.setIcon(0, QIcon(icon_path))
            item.addChild(new_item)
            item.setExpanded(True)  # 展开项目以显示新添加的内容
            # 定义要创建的文件路径
            file_path = osp.join(absolute_path, f"{text}.json")
            if item.text(0) == "送粉":
                data = {
                    "熔覆材料": "",
                    "基板材料": "",
                    "粉末粒径(μm)": 0,
                    "基板尺寸(mm)": 0,
                    "激光功率(W)": 0,
                    "熔覆速度(mm/s)": 0,
                    "送粉转速(r/min)": 0,
                    "质量添加(g/min)": 0,
                    "光斑电压(V)": 0,
                    "光斑直径(mm)": 0,
                    "道间间隔(s)": 0,
                    "层间间隔(s)": 0,
                    "道间偏移(mm)": 0,
                    "层间抬升(mm)": 0,
                    "保护气及流量(L/min)": 0,
                    "载气及流量(L/min)": 0
                }
            else:
                data = {
                    "熔覆材料": "",
                    "基板材料": "",
                    "丝材直径(mm)": 0,
                    "基板尺寸(mm)": 0,
                    "激光功率(W)": 0,
                    "熔覆速度(mm/s)": 0,
                    "送丝速度(m/min)": 0,
                    "质量添加(g/min)": 0,
                    "道间偏移(mm)": 0,
                    "层间抬升(mm)": 0,
                    "保护气及流量(L/min)": 0,
                    "气刀流量(L/min)": 0,
                    "加工前保护气时长(s)": 0,
                    "保护气保持时间(s)": 0
                }
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
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
        dialog = ProgramDialog(self, item)
        dialog.exec_()
    elif item and item.data(0, Qt.UserRole + 1) == "模型类型":
        dialog = ModelDialog(self, item)
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
        unfolder = menu.addAction("展开/收起")
        open_action.triggered.connect(lambda: self.open_type_library(item))
        unfolder.triggered.connect(lambda: self.unfolder(item))
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
        choose = menu.addAction("选择")
        rename_action = menu.addAction("重命名")
        copy_action = menu.addAction("复制")
        del_action = menu.addAction("删除")
        choose.triggered.connect(lambda: choose_project(self, item))
        copy_action.triggered.connect(lambda: self.copy(item))
        rename_action.triggered.connect(lambda: self.rename(item))
        del_action.triggered.connect(lambda: self.delete(item))
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))

def choose_project(self, item):
    project_name = item.text(0)
    self.treeWidget.clear()
    self.choosed_project = osp.join(self.projectroot, project_name)
    top_item = self.create_top_item(self.choosed_project, "所选项目")  # 创建topitem
    top_item.setExpanded(True)  # 固定展开 top_item
    self.list_project_dir(top_item, self.choosed_project)  # 递归遍历