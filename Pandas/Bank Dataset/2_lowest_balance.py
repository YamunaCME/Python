import pandas as pd
df=pd.read_csv("Bankdataset.csv")
df["Balance"] = df["Balance"].str.replace(",", "").astype(float)
print(df[df["Balance"] == df["Balance"].min()])