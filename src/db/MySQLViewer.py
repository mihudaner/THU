from PySide2.QtWidgets import *  # 不止这一个外部库，其它的库我在需要用到时单独引入
from PySide2.QtCore import Signal


from db.sql import SQL
from db.MySQLViewer_ui import Ui_Form

"D:\\soft\\Anaconda\\envs\\py37\\Scripts\\pyside2-uic -o  MySQLViewer_ui.py MySQLViewer.ui"

class DialogWindow(QDialog):
    infoSubmitted = Signal(str)  # 自定义信号

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(150, 150, 300, 200)
        self.setWindowTitle('Dialog Window')

        self.label = QLabel('Enter your info:', self)
        self.inputField = QLineEdit(self)
        self.submitButton = QPushButton('Submit', self)
        self.submitButton.clicked.connect(self.submitInfo)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.inputField)
        layout.addWidget(self.submitButton)

        self.setLayout(layout)

    def submitInfo(self):
        text = self.inputField.text()
        self.infoSubmitted.emit(text)  # 发射信号
        self.close()


class MySQLViewer(QWidget):
    def __init__(self, parent=None):
        super(MySQLViewer, self).__init__(parent)
        self.db = SQL()
        self.initUI()  # 初始化窗口

    def initUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.widgets = self.ui

        self.setWindowTitle("使用表格显示数据库中的数据")

        self.updateshow()

        # 连接双击信号和槽函数
        # self.widgets.tableWidget.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.widgets.btn_updata_db.clicked.connect(self.updateshow)

    def updateshow(self):
        result = self.db.show_all_items()  # 获取所有记录
        row = self.db.cursor.rowcount  # 获取记录个数，用于设置表格的行数
        vol = len(result[0])  # 获取字段数，用于设置表格的列数

        self.widgets.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.widgets.tableWidget.setRowCount(row)  # 设置表格行数
        self.widgets.tableWidget.setColumnCount(vol)  # 设置表格列数

        # 设置表头的名称

        self.widgets.tableWidget.setHorizontalHeaderLabels(
            # ['id', 'rgb_path', 'point_path', 'timestemp', ' frame_rate', 'exposure', 'gain', 'rgb_h', 'rgb_w', 'points_num', 'defect_num'])
            ['id', 'data_path', 'timestemp', 'exposure', 'gain', 'rgb_h', 'rgb_w', 'points_num', 'defect_num', ' n0x', ' n0y', 'n0z'])

        for i in range(row):  # 遍历行
            for j in range(vol):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))
                self.widgets.tableWidget.setItem(i, j, data)  # 转换后可插入表格

        self.widgets.tableWidget.resizeColumnToContents(row)  # 使列宽跟随内容改变
        self.widgets.tableWidget.resizeRowToContents(vol)  # 使行高跟随内容改变
        self.widgets.tableWidget.setAlternatingRowColors(True)  # 使表格颜色交错显示

    def add_frame(self, data_list):
        self.db.add_frame(data_list)
        return

    def on_item_double_clicked(self, item):
        # 获取双击的行和列
        row = item.row()
        col = item.column()

        # 获取该行的数据
        data = [self.widgets.tableWidget.item(row, c).text() for c in range(self.widgets.tableWidget.columnCount())]

        # 打印该行的信息
        print(f'Double clicked on row {row}, data: {data}')
        return data


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)  # 创建窗口程序
    demo = MySQLViewer()  # 创建窗口类对象
    demo.show()  # 显示窗口
    sys.exit(app.exec_())
