import sqlite3

conn = sqlite3.connect("college.db")
c=conn.cursor()
#c.execute(""" create table student19(
#id integer,
#name text,
#course text,
#marks integer
#)""")

c.execute(""" insert into student19 values(1,"Anitha","python",99),(2,"Anjali","java",56),(3,"harika","python",78),(4,"rajee","java",100),(5,"deepthi","python",87)""")
c.execute("select *  from student19 where name like 'A%' ")
print(c.fetchall())