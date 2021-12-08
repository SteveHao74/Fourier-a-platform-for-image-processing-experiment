# pyuic5  mych2_qt.ui -o mych2_qt.py
from PyQt5 import QtWidgets
from mych2_qt import Ui_SAEE_chapter2
from PyQt5.QtWidgets import QFileDialog
from mych2_api import CH2_API
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2

class mych2window(QtWidgets.QMainWindow, Ui_SAEE_chapter2):
    def  __init__ (self):
        super(mych2window, self).__init__()
        self.setupUi(self)
        self.sd_pic=0
        self.sd_pic_path = ""
        import os
        base_address = os.path.dirname(__file__)  # 获得当前所在绝对路径（不知道用户会把此程序发在哪，需要随时重新更新）
        self.setWindowIcon(QIcon(base_address+"/pic/logo.png"))
        ######################ch2
        ##ch2p1
        self.selectpicture.clicked.connect(self.c2p1_read_file)  # 打开
        ##ch2p2
        self.Bts_21.clicked.connect(self.c2p21_smallfile)
        self.SL_1_21.valueChanged.connect(self.LC_21.display)
        self.Bts_22.clicked.connect(self.c2p22_bigfile)
        self.SL_1_22.valueChanged.connect(self.LC_22.display)
        ##ch2p3
        self.Bts_3.clicked.connect(self.c2p3_gray_file)
        self.SL_3.valueChanged.connect(self.LC_3.display)
        # self.save.triggered.connect(self.save_file)#保存
        # #编辑
        # self.zoomin.triggered.connect(self.zoomin_file)#放大
        # self.zoomout.triggered.connect(self.zoomout_file)#缩小
        # self.gray.triggered.connect(self.gray_file)#灰度
        # self.light.triggered.connect(self.light_file)#亮度
        # self.rotate.triggered.connect(self.rotate_file)#旋转
        # self.screenshots.triggered.connect(self.screenshots_file)#截图
        # #按钮功能
        # #浏览
        # self.Scan.clicked.connect(self.scan_file)


    def c2p1_read_file(self):
        #选取文件
        self.sd_pic_path, filetype =QFileDialog.getOpenFileName(self, "打开文件", "D:/imagetest", "All Files(*);;Text Files(*.jpg)")
        if  self.sd_pic_path :
            print(self.sd_pic_path, filetype)
            self.LB_pic_1.setPixmap(QPixmap.fromImage(QImage(self.sd_pic_path)))
            self.sd_pic= cv2.imread(self.sd_pic_path)
            height, width, channel= self.sd_pic.shape[0],self.sd_pic.shape[1],self.sd_pic.shape[2]
            self.information.setText("X  : " +str(width)  + " , Y : " + str(height) + " , channel  : " + str(channel))
    #
    # def save_file(self):
    #     #获取文件路径
    #     file_path = self.lineEdit.text()
    #     if file_path=='':
    #         self.showMessageBox()
    #     else:
    #         # 用全局变量保存所有需要保存的变量在内存中的值。
    #         file_name = QFileDialog.getSaveFileName(self,"文件保存","D:/imagetest/save","All Files (*);;Text Files (*.png)")
    #         print(file_name[0])
    #         #btn=button_self()
    #         #btn.file_save(file_path,file_name[0])
    #
    def c2p21_smallfile(self):
        index = self.SL_1_21.value()
        if self.checkBox_21.isChecked() :
            if self.sd_pic_path =='':
                self.showMessageBox()
            else:
                CH2_API.p21_imagereduction(index,self.sd_pic_path )
        else :
            CH2_API.p21_imagereduction()
    #
    def c2p22_bigfile(self):
        index = self.SL_1_22.value()
        if self.checkBox_22.isChecked():
            if self.sd_pic_path == '':
                self.showMessageBox()
            else:
                CH2_API.p22_imagemagnification(self.CB_22.currentIndex(),index, self.sd_pic_path)
        else:
            CH2_API.p22_imagemagnification(self.CB_22.currentIndex())

    def c2p3_gray_file(self):#灰度
        index = self.SL_3.value()
        if self.checkBox_3.isChecked():
            if self.sd_pic_path == '':
                self.showMessageBox()
            else:
                CH2_API.p3_imagegray(index, self.sd_pic_path)
        else:
            CH2_API.p3_imagegray(index)

    def showMessageBox(self):
       res_3 = QMessageBox.warning(self, "警告", "请选择文件，再执行该操作！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mych2window()
    ui.show()
    sys.exit(app.exec_())
