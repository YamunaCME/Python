import pandas as pd
df = pd.read_csv("Book1.csv")
print("top five players:")
df["Runs"] = df["Runs"].str.replace(",","").astype(int)
print(df.nlargest(5, "Runs"))