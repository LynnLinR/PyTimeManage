import sys

from PyQt5.QtWidgets import QApplication, QDialog

import Login
import mainwindow


def main():
    app = QApplication(sys.argv)
    login = Login.Login()
    if login.exec_() == QDialog.Accepted:
        ex = mainwindow.MessageBox()
        ex.show()
        app.exec_()
        # 生成可执行程序时加上,给父进程一个返回值表示退出状态
        # sys.exit(app.exec_())


if __name__ == '__main__':
    main()
