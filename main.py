import sys

from PyQt5.QtWidgets import QApplication, QDialog

import Login
import mainwindow

# mainwindow.main()
app = QApplication(sys.argv)
login = Login.Login()
if login.exec_() == QDialog.Accepted:
    ex = mainwindow.MessageBox()
    ex.show()
    app.exec_()
