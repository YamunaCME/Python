import sqlite3

conn = sqlite3.connect("college.db")
c=conn.cursor()
#c.execute(""" create table student4(
#id integer,
#name text,
#age integer,
#marks integer)""")
c.execute(""" insert into student4 values(1,"hema",17,99),(2,"renu",18,67),(3,"harika",19,100),(4,"rajee",16,56),(5,"deepthi",19,80)""")
c.execute("select name from student4 ")
print(c.fetchall())