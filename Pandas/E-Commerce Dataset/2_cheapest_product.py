import pandas as pd
df = pd.read_csv("E-commercedataset.csv")
cheapest_product = df.loc[df['price'].idxmin()]
print(cheapest_product)