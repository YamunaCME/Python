import sqlite3

conn = sqlite3.connect("college.db")
c=conn.cursor()
c.execute(""" create table student(
id integer,
name text,
age integer,
marks integer)""")
