
import os
import pandas as pd

directory = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(os.path.join(directory, '..', 'data', '2-Online Retail_filtered.xlsx'))

#Recency
last_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

recency_df = df.groupby('CustomerID')['InvoiceDate'].max().reset_index()
recency_df['Recency'] = (last_date - recency_df['InvoiceDate']).dt.days
recency_df = recency_df.drop(columns='InvoiceDate')

#Frequency
frequency_df = df.groupby('CustomerID')['InvoiceNo'].nunique().reset_index()
frequency_df = frequency_df.rename(columns={'InvoiceNo': 'Frequency'})

#Monetary
df['Total'] = df['Quantity'] * df['UnitPrice']

monetary_df = df.groupby('CustomerID')['Total'].sum().reset_index()
monetary_df = monetary_df.rename(columns={'Total': 'Monetary'})

#Merging
rfm_df = pd.merge(recency_df, frequency_df, on='CustomerID')
rfm_df = pd.merge(rfm_df, monetary_df, on='CustomerID')
