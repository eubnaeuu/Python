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

    sql = "SELECT * FROM stock_sync_0121 ORDER BY in_time limit 3;"
    curs.execute(sql)

    result = curs.fetchall()

    arr = []
    for idx, row in enumerate(result):
        arr.append(row)
    return np.array(arr)   

arrCode = getCodes()
arrPrice = getPrices()

# print(arrPrice[0][0])
# print(arrPrice[1][0])
# print(arrPrice[2][0])

arrz = []

for idx, item in enumerate(arrCode):
    tmp = []
    for i in range(3):
        tmp.append(arrPrice[i][idx])
    arrz.append(tmp)
    
print(arrz)
# arrz = []
# arr_name = getNames()
# for item in arr_name:
#     arrz.append(getPrices(item))
#
# arr_per_z = []
# tmp = []
# for i in range(len(arr_name)):
#     if arrz[i][0]==0:
#         continue
#     else:
#         tmp = (arrz[i]/arrz[i][0])*100
#     arr_per_z.append(tmp)
#
#
# fig = plt.figure()
# ax = plt.axes(projection='3d')
#
# y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# for idx, item in enumerate(arr_per_z):
#     ax.plot3D(x+idx,y,item)
#
# ax.set_title('3D line plot')
# plt.show()







        

