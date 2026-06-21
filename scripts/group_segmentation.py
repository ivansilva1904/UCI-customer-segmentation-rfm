
import pandas as pd
import os

directory = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(os.path.join(directory, '..', 'data', '5-Online Retail_RFM KMeans.xlsx'))

rfm_df = pd.DataFrame()

rfm_df['Recency mean'] = df.groupby('Cluster')['Recency'].mean()
rfm_df['Frequency mean'] = df.groupby('Cluster')['Frequency'].mean()
rfm_df['Monetary mean'] = df.groupby('Cluster')['Monetary'].mean()

rfm_df = rfm_df.reset_index()

print(rfm_df)
print(f"The groups are:\nCluster 1: Loyal clients\nCluster 0: New clients\nCluster 2: At risk clients\nCluster 3: Inactive clients")

