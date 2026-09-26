import pandas as pd
df=pd.read_csv("Bankdataset.csv")
df["City"] = df["City"].str.replace(",", "").astype(str)
print(df.groupby("City")["Customer_ID"].count())