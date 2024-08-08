import time
from .get_plane import *

matplotlib.use('Qt5Agg')
import open3d as o3d


def pcd_rotate_normal(pointcloud, n0, n1):
    """
    点云法向量旋转
    Args:
        pointcloud: 输入点云
        n0(array): 1x3, 原始法向量
        n1(array): 1x3, 目标法向量

    Returns:
        pcd : open3d PointCloud, 旋转后点云
    """

    n0_norm2 = np.sqrt(sum(n0 ** 2))
    n1_norm2 = np.sqrt(sum(n1 ** 2))
    theta = np.arccos(sum(n0 * n1) / n0_norm2 / n1_norm2)
    r_axis = np.array([n1[2] * n0[1] - n0[2] * n1[1], n0[2] * n1[0] - n1[2] * n0[0], n0[0] * n1[1] - n1[0] * n0[1]])
    r_axis = r_axis * theta / np.sqrt(sum(r_axis ** 2))
    R = pointcloud.get_rotation_matrix_from_axis_angle(r_axis.T)
    pointcloud.rotate(R)
    points = np.asarray(pointcloud.points)
    return pointcloud


def deep_analysis(pts):
    # 旋转器件，调整角度
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pts)
    pcd = pcd_rotate_normal(pcd, np.array((-6.5, 7.5, 28.68)), np.array((0, 0, 1)))
    pts = np.asarray(pcd.points)
    # show_point(pts, points)

    # 求平面
    t1 = time.perf_counter()
    x = pts[:, 0:1]
    y = pts[:, 1:2]
    z = pts[:, 2:3]
    size = pts.shape[0]

    # 倾斜平面
    X, R = get_plane(x, y, z, size)
    #  求深度
    # z max   与孔洞平面距离d
    z_index = np.argmax(z)
    d_point = [x[z_index], y[z_index], z[z_index]]  # z值最大为最深点

    # 求平面中点，及中间平面
    # 中点
    point_Center2 = 1 / 2 * np.array((min(x) + max(x), min(y) + max(y)))
    z_1 = X[0, 0] * point_Center2[0] + X[1, 0] * point_Center2[1] + X[2, 0]
    point_Center3 = [point_Center2[0], point_Center2[1], z_1]
    # 中间平面  d‘
    z2 = z_1
    x_p = np.linspace(min(x), max(x), 100)  # ？
    z_p1 = np.full(x_p.shape, z_1)
    z_index = np.argmax(z)
    t2 = time.perf_counter()
    t = t2 - t1
    print(f"max depth(Centor): {z[z_index] - z2}")
    print(f"time: {t}")

    # 展示图像
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, projection='3d')
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_zlabel("z")
    ax1.scatter(d_point[0], d_point[1], d_point[2], c='g', marker='*', s=80)
    ax1.scatter(x, y, z, c='r', marker='o')
    x_p = np.linspace(min(x), max(x), 100)
    y_p = np.linspace(min(y), max(y), 100)
    x_p, y_p = np.meshgrid(x_p, y_p)

    # 倾斜平面的Z
    z_p = X[0, 0] * x_p + X[1, 0] * y_p + X[2, 0]
    ax1.plot_wireframe(x_p, y_p, z_p, rstride=10, cstride=10)

    # 计算平面夹角
    n1 = np.array((X[0, 0], X[1, 0], -1))
    n2 = np.array((0, 0, 1))
    l_1 = np.sqrt(n1.dot(n1))
    l_2 = np.sqrt(n2.dot(n2))
    dian = n1.dot(n2)
    cos_ = dian / (l_1 * l_2)
    angle_hu = np.arccos(cos_)
    angle_d = angle_hu * 180 / np.pi
    print(f"角度：{min(angle_d, 180 - angle_d)}")

    # “中间”平面及中点
    ax1.scatter(point_Center3[0], point_Center3[1], z_1, c='b', marker='*', s=80)
    ax1.plot_wireframe(x_p, y_p, z_p1, rstride=10, cstride=10, color='yellow')

    plt.show()
