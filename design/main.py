# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(895, 712)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.word = QtWidgets.QTextEdit(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(20, 20, 691, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.word.setFont(font)
        self.word.setStyleSheet("")
        self.word.setObjectName("word")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_1.setGeometry(QtCore.QRect(20, 110, 301, 551))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_1.setFont(font)
        self.tableWidget_1.setStyleSheet("")
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(0)
        self.tableWidget_1.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(330, 110, 271, 551))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(730, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(15)
        self.btn_search.setFont(font)
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_search.setStyleSheet("")
        self.btn_search.setObjectName("btn_search")
        self.info_1 = QtWidgets.QLabel(self.centralwidget)
        self.info_1.setEnabled(True)
        self.info_1.setGeometry(QtCore.QRect(20, 70, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.info_1.setFont(font)
        self.info_1.setStyleSheet("")
        self.info_1.setAlignment(QtCore.Qt.AlignCenter)
        self.info_1.setObjectName("info_1")
        self.info_2 = QtWidgets.QLabel(self.centralwidget)
        self.info_2.setEnabled(True)
        self.info_2.setGeometry(QtCore.QRect(330, 70, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.info_2.setFont(font)
        self.info_2.setStyleSheet("")
        self.info_2.setAlignment(QtCore.Qt.AlignCenter)
        self.info_2.setObjectName("info_2")
        self.info_3 = QtWidgets.QLabel(self.centralwidget)
        self.info_3.setEnabled(True)
        self.info_3.setGeometry(QtCore.QRect(610, 70, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.info_3.setFont(font)
        self.info_3.setStyleSheet("")
        self.info_3.setAlignment(QtCore.Qt.AlignCenter)
        self.info_3.setObjectName("info_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(610, 110, 271, 551))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setStyleSheet("")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 895, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Словарный поиск"))
        self.btn_search.setText(_translate("MainWindow", "Поиск"))
        self.info_1.setText(_translate("MainWindow", "ССС"))
        self.info_2.setText(_translate("MainWindow", "СДРЯ"))
        self.info_3.setText(_translate("MainWindow", "ЭССЯ"))
