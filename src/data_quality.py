import pandas as pd

df = pd.read_excel('data/raw/Online Retail.xlsx')
print(df.isnull().sum())
print(df.duplicated().sum())
print(df[df['Quantity']<0].shape[0])
print(df[df['UnitPrice']==0].shape[0])
print(df['Country'].nunique())
