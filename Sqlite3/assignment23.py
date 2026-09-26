import sqlite3

conn = sqlite3.connect("college.db")
c=conn.cursor()
c.execute(""" create table student23(
id integer,
name text,
age integer,
marks integer)""")

c.execute(""" create table course(
course_id integer,
course_name text)""")


c.execute(""" create table enrollments(
couse_id integer,
cousrse_name text,
joining_date date)""")

