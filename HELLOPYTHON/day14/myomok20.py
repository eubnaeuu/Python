
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic, QtGui
from PyQt5.Qt import QSize, QMessageBox
from conda.common._logic import TRUE

form_class = uic.loadUiType("myomok20.ui")[0]
class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100,100,900,800)
        self.flag_wb = True
        self.comi = 0
        self.comj = 0
        self.flag_ing = True
        self.arr2d = [
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                                              
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                                              
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                                              
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
            ]
        self.length = len(self.arr2d[0])
        self.pbtn2d = []
        
        for i in range(self.length):
            pb_line = []
            for j in range(self.length):
                tmp = QPushButton(self)
                tmp.setIconSize(QSize(40,40))
                tmp.setGeometry(j*40,i*40,40,40)  # x,y,width,height
                tmp.setIcon(QtGui.QIcon('0.png'))
                tmp.setToolTip("{},{}".format(i,j))
                tmp.clicked.connect(self.btnClick)
                pb_line.append(tmp)
            self.pbtn2d.append(pb_line)
        
        self.resetbtn = QPushButton(self)
        self.resetbtn.setGeometry(800, 70, 80, 40)
        self.resetbtn.setText('reset')
        self.resetbtn.clicked.connect(self.myreset)
        self.myrender()
        
    def myrender(self):
        for i in range(self.length):
            for j in range(self.length):
                if self.arr2d[i][j]==0:
                    self.pbtn2d[i][j].setIcon(QtGui.QIcon('0.png'))
                elif self.arr2d[i][j]==1:
                    self.pbtn2d[i][j].setIcon(QtGui.QIcon('1.png'))
                else:
                    self.pbtn2d[i][j].setIcon(QtGui.QIcon('2.png'))
                    
                    


    def getUp(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except :
            return cnt
        
    def getDw(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except : 
            return cnt   
         
    def getLe(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except :
            return cnt
    def getRi(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except : 
            return cnt        
    def getUR(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except :
            return cnt
        
    def getDL(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except : 
            return cnt
        
    def getUL(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except :
            return cnt
        
    def getDR(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except : 
            return cnt
        
        
    def check(self,i,j,stone) :
        up = self.getUp(i,j,stone)
        down = self.getDw(i,j,stone)
        le = self.getRi(i,j,stone)
        ri = self.getLe(i,j,stone)
        dl = self.getDL(i,j,stone)
        ur = self.getUR(i,j,stone)
        ul = self.getUL(i,j,stone)
        dr = self.getDR(i,j,stone)
        
        d1 = up+down+1
        d2 = le+ri+1
        d3 = dl+ur+1
        d4 = dr+ul+1
        
        print("d1:",d1,"d2:",d2,"d3:",d3,"d4:",d4)
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            print("요기 들어옴")
            self.flag_ing=False
            
            if self.flag_wb:
                QMessageBox.about(self, '알림창', "흑돌이 승리하였습니다")
            else:
                QMessageBox.about(self, '알림창', "백돌이 승리하였습니다")
            
            return
        
        self.flag_wb = not self.flag_wb                
                    
    
    def Putcom(self,i,j):
        self.arr2d[self.comi][self.comj] = 2
        stone = 2
        if self.comj > self.length-1:
            self.comi += 1
            self.comj = 0
        self.flag_wb = not self.flag_wb
         
    
    def btnClick(self):
        if not self.flag_ing :
            return 
        self.resetbtn.setDisabled(True)
        
        gps = []
        gps = self.sender().toolTip().split(",")
        i = int(gps[0])
        j = int(gps[1])
        
        if self.arr2d[i][j] != 0:
            return
        stone = 0
        if self.flag_wb:
            self.arr2d[i][j] = 1
            stone = 1
            self.myrender()
            self.check(i,j,stone)
            
            self.comj += 1
            self.Putcom(self.comi,self.comj)
            self.myrender()
            self.check(self.comi,self.comj,stone)
            
        
    def myreset(self):
        for i in range(self.length):
            for j in range(self.length):
                self.arr2d[i][j] = 0
        self.flag_wb = True
        self.flag_ing = True
        self.cnt = 0
        self.myrender()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   myWindow = MyWindow()
   myWindow.show()
   sys.exit(app.exec_())
