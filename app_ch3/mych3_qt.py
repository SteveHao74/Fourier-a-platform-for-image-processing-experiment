# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wide_mych3_qt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ch3_Window(object):
    def setupUi(self, Ch3_Window):
        Ch3_Window.setObjectName("Ch3_Window")
        Ch3_Window.setWindowModality(QtCore.Qt.ApplicationModal)
        Ch3_Window.resize(1595, 830)
        Ch3_Window.setMinimumSize(QtCore.QSize(800, 0))
        Ch3_Window.setMaximumSize(QtCore.QSize(1600, 1106))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        Ch3_Window.setFont(font)
        Ch3_Window.setAutoFillBackground(True)
        Ch3_Window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Ch3_Window)
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
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Box_p1.setFont(font)
        self.Box_p1.setAutoFillBackground(True)
        self.Box_p1.setTitle("")
        self.Box_p1.setObjectName("Box_p1")
        self.LB_1 = QtWidgets.QLabel(self.Box_p1)
        self.LB_1.setGeometry(QtCore.QRect(50, 640, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_1.sizePolicy().hasHeightForWidth())
        self.LB_1.setSizePolicy(sizePolicy)
        self.LB_1.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_1.setObjectName("LB_1")
        self.selectpicture = QtWidgets.QToolButton(self.Box_p1)
        self.selectpicture.setEnabled(True)
        self.selectpicture.setGeometry(QtCore.QRect(300, 110, 121, 41))
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
        self.information.setGeometry(QtCore.QRect(150, 640, 441, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.information.sizePolicy().hasHeightForWidth())
        self.information.setSizePolicy(sizePolicy)
        self.information.setMinimumSize(QtCore.QSize(311, 21))
        self.information.setObjectName("information")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Box_p1)
        self.scrollArea_2.setGeometry(QtCore.QRect(40, 170, 571, 421))
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
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LB_4.setFont(font)
        self.LB_4.setObjectName("LB_4")
        self.RB_P1_self = QtWidgets.QRadioButton(self.Box_p1)
        self.RB_P1_self.setGeometry(QtCore.QRect(70, 120, 141, 20))
        self.RB_P1_self.setObjectName("RB_P1_self")
        self.RB_P1_default = QtWidgets.QRadioButton(self.Box_p1)
        self.RB_P1_default.setGeometry(QtCore.QRect(70, 60, 115, 19))
        self.RB_P1_default.setChecked(True)
        self.RB_P1_default.setObjectName("RB_P1_default")
        self.gridLayout_4.addWidget(self.Box_p1, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(890, 700))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 933, 828))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setMinimumSize(QtCore.QSize(841, 650))
        self.tabWidget.setMaximumSize(QtCore.QSize(950, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(50, 50))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.P2_page = QtWidgets.QWidget()
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
        self.groupBox.setMinimumSize(QtCore.QSize(530, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(650, 16777215))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Bt_p2_run = QtWidgets.QToolButton(self.groupBox)
        self.Bt_p2_run.setEnabled(True)
        self.Bt_p2_run.setGeometry(QtCore.QRect(40, 750, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p2_run.sizePolicy().hasHeightForWidth())
        self.Bt_p2_run.setSizePolicy(sizePolicy)
        self.Bt_p2_run.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p2_run.setStyleSheet("\n"
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
        self.Bt_p2_run.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p2_run.setAutoRaise(False)
        self.Bt_p2_run.setObjectName("Bt_p2_run")
        self.CB_p2_select = QtWidgets.QComboBox(self.groupBox)
        self.CB_p2_select.setGeometry(QtCore.QRect(180, 20, 151, 22))
        self.CB_p2_select.setEditable(False)
        self.CB_p2_select.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.CB_p2_select.setObjectName("CB_p2_select")
        self.CB_p2_select.addItem("")
        self.CB_p2_select.addItem("")
        self.CB_p2_select.addItem("")
        self.CB_p2_select.addItem("")
        self.LB_24 = QtWidgets.QLabel(self.groupBox)
        self.LB_24.setGeometry(QtCore.QRect(30, 20, 121, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_24.sizePolicy().hasHeightForWidth())
        self.LB_24.setSizePolicy(sizePolicy)
        self.LB_24.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_24.setObjectName("LB_24")
        self.LC_p2_log = QtWidgets.QLCDNumber(self.groupBox)
        self.LC_p2_log.setGeometry(QtCore.QRect(440, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LC_p2_log.setFont(font)
        self.LC_p2_log.setStyleSheet("color: rgb(0, 0, 0);")
        self.LC_p2_log.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LC_p2_log.setLineWidth(5)
        self.LC_p2_log.setMidLineWidth(5)
        self.LC_p2_log.setMode(QtWidgets.QLCDNumber.Dec)
        self.LC_p2_log.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LC_p2_log.setProperty("intValue", 1)
        self.LC_p2_log.setObjectName("LC_p2_log")
        self.LB_26 = QtWidgets.QLabel(self.groupBox)
        self.LB_26.setGeometry(QtCore.QRect(30, 70, 131, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_26.sizePolicy().hasHeightForWidth())
        self.LB_26.setSizePolicy(sizePolicy)
        self.LB_26.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_26.setObjectName("LB_26")
        self.SL_p2_log = QtWidgets.QSlider(self.groupBox)
        self.SL_p2_log.setGeometry(QtCore.QRect(180, 70, 211, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_p2_log.sizePolicy().hasHeightForWidth())
        self.SL_p2_log.setSizePolicy(sizePolicy)
        self.SL_p2_log.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_p2_log.setMinimum(1)
        self.SL_p2_log.setMaximum(50)
        self.SL_p2_log.setPageStep(1)
        self.SL_p2_log.setProperty("value", 1)
        self.SL_p2_log.setSliderPosition(1)
        self.SL_p2_log.setOrientation(QtCore.Qt.Horizontal)
        self.SL_p2_log.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_p2_log.setTickInterval(1)
        self.SL_p2_log.setObjectName("SL_p2_log")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 280, 181, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(30, 120, 301, 31))
        self.label_10.setObjectName("label_10")
        self.sBox_p2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.sBox_p2.setGeometry(QtCore.QRect(360, 120, 91, 41))
        self.sBox_p2.setProperty("value", 1.0)
        self.sBox_p2.setObjectName("sBox_p2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 320, 441, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.VL_p2_chart = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.VL_p2_chart.setContentsMargins(0, 0, 0, 0)
        self.VL_p2_chart.setObjectName("VL_p2_chart")
        self.PX1 = QtWidgets.QSpinBox(self.groupBox)
        self.PX1.setGeometry(QtCore.QRect(155, 200, 51, 31))
        self.PX1.setMaximum(255)
        self.PX1.setProperty("value", 90)
        self.PX1.setObjectName("PX1")
        self.PY1 = QtWidgets.QSpinBox(self.groupBox)
        self.PY1.setGeometry(QtCore.QRect(155, 240, 51, 31))
        self.PY1.setMaximum(255)
        self.PY1.setProperty("value", 50)
        self.PY1.setObjectName("PY1")
        self.LB_29 = QtWidgets.QLabel(self.groupBox)
        self.LB_29.setGeometry(QtCore.QRect(30, 170, 321, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_29.sizePolicy().hasHeightForWidth())
        self.LB_29.setSizePolicy(sizePolicy)
        self.LB_29.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_29.setObjectName("LB_29")
        self.LB_30 = QtWidgets.QLabel(self.groupBox)
        self.LB_30.setGeometry(QtCore.QRect(70, 200, 61, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_30.sizePolicy().hasHeightForWidth())
        self.LB_30.setSizePolicy(sizePolicy)
        self.LB_30.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_30.setObjectName("LB_30")
        self.LB_31 = QtWidgets.QLabel(self.groupBox)
        self.LB_31.setGeometry(QtCore.QRect(70, 240, 61, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_31.sizePolicy().hasHeightForWidth())
        self.LB_31.setSizePolicy(sizePolicy)
        self.LB_31.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_31.setObjectName("LB_31")
        self.LB_32 = QtWidgets.QLabel(self.groupBox)
        self.LB_32.setGeometry(QtCore.QRect(250, 240, 61, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_32.sizePolicy().hasHeightForWidth())
        self.LB_32.setSizePolicy(sizePolicy)
        self.LB_32.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_32.setObjectName("LB_32")
        self.LB_33 = QtWidgets.QLabel(self.groupBox)
        self.LB_33.setGeometry(QtCore.QRect(250, 200, 61, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_33.sizePolicy().hasHeightForWidth())
        self.LB_33.setSizePolicy(sizePolicy)
        self.LB_33.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_33.setObjectName("LB_33")
        self.PY2 = QtWidgets.QSpinBox(self.groupBox)
        self.PY2.setGeometry(QtCore.QRect(330, 240, 51, 31))
        self.PY2.setMaximum(255)
        self.PY2.setProperty("value", 200)
        self.PY2.setObjectName("PY2")
        self.PX2 = QtWidgets.QSpinBox(self.groupBox)
        self.PX2.setGeometry(QtCore.QRect(330, 200, 51, 31))
        self.PX2.setMaximum(255)
        self.PX2.setProperty("value", 150)
        self.PX2.setObjectName("PX2")
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.tabWidget.addTab(self.P2_page, "")
        self.P3_page = QtWidgets.QWidget()
        self.P3_page.setObjectName("P3_page")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.P3_page)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.P3_page)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(300, 0))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.textBrowser_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(139, 255, 131);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_3.addWidget(self.textBrowser_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.P3_page)
        self.groupBox_2.setMinimumSize(QtCore.QSize(530, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.LB_25 = QtWidgets.QLabel(self.groupBox_2)
        self.LB_25.setGeometry(QtCore.QRect(20, 20, 131, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_25.sizePolicy().hasHeightForWidth())
        self.LB_25.setSizePolicy(sizePolicy)
        self.LB_25.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_25.setObjectName("LB_25")
        self.LB_27 = QtWidgets.QLabel(self.groupBox_2)
        self.LB_27.setGeometry(QtCore.QRect(30, 140, 131, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_27.sizePolicy().hasHeightForWidth())
        self.LB_27.setSizePolicy(sizePolicy)
        self.LB_27.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_27.setObjectName("LB_27")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea_3.setGeometry(QtCore.QRect(30, 320, 361, 321))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 422, 422))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LB_p3_pic = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_p3_pic.sizePolicy().hasHeightForWidth())
        self.LB_p3_pic.setSizePolicy(sizePolicy)
        self.LB_p3_pic.setMinimumSize(QtCore.QSize(400, 400))
        self.LB_p3_pic.setText("")
        self.LB_p3_pic.setObjectName("LB_p3_pic")
        self.gridLayout_2.addWidget(self.LB_p3_pic, 1, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.LB_28 = QtWidgets.QLabel(self.groupBox_2)
        self.LB_28.setGeometry(QtCore.QRect(30, 180, 241, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_28.sizePolicy().hasHeightForWidth())
        self.LB_28.setSizePolicy(sizePolicy)
        self.LB_28.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_28.setObjectName("LB_28")
        self.Bt_p3_selectpic = QtWidgets.QToolButton(self.groupBox_2)
        self.Bt_p3_selectpic.setEnabled(True)
        self.Bt_p3_selectpic.setGeometry(QtCore.QRect(230, 250, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3_selectpic.sizePolicy().hasHeightForWidth())
        self.Bt_p3_selectpic.setSizePolicy(sizePolicy)
        self.Bt_p3_selectpic.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3_selectpic.setStyleSheet("\n"
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
        self.Bt_p3_selectpic.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p3_selectpic.setAutoRaise(False)
        self.Bt_p3_selectpic.setObjectName("Bt_p3_selectpic")
        self.RB_P3_default = QtWidgets.QRadioButton(self.groupBox_2)
        self.RB_P3_default.setGeometry(QtCore.QRect(30, 220, 115, 19))
        self.RB_P3_default.setChecked(True)
        self.RB_P3_default.setObjectName("RB_P3_default")
        self.RB_P3_self = QtWidgets.QRadioButton(self.groupBox_2)
        self.RB_P3_self.setGeometry(QtCore.QRect(30, 260, 181, 20))
        self.RB_P3_self.setObjectName("RB_P3_self")
        self.Bt_p3_match = QtWidgets.QToolButton(self.groupBox_2)
        self.Bt_p3_match.setEnabled(True)
        self.Bt_p3_match.setGeometry(QtCore.QRect(60, 670, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3_match.sizePolicy().hasHeightForWidth())
        self.Bt_p3_match.setSizePolicy(sizePolicy)
        self.Bt_p3_match.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3_match.setStyleSheet("\n"
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
        self.Bt_p3_match.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p3_match.setAutoRaise(False)
        self.Bt_p3_match.setObjectName("Bt_p3_match")
        self.Bt_p3_equal = QtWidgets.QToolButton(self.groupBox_2)
        self.Bt_p3_equal.setEnabled(True)
        self.Bt_p3_equal.setGeometry(QtCore.QRect(40, 70, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3_equal.sizePolicy().hasHeightForWidth())
        self.Bt_p3_equal.setSizePolicy(sizePolicy)
        self.Bt_p3_equal.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3_equal.setStyleSheet("\n"
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
        self.Bt_p3_equal.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p3_equal.setAutoRaise(False)
        self.Bt_p3_equal.setObjectName("Bt_p3_equal")
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.P3_page, "")
        self.P4_page = QtWidgets.QWidget()
        self.P4_page.setObjectName("P4_page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.P4_page)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.P4_page)
        self.textBrowser_3.setMinimumSize(QtCore.QSize(300, 0))
        self.textBrowser_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.textBrowser_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(139, 255, 131);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout_2.addWidget(self.textBrowser_3)
        self.groupBox_6 = QtWidgets.QGroupBox(self.P4_page)
        self.groupBox_6.setMinimumSize(QtCore.QSize(530, 0))
        self.groupBox_6.setMaximumSize(QtCore.QSize(650, 16777215))
        self.groupBox_6.setAutoFillBackground(True)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.CB_p4_smo = QtWidgets.QComboBox(self.groupBox_6)
        self.CB_p4_smo.setGeometry(QtCore.QRect(200, 30, 231, 22))
        self.CB_p4_smo.setEditable(False)
        self.CB_p4_smo.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.CB_p4_smo.setObjectName("CB_p4_smo")
        self.CB_p4_smo.addItem("")
        self.CB_p4_smo.addItem("")
        self.CB_p4_smo.addItem("")
        self.RB_P4_smooth = QtWidgets.QRadioButton(self.groupBox_6)
        self.RB_P4_smooth.setGeometry(QtCore.QRect(20, 30, 115, 19))
        self.RB_P4_smooth.setChecked(False)
        self.RB_P4_smooth.setObjectName("RB_P4_smooth")
        self.RB_P4_sharp = QtWidgets.QRadioButton(self.groupBox_6)
        self.RB_P4_sharp.setGeometry(QtCore.QRect(20, 100, 121, 20))
        self.RB_P4_sharp.setObjectName("RB_P4_sharp")
        self.RB_P4_self = QtWidgets.QRadioButton(self.groupBox_6)
        self.RB_P4_self.setGeometry(QtCore.QRect(20, 170, 401, 20))
        self.RB_P4_self.setChecked(True)
        self.RB_P4_self.setObjectName("RB_P4_self")
        self.CB_p4_sha = QtWidgets.QComboBox(self.groupBox_6)
        self.CB_p4_sha.setGeometry(QtCore.QRect(200, 100, 231, 22))
        self.CB_p4_sha.setEditable(False)
        self.CB_p4_sha.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.CB_p4_sha.setObjectName("CB_p4_sha")
        self.CB_p4_sha.addItem("")
        self.CB_p4_sha.addItem("")
        self.CB_p4_sha.addItem("")
        self.CB_p4_sha.addItem("")
        self.CB_p4_sha.addItem("")
        self.Bt_p4_run = QtWidgets.QToolButton(self.groupBox_6)
        self.Bt_p4_run.setEnabled(True)
        self.Bt_p4_run.setGeometry(QtCore.QRect(50, 480, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p4_run.sizePolicy().hasHeightForWidth())
        self.Bt_p4_run.setSizePolicy(sizePolicy)
        self.Bt_p4_run.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p4_run.setStyleSheet("\n"
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
        self.Bt_p4_run.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p4_run.setAutoRaise(False)
        self.Bt_p4_run.setObjectName("Bt_p4_run")
        self.widget = QtWidgets.QWidget(self.groupBox_6)
        self.widget.setGeometry(QtCore.QRect(30, 230, 198, 186))
        self.widget.setStyleSheet("border:1px solid #1B89CA;")
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sBox_11 = QtWidgets.QSpinBox(self.widget)
        self.sBox_11.setMinimumSize(QtCore.QSize(50, 50))
        self.sBox_11.setMinimum(-50)
        self.sBox_11.setMaximum(50)
        self.sBox_11.setObjectName("sBox_11")
        self.gridLayout_3.addWidget(self.sBox_11, 0, 0, 1, 1)
        self.sBox_12 = QtWidgets.QSpinBox(self.widget)
        self.sBox_12.setMinimumSize(QtCore.QSize(50, 50))
        self.sBox_12.setMinimum(-50)
        self.sBox_12.setMaximum(50)
        self.sBox_12.setObjectName("sBox_12")
        self.gridLayout_3.addWidget(self.sBox_12, 0, 1, 1, 1)
        self.sBox_13 = QtWidgets.QSpinBox(self.widget)
        self.sBox_13.setMinimumSize(QtCore.QSize(50, 50))
        self.sBox_13.setMinimum(-50)
        self.sBox_13.setMaximum(50)
        self.sBox_13.setObjectName("sBox_13")
        self.gridLayout_3.addWidget(self.sBox_13, 0, 2, 1, 1)
        self.sBox_21 = QtWidgets.QSpinBox(self.widget)
        self.sBox_21.setMinimumSize(QtCore.QSize(50, 50))
        self.sBox_21.setMinimum(-50)
        self.sBox_21.setMaximum(50)
        self.sBox_21.setObjectName("sBox_21")
        self.gridLayout_3.addWidget(self.sBox_21, 1, 0, 1, 1)
        self.sBox_22 = QtWidgets.QSpinBox(self.widget)
        self.sBox_22.setMinimumSize(QtCore.QSize(50, 50))
        self.sBox_22.setMinimum(-50)
        self.sBox_22.setMaximum(50)
        self.sBox_22.setObjectName("sBox_22")
        self.gridLayout_3.addWidget(self.sBox_22, 1, 1, 1, 1)
        self.sBox_23 = QtWidgets.QSpinBox(self.widget)
        self.sBox_23.setMinimumSize(QtCore.QSize(50, 50))
        self.sBox_23.setMinimum(-50)
        self.sBox_23.setMaximum(50)
        self.sBox_23.setObjectName("sBox_23")
        self.gridLayout_3.addWidget(self.sBox_23, 1, 2, 1, 1)
        self.sBox_31 = QtWidgets.QSpinBox(self.widget)
        self.sBox_31.setMinimumSize(QtCore.QSize(50, 50))
        self.sBox_31.setMinimum(-50)
        self.sBox_31.setMaximum(50)
        self.sBox_31.setObjectName("sBox_31")
        self.gridLayout_3.addWidget(self.sBox_31, 2, 0, 1, 1)
        self.sBox_32 = QtWidgets.QSpinBox(self.widget)
        self.sBox_32.setMinimumSize(QtCore.QSize(50, 50))
        self.sBox_32.setMinimum(-50)
        self.sBox_32.setMaximum(50)
        self.sBox_32.setObjectName("sBox_32")
        self.gridLayout_3.addWidget(self.sBox_32, 2, 1, 1, 1)
        self.sBox_33 = QtWidgets.QSpinBox(self.widget)
        self.sBox_33.setMinimumSize(QtCore.QSize(50, 50))
        self.sBox_33.setMinimum(-50)
        self.sBox_33.setMaximum(50)
        self.sBox_33.setObjectName("sBox_33")
        self.gridLayout_3.addWidget(self.sBox_33, 2, 2, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        self.tabWidget.addTab(self.P4_page, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 1, 1, 1)
        Ch3_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ch3_Window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Ch3_Window)

    def retranslateUi(self, Ch3_Window):
        _translate = QtCore.QCoreApplication.translate
        Ch3_Window.setWindowTitle(_translate("Ch3_Window", "Chapter 3 ?????????????????????"))
        self.LB_1.setText(_translate("Ch3_Window", "???????????????"))
        self.selectpicture.setText(_translate("Ch3_Window", "?????????????????????"))
        self.LB_4.setText(_translate("Ch3_Window", "Part 1 ?????????????????????"))
        self.RB_P1_self.setText(_translate("Ch3_Window", "?????????????????????"))
        self.RB_P1_default.setText(_translate("Ch3_Window", "??????????????????"))
        self.textBrowser.setHtml(_translate("Ch3_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">PART2:????????????</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">???????????????</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">1???????????????????????????????????????????????????????????????????????????????????????????????????</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">2??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">????????????????????????????????????C???<br />?????????????????????????????????????????????????????????????????????????????????????????????n??????????????????</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">????????????:?????????????????????????????????????????????????????????????????????????????? ??????????????????????????? ??? ???????????????????????????????????????????????????????????????</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">3?????????????????????????????????????????? ???PART1??????</span></p></body></html>"))
        self.Bt_p2_run.setText(_translate("Ch3_Window", "????????????"))
        self.CB_p2_select.setItemText(0, _translate("Ch3_Window", "????????????"))
        self.CB_p2_select.setItemText(1, _translate("Ch3_Window", "????????????"))
        self.CB_p2_select.setItemText(2, _translate("Ch3_Window", "????????????"))
        self.CB_p2_select.setItemText(3, _translate("Ch3_Window", "????????????"))
        self.LB_24.setText(_translate("Ch3_Window", "?????????????????????"))
        self.LB_26.setText(_translate("Ch3_Window", "?????????????????? C???"))
        self.label_9.setText(_translate("Ch3_Window", "????????????????????????????????????"))
        self.label_10.setText(_translate("Ch3_Window", "???????????? L??????????????????????????????????????????"))
        self.LB_29.setText(_translate("Ch3_Window", "???????????????????????????????????????0-255?????????"))
        self.LB_30.setText(_translate("Ch3_Window", "???1   X???"))
        self.LB_31.setText(_translate("Ch3_Window", "???1   Y???"))
        self.LB_32.setText(_translate("Ch3_Window", "???2   Y???"))
        self.LB_33.setText(_translate("Ch3_Window", "???2   X???"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.P2_page), _translate("Ch3_Window", "Part 2. ????????????"))
        self.textBrowser_2.setHtml(_translate("Ch3_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">PART3:???????????????</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">???????????????</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">1??????????????????????????????????????? ????????????????????????????????????????????????????????????????????????????????????????????????????????????</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">??????????????????</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">1????????????????????? ?????????????????????????????????????????????????????????????????????????????????</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">2?????????????????????????????????????????? ???PART1??????</span></p></body></html>"))
        self.LB_25.setText(_translate("Ch3_Window", "1.??????????????????"))
        self.LB_27.setText(_translate("Ch3_Window", "2.???????????????"))
        self.LB_28.setText(_translate("Ch3_Window", "??????????????????????????????????????????"))
        self.Bt_p3_selectpic.setText(_translate("Ch3_Window", "?????????????????????"))
        self.RB_P3_default.setText(_translate("Ch3_Window", "??????????????????"))
        self.RB_P3_self.setText(_translate("Ch3_Window", "?????????????????????"))
        self.Bt_p3_match.setText(_translate("Ch3_Window", "????????????"))
        self.Bt_p3_equal.setText(_translate("Ch3_Window", "???????????? "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.P3_page), _translate("Ch3_Window", "Part 3. ???????????????"))
        self.textBrowser_3.setHtml(_translate("Ch3_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">PART4:????????????????????????</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">???????????????</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">??????????????????????????????????????????</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">1?????????????????????????????????????????? ??????</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">2??????????????????Roberts,Prewitt,Sobel??????????????????Canny???????????????????????????????????????????????????????????????</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">3????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-weight:400;\"><br /></p></body></html>"))
        self.CB_p4_smo.setItemText(0, _translate("Ch3_Window", "???????????????"))
        self.CB_p4_smo.setItemText(1, _translate("Ch3_Window", "???????????????(????????????)"))
        self.CB_p4_smo.setItemText(2, _translate("Ch3_Window", "???????????????"))
        self.RB_P4_smooth.setText(_translate("Ch3_Window", "????????????"))
        self.RB_P4_sharp.setText(_translate("Ch3_Window", "????????????"))
        self.RB_P4_self.setText(_translate("Ch3_Window", "???????????????????????????????????????????????????,???3x3?????????"))
        self.CB_p4_sha.setItemText(0, _translate("Ch3_Window", "??????-Roberts??????????????????"))
        self.CB_p4_sha.setItemText(1, _translate("Ch3_Window", "??????-Prewitt????????????"))
        self.CB_p4_sha.setItemText(2, _translate("Ch3_Window", "??????-Sobel????????????"))
        self.CB_p4_sha.setItemText(3, _translate("Ch3_Window", "??????-??????????????????"))
        self.CB_p4_sha.setItemText(4, _translate("Ch3_Window", "Canny??????????????????"))
        self.Bt_p4_run.setText(_translate("Ch3_Window", "?????????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.P4_page), _translate("Ch3_Window", "Part 4. ????????????????????????"))

