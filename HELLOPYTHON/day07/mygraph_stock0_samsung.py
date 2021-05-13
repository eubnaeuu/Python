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
    
    arr = []
    for row in result:
        arr.append(row)
    return arr   
    
def getPrices(s_name):
    conn = pymysql.connect(
        user='root', passwd='java', host='127.0.0.1', db='python', charset='utf8'
    )
    
    curs = conn.cursor()
    
# 방법1
    sql = "SELECT s_code, s_name, s_price, crawl_date FROM stock WHERE s_name= %s ORDER BY crawl_date;"
    curs.execute(sql,s_name)
# 방법2
    # sql2 = "SELECT s_code, s_name, s_price, crawl_date FROM stock WHERE s_code= '{}' ORDER BY crawl_date;".format(s_name)
    # curs.execute(sql)
    
    result = curs.fetchall()
    
    arr = []
    for row in result:
        arr.append(row[2])
    return arr   



fig = plt.figure()
ax = plt.axes(projection='3d')
# z = np.linspace(0, 1, 100)

s_price1 = []
s_price2 = []

for row in getPrices('삼성전자'):
    s_price1.append(row)
for row in getPrices('삼성전자우'):
    s_price2.append(row)

np_z1 = np.array(s_price1)
np_z2 = np.array(s_price2)
y = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# x = np.sin(5 * z)
# y = np.cos(1 * z)
ax.plot3D(0, 0, 1000000, 'maroon')
ax.plot3D(0, 0, 0, 'maroon')
ax.plot3D(x, y, np_z1, 'maroon')
ax.plot3D(x+1, y, np_z2, 'blue')
ax.set_title('3D line plot')
plt.show()







        

