"""
弹窗测试用

作者：Lynn Lin
最后一次编辑：2018/9/29
"""
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget
import sys


class MessageBox(QWidget):
    def __init__(self, parent=None):
        super(MessageBox, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # self.setGeometry(300, 300, 300, 200)
        self.resize(400, 150)
        self.center()
        self.setStyleSheet("background: black")

        self.setWindowTitle('message widget')
        # self.show()

    def handle_click(self, parent=None):
        if not self.isVisible():
            parent.widget = MessageBox()
            parent.widget.show()
            # self.show()
            # self.exec_()

    def handle_close(self):
        self.close()

    def center(self):
        qr = self.frameGeometry()  # 获取父类的几何形状
        cp = QDesktopWidget().availableGeometry().center()  # QDesktopWidget获取桌面窗口信息
        qr.moveCenter(cp)  # 将形状放在移动到桌面中央
        self.move(qr.topLeft())  # 获取形状的左上角位置，写入父类


def main():
    app = QApplication(sys.argv)
    ex = MessageBox()
    app.exec_()


if __name__ == '__main__':
    main()
