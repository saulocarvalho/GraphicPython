from textwrap import shorten
from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame, QLineEdit, QPushButton
from PySide2.QtCore import Qt, QSize
import sys
import pyshorteners

from layout_color import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QvBoxLayout")
        self.resize(QSize(400,300))
        #Resize pode seta um tamanho para a tela, mas não é fixo

        layout = QVBoxLayout()

        self.frame = QFrame()

        self.link = QLineEdit(self.frame)
        self.link.setPlaceholderText('Paste your URL here')

        self.btn = QPushButton(self.frame)
        self.btn.setText('Do it')

        self.result = QLineEdit(self.frame)

        self.frame.setLayout(layout)
        layout.addWidget(self.link)
        layout.addWidget(self.btn)
        layout.addWidget(self.result)

        self.btn.clicked.connect(self.link_shortener)

        self.setCentralWidget(self.frame)


    def link_shortener(self):
        short = pyshorteners.Shortener()
        new_link = short.tinyurl.short(self.link.text())
        self.result.setText(new_link)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()