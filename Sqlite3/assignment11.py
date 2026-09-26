import sqlite3

conn = sqlite3.connect("college.db")
c=conn.cursor()
#c.execute(""" create table student10(
#id integer,
#name text,
#age integer,
#marks integer)""")
data=[(1,"hema",17,99),(2,"renu",18,67),(3,"harika",19,100),(4,"rajee",16,56)]

c.executemany(""" insert into student10 values(?,?,?,?)""",data)
c.execute("select * from student10")
print(c.fetchall())