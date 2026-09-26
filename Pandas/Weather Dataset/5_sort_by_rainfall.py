import pandas as pd
df = pd.read_csv("weather_data.csv")
df_sorted = df.sort_values("Rainfall")
print(df_sorted)