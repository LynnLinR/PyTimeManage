import sys

from PyQt5.QtWidgets import QApplication

import Test

app = QApplication(sys.argv)
login = Test.Login()
app.exec()

if login.show():
    print("登录成功")
else:
    print("登录退出")
