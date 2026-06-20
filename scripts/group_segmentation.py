
import pandas as pd
import os

directory = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(os.path.join(directory, '..', 'data', '5-Online Retail_RFM KMeans.xlsx'))

#no log
nolog_df = pd.DataFrame()

nolog_df['Recency mean'] = df.groupby('No log cluster')['Recency'].mean()
nolog_df['Frequency mean'] = df.groupby('No log cluster')['Frequency'].mean()
nolog_df['Monetary mean'] = df.groupby('No log cluster')['Monetary'].mean()

nolog_df = nolog_df.reset_index()

#log
log_df = pd.DataFrame()

log_df['Recency mean'] = df.groupby('Log cluster')['Recency'].mean()
log_df['Frequency mean'] = df.groupby('Log cluster')['Frequency'].mean()
log_df['Monetary mean'] = df.groupby('Log cluster')['Monetary'].mean()

log_df = log_df.reset_index()

print(nolog_df)
print("\n")
print(log_df)

