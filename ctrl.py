#ch 5.2.1 ctrl.py

class Control:
    
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def connectSignals(self):
        self.view.button.clicked.connect(self.view.activateMessage)
        self.view.button2.clicked.connect(self.view.clearMessage)

        
