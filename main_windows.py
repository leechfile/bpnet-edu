# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-image:url(\"image/py-img.png\");")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 110, 311, 121))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.edu_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edu_btn.setGeometry(QtCore.QRect(110, 270, 131, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.edu_btn.setFont(font)
        self.edu_btn.setObjectName("edu_btn")
        self.test_nerual = QtWidgets.QPushButton(self.centralwidget)
        self.test_nerual.setGeometry(QtCore.QRect(320, 270, 131, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.test_nerual.setFont(font)
        self.test_nerual.setObjectName("test_nerual")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(520, 270, 131, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "主界面"))
        self.label.setText(_translate("MainWindow", "神经网络教学系统"))
        self.edu_btn.setText(_translate("MainWindow", "教育网络"))
        self.test_nerual.setText(_translate("MainWindow", "测试网络"))
        self.exit_btn.setText(_translate("MainWindow", "退出"))
