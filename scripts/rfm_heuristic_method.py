
import os
import pandas as pd

directory = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(os.path.join(directory, '..', 'data', '3-Online Retail_RFM.xlsx'))

#Categorizing with a rule-based method by quintiles
asc_labels = [1,2,3,4,5]
desc_labels = [5,4,3,2,1]

df['R-score'] = pd.qcut(df['Recency'], q=5, labels=desc_labels)
df['F-score'] = pd.qcut(df['Frequency'].rank(method='first'), q=5, labels=asc_labels)
df['M-score'] = pd.qcut(df['Monetary'], q=5, labels=asc_labels)

df['Score'] = df['R-score'].astype(str) + df['F-score'].astype(str) + df['M-score'].astype(str)

df.to_excel(os.path.join(directory, '..', 'data', '4-Online Retail_RFM heuristics.xlsx'), index=False)
print(df)
