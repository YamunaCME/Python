import sqlite3

conn = sqlite3.connect("college.db")
c=conn.cursor()
c.execute(""" create table student21(
id integer,
name text,
age integer,
marks integer)""")
data=[(1,"hema",17,99),(2,"renu",18,67),(3,"harika",19,100),(4,"rajee",16,56)]

c.executemany(""" insert into student21 values(?,?,?,?)""",data)

try:
    id=int(input("enter id:"))
    c.execute("select * from student21 where id=?",(id))
except ValueError as e:
    print("Invalid input")
finally:
    print("end program")

