import sqlite3

conn = sqlite3.connect("college.db")
c=conn.cursor()
#c.execute(""" create table student7(
#id integer,
#name text,
#age integer,
#course text)""")
c.execute(""" insert into student7 values(1,"hema",17,"python"),(2,"renu",18,"python"),(3,"harika",19,"java"),(4,"rajee",16,"python"),(5,"deepthi",19,"java")""")
c.execute("select * from student7 where id='1' ")
print(c.fetchall())