# -*- coding = utf-8 -*-
# @Time: 2021/7/11 下午 10:11
# @Software: PyCharm

import sqlite3

#連接數據庫
conn = sqlite3.connect("test.db")   #打開或創建數據庫文件

print("成功打開數據庫")

conn.close()        #關閉數據庫連結

#2.創建數據表
# c = conn.cursor()  #獲取游標
#
# sql = """
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# """
#
# c.execute(sql)      #執行sql語句
# conn.commit()       #提交數據庫操作
# conn.close()        #關閉數據庫連結
#
# print("成功建表")

#3.插入數據

conn = sqlite3.connect("test.db")   #打開或創建數據庫文件

c = conn.cursor()  #獲取游標

sql1 = """
    insert into company (id,name,age,address,salary)
        values (1,'Fe',20,"Taoyuan",8000);
"""

sql2 = """
    insert into company (id,name,age,address,salary)
        values (2,'FE-01 TEST TYPE',1,"Internet",0);
"""

c.execute(sql1)      #執行sql1語句
c.execute(sql2)      #執行sql2語句
conn.commit()       #提交數據庫操作
conn.close()        #關閉數據庫連結

print("插入數據完畢")


#4.查詢數據

conn = sqlite3.connect("test.db")   #打開或創建數據庫文件

c = conn.cursor()   #獲取游標

sql = "select id,name,address,salary from company"

cursor = c.execute(sql)

for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3],"\n")

conn.close()        #關閉數據庫連結

print("查詢完畢")