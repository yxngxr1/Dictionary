# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.word = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word.sizePolicy().hasHeightForWidth())
        self.word.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.word.setFont(font)
        self.word.setObjectName("word")
        self.horizontalLayout_3.addWidget(self.word)
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.btn_search.setFont(font)
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_search.setStyleSheet("")
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_3.addWidget(self.btn_search)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.info_1 = QtWidgets.QLabel(self.centralwidget)
        self.info_1.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.info_1.setFont(font)
        self.info_1.setStyleSheet("")
        self.info_1.setAlignment(QtCore.Qt.AlignCenter)
        self.info_1.setObjectName("info_1")
        self.horizontalLayout.addWidget(self.info_1)
        self.info_2 = QtWidgets.QLabel(self.centralwidget)
        self.info_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.info_2.setFont(font)
        self.info_2.setStyleSheet("")
        self.info_2.setAlignment(QtCore.Qt.AlignCenter)
        self.info_2.setObjectName("info_2")
        self.horizontalLayout.addWidget(self.info_2)
        self.info_3 = QtWidgets.QLabel(self.centralwidget)
        self.info_3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.info_3.setFont(font)
        self.info_3.setStyleSheet("")
        self.info_3.setAlignment(QtCore.Qt.AlignCenter)
        self.info_3.setObjectName("info_3")
        self.horizontalLayout.addWidget(self.info_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.tableWidget_1.setFont(font)
        self.tableWidget_1.setStyleSheet("")
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(0)
        self.tableWidget_1.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget_1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget_2)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setStyleSheet("")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.error = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setText("")
        self.error.setObjectName("error")
        self.verticalLayout.addWidget(self.error)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Словарный поиск"))
        self.btn_search.setText(_translate("MainWindow", "Поиск"))
        self.info_1.setText(_translate("MainWindow", "ССС"))
        self.info_2.setText(_translate("MainWindow", "СДРЯ"))
        self.info_3.setText(_translate("MainWindow", "ЭССЯ"))
