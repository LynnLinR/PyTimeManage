
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import Login


class MessageBox(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        loadUi('mainfile.ui', self)


def main():
    app = QApplication(sys.argv)
    ex = MessageBox()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
