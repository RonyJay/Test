# coding:utf-8
'''
预期结果里面输入SQL语句，拿到数据，对比实际结果
'''
import pymysql

# 连接database
conn = pymysql.connect(
    host='localhost',
    user='user',
    password='password',
    database='xxx',
    charset='utf8')
# 得到一个可以执行SQL语句的光标对象
cur = conn.cursor()
cur.execute("select * from items where item_id='666'")
print(cur.fetchone())