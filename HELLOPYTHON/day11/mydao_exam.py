import pymysql

class DaoExam :
    
    def __init__(self):
        self.conn = pymysql.connect(
        user='root', 
        passwd='java', 
        host='127.0.0.1', 
        db='python', 
        charset='utf8'
        )
        
        
    def myselect(self):
        ret = []
        curs = self.conn.cursor() 

        sql = "SELECT e_id ,kor ,eng ,math FROM exam;"
        curs.execute(sql)

        result = curs.fetchall() # 모든행 

        for row in result:
            ret.append({"e_id":row[0],"kor":row[1],"eng":row[2],"math":row[3]})
            
        return ret
            
            
    def myinsert(self, e_id ,kor ,eng ,math):
        param = [e_id ,kor ,eng ,math]
        curs = self.conn.cursor()
        sql = "INSERT INTO exam(e_id ,kor ,eng ,math) VALUES(%s,%s,%s,%s);"
        cnt = curs.execute(sql,param)

        self.conn.commit()
        
        return cnt
    
    def myupdate(self, e_id ,kor ,eng ,math):
        curs = self.conn.cursor()
        sql = f"""
                UPDATE exam
                SET
                kor='{kor}',
                eng='{eng}',
                math='{math}'
                WHERE
                e_id='{e_id}' 
            """
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    
    def mydelete(self, e_id):
        curs = self.conn.cursor() 
        param = e_id
        sql = "DELETE FROM exam WHERE e_id = %s;"
        
        cnt = curs.execute(sql,param)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.conn.close()
        
if __name__== '__main__':
    
    de = DaoExam()
    
    # cnt = de.myinsert('a003','50','43','99')
    # list = de.myselect()
    # cnt = de.myupdate('a002','42','52','12')
    cnt = de.mydelete('a002')
    
    # print(list)
    print(cnt)
    