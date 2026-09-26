import sqlite3

conn = sqlite3.connect("college.db")
c=conn.cursor()
c.execute(""" create table student20(
id integer,
name text,
course text,
marks integer
)""")

c.execute(""" insert into student20 values(1,"hema","python",99),(2,"renu","java",56),(3,"harika","python",78),(4,"rajee","java",100),(5,"deepthi","python",87)""")
c.execute("select * from student20 where marks between 60 and 90 ")
print(c.fetchall())