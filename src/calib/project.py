import cv2
import numpy as np
import open3d as o3d
from mayavi import mlab
import pickle
from point2rgb import test_run_calib, show_project_res


def show_point(*points_list):
    """
    显示点云
    :param points_list:
    :return:
    """
    fig = mlab.figure("point", bgcolor=(0, 0, 0), size=(1650, 1500))

    for i, points in enumerate(points_list):
        x = points[:, 0]  # x position of point
        y = points[:, 1]  # y position of point
        z = points[:, 2] + i * 0.01  # z position of point
        colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

        mlab.points3d(x, y, z,
                      scale_factor=0.1 + 0.2 * i,
                      # z,
                      color=colors[i],  # Values used for Color
                      mode="point" if i == 0 else "sphere",
                      # mode="sphere",
                      colormap='spectral',  # 'bone', 'copper', 'gnuplot'
                      # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                      figure=fig,
                      )

    mlab.show()


def load_label(path):
    with open(path, 'rb') as file:
        loaded_data = pickle.load(file)
    # 打印加载的对象
    print(loaded_data)
    return loaded_data


def flip_xyz(p, fliter=True):
    """
    点云平移（fliter: 是否会过滤值为0点，False的话返回的点z为0，true删除）
    Args:
        p: 输入点云
        fliter: 是否会过滤值为0点，False的话返回的点z为0，true删除

    Returns:
        p:平移后的点云
        x: 平移后的点云
        y: 平移后的点云
        z: 平移后的点云
        mask: 平移后的点云
    """

    mask = np.isnan(p[:, 2])
    p[mask] = np.array([0, 0, 0])

    if fliter:
        mask = p[:, 2] != 0
        p = p[mask]

    x = np.sort(p[:, 0])
    y = np.sort(p[:, 1])
    z = np.sort(p[:, 2])

    x = x[int(len(x) / 2)]
    y = y[int(len(y) / 2)]
    z = z[int(len(z) / 2)]

    if not fliter:
        mask = p[:, 2] == 0
        p[mask] = z

    p = p - np.array([x, y, z])

    return p, x, y, z, mask


def get_points_inbox(box, projected_points):
    """
        第idx个label内的点云

    """
    points = np.reshape(projected_points, (-1, 2))
    print(box)
    print(points)
    mask1 = points[:, 0] > box[0]
    mask2 = points[:, 0] < box[2]
    mask3 = points[:, 1] > box[1]
    mask4 = points[:, 1] < box[3]
    mask = mask1 & mask2 & mask3 & mask4
    return mask


def get_points_inbox_all(boxs, projected_points):
    """
        第idx个label内的点云

    """
    mask = get_points_inbox(boxs[0], projected_points)
    for i in range(1, len(boxs)):
        mask = mask | get_points_inbox(boxs[i], projected_points)
    return mask


def load_ply_points(point_path):
    pts = o3d.io.read_point_cloud(point_path)
    # 访问PLY数据
    _ = np.asarray(pts.points)
    pts = _.copy()
    # 点云resize和点云rgb一样的shape
    return pts


if __name__ == "__main__":
    label_path = r"E:\Work\THU\code\THU_Project_project\data\zivid_labels\000023.pkl"
    point_path = r"E:\Work\THU\code\THU_Project_project\data\zivid_points\000023.ply"
    hik_img = cv2.imread(r"E:\Work\THU\code\THU_Project_project\data\hik_img\000025.jpg")

    labels = load_label(label_path)
    pts = load_ply_points(point_path)
    pts = np.resize(pts, (1200, 1920, 3))
    # ROI
    pts = pts[300:300 + 800, 500:500 + 800, :]

    pts = np.reshape(pts, (-1, 3))
    flip_xyz(pts, fliter=True)
    rvec, tvec, camera_matrix, dist_coeffs = test_run_calib(show=False)
    np.save("rvec.npy", rvec)
    np.save("tvec.npy", tvec)
    np.save("camera_matrix.npy", camera_matrix)
    np.save("dist_coeffs.npy", dist_coeffs)

    projected_points, _ = cv2.projectPoints(pts.reshape(1, -1, 3), rvec, tvec, camera_matrix, dist_coeffs)
    # 2d点在不在mask内
    mask = get_points_inbox_all(labels, projected_points)
    fault_pts = pts[mask]

    show_point(pts, fault_pts)
    show_project_res(projected_points[mask], hik_img)
