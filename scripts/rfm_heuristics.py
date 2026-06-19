
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

#Categorizing with a rule-based method by quintiles
asc_labels = [1,2,3,4,5]
desc_labels = [5,4,3,2,1]

rfm_df['R-score'] = pd.qcut(rfm_df['Recency'], q=5, labels=desc_labels)
rfm_df['F-score'] = pd.qcut(rfm_df['Frequency'].rank(method='first'), q=5, labels=asc_labels)
rfm_df['M-score'] = pd.qcut(rfm_df['Monetary'], q=5, labels=asc_labels)

rfm_df['Score'] = rfm_df['R-score'].astype(str) + rfm_df['F-score'].astype(str) + rfm_df['M-score'].astype(str)

rfm_df.to_excel(os.path.join(directory, '..', 'data', '3-Online Retail_RFM heuristics.xlsx'), index=False)
print(rfm_df)
