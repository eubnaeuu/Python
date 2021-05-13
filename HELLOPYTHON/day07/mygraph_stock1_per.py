from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql

def getNames():
    conn = pymysql.connect(
        user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8'
    )
    
    curs = conn.cursor()
    
    sql = "SELECT distinct s_name FROM stock ORDER BY 1"
    curs.execute(sql)
    result = curs.fetchall()
    
    pricearr = []
    for row in result:
       pricearr.append(row[0])
    return pricearr   

def getPrices(s_name):
    conn = pymysql.connect(
        user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8'
    )
    
    curs = conn.cursor()
    
    sql = "SELECT s_price FROM stock WHERE s_name= %s ORDER BY crawl_date;"
    curs.execute(sql,s_name)
    
    result = curs.fetchall()
    
    arr = []
    for idx, row in enumerate(result):
        if row[0]==0:
            continue
        elif idx == 0 :
            firstprice = row[0]
            arr.append(100)
        else:
            arr.append(round(firstprice/row[0]*100,2))
            
    return arr

fig = plt.figure()
ax = plt.axes(projection='3d')

y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

namelist = getNames()
for idx, item in enumerate(namelist):
    if len(getPrices(item)) != 0 :
        z = np.array(getPrices(item))
        x = np.array([idx, idx, idx, idx, idx, idx, idx, idx, idx, idx])
        if idx==0:
            idx=1
        ax.plot3D(x,y,z,'red')
    else:
        continue
ax.set_title('3D line plot')
plt.show()







        

