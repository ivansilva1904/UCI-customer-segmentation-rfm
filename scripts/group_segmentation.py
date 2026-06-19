
import pandas as pd
import os

directory = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(os.path.join(directory, '..', 'data', '4-Online Retail_RFM KMeans.xlsx'))

group_df = pd.DataFrame()

group_df['Recency mean'] = df.groupby('Cluster log')['Recency'].mean()
group_df['Frequency mean'] = df.groupby('Cluster log')['Frequency'].mean()
group_df['Monetary mean'] = df.groupby('Cluster log')['Monetary'].mean()

group_df = group_df.reset_index()

print(group_df)
print(f"\nThe groups are:\nCluster 1: VIP clients\nCluster 0: New clients\nCluster 2: At risk clients\nCluster 3: Lost clients")

