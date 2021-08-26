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
        self.btnResize.clicked.connect(self.resize_img)

    def open_file_img(self):
        img_path, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Arquivo de Imagem',
            r'C:\Users\MF\Pictures'
        )
        self.inputFileImg.setText(img_path)
        self.original_img = QPixmap(img_path)
        self.labelImg.setPixmap(self.original_img)
        self.inputWidth.setText(str(self.original_img.width()))
        self.inputHeight.setText(str(self.original_img.height()))

    def resize_img(self):
        width = int(self.inputWidth.text())
        self.new_img = self.original_img.scaledToWidth(width)
        self.labelImg.setPixmap(self.new_img)
        self.inputWidth.setText(str(self.new_img.width()))
        self.inputHeight.setText(str(self.new_img.height()))



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    resize = Resize()
    resize.show()
    qt.exec_()
