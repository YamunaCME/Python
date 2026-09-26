import pandas as pd
df = pd.read_csv("weather_data.csv")
cites_above_35 = df[df["Temperature"] > 35]["City"].tolist()
print(cites_above_35)