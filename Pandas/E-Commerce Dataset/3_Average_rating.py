import pandas as pd
df = pd.read_csv("E-commercedataset.csv")
average_rating = df['Rating'].mean()
print(average_rating)