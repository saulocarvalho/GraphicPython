from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QSlider, QDial
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Qslider")
        self.setFixedSize(QSize(400,300))

        dial = QDial()
        dial.setRange(0,100)
        dial.setSingleStep(0.5)

        dial.valueChanged.connect(self.value_changed)
        dial.sliderMoved.connect(self.slider_position)
        dial.sliderPressed.connect(self.slider_pressed)
        dial.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(dial)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print('position', p)
    
    def slider_pressed(self):
        print('pressed')
    
    def slider_released(self):
        print('released')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()