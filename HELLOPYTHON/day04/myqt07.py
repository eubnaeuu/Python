
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from numpy import random

form_class = uic.loadUiType("myqt07.ui")[0]
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        strMine = self.lemine.text()
        
        ran = random.random()
        print(ran)
        if(ran<(1/3)):
            strCom = "가위"
        elif(ran<(2/3)):
            strCom = "바위"
        else:
            strCom = "보"
            
        self.lecom.setText(strCom)
        result = ""
        draw = "비김"
        win = "승"
        loose = "패"
        
        if((strMine=="가위") and (strCom=="가위")): 
            result = draw
        if((strMine=="가위") and (strCom=="바위")): 
            result = loose
        if((strMine=="가위") and (strCom=="보")): 
            result = win
            
        if((strMine=="바위") and (strCom=="가위")): 
            result = win
        if((strMine=="바위") and (strCom=="바위")): 
            result = draw
        if((strMine=="바위") and (strCom=="보")):
            result = loose
            
        if((strMine=="보") and (strCom=="가위")): 
            result = loose
        if((strMine=="보") and (strCom=="바위")): 
            result = win
        if((strMine=="보") and (strCom=="보")):
            result = draw
        
        self.leresult.setText(result)
        
if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = MyWindow()
   myWindow.show()
   sys.exit(app.exec_())
   
   
   
   