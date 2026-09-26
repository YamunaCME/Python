import pandas as pd
students={
    "Roll No:":[101,102,103,104],
    "Name:":["lakshmi","Ravi","Sita","Kumar"],
    "Marks:":[85,90,78,92]
} 
df=pd.DataFrame(students)

print(df[df["Marks:"]>80])
print(df[df["Marks:"]<80])
df["Age:"]=[20,21,22,23]
print(df[df["Age:"]==20])
print(df[df["Age:"]>20])

print(df[(df["Marks:"]>80) & (df["Age:"]>20)])

print(df[(df["Marks:"]>0) | (df["Age:"]>20)])