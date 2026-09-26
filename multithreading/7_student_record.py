from threading import Thread
import time
def display1(phy,che,maths):
 print("total=",phy+che+maths)

def display2(phy,che,maths):
 print("average=",phy+che+maths/3) 
 
phy=int(input("enter physics marks:"))
che=int(input("enter chemistry marks:"))
maths=int(input("enter maths marks:"))

t1=Thread(target=display1,args=("phy","che","maths"))
t2=Thread(target=display2,args=("phy","che","maths"))
t1.start
t2.start() 
