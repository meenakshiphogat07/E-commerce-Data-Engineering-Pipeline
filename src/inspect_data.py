import pandas as pd

df = pd.read_excel('data/raw/Online Retail.xlsx')
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)