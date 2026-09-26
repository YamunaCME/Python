import pandas as pd
students={
    "Roll No:":[101,102,103,104],
    "Name:":["Lakshmi","Ravi","Sita","Kumar"],
    "Marks:":[85,90,78,92]
} 
df=pd.DataFrame(students)
print(df)
print(df.loc[0])
print(df.loc[3])
print(df.iloc[2])
print(df.iloc[1:3])

print(df.loc[0, ["Name:", "Marks:"]])