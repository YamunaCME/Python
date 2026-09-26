import pandas as pd
df = pd.read_csv("E-commercedataset.csv")
most_expensive_product = df.loc[df['price'].idxmax()]
print(most_expensive_product)