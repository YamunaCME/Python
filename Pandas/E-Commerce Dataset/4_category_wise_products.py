import pandas as pd
df = pd.read_csv("E-commercedataset.csv")
category_wise_products = df.groupby('Category')['Product'].apply(list)
print(category_wise_products)