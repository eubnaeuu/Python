
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from numpy import random

form_class = uic.loadUiType("myqt09.ui")[0]
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn0.clicked.connect(lambda: self.btnClick("0"))
        self.btn1.clicked.connect(lambda: self.btnClick("1"))
        self.btn2.clicked.connect(lambda: self.btnClick("2"))
        self.btn3.clicked.connect(lambda: self.btnClick("3"))
        self.btn4.clicked.connect(lambda: self.btnClick("4"))
        self.btn5.clicked.connect(lambda: self.btnClick("5"))
        self.btn6.clicked.connect(lambda: self.btnClick("6"))
        self.btn7.clicked.connect(lambda: self.btnClick("7"))
        self.btn8.clicked.connect(lambda: self.btnClick("8"))
        self.btn9.clicked.connect(lambda: self.btnClick("9"))
        self.btnCall.clicked.connect(self.btnCallClick)
        
    str = "";
     
    def btnClick(self, num):
        str = self.tf.toPlainText()
        str+= num
        self.tf.setPlainText(str)
    
    def btnCallClick(self):
        str = self.tf.toPlainText()
        QMessageBox.question(self, 'calling~', str, QMessageBox.Yes, QMessageBox.NoButton)
       
        
if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = MyWindow()
   myWindow.show()
   sys.exit(app.exec_())
   
   
   
   