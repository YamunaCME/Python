import pandas as pd
students={
    "Roll No:":[101,102,103,104],
    "Name:":["Lakshmi","Ravi","Sita","Kumar"],
    "Marks:":[85,90,38,92]
} 
df=pd.DataFrame(students)
df["Result:"] = ["Pass" if marks >= 40 else "Fail" for marks in df["Marks:"]]
print(df)
df["Bonus"]=df["Marks:"]+5
print(df)
df["Grade"]=["A" if marks>=90 else "B" if marks>80 and marks<90 else "C" if marks>70 and marks<80 else "D" if marks<70 else "Fail" for marks in df["Marks:"]]
print(df)
