# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 190, 381, 541))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 155, 91, 21))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_command = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_command.setGeometry(QtCore.QRect(40, 110, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        self.lineEdit_command.setFont(font)
        self.lineEdit_command.setObjectName("lineEdit_command")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 85, 101, 21))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(290, 110, 75, 31))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(16)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setAutoDefault(False)
        self.pushButton_create.setDefault(False)
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_exec = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exec.setGeometry(QtCore.QRect(30, 10, 81, 51))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(20)
        self.pushButton_exec.setFont(font)
        self.pushButton_exec.setObjectName("pushButton_exec")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(120, 10, 81, 51))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(20)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(290, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(16)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Epic RPG"))
        self.label.setText(_translate("MainWindow", "指令集："))
        self.label_2.setText(_translate("MainWindow", "新增指令："))
        self.pushButton_create.setText(_translate("MainWindow", "新增"))
        self.pushButton_exec.setText(_translate("MainWindow", "啟動"))
        self.pushButton_close.setText(_translate("MainWindow", "關閉"))
        self.pushButton_save.setText(_translate("MainWindow", "資料存檔"))
