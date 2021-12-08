# pyuic5  mych9_qt.ui -o mych9_qt.py
from PyQt5 import QtWidgets,QtCore
from mych9_qt import Ui_Ch9_Window
from PyQt5.QtWidgets import QFileDialog
from mych9_api import CH9_API
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import numpy as np
import sip#为了释放无用控件资源

CH9_API=CH9_API()




class draw_pixal (QtWidgets.QPushButton):
    LeftPressed = QtCore.pyqtSignal (int, int)  # 定义信号
    keep_pressed = True

    def __init__(self, i, j, num, parent=None):
        super (draw_pixal, self).__init__ (parent)
        self.num = num
        self.i = i
        self.j = j
        self.state = 0  # 0,1,2
        self.setStyleSheet("background-color : rgb(75, 75, 75)")
        # self.setStyleSheet("::hover{background-color : rgb(255, 0, 0)}")
        # self.setMouseTracking(True)

    def mousePressEvent(self, e):  ##重载一下鼠标点击事件
        if e.buttons() == QtCore.Qt.LeftButton:
            self.state = 1 - self.state
            if self.state == 1:
                self.setStyleSheet("background-color : white")
                print(123)
            else:
                self.setStyleSheet("background-color : rgb(75, 75, 75)")
            self.LeftPressed.emit(self.i, self.j)
        elif e.buttons() == QtCore.Qt.RightButton:
            self.RightPressed.emit(self.i, self.j)



    # def mousePressEvent(self, e):  ##重载一下鼠标点击事件
    #     draw_pixal.keep_pressed = True
    #     print(draw_pixal.keep_pressed)
    #
    #
    #
    # def mouseReleaseEvent(self, e):  ##重载一下鼠标点击事件
    #     draw_pixal.keep_pressed = False
    #     print(draw_pixal.keep_pressed)

    # def enterEvent(self, a):
    #     if a.buttons() == QtCore.Qt.LeftButton:
    #         print("yes")
    #     if draw_pixal.keep_pressed  == True:
    #         self.state=1-self.state
    #         if self.state ==1:
    #             self.setStyleSheet("background-color : white")
    #             print(123)
    #         else:
    #             self.setStyleSheet("background-color : rgb(75, 75, 75)")
    #         self.LeftPressed.emit(self.i, self.j)

    # def mouseMoveEvent(self, e):
    #     print(1)
    #     if self.underMouse():
    #         print(self.i,self.j)
    #         if draw_pixal.keep_pressed == True:
    #             self.state=1-self.state
    #             if self.state ==1:
    #                 self.setStyleSheet("background-color : white")
    #                 print(123)
    #             else:
    #                 self.setStyleSheet("background-color : rgb(75, 75, 75)")
    #             self.LeftPressed.emit(self.i, self.j)
    #     else:
    #         print(self.i, self.j,"ok")
    #     print(00)
    #     if draw_pixal.keep_pressed  == True:
    #         self.state=1-self.state
    #         if self.state ==1:
    #             self.setStyleSheet("background-color : white")
    #             print(123)
    #         else:
    #             self.setStyleSheet("background-color : rgb(75, 75, 75)")
    #         self.LeftPressed.emit(self.i, self.j)
    #
    # def dropEvent(self, e):
    #     print(89)

class click_pixal (QtWidgets.QLabel):
    LeftPressed = QtCore.pyqtSignal (int, int)  # 定义信号
    RightPressed = QtCore.pyqtSignal (int, int)

    def __init__(self, i, j, num, parent=None):
        super (click_pixal, self).__init__ (parent)
        self.num = num
        self.i = i
        self.j = j
        self.state = 0  # 0,1,2
        self.setStyleSheet("background-color : rgb(75, 75, 75)")

        # self.setStyleSheet("::hover{background-color : red}")


    def mousePressEvent(self, e):  ##重载一下鼠标点击事件
        if e.buttons () == QtCore.Qt.LeftButton :
            self.state=1-self.state
            if self.state ==1:
                self.setStyleSheet("background-color : white")
                print(123)
            else:
                self.setStyleSheet("background-color : rgb(75, 75, 75)")
            self.LeftPressed.emit(self.i, self.j)
        elif e.buttons () == QtCore.Qt.RightButton:
            self.RightPressed.emit (self.i, self.j)


