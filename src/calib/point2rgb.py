import cv2
import numpy as np
import open3d as o3d
from mayavi import mlab

# 标定板内点个数
(grows, gcols) = (11, 8)


def show_img(img):
    """
    显示图片
    :param img:
    :return:
    """
    cv2.imshow("img", img)
    # 等待用户按下任意键，然后关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show_project_res(projected_points, img):
    """
    显示投影结果
    :param projected_points: 投影到图像的像素位置
    :param img: img
    :return:
    """
    # 指定圆的颜色（BGR 格式，红色为 (0, 0, 255)）
    color = (0, 0, 255)
    # 指定线条宽度（如果为-1，则填充圆）
    thickness = 1
    # 遍历像素坐标列表并在每个位置绘制圆圈
    for (x, y) in np.squeeze(projected_points, axis=1):
        center = (int(x), int(y))
        radius = 8        # 圆的半径，根据需要调整
        cv2.circle(img, center, radius, color, thickness)
    show_img(img)
    return


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
                      # mode="point",
                      mode="sphere",
                      colormap='spectral',  # 'bone', 'copper', 'gnuplot'
                      # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                      figure=fig,
                      )

    mlab.show()


def get_datas(hik_path, zivid_rgb_path, point_path, down_rate=2):
    """
    读取获得一组数据
    :param hik_path:
    :param zivid_rgb_path:
    :param point_path:
    :return:
    """
    hik_img = cv2.imread(hik_path)
    hik_img = cv2.resize(hik_img, (hik_img.shape[1] // down_rate, hik_img.shape[0] // down_rate))
    # hik_img = cv2.resize(hik_img, (hik_img.shape[1], hik_img.shape[0]))

    zivid_rgb = cv2.imread(zivid_rgb_path)
    # 读取PLY文件
    pts = o3d.io.read_point_cloud(point_path)
    # 访问PLY数据
    _ = np.asarray(pts.points)
    pts = _.copy()
    # 点云resize和点云rgb一样的shape
    pts = np.resize(pts, (zivid_rgb.shape[0], zivid_rgb.shape[1], 3))
    return hik_img, zivid_rgb, pts


def detect_corner(img):
    """
    标定板检测角点
    :param img:
    :return: 角点np数组
    """

    # 查找标定板角点
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    found, corners = cv2.findChessboardCorners(gray, (gcols, grows), None)

    # 如果找到了角点
    if found:
        # 绘制角点并显示图像
        cv2.drawChessboardCorners(img, (grows, gcols), corners, found)
        show_img(img)
        return np.squeeze(corners, axis=1)  # 去除第二个维度
    else:
        print("未找到标定板角点。")
        return False


# 定义一个函数来执行相机标定
def calibrate_camera(object_points, image_points, img):
    """
    相机标定获取相机内参和畸变参数
    :param object_points: xyz点
    :param image_points: 图像点
    :param img: 图像
    :return: camera_matrix, dist_coeffs
    """
    # 进行相机标定
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 创建一个初始的相机内部矩阵
    # 初始内部矩阵（您应该用实际的相机参数替换这些值）
    fx = 1000.0  # 像素的焦距（x轴）
    fy = 1000.0  # 像素的焦距（y轴）
    cx = 640.0  # 像素的主点（x轴）
    cy = 480.0  # 像素的主点（y轴）

    # 创建初始内部矩阵
    camera_matrix = np.array([[fx, 0, cx],
                              [0, fy, cy],
                              [0, 0, 1]])

    # 畸变系数（您应该用实际的值替换这些值）
    dist_coeffs = np.zeros((4, 1))

    retval, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
        objectPoints=object_points,
        imagePoints=image_points,
        imageSize=gray.shape[::-1],  # 图片尺寸
        cameraMatrix=camera_matrix,  # 如果已知内参，可以在这里提供
        distCoeffs=dist_coeffs,  # 如果已知畸变参数，可以在这里提供
        # flags=cv2.CALIB_RATIONAL_MODEL  # 可以选择使用更高级的标定模型
        flags=(cv2.CALIB_USE_INTRINSIC_GUESS + cv2.CALIB_FIX_PRINCIPAL_POINT)
        # ！！！opencv版本  3.4.2.16和flag不同会报错
    )

    return camera_matrix, dist_coeffs


# 定义一个函数来估计相机的外部参数
def estimate_camera_pose(points_3d, points_2d, camera_matrix, dist_coeffs):
    """
    计算相机的外部参数
    :param points_3d: xyz角点
    :param points_2d: 角度像素位置
    :param camera_matrix:
    :param dist_coeffs:
    :return: rvec, tvec
    """
    # 使用solvePnP函数估计相机的外部参数
    retval, rvec, tvec = cv2.solvePnP(points_3d, points_2d, camera_matrix, dist_coeffs)
    # https://blog.csdn.net/qq_36187544/article/details/102626629
    return rvec, tvec


def test_run_calib(show=False):
    hik_imgs, zivid_points, zivid_rgbs = [], [], []
    for i in range(1, 13):
        # hik被投影的图像
        hik_imgs.append(r"E:\Work\THU\code\THU_Project_project\data\hik_img/%06d.png" % i)
        # 点云路径
        zivid_points.append(r"E:\Work\THU\code\THU_Project_project\data\zivid_points/%06d.ply" % i)
        # 点云rgb路径
        zivid_rgbs.append(r"E:\Work\THU\code\THU_Project_project\data\zivid_rgb/%06d.png" % i)
    rvec, tvec, camera_matrix, dist_coeffs = run_calib(hik_imgs, zivid_points, zivid_rgbs, show=show)
    return rvec, tvec, camera_matrix, dist_coeffs


def run_calib(hik_imgs, zivid_points, zivid_rgbs, down_rate=2, show=False):
    """

    Parameters
    ----------
    hik_imgs 标定使用的HIK图像路径
    zivid_points 标定使用的Zivid点云路径
    zivid_rgbs 标定使用的ZividRGB路径
    down_rate 标定的下采样倍率，如果设置1图像过大结果反而不好
    show 是否显示中间结果
    Returns 坐标转换需要的矩阵
    -------

    """
    all_point_corners = []
    all_img_corners = []

    for i in range(0, len(hik_imgs)):
        print("%06d" % i)
        point_corners = []
        # 从路径加载所有数据
        hik_img, zivid_rgb, pts = get_datas(hik_imgs[i], zivid_rgbs[i], zivid_points[i], down_rate)  # pts[1200,1920]

        # 检测ZIVID图像上的标定板角度坐标
        zivid_rgb_corners = detect_corner(zivid_rgb)
        # 检测HIK图像上的标定板角度坐标
        hik_img_corners = detect_corner(hik_img)

        # zivid_rgb_corners像素点转对应的xyz点point_corners
        if zivid_rgb_corners is not False:
            for i in range(zivid_rgb_corners.shape[0]):
                w = int(zivid_rgb_corners[i][0])
                h = int(zivid_rgb_corners[i][1])
                # print(w, h)
                # ZIVID图像上检测到的角点的像素对应的点云坐标如果是NAN则用邻点代替
                while np.isnan(pts[int(h)][int(w)][0]):
                    print("warning calib  have a nan!")
                    h += 1
                    w += 1
                point_corners.append(pts[int(h)][int(w)])
        # 获得所有的标定板的点云xyz和HIK图像上的像素坐标
        all_point_corners.append(point_corners)
        all_img_corners.append(hik_img_corners)
        if True:
            show_point(pts[::5, ::5].reshape((-1, 3)), np.asarray(point_corners, dtype=np.float32))

    all_point_corners = np.asarray(all_point_corners, dtype=np.float32)
    all_img_corners = np.asarray(all_img_corners, dtype=np.float32)

    # 使用所有的点云和图像角点进行相机标定
    camera_matrix, dist_coeffs = calibrate_camera(all_point_corners, all_img_corners, hik_img)
    # 打印相机内参和畸变参数
    print("Camera Matrix (Intrinsic Parameters):")
    print(camera_matrix)
    print("\nDistortion Coefficients:")
    print(dist_coeffs)

    rvec, tvec = estimate_camera_pose(all_point_corners[0], all_img_corners[0], camera_matrix, dist_coeffs)
    # 打印外部参数
    print("Rotation Vector (rvec):")
    print(rvec)
    print("Translation Vector (tvec):")
    print(tvec)

    # 现在你已经有了相机的内参和畸变参数，可以使用它们将点云坐标投影到像素坐标

    for i in range(0, len(hik_imgs)):
        new_element = np.array([20.81854, -17.99710, 398.91553])
        cloud_point = all_point_corners[i]
        cloud_point = np.append(cloud_point, [new_element], axis=0)

        # 使用solvePnP估计的外部参数（rvec和tvec）和相机内参将3D点投影到像素坐标
        # projected_points是投影后的2D像素坐标
        projected_points, _ = cv2.projectPoints(cloud_point.reshape(1, -1, 3), rvec, tvec, camera_matrix, dist_coeffs)

        hik_img, zivid_rgb, pts = get_datas(hik_imgs[i], zivid_rgbs[i], zivid_points[i])
        if show:
            show_project_res(projected_points, hik_img)
    return rvec, tvec, camera_matrix, dist_coeffs


if __name__ == "__main__":
    test_run_calib(show=True)
