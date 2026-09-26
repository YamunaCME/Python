import pandas as pd
students={
    "Roll No:":[101,102,103,104],
    "Name:":["Lakshmi","Ravi","Sita","Kumar"],
    "Marks:":[85,90,78,92]
} 
df=pd.DataFrame(students)
print(df)
print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe())