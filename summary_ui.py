# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'summary_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(200, 180, 391, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(200, 240, 371, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 340, 93, 28))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(MainWindow.p1_ck)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "潘龙挺陈钦婵诊所信息录入系统"))
        self.radioButton_3.setText(_translate("MainWindow", "诊所录入信息查找与补充系统"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
import sys
from PyQt5 import QtWidgets, QtGui
from os import listdir,path
from subprocess import getstatusoutput
filename_list=listdir("./database/")
class Mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        # super(Mywindow, self).__init__()

        QtWidgets.QMainWindow.__init__(self,parent)
        self.use_palette()
        self.setupUi(self)
        self.info=""
    def use_palette(self):
        self.setWindowTitle("设置背景图片")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./timg2.jpg")))
        self.setPalette(window_pale)
    def p1_ck(self):
        reply = QtWidgets.QMessageBox.question(self,
                                               "温馨提示",
                                               "确认登录？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if self.radioButton.isChecked():
            if path.exists("project.exe"):
                rc, out = getstatusoutput("project.exe")
        elif self.radioButton_3.isChecked():
            if path.exists("search_and_delete.exe"):
                rc, out = getstatusoutput("search_and_delete.exe")
        else:
            print("【INFO】您未勾选进入的项目！")
app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.resize(850, 600)
window.show()
sys.exit(app.exec_())