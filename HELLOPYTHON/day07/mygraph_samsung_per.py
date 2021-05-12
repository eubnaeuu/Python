from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pymysql






def getNames():
    conn = pymysql.connect(
        user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8'
    )
    
    curs = conn.cursor()
    
    sql = "SELECT distinct s_code FROM stock ORDER BY 1"
    curs.execute(sql)
    result = curs.fetchall()
    
    arr = []
    for row in result:
        arr.append(str(row).replace(",","").replace("'", ""))
    return arr   
    
    
def getPrices(tutes):
    conn = pymysql.connect(
        user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8'
    )
    
    curs = conn.cursor()
    
# 방법1
    sql = "SELECT s_code, s_name, s_price, crawl_date FROM stock WHERE s_code= %s ORDER BY crawl_date;"
    curs.executemany(sql,tutes)
    
    result = curs.fetchall()
    
    arr = []
    for row in result:
        arr.append(row[2])
    return arr   

arr = getPrices(getNames())

fig = plt.figure()
ax = plt.axes(projection='3d')
# z = np.linspace(0, 1, 100)


def toPer(str):
    price = []
    for idx, row in enumerate(getPrices(str)):
        if idx == 0 :
            price.append(100)
            firstprice = row
        else: 
            price.append(firstprice/row*100)
    return price
    
    

y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# x = np.sin(5 * z)
# y = np.cos(1 * z)

# ax.plot3D(x, y, np_z1, 'maroon')
# ax.plot3D(x+1, y, np_z2, 'blue')
# ax.set_title('3D line plot')
# plt.show()







        

