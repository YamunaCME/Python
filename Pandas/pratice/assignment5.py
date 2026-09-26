import pandas as pd
students={
    "Roll No:":[101,102,103,104],
    "Name:":["Aakshmi","Ravi","Sita","Kumar"],
    "Marks:":[85,90,78,92]
} 
df=pd.DataFrame(students)
print(df.sort_values(["Marks:"]))
print(df.sort_values(["Marks:"],ascending=False))
df["Age:"]=[20,21,22,23]
print(df.sort_values(["Age:"]))
print(df.sort_values(["Age:"],ascending=False))
print(df.sort_values(["Name:"]))