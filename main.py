import sqlite3
from sqlite3 import Error
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from design.main import Ui_MainWindow
import os


class Search(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.info.setVisible(False)
        self.info_2.setVisible(False)
        self.btn_search.clicked.connect(self.search_word)

        if os.path.exists("words.db") is False:
            self.create_bd()
            self.add_data()

        self.con_one = sqlite3.connect("words.db")
        self.cur_one = self.con_one.cursor()

    def search_word(self):
        word = self.word.toPlainText()
        print(word)
        if len(word) != 0:
            info1 = self.cur_one.execute("""select * from words1 where translate like '%{}%'""".format(word)).fetchall()
            info2 = self.cur_one.execute("""select * from words2 where translate like '%{}%'""".format(word)).fetchall()
            self.view(info1, self.tableWidget_1, self.info)
            self.view(info2, self.tableWidget_2, self.info_2)
        else:
            info1 = self.cur_one.execute("""select * from words1""").fetchall()
            info2 = self.cur_one.execute("""select * from words2""").fetchall()
            self.view(info1, self.tableWidget_1, self.info)
            self.view(info2, self.tableWidget_2, self.info_2)

    def view(self, info, table, wrong):
        if len(info) > 0:
            table.clear()

            table.setRowCount(len(info))
            table.setColumnCount(len(info[0]))

            for i, elem in enumerate(info):
                for j, val in enumerate(elem):
                    table.setItem(i, j, QTableWidgetItem(str(val)))
            wrong.setVisible(False)
        else:
            table.clear()
            wrong.setVisible(True)
            wrong.setText('Ничего не найдено!')

    def create_table(self, conn, table):
        try:
            c = conn.cursor()
            c.execute(table)
        except Error as e:
            print(e)

    def create_bd(self):
        database = r"words.db"
        words1_table = """ CREATE TABLE words1 (
                                        word      STRING,
                                        translate STRING);"""

        words2_table = """CREATE TABLE words2 (
                                        word      STRING,
                                        translate STRING);"""

        conn = sqlite3.connect(database)
        self.create_table(conn, words1_table)
        self.create_table(conn, words2_table)

    def add_data(self):

        #  words1
        data = open("data/СДРЯ.txt", mode='r', encoding='utf-8').readlines()
        con = sqlite3.connect("words.db")
        cur = con.cursor()
        for i in data:
            a, b = i.split('\t')
            b = b.split('\n')[0][:-1]
            cur.execute("""INSERT INTO words1(word) VALUES('{}')""".format(a)).fetchall()
            cur.execute("""UPDATE words1 SET translate = '{}' where word = '{}'""".format(b, a)).fetchall()
            con.commit()
        con.close()

        # words2
        data = open("data/ЭССЯ.txt", mode='r', encoding='utf-8').readlines()
        con = sqlite3.connect("words.db")
        cur = con.cursor()
        for i in data:
            a, b = i.split('\t')
            b = b.split('\n')[0][:-1]
            cur.execute("""INSERT INTO words2(word) VALUES("{}")""".format(a)).fetchall()
            cur.execute('''UPDATE words2 SET translate = "{}" where word = "{}"'''.format(b, a)).fetchall()
            con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Search()
    ex.show()
    sys.exit(app.exec_())
