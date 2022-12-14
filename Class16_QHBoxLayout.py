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

        layout = QHBoxLayout()
        layout.addWidget(Color('green'))
        layout.addWidget(Color('white'))
        layout.addWidget(Color('red'))

        widget = QWidget()
        widget.setLayout(layout)




        self.setCentralWidget(widget)





app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()