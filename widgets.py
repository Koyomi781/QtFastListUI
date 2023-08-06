# -*- coding: utf-8 -*-
# @Time    : 2023/7/29 6:51

import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QApplication, QFrame
import webbrowser

from imgs_rc import *

class TestWidge(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('TEST')
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)


class TestWidget2(QWidget):
    def __init__ (self, parent = None):
        super(TestWidget2, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel    = QLabel()
        self.textDownQLabel  = QLabel()
        self.textDownQLabel.setText('IEJwiaejeo')
        self.textUpQLabel.setText('aejawehiahu')
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QHBoxLayout()
        self.iconQLabel      = QPushButton()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
     # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
        color: rgb(0, 0, 255);
     ''')
        self.textDownQLabel.setStyleSheet('''
         color: rgb(255, 0, 0);
     ''')


class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0,0,0,0)
        self.allLayout = QVBoxLayout()
        self.frame = QFrame()
        self.frame.setMinimumSize(600,600)
        self.frame.setStyleSheet('''
        QPushButton{
        background-color: rgb(255, 255, 255);
        font: 75 11pt "Microsoft YaHei UI";
        border: 2px solid black;
        border-radius:7px
        }
        QPushButton:hover{
            background-color: rgb(211, 211, 211);
        }
        ''')
        self.frame.setContentsMargins(11, 11, 11, 11)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(8)
        self.BL = QPushButton('哔哩哔哩')
        self.BL.setIcon(QtGui.QIcon(':/icon/uisource/source/bilibili.svg'))
        self.TT = QPushButton('推特')
        self.TT.setIcon(QtGui.QIcon(':/icon/uisource/source/icon-kfckfc.svg'))
        self.GH = QPushButton('GitHub')
        self.GH.setIcon(QtGui.QIcon(':/icon/uisource/source/github.svg'))
        self.layout.addWidget(self.BL)
        self.layout.addWidget(self.TT)
        self.layout.addWidget(self.GH)
        self.frame.setLayout(self.layout)
        self.allLayout.addWidget(self.frame, 10, Qt.AlignCenter)
        self.setLayout(self.allLayout)

        self.BL.clicked.connect(lambda: webbrowser.open('https://space.bilibili.com/178360345'))
        self.GH.clicked.connect(lambda: webbrowser.open('https://github.com/Koyomi781'))
        self.TT.clicked.connect(lambda: webbrowser.open('https://twitter.com/koyomi84937256'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = HomePage()
    win.show()
    sys.exit(app.exec_())