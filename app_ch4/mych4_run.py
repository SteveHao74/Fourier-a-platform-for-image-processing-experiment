# pyuic5  wide_mych4_qt.ui -o mych4_qt.py
from PyQt5 import QtWidgets
from mych4_qt import Ui_Ch4_Window
from PyQt5.QtWidgets import QFileDialog
from mych4_api import CH4_API
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
CH4_API=CH4_API()

class mych4window(QtWidgets.QMainWindow, Ui_Ch4_Window):
    def  __init__ (self):
        super(mych4window, self).__init__()
        self.setupUi(self)
        import os
        base_address = os.path.dirname(__file__)  # 获得当前所在绝对路径（不知道用户会把此程序发在哪，需要随时重新更新）
        self.setWindowIcon(QIcon(base_address+"/pic/logo.png"))
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 无边框，置顶
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 透明背景色

        ################预存图片：opencv格式#############
        self.sd_pic=[]##用于存自定义图片
        # '4.2.jpg'纹理，'4.3.jpg'文本，'4.4.jpg'人像，'4.5.jpg'扫描线

        self.pic_p2  =  cv2.imread(base_address+"/pic/4.1.jpg")
        self.pic_p3_1 = cv2.imread(base_address+'/pic/4.2.jpg')
        self.pic_p3_2 = cv2.imread(base_address+'/pic/4.3.jpg')
        self.pic_p3_3 = cv2.imread(base_address+'/pic/4.4.jpg')
        self.pic_p3_4 = cv2.imread(base_address+'/pic/4.5.jpg')
        print(self.pic_p2)
        self.sd_pic_path = ""
        self.current_deal_pic = []
        self.p2_fshift=0#用于存储P2部分拆分步骤中所需要公用的傅里叶变换结果
        self.c4p1_show_pic(0, 0)#刚打开时，默认显示

        # ##ch4p1
        self.selectpicture.clicked.connect(self.c4p1_read_file)  # 打开
        self.selectpicture.setEnabled(False)#默认是使用默认图片，所以加载图片按钮为冻结状态,当激光按钮选择自定义图片时，将解冻
        # ##ch4p2
        self.RB_P1_default.toggled.connect(self.c4p1_frozen_button)
        self.RB_P1_default.toggled.connect(lambda: self.c4p1_show_pic(self.tabWidget.currentIndex(), self.CB_3.currentIndex()))
        self.Bt_p2tl.clicked.connect(lambda:self.c4p2_FFT_IFFT_ALL(0))
        self.Bt_p2st1.clicked.connect(lambda:self.c4p2_FFT_IFFT_ALL(1))
        self.Bt_p2st2.clicked.connect(lambda:self.c4p2_FFT_IFFT_ALL(2))
        self.Bt_p2st3.clicked.connect(lambda:self.c4p2_FFT_IFFT_ALL(3))
        self.Bt_p2st4.clicked.connect(lambda:self.c4p2_FFT_IFFT_ALL(4))
        self.c4p1_frozen_button()#初始化冷冻按钮

        self.Bt_p2_cross.clicked.connect(lambda: self.c4p2_FFT_IFFT_ALL(5))

        self.LB_pic_3.setPixmap(QPixmap.fromImage(QImage(base_address+'/pic/look.jpg')))
        # ##ch4p3

        self.tabWidget.currentChanged.connect(lambda: self.c4p1_show_pic(self.tabWidget.currentIndex(), self.CB_3.currentIndex()))
        self.CB_3.currentIndexChanged.connect(lambda:self.c4p1_show_pic(1,self.CB_3.currentIndex()))
        self.Bt_p3_L1.clicked.connect(lambda:self.c4p3_filter_all(1))
        self.Bt_p3_L2.clicked.connect(lambda:self.c4p3_filter_all(2))
        self.Bt_p3_L3.clicked.connect(lambda:self.c4p3_filter_all(3))
        self.Bt_p3_H1.clicked.connect(lambda:self.c4p3_filter_all(4))
        self.Bt_p3_H2.clicked.connect(lambda:self.c4p3_filter_all(5))
        self.Bt_p3_H3.clicked.connect(lambda:self.c4p3_filter_all(6))
        self.Bt_p3_TL.clicked.connect(lambda:self.c4p3_filter_all(7))

        self.SL_31.valueChanged.connect(self.LC_31.display)
        self.SL_32.valueChanged.connect(self.LC_32.display)
        self.SL_33.valueChanged.connect(self.LC_33.display)
        self.SL_34.valueChanged.connect(self.LC_34.display)

    ##################################tool_functions#######################################
    def cvimg_to_qtimg(self,cvimg):#把CV格式图片转换成QImage格式
        height, width, depth = cvimg.shape
        cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
        cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)
        return cvimg

    ###################################part1###########################################

    def c4p1_read_file(self):
        #选取文件
        self.sd_pic_path, filetype =QFileDialog.getOpenFileName(self, "打开文件", "D:/imagetest", "All Files(*);;Text Files(*.jpg)")
        if  self.sd_pic_path :
            print(self.sd_pic_path, filetype)
            self.sd_pic= cv2.imread(self.sd_pic_path)
            self.c4p1_show_pic()

    def c4p1_show_pic(self,page=0,id=0):
        print(1)
        if self.RB_P1_default.isChecked()==True:##激光按钮选中了使用默认图片
            print(2)
            self.selectpicture.setEnabled(False)
            if page == 0:#part2对应TabWidget的page1
                self.current_deal_pic = self.pic_p2
            elif page== 1 :#part3对应TabWidget的page2
                if id == 0:
                    self.current_deal_pic = self.pic_p3_1
                if id == 1:
                    self.current_deal_pic = self.pic_p3_2
                if id == 2:
                    self.current_deal_pic = self.pic_p3_3
                if id == 3:
                    self.current_deal_pic = self.pic_p3_4
        else :###激光按钮选中了使用自定义图片
            self.selectpicture.setEnabled(True)
            self.current_deal_pic = self.sd_pic

        if self.current_deal_pic == []:#未加载图片
            print(5)
            self.LB_pic_1.setPixmap(QPixmap(""))
            self.information.setText("X  : " + "  " + " , Y : " + "  " + " , channel  : " + "  ")
            print(6)
        else:
            QImage_pic = self.cvimg_to_qtimg(self.current_deal_pic)
            print(4)
            self.LB_pic_1.setPixmap(QPixmap.fromImage(QImage_pic))
            height, width, channel = self.current_deal_pic.shape[0], self.current_deal_pic.shape[1], self.current_deal_pic.shape[2]
            self.information.setText("X  : " +str(width)  + " , Y : " + str(height) + " , channel  : " + str(channel))
        self.c4p1_frozen_button()


    def c4p1_frozen_button(self):
        self.Bt_p2st2.setEnabled(False)
        self.Bt_p2st3.setEnabled(False)
        self.Bt_p2st4.setEnabled(False)
        self.Pb_p2.setValue(0)

    ###################################part2###########################################
    def c4p2_FFT_IFFT_ALL(self , step=10):
        if self.current_deal_pic ==[]:
            self.showMessageBox()
            return
        if step>0 and step<5:#分解步骤显示
            if  self.Pb_p2.value() >= (step-1)*25:
                if step == 1:
                    self.p2_fshift =CH4_API.p2s1_FFT_shift(self.current_deal_pic)
                    self.Bt_p2st2.setEnabled(True)
                    self.Bt_p2st3.setEnabled(False)
                    self.Bt_p2st4.setEnabled(False)
                elif step == 2:
                    print(self.p2_fshift)
                    CH4_API.p2s2_amplitude_reconstruction(self.current_deal_pic,self.p2_fshift)
                    self.Bt_p2st3.setEnabled(True)
                    self.Bt_p2st4.setEnabled(False)
                elif step == 3:
                    CH4_API.p2s3_phase_reconstruction(self.current_deal_pic,self.p2_fshift)
                    self.Bt_p2st4.setEnabled(True)
                elif step == 4:
                    CH4_API.p2s4_double_reconstruction(self.current_deal_pic,self.p2_fshift)
                self.Pb_p2.setValue(step*25)
            else:
                self.orderwarning_Message()
                return
        else:#step==0:show_in_all,step0完整显示
            if step == 5:
                CH4_API.p2_cross_reconstruction(self.current_deal_pic, self.p2_fshift)
            else:
                CH4_API.p2tl_FFT_IFFT(self.current_deal_pic)
    #
    def c4p3_filter_all(self,step):
        if self.current_deal_pic ==[]:
            self.showMessageBox()
            return
        d_lp = self.SL_31.value()
        btorder_lp=self.SL_32.value()
        d_hp = self.SL_33.value()
        btorder_hp = self.SL_34.value()
        print(self.current_deal_pic)
        if step == 1:
            CH4_API.p3_show_ideal_low_pass(self.current_deal_pic,d_lp)
        elif step == 2:
            CH4_API.p3_show_butterworth_low_pass(self.current_deal_pic, d_lp, btorder_lp)
        elif step == 3:
            CH4_API.p3_show_gaussian_low_pass(self.current_deal_pic, d_lp)
        elif step == 4:
            CH4_API.p3_show_ideal_high_pass(self.current_deal_pic, d_hp)
        elif step == 5:
            CH4_API.p3_show_butterworth_high_pass(self.current_deal_pic,d_hp,btorder_hp)
        elif step == 6:
            CH4_API.p3_show_gaussian_high_pass(self.current_deal_pic, d_hp)
        elif step == 7:
            CH4_API.p3_show_all_filter(self.current_deal_pic, d_lp, btorder_lp,d_hp,btorder_hp)


##################################################异常处理机制
    def showMessageBox(self):
       res_3 = QMessageBox.warning(self, "警告", "请选择文件，再执行该操作！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def orderwarning_Message(self):
        res_3 = QMessageBox.warning(self, "警告", "请按步骤顺序，依次点击操作！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mych4window()
    ui.show()
    sys.exit(app.exec_())
