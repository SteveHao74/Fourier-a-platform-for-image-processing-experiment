# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageprocess.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1093, 853)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Magnify = QtWidgets.QToolButton(self.centralwidget)
        self.Magnify.setObjectName("Magnify")
        self.gridLayout.addWidget(self.Magnify, 2, 0, 1, 1)
        self.Next = QtWidgets.QToolButton(self.centralwidget)
        self.Next.setObjectName("Next")
        self.gridLayout.addWidget(self.Next, 1, 2, 1, 1)
        self.R90CCW = QtWidgets.QToolButton(self.centralwidget)
        self.R90CCW.setObjectName("R90CCW")
        self.gridLayout.addWidget(self.R90CCW, 2, 2, 1, 1)
        self.Back = QtWidgets.QToolButton(self.centralwidget)
        self.Back.setObjectName("Back")
        self.gridLayout.addWidget(self.Back, 1, 1, 1, 1)
        self.Exit = QtWidgets.QToolButton(self.centralwidget)
        self.Exit.setAutoFillBackground(False)
        self.Exit.setObjectName("Exit")
        self.gridLayout.addWidget(self.Exit, 2, 3, 1, 1)
        self.Mark = QtWidgets.QToolButton(self.centralwidget)
        self.Mark.setObjectName("Mark")
        self.gridLayout.addWidget(self.Mark, 1, 3, 1, 1)
        self.R90CW = QtWidgets.QToolButton(self.centralwidget)
        self.R90CW.setObjectName("R90CW")
        self.gridLayout.addWidget(self.R90CW, 2, 1, 1, 1)
        self.Scan = QtWidgets.QToolButton(self.centralwidget)
        self.Scan.setEnabled(True)
        self.Scan.setObjectName("Scan")
        self.gridLayout.addWidget(self.Scan, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 551, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 41))
        self.label.setObjectName("label")
        self.label_pic = QtWidgets.QLabel(self.frame)
        self.label_pic.setGeometry(QtCore.QRect(60, 100, 631, 591))
        self.label_pic.setText("")
        self.label_pic.setObjectName("label_pic")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1093, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName("menu_6")
        self.menu_7 = QtWidgets.QMenu(self.menubar)
        self.menu_7.setObjectName("menu_7")
        self.menu_8 = QtWidgets.QMenu(self.menubar)
        self.menu_8.setObjectName("menu_8")
        self.menu_9 = QtWidgets.QMenu(self.menubar)
        self.menu_9.setObjectName("menu_9")
        self.menu_10 = QtWidgets.QMenu(self.menubar)
        self.menu_10.setObjectName("menu_10")
        self.menu_11 = QtWidgets.QMenu(self.menubar)
        self.menu_11.setObjectName("menu_11")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open = QtWidgets.QAction(MainWindow)
        self.open.setCheckable(False)
        self.open.setChecked(False)
        self.open.setEnabled(True)
        self.open.setObjectName("open")
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setCheckable(False)
        self.save.setObjectName("save")
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setCheckable(True)
        self.exit.setObjectName("exit")
        self.zoomin = QtWidgets.QAction(MainWindow)
        self.zoomin.setCheckable(False)
        self.zoomin.setObjectName("zoomin")
        self.zoomout = QtWidgets.QAction(MainWindow)
        self.zoomout.setCheckable(False)
        self.zoomout.setObjectName("zoomout")
        self.gray = QtWidgets.QAction(MainWindow)
        self.gray.setCheckable(False)
        self.gray.setObjectName("gray")
        self.light = QtWidgets.QAction(MainWindow)
        self.light.setCheckable(False)
        self.light.setObjectName("light")
        self.rotate = QtWidgets.QAction(MainWindow)
        self.rotate.setCheckable(False)
        self.rotate.setObjectName("rotate")
        self.screenshots = QtWidgets.QAction(MainWindow)
        self.screenshots.setCheckable(False)
        self.screenshots.setObjectName("screenshots")
        self.FFT = QtWidgets.QAction(MainWindow)
        self.FFT.setCheckable(False)
        self.FFT.setObjectName("FFT")
        self.cos = QtWidgets.QAction(MainWindow)
        self.cos.setCheckable(False)
        self.cos.setObjectName("cos")
        self.Radon = QtWidgets.QAction(MainWindow)
        self.Radon.setCheckable(False)
        self.Radon.setObjectName("Radon")
        self.gauss = QtWidgets.QAction(MainWindow)
        self.gauss.setCheckable(False)
        self.gauss.setObjectName("gauss")
        self.sault = QtWidgets.QAction(MainWindow)
        self.sault.setCheckable(False)
        self.sault.setObjectName("sault")
        self.spot = QtWidgets.QAction(MainWindow)
        self.spot.setCheckable(False)
        self.spot.setObjectName("spot")
        self.poisson = QtWidgets.QAction(MainWindow)
        self.poisson.setCheckable(False)
        self.poisson.setObjectName("poisson")
        self.highpass = QtWidgets.QAction(MainWindow)
        self.highpass.setCheckable(False)
        self.highpass.setObjectName("highpass")
        self.lowpass = QtWidgets.QAction(MainWindow)
        self.lowpass.setCheckable(False)
        self.lowpass.setObjectName("lowpass")
        self.linearsmooth = QtWidgets.QAction(MainWindow)
        self.linearsmooth.setCheckable(False)
        self.linearsmooth.setObjectName("linearsmooth")
        self.nonlinear = QtWidgets.QAction(MainWindow)
        self.nonlinear.setCheckable(False)
        self.nonlinear.setObjectName("nonlinear")
        self.linearsharpen = QtWidgets.QAction(MainWindow)
        self.linearsharpen.setCheckable(False)
        self.linearsharpen.setObjectName("linearsharpen")
        self.nonlinearsharp = QtWidgets.QAction(MainWindow)
        self.nonlinearsharp.setCheckable(False)
        self.nonlinearsharp.setObjectName("nonlinearsharp")
        self.Rhistogram = QtWidgets.QAction(MainWindow)
        self.Rhistogram.setCheckable(False)
        self.Rhistogram.setObjectName("Rhistogram")
        self.Ghistogram = QtWidgets.QAction(MainWindow)
        self.Ghistogram.setCheckable(False)
        self.Ghistogram.setObjectName("Ghistogram")
        self.Bhistogram = QtWidgets.QAction(MainWindow)
        self.Bhistogram.setCheckable(False)
        self.Bhistogram.setObjectName("Bhistogram")
        self.pseenhance = QtWidgets.QAction(MainWindow)
        self.pseenhance.setCheckable(False)
        self.pseenhance.setObjectName("pseenhance")
        self.realenhance = QtWidgets.QAction(MainWindow)
        self.realenhance.setCheckable(False)
        self.realenhance.setObjectName("realenhance")
        self.histogramequal = QtWidgets.QAction(MainWindow)
        self.histogramequal.setCheckable(False)
        self.histogramequal.setObjectName("histogramequal")
        self.NTSC = QtWidgets.QAction(MainWindow)
        self.NTSC.setCheckable(False)
        self.NTSC.setObjectName("NTSC")
        self.YCbCr = QtWidgets.QAction(MainWindow)
        self.YCbCr.setCheckable(False)
        self.YCbCr.setObjectName("YCbCr")
        self.HSV = QtWidgets.QAction(MainWindow)
        self.HSV.setCheckable(False)
        self.HSV.setObjectName("HSV")
        self.divide = QtWidgets.QAction(MainWindow)
        self.divide.setCheckable(False)
        self.divide.setObjectName("divide")
        self.morphology = QtWidgets.QAction(MainWindow)
        self.morphology.setCheckable(False)
        self.morphology.setObjectName("morphology")
        self.feature = QtWidgets.QAction(MainWindow)
        self.feature.setCheckable(False)
        self.feature.setObjectName("feature")
        self.imageclassify = QtWidgets.QAction(MainWindow)
        self.imageclassify.setCheckable(False)
        self.imageclassify.setObjectName("imageclassify")
        self.menu.addAction(self.open)
        self.menu.addAction(self.save)
        self.menu.addAction(self.exit)
        self.menu_2.addAction(self.zoomin)
        self.menu_2.addAction(self.zoomout)
        self.menu_2.addAction(self.gray)
        self.menu_2.addAction(self.light)
        self.menu_2.addAction(self.rotate)
        self.menu_2.addAction(self.screenshots)
        self.menu_3.addAction(self.FFT)
        self.menu_3.addAction(self.cos)
        self.menu_3.addAction(self.Radon)
        self.menu_4.addAction(self.gauss)
        self.menu_4.addAction(self.sault)
        self.menu_4.addAction(self.spot)
        self.menu_4.addAction(self.poisson)
        self.menu_5.addAction(self.highpass)
        self.menu_5.addAction(self.lowpass)
        self.menu_5.addAction(self.linearsmooth)
        self.menu_5.addAction(self.nonlinear)
        self.menu_5.addAction(self.linearsharpen)
        self.menu_5.addAction(self.nonlinearsharp)
        self.menu_6.addAction(self.Rhistogram)
        self.menu_6.addAction(self.Ghistogram)
        self.menu_6.addAction(self.Bhistogram)
        self.menu_7.addAction(self.pseenhance)
        self.menu_7.addAction(self.realenhance)
        self.menu_7.addAction(self.histogramequal)
        self.menu_7.addAction(self.NTSC)
        self.menu_7.addAction(self.YCbCr)
        self.menu_7.addAction(self.HSV)
        self.menu_8.addAction(self.divide)
        self.menu_9.addAction(self.morphology)
        self.menu_10.addAction(self.feature)
        self.menu_11.addAction(self.imageclassify)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_7.menuAction())
        self.menubar.addAction(self.menu_8.menuAction())
        self.menubar.addAction(self.menu_9.menuAction())
        self.menubar.addAction(self.menu_10.menuAction())
        self.menubar.addAction(self.menu_11.menuAction())

        self.retranslateUi(MainWindow)
        self.Exit.clicked.connect(MainWindow.close)
        self.exit.changed.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SASS_第二章"))
        self.Magnify.setText(_translate("MainWindow", "Magnify"))
        self.Next.setText(_translate("MainWindow", "下一张"))
        self.R90CCW.setText(_translate("MainWindow", "R90°CCW"))
        self.Back.setText(_translate("MainWindow", "上一张"))
        self.Exit.setText(_translate("MainWindow", "退出"))
        self.Mark.setText(_translate("MainWindow", "添加水印"))
        self.R90CW.setText(_translate("MainWindow", "R90°CW"))
        self.Scan.setText(_translate("MainWindow", "浏览"))
        self.label.setText(_translate("MainWindow", "图片文件地址："))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "变换"))
        self.menu_4.setTitle(_translate("MainWindow", "噪声"))
        self.menu_5.setTitle(_translate("MainWindow", "滤波"))
        self.menu_6.setTitle(_translate("MainWindow", "直方图统计"))
        self.menu_7.setTitle(_translate("MainWindow", "图像增强"))
        self.menu_8.setTitle(_translate("MainWindow", "阈值分割"))
        self.menu_9.setTitle(_translate("MainWindow", "形态学处理"))
        self.menu_10.setTitle(_translate("MainWindow", "特征提取"))
        self.menu_11.setTitle(_translate("MainWindow", "图像分类与识别"))
        self.open.setText(_translate("MainWindow", "打开"))
        self.save.setText(_translate("MainWindow", "保存"))
        self.exit.setText(_translate("MainWindow", "退出"))
        self.zoomin.setText(_translate("MainWindow", "放大"))
        self.zoomout.setText(_translate("MainWindow", "缩小"))
        self.gray.setText(_translate("MainWindow", "灰度"))
        self.light.setText(_translate("MainWindow", "亮度"))
        self.rotate.setText(_translate("MainWindow", "旋转"))
        self.screenshots.setText(_translate("MainWindow", "截图"))
        self.FFT.setText(_translate("MainWindow", "傅里叶变换FFT"))
        self.cos.setText(_translate("MainWindow", "离散余弦变换"))
        self.Radon.setText(_translate("MainWindow", "Radon变换"))
        self.gauss.setText(_translate("MainWindow", "高斯噪声"))
        self.sault.setText(_translate("MainWindow", "椒盐噪声"))
        self.spot.setText(_translate("MainWindow", "斑点噪声"))
        self.poisson.setText(_translate("MainWindow", "泊松噪声"))
        self.highpass.setText(_translate("MainWindow", "高通滤波"))
        self.lowpass.setText(_translate("MainWindow", "低通滤波"))
        self.linearsmooth.setText(_translate("MainWindow", "平滑滤波（线性）"))
        self.nonlinear.setText(_translate("MainWindow", "平滑滤波（非线性）"))
        self.linearsharpen.setText(_translate("MainWindow", "锐化滤波（线性）"))
        self.nonlinearsharp.setText(_translate("MainWindow", "锐化滤波（非线性）"))
        self.Rhistogram.setText(_translate("MainWindow", "R直方图"))
        self.Ghistogram.setText(_translate("MainWindow", "G直方图"))
        self.Bhistogram.setText(_translate("MainWindow", "B直方图"))
        self.pseenhance.setText(_translate("MainWindow", "伪彩色增强"))
        self.realenhance.setText(_translate("MainWindow", "真彩色增强"))
        self.histogramequal.setText(_translate("MainWindow", "直方图均衡"))
        self.NTSC.setText(_translate("MainWindow", "NTSC颜色模型"))
        self.YCbCr.setText(_translate("MainWindow", "YCbCr颜色模型"))
        self.HSV.setText(_translate("MainWindow", "HSV颜色模型"))
        self.divide.setText(_translate("MainWindow", "阈值分割"))
        self.morphology.setText(_translate("MainWindow", "形态学处理"))
        self.feature.setText(_translate("MainWindow", "特征提取"))
        self.imageclassify.setText(_translate("MainWindow", "图像分类与识别"))

