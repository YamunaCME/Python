import pandas as pd
df = pd.read_csv("weather_data.csv")
hottest_city = df.loc[df["Temperature"].idxmax()]["City"]
print(hottest_city)