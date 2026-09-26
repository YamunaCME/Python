import pandas as pd
df = pd.read_csv("Book1.csv")
print("Team-wise Average Runs:")
df["Runs"] = df["Runs"].str.replace(",","").astype(int)
print(df.groupby("Team")["Runs"].mean())