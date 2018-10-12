
import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi


class Login(QDialog):
    '''测试'''

    def __init__(self, * args):
        super(Login, self).__init__(*args)
        loadUi('Login.ui', self)
        self.labelTips.hide()
        self.pushButtonOK.clicked.connect(self.slotLogin)
        self.pushButtonCancle.clicked.connect(self.close)

    def slotLogin(self):
        if self.lineEditUser.text() != "admin" or self.lineEditPasswd.text() != "123456":
            self.labelTips.show()
            # self.labelTips.setText("用户名或密码错误！")
        else:
            self.accept()  # 调用主界面，同时进行访客记录

    def closeEvent(self, event):  # 关闭QWidget父类时自动调用的函数
        reply = QMessageBox.question(
            self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
