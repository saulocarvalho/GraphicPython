from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My First App")

        self.button = QPushButton("Click here!")

        self.setFixedSize(QSize(400,300))

        self.setCentralWidget(self.button)

        self.button.clicked.connect(self.clicked_button)


    def clicked_button(self):
        print("You clicked the button!")
        self.button.setEnabled(False)
        self.setWindowTitle("Just One Click")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()