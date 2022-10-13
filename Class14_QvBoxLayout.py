from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide2.QtCore import Qt, QSize
import sys

from layout_color import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QvBoxLayout")
        #self.setFixedSize(QSize(400,300))

        layout = QVBoxLayout()

        layout.addWidget(Color('black'))
        layout.addWidget(Color('red'))
        layout.addWidget(Color('yellow'))
        layout.addWidget(Color('white'))

        Widget = QWidget()
        Widget.setLayout(layout)

        self.setCentralWidget(Widget)





app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()