# pyuic5 design.ui -o design.py -> p/ converter .ui em .py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap  # p/ abrir as imgs
from design import *


class Resize(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnOpenImg.clicked.connect(self.open_file_img)

    def open_file_img(self):
        img, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Arquivo de Imagem',
            r'C:\Users\MF\Pictures'
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    resize = Resize()
    resize.show()
    qt.exec_()
