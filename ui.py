# ch5.2.1 ui.py

from PyQt5.QtWidgets import ( QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox, QPlainTextEdit, QHBoxLayout, QLabel)   
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, Qt


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate() #현재날짜 저장
        self.initUI()

    def initUI(self):
        self.label = QLabel(self.date.toString(Qt.DefaultLocaleLongDate), self)
        self.te1 = QPlainTextEdit(self)
        self.te1.setReadOnly(True)

        self.button2 = QPushButton('Clear', self)
        self.button2.clicked.connect(self.clearMessage)

        self.button = QPushButton('Message', self)
        self.button.clicked.connect(self.activateMessage)

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.button)
        hbox.addWidget(self.button2)        

        vbox=QVBoxLayout()
        vbox.addWidget(self.te1)    
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addWidget(self.label)  


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

