
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
#import matplotlib.pyplot as plt
#from kneed import KneeLocator

directory = os.path.dirname(os.path.abspath(__file__))
df = pd.read_excel(os.path.join(directory, '..', 'data', '3-Online Retail_RFM.xlsx'))

#Initializing scaler
scaler = StandardScaler()

#Selecting columns from the table and applying a logarithmic transformation to the values
rfm_raw_values = df[['Recency', 'Frequency', 'Monetary']]
rfm_log_values = np.log1p(rfm_raw_values)

#Standarizing the values
rfm_log_std_values = scaler.fit_transform(rfm_log_values)

"""This is to simulate the optimal number of groups based in their inertia
#Calculating the inertia for each number of groups (1-10)
inertia = []
groups = range(1,11)

#Simulating groups
for i in groups:
    kmeans_model = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans_model.fit(rfm_std_values)
    inertia.append(kmeans_model.inertia_)

#Obtaining the optimal number of groups
elbow_value = KneeLocator(groups, inertia, curve='convex', direction='decreasing').elbow
print(f"Elbow: {elbow_value}")
"""

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

#Training the definitive model and assigning the number of cluster to each client
rfm_model_log = KMeans(n_clusters=4, random_state=42, n_init=10)
df['Cluster'] = rfm_model_log.fit_predict(rfm_log_std_values)

df.to_excel(os.path.join(directory, '..', 'data', '5-Online Retail_RFM KMeans.xlsx'), index=False)
print(f"End result:\n{df}")



