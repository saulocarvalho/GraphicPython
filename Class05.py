from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import Qt, QSize

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Aula 05")

        Widget = QLabel("Aula 05 - Label")
        font = Widget.font()
        font.setPointSize(35)
        Widget.setFont(font)


        self.setFixedSize(QSize(400,300))
        Widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(Widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()