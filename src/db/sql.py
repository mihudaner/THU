# SQL注入
# 此处商品名称输入为:'or 1=1 or '1时即可打印出所有数据
#  'or 1=1 or'1或者 'or 1=1 or' 这里的两个单引号表示与'%s'的两个单引号进行配对 单引号双引号取决于input接受输入时的"%s"还是'%s'  select * from goods where name = ''or 1=1 or'1';
#  select * from goods where name = ""or 1=1 or "";

import PySide2
from pymysql import *
from datetime import datetime


class SQL(object):
    def __init__(self):
        # 创建connection连接  连接对象
        self.conn = connect(host="localhost", port=3306, user='root', password="root", database='thu', charset='utf8')
        # 获取Cursor对象  游标对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭cursor对象
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        fetchall = self.cursor.fetchall()
        for temp in fetchall:
            print(temp)
        return fetchall

    def show_all_items(self):
        sql = "select * from frame;"
        return self.execute_sql(sql)

    def show_column(self):
        tag = input("input column tag:")
        sql = "select %s from frame;" % tag
        self.execute_sql(sql)

    def add_frame(self, data_list):
        """
        data_list:
            data_path = "/path/to/your/rgb/image.jpg"
            timestemp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            exposure = 0.5
            gain = 1.0
            rgb_h = 1080
            rgb_w = 1920
            points_num = 10000
            defect_num = 5
            n0x = 1.0
            n0y = 1080.0
            n0z = 1920.0
        """
        # 构造插入语句
        sql = """
                INSERT INTO frame(data_path , timestemp, exposure, gain, rgb_h, rgb_w, points_num, defect_num, n0x,n0y, n0z)
                VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s);
                """

        # print(sql, (data_path, timestemp, exposure, gain, rgb_h, rgb_w, points_num, defect_num, n0x, n0y, n0z))
        # 执行插入操作
        # self.cursor.execute(sql, [data_path, timestemp, exposure, gain, rgb_h, rgb_w, points_num, defect_num, n0x, n0y, n0z])

        print(sql, data_list)
        self.cursor.execute(sql, data_list)

        self.conn.commit()

    def get_info_by_id(self):
        id = input("请输入要查询的frame_id:")
        sql = """select * from frame where id = '%s';""" % id
        print("——————————————>%s<-------------" % sql)
        self.execute_sql(sql)

    @staticmethod
    def print_menu():
        print("--------------------京东--------------------")
        print("1:所有的数据")
        print("2:所有的数据的某一列")
        print("3:添加数据")
        print("4:获取数据通过id")
        num = input("请输入对应功能序号:")
        return num

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                # 调用所有商品
                self.show_all_items()

            elif num == "2":
                self.show_column()

            elif num == "3":
                self.add_frame()

            elif num == "4":
                self.get_info_by_id()

            else:
                print("输入有误,请重新输入!")


def main():
    # 创建一个京东商城对象
    jd = SQL()
    # 调用这个对象的run方法
    jd.run()


if __name__ == "__main__":
    main()
