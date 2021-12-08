# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mych9_qt.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ch9_Window(object):
    def setupUi(self, Ch9_Window):
        Ch9_Window.setObjectName("Ch9_Window")
        Ch9_Window.resize(939, 909)
        Ch9_Window.setMinimumSize(QtCore.QSize(900, 0))
        Ch9_Window.setMaximumSize(QtCore.QSize(950, 1106))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Ch9_Window.setFont(font)
        Ch9_Window.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ch9_Window.setWindowIcon(icon)
        Ch9_Window.setAutoFillBackground(True)
        Ch9_Window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Ch9_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(1, 0, 941, 911))
        self.scrollArea.setMinimumSize(QtCore.QSize(870, 900))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.HLine)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(5)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -180, 900, 1200))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget_P1 = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget_P1.setMinimumSize(QtCore.QSize(831, 600))
        self.tabWidget_P1.setAutoFillBackground(True)
        self.tabWidget_P1.setObjectName("tabWidget_P1")
        self.P11_page = QtWidgets.QWidget()
        self.P11_page.setObjectName("P11_page")
        self.groupBox_3 = QtWidgets.QGroupBox(self.P11_page)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 891, 571))
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.information = QtWidgets.QTextBrowser(self.groupBox_3)
        self.information.setGeometry(QtCore.QRect(290, 470, 441, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.information.sizePolicy().hasHeightForWidth())
        self.information.setSizePolicy(sizePolicy)
        self.information.setMinimumSize(QtCore.QSize(311, 21))
        self.information.setObjectName("information")
        self.selectpicture = QtWidgets.QToolButton(self.groupBox_3)
        self.selectpicture.setEnabled(True)
        self.selectpicture.setGeometry(QtCore.QRect(50, 120, 141, 41))
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
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_3)
        self.scrollArea_2.setGeometry(QtCore.QRect(260, 60, 521, 381))
        self.scrollArea_2.setMinimumSize(QtCore.QSize(521, 381))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 622, 622))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout.setObjectName("formLayout")
        self.LB_pic_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_pic_1.sizePolicy().hasHeightForWidth())
        self.LB_pic_1.setSizePolicy(sizePolicy)
        self.LB_pic_1.setMinimumSize(QtCore.QSize(600, 600))
        self.LB_pic_1.setText("")
        self.LB_pic_1.setObjectName("LB_pic_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.LB_pic_1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.LB_1 = QtWidgets.QLabel(self.groupBox_3)
        self.LB_1.setGeometry(QtCore.QRect(120, 470, 81, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_1.sizePolicy().hasHeightForWidth())
        self.LB_1.setSizePolicy(sizePolicy)
        self.LB_1.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_1.setObjectName("LB_1")
        self.tabWidget_P1.addTab(self.P11_page, "")
        self.P12_page = QtWidgets.QWidget()
        self.P12_page.setObjectName("P12_page")
        self.groupBox_4 = QtWidgets.QGroupBox(self.P12_page)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 901, 571))
        self.groupBox_4.setAutoFillBackground(True)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.P12_pixmap = QtWidgets.QGroupBox(self.groupBox_4)
        self.P12_pixmap.setGeometry(QtCore.QRect(280, 0, 621, 511))
        self.P12_pixmap.setTitle("")
        self.P12_pixmap.setObjectName("P12_pixmap")
        self.gridLayoutWidget = QtWidgets.QWidget(self.P12_pixmap)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.GL_PM_P12 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.GL_PM_P12.setContentsMargins(0, 0, 0, 0)
        self.GL_PM_P12.setObjectName("GL_PM_P12")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 0, 261, 511))
        self.textBrowser_3.setStyleSheet("\n"
"\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(139, 255, 131);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.P12savepicture = QtWidgets.QToolButton(self.groupBox_4)
        self.P12savepicture.setEnabled(True)
        self.P12savepicture.setGeometry(QtCore.QRect(670, 520, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P12savepicture.sizePolicy().hasHeightForWidth())
        self.P12savepicture.setSizePolicy(sizePolicy)
        self.P12savepicture.setMinimumSize(QtCore.QSize(81, 21))
        self.P12savepicture.setStyleSheet("\n"
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
        self.P12savepicture.setObjectName("P12savepicture")
        self.Bt_p1clear = QtWidgets.QToolButton(self.groupBox_4)
        self.Bt_p1clear.setEnabled(True)
        self.Bt_p1clear.setGeometry(QtCore.QRect(430, 520, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p1clear.sizePolicy().hasHeightForWidth())
        self.Bt_p1clear.setSizePolicy(sizePolicy)
        self.Bt_p1clear.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p1clear.setAutoFillBackground(False)
        self.Bt_p1clear.setStyleSheet("\n"
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
        self.Bt_p1clear.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p1clear.setAutoRaise(False)
        self.Bt_p1clear.setObjectName("Bt_p1clear")
        self.tabWidget_P1.addTab(self.P12_page, "")
        self.gridLayout.addWidget(self.tabWidget_P1, 0, 0, 1, 1)
        self.tabWidget_P2 = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget_P2.setMinimumSize(QtCore.QSize(841, 600))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_P2.setFont(font)
        self.tabWidget_P2.setAutoFillBackground(True)
        self.tabWidget_P2.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_P2.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_P2.setIconSize(QtCore.QSize(50, 50))
        self.tabWidget_P2.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget_P2.setObjectName("tabWidget_P2")
        self.P2_page = QtWidgets.QWidget()
        self.P2_page.setObjectName("P2_page")
        self.textBrowser = QtWidgets.QTextBrowser(self.P2_page)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 321, 641))
        self.textBrowser.setStyleSheet("font: 9pt \"Roman\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(139, 255, 131);")
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(self.P2_page)
        self.groupBox.setGeometry(QtCore.QRect(320, 0, 581, 701))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.check_p2 = QtWidgets.QCheckBox(self.groupBox)
        self.check_p2.setGeometry(QtCore.QRect(20, 360, 361, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.check_p2.setFont(font)
        self.check_p2.setObjectName("check_p2")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 301, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 100, 200, 200))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_5)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 201, 201))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.GL_KL = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.GL_KL.setContentsMargins(0, 0, 0, 0)
        self.GL_KL.setObjectName("GL_KL")
        self.CB_P2 = QtWidgets.QComboBox(self.groupBox)
        self.CB_P2.setGeometry(QtCore.QRect(300, 100, 111, 21))
        self.CB_P2.setEditable(False)
        self.CB_P2.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.CB_P2.setObjectName("CB_P2")
        self.CB_P2.addItem("")
        self.CB_P2.addItem("")
        self.CB_P2.addItem("")
        self.CB_P2.addItem("")
        self.Bt_p2run = QtWidgets.QToolButton(self.groupBox)
        self.Bt_p2run.setEnabled(True)
        self.Bt_p2run.setGeometry(QtCore.QRect(30, 440, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p2run.sizePolicy().hasHeightForWidth())
        self.Bt_p2run.setSizePolicy(sizePolicy)
        self.Bt_p2run.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p2run.setAutoFillBackground(False)
        self.Bt_p2run.setStyleSheet("\n"
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
        self.Bt_p2run.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p2run.setAutoRaise(False)
        self.Bt_p2run.setObjectName("Bt_p2run")
        self.LB_9 = QtWidgets.QLabel(self.groupBox)
        self.LB_9.setGeometry(QtCore.QRect(30, 50, 471, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_9.sizePolicy().hasHeightForWidth())
        self.LB_9.setSizePolicy(sizePolicy)
        self.LB_9.setMinimumSize(QtCore.QSize(45, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LB_9.setFont(font)
        self.LB_9.setStyleSheet("border:5px;border-color: green")
        self.LB_9.setObjectName("LB_9")
        self.LB_10 = QtWidgets.QLabel(self.groupBox)
        self.LB_10.setGeometry(QtCore.QRect(20, 330, 181, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_10.sizePolicy().hasHeightForWidth())
        self.LB_10.setSizePolicy(sizePolicy)
        self.LB_10.setMinimumSize(QtCore.QSize(45, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LB_10.setFont(font)
        self.LB_10.setObjectName("LB_10")
        self.tabWidget_P2.addTab(self.P2_page, "")
        self.P3_page = QtWidgets.QWidget()
        self.P3_page.setObjectName("P3_page")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.P3_page)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 301, 701))
        self.textBrowser_2.setStyleSheet("font: 9pt \"Roman\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(139, 255, 131);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.P3_page)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 0, 601, 751))
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.check_p3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_p3.setGeometry(QtCore.QRect(20, 40, 341, 41))
        self.check_p3.setObjectName("check_p3")
        self.Bt_p3holefill = QtWidgets.QToolButton(self.groupBox_2)
        self.Bt_p3holefill.setEnabled(True)
        self.Bt_p3holefill.setGeometry(QtCore.QRect(30, 220, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_p3holefill.sizePolicy().hasHeightForWidth())
        self.Bt_p3holefill.setSizePolicy(sizePolicy)
        self.Bt_p3holefill.setMinimumSize(QtCore.QSize(81, 21))
        self.Bt_p3holefill.setStyleSheet("\n"
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
        self.Bt_p3holefill.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.Bt_p3holefill.setAutoRaise(False)
        self.Bt_p3holefill.setObjectName("Bt_p3holefill")
        self.LC_3 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.LC_3.setGeometry(QtCore.QRect(330, 150, 51, 31))
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
        self.LC_3.setProperty("intValue", 1)
        self.LC_3.setObjectName("LC_3")
        self.SL_3 = QtWidgets.QSlider(self.groupBox_2)
        self.SL_3.setGeometry(QtCore.QRect(170, 150, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SL_3.sizePolicy().hasHeightForWidth())
        self.SL_3.setSizePolicy(sizePolicy)
        self.SL_3.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.SL_3.setMinimum(1)
        self.SL_3.setMaximum(20)
        self.SL_3.setPageStep(1)
        self.SL_3.setProperty("value", 1)
        self.SL_3.setSliderPosition(1)
        self.SL_3.setOrientation(QtCore.Qt.Horizontal)
        self.SL_3.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.SL_3.setTickInterval(1)
        self.SL_3.setObjectName("SL_3")
        self.LB_p3 = QtWidgets.QLabel(self.groupBox_2)
        self.LB_p3.setGeometry(QtCore.QRect(50, 150, 111, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_p3.sizePolicy().hasHeightForWidth())
        self.LB_p3.setSizePolicy(sizePolicy)
        self.LB_p3.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_p3.setStyleSheet("border:5px;border-color: green")
        self.LB_p3.setObjectName("LB_p3")
        self.LB_p3_2 = QtWidgets.QLabel(self.groupBox_2)
        self.LB_p3_2.setGeometry(QtCore.QRect(410, 150, 111, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_p3_2.sizePolicy().hasHeightForWidth())
        self.LB_p3_2.setSizePolicy(sizePolicy)
        self.LB_p3_2.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_p3_2.setStyleSheet("border:5px;border-color: green")
        self.LB_p3_2.setObjectName("LB_p3_2")
        self.LB_p3_3 = QtWidgets.QLabel(self.groupBox_2)
        self.LB_p3_3.setGeometry(QtCore.QRect(50, 100, 371, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_p3_3.sizePolicy().hasHeightForWidth())
        self.LB_p3_3.setSizePolicy(sizePolicy)
        self.LB_p3_3.setMinimumSize(QtCore.QSize(45, 16))
        self.LB_p3_3.setStyleSheet("border:5px;border-color: green")
        self.LB_p3_3.setObjectName("LB_p3_3")
        self.tabWidget_P2.addTab(self.P3_page, "")
        self.gridLayout.addWidget(self.tabWidget_P2, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        Ch9_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ch9_Window)
        self.tabWidget_P1.setCurrentIndex(1)
        self.tabWidget_P2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Ch9_Window)

    def retranslateUi(self, Ch9_Window):
        _translate = QtCore.QCoreApplication.translate
        Ch9_Window.setWindowTitle(_translate("Ch9_Window", "chapter 9. 形态学基础 "))
        self.selectpicture.setText(_translate("Ch9_Window", "选择自定义图片"))
        self.LB_1.setText(_translate("Ch9_Window", "图片信息："))
        self.tabWidget_P1.setTabText(self.tabWidget_P1.indexOf(self.P11_page), _translate("Ch9_Window", "Part 1.1 导入图片"))
        self.textBrowser_3.setHtml(_translate("Ch9_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roman\'; font-size:10pt;\">第九章 形态学基础</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roman\'; font-size:10pt; font-weight:600;\">实验内容：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roman\'; font-size:10pt;\">PART1 : 亲手绘制像素图/导入图片 以供后续处理</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roman\'; font-size:10pt;\">PART2: 形态学基础操作</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roman\'; font-size:10pt;\">PART3: 孔洞填充</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roman\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roman\'; font-size:10pt; font-weight:600;\">PART1 : 亲手绘制像素图/导入图片 以供后续处理</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roman\'; font-size:10pt; font-weight:600;\">1，通过顶栏 可以切换 自定义图片的方式：手绘和导入图片，当前停留的界面所对应的图像将被作为后续处理的对象</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roman\'; font-size:10pt; font-weight:600;\">2，手绘像素格：可通过单次点击选中像素块，使其变白色（代表形态学中的1），再次点击则变成黑色（形态学中的0），不可通过按住选中（待开发）。可点击【完全擦出】，或点击【保存图像】到电脑本地。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roman\'; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roman\'; font-size:10pt; font-weight:600;\"><br /></p></body></html>"))
        self.P12savepicture.setText(_translate("Ch9_Window", "保存图像"))
        self.Bt_p1clear.setText(_translate("Ch9_Window", "完全擦除"))
        self.tabWidget_P1.setTabText(self.tabWidget_P1.indexOf(self.P12_page), _translate("Ch9_Window", "Part 1.2手绘像素格"))
        self.tabWidget_P2.setStyleSheet(_translate("Ch9_Window", "\n"
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
        self.textBrowser.setHtml(_translate("Ch9_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roman\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">PART2 形态学基础操作</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">实验步骤：</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">1，自定义结构元：请先生成特定大小的基础轮廓（右侧可选，如3*3，点击基础生成即可），之后左键选择具体像素格为黑色“1”，右键可定义锚点（原点），其余为白色“0”</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">2，基础操作包括：腐蚀，膨胀，求边界，开，闭操作：当勾选自定义图片时，操作对象将由part1当前停留页面提供图片(如停留在“Part 1.2手绘像素格”，则将处理手绘图)</span></p></body></html>"))
        self.check_p2.setText(_translate("Ch9_Window", "是否自定义图片（默认使用软件自带图片）"))
        self.label_8.setText(_translate("Ch9_Window", "腐蚀，膨胀，开，闭操作"))
        self.CB_P2.setItemText(0, _translate("Ch9_Window", "    2*2"))
        self.CB_P2.setItemText(1, _translate("Ch9_Window", "    3*3"))
        self.CB_P2.setItemText(2, _translate("Ch9_Window", "    4*4"))
        self.CB_P2.setItemText(3, _translate("Ch9_Window", "    5*5"))
        self.Bt_p2run.setText(_translate("Ch9_Window", "基础操作"))
        self.LB_9.setText(_translate("Ch9_Window", "1，手绘定制结构元  注：后续的part都将沿用这个自制结构元"))
        self.LB_10.setText(_translate("Ch9_Window", "2，基础操作"))
        self.tabWidget_P2.setTabText(self.tabWidget_P2.indexOf(self.P2_page), _translate("Ch9_Window", "Part2.形态学基础操作"))
        self.textBrowser_2.setHtml(_translate("Ch9_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roman\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">PART3 孔洞填充</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">实验步骤：</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600;\">本部分将拆解展示孔洞填充的迭代过程，可通过滑条设置观测的频率，如每5次迭代观测一次，可以观察到每次迭代过程中 图像被膨胀的情况，背景慢慢被填充满，最后只剩下前景，再取反实际上就用曲线救国的方式实现了孔洞填充。但是有一个问题，这种方法高度依赖前景的轮廓和边界，把它作为一个护城河，防止膨胀到内部，但这种防御能成立的前提是，结构元的“半径”要小于轮廓厚度，否则，根本防不住，最后不会有任何效果</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Ch9_Window", "Part3.孔洞填充"))
        self.check_p3.setText(_translate("Ch9_Window", "是否自定义图片（默认使用软件自带图片）"))
        self.Bt_p3holefill.setText(_translate("Ch9_Window", "孔洞填充"))
        self.LB_p3.setText(_translate("Ch9_Window", "设置观测间隔："))
        self.LB_p3_2.setText(_translate("Ch9_Window", "次迭代"))
        self.LB_p3_3.setText(_translate("Ch9_Window", "此部分结构元将延用part2中的自定义结构元"))
        self.tabWidget_P2.setTabText(self.tabWidget_P2.indexOf(self.P3_page), _translate("Ch9_Window", "Part3.孔洞填充"))
