import sqlite3

conn = sqlite3.connect("college.db")
c=conn.cursor()
#c.execute(""" create table student22(
#id integer,
#name text,
#age integer)""")

while True:
    print("****** menu *******")
    print("1.Insert")
    print("2.Update")
    print("3.Delete")
    print("4.Display")

    choice=int(input("enter your choice:"))
    match choice:
     case 1:
       n1=int(input("enter id"))
       n2=input("enter name:")
       n3=int(input("enter your age:"))
       d=[(n1,n2,n3)]
       c.executemany(""" insert into student22 values(?,?,?)""",d)
          
       conn.commit()
       print("insertion completed sucessfully!")  
       break;  
     case 2:
       n1=int(input("enter id"))
       n2=input("enter new name:")
       n3=int(input("enter your age:"))
       c.execute("update student22 set name=?,age=? where id=?",(n2,n3,n1))
      
       conn.commit()
       print("updation completed sucessfully!")  
       break;  
     case 3:
       n1=int(input("enter id for deletion"))
   
       c.execute("delete from student22 where id=?",(n1,))
      
       conn.commit()
       print("deletion completed sucessfully!")  
       break;  
     case 4:
       c.execute("select * from student22")
       print(c.fetchall())   
     case _:
      print("invalid input")


      


