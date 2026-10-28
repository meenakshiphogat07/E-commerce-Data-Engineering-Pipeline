import pandas as pd

df = pd.read_excel('data/raw/Online Retail.xlsx')

df_clean=df.drop_duplicates()
print(df.shape[0], df_clean.shape[0])
df_clean=df_clean.dropna(subset=['Description'])
print(df_clean.shape[0])
print(df_clean['CustomerID'].isnull().sum())
