from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql

def getNames():
    conn = pymysql.connect(
        user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8'
    )
    
    curs = conn.cursor()
    
    sql = "SELECT s_code, s_name, s_price, crawl_date FROM stock ORDER BY s_code, crawl_date;"
    curs.execute(sql)
    result = curs.fetchall()
    
    arr = []
    for row in result:
        print(row[0])
    return arr
   
getNames()
def getPrices(str):
    conn = pymysql.connect(
        user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8'
    )
    
    curs = conn.cursor()
    
    sql = "SELECT s_code, s_name, s_price, crawl_date FROM stock WHERE s_code= %s ORDER BY crawl_date;"
    curs.execute(sql,str)
    
    result = curs.fetchall()
    
    arr = []
    for idx, row in enumerate(result):
        if idx == 0 :
            firstprice = row[2]
            if row[2]==0:
                arr.append(0)
            else:
                arr.append(100)
        elif row[2]== 0:
            arr.append(0)
        else:
            arr.append(round(firstprice/row[2]*100,2))
    return arr

np_z = []
fig = plt.figure()
ax = plt.axes(projection='3d')
# z = np.linspace(0, 1, 100)

y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# for idx, item in enumerate(arr):
# for idx, item in enumerate(getNames()):
#     if(item!=None):
#         print(getPrices(item))
    
    # z = np.array(getPrices(item))
    # x = np.array([idx, idx, idx, idx, idx, idx, idx, idx, idx, idx])
    # ax.plot3D(x,y,z,'blue')
    # ax.plot3D(x,y,np.array(getPrices(item)),'blue')
# ax.set_title('3D line plot')
# plt.show()







        

