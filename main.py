import sqlite3
from sqlite3 import Error
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from design.design import Ui_MainWindow
import os


class Search(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.word.returnPressed.connect(self.search_word)
        self.btn_search.clicked.connect(self.search_word)
        self.error_count = 1
        self.write_flag = False

        # utf-8 format
        self.files = ["data/ССС.txt", "data/СДРЯ.txt", "data/ЭССЯ.txt"]

        # create bd
        if os.path.exists("words.db") is False:
            self.create_bd()
            self.add_data()

        # check errors
        if os.path.exists('errors.txt'):
            self.statusBar().showMessage('Программа запущена с ошибкой/ами! Результаты сохранены в "errors.txt"')
        else:
            self.statusBar().showMessage('v.1.1 © 2020 Дерганов Георгий')

        if self.write_flag:
            self.f.close()

        self.con_one = sqlite3.connect("words.db")
        self.cur_one = self.con_one.cursor()

    def search_word(self):
        word = self.word.text().replace('"', "")

        if len(word) > 0:
            info1 = self.cur_one.execute("""select * from words1 where translate like "%{}%" """.format(word)).fetchall()
            info2 = self.cur_one.execute("""select * from words2 where translate like "%{}%" """.format(word)).fetchall()
            info3 = self.cur_one.execute("""select * from words3 where translate like "%{}%" """.format(word)).fetchall()
        else:
            info1 = self.cur_one.execute("""select * from words1""").fetchall()
            info2 = self.cur_one.execute("""select * from words2""").fetchall()
            info3 = self.cur_one.execute("""select * from words3""").fetchall()

        self.view(info1, self.tableWidget_1)
        self.view(info2, self.tableWidget_2)
        self.view(info3, self.tableWidget_3)

    def view(self, info, table):
        if len(info) > 0:
            table.clear()
            table.setRowCount(len(info))
            table.setColumnCount(len(info[0]))
            table.setHorizontalHeaderLabels(['Слово', 'Перевод'])

            for i, elem in enumerate(info):
                for j, val in enumerate(elem):
                    table.setItem(i, j, QTableWidgetItem(str(val)))

            if table == self.tableWidget_1:
                self.info_1.setText('ССС (найдено {})'.format(len(info)))
            elif table == self.tableWidget_2:
                self.info_2.setText('СДРЯ (найдено {})'.format(len(info)))
            elif table == self.tableWidget_3:
                self.info_3.setText('ЭССЯ (найдено {})'.format(len(info)))

            table.resizeColumnsToContents()
            table.verticalHeader().setMinimumSectionSize(10)

        else:
            table.clear()
            table.setRowCount(0)
            table.setColumnCount(0)

            if table == self.tableWidget_1:
                self.info_1.setText('ССС (не найдено)')
            elif table == self.tableWidget_2:
                self.info_2.setText('СДРЯ (не найдено)')
            elif table == self.tableWidget_3:
                self.info_3.setText('ЭССЯ (не найдено)')

    def create_bd(self):
        database = r"words.db"
        conn = sqlite3.connect(database)
        for i in range(1, len(self.files) + 1):
            dict = """create table words{}(word string, translate string);""".format(i)
            self.create_table(conn, dict)

    def create_table(self, conn, table):
        try:
            c = conn.cursor()
            c.execute(table)
        except Error as e:
            print(e)

    def add_data(self):
        for n, file in enumerate(self.files):
            data = open(file, mode='r', encoding='utf-8').read().split('\n')
            con = sqlite3.connect("words.db")
            cur = con.cursor()
            for i in data:
                try:
                    a, b = i.split('\t')
                    cur.execute("""insert into words{}(word, translate) values("{}", "{}")""".format(n + 1, a, b)).fetchall()
                    con.commit()
                except Exception as e:
                    self.write_error(i, file, e)
                    continue
            con.close()

    def write_error(self, i, file, e):
        self.write_flag = True
        if not os.path.exists('errors.txt'):
            self.f = open('errors.txt', 'w')

        error = 'Ошибка({}) в файле: "{}", в строке: "{}"'.format(e, file, i)
        self.f.write("{}) {}\n".format(self.error_count, error))
        print('Ошибочка:', self.error_count)
        self.error_count += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Search()
    ex.show()
    sys.exit(app.exec_())
