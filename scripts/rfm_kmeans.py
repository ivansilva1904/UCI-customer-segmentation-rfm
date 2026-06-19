
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from kneed import KneeLocator

"""
It's important to clarify that this code will generate 
two groups for each customer for comparison purposes:
*One group receives a logarithmic transformation "Log cluster"
*The other doesn't "No log cluster"
*The correct or more "precise" way to segment the groups
is with the logarithmic transformation, hence why it's used 
in the "Business RFM" dashboard
"""

directory = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(os.path.join(directory, '..', 'data', '3-Online Retail_RFM heuristics.xlsx'))

#Selecting columns from the table and standarizing its values
rfm_raw_values = df[['Recency', 'Frequency', 'Monetary']]
scaler = StandardScaler()
rfm_std_values = scaler.fit_transform(rfm_raw_values)

#Logarithmic transformation on the values
rfm_log_values = np.log1p(rfm_raw_values)
rfm_log_std = scaler.fit_transform(rfm_log_values)

#Calculating the inertia for each number of groups (1-10)
inertia = []
groups = range(1,11)

for i in groups:
    kmeans_model = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans_model.fit(rfm_log_std)
    inertia.append(kmeans_model.inertia_)

"""Just something to check the inertia values and graph
print("Inertia:", *inertia, sep="\n ")

plt.figure(figsize=(10, 6))
plt.plot(groups, inertia, marker='o', linestyle='--', color='b')
plt.title('Elbow method', fontsize=16)
plt.xlabel('Number of groups', fontsize=12)
plt.ylabel('Inertia', fontsize=12)
plt.xticks(groups)
plt.show()
"""

#Obtaining the optimal number of groups
elbow_value = KneeLocator(groups, inertia, curve='convex', direction='decreasing').elbow

print(f"Elbow log: {elbow_value}")

inertia2 = []
for i in groups:
    kmeans_model = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans_model.fit(rfm_std_values)
    inertia2.append(kmeans_model.inertia_)

elbow_value = KneeLocator(groups, inertia2, curve='convex', direction='decreasing').elbow
print(f"Elbow no log: {elbow_value}")
"""
#Training the definitive model and assigning the number of cluster to each client
rfm_model = KMeans(n_clusters=elbow_value, random_state=42, n_init=10)
df['No log cluster'] = rfm_model.fit_predict(rfm_std_values)

rfm_log_model = KMeans(n_clusters=elbow_value, random_state=42, n_init=10)
df['Log cluster'] = rfm_log_model.fit_predict(rfm_log_std)

df.to_excel(os.path.join(directory, '..', 'data', '4-Online Retail_RFM heuristics and KMeans.xlsx'), index=False)
print(df)
"""


