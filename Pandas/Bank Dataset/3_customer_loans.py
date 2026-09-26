import pandas as pd
df=pd.read_csv("Bankdataset.csv")
df["Loan"] = df["Loan"].str.replace(",", "").astype(float)
print(df[df['Loan']>500000])