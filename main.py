#ch 4.2.1 main.py
import sys
from PyQt5.QtWidgets import ( QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox, QPlainTextEdit)   
from PyQt5.QtGui import QIcon

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit(self)
        self.te1.setReadOnly(True)

        self.button = QPushButton('Message', self)
        self.button.clicked.connect(self.activateMessage)

        vbox=QVBoxLayout()
        vbox.addWidget(self.te1)    
        vbox.addStretch(1)
        vbox.addWidget(self.button)
        vbox.addStretch(1)

        self.setLayout(vbox)

        # self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Calculator')
        self.resize(256, 256)
        self.show()

    def activateMessage(self):
        # QMessageBox.information(self, 'Information', 'Button Clicked!')
        self.te1.appendPlainText('Button Clicked!') 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())

        
