# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wide_mych5_qt.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ch5_Window(object):
    def setupUi(self, Ch5_Window):
        Ch5_Window.setObjectName("Ch5_Window")
        Ch5_Window.setWindowModality(QtCore.Qt.ApplicationModal)
        Ch5_Window.resize(1600, 752)
        Ch5_Window.setMinimumSize(QtCore.QSize(800, 0))
        Ch5_Window.setMaximumSize(QtCore.QSize(1600, 1106))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        Ch5_Window.setFont(font)
        Ch5_Window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Ch5_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Box_p1 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Box_p1.sizePolicy().hasHeightForWidth())
        self.Box_p1.setSizePolicy(sizePolicy)
        self.Box_p1.setMinimumSize(QtCore.QSize(660, 500))
        self.Box_p1.setAutoFillBackground(True)
        self.Box_p1.setTitle("")
        self.Box_p1.setObjectName("Box_p1")
        self.selectpicture = QtWidgets.QToolButton(self.Box_p1)
        self.selectpicture.setEnabled(True)
        self.selectpicture.setGeometry(QtCore.QRect(280, 100, 121, 41))
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
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Box_p1)
        self.scrollArea_2.setGeometry(QtCore.QRect(30, 170, 561, 431))
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
        self.RB_P1_self.setGeometry(QtCore.QRect(60, 110, 181, 20))
        self.RB_P1_self.setObjectName("RB_P1_self")
        self.RB_P1_default = QtWidgets.QRadioButton(self.Box_p1)
        self.RB_P1_default.setGeometry(QtCore.QRect(60, 60, 181, 19))
        self.RB_P1_default.setChecked(True)
        self.RB_P1_default.setObjectName("RB_P1_default")
        self.information = QtWidgets.QTextBrowser(self.Box_p1)
        self.information.setGeometry(QtCore.QRect(130, 640, 441, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.information.sizePolicy().hasHeightForWidth())
        self.information.setSizePolicy(sizePolicy)
        self.information.setMinimumSize(QtCore.QSize(311, 21))
        self.information.setObjectName("information")
        self.LB_1 = QtWidgets.QLabel(self.Box_p1)
        self.LB_1.setGeometry(QtCore.QRect(30, 640, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_1.sizePolicy().hasHeightForWidth())
        self.LB_1.setSizePolicy(sizePolicy)
        self.LB_1.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_1.setObjectName("LB_1")
        self.gridLayout_4.addWidget(self.Box_p1, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(920, 700))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 938, 750))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setMinimumSize(QtCore.QSize(841, 650))
        self.tabWidget.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(50, 50))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.P2_page = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.P2_page.setFont(font)
        self.P2_page.setObjectName("P2_page")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.P2_page)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.P2_page)
        self.textBrowser.setMinimumSize(QtCore.QSize(300, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(300, 16777215))
        self.textBrowser.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(139, 255, 131);")
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_4.addWidget(self.textBrowser)
        self.groupBox = QtWidgets.QGroupBox(self.P2_page)
        self.groupBox.setMinimumSize(QtCore.QSize(580, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(630, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setStyleSheet("\n"
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
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Bt_p2_fuyuan = QtWidgets.QToolButton(self.groupBox)
        self.Bt_p2_fuyuan.setEnabled(True)
        self.Bt_p2_fuyuan.setGeometry(QtCore.QRect(40, 470, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p2_fuyuan.sizePolicy().hasHeightForWidth())
        self.Bt_p2_fuyuan.setSizePolicy(sizePolicy)
        self.Bt_p2_fuyuan.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p2_fuyuan.setStyleSheet("\n"
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
        self.Bt_p2_fuyuan.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p2_fuyuan.setAutoRaise(False)
        self.Bt_p2_fuyuan.setObjectName("Bt_p2_fuyuan")
        self.CB_p2_sel_filter = QtWidgets.QComboBox(self.groupBox)
        self.CB_p2_sel_filter.setGeometry(QtCore.QRect(250, 380, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.CB_p2_sel_filter.setFont(font)
        self.CB_p2_sel_filter.setEditable(False)
        self.CB_p2_sel_filter.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.CB_p2_sel_filter.setObjectName("CB_p2_sel_filter")
        self.CB_p2_sel_filter.addItem("")
        self.CB_p2_sel_filter.addItem("")
        self.CB_p2_sel_filter.addItem("")
        self.CB_p2_sel_filter.addItem("")
        self.CB_p2_sel_filter.addItem("")
        self.LB_24 = QtWidgets.QLabel(self.groupBox)
        self.LB_24.setGeometry(QtCore.QRect(50, 380, 131, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_24.sizePolicy().hasHeightForWidth())
        self.LB_24.setSizePolicy(sizePolicy)
        self.LB_24.setMinimumSize(QtCore.QSize(45, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LB_24.setFont(font)
        self.LB_24.setObjectName("LB_24")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.LC_p2_percentage = QtWidgets.QLCDNumber(self.groupBox)
        self.LC_p2_percentage.setGeometry(QtCore.QRect(440, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_p2_percentage.setFont(font)
        self.LC_p2_percentage.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_p2_percentage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_p2_percentage.setLineWidth(5)
        self.LC_p2_percentage.setMidLineWidth(5)
        self.LC_p2_percentage.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_p2_percentage.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_p2_percentage.setProperty("intValue", 1)
        self.LC_p2_percentage.setObjectName("LC_p2_percentage")
        self.SL_p2_percentage = QtWidgets.QSlider(self.groupBox)
        self.SL_p2_percentage.setGeometry(QtCore.QRect(250, 120, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_p2_percentage.sizePolicy().hasHeightForWidth())
        self.SL_p2_percentage.setSizePolicy(sizePolicy)
        self.SL_p2_percentage.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_p2_percentage.setMinimum(0)
        self.SL_p2_percentage.setMaximum(100)
        self.SL_p2_percentage.setPageStep(1)
        self.SL_p2_percentage.setProperty("value", 1)
        self.SL_p2_percentage.setSliderPosition(1)
        self.SL_p2_percentage.setOrientation(QtCore.Qt.Horizontal)
        self.SL_p2_percentage.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_p2_percentage.setTickInterval(1)
        self.SL_p2_percentage.setObjectName("SL_p2_percentage")
        self.CB_p2_sel_noise = QtWidgets.QComboBox(self.groupBox)
        self.CB_p2_sel_noise.setGeometry(QtCore.QRect(250, 60, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.CB_p2_sel_noise.setFont(font)
        self.CB_p2_sel_noise.setEditable(False)
        self.CB_p2_sel_noise.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.CB_p2_sel_noise.setObjectName("CB_p2_sel_noise")
        self.CB_p2_sel_noise.addItem("")
        self.CB_p2_sel_noise.addItem("")
        self.CB_p2_sel_noise.addItem("")
        self.CB_p2_sel_noise.addItem("")
        self.LB_29 = QtWidgets.QLabel(self.groupBox)
        self.LB_29.setGeometry(QtCore.QRect(20, 120, 211, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_29.sizePolicy().hasHeightForWidth())
        self.LB_29.setSizePolicy(sizePolicy)
        self.LB_29.setMinimumSize(QtCore.QSize(45, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.LB_29.setFont(font)
        self.LB_29.setObjectName("LB_29")
        self.LB_30 = QtWidgets.QLabel(self.groupBox)
        self.LB_30.setGeometry(QtCore.QRect(40, 180, 111, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_30.sizePolicy().hasHeightForWidth())
        self.LB_30.setSizePolicy(sizePolicy)
        self.LB_30.setMinimumSize(QtCore.QSize(45, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.LB_30.setFont(font)
        self.LB_30.setObjectName("LB_30")
        self.SL_p2_mean = QtWidgets.QSlider(self.groupBox)
        self.SL_p2_mean.setGeometry(QtCore.QRect(260, 170, 171, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_p2_mean.sizePolicy().hasHeightForWidth())
        self.SL_p2_mean.setSizePolicy(sizePolicy)
        self.SL_p2_mean.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_p2_mean.setMinimum(-50)
        self.SL_p2_mean.setMaximum(50)
        self.SL_p2_mean.setSingleStep(1)
        self.SL_p2_mean.setPageStep(1)
        self.SL_p2_mean.setProperty("value", 0)
        self.SL_p2_mean.setSliderPosition(0)
        self.SL_p2_mean.setOrientation(QtCore.Qt.Horizontal)
        self.SL_p2_mean.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_p2_mean.setTickInterval(10)
        self.SL_p2_mean.setObjectName("SL_p2_mean")
        self.LC_p2_mean = QtWidgets.QLCDNumber(self.groupBox)
        self.LC_p2_mean.setGeometry(QtCore.QRect(450, 180, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_p2_mean.setFont(font)
        self.LC_p2_mean.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_p2_mean.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_p2_mean.setLineWidth(5)
        self.LC_p2_mean.setMidLineWidth(5)
        self.LC_p2_mean.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_p2_mean.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_p2_mean.setProperty("value", 0.0)
        self.LC_p2_mean.setProperty("intValue", 0)
        self.LC_p2_mean.setObjectName("LC_p2_mean")
        self.LB_31 = QtWidgets.QLabel(self.groupBox)
        self.LB_31.setGeometry(QtCore.QRect(500, 110, 45, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_31.sizePolicy().hasHeightForWidth())
        self.LB_31.setSizePolicy(sizePolicy)
        self.LB_31.setMinimumSize(QtCore.QSize(45, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LB_31.setFont(font)
        self.LB_31.setStyleSheet(" border:0px solid #1B89CA;  \\n    border-radius:5px;   ")
        self.LB_31.setObjectName("LB_31")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(30, 320, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.LB_33 = QtWidgets.QLabel(self.groupBox)
        self.LB_33.setGeometry(QtCore.QRect(40, 60, 131, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_33.sizePolicy().hasHeightForWidth())
        self.LB_33.setSizePolicy(sizePolicy)
        self.LB_33.setMinimumSize(QtCore.QSize(45, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.LB_33.setFont(font)
        self.LB_33.setObjectName("LB_33")
        self.Bt_p2_tuihua = QtWidgets.QToolButton(self.groupBox)
        self.Bt_p2_tuihua.setEnabled(True)
        self.Bt_p2_tuihua.setGeometry(QtCore.QRect(40, 240, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p2_tuihua.sizePolicy().hasHeightForWidth())
        self.Bt_p2_tuihua.setSizePolicy(sizePolicy)
        self.Bt_p2_tuihua.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p2_tuihua.setStyleSheet("\n"
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
        self.Bt_p2_tuihua.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p2_tuihua.setAutoRaise(False)
        self.Bt_p2_tuihua.setObjectName("Bt_p2_tuihua")
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.tabWidget.addTab(self.P2_page, "")
        self.P3_page = QtWidgets.QWidget()
        self.P3_page.setObjectName("P3_page")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.P3_page)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.P3_page)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(300, 0))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(380, 16777215))
        self.textBrowser_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(139, 255, 131);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_3.addWidget(self.textBrowser_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.P3_page)
        self.groupBox_2.setMinimumSize(QtCore.QSize(460, 0))
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.SL_p3_period = QtWidgets.QSlider(self.groupBox_2)
        self.SL_p3_period.setGeometry(QtCore.QRect(190, 80, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_p3_period.sizePolicy().hasHeightForWidth())
        self.SL_p3_period.setSizePolicy(sizePolicy)
        self.SL_p3_period.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_p3_period.setMinimum(10)
        self.SL_p3_period.setMaximum(100)
        self.SL_p3_period.setPageStep(1)
        self.SL_p3_period.setProperty("value", 10)
        self.SL_p3_period.setSliderPosition(10)
        self.SL_p3_period.setOrientation(QtCore.Qt.Horizontal)
        self.SL_p3_period.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_p3_period.setTickInterval(1)
        self.SL_p3_period.setObjectName("SL_p3_period")
        self.LB_25 = QtWidgets.QLabel(self.groupBox_2)
        self.LB_25.setGeometry(QtCore.QRect(50, 370, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_25.sizePolicy().hasHeightForWidth())
        self.LB_25.setSizePolicy(sizePolicy)
        self.LB_25.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_25.setObjectName("LB_25")
        self.LB_32 = QtWidgets.QLabel(self.groupBox_2)
        self.LB_32.setGeometry(QtCore.QRect(40, 80, 111, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_32.sizePolicy().hasHeightForWidth())
        self.LB_32.setSizePolicy(sizePolicy)
        self.LB_32.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_32.setObjectName("LB_32")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(10, 320, 391, 31))
        self.label_12.setObjectName("label_12")
        self.CB_p3_sel_filter = QtWidgets.QComboBox(self.groupBox_2)
        self.CB_p3_sel_filter.setGeometry(QtCore.QRect(170, 370, 161, 22))
        self.CB_p3_sel_filter.setEditable(False)
        self.CB_p3_sel_filter.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.CB_p3_sel_filter.setObjectName("CB_p3_sel_filter")
        self.CB_p3_sel_filter.addItem("")
        self.CB_p3_sel_filter.addItem("")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 241, 31))
        self.label_10.setObjectName("label_10")
        self.LC_p3_period = QtWidgets.QLCDNumber(self.groupBox_2)
        self.LC_p3_period.setGeometry(QtCore.QRect(390, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_p3_period.setFont(font)
        self.LC_p3_period.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_p3_period.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_p3_period.setLineWidth(5)
        self.LC_p3_period.setMidLineWidth(5)
        self.LC_p3_period.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_p3_period.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_p3_period.setProperty("intValue", 10)
        self.LC_p3_period.setObjectName("LC_p3_period")
        self.Bt_p3_fuyuan = QtWidgets.QToolButton(self.groupBox_2)
        self.Bt_p3_fuyuan.setEnabled(True)
        self.Bt_p3_fuyuan.setGeometry(QtCore.QRect(20, 590, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3_fuyuan.sizePolicy().hasHeightForWidth())
        self.Bt_p3_fuyuan.setSizePolicy(sizePolicy)
        self.Bt_p3_fuyuan.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3_fuyuan.setStyleSheet("\n"
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
        self.Bt_p3_fuyuan.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p3_fuyuan.setAutoRaise(False)
        self.Bt_p3_fuyuan.setObjectName("Bt_p3_fuyuan")
        self.Bt_p3_tuihua = QtWidgets.QToolButton(self.groupBox_2)
        self.Bt_p3_tuihua.setEnabled(True)
        self.Bt_p3_tuihua.setGeometry(QtCore.QRect(40, 210, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3_tuihua.sizePolicy().hasHeightForWidth())
        self.Bt_p3_tuihua.setSizePolicy(sizePolicy)
        self.Bt_p3_tuihua.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3_tuihua.setStyleSheet("\n"
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
        self.Bt_p3_tuihua.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p3_tuihua.setAutoRaise(False)
        self.Bt_p3_tuihua.setObjectName("Bt_p3_tuihua")
        self.LB_34 = QtWidgets.QLabel(self.groupBox_2)
        self.LB_34.setGeometry(QtCore.QRect(40, 150, 121, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_34.sizePolicy().hasHeightForWidth())
        self.LB_34.setSizePolicy(sizePolicy)
        self.LB_34.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_34.setObjectName("LB_34")
        self.SL_p3_amplitude = QtWidgets.QSlider(self.groupBox_2)
        self.SL_p3_amplitude.setGeometry(QtCore.QRect(190, 150, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_p3_amplitude.sizePolicy().hasHeightForWidth())
        self.SL_p3_amplitude.setSizePolicy(sizePolicy)
        self.SL_p3_amplitude.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_p3_amplitude.setMinimum(0)
        self.SL_p3_amplitude.setMaximum(100)
        self.SL_p3_amplitude.setPageStep(1)
        self.SL_p3_amplitude.setProperty("value", 1)
        self.SL_p3_amplitude.setSliderPosition(1)
        self.SL_p3_amplitude.setOrientation(QtCore.Qt.Horizontal)
        self.SL_p3_amplitude.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_p3_amplitude.setTickInterval(1)
        self.SL_p3_amplitude.setObjectName("SL_p3_amplitude")
        self.LC_p3_amplitude = QtWidgets.QLCDNumber(self.groupBox_2)
        self.LC_p3_amplitude.setGeometry(QtCore.QRect(390, 150, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_p3_amplitude.setFont(font)
        self.LC_p3_amplitude.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_p3_amplitude.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_p3_amplitude.setLineWidth(5)
        self.LC_p3_amplitude.setMidLineWidth(5)
        self.LC_p3_amplitude.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_p3_amplitude.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_p3_amplitude.setProperty("intValue", 1)
        self.LC_p3_amplitude.setObjectName("LC_p3_amplitude")
        self.LB_35 = QtWidgets.QLabel(self.groupBox_2)
        self.LB_35.setGeometry(QtCore.QRect(20, 430, 191, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_35.sizePolicy().hasHeightForWidth())
        self.LB_35.setSizePolicy(sizePolicy)
        self.LB_35.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_35.setObjectName("LB_35")
        self.SL_p3_filter_diode = QtWidgets.QSlider(self.groupBox_2)
        self.SL_p3_filter_diode.setGeometry(QtCore.QRect(230, 430, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_p3_filter_diode.sizePolicy().hasHeightForWidth())
        self.SL_p3_filter_diode.setSizePolicy(sizePolicy)
        self.SL_p3_filter_diode.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_p3_filter_diode.setMinimum(10)
        self.SL_p3_filter_diode.setMaximum(100)
        self.SL_p3_filter_diode.setPageStep(1)
        self.SL_p3_filter_diode.setProperty("value", 10)
        self.SL_p3_filter_diode.setSliderPosition(10)
        self.SL_p3_filter_diode.setOrientation(QtCore.Qt.Horizontal)
        self.SL_p3_filter_diode.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_p3_filter_diode.setTickInterval(1)
        self.SL_p3_filter_diode.setObjectName("SL_p3_filter_diode")
        self.LC_p3_diode = QtWidgets.QLCDNumber(self.groupBox_2)
        self.LC_p3_diode.setGeometry(QtCore.QRect(430, 430, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_p3_diode.setFont(font)
        self.LC_p3_diode.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_p3_diode.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_p3_diode.setLineWidth(5)
        self.LC_p3_diode.setMidLineWidth(5)
        self.LC_p3_diode.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_p3_diode.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_p3_diode.setProperty("intValue", 10)
        self.LC_p3_diode.setObjectName("LC_p3_diode")
        self.LC_p3_coordinateX = QtWidgets.QLCDNumber(self.groupBox_2)
        self.LC_p3_coordinateX.setGeometry(QtCore.QRect(430, 480, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_p3_coordinateX.setFont(font)
        self.LC_p3_coordinateX.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_p3_coordinateX.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_p3_coordinateX.setLineWidth(5)
        self.LC_p3_coordinateX.setMidLineWidth(5)
        self.LC_p3_coordinateX.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_p3_coordinateX.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_p3_coordinateX.setProperty("intValue", 1)
        self.LC_p3_coordinateX.setObjectName("LC_p3_coordinateX")
        self.SL_p3_filter_coordinateX = QtWidgets.QSlider(self.groupBox_2)
        self.SL_p3_filter_coordinateX.setGeometry(QtCore.QRect(230, 480, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_p3_filter_coordinateX.sizePolicy().hasHeightForWidth())
        self.SL_p3_filter_coordinateX.setSizePolicy(sizePolicy)
        self.SL_p3_filter_coordinateX.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_p3_filter_coordinateX.setMinimum(1)
        self.SL_p3_filter_coordinateX.setMaximum(100)
        self.SL_p3_filter_coordinateX.setPageStep(1)
        self.SL_p3_filter_coordinateX.setProperty("value", 1)
        self.SL_p3_filter_coordinateX.setSliderPosition(1)
        self.SL_p3_filter_coordinateX.setOrientation(QtCore.Qt.Horizontal)
        self.SL_p3_filter_coordinateX.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_p3_filter_coordinateX.setTickInterval(1)
        self.SL_p3_filter_coordinateX.setObjectName("SL_p3_filter_coordinateX")
        self.LB_36 = QtWidgets.QLabel(self.groupBox_2)
        self.LB_36.setGeometry(QtCore.QRect(20, 480, 201, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_36.sizePolicy().hasHeightForWidth())
        self.LB_36.setSizePolicy(sizePolicy)
        self.LB_36.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_36.setObjectName("LB_36")
        self.LC_p3_coordinateY = QtWidgets.QLCDNumber(self.groupBox_2)
        self.LC_p3_coordinateY.setGeometry(QtCore.QRect(430, 530, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_p3_coordinateY.setFont(font)
        self.LC_p3_coordinateY.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_p3_coordinateY.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_p3_coordinateY.setLineWidth(5)
        self.LC_p3_coordinateY.setMidLineWidth(5)
        self.LC_p3_coordinateY.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_p3_coordinateY.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_p3_coordinateY.setProperty("intValue", 1)
        self.LC_p3_coordinateY.setObjectName("LC_p3_coordinateY")
        self.SL_p3_filter_coordinateY = QtWidgets.QSlider(self.groupBox_2)
        self.SL_p3_filter_coordinateY.setGeometry(QtCore.QRect(230, 530, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_p3_filter_coordinateY.sizePolicy().hasHeightForWidth())
        self.SL_p3_filter_coordinateY.setSizePolicy(sizePolicy)
        self.SL_p3_filter_coordinateY.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_p3_filter_coordinateY.setMinimum(1)
        self.SL_p3_filter_coordinateY.setMaximum(100)
        self.SL_p3_filter_coordinateY.setPageStep(1)
        self.SL_p3_filter_coordinateY.setProperty("value", 1)
        self.SL_p3_filter_coordinateY.setSliderPosition(1)
        self.SL_p3_filter_coordinateY.setOrientation(QtCore.Qt.Horizontal)
        self.SL_p3_filter_coordinateY.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_p3_filter_coordinateY.setTickInterval(1)
        self.SL_p3_filter_coordinateY.setObjectName("SL_p3_filter_coordinateY")
        self.LB_37 = QtWidgets.QLabel(self.groupBox_2)
        self.LB_37.setGeometry(QtCore.QRect(70, 530, 141, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_37.sizePolicy().hasHeightForWidth())
        self.LB_37.setSizePolicy(sizePolicy)
        self.LB_37.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_37.setObjectName("LB_37")
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.P3_page, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 1, 1, 1)
        Ch5_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ch5_Window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Ch5_Window)

    def retranslateUi(self, Ch5_Window):
        _translate = QtCore.QCoreApplication.translate
        Ch5_Window.setWindowTitle(_translate("Ch5_Window", "Chapter 5 图像复原"))
        self.selectpicture.setText(_translate("Ch5_Window", "加载自定义图片"))
        self.LB_4.setText(_translate("Ch5_Window", "Part 1 原始图片"))
        self.RB_P1_self.setText(_translate("Ch5_Window", "使用自定义图片"))
        self.RB_P1_default.setText(_translate("Ch5_Window", "使用默认图片"))
        self.LB_1.setText(_translate("Ch5_Window", "图片信息："))
        self.textBrowser.setHtml(_translate("Ch5_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">PART2.空间域复原滤波</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">实验步骤：</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">一，给图像 添加 空间域加性噪声</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">1，选择噪声类型 并 设定相应参数</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">2，点击【进行退化】</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">注：必先进行退化，因为 后续复原是以退化结果为原材料的。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">二，空间域复原方法</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">1，选择空间与滤波类型：均值，谐波，逆谐波，统计排序，自适应（存在一定运算问题，时间可能会很长）</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">2，点击【进行复原】</span></p></body></html>"))
        self.Bt_p2_fuyuan.setText(_translate("Ch5_Window", "进行复原"))
        self.CB_p2_sel_filter.setItemText(0, _translate("Ch5_Window", "均值滤波"))
        self.CB_p2_sel_filter.setItemText(1, _translate("Ch5_Window", "谐波滤波"))
        self.CB_p2_sel_filter.setItemText(2, _translate("Ch5_Window", "逆谐波滤波"))
        self.CB_p2_sel_filter.setItemText(3, _translate("Ch5_Window", "统计排序滤波"))
        self.CB_p2_sel_filter.setItemText(4, _translate("Ch5_Window", "自适应滤波"))
        self.LB_24.setText(_translate("Ch5_Window", "选择滤波类型："))
        self.label_9.setText(_translate("Ch5_Window", "1，退化——加性噪声"))
        self.CB_p2_sel_noise.setItemText(0, _translate("Ch5_Window", "胡椒噪声"))
        self.CB_p2_sel_noise.setItemText(1, _translate("Ch5_Window", "盐噪声"))
        self.CB_p2_sel_noise.setItemText(2, _translate("Ch5_Window", "椒盐噪声"))
        self.CB_p2_sel_noise.setItemText(3, _translate("Ch5_Window", "高斯噪声"))
        self.LB_29.setText(_translate("Ch5_Window", "椒盐噪声：噪声占总空间比重"))
        self.LB_30.setText(_translate("Ch5_Window", "高斯噪声均值："))
        self.LB_31.setText(_translate("Ch5_Window", "%"))
        self.label_11.setText(_translate("Ch5_Window", "2，复原——空间滤波：将对以上的退化图像进行滤波"))
        self.LB_33.setText(_translate("Ch5_Window", "选择噪声类型："))
        self.Bt_p2_tuihua.setText(_translate("Ch5_Window", "进行退化"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.P2_page), _translate("Ch5_Window", "Part 2. 空间域复原滤波"))
        self.textBrowser_2.setHtml(_translate("Ch5_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">PART3.频率域复原滤波</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">实验步骤：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">本部分设计初衷是，首先定向加已知周期的噪声，以求在频率谱中能清晰地发现其影响，并通过复原中的陷波滤波带阻滤波等方法定向地消除噪声。难点在于精确地消除噪声。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">一，给图像 添加 频率域 正弦周期噪声</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">1，设定正弦噪声的周期和幅值，xy两轴向会对等产生正弦噪声进行叠加</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">2，点击【进行退化】，观察退化后的频谱图，可能会发现并没有预期那样只有X,Y轴上有亮点，而是其他部分也有成片的小部分光晕，这是因为叠加噪声时做的是加法，幅值太大时，超过了255，达到了限幅，这也就使得原本的理想正弦干扰，受限于限幅而发生了各种减损，波峰处成了不规则噪声，这势必引入更复杂丰富的频率分量，但是当你把幅值降到比较小，就可以看见比较完美的图了。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">注：必先进行退化，因为 后续复原是以退化结果为原材料的。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">二，空间域复原方法</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">1，带阻滤波和陷波滤波，带阻只有唯一的半径可设置，不过其针对定点频率的过滤效果会非常糟糕，因为他会把一圈都滤除，伤及无辜。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">而相比之下，陷波滤波可以只指定特定的频率点，精准消除噪声。注意：陷波半径表征的是以陷波点为圆心的衰减范围，而参数里是复用的，初值之所以设为10，是因为若陷波半径太小，会很难击中噪声。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">陷波坐标点：只允许设置在 X，Y轴上（正负半轴会自动对称生成陷波点），但关于坐标点该如何设置才能准确消除噪声 就需要 各位自行思考了（理论计算），需注意，退化施加噪声时设置的是“空间周期”，而陷波滤波作为频域滤波，设置的坐标点是在频域中，他们各自图像的单位是不一样的，例如空间噪声的周期虽然设置为10pixel,但陷波点的坐标肯定不是10，一定还跟图像的尺寸有关，且因图像的长宽不一样，虽然空间域里XY方向的噪声周期相等，但频率域时噪声点所在位置在两轴方向也会不同。图像尺寸可以在Part1中最下面图像信息处查看。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">2，点击【进行复原】</span></p></body></html>"))
        self.LB_25.setText(_translate("Ch5_Window", "滤波种类："))
        self.LB_32.setText(_translate("Ch5_Window", "正交噪声周期："))
        self.label_12.setText(_translate("Ch5_Window", "2，复原——频率域滤波：将对以上的退化图像进行滤波"))
        self.CB_p3_sel_filter.setItemText(0, _translate("Ch5_Window", "带阻滤波"))
        self.CB_p3_sel_filter.setItemText(1, _translate("Ch5_Window", "陷波滤波"))
        self.label_10.setText(_translate("Ch5_Window", "1，退化——手动添加周期性噪声"))
        self.Bt_p3_fuyuan.setText(_translate("Ch5_Window", "进行复原"))
        self.Bt_p3_tuihua.setText(_translate("Ch5_Window", "进行退化"))
        self.LB_34.setText(_translate("Ch5_Window", "正交噪声幅值："))
        self.LB_35.setText(_translate("Ch5_Window", "带阻/陷波 滤波直径D："))
        self.LB_36.setText(_translate("Ch5_Window", "陷波： X轴上陷波点坐标："))
        self.LB_37.setText(_translate("Ch5_Window", " Y轴上陷波点坐标："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.P3_page), _translate("Ch5_Window", "Part 3. 频率域复原滤波"))
