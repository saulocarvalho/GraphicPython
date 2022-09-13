from tkinter import Widget
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QDialog, QPushButton, QMessageBox
from PySide2.QtCore import Qt, QSize
import sys

from layout_color import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QDialog")
        self.resize(QSize(400,300))
        self.button = QPushButton("Click Here")


        self.setCentralWidget(self.button)

        #self.button.clicked.connect(self.clicked_button)
        self.button.clicked.connect(self.clicked_button2)
#botao_sim = mensagem.button(QMessageBox.Yes)
        #botao_sim.setText('Sim')
        #Para alterar o nome dos botões

    def clicked_button(self):
        #d = QDialog(self)
        #d.setWindowTitle('Hello')
        #d.exec_()
        msg = QMessageBox(self)
        msg.setWindowTitle('I have a question!')
        msg.setText("This is a simple dialog")
        #msg.setIcon(QMessageBox.Question)
        #msg.setIcon(QMessageBox.Information)
        #msg.setIcon(QMessageBox.Critical)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_( )

    def clicked_button2(self):
        msg = QMessageBox(self)
        msg.setWindowTitle('I have a question!')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        msg.setText("This is a simple dialog")
        msg.setIcon(QMessageBox.Warning)
        result = msg.exec_( )

        if result == QMessageBox.Yes:
            print('Yes')
        else:
            print('No')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()