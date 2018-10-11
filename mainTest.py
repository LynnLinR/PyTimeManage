import sys
from PyQt5.QtWidgets import QApplication
import Test

app = QApplication(sys.argv)
login = Test.Login()
if login.exec():
    print("登录成功")
else:
    print("登录退出")
sys.exit(app.exec())