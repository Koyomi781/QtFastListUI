# -*- coding: utf-8 -*-
# @Time    : 2023/7/29 6:04
from PyQt5.QtCore import QSize

from Mainui import *
from PyQt5.QtWidgets import QMainWindow, QListWidget, QListWidgetItem

from widgets import *


class AddRightButton(QPushButton):
    def __init__(self, btname, item):
        super(AddRightButton, self).__init__(parent= None)
        self.item = item
        self.setObjectName('rightbtn')
        self.setCheckable(True)
        self.setChecked(True)
        self.setMinimumHeight(50)
        self.setIcon(QtGui.QIcon(':/icon/uisource/source/向右.svg'))
        self.toggled.connect(self.icon_change)
        self.setText(btname)

    def icon_change(self):
        if self.isChecked():
            self.setIcon(QtGui.QIcon(':/icon/uisource/source/向右.svg'))
        else:
            self.setIcon(QtGui.QIcon(':/icon/uisource/source/向下.svg'))

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(AddRightButton, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))


class AddRightItem(QListWidget):
    def __init__(self, btnames: list, widgets: list):
        super().__init__()
        # 不可选中和无焦点（即无虚线框）
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.setFocusPolicy(Qt.NoFocus)

        # 添加item
        for btname, widget in zip(btnames, widgets):
            btn_item = QListWidgetItem(self)
            btn = AddRightButton(btname, btn_item)
            btn_item.setSizeHint(btn.sizeHint())
            self.addItem(btn_item)
            self.setItemWidget(btn_item, btn)

            # 添加折叠窗口
            wgt_item = QListWidgetItem(self)
            wgt_item.setSizeHint(widget().sizeHint())
            wgt_item.setHidden(True)
            btn.toggled.connect(wgt_item.setHidden)
            self.addItem(wgt_item)
            self.setItemWidget(wgt_item, widget())

            # 空白item 增加间距
            block_item = QListWidgetItem(self)
            self.addItem(block_item)


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.title.setText('Title')
        # self.setWindowOpacity(0.99)  # 设置窗口透明度
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 添加阴影
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(1, 1)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(Qt.gray)
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.ui.stackedWidget.setContentsMargins(5, 11, 5, 0)

        # 右侧窗口初始化
        self.RightWidgetInit()

        # 登录位置
        self.ui.user.setIcon(QtGui.QIcon(':/icon/uisource/source/无效用户.svg'))
        self.ui.user.setText('您未登录')
        self.ui.user.setCursor(Qt.PointingHandCursor)

        self.SetQss()
        self.show()


    # 初始化右侧页面
    def RightWidgetInit(self):
        self.vlayout = QVBoxLayout()
        self.vlayout.setContentsMargins(0, 10, 0, 0)

        # 添加普通页面
        self.AddLeftItem('首页', ':/icon/uisource/source/首页A.svg', HomePage())

        # 添加列表页面
        # 1
        test_page_item = AddRightItem(['test', 'test2'], [TestWidge, TestWidget2])
        self.AddLeftItem('test', ':/icon/uisource/source/退出登录.svg', test_page_item)

        # 2
        test1_page_item = AddRightItem(['test', 'test2'], [TestWidge, TestWidget2])
        self.AddLeftItem('test1', ':/icon/uisource/source/无效用户.svg', test1_page_item)

        # 3
        test2_page_item = AddRightItem(['test', 'test2'], [TestWidge, TestWidget2])
        self.AddLeftItem('test2', ':/icon/uisource/source/取消（关闭）.svg', test2_page_item)

        self.vlayout.addStretch()

    # 添加侧边栏按钮，并绑定右侧页面
    def AddLeftItem(self, btname: str, icon_path: str, widget):
        # 侧边栏按钮
        btn = QPushButton()
        btn.setIcon(QtGui.QIcon(icon_path))
        btn.setMinimumHeight(50)
        btn.setCheckable(True)
        btn.setAutoExclusive(True)
        btn.setText(btname)
        # 事件绑定
        btn.toggled.connect(lambda: self.GoPage(widget))
        self.vlayout.addWidget(btn)
        self.ui.left.setLayout(self.vlayout)

    # 跳转右侧页面
    def GoPage(self, widget):
        self.ui.stackedWidget.addWidget(widget)
        self.ui.stackedWidget.setCurrentWidget(widget)

    # 全局QSS
    def SetQss(self):
        with open(f'uisource/demo.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            super(MainWin, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    def mouseMoveEvent(self, event):
        try:
            if self.start_y <= 86:
                super(MainWin, self).mouseMoveEvent(event)
                dis_x = event.x() - self.start_x
                dis_y = event.y() - self.start_y
                self.move(self.x() + dis_x, self.y() + dis_y)
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    sys.exit(app.exec_())
