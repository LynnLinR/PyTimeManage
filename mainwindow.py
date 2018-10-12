"""
弹窗测试用

作者：Lynn Lin
最后一次编辑：2018/9/29
"""
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QDialog
import sys

import Login


class MessageBox(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.resize(400, 150)
        self.center()
        self.setStyleSheet("background: black")

        self.setWindowTitle('main widget')

    def center(self):
        qr = self.frameGeometry()  # 获取父类的几何形状
        cp = QDesktopWidget().availableGeometry().center()  # QDesktopWidget获取桌面窗口信息
        qr.moveCenter(cp)  # 将形状放在移动到桌面中央
        self.move(qr.topLeft())  # 获取形状的左上角位置，写入父类


def main():
    # app = QApplication(sys.argv)
    # ex = MessageBox()
    # ex.show()
    # app.exec_()

    app = QApplication(sys.argv)
    login = Login.Login()
    if login.exec_() == QDialog.Accepted:
        ex = MessageBox()
        ex.show()
        app.exec_()


if __name__ == '__main__':
    main()
