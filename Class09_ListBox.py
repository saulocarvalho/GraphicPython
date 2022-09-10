from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QListWidget
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("List Box")
        self.setFixedSize(QSize(400,300))

        lb = QListWidget()
        lb.addItems(['item 1', 'item 2', 'item 3'])

        lb.currentItemChanged.connect(self.index_changed)
        lb.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(lb)

    def index_changed(self, i):
            print(i.text())

    def text_changed(self, s):
            print(s)
            if s == "item 1":
                print('ok')
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()