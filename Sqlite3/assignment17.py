import sqlite3

conn = sqlite3.connect("college.db")
c=conn.cursor()
c.execute(""" create table student17(
id integer,
name text,
age integer,
course text)""")

c.execute(""" insert into student17 values(1,"hema",17,"python"),(2,"renu",18,"java"),(3,"harika",19,"python"),(4,"rajee",16,"java"),(5,"deepthi",19,"python")""")
c.execute("select course,count(*) from student17 group by course ")
print(c.fetchall())