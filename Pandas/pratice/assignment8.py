import pandas as pd
import numpy as np

students = {
    "name": ["Lakshmi", "Ravi", "Sita", "Kumar"],
    "marks": [85, np.nan, 78, np.nan]
}

df = pd.DataFrame(students)

print(df)
print("\nMissing Values:")
print(df.isnull())
print("\nCount of Missing Values:")
print(df.isnull().sum())
print(df.fillna(0))
print("Replacing NAN values with average of marks")
df["marks"] = df["marks"].fillna(df["marks"].mean())
print(df)
print(df.dropna())
print(df)
