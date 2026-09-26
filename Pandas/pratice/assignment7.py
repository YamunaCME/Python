import pandas as pd
students={
    "Roll No:":[101,102,103,104],
    "Name:":["Lakshmi","Ravi","Sita","Kumar"],
    "Marks:":[85,90,78,92]
} 
df=pd.DataFrame(students)
df.loc[1, "Marks:"] = 95
print(df)
df["Age:"]=[20,21,22,20]
df.loc[0,"Age:"] =25
print(df)

df["Marks:"] =df["Marks:"] +5
print(df)
df["Age:"] = df["Age:"].replace({20: 21})
print(df)
