from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Aula 06")

        Widget = QLabel("Pixmap")
        Widget.setPixmap(QPixmap("Ant_1.jpg"))
        Widget.setScaledContents(True)

        self.setCentralWidget(Widget)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()