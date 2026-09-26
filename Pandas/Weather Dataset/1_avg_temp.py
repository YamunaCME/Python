import pandas as pd
df = pd.read_csv("weather_data.csv")
average_temp = df["Temperature"].mean()
print(average_temp)