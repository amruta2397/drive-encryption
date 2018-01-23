from  PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Encryption_window import Encryption_Window
from AddNewKey_window import AddNewKey_Window
from DeleteExistingKey_window import DeleteKey_Window
from PyQt5.Qt import *
import sys
import os

class Main_Window(QWidget):
    def __init__(self):
        super(Main_Window, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(400, 300)

        self.encrpyt = QRadioButton("Encrypt the USB Drives")
        self.encrpyt.setCheckable(True)
        self.encrpyt.setChecked(False)
        layout.addWidget(self.encrpyt)

        self.add_new_key = QRadioButton("Add New Key")
        self.add_new_key.setCheckable(True)
        self.add_new_key.setChecked(False)
        layout.addWidget(self.add_new_key)

        self.delete_key = QRadioButton("Delete Existing Key")
        self.delete_key.setCheckable(True)
        self.delete_key.setChecked(False)
        layout.addWidget(self.delete_key)

        self.encrpyt.toggled.connect(self.Encrypt)
        self.add_new_key.toggled.connect(self.AddNewKey)
        self.delete_key.toggled.connect(self.DeleteKey)



    def Encrypt(self):
        if self.encrpyt.isChecked():
            self.window = QWidget.QMainWindow()
            self.encryption1 = Encryption_Window()
            self.window.show()


    def AddNewKey(self):
        if self.add_new_key.isChecked():
            self.window = QWidget.QMainWindow()
            self.encryption1 = AddNewKey_Window()
            self.window.show()


    def DeleteKey(self):
        if self.delete_key.isChecked():
            self.window = QWidget.QMainWindow()
            self.encryption1 = DeleteKey_Window()
            self.window.show()




def run():
        app = QApplication(sys.argv)
        screen = Main_Window()
        screen.show()
        sys.exit(app.exec_())

run()