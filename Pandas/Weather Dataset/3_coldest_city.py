import pandas as pd
df = pd.read_csv("weather_data.csv")
coldest_city = df.loc[df["Temperature"].idxmin()]["City"]
print(coldest_city)