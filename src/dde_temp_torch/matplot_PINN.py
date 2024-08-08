# importing various libraries
import time
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl



class PINNWidget(QWidget):

    # constructor
    def __init__(self, parent=None):
        super(PINNWidget, self).__init__(parent)

        # a figure instance to plot on
        self.fig = plt.figure(figsize=(10, 4), dpi=200)
        self.canvas = FigureCanvas(self.fig)
        # self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QVBoxLayout()
        # # adding tool bar to the layout
        # layout.addWidget(self.toolbar)
        # adding canvas to the layout
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # self.setFixedSize(self.parent().width(), self.parent().height())  # 设置宽度为 300，高度为 200


    # action called by the push button
    def plot(self, data_dict):

        location, temperature, t = data_dict["location"], data_dict["temperature"], data_dict["time"]
        # clearing old figure
        self.fig.clear()
        x, y, z = location[:, 0:1], location[:, 1:2], location[:, 2:3]
        # create an axis
        ax = self.fig.add_axes(Axes3D(self.fig))

        norm = mpl.colors.Normalize(vmin=min(temperature), vmax=max(temperature))
        cm = plt.cm.get_cmap('plasma')

        ax.set_box_aspect((40, 20, 5))
        ax.set_xticks([0, 10, 20, 30, 40])
        ax.set_yticks([0, 5, 10, 15, 20])
        ax.set_zticks([0, 5])

        im = ax.scatter3D(x, y, z, norm=norm, c=temperature, cmap=cm)

        position = self.fig.add_axes([0.15, 0.12, 0.015, 0.78])  # 位置[左,下,宽,高]
        cb = self.fig.colorbar(im, cax=position)
        colorbarfontdict = {"size": 20, "color": "k", 'family': 'Times New Roman'}
        cb.ax.set_title('unit:K', fontdict=colorbarfontdict, pad=5)
        cb.ax.tick_params(labelsize=15, direction='in')

        title_fontdict = {"size": 25, "color": "k", 'family': 'Times New Roman'}
        ax.set_title(f"PINN temperature at {t:.2f}s", fontdict=title_fontdict)

        text_fontdict = {"size": 20, "color": "k", 'family': 'Times New Roman'}
        ax.text2D(-0.03, 0.05, f"Max temperature: {max(temperature)[0]:.0f}K", fontdict=text_fontdict)
        t1 = time.time()
        # refresh canvas
        self.canvas.draw()
        print(f"PINN plot time:{time.time() - t1}")

    def closeEvent(self, event):
        self.data_thread.stop()
        self.data_thread.wait()
        super().closeEvent(event)


# driver code
if __name__ == '__main__':
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = QplotWidget()

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())
