import sqlite3

conn = sqlite3.connect("college.db")
c=conn.cursor()
c.execute(""" create table student25(
id integer,
name text,
age integer,
course_id integer)""")

c.execute(""" create table course10(
course_id integer,
course_name text,
foreign key (course_id) references student25(course_id))""")