"""
研究PyQt5用的代码
通过这个代码和tkinter进行对比。
试着一边学习一边开发桌面应用

作者：Lynn Lin
最后一次编辑：2018/9/17
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QPushButton, QMessageBox, QDesktopWidget


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setToolTip('this is <b>QMainWindow</b>')

        # 按钮提示框
        btn = QPushButton('Button', self)
        btn.setToolTip('this is <b>QPushButton</b>')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # 信号与槽
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(self.close)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 100)

        self.setGeometry(300, 300, 300, 200)
        self.resize(250, 150)
        self.center()

        self.statusBar().showMessage('Ready')

        # menubar = self.menuBar()
        # WorkMenu = menubar.addMenu('&Work')
        # WorkMenu.addAction(exitAction)

        self.setWindowTitle('main widget')
        self.show()

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


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()

    # sys.exit(app.exec_())
    app.exec_()
