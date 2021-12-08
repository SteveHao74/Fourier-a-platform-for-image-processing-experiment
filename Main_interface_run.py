# pyuic5  Main_interface_qt.ui -o Main_interface_qt.py
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import  sys
from Main_interface_qt import Ui_SAEE_main

import app_ch2.mych2_run
import  app_ch3.mych3_run
import  app_ch4.mych4_run
import  app_ch5.mych5_run
import  app_ch9.mych9_run


class Main_window(QtWidgets.QMainWindow, Ui_SAEE_main):
    def  __init__ (self):
        super(Main_window, self).__init__()
        self.setupUi(self)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  #
        # self.setAttribute(Qt.WA_TranslucentBackground)  #
        self.Bt_mn_ch2.clicked.connect(lambda:self.select_chapter(2))  # 打开
        self.Bt_mn_ch3.clicked.connect(lambda:self.select_chapter(3))  # 打开
        self.Bt_mn_ch4.clicked.connect(lambda:self.select_chapter(4))  # 打开
        self.Bt_mn_ch5.clicked.connect(lambda:self.select_chapter(5))  # 打开
        self.Bt_mn_ch9.clicked.connect(lambda:self.select_chapter(9))  # 打开
        self.aboutus.setVisible(False)
        self.Bt_aboutus.pressed.connect(lambda: self.aboutus.setVisible(True))  #
        self.Bt_aboutus.released.connect(lambda: self.aboutus.setVisible(False))

    def select_chapter(self,id):
        print(id)
        if id == 2:
            self.ui = app_ch2.mych2_run.mych2window()
        elif id == 3:
            print(id)
            self.ui = app_ch3.mych3_run.mych3window()
            print(id)
        elif id == 4:
            self.ui = app_ch4.mych4_run.mych4window()
        elif id == 5:
            self.ui = app_ch5.mych5_run.mych5window()
        elif id == 9:
            self.ui = app_ch9.mych9_run.mych9window()
        else :
            return
        self.ui.show()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提醒',"确定退出?", QMessageBox.Yes |QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__=="__main__":

    app=QtWidgets.QApplication(sys.argv)
    ui = Main_window()
    ui.show()
    sys.exit(app.exec_())
