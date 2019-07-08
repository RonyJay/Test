# coding:utf-8
'''
预期结果里面输入SQL语句，拿到数据，对比实际结果
'''
import pymysql.cursors
import json

class OperationMysql:
    def __init__(self):
        # 连接database
        self.conn = pymysql.connect(
            host='localhost',
            user='user',
            password='password',
            database='xxx',
            charset='utf8',
            #以字典的形式返回操作结果
            cursorclass=pymysql.cursors.DictCursor)
        # 得到一个可以执行SQL语句的光标对象
        self.cur = self.conn.cursor()

    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result=json.dumps(result)
        return result


if __name__ == '__main__':
    op_mysql = OperationMysql()
    op_mysql.search_one("select * from items where item_id='666'")
