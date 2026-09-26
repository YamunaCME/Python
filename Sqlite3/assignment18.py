import sqlite3

conn = sqlite3.connect("college.db")
c=conn.cursor()
c.execute(""" create table stud18(
id integer,
name text,
course text,
marks integer
)""")

c.execute(""" insert into stud18 values(1,"hema","python",99),(2,"renu","java",56),(3,"harika","python",78),(4,"rajee","java",100),(5,"deepthi","python",87)""")
c.execute("select course,avg(marks) from stud18 group by course ")
print(c.fetchall())