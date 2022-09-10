from re import S
from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Aula 06")
        ck = QCheckBox("Check if true")
        ck.setCheckState(Qt.Checked)
        ck.stateChanged.connect(self.show_State)
        ck.setCheckState(Qt.PartiallyChecked)
        
        self.setCentralWidget(ck)

    def show_State(self,s):
        print(s == Qt.Checked)
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()