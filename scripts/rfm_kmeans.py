
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
df = pd.read_excel(os.path.join(directory, '..', 'data', '3-Online Retail_RFM.xlsx'))

#Initializing scaler
scaler = StandardScaler()

#Selecting columns from the table and standarizing its values without logarithmic transformation
rfm_raw_values = df[['Recency', 'Frequency', 'Monetary']]
rfm_std_nolog = scaler.fit_transform(rfm_raw_values)

#Same process as before but with logarithmic transformation
rfm_log_values = np.log1p(rfm_raw_values)
rfm_std_log = scaler.fit_transform(rfm_log_values)

#Calculating the inertia for each number of groups (1-10)
inertia_nolog = []
inertia_log = []
groups = range(1,11)

#Simulating groups with no log
for i in groups:
    kmeans_model = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans_model.fit(rfm_std_nolog)
    inertia_nolog.append(kmeans_model.inertia_)

#Simulating groups with log
for i in groups:
    kmeans_model = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans_model.fit(rfm_std_log)
    inertia_log.append(kmeans_model.inertia_)

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
elbow_value_nolog = KneeLocator(groups, inertia_nolog, curve='convex', direction='decreasing').elbow
print(f"Elbow without LOGT: {elbow_value_nolog}")

elbow_value_log = KneeLocator(groups, inertia_log, curve='convex', direction='decreasing').elbow
print(f"Elbow with LOGT: {elbow_value_log}")

#Training the definitive model and assigning the number of cluster to each client
rfm_model_nolog = KMeans(n_clusters=elbow_value_nolog, random_state=42, n_init=10)
df['No log cluster'] = rfm_model_nolog.fit_predict(rfm_std_nolog)

rfm_model_log = KMeans(n_clusters=elbow_value_log, random_state=42, n_init=10)
df['Log cluster'] = rfm_model_log.fit_predict(rfm_std_log)

df.to_excel(os.path.join(directory, '..', 'data', '5-Online Retail_RFM KMeans.xlsx'), index=False)
print(f"End result:\n{df}")



