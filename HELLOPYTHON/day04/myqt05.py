
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from numpy import random

form_class = uic.loadUiType("myqt05.ui")[0]
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        strMine = self.lemine.text()
        ran = random.random()
        if(ran<0.5):
            strCom = "홀"
        else:
            strCom = "짝"
        self.lecom.setText(strCom)
        if(strCom==strMine):
            self.leresult.setText("승")
        else:
            self.leresult.setText("패")

if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = MyWindow()
   myWindow.show()
   sys.exit(app.exec_())
   
   
   
   