from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql


# 마지막 행  못없ㅇ맴
def getCodes():
    conn = pymysql.connect(
        user='root', passwd='java', host='127.0.0.1', db='_stock_old', charset='utf8'
    )
    curs = conn.cursor()
    sql = "SELECT COLUMN_NAME from  INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'stock_sync_0121'"
    curs.execute(sql)
    result = curs.fetchall()
    
    arrCode = []
    for idx, row in enumerate(result):
        if idx == len(result)-1:
            continue
        else:
            arrCode.append(row[0])
    return arrCode   

def getPrices():
    conn = pymysql.connect(
        user='root', passwd='java', host='127.0.0.1', db='_stock_old', charset='utf8'
    )

    curs = conn.cursor()

    sql = "SELECT * FROM stock_sync_0121 ORDER BY in_time;"
    curs.execute(sql)
    result = curs.fetchall()

# idx = 행수만큼 8000
    arr = []
    for idx, item_o in enumerate(result):
        tmp = []
        for i, item_i in enumerate(item_o): # 필드크기만큼 900
            if i < (len(item_o)-1):
                tmp.append(int(item_i))
            else:
                break
        arr.append(tmp)
        
    return arr



arrCode = getCodes()
arrPriceTmp = np.array(getPrices())

cntCode = len(arrCode)
cntRow = len(arrPriceTmp)

print(" 종목 개수 : ",cntCode)
print("행 개수 : ",cntRow)

firstPrice = arrPriceTmp[0]

# 파산 종목 초기값 -1로 통일
for i, item in enumerate(firstPrice):
    if item == 0:
        firstPrice[i] = -1;
        
# toper 만들기
arrPrice = []
for idx, item in enumerate(arrPriceTmp):
    arrPrice.append((item/firstPrice)*100)
print(len(arrPrice))
print(len(arrPrice[0]))

arrz = []
for idx in range(cntCode):
    tmp = []
    for i in range(cntRow):
        tmp.append(arrPrice[i][idx])
    arrz.append(tmp)

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.zeros(3952)
y = np.arange(0, 3952)
print(x,len(x))
print(y,len(y))
for idx, item in enumerate(arrz):
    ax.plot3D(x+idx,y,np.array(item))
ax.set_title('3D line plot')
plt.show()







        

