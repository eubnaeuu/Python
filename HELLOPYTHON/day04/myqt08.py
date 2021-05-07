
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from numpy import random

form_class = uic.loadUiType("myqt08.ui")[0]
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        dan = int(self.le.text())
        str = ""
        for i in range(1,10):
            # str += dan + " x " + i + " = " + dan*i
            str += "{} x {} = {}\n".format(dan,i,dan*i)   
        self.tb.setText(str)
        
if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = MyWindow()
   myWindow.show()
   sys.exit(app.exec_())
   
   
   
   