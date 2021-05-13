
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic, QtGui
from PyQt5.Qt import QSize

form_class = uic.loadUiType("myomok01.ui")[0]
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.player = [1,2]
        self.arr2d = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,2,0,0,0,0],
            
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
            ]
        self.pbtn2d = []
        
        for i in range(10):
            pb_line = []
            for j in range(10):
                tmp = QPushButton(self)
                tmp.setIconSize(QSize(40,40))
                tmp.setGeometry(j*40,i*40,40,40)  # x,y,width,height
                tmp.setIcon(QtGui.QIcon('0.png'))
                tmp.setToolTip("{},{}".format(i,j))
                tmp.clicked.connect(self.btnClick)
                pb_line.append(tmp)
            self.pbtn2d.append(pb_line)
    
        self.myrender()
        
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j]==0:
                    self.pbtn2d[i][j].setIcon(QtGui.QIcon('0.png'))
                elif self.arr2d[i][j]==1:
                    self.pbtn2d[i][j].setIcon(QtGui.QIcon('1.png'))
                else:
                    self.pbtn2d[i][j].setIcon(QtGui.QIcon('2.png'))
            
    def btnClick(self):
        # print(self.sender()) # 해당 객체 (target, source, sender)
        gps = []
        gps = self.sender().toolTip().split(",")
        x = int(gps[0])
        y = int(gps[1])
        if self.arr2d[x][y] != 0:
            print("이미")
        else:
            self.arr2d[x][y] = 1
        self.myrender()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = MyWindow()
   myWindow.show()
   sys.exit(app.exec_())
