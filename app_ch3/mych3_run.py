# pyuic5  wide_mych3_qt.ui -o mych3_qt.py

from PyQt5 import QtWidgets
from mych3_qt import Ui_Ch3_Window
from PyQt5.QtWidgets import QFileDialog
from mych3_api import CH3_API
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
CH3_API=CH3_API()
import pyqtgraph as pg
import numpy as np
import sip#为了释放无用控件资源


class mych3window(QtWidgets.QMainWindow, Ui_Ch3_Window):
    def  __init__ (self):
        super(mych3window, self).__init__()
        self.setupUi(self)
        import os
        base_address = os.path.dirname(__file__)  # 获得当前所在绝对路径（不知道用户会把此程序发在哪，需要随时重新更新）
        self.setWindowIcon(QIcon(base_address + "/pic/logo.png"))
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 无边框，置顶
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 透明背景色

        ################预存图片：opencv格式#############
        self.sd_pic_path = ""
        self.sd_pic=[]##用于存自定义图片
        import os
        base_address = os.path.dirname(__file__)  # 获得当前所在绝对路径（不知道用户会把此程序发在哪，需要随时重新更新）
        self.pic_p2p3  =  cv2.imread(base_address+"/pic/boat.jpg")
        self.pic_p4 = cv2.imread(base_address+"/pic/lena.jpg")
        self.current_deal_pic = []
        self.c3p1_show_pic(0)#刚打开时，默认显示

        ###################ch3p1#####################
        self.selectpicture.clicked.connect(self.c3p1_read_file)  # 打开
        self.selectpicture.setEnabled(False)#默认是使用默认图片，所以加载图片按钮为冻结状态,当激光按钮选择自定义图片时，将解冻
        self.RB_P1_default.toggled.connect(lambda: self.c3p1_show_pic(self.tabWidget.currentIndex()))
        self.tabWidget.currentChanged.connect(lambda: self.c3p1_show_pic(self.tabWidget.currentIndex()))
        ###################ch3p2######################################
        self.Bt_p2_run.clicked.connect(lambda:self.c3p2_main(self.CB_p2_select.currentIndex()))
        self.SL_p2_log.valueChanged.connect(self.LC_p2_log.display)
        self.SL_p2_log.valueChanged.connect(lambda: self.c3p2_draw_chart(1))
        self.sBox_p2.valueChanged.connect(lambda: self.c3p2_draw_chart(2))
        self.PX1.valueChanged.connect(lambda: self.c3p2_draw_chart(3))
        self.PX2.valueChanged.connect(lambda: self.c3p2_draw_chart(3))
        self.PY1.valueChanged.connect(lambda: self.c3p2_draw_chart(3))
        self.PY2.valueChanged.connect(lambda: self.c3p2_draw_chart(3))
        self.CB_p2_select.currentIndexChanged.connect(lambda: self.c3p2_draw_chart(self.CB_p2_select.currentIndex()))
        self.chart = None
        self.c3p2_draw_chart(0)

        ###################ch3p3#################
        self.sd_ref_path = ""
        self.sd_ref_pic = []  ##用于存自定义直方图匹配的参考图片
        self.pic_p3_ref = cv2.imread(base_address+'/pic/room.jpg')#默认的参考图像
        self.current_ref_pic = []#真正被选择用于参考的图像
        self.Bt_p3_equal.clicked.connect(lambda:self.c3p3_main(0))
        self.Bt_p3_match.clicked.connect(lambda:self.c3p3_main(1))
        self.Bt_p3_selectpic.clicked.connect(self.c3p3_read_file)
        self.RB_P3_default.toggled.connect(self.c3p3_show_pic)#将单选按钮和图像切换函数相绑定
        self.c3p3_show_pic()
        ##############ch3p4#######################
        self.kernel_component=[[self.sBox_11,self.sBox_12,self.sBox_13],[self.sBox_21,self.sBox_22,self.sBox_23],[self.sBox_31,self.sBox_32,self.sBox_33]]
        self.Bt_p4_run.clicked.connect(self.c3p4_main)
    ##################################tool_functions#######################################
    def cvimg_to_qtimg(self,cvimg):#把CV格式图片转换成QImage格式
        height, width, depth = cvimg.shape
        cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
        cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)
        return cvimg

    ###################################part1###########################################

    def c3p1_read_file(self):
        #选取文件
        self.sd_pic_path, filetype =QFileDialog.getOpenFileName(self, "打开文件", "D:/imagetest", "All Files(*);;Text Files(*.jpg)")
        if  self.sd_pic_path :
            self.sd_pic= cv2.imread(self.sd_pic_path)
            self.c3p1_show_pic()

    def c3p1_show_pic(self,page=0):
        if self.RB_P1_default.isChecked()==True:##激光按钮选中了使用默认图片
            self.selectpicture.setEnabled(False)
            if page == 0:#part2对应TabWidget的page1
                self.current_deal_pic = self.pic_p2p3
            elif page== 1 :#part3对应TabWidget的page2
                self.current_deal_pic = self.pic_p2p3
            elif page == 2:
                self.current_deal_pic = self.pic_p4
        else :###激光按钮选中了使用自定义图片
            self.selectpicture.setEnabled(True)
            self.current_deal_pic = self.sd_pic

        if self.current_deal_pic == []:#未加载图片
            self.LB_pic_1.setPixmap(QPixmap(""))
            self.information.setText("X  : " + "  " + " , Y : " + "  " + " , channel  : " + "  ")
        else:
            QImage_pic = self.cvimg_to_qtimg(self.current_deal_pic)#把用opencv读进来的图像转换成qt里的格式，不然无法在UI里正常显示
            self.LB_pic_1.setPixmap(QPixmap.fromImage(QImage_pic))
            height, width, channel = self.current_deal_pic.shape[0], self.current_deal_pic.shape[1], self.current_deal_pic.shape[2]
            self.information.setText("X  : " +str(width)  + " , Y : " + str(height) + " , channel  : " + str(channel))


    ###################################part2 灰度变换###########################################
    def c3p2_main(self,step):
        if self.current_deal_pic ==[]:
            self.showMessageBox()
            return
        C_log = self.SL_p2_log.value()
        L_power =self.sBox_p2.value()

        if step == 0:
            CH3_API.p2_Opposite_Tranform(self.current_deal_pic)
        elif step == 1:
            CH3_API.p2_log_Tranform(self.current_deal_pic, C_log)
        elif step == 2:
            CH3_API.p2_Power_Transform(self.current_deal_pic,L_power)
        elif step == 3:
            if self.PX1.value()<self.PX2.value():
                point_x = np.array([self.PX1.value(), self.PX2.value()])
                point_y = np.array([self.PY1.value(), self.PY2.value()])
            else:
                point_x = np.array([self.PX2.value(), self.PX1.value()])
                point_y = np.array([self.PY2.value(), self.PY1.value()])
            CH3_API.p2_FenDuan_Transform(self.current_deal_pic,point_x,point_y )

    def c3p2_draw_chart(self,step):
        if self.chart != None:
            self.VL_p2_chart.removeWidget(self.chart)
            sip.delete(self.chart)
        x_axis  = np.linspace(0, 255, 255)     #给出分段函数图中该段中 X的范围，并规定点的数量
        y_axis = np.array([])
        if step == 0:
            self.SL_p2_log.setEnabled(False)
            self.sBox_p2.setEnabled(False)
            y_axis = 255-x_axis
        elif step == 1:#对数
            self.SL_p2_log.setEnabled(True)
            self.sBox_p2.setEnabled(False)
            y_axis = np.log(1 + x_axis)*self.SL_p2_log.value()
        elif step == 2:
            self.SL_p2_log.setEnabled(False)
            self.sBox_p2.setEnabled(True)
            y_axis = np.power(x_axis,self.sBox_p2.value())
        elif step == 3:
            self.SL_p2_log.setEnabled(False)
            self.sBox_p2.setEnabled(False)
            if self.PX1.value()<self.PX2.value():
                point_x = np.array([self.PX1.value(), self.PX2.value()])
                point_y = np.array([self.PY1.value(), self.PY2.value()])
            else:
                point_x = np.array([self.PX2.value(), self.PX1.value()])
                point_y = np.array([self.PY2.value(), self.PY1.value()])
            x1_axis=np.linspace(0, point_x[0], point_x[0])
            x2_axis=np.linspace(point_x[0], point_x[1], point_x[1]-point_x[0])
            x3_axis=np.linspace(point_x[1],255, 255-point_x[1])
            y1_axis = (point_y[0]/point_x[0])*x1_axis
            y2_axis = [((point_y[1]-point_y[0])/(point_x[1]-point_x[0]))*(x2-point_x[0])+point_y[0]  for x2 in x2_axis]
            y3_axis = [((255-point_y[1])/(255-point_x[1]))*(x3-point_x[1])+point_y[1] for x3 in x3_axis ]
            y_axis = np.append(y1_axis,y2_axis)
            y_axis = np.append(y_axis,y3_axis)


        self.chart =pg.PlotWidget()
        self.chart.plot(x_axis,y_axis)
        self.chart.showGrid(x=True, y=True)
        self.VL_p2_chart.addWidget(self.chart)

    ###################################part3_直方图处理################################
    def c3p3_main(self,step):
        if step == 0:
            CH3_API.p3_Hist_Equalize(self.current_deal_pic)
        elif step == 1:
            CH3_API.p3_Hist_Match(self.current_deal_pic , self.current_ref_pic)
    def c3p3_read_file(self):
        #选取文件
        self.sd_ref_path, filetype =QFileDialog.getOpenFileName(self, "打开文件", "D:/imagetest", "All Files(*);;Text Files(*.jpg)")
        if  self.sd_ref_path :
            self.sd_ref_pic= cv2.imread(self.sd_ref_path)
            self.c3p3_show_pic()

    def c3p3_show_pic(self):
        if self.RB_P3_default.isChecked()==True:##激光按钮选中了使用默认图片
                self.current_ref_pic = self.pic_p3_ref
                self.Bt_p3_selectpic.setEnabled(False)
        else :###激光按钮选中了使用自定义图片
            self.Bt_p3_selectpic.setEnabled(True)
            self.current_ref_pic = self.sd_ref_pic

        if self.current_ref_pic == []:#未加载图片
            self.LB_p3_pic.setPixmap(QPixmap(""))

        else:
            QImage_pic = self.cvimg_to_qtimg(self.current_ref_pic)
            self.LB_p3_pic.setPixmap(QPixmap.fromImage(QImage_pic))


    #######################################part4#######################################
    def c3p4_main(self):
        if self.current_deal_pic ==[]:
            self.showMessageBox()
            return

        if self.RB_P4_self.isChecked()==True:#是否选择自定义卷积滤波
            tmp_kernel=self.kernel_read()
            CH3_API.p4_convolutional_filter(self.current_deal_pic,tmp_kernel)
        elif self.RB_P4_smooth.isChecked() == True:
            id = self.CB_p4_smo.currentIndex()
            if id == 0:
                CH3_API.p4_smooth_boxfilter(self.current_deal_pic)
            elif id == 1:
                CH3_API.p4_smooth_weightfilter(self.current_deal_pic)
            elif id ==2:
                CH3_API.p4_smooth_middlefilter(self.current_deal_pic)
        elif self.RB_P4_sharp.isChecked() == True:
            id = self.CB_p4_sha.currentIndex()
            if id == 0:
                CH3_API.p4_sharpen_Roberts(self.current_deal_pic)
            elif id == 1:
                CH3_API.p4_sharpen_Prewitt(self.current_deal_pic)
            elif id == 2:
                CH3_API.p4_sharpen_Sobel(self.current_deal_pic)
            elif id == 3:
                CH3_API.p4_sharpen_Laplace(self.current_deal_pic)
            elif id == 4:
                CH3_API.p4_edge_canny(self.current_deal_pic)


    def kernel_read(self):
        kernel=[]
        for i in range(0,3) :
            kernel.append([])
            for j in range(0,3):
                kernel[i].append(self.kernel_component[i][j].value())
        return kernel
##################################################异常处理机制
    def showMessageBox(self):
       res_3 = QMessageBox.warning(self, "警告", "请选择文件，再执行该操作！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def orderwarning_Message(self):
        res_3 = QMessageBox.warning(self, "警告", "请按步骤顺序，依次点击操作！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


# if __name__=="__main__":

def start():
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mych3window()
    ui.show()
    #
    sys.exit(app.exec_())
# if __name__=="__main__":
#     start()