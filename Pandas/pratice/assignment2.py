import pandas as pd
students={
    "Roll No:":[101,102,103,104],
    "Name:":["Lakshmi","Ravi","Sita","Kumar"],
    "Marks:":[85,90,78,92]
} 
df=pd.DataFrame(students)
print(df)
print(df["Marks:"])
print(df["Name:"])
print(df[["Roll No:","Marks:"]])
print(df.count())
print(df.shape[1])
print(df.shape[0])
df["Age:"]=[20,21,22,23]
df.drop("Age:",axis=1, inplace=True)
print(df)
