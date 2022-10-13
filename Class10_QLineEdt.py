from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QListWidget, QLineEdit
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit")
        self.setFixedSize(QSize(400,300))

        self.le = QLineEdit()
        self.le.setMaxLength(10)
        self.le.setPlaceholderText('Enter your name')

        self.le.returnPressed.connect(self.return_pressed)
        self.le.selectionChanged.connect(self.selection_changed)
        self.le.textChanged.connect(self.text_changed)
        self.le.textEdited.connect(self.text_edited)
        
        self.le.setInputMask('000.000.000-00;_')

        self.setCentralWidget(self.le)
    
    def return_pressed(self):
        print('Botão Clicado')
        self.centralWidget().setText(f"Olá {self.le.text()}")

    def selection_changed(self):
        print('Changed selection')
        print(self.centralWidget().selectedText())
    
    def text_changed(self,s):
        print('Text changed')
        print(s)
    
    def text_edited(self, s):
        print('text edited...')
        print(s)
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()