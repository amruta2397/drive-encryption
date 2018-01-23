from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os

class Encryption_Window(QWidget):
    def __init__(self):
        super(Encryption_Window, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(600,400)

        self.cmb = QComboBox()
        self.cmb.addItem("Select USB Drive Properly")

        layout.addWidget(self.cmb)

        button = QPushButton("Format")
        #self.button.addButton(button)
        layout.addWidget(button)

        self.pwdlabel = QLabel("Enter Password")
        layout.addWidget(self.pwdlabel)
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password)

        self.cnfpwdlabel = QLabel("Confirm Password")
        layout.addWidget(self.cnfpwdlabel)
        self.confirmpassword = QLineEdit()
        self.confirmpassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirmpassword)

        button = QPushButton("Enter Password")
        #self.button.addButton(button)
        layout.addWidget(button)



def run():
    app = QApplication(sys.argv)
    screen = Encryption_Window()
    screen.show()
    sys.exit(app.exec_())

run()


