
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic, QtGui
from qtconsole.qstringhelpers import qstring_length

form_class = uic.loadUiType("myqt01.ui")[0]
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.idx = 0
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        self.idx += 1
        loc_idx = self.idx % 3
        self.pb.setIcon(QtGui.QIcon(str(loc_idx)+'.png'))

if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = MyWindow()
   myWindow.show()
   sys.exit(app.exec_())
