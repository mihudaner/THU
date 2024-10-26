import numpy as np
from mayavi import mlab

from pathlib import Path


def show_point(*points_list):
    fig = mlab.figure("point", bgcolor=(0, 0, 0), size=(1650, 1500))

    for i, points in enumerate(points_list):
        x = points[:, 0]  # x position of point
        y = points[:, 1]  # y position of point
        z = points[:, 2] + i * 0.01  # z position of point
        colors = [(1, 0, 0), (0, 1, 0), (1, 1, 1)]

        mlab.points3d(x, y, z,
                      scale_factor=0.05 - 0.01 * i,
                      # z,
                      color=colors[i],  # Values used for Color
                      mode="point",
                      # mode="sphere",
                      colormap='spectral',  # 'bone', 'copper', 'gnuplot'
                      # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                      figure=fig,
                      )

    mlab.show()


if __name__ == "__main__":
    real_pointcloud = np.fromfile(r"F:\ONCE\data\000092\lidar_roof/1616442789799.bin", dtype=np.float32,
                                  count=-1).reshape([-1, 4])
    show_point(real_pointcloud)
