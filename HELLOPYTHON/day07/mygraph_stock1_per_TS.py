from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql

def getNames():
    conn = pymysql.connect(
        user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8'
    )
    
    curs = conn.cursor()
    
    sql = "SELECT distinct s_name FROM stock ORDER BY 1 limit 10"
    curs.execute(sql)
    result = curs.fetchall()
    
    arrName = []
    for row in result:
       arrName.append(row[0])
    return arrName   

def getPrices(s_name):
    conn = pymysql.connect(
        user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8'
    )
    
    curs = conn.cursor()
    
    sql = "SELECT s_price FROM stock WHERE s_name= %s ORDER BY crawl_date;"
    curs.execute(sql,s_name)
    
    result = curs.fetchall()
    
    arr = []
    for row in result:
        arr.append(row[0])
    return np.array(arr)   


arrz = []
arr_name = getNames()
for item in arr_name:
    arrz.append(getPrices(item))

arr_per_z = []
tmp = []
for i in range(len(arr_name)):
    if arrz[i][0]==0:
        continue
    else:
        tmp = (arrz[i]/arrz[i][0])*100
    arr_per_z.append(tmp)


fig = plt.figure()
ax = plt.axes(projection='3d')

y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
for idx, item in enumerate(arr_per_z):
    ax.plot3D(x+idx,y,item)

ax.set_title('3D line plot')
plt.show()







        

