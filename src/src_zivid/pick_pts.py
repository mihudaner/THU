# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2023/10/18 9:20
# # @Author  : mihudan~
# # @File    : pick_pts.py
# @Description :
import open3d as o3d
import numpy as np
from mayavi import mlab


def show_pick():

    figure = mlab.gcf() #获取当前窗口指针

    figure.scene.disable_render = True
    #1.小球场景初始化建立
    # 用mlab.points3d建立红色和白色小球的集合
    x1, y1, z1 = np.random.random((3,10))   #3行10列分给三个元素，每个都是以为数组含10元素
    red_glyphs = mlab.points3d(x1,y1,z1,color=(1,0,0),resolution=10)    #创建10个红球，位置为x1,y1,z1，分辨率为10的小球

    x2, y2, z2 = np.random.random((3,10))   #3行10列分给三个元素，每个都是以为数组含10元素
    white_glyphs = mlab.points3d(x2,y2,z2,color=(0.9,0.9,0.9),resolution=10)    #创建10个白球

    # 2.选取框初始化建立
    outline = mlab.outline(line_width=3)
    outline.outline_mode = "cornered"
    outline.bounds = (x1[0]-0.1,x1[0]+0.1,
                      y1[0]-0.1,y1[0]+0.1,
                      z1[0]-0.1,z1[0]+0.1,
                      )

    figure.scene.disable_render = False


    #获取一个红色小球的所有顶点,我们只是想要知道每个小球的顶点数目而已，所以不用考虑其他
    glyph_points = red_glyphs.glyph.glyph_source.glyph_source.output.points.to_array()

    #3.选取回调函数的结构
    def piker_callback(picker): #当鼠标点击会返回一个vtk picker对象，我们将对该对象进行处理判断
        if picker.actor in red_glyphs.actor.actors:
            # 确定该小球的ID，
            point_id = int(picker.point_id/glyph_points.shape[0])   #picker.point_id是picker对象选取的顶点ID，glyph_points.shape[0]记录了82这个值，通过这个计算出小球的ID
            if point_id != -1:  #表示有红色小球被选取了
                #计算与此红色小球相关的坐标
                x,y,z = x1[point_id],y1[point_id],z1[point_id]
                #将外框移动到小球上
                outline.bounds = (
                    x - 0.1, x + 0.1,
                    y - 0.1, y + 0.1,
                    z - 0.1, z + 0.1,
                )
                print(x,y,z)

    picker = figure.on_mouse_pick(piker_callback)
    picker.tolerance = 0.01     #设置tolerance参数提高精确度

    mlab.title("Click on red balls")    #设置窗口的标题文字

    mlab.show()

#
# pcd = o3d.io.read_point_cloud(r"E:\Work\THU\code\THU_Project_project\src\src_zivid\cal_hole\hole_ply\4.ply")
# vis = o3d.visualization.VisualizerWithVertexSelection()
# vis.create_window(window_name='Open3D', visible=True)
# vis.add_geometry(pcd)
# vis.run()
# point = vis.get_picked_points()
# vis.destroy_window()
# print(point[0].index, np.asarray(point[0].coord))
#
show_pick()