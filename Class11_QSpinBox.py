from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QspinBox")
        self.setFixedSize(QSize(400,300))

        self.spin = QSpinBox()
        self.spin = QDoubleSpinBox()
        #A diferença entra Spin é número inteiro e doublespin flutuante
        self.spin.setMinimum(-5)
        self.spin.setMaximum(5)
        self.spin.setPrefix('R$ ')
        self.spin.setSuffix(' C')

        self.spin.valueChanged.connect(self.value_changed)
        self.spin.valueChanged[str].connect(self.value_changed_str)
       
        self.setCentralWidget(self.spin)

    def value_changed(self, i):
        print(i)
    
    def value_changed_str(self, s):
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()