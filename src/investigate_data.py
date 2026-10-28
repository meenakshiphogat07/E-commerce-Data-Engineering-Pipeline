import pandas as pd

df = pd.read_excel('data/raw/Online Retail.xlsx')
print(
    df[df['Quantity'] < 0][
        ['InvoiceNo', 'StockCode', 'Quantity', 'UnitPrice', 'Country']
    ].head(10)
)
print(df[df['InvoiceNo'].str.startswith('C', na=False)].head(10))
print(df[df['CustomerID'].isnull()].head(10))
df['Revenue'] = df['Quantity'] * df['UnitPrice']
print(df[['InvoiceNo', 'Quantity', 'UnitPrice', 'Revenue']].head())