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
        MainWindow.resize(1000, 848)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.word = QtWidgets.QTextEdit(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(310, 40, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.word.setFont(font)
        self.word.setStyleSheet("background-color: rgba(255,255,255,100);border: 1px solid #1565C0;border-radius: 8px;")
        self.word.setObjectName("word")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_1.setGeometry(QtCore.QRect(40, 180, 441, 551))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_1.setFont(font)
        self.tableWidget_1.setStyleSheet("")
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(0)
        self.tableWidget_1.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(530, 180, 441, 551))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 150, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(430, 100, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(15)
        self.btn_search.setFont(font)
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_search.setStyleSheet("background-color:rgba(0, 255, 0, 80);border-radius: 8")
        self.btn_search.setObjectName("btn_search")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setEnabled(True)
        self.info.setGeometry(QtCore.QRect(70, 750, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.info.setFont(font)
        self.info.setStyleSheet("background-color:rgba(255, 0, 0, 100);border-radius: 10")
        self.info.setText("")
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.info.setObjectName("info")
        self.info_2 = QtWidgets.QLabel(self.centralwidget)
        self.info_2.setEnabled(True)
        self.info_2.setGeometry(QtCore.QRect(550, 750, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.info_2.setFont(font)
        self.info_2.setStyleSheet("background-color:rgba(255, 0, 0, 100);border-radius: 10")
        self.info_2.setText("")
        self.info_2.setAlignment(QtCore.Qt.AlignCenter)
        self.info_2.setObjectName("info_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "СДРЯ и ЭССЯ"))
        self.label.setText(_translate("MainWindow", "Слово на русском"))
        self.label_2.setText(_translate("MainWindow", "СДРЯ"))
        self.label_3.setText(_translate("MainWindow", "ЭССЯ"))
        self.btn_search.setText(_translate("MainWindow", "Найти"))