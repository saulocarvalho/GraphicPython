from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
from PySide2.QtCore import Qt, QSize
import sys

from layout_color import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QHBoxLayout")
        self.resize(QSize(400,300))


        self.setCentralWidget(Widget)

        #Aula pausada no minuto 0:27



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()