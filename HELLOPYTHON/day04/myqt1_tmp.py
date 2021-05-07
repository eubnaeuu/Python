import sys
from PyQt5 import QtWidgets ,uic
from PyQt5.QtWidgets import QLabel, QPushButton

class Form(QtWidgets.QDialog):
 def __init__(self):
  super().__init__()
  self.ui = uic.loadUi("myqt01.ui") #ui 파일 불러오기
  # self.pb.clicked.connect(self.btnClick())
  self.ui.show()

 def btnClick(self):
        print("버튼클릭중")

if __name__ == '__main__':
 app = QtWidgets.QApplication(sys.argv)
 w = Form()
 sys.exit(app.exec())