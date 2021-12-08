# pyuic5  wide_mych5_qt.ui -o mych5_qt.py
from PyQt5 import QtWidgets
from mych5_qt import Ui_Ch5_Window
from PyQt5.QtWidgets import QFileDialog
from mych5_api import CH5_API
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
CH5_API=CH5_API()



class mych5window(QtWidgets.QMainWindow, Ui_Ch5_Window):
    def  __init__ (self):
        super(mych5window, self).__init__()
        self.setupUi(self)
        import os
        base_address = os.path.dirname(__file__)  # 获得当前所在绝对路径（不知道用户会把此程序发在哪，需要随时重新更新）
        self.setWindowIcon(QIcon(base_address+"/pic/logo.png"))
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 无边框，置顶
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 透明背景色

        ################预存图片：opencv格式#############
        self.sd_pic_path = ""
        self.sd_pic=[]##用于存自定义图片
        self.pic_p2p3  =  cv2.imread(base_address+"/pic/boat.jpg")
        self.current_deal_pic = []
        self.c5p1_show_pic(0)#刚打开时，默认显示

        ###################ch5p1#####################
        self.selectpicture.clicked.connect(self.c5p1_read_file)  # 打开
        self.selectpicture.setEnabled(False)#默认是使用默认图片，所以加载图片按钮为冻结状态,当激光按钮选择自定义图片时，将解冻
        self.RB_P1_default.toggled.connect(lambda: self.c5p1_show_pic())
        ###################ch5p2######################################
        self.Bt_p2_fuyuan.setEnabled(False)#点击退化之后才能解冻
        self.Bt_p2_tuihua.clicked.connect(lambda:self.c5p2_main(0,self.CB_p2_sel_noise.currentIndex()))
        self.Bt_p2_fuyuan.clicked.connect(lambda: self.c5p2_main(1,self.CB_p2_sel_filter.currentIndex()))
        self.SL_p2_percentage.valueChanged.connect(self.LC_p2_percentage.display)
        self.SL_p2_mean.valueChanged.connect(self.LC_p2_mean.display)
        ###################ch5p3#################
        self.Bt_p3_fuyuan.setEnabled(False)#点击退化之后才能解冻
        self.Bt_p3_tuihua.clicked.connect(lambda:self.c5p3_main(0,0))
        self.Bt_p3_fuyuan.clicked.connect(lambda: self.c5p3_main(1, self.CB_p3_sel_filter.currentIndex()))
        self.SL_p3_period.valueChanged.connect(self.LC_p3_period.display)
        self.SL_p3_amplitude.valueChanged.connect(self.LC_p3_amplitude.display)
        self.SL_p3_filter_diode.valueChanged.connect(self.LC_p3_diode.display)
        self.SL_p3_filter_coordinateX.valueChanged.connect(self.LC_p3_coordinateX.display)
        self.SL_p3_filter_coordinateY.valueChanged.connect(self.LC_p3_coordinateY.display)

    ##################################tool_functions#######################################
    def cvimg_to_qtimg(self,cvimg):#把CV格式图片转换成QImage格式
        height, width, depth = cvimg.shape
        cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
        cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)
        return cvimg

    ###################################part1###########################################

    def c5p1_read_file(self):
        #选取文件
        self.sd_pic_path, filetype =QFileDialog.getOpenFileName(self, "打开文件", "D:/imagetest", "All Files(*);;Text Files(*.jpg)")
        if  self.sd_pic_path :
            self.sd_pic= cv2.imread(self.sd_pic_path)
            self.c5p1_show_pic()

    def c5p1_show_pic(self,page=0):
        if self.RB_P1_default.isChecked()==True:##激光按钮选中了使用默认图片
            self.selectpicture.setEnabled(False)
            self.current_deal_pic = self.pic_p2p3
        else :###激光按钮选中了使用自定义图片
            self.selectpicture.setEnabled(True)
            self.current_deal_pic = self.sd_pic

        if self.current_deal_pic == []:#未加载图片
            self.LB_pic_1.setPixmap(QPixmap(""))
            self.information.setText("X  : " + "  " + " , Y : " + "  " + " , channel  : " + "  ")
        else:
            QImage_pic = self.cvimg_to_qtimg(self.current_deal_pic)
            self.LB_pic_1.setPixmap(QPixmap.fromImage(QImage_pic))
            height, width, channel = self.current_deal_pic.shape[0], self.current_deal_pic.shape[1], self.current_deal_pic.shape[2]
            self.information.setText("X  : " +str(width)  + " , Y : " + str(height) + " , channel  : " + str(channel))


    ###################################part2 空域滤波###########################################
    def c5p2_main(self,step,id):
        if self.current_deal_pic ==[]:
            self.showMessageBox()
            return
        percentage = float(self.SL_p2_percentage.value())/100#椒盐噪声信噪比
        mean = self.SL_p2_mean.value()#高斯噪声均值

        if step == 0:#退化
            if id <3:#0,1,2分别为 椒噪声，盐噪声，椒盐噪声
                CH5_API.p2_additive_noise_pepper_salt(self.current_deal_pic,percentage,id)
            elif id == 3:
                CH5_API.p2_additive_noise_gasuss(self.current_deal_pic, mean)
            self.Bt_p2_fuyuan.setEnabled(True)  # 点击退化之后才能解冻
        if step == 1:#复原
            if id == 0:
                CH5_API.p2_mean_filter(CH5_API.additive_noise_pic)
            elif id == 1:
                CH5_API.p2_Harmonic_filter(CH5_API.additive_noise_pic)
            elif id == 2:
                CH5_API.p2_inverse_Harmonic(CH5_API.additive_noise_pic)
            elif id == 3:
                CH5_API.p2_statistic_sort_filter(CH5_API.additive_noise_pic)
            elif id == 4:
                CH5_API.p2_adaptive_median_filter(CH5_API.additive_noise_pic)


    ###################################part3_频率域滤波################################
    def c5p3_main(self, step, id=0):
        if self.current_deal_pic == []:
            self.showMessageBox()
            return
        amplitude = self.SL_p3_amplitude.value()  # 椒盐噪声信噪比
        period = self.SL_p3_period.value()  # 高斯噪声均值
        diode =self.SL_p3_filter_diode.value()
        coordinate_X=self.SL_p3_filter_coordinateX.value()
        coordinate_Y=self.SL_p3_filter_coordinateY.value()
        if step == 0:  # 退化
            CH5_API.p3_periodic_noise(self.current_deal_pic,period,amplitude)
            self.Bt_p3_fuyuan.setEnabled(True)
        if step == 1:  # 复原
            if id == 0:
                CH5_API.p3_band_stop_filter(CH5_API.periodic_noise_pic,diode)
            elif id == 1:
                CH5_API.p3_notch_filter(CH5_API.periodic_noise_pic,coordinate_X,coordinate_Y,diode)

##################################################异常处理机制###########################
    def showMessageBox(self):
       res_3 = QMessageBox.warning(self, "警告", "请选择文件，再执行该操作！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def orderwarning_Message(self):
        res_3 = QMessageBox.warning(self, "警告", "请按步骤顺序，依次点击操作！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mych5window()
    ui.show()
    #
    sys.exit(app.exec_())
