#coding:utf-8
#import MySQLdb.cursors
import pymysql
import json
class OperationMysql():
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='hd123456',
            db='emp',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
            )
        self.cur = self.conn.cursor()
    #查询一条数据
    def search_one(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
      #  result = json.dumps(result)
        print(type(result))
        keys=[key for key in result.keys()   ]
        print(keys)
        return result
    def insert_one(self,sql,data):
       # data = (6, 18, 2)
        self.cur.execute(sql, data)
        self.conn.commit()
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one("select * from student where sname='tome'")
    op_mysql.insert_one( "INSERT INTO student (sid, sname, classid) VALUES (%s, %s, %s)", (11, 18, 2) )
    print(res)