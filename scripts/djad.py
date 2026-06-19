import os
import pandas as pd

directory = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(os.path.join(directory, '..', 'data', '4-Online Retail_RFM KMeans.xlsx'))

rfm_df = pd.DataFrame()
rfm_df = df.groupby('Cluster')[['Recency', 'Frequency', 'Monetary']].mean().reset_index()

print(rfm_df)
