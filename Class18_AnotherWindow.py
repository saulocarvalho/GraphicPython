from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from PySide2.QtCore import Qt, QSize
import sys

from layout_color import Color

class AnotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Second Window')
        self.resize(QSize(400,300))

        layout = QVBoxLayout()
        self.label = QLabel('Another Window')
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setCentralWidget(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QDialog")
        self.resize(QSize(400,300))
        self.button = QPushButton("Click Here")
        self.button.clicked.connect(self.show_window)

        self.setCentralWidget(self.button)
    
    def show_window(self,c):
        self.w = AnotherWindow()
        self.w.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()