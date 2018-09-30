from PyQt5
def center(self):
        qr = self.frameGeometry()  # 获取父类的几何形状
        cp = QDesktopWidget().availableGeometry().center()  # QDesktopWidget获取桌面窗口信息
        qr.moveCenter(cp)  # 将形状放在移动到桌面中央
        self.move(qr.topLeft())  # 获取形状的左上角位置，写入父类
