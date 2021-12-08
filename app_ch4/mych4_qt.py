# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wide_mych4_qt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ch4_Window(object):
    def setupUi(self, Ch4_Window):
        Ch4_Window.setObjectName("Ch4_Window")
        Ch4_Window.setWindowModality(QtCore.Qt.ApplicationModal)
        Ch4_Window.resize(1595, 792)
        Ch4_Window.setMinimumSize(QtCore.QSize(800, 0))
        Ch4_Window.setMaximumSize(QtCore.QSize(1600, 1106))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        Ch4_Window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../picturesource/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ch4_Window.setWindowIcon(icon)
        Ch4_Window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Ch4_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Box_p1 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Box_p1.sizePolicy().hasHeightForWidth())
        self.Box_p1.setSizePolicy(sizePolicy)
        self.Box_p1.setMinimumSize(QtCore.QSize(700, 500))
        self.Box_p1.setAutoFillBackground(True)
        self.Box_p1.setTitle("")
        self.Box_p1.setObjectName("Box_p1")
        self.LB_1 = QtWidgets.QLabel(self.Box_p1)
        self.LB_1.setGeometry(QtCore.QRect(80, 640, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_1.sizePolicy().hasHeightForWidth())
        self.LB_1.setSizePolicy(sizePolicy)
        self.LB_1.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_1.setObjectName("LB_1")
        self.selectpicture = QtWidgets.QToolButton(self.Box_p1)
        self.selectpicture.setEnabled(True)
        self.selectpicture.setGeometry(QtCore.QRect(280, 110, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectpicture.sizePolicy().hasHeightForWidth())
        self.selectpicture.setSizePolicy(sizePolicy)
        self.selectpicture.setMinimumSize(QtCore.QSize(81, 21))
        self.selectpicture.setObjectName("selectpicture")
        self.information = QtWidgets.QTextBrowser(self.Box_p1)
        self.information.setGeometry(QtCore.QRect(180, 640, 441, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.information.sizePolicy().hasHeightForWidth())
        self.information.setSizePolicy(sizePolicy)
        self.information.setMinimumSize(QtCore.QSize(311, 21))
        self.information.setObjectName("information")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Box_p1)
        self.scrollArea_2.setGeometry(QtCore.QRect(60, 170, 571, 421))
        self.scrollArea_2.setMinimumSize(QtCore.QSize(521, 381))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 829, 822))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout.setObjectName("formLayout")
        self.LB_pic_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_pic_1.sizePolicy().hasHeightForWidth())
        self.LB_pic_1.setSizePolicy(sizePolicy)
        self.LB_pic_1.setMinimumSize(QtCore.QSize(800, 800))
        self.LB_pic_1.setText("")
        self.LB_pic_1.setObjectName("LB_pic_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.LB_pic_1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.LB_4 = QtWidgets.QLabel(self.Box_p1)
        self.LB_4.setGeometry(QtCore.QRect(40, 0, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_4.sizePolicy().hasHeightForWidth())
        self.LB_4.setSizePolicy(sizePolicy)
        self.LB_4.setMinimumSize(QtCore.QSize(45, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LB_4.setFont(font)
        self.LB_4.setObjectName("LB_4")
        self.RB_P1_self = QtWidgets.QRadioButton(self.Box_p1)
        self.RB_P1_self.setGeometry(QtCore.QRect(70, 120, 151, 20))
        self.RB_P1_self.setObjectName("RB_P1_self")
        self.RB_P1_default = QtWidgets.QRadioButton(self.Box_p1)
        self.RB_P1_default.setGeometry(QtCore.QRect(70, 60, 151, 19))
        self.RB_P1_default.setChecked(True)
        self.RB_P1_default.setObjectName("RB_P1_default")
        self.horizontalLayout.addWidget(self.Box_p1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(870, 700))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 893, 790))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setMinimumSize(QtCore.QSize(841, 650))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(50, 50))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.P2_page = QtWidgets.QWidget()
        self.P2_page.setObjectName("P2_page")
        self.textBrowser = QtWidgets.QTextBrowser(self.P2_page)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 261, 771))
        self.textBrowser.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(139, 255, 131);")
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(self.P2_page)
        self.groupBox.setGeometry(QtCore.QRect(260, 0, 631, 771))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Pb_p2 = QtWidgets.QProgressBar(self.groupBox)
        self.Pb_p2.setGeometry(QtCore.QRect(380, 70, 31, 241))
        self.Pb_p2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Pb_p2.setAutoFillBackground(False)
        self.Pb_p2.setProperty("value", 0)
        self.Pb_p2.setOrientation(QtCore.Qt.Vertical)
        self.Pb_p2.setInvertedAppearance(True)
        self.Pb_p2.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.Pb_p2.setObjectName("Pb_p2")
        self.Bt_p2st1 = QtWidgets.QToolButton(self.groupBox)
        self.Bt_p2st1.setEnabled(True)
        self.Bt_p2st1.setGeometry(QtCore.QRect(50, 70, 261, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p2st1.sizePolicy().hasHeightForWidth())
        self.Bt_p2st1.setSizePolicy(sizePolicy)
        self.Bt_p2st1.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p2st1.setStyleSheet("\n"
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
        self.Bt_p2st1.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p2st1.setAutoRaise(False)
        self.Bt_p2st1.setObjectName("Bt_p2st1")
        self.Bt_p2st3 = QtWidgets.QToolButton(self.groupBox)
        self.Bt_p2st3.setEnabled(True)
        self.Bt_p2st3.setGeometry(QtCore.QRect(50, 200, 261, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p2st3.sizePolicy().hasHeightForWidth())
        self.Bt_p2st3.setSizePolicy(sizePolicy)
        self.Bt_p2st3.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p2st3.setStyleSheet("\n"
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
        self.Bt_p2st3.setObjectName("Bt_p2st3")
        self.Bt_p2st2 = QtWidgets.QToolButton(self.groupBox)
        self.Bt_p2st2.setEnabled(True)
        self.Bt_p2st2.setGeometry(QtCore.QRect(50, 130, 261, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p2st2.sizePolicy().hasHeightForWidth())
        self.Bt_p2st2.setSizePolicy(sizePolicy)
        self.Bt_p2st2.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p2st2.setStyleSheet("\n"
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
        self.Bt_p2st2.setObjectName("Bt_p2st2")
        self.Bt_p2st4 = QtWidgets.QToolButton(self.groupBox)
        self.Bt_p2st4.setEnabled(True)
        self.Bt_p2st4.setGeometry(QtCore.QRect(50, 270, 261, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p2st4.sizePolicy().hasHeightForWidth())
        self.Bt_p2st4.setSizePolicy(sizePolicy)
        self.Bt_p2st4.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p2st4.setStyleSheet("\n"
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
        self.Bt_p2st4.setObjectName("Bt_p2st4")
        self.Bt_p2tl = QtWidgets.QToolButton(self.groupBox)
        self.Bt_p2tl.setEnabled(True)
        self.Bt_p2tl.setGeometry(QtCore.QRect(50, 330, 261, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p2tl.sizePolicy().hasHeightForWidth())
        self.Bt_p2tl.setSizePolicy(sizePolicy)
        self.Bt_p2tl.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p2tl.setStyleSheet("\n"
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
        self.Bt_p2tl.setObjectName("Bt_p2tl")
        self.Bt_p2_cross = QtWidgets.QToolButton(self.groupBox)
        self.Bt_p2_cross.setEnabled(True)
        self.Bt_p2_cross.setGeometry(QtCore.QRect(300, 550, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p2_cross.sizePolicy().hasHeightForWidth())
        self.Bt_p2_cross.setSizePolicy(sizePolicy)
        self.Bt_p2_cross.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p2_cross.setStyleSheet("\n"
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
        self.Bt_p2_cross.setObjectName("Bt_p2_cross")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 430, 391, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 400, 181, 16))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(30, 10, 301, 16))
        self.label_8.setObjectName("label_8")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(70, 500, 191, 191))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.LB_pic_3 = QtWidgets.QLabel(self.groupBox_5)
        self.LB_pic_3.setGeometry(QtCore.QRect(0, 0, 191, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_pic_3.sizePolicy().hasHeightForWidth())
        self.LB_pic_3.setSizePolicy(sizePolicy)
        self.LB_pic_3.setMinimumSize(QtCore.QSize(0, 0))
        self.LB_pic_3.setText("")
        self.LB_pic_3.setObjectName("LB_pic_3")
        self.tabWidget.addTab(self.P2_page, "")
        self.P3_page = QtWidgets.QWidget()
        self.P3_page.setObjectName("P3_page")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.P3_page)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 251, 761))
        self.textBrowser_2.setMinimumSize(QtCore.QSize(251, 0))
        self.textBrowser_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(139, 255, 131);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.P3_page)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 0, 634, 763))
        self.groupBox_2.setMinimumSize(QtCore.QSize(634, 0))
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setMinimumSize(QtCore.QSize(591, 311))
        self.groupBox_3.setObjectName("groupBox_3")
        self.SL_34 = QtWidgets.QSlider(self.groupBox_3)
        self.SL_34.setGeometry(QtCore.QRect(250, 230, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_34.sizePolicy().hasHeightForWidth())
        self.SL_34.setSizePolicy(sizePolicy)
        self.SL_34.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_34.setMinimum(1)
        self.SL_34.setMaximum(10)
        self.SL_34.setSliderPosition(1)
        self.SL_34.setOrientation(QtCore.Qt.Horizontal)
        self.SL_34.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_34.setTickInterval(1)
        self.SL_34.setObjectName("SL_34")
        self.LB_7 = QtWidgets.QLabel(self.groupBox_3)
        self.LB_7.setGeometry(QtCore.QRect(130, 180, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_7.sizePolicy().hasHeightForWidth())
        self.LB_7.setSizePolicy(sizePolicy)
        self.LB_7.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_7.setObjectName("LB_7")
        self.LC_34 = QtWidgets.QLCDNumber(self.groupBox_3)
        self.LC_34.setGeometry(QtCore.QRect(430, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_34.setFont(font)
        self.LC_34.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_34.setLineWidth(5)
        self.LC_34.setMidLineWidth(5)
        self.LC_34.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_34.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_34.setProperty("intValue", 1)
        self.LC_34.setObjectName("LC_34")
        self.SL_31 = QtWidgets.QSlider(self.groupBox_3)
        self.SL_31.setGeometry(QtCore.QRect(220, 60, 231, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_31.sizePolicy().hasHeightForWidth())
        self.SL_31.setSizePolicy(sizePolicy)
        self.SL_31.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_31.setMinimum(0)
        self.SL_31.setMaximum(200)
        self.SL_31.setProperty("value", 200)
        self.SL_31.setSliderPosition(200)
        self.SL_31.setOrientation(QtCore.Qt.Horizontal)
        self.SL_31.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_31.setTickInterval(2)
        self.SL_31.setObjectName("SL_31")
        self.SL_32 = QtWidgets.QSlider(self.groupBox_3)
        self.SL_32.setGeometry(QtCore.QRect(250, 110, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_32.sizePolicy().hasHeightForWidth())
        self.SL_32.setSizePolicy(sizePolicy)
        self.SL_32.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_32.setMinimum(1)
        self.SL_32.setMaximum(10)
        self.SL_32.setPageStep(1)
        self.SL_32.setProperty("value", 1)
        self.SL_32.setSliderPosition(1)
        self.SL_32.setOrientation(QtCore.Qt.Horizontal)
        self.SL_32.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_32.setTickInterval(1)
        self.SL_32.setObjectName("SL_32")
        self.LC_32 = QtWidgets.QLCDNumber(self.groupBox_3)
        self.LC_32.setGeometry(QtCore.QRect(430, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_32.setFont(font)
        self.LC_32.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_32.setLineWidth(5)
        self.LC_32.setMidLineWidth(5)
        self.LC_32.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_32.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_32.setProperty("intValue", 1)
        self.LC_32.setObjectName("LC_32")
        self.LC_33 = QtWidgets.QLCDNumber(self.groupBox_3)
        self.LC_33.setGeometry(QtCore.QRect(480, 180, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_33.setFont(font)
        self.LC_33.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_33.setLineWidth(5)
        self.LC_33.setMidLineWidth(5)
        self.LC_33.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_33.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_33.setProperty("intValue", 1)
        self.LC_33.setObjectName("LC_33")
        self.LC_31 = QtWidgets.QLCDNumber(self.groupBox_3)
        self.LC_31.setGeometry(QtCore.QRect(480, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_31.setFont(font)
        self.LC_31.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_31.setLineWidth(5)
        self.LC_31.setMidLineWidth(5)
        self.LC_31.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_31.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_31.setProperty("intValue", 200)
        self.LC_31.setObjectName("LC_31")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(130, 230, 111, 31))
        self.label_2.setObjectName("label_2")
        self.LB_5 = QtWidgets.QLabel(self.groupBox_3)
        self.LB_5.setGeometry(QtCore.QRect(60, 40, 101, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_5.sizePolicy().hasHeightForWidth())
        self.LB_5.setSizePolicy(sizePolicy)
        self.LB_5.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_5.setObjectName("LB_5")
        self.SL_33 = QtWidgets.QSlider(self.groupBox_3)
        self.SL_33.setGeometry(QtCore.QRect(220, 180, 231, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_33.sizePolicy().hasHeightForWidth())
        self.SL_33.setSizePolicy(sizePolicy)
        self.SL_33.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_33.setMinimum(1)
        self.SL_33.setMaximum(200)
        self.SL_33.setProperty("value", 1)
        self.SL_33.setSliderPosition(1)
        self.SL_33.setOrientation(QtCore.Qt.Horizontal)
        self.SL_33.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_33.setTickInterval(2)
        self.SL_33.setObjectName("SL_33")
        self.LB_6 = QtWidgets.QLabel(self.groupBox_3)
        self.LB_6.setGeometry(QtCore.QRect(50, 150, 101, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_6.sizePolicy().hasHeightForWidth())
        self.LB_6.setSizePolicy(sizePolicy)
        self.LB_6.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_6.setObjectName("LB_6")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(130, 110, 111, 31))
        self.label.setObjectName("label")
        self.LB_8 = QtWidgets.QLabel(self.groupBox_3)
        self.LB_8.setGeometry(QtCore.QRect(130, 70, 71, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_8.sizePolicy().hasHeightForWidth())
        self.LB_8.setSizePolicy(sizePolicy)
        self.LB_8.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_8.setObjectName("LB_8")
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setMinimumSize(QtCore.QSize(610, 421))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.Bt_p3_TL = QtWidgets.QToolButton(self.groupBox_4)
        self.Bt_p3_TL.setEnabled(True)
        self.Bt_p3_TL.setGeometry(QtCore.QRect(470, 170, 101, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3_TL.sizePolicy().hasHeightForWidth())
        self.Bt_p3_TL.setSizePolicy(sizePolicy)
        self.Bt_p3_TL.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3_TL.setStyleSheet("\n"
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
        self.Bt_p3_TL.setObjectName("Bt_p3_TL")
        self.Bt_p3_L3 = QtWidgets.QToolButton(self.groupBox_4)
        self.Bt_p3_L3.setEnabled(True)
        self.Bt_p3_L3.setGeometry(QtCore.QRect(60, 270, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3_L3.sizePolicy().hasHeightForWidth())
        self.Bt_p3_L3.setSizePolicy(sizePolicy)
        self.Bt_p3_L3.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3_L3.setStyleSheet("\n"
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
        self.Bt_p3_L3.setObjectName("Bt_p3_L3")
        self.Bt_p3_H2 = QtWidgets.QToolButton(self.groupBox_4)
        self.Bt_p3_H2.setEnabled(True)
        self.Bt_p3_H2.setGeometry(QtCore.QRect(270, 210, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3_H2.sizePolicy().hasHeightForWidth())
        self.Bt_p3_H2.setSizePolicy(sizePolicy)
        self.Bt_p3_H2.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3_H2.setStyleSheet("\n"
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
        self.Bt_p3_H2.setObjectName("Bt_p3_H2")
        self.Bt_p3_L2 = QtWidgets.QToolButton(self.groupBox_4)
        self.Bt_p3_L2.setEnabled(True)
        self.Bt_p3_L2.setGeometry(QtCore.QRect(60, 210, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3_L2.sizePolicy().hasHeightForWidth())
        self.Bt_p3_L2.setSizePolicy(sizePolicy)
        self.Bt_p3_L2.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3_L2.setStyleSheet("\n"
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
        self.Bt_p3_L2.setObjectName("Bt_p3_L2")
        self.Bt_p3_H3 = QtWidgets.QToolButton(self.groupBox_4)
        self.Bt_p3_H3.setEnabled(True)
        self.Bt_p3_H3.setGeometry(QtCore.QRect(270, 270, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3_H3.sizePolicy().hasHeightForWidth())
        self.Bt_p3_H3.setSizePolicy(sizePolicy)
        self.Bt_p3_H3.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3_H3.setStyleSheet("\n"
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
        self.Bt_p3_H3.setObjectName("Bt_p3_H3")
        self.Bt_p3_L1 = QtWidgets.QToolButton(self.groupBox_4)
        self.Bt_p3_L1.setEnabled(True)
        self.Bt_p3_L1.setGeometry(QtCore.QRect(60, 150, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3_L1.sizePolicy().hasHeightForWidth())
        self.Bt_p3_L1.setSizePolicy(sizePolicy)
        self.Bt_p3_L1.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3_L1.setStyleSheet("\n"
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
        self.Bt_p3_L1.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p3_L1.setAutoRaise(False)
        self.Bt_p3_L1.setObjectName("Bt_p3_L1")
        self.Bt_p3_H1 = QtWidgets.QToolButton(self.groupBox_4)
        self.Bt_p3_H1.setEnabled(True)
        self.Bt_p3_H1.setGeometry(QtCore.QRect(270, 150, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3_H1.sizePolicy().hasHeightForWidth())
        self.Bt_p3_H1.setSizePolicy(sizePolicy)
        self.Bt_p3_H1.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3_H1.setStyleSheet("\n"
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
        self.Bt_p3_H1.setObjectName("Bt_p3_H1")
        self.LB_3 = QtWidgets.QLabel(self.groupBox_4)
        self.LB_3.setGeometry(QtCore.QRect(230, 120, 101, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_3.sizePolicy().hasHeightForWidth())
        self.LB_3.setSizePolicy(sizePolicy)
        self.LB_3.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_3.setObjectName("LB_3")
        self.LB_2 = QtWidgets.QLabel(self.groupBox_4)
        self.LB_2.setGeometry(QtCore.QRect(20, 120, 101, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_2.sizePolicy().hasHeightForWidth())
        self.LB_2.setSizePolicy(sizePolicy)
        self.LB_2.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_2.setObjectName("LB_2")
        self.CB_3 = QtWidgets.QComboBox(self.groupBox_4)
        self.CB_3.setGeometry(QtCore.QRect(300, 40, 151, 22))
        self.CB_3.setEditable(False)
        self.CB_3.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.CB_3.setObjectName("CB_3")
        self.CB_3.addItem("")
        self.CB_3.addItem("")
        self.CB_3.addItem("")
        self.CB_3.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 241, 16))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.P3_page, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        Ch4_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ch4_Window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Ch4_Window)

    def retranslateUi(self, Ch4_Window):
        _translate = QtCore.QCoreApplication.translate
        Ch4_Window.setWindowTitle(_translate("Ch4_Window", "Chapter 4 频域图像增强"))
        self.LB_1.setText(_translate("Ch4_Window", "图片信息："))
        self.selectpicture.setStyleSheet(_translate("Ch4_Window", "\n"
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
""))
        self.selectpicture.setText(_translate("Ch4_Window", "加载自定义图片"))
        self.LB_4.setText(_translate("Ch4_Window", "Part 1 自定义原始图片"))
        self.RB_P1_self.setText(_translate("Ch4_Window", "使用自定义图片"))
        self.RB_P1_default.setText(_translate("Ch4_Window", "使用默认图片"))
        self.textBrowser.setHtml(_translate("Ch4_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">PART2 傅里叶变换与重构</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">实验内容：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">1，基础变换和重构</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">2，双图混合重构</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">实验步骤：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">1，基础变换和重构：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; font-size:10pt;\">这里将整个傅里叶过程拆解成 四步，必须按顺序进行，执行完前一步产生中间结果后，才可以进行下一步，不可跳步。这一点由冻结按钮实现，不允许被执行的按钮将被 冻结（冻结体现为按钮的字是灰色，且按钮点击不动，如 第一步尚未执行时，后续步骤都不允许进行；而若已执行完第四步后，重新执行第一步，则会使后续以解冻的步骤全部失效重新被冻结）。</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; font-size:10pt;\">按钮的右侧有一个对应进度条，实时记录了当前已经完成的进度，迷茫时可看看进度条。相对比整个过程则可以点击完整演示。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2，</span><span style=\" font-family:\'SimSun\'; font-size:12pt;\">双图混合重构：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">小图为picture1，Part1中的大图是picture2，点击交叉融合即可。</span></p></body></html>"))
        self.Bt_p2st1.setText(_translate("Ch4_Window", "Step 1:图像的傅里叶变换及中心化"))
        self.Bt_p2st3.setText(_translate("Ch4_Window", "Step 3:使用相位谱重构原图"))
        self.Bt_p2st2.setText(_translate("Ch4_Window", "Step 2:使用幅度谱重构原图"))
        self.Bt_p2st4.setText(_translate("Ch4_Window", "Step 4:使用双谱重构原图"))
        self.Bt_p2tl.setText(_translate("Ch4_Window", "完整演示"))
        self.Bt_p2_cross.setText(_translate("Ch4_Window", "交叉融合重建"))
        self.label_4.setText(_translate("Ch4_Window", "注：picture1:如下图 ； picture2:即为自定义图片"))
        self.label_5.setText(_translate("Ch4_Window", "双图混合重构"))
        self.label_8.setText(_translate("Ch4_Window", "1，基础变换和重构：请按顺序完成如下步骤"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.P2_page), _translate("Ch4_Window", "Part2.傅里叶变换与重构"))
        self.textBrowser_2.setHtml(_translate("Ch4_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">PART3 频率域滤波</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">实验内容：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">低通滤波</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">1，理想低通滤波</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">2，巴特沃斯低通滤波</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">3，高斯低通滤波</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">高通滤波</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">1，理想高通滤波</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">2，巴特沃斯高通滤波</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">3，高斯高通滤波</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">实验步骤：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">首先在 统一调参区 进行调参，注意，频率半径参数是高通或低通里所有滤波器共用的参数</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">之后在 操作区，选择处理图像对象，如果使用自定义图片 则只需在左侧 ！PART1！中 点击 “使用自定义图片”；但当选择“默认图片”时，则可在下拉菜单中选择多种示例图片。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">总之，当前到底处理的是什么图片，只需要看PART1中显示的图片即可，所见即所得。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">对应按钮运行</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("Ch4_Window", "统一调参区"))
        self.LB_7.setText(_translate("Ch4_Window", "频率半径："))
        self.label_2.setText(_translate("Ch4_Window", "巴特沃斯阶数："))
        self.LB_5.setText(_translate("Ch4_Window", "低通滤波器："))
        self.LB_6.setText(_translate("Ch4_Window", "高通滤波器："))
        self.label.setText(_translate("Ch4_Window", "巴特沃斯阶数："))
        self.LB_8.setText(_translate("Ch4_Window", "频率半径："))
        self.groupBox_4.setTitle(_translate("Ch4_Window", "操作区"))
        self.Bt_p3_TL.setText(_translate("Ch4_Window", "综合对比"))
        self.Bt_p3_L3.setText(_translate("Ch4_Window", "3，高斯低通滤波"))
        self.Bt_p3_H2.setText(_translate("Ch4_Window", "2，巴特沃斯高通滤波"))
        self.Bt_p3_L2.setText(_translate("Ch4_Window", "2，巴特沃斯低通滤波"))
        self.Bt_p3_H3.setText(_translate("Ch4_Window", "3，高斯高通滤波"))
        self.Bt_p3_L1.setText(_translate("Ch4_Window", "1，理想低通滤波"))
        self.Bt_p3_H1.setText(_translate("Ch4_Window", "1，理想高通滤波"))
        self.LB_3.setText(_translate("Ch4_Window", "高通滤波器："))
        self.LB_2.setText(_translate("Ch4_Window", "低通滤波器："))
        self.CB_3.setItemText(0, _translate("Ch4_Window", "纹理"))
        self.CB_3.setItemText(1, _translate("Ch4_Window", "文字"))
        self.CB_3.setItemText(2, _translate("Ch4_Window", "人像"))
        self.CB_3.setItemText(3, _translate("Ch4_Window", "扫描线"))
        self.label_3.setText(_translate("Ch4_Window", "图片选择：（可选用自定义图片）"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.P3_page), _translate("Ch4_Window", "Part3.频率域滤波"))

