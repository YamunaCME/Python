import pandas as pd
df = pd.read_csv("E-commercedataset.csv")
total_inventory_value = (df['price']*df['Quantity']).sum()
print(total_inventory_value)