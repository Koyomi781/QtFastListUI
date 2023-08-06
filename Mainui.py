# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1268, 864)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QFrame#frame_2{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"QPushButton{\n"
"    border:none;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setStyleSheet("font: 18pt \"微软雅黑\";")
        self.title.setText("")
        self.title.setObjectName("title")
        self.horizontalLayout_2.addWidget(self.title)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.user = QtWidgets.QPushButton(self.frame)
        self.user.setStyleSheet("QPushButton{\n"
"    font: 10pt \"微软雅黑\";\n"
"    color: rgb(84, 84, 84);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.user.setObjectName("user")
        self.horizontalLayout_2.addWidget(self.user)
        self.logout = QtWidgets.QPushButton(self.frame)
        self.logout.setText("")
        self.logout.setObjectName("logout")
        self.horizontalLayout_2.addWidget(self.logout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.minsize = QtWidgets.QPushButton(self.frame)
        self.minsize.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:3px;\n"
"    padding-left:3px;\n"
"}")
        self.minsize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/uisource/source/减去（无框）.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minsize.setIcon(icon)
        self.minsize.setIconSize(QtCore.QSize(25, 30))
        self.minsize.setObjectName("minsize")
        self.horizontalLayout_2.addWidget(self.minsize)
        self.close = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy)
        self.close.setMaximumSize(QtCore.QSize(100, 30))
        self.close.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:3px;\n"
"    padding-left:3px;\n"
"}")
        self.close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/uisource/source/取消（关闭）.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon1)
        self.close.setIconSize(QtCore.QSize(30, 30))
        self.close.setObjectName("close")
        self.horizontalLayout_2.addWidget(self.close)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy)
        self.left.setStyleSheet("")
        self.left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left.setObjectName("left")
        self.horizontalLayout.addWidget(self.left)
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.right = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy)
        self.right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right.setObjectName("right")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.right)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.right)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.right)
        self.line.raise_()
        self.left.raise_()
        self.right.raise_()
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_2.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close.clicked.connect(MainWindow.close)
        self.minsize.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

import imgs_rc
