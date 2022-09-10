from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Combo Box")
        self.setFixedSize(QSize(400,300))

        self.widget = QComboBox()
        self.widget.addItems(['item 1', 'item 2', 'item 3'])

        self.widget.currentIndexChanged.connect(self.index_change)
        self.widget.currentTextChanged.connect(self.text_change)

        self.setCentralWidget(self.widget)

    def index_change(self, i):
        print(i)

    def text_change(self, s):
        print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()