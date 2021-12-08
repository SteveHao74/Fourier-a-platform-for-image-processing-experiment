# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mych2_qt.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SAEE_chapter2(object):
    def setupUi(self, SAEE_chapter2):
        SAEE_chapter2.setObjectName("SAEE_chapter2")
        SAEE_chapter2.resize(1145, 989)
        SAEE_chapter2.setMinimumSize(QtCore.QSize(0, 0))
        SAEE_chapter2.setMaximumSize(QtCore.QSize(1145, 989))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        SAEE_chapter2.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SAEE_chapter2.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SAEE_chapter2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 291, 981))
        self.textBrowser.setStyleSheet("font: 9pt \"Roman\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(139, 255, 131);")
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 10, 852, 981))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Box_p1 = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Box_p1.sizePolicy().hasHeightForWidth())
        self.Box_p1.setSizePolicy(sizePolicy)
        self.Box_p1.setMinimumSize(QtCore.QSize(850, 501))
        self.Box_p1.setMaximumSize(QtCore.QSize(850, 501))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Box_p1.setFont(font)
        self.Box_p1.setAutoFillBackground(True)
        self.Box_p1.setStyleSheet("")
        self.Box_p1.setObjectName("Box_p1")
        self.LB_1 = QtWidgets.QLabel(self.Box_p1)
        self.LB_1.setGeometry(QtCore.QRect(80, 450, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_1.sizePolicy().hasHeightForWidth())
        self.LB_1.setSizePolicy(sizePolicy)
        self.LB_1.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_1.setObjectName("LB_1")
        self.selectpicture = QtWidgets.QToolButton(self.Box_p1)
        self.selectpicture.setEnabled(True)
        self.selectpicture.setGeometry(QtCore.QRect(10, 40, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectpicture.sizePolicy().hasHeightForWidth())
        self.selectpicture.setSizePolicy(sizePolicy)
        self.selectpicture.setMinimumSize(QtCore.QSize(81, 21))
        self.selectpicture.setStyleSheet("\n"
"\n"
"QToolButton\n"
"                     {text-align : center;\n"
"                     background-color : rgb(0, 255, 255);\n"
"                     font: bold;\n"
"                     border-color: blue;\n"
"                     border-width: 2px;\n"
"                     border-radius: 10px;\n"
"                     padding: 6px;\n"
"                     height : 14px;\n"
"                     border-style: outset;\n"
"                     font : 14px;}\n"
"                     QToolButton:hover\n"
"                     {text-align : center;\n"
"                     color : red;\n"
"                     font: bold;\n"
"                     border-color: gray;\n"
"                     border-width: 2px;\n"
"                     border-radius: 10px;\n"
"                     padding: 6px;\n"
"                     height : 14px;\n"
"                     border-style: outset;\n"
"                     font : 14px;}\n"
"\n"
"")
        self.selectpicture.setObjectName("selectpicture")
        self.information = QtWidgets.QTextBrowser(self.Box_p1)
        self.information.setGeometry(QtCore.QRect(220, 450, 441, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.information.sizePolicy().hasHeightForWidth())
        self.information.setSizePolicy(sizePolicy)
        self.information.setMinimumSize(QtCore.QSize(311, 21))
        self.information.setObjectName("information")
        self.scrollArea = QtWidgets.QScrollArea(self.Box_p1)
        self.scrollArea.setGeometry(QtCore.QRect(180, 50, 521, 381))
        self.scrollArea.setMinimumSize(QtCore.QSize(521, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-131, 0, 629, 622))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.LB_pic_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_pic_1.sizePolicy().hasHeightForWidth())
        self.LB_pic_1.setSizePolicy(sizePolicy)
        self.LB_pic_1.setMinimumSize(QtCore.QSize(600, 600))
        self.LB_pic_1.setText("")
        self.LB_pic_1.setObjectName("LB_pic_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.LB_pic_1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.Box_p1)
        self.Box_p2 = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Box_p2.sizePolicy().hasHeightForWidth())
        self.Box_p2.setSizePolicy(sizePolicy)
        self.Box_p2.setMinimumSize(QtCore.QSize(0, 0))
        self.Box_p2.setAutoFillBackground(True)
        self.Box_p2.setStyleSheet("")
        self.Box_p2.setObjectName("Box_p2")
        self.frame21 = QtWidgets.QFrame(self.Box_p2)
        self.frame21.setGeometry(QtCore.QRect(0, 20, 431, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame21.sizePolicy().hasHeightForWidth())
        self.frame21.setSizePolicy(sizePolicy)
        self.frame21.setAutoFillBackground(True)
        self.frame21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame21.setObjectName("frame21")
        self.LB_p_21 = QtWidgets.QLabel(self.frame21)
        self.LB_p_21.setGeometry(QtCore.QRect(30, 70, 101, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_p_21.sizePolicy().hasHeightForWidth())
        self.LB_p_21.setSizePolicy(sizePolicy)
        self.LB_p_21.setObjectName("LB_p_21")
        self.SL_1_21 = QtWidgets.QSlider(self.frame21)
        self.SL_1_21.setGeometry(QtCore.QRect(160, 80, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_1_21.sizePolicy().hasHeightForWidth())
        self.SL_1_21.setSizePolicy(sizePolicy)
        self.SL_1_21.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_1_21.setMinimum(1)
        self.SL_1_21.setMaximum(32)
        self.SL_1_21.setSliderPosition(1)
        self.SL_1_21.setOrientation(QtCore.Qt.Horizontal)
        self.SL_1_21.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_1_21.setTickInterval(4)
        self.SL_1_21.setObjectName("SL_1_21")
        self.Bts_21 = QtWidgets.QToolButton(self.frame21)
        self.Bts_21.setGeometry(QtCore.QRect(190, 140, 91, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bts_21.sizePolicy().hasHeightForWidth())
        self.Bts_21.setSizePolicy(sizePolicy)
        self.Bts_21.setStyleSheet("\n"
"\n"
"QToolButton\n"
"                     {text-align : center;\n"
"                     background-color : rgb(0, 255, 255);\n"
"                     font: bold;\n"
"                     border-color: blue;\n"
"                     border-width: 2px;\n"
"                     border-radius: 10px;\n"
"                     padding: 6px;\n"
"                     height : 14px;\n"
"                     border-style: outset;\n"
"                     font : 14px;}\n"
"                     QToolButton:hover\n"
"                     {text-align : center;\n"
"                     color : red;\n"
"                     font: bold;\n"
"                     border-color: gray;\n"
"                     border-width: 2px;\n"
"                     border-radius: 10px;\n"
"                     padding: 6px;\n"
"                     height : 14px;\n"
"                     border-style: outset;\n"
"                     font : 14px;}\n"
"\n"
"")
        self.Bts_21.setObjectName("Bts_21")
        self.checkBox_21 = QtWidgets.QCheckBox(self.frame21)
        self.checkBox_21.setGeometry(QtCore.QRect(160, 10, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_21.sizePolicy().hasHeightForWidth())
        self.checkBox_21.setSizePolicy(sizePolicy)
        self.checkBox_21.setMinimumSize(QtCore.QSize(171, 16))
        self.checkBox_21.setObjectName("checkBox_21")
        self.OL_21 = QtWidgets.QLabel(self.frame21)
        self.OL_21.setGeometry(QtCore.QRect(30, 9, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OL_21.sizePolicy().hasHeightForWidth())
        self.OL_21.setSizePolicy(sizePolicy)
        self.OL_21.setMinimumSize(QtCore.QSize(91, 20))
        self.OL_21.setObjectName("OL_21")
        self.LC_21 = QtWidgets.QLCDNumber(self.frame21)
        self.LC_21.setGeometry(QtCore.QRect(340, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_21.setFont(font)
        self.LC_21.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_21.setLineWidth(5)
        self.LC_21.setMidLineWidth(5)
        self.LC_21.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_21.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_21.setProperty("intValue", 1)
        self.LC_21.setObjectName("LC_21")
        self.frame_22 = QtWidgets.QFrame(self.Box_p2)
        self.frame_22.setGeometry(QtCore.QRect(430, 20, 421, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setAutoFillBackground(True)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.LB_p_22 = QtWidgets.QLabel(self.frame_22)
        self.LB_p_22.setGeometry(QtCore.QRect(20, 70, 101, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_p_22.sizePolicy().hasHeightForWidth())
        self.LB_p_22.setSizePolicy(sizePolicy)
        self.LB_p_22.setAutoFillBackground(True)
        self.LB_p_22.setObjectName("LB_p_22")
        self.checkBox_22 = QtWidgets.QCheckBox(self.frame_22)
        self.checkBox_22.setGeometry(QtCore.QRect(140, 10, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_22.sizePolicy().hasHeightForWidth())
        self.checkBox_22.setSizePolicy(sizePolicy)
        self.checkBox_22.setObjectName("checkBox_22")
        self.SL_1_22 = QtWidgets.QSlider(self.frame_22)
        self.SL_1_22.setGeometry(QtCore.QRect(150, 80, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_1_22.sizePolicy().hasHeightForWidth())
        self.SL_1_22.setSizePolicy(sizePolicy)
        self.SL_1_22.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_1_22.setMinimum(1)
        self.SL_1_22.setMaximum(32)
        self.SL_1_22.setSliderPosition(1)
        self.SL_1_22.setOrientation(QtCore.Qt.Horizontal)
        self.SL_1_22.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_1_22.setTickInterval(4)
        self.SL_1_22.setObjectName("SL_1_22")
        self.LC_22 = QtWidgets.QLCDNumber(self.frame_22)
        self.LC_22.setGeometry(QtCore.QRect(330, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_22.setFont(font)
        self.LC_22.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_22.setLineWidth(5)
        self.LC_22.setMidLineWidth(5)
        self.LC_22.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_22.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_22.setProperty("intValue", 1)
        self.LC_22.setObjectName("LC_22")
        self.CB_22 = QtWidgets.QComboBox(self.frame_22)
        self.CB_22.setGeometry(QtCore.QRect(110, 150, 151, 22))
        self.CB_22.setEditable(False)
        self.CB_22.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.CB_22.setObjectName("CB_22")
        self.CB_22.addItem("")
        self.CB_22.addItem("")
        self.Bts_22 = QtWidgets.QToolButton(self.frame_22)
        self.Bts_22.setGeometry(QtCore.QRect(300, 150, 91, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bts_22.sizePolicy().hasHeightForWidth())
        self.Bts_22.setSizePolicy(sizePolicy)
        self.Bts_22.setStyleSheet("\n"
"\n"
"QToolButton\n"
"                     {text-align : center;\n"
"                     background-color : rgb(0, 255, 255);\n"
"                     font: bold;\n"
"                     border-color: blue;\n"
"                     border-width: 2px;\n"
"                     border-radius: 10px;\n"
"                     padding: 6px;\n"
"                     height : 14px;\n"
"                     border-style: outset;\n"
"                     font : 14px;}\n"
"                     QToolButton:hover\n"
"                     {text-align : center;\n"
"                     color : red;\n"
"                     font: bold;\n"
"                     border-color: gray;\n"
"                     border-width: 2px;\n"
"                     border-radius: 10px;\n"
"                     padding: 6px;\n"
"                     height : 14px;\n"
"                     border-style: outset;\n"
"                     font : 14px;}\n"
"\n"
"")
        self.Bts_22.setObjectName("Bts_22")
        self.OL_22 = QtWidgets.QLabel(self.frame_22)
        self.OL_22.setGeometry(QtCore.QRect(20, 10, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OL_22.sizePolicy().hasHeightForWidth())
        self.OL_22.setSizePolicy(sizePolicy)
        self.OL_22.setObjectName("OL_22")
        self.LB_p_23 = QtWidgets.QLabel(self.frame_22)
        self.LB_p_23.setGeometry(QtCore.QRect(20, 140, 101, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_p_23.sizePolicy().hasHeightForWidth())
        self.LB_p_23.setSizePolicy(sizePolicy)
        self.LB_p_23.setAutoFillBackground(True)
        self.LB_p_23.setObjectName("LB_p_23")
        self.verticalLayout.addWidget(self.Box_p2)
        self.Box_p3 = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Box_p3.sizePolicy().hasHeightForWidth())
        self.Box_p3.setSizePolicy(sizePolicy)
        self.Box_p3.setAutoFillBackground(True)
        self.Box_p3.setStyleSheet("")
        self.Box_p3.setObjectName("Box_p3")
        self.Bts_3 = QtWidgets.QToolButton(self.Box_p3)
        self.Bts_3.setGeometry(QtCore.QRect(600, 90, 101, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bts_3.sizePolicy().hasHeightForWidth())
        self.Bts_3.setSizePolicy(sizePolicy)
        self.Bts_3.setStyleSheet("\n"
"\n"
"QToolButton\n"
"                     {text-align : center;\n"
"                     background-color : rgb(0, 255, 255);\n"
"                     font: bold;\n"
"                     border-color: blue;\n"
"                     border-width: 2px;\n"
"                     border-radius: 10px;\n"
"                     padding: 6px;\n"
"                     height : 14px;\n"
"                     border-style: outset;\n"
"                     font : 14px;}\n"
"                     QToolButton:hover\n"
"                     {text-align : center;\n"
"                     color : red;\n"
"                     font: bold;\n"
"                     border-color: gray;\n"
"                     border-width: 2px;\n"
"                     border-radius: 10px;\n"
"                     padding: 6px;\n"
"                     height : 14px;\n"
"                     border-style: outset;\n"
"                     font : 14px;}\n"
"\n"
"")
        self.Bts_3.setObjectName("Bts_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.Box_p3)
        self.checkBox_3.setGeometry(QtCore.QRect(40, 40, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setObjectName("checkBox_3")
        self.OL_2_2 = QtWidgets.QLabel(self.Box_p3)
        self.OL_2_2.setGeometry(QtCore.QRect(40, 90, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OL_2_2.sizePolicy().hasHeightForWidth())
        self.OL_2_2.setSizePolicy(sizePolicy)
        self.OL_2_2.setObjectName("OL_2_2")
        self.SL_3 = QtWidgets.QSlider(self.Box_p3)
        self.SL_3.setGeometry(QtCore.QRect(230, 100, 221, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_3.sizePolicy().hasHeightForWidth())
        self.SL_3.setSizePolicy(sizePolicy)
        self.SL_3.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_3.setMinimum(2)
        self.SL_3.setMaximum(256)
        self.SL_3.setProperty("value", 256)
        self.SL_3.setSliderPosition(256)
        self.SL_3.setOrientation(QtCore.Qt.Horizontal)
        self.SL_3.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_3.setTickInterval(16)
        self.SL_3.setObjectName("SL_3")
        self.LC_3 = QtWidgets.QLCDNumber(self.Box_p3)
        self.LC_3.setGeometry(QtCore.QRect(480, 100, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_3.setFont(font)
        self.LC_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_3.setLineWidth(5)
        self.LC_3.setMidLineWidth(5)
        self.LC_3.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_3.setProperty("intValue", 256)
        self.LC_3.setObjectName("LC_3")
        self.verticalLayout.addWidget(self.Box_p3)
        SAEE_chapter2.setCentralWidget(self.centralwidget)

        self.retranslateUi(SAEE_chapter2)
        QtCore.QMetaObject.connectSlotsByName(SAEE_chapter2)

    def retranslateUi(self, SAEE_chapter2):
        _translate = QtCore.QCoreApplication.translate
        SAEE_chapter2.setWindowTitle(_translate("SAEE_chapter2", "chapter 2 . 图像处理基础"))
        self.textBrowser.setHtml(_translate("SAEE_chapter2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roman\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">第一章 图像处理基础</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">本章实验内容：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">PART1:图像导入</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">PART2：空间分辨率：</span><span style=\" font-family:\'SimSun\'; font-size:10pt;\">2.1 缩小；2.2 放大</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">PART3：灰度级分辨率</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">PART1:图像导入</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">点击“加载自定义图片” 即可 选择本地路径 从而导入自定义图片，在下面图片信息栏中，图像的空间分辨率大小和通道信息将会显示出来。如果想要使用 导入的图片作为后续PART的处理对象，则需要在特定PART勾选 “使用自定义图片”，否则将会使用软件自带图片。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">PART2：空间分辨率</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">注：如果想要使用 导入的图片作为后续PART的处理对象，则需要在特定PART勾选 “使用自定义图片”，否则将会使用软件自带图片。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">缩小：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">1，使用滑动条设定缩小倍数 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">2，点击“显示效果”，将弹出结果。每次使用滑条 改变倍数后，需要重新点击“显示效果”；</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">放大：<br />1，设定放大倍数同理，</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">2，选择插值方法：可以通过下拉选项，共两种：“最近邻法”，“双线性内插值法”。应注意使用相同方法而不同倍数的对比，和使用相同倍数而不同方法的对比。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">3，点击【显示效果】</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:600;\">PART3：灰度级分辨率</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">1，使用滑动条设置灰度级数</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10pt;\">2，点击【显示效果 】，注意观察因灰度级较少而造成的伪轮廓现象</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:10pt;\"><br /></p></body></html>"))
        self.Box_p1.setTitle(_translate("SAEE_chapter2", "Part 1 自定义原始图片"))
        self.LB_1.setText(_translate("SAEE_chapter2", "图片信息："))
        self.selectpicture.setText(_translate("SAEE_chapter2", "加载自定义图片"))
        self.Box_p2.setTitle(_translate("SAEE_chapter2", "Part 2 空间分辨率"))
        self.LB_p_21.setText(_translate("SAEE_chapter2", "边缩小倍数："))
        self.Bts_21.setText(_translate("SAEE_chapter2", "显示效果"))
        self.checkBox_21.setText(_translate("SAEE_chapter2", "使用自定义图片"))
        self.OL_21.setText(_translate("SAEE_chapter2", "2.1 缩小"))
        self.LB_p_22.setText(_translate("SAEE_chapter2", "边放大倍数："))
        self.checkBox_22.setText(_translate("SAEE_chapter2", "使用自定义图片"))
        self.CB_22.setItemText(0, _translate("SAEE_chapter2", "INTER_NEAREST"))
        self.CB_22.setItemText(1, _translate("SAEE_chapter2", "INTER_LINEAR"))
        self.Bts_22.setText(_translate("SAEE_chapter2", "显示效果"))
        self.OL_22.setText(_translate("SAEE_chapter2", "2.2 放大"))
        self.LB_p_23.setText(_translate("SAEE_chapter2", "插补方法："))
        self.Box_p3.setTitle(_translate("SAEE_chapter2", "Part 3 灰度级分辨率"))
        self.Bts_3.setText(_translate("SAEE_chapter2", "显示效果"))
        self.checkBox_3.setText(_translate("SAEE_chapter2", "使用自定义图片"))
        self.OL_2_2.setText(_translate("SAEE_chapter2", "设置灰度级数："))
