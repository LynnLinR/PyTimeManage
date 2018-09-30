"""
研究PyQt5用的代码
通过这个代码和tkinter进行对比。
试着一边学习一边开发桌面应用

作者：Lynn Lin
最后一次编辑：2018/9/29
"""
import sys
from PyQt5.QtWidgets import *
from MyMessageBox import MessageBox


class Example(QWidget):
    # close_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # self.setToolTip('this is <b>QWidget</b>')

        btn = QPushButton('Strat', self)
        btn.resize(btn.sizeHint())

        qbtn = QPushButton('Quit', self)
        qbtn.resize(qbtn.sizeHint())

        # 按钮提示框
        btn.setToolTip('Start the time')

        # 按钮位置
        btn.move(50, 50)
        qbtn.move(50, 100)

        # 信号与槽
        btn.clicked.connect(self.onclick)
        qbtn.clicked.connect(self.close)

        self.resize(250, 150)
        self.center()
        self.setWindowTitle('main widget')

    def center(self):
        qr = self.frameGeometry()  # 获取父类的几何形状
        cp = QDesktopWidget().availableGeometry().center()  # QDesktopWidget获取桌面窗口信息
        qr.moveCenter(cp)  # 将形状放在移动到桌面中央
        self.move(qr.topLeft())  # 获取形状的左上角位置，写入父类

    def closeEvent(self, event):  # 关闭QWidget父类时自动调用的函数
        reply = QMessageBox.question(
            self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def onclick(self):
        newWindow = MessageBox()
        newWindow.handle_click(self)

# def showMessageBox():
#     view = new MyMessageBox(this)
#     view.main()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()
    ex.show()

    # sys.exit(app.exec_())
    app.exec_()
