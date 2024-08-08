#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 16:01
# @Author  : mihudan~
# @File    : dropout_reflect.py
# @Description :
# 国外的qt的点云嵌入式显示点云模块

# First, and before importing any Enthought packages, set the ETS_TOOLKIT
# environment variable to qt4, to tell Traits that we will use Qt.
import os
# os.environ['ETS_TOOLKIT'] = 'qt5'
# By default, the PySide binding will be used. If you want the PyQt bindings
# to be used, you need to set the QT_API environment variable to 'pyqt'
# os.environ['QT_API'] = 'pyqt5'

# To be able to use PySide or PyQt4 and not run in conflicts with traits,
# we need to import QWidget and QtCore from pyface.qt
from PySide2.QtWidgets import QWidget
from PySide2 import QtWidgets
# Alternatively, you can bypass this line, but you need to make sure that
# the following lines are executed before the import of PyQT:
from PySide2.QtCore import *
from PySide2.QtGui import *
import numpy as np
from traits.api import HasTraits, Instance, on_trait_change
from traitsui.api import View, Item
from mayavi.core.ui.api import MayaviScene, MlabSceneModel, \
    SceneEditor


# create direct grid as 256**3 x 4 array
def create_8bit_rgb_lut():
    """创建rgb查找表"""
    xl = np.mgrid[0:256, 0:256, 0:256]
    lut = np.vstack((xl[0].reshape(1, 256 ** 3),
                     xl[1].reshape(1, 256 ** 3),
                     xl[2].reshape(1, 256 ** 3),
                     255 * np.ones((1, 256 ** 3)))).T
    return lut.astype('int32')


# indexing function to above grid
def rgb_2_scalar_idx(r, g, b):
    """rgb转color的idx"""
    return 256 ** 2 * r + 256 * g + b


################################################################################
# The actual visualization
class Visualization(HasTraits):
    scene = Instance(MlabSceneModel, ())

    @on_trait_change('scene.activated')
    def update_plot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.
        # We can do normal mlab calls on the embedded scene.
        self.scene.mlab.test_points3d()
        return

    # the layout of the dialog screated
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=600, width=600, show_label=False),
                resizable=True  # We need this to resize with the parent widget
                )


################################################################################
# The QWidget containing the visualization, this is pure PyQt4 code.
class MayaviQWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.visualization = Visualization()

        # If you want to debug, beware that you need to remove the Qt
        # input hook.
        # QtCore.pyqtRemoveInputHook()
        # import pdb ; pdb.set_trace()
        # QtCore.pyqtRestoreInputHook()

        # The edit_traits call will generate the widget to embed.
        self.ui = self.visualization.edit_traits(parent=self,
                                                 kind='subpanel').control

        layout.addWidget(self.ui)
        self.ui.setParent(self)

        self.visualization.scene.mlab.clf()

        # 1.小球场景初始化建立
        # 用mlab.points3d建立红色和白色小球的集合
        x1, y1, z1 = np.random.random((3, 10))  # 3行10列分给三个元素，每个都是以为数组含10元素
        self.show_pts_with_pick(x1, y1, z1)

    def show_pts_with_pick(self, x1, y1, z1):
        figure = self.visualization.scene.mlab.gcf()  # 获取当前窗口指针

        figure.scene.disable_render = True
        red_glyphs = self.visualization.scene.mlab.points3d(x1, y1, z1, color=(1, 0, 0), resolution=10)  # 创建10个红球，位置为x1,y1,z1，分辨率为10的小球
        # 2.选取框初始化建立
        outline = self.visualization.scene.mlab.outline(line_width=3)
        outline.outline_mode = "cornered"
        outline.bounds = (x1[0] - 0.1, x1[0] + 0.1,
                          y1[0] - 0.1, y1[0] + 0.1,
                          z1[0] - 0.1, z1[0] + 0.1,
                          )

        figure.scene.disable_render = False

        # 获取一个红色小球的所有顶点,我们只是想要知道每个小球的顶点数目而已，所以不用考虑其他
        glyph_points = red_glyphs.glyph.glyph_source.glyph_source.output.points.to_array()

        # 3.选取回调函数的结构
        def piker_callback(picker):  # 当鼠标点击会返回一个vtk picker对象，我们将对该对象进行处理判断
            if picker.actor in red_glyphs.actor.actors:
                # 确定该小球的ID，
                point_id = int(picker.point_id / glyph_points.shape[0])  # picker.point_id是picker对象选取的顶点ID，glyph_points.shape[0]记录了82这个值，通过这个计算出小球的ID
                if point_id != -1:  # 表示有红色小球被选取了
                    # 计算与此红色小球相关的坐标
                    x, y, z = x1[point_id], y1[point_id], z1[point_id]
                    # 将外框移动到小球上
                    outline.bounds = (
                        x - 0.1, x + 0.1,
                        y - 0.1, y + 0.1,
                        z - 0.1, z + 0.1,
                    )
                    print(x, y, z)

        picker = figure.on_mouse_pick(piker_callback)
        picker.tolerance = 0.01  # 设置tolerance参数提高精确度

        self.visualization.scene.mlab.title("Click on red balls")  # 设置窗口的标题文字


if __name__ == "__main__":
    # Don't create a new QApplication, it would unhook the Events
    # set by Traits on the existing QApplication. Simply use the
    # '.instance()' method to retrieve the existing one.
    app = QtWidgets.QApplication.instance()
    container = QWidget()
    container.setWindowTitle("Embedding Mayavi in a PyQt4 Application")
    # define a "complex" layout to test the behaviour
    layout = QtWidgets.QGridLayout(container)

    # put some stuff around mayavi
    mayavi_widget = MayaviQWidget(container)

    layout.addWidget(mayavi_widget, 1, 1)
    container.show()
    window = QtWidgets.QMainWindow()
    window.setCentralWidget(container)
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.show()

    # Start the main event loop.
    app.exec_()
