# -*- coding: UTF8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from main import Ui_MainWindow
from rename import Ui_Form

class MainClass(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainClass, self).__init__(parent = None)
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        #self.setFixedSize(self.width(), self.height())
        #self.Ui.BtnOpenC.clicked.connect(self.Child)
        self.Ui.pushButton_rename.clicked.connect(self.rename)

    # 打开子窗体
    def rename(self):
        print("打开子窗体")

        self.rename = Ui_Form()
        #self.Dialog = QtWidgets.QDialog(self)  # 不加self 不在父窗体中， 有两个任务栏 。 加self 表示在父子在窗体中在一个任务栏

        self.Form = QtWidgets.QWidget()

        self.rename.setupUi2(self.Form)

        self.rename.pushButton_ok.clicked.connect(self.GetRenameFormat)
        self.rename.pushButton_cancel.clicked.connect(self.APPclose)

        #self.Form.exec_()

        #Form = QtWidgets.QWidget()
        #ui = Ui_Form()
        #ui.setupUi(Form)

        self.Form.show()
        #self.Form.exec_()
        #sys.exit(app.exec_())

    # 获取 弹框中填写的数据

    def GetRenameFormat(self):
        """将参数传递到main"""
        print(self.rename.label_example.Text())
        renameDate = self.rename.label_example.setText()
        #self.Ui.lineEdit_rename.Text(renameDate)
        #self.Form.close()

        #LineData=self.WChild.lineEdit.text()
        #self.Ui.textEdit.setText(LineData)
        #self.Dialog.close()
    # 关闭当前弹框
    def APPclose(self):
        self.Form.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainApp = MainClass()
    MainApp.show()
    sys.exit(app.exec_())