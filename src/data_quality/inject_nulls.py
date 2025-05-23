import pandas as pd

df = pd.read_csv('data/raw/olist/olist_customers_dataset.csv')
print(df.head())

df.to_csv('data/raw/olist/olist_customers_dataset.csv', index=False)