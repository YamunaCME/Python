import pandas as pd
df = pd.read_csv("Book1.csv")
print("highest runs:")
df["Runs"] = df["Runs"].str.replace(",","").astype(int)
print("Highest Strike Rate:")
print(df[df["Strike Rate"] == df["Strike Rate"].max()])
