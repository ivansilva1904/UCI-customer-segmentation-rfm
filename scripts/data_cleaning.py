
import os
import pandas as pd

directory = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(os.path.join(directory, '..', 'data', '1-Online Retail.xlsx'))

#Verifying how many cells are invalid
print(f"----------Table analysis before filtering process----------")
customerid_empty = df['CustomerID'].isna().sum()
description_empty = df['Description'].isna().sum()
quantity_negative = (df['Quantity'] < 0).sum()
unitprice_negative = (df['UnitPrice'] <= 0).sum()

invoiceno_text = df['InvoiceNo'].astype(str)
invoiceno_alphanumeric = (~invoiceno_text.str.isdigit()).sum()

print(f"CustomerID: {customerid_empty}")
print(f"Description: {description_empty}")
print(f"Quantity: {quantity_negative}")
print(f"UnitPrice: {unitprice_negative}")
print(f"InvoiceNo: {invoiceno_alphanumeric}")

#Filtering out rows with invalid values
df_filtered = df[
    (df['InvoiceNo'].astype(str).str.isdigit() == True) &
    (df['Description'].isna() == False) &
    (df['Quantity'] > 0) &
    (df['UnitPrice'] > 0) &
    (df['CustomerID'].isna() == False)
]

#Verifying how many cells are invalid after filtering
print(f"----------Table analysis after filtering process----------")
customerid_empty = df_filtered['CustomerID'].isna().sum()
description_empty = df_filtered['Description'].isna().sum()
quantity_negative = (df_filtered['Quantity'] < 0).sum()
unitprice_negative = (df_filtered['UnitPrice'] <= 0).sum()

invoiceno_text = df_filtered['InvoiceNo'].astype(str)
invoiceno_alphanumeric = (~invoiceno_text.str.isdigit()).sum()

print(f"CustomerID: {customerid_empty}")
print(f"Description: {description_empty}")
print(f"Quantity: {quantity_negative}")
print(f"UnitPrice: {unitprice_negative}")
print(f"InvoiceNo: {invoiceno_alphanumeric}")

#Saving cleaned file
df_filtered.to_excel(os.path.join(directory, '..', 'data', '2-Online Retail_filtered.xlsx'), index=False)

