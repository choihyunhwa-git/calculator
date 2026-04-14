# ch5.2.1 ui.py

from PyQt5.QtWidgets import ( QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox, QPlainTextEdit, QHBoxLayout,
                             QLineEdit, QComboBox)    
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit(self)
        self.te1.setReadOnly(True)

        self.button2 = QPushButton('Clear', self)
        self.button2.clicked.connect(self.clearMessage)

        self.button = QPushButton('Message', self)
        self.button.clicked.connect(self.activateMessage)

        self.le1 = QLineEdit('0',self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)

        self.le2 = QLineEdit('0',self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)

        self.combo = QComboBox(self)
        self.combo.addItems(['+', '-', '*', '/'])

        hbox_formula = QHBoxLayout()
        hbox_formula.addWidget(self.le1)
        hbox_formula.addWidget(self.combo)
        hbox_formula.addWidget(self.le2)

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.button)
        hbox.addWidget(self.button2)        

        vbox=QVBoxLayout()
        vbox.addWidget(self.te1)    
        vbox.addStretch(1)
        vbox.addLayout(hbox_formula)    
        vbox.addLayout(hbox)
        vbox.addStretch(1)


        self.setLayout(vbox)

        # self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Calculator')
        self.resize(256, 256)
        self.show()

    def activateMessage(self):
        # QMessageBox.information(self, 'Information', 'Button Clicked!')
        self.te1.appendPlainText('Button Clicked!') 

    def clearMessage(self):
        self.te1.clear()    