class mych9window(QtWidgets.QMainWindow, Ui_Ch9_Window):
    def  __init__ (self):
        super(mych9window, self).__init__()
        self.setupUi(self)
        self.sd_pic=0
        self.P12_pixmap.setMouseTracking(True)
        import os
        base_address = os.path.dirname(__file__)  # 获得当前所在绝对路径（不知道用户会把此程序发在哪，需要随时重新更新）
        self.setWindowIcon(QIcon(base_address+"/pic/logo.png"))
        # ##################ch9p1
        ###################
        self.sd_pic_path = ""
        self.P12savepicture.clicked.connect(self.P1_save_file)
        self.row=12
        self.column=15
        self.P12_mypixmap=[]#存储着P12的所有手绘像素格label
        self.P12_mypixmap = self.P1_create_pixmap(self.row, self.column)
        self.pixpicture=np.ones((self.row,self.column),np.uint8)*0#用于记录手绘像素图，以便后续传入处理，未选中的为黑色，选中的为白色
        ##################
        self.selectpicture.clicked.connect(self.P1_read_file)  # 打开
        self.Bt_p1clear.clicked.connect(self.P1_clear_pixmap)  # 打开
        # ######################P2
        self.anchor=(-1,-1)#默认未用右键设置锚点时，为无效值，传入函数时会被警告先选锚点
        self.kernel_map=[]
        self.kernel_picture=[] #记录绘制kernel的每一点数值
        self.CB_P2.currentIndexChanged.connect(lambda:self.P2_create_kernel(self.CB_P2.currentIndex()+2,self.CB_P2.currentIndex()+2))#根据选择的大小绘制kernel
        self.Bt_p2run.clicked.connect(self.P2_main_basic)
        self.P2_create_kernel(2,2)#初始化默认2*2kenel
        #########################p3
        self.Bt_p3holefill.clicked.connect(self.P3_main_holefill)
        self.SL_3.valueChanged.connect(self.LC_3.display)

    def P1_read_file(self):
        #选取文件
        self.sd_pic_path, filetype =QFileDialog.getOpenFileName(self, "打开文件", "D:/imagetest", "All Files(*);;Text Files(*.jpg)")
        if  self.sd_pic_path :
            print(self.sd_pic_path, filetype)
            self.LB_pic_1.setPixmap(QPixmap.fromImage(QImage(self.sd_pic_path)))
            self.sd_pic= cv2.imread(self.sd_pic_path)
            b, g, r = cv2.split(self.sd_pic)
            self.sd_pic = cv2.merge([r, g, b])
            height, width, channel= self.sd_pic.shape[0],self.sd_pic.shape[1],self.sd_pic.shape[2]
            self.information.setText("X  : " +str(width)  + " , Y : " + str(height) + " , channel  : " + str(channel))

    def P1_save_file(self):
       # 用全局变量保存所有需要保存的变量在内存中的值。
        file_name, filetype = QFileDialog.getSaveFileName(self,"文件保存","D:","Text Files (*.jpg)")#一定注意，此函数返回俩个参数
        if file_name:
            print(file_name)
            cv2.imwrite(file_name, self.pixpicture)


    def P1_create_pixmap(self,row,column):
        self.GL_PM_P12.setSpacing(0)#先清空，避免上次残余
        mypixmap = []
        for i in range(0, row):
            mypixmap.append([])
            for j in range(0, column):
                pixal = draw_pixal(i, j, 0, "")
                pixal.setMinimumSize(45, 45)
                # pixal.setFrameShape(QtWidgets.QFrame.WinPanel)
                # pixal.setFrameShadow(QtWidgets.QFrame.Raised)
                # pixal.setAlignment(Qt.AlignCenter)

                pixal.LeftPressed.connect(self.P1_LeftPressed_react)
                mypixmap[i].append(pixal)
                self.GL_PM_P12.addWidget(pixal, i, j)
        return mypixmap

    def P1_clear_pixmap(self):
        for i in range(0, len(self.P12_mypixmap)):
            for j in range(0, len(self.P12_mypixmap[0])):
                self.P12_mypixmap[i][j].state=0
                self.P12_mypixmap[i][j].setStyleSheet("background-color : rgb(75, 75, 75)")
                self.pixpicture[i][j]=0

    def P1_LeftPressed_react(self,i,j):
        self.pixpicture[i][j]=(self.P12_mypixmap[i][j].state)*255#点击代表选中，选中则为白色


    def P2_main_basic(self):
        print(self.anchor)
        if self.anchor==(-1,-1):
            self.anchorwarning_Message()
            return
        print(self.anchor)
        if self.check_p2.isChecked():#使用自定义的图片
            if self.tabWidget_P1.currentIndex()==0:#选择加载导入图片
                if self.sd_pic_path =='':
                    self.showMessageBox()
                    return
                else:
                    CH9_API.basic_operation(self.kernel_picture, self.anchor,self.sd_pic)#使用加载好的图
            elif self.tabWidget_P1.currentIndex()==1:#选择使用手绘像素图
                CH9_API.basic_operation(self.kernel_picture, self.anchor, self.pixpicture)#使用手绘图
        else:
            CH9_API.basic_operation(self.kernel_picture, self.anchor)#不传入图像，使得其调用默认预置图像

    def P2_clear_kernel(self):
        for i in range(0, len(self.kernel_map)):
            for j in range(0, len(self.kernel_map[0])):
                self.kernel_map[i][j].state=0
                self.kernel_map[i][j].setStyleSheet("background-color : rgb(75, 75, 75)")
                self.kernel_picture[i][j]=0#清空时候应该涂黑
                self.GL_KL.removeWidget(self.kernel_map[i][j])
                sip.delete(self.kernel_map[i][j])
        self.kernel_map = []
        self.kernel_picture = []  # 彻底清空

    def P2_create_kernel(self, row, column):
        # self.GL_KL.setSpacing(0)  # 先清空，避免上次残余
        self.P2_clear_kernel()
        self.anchor = (-1, -1)#没回都要重新初始化锚点位置
        self.kernel_picture=np.zeros((row,column),np.uint8)#初始化为全黑，代表没选，选中则变白色
        for i in range(0, row):
            self.kernel_map.append([])
            for j in range(0, column):
                pixal = click_pixal(i, j, 0, "")
                pixal.setMinimumSize(45, 45)
                pixal.setFrameShape(QtWidgets.QFrame.WinPanel)
                pixal.setFrameShadow(QtWidgets.QFrame.Raised)
                pixal.setAlignment(Qt.AlignCenter)
                pixal.LeftPressed.connect(self.P2_LeftPressed_react)
                pixal.RightPressed.connect(self.P2_RightPressed_react)
                self.kernel_map[i].append(pixal)
                self.GL_KL.addWidget(pixal, i, j)

    def P2_LeftPressed_react(self, i, j):
        self.kernel_picture[i][j] = (self.kernel_map[i][j].state) * 255#选中时由黑到白
        if (self.anchor[0],self.anchor[1])==(i,j):
            self.anchor=(-1,-1)

    def P2_RightPressed_react(self,i,j):
        x = self.anchor[0]
        y = self.anchor[1]
        if   (x,y)!=(-1,-1):
            self.kernel_map[x][y].setStyleSheet("background-color : white")#上一个
            self.kernel_picture[x][y]=255#被剥夺了锚点的位置应该变白
        self.anchor=(i,j)#更新选中的锚点坐标
        self.kernel_map[i][j].state = 1
        self.kernel_picture[i][j] = 255  # 被剥夺了锚点的位置应该变白
        self.kernel_map[i][j].setStyleSheet("background-color : blue")  # 新锚点涂成灰色

    def P3_main_holefill(self):
        if self.anchor == (-1, -1):
            self.drawkernelwarning_Message()
            return
        iteration = self.SL_3.value()#读取迭代次数
        if self.check_p3.isChecked():#使用自定义的图片
            if self.tabWidget_P1.currentIndex()==0:#选择加载导入图片
                if self.sd_pic_path =='':
                    self.showMessageBox()
                    return
                else:
                    CH9_API.hole_filling(self.kernel_picture,self.anchor,iteration,self.sd_pic)#使用加载好的图
            elif self.tabWidget_P1.currentIndex()==1:#选择使用手绘像素图
                CH9_API.hole_filling(self.kernel_picture,self.anchor,iteration,self.pixpicture)#使用手绘图
        else:
            CH9_API.hole_filling(self.kernel_picture,self.anchor,iteration)#不传入图像，使得其调用默认预置图像


##################################################异常处理机制
    def showMessageBox(self):
       res_3 = QMessageBox.warning(self, "警告", "请选择文件，再执行该操作！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def orderwarning_Message(self):
        res_3 = QMessageBox.warning(self, "警告", "请按步骤顺序，依次点击操作！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def anchorwarning_Message(self):
        res_3 = QMessageBox.warning(self, "警告", "请先用右键为结构元指定锚点位置！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def drawkernelwarning_Message(self):
        res_3 = QMessageBox.warning(self, "警告", "请先在PART2中绘制结构元和锚点！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mych9window()
    ui.show()
    sys.exit(app.exec_())
