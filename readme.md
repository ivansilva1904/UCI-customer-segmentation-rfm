# RFM Segmentation Project

This is a personal project based in a public dataset from The UCI Machine Learning Repository. My purpose with this project is to learn the basics of a Recency, Frequency and Monetary (RFM) analysis regarding the programming of the data pipeline, which you can run with ```py scripts/main.py```, and its end result showed in a Power BI (PBI) dashboard.

## ETL
The first step was to download the raw dataset from this [repository](https://archive.ics.uci.edu/dataset/352/online+retail). Then, I start with the process of cleaning the data, for which, I must confess, didn't approach with the most scientific methodology. In excel, I transform the range of data into a proper table, after that I checked each column through the autofilter menu looking for null or inconsistent values. Those were:
* CustomerID: null values
* Description: null values
* Quantity: negative values
* UnitPrice: null values
* InvoiceNo: alphanumeric values (which had a 'C' meaning "Cancelled")
#### Once I knew all the columns with problems, I counted and filter them out of the dataset using the Pandas library and saved the new file in the data directoy.

## Creating the RFM columns
This was very simple, I used the "groupby()" method from pandas to group all the purchases from the same CustomerID and then calculate the three values of the analysis. This was also saved in a new file in the data directoty.

## Heuristic vs. KMeans
At this point I only knew about the rule-based method to rank customers, but while researching about this I found out about the KMeans approach to group datasets based in their behavior using the Scikit-learn library in python. I liked the idea of trying that library and, because this is a project to gain experience, I decided to apply the KMeans algorithm to the main page of the dashboard and dedicate a different page to compare how both methods rank the customers. Having said that, I ran into a lot of problems which I will explain in the "KMeans methodology problems" section.
Starting with the rule-based method, I split the dataset obtained in the previous stage into quintiles with pandas and assigned a score to each RFM category from 1 to 5 based in the quintil they fell on. I also wrote the score concatenated into the same column and saved that as an independent file in data.
For the KMeans method, I first applied a logarithmic transformation to the data to ensure the values don't present a big asymmetry between one another. Then I standarized the values with Scikit-learn and trained the KMeans model with a fixated number of cluster, for which I chose 4. All of this was saved in another file in data.

## Group segmentation
Once I had all the customers ranked, I used the groupby method again to check the average values for each RFM column in the 4 clusters previously created. Based in my analysis of the next table:
| Cluster | Recency mean | Frequency mean | Monetary mean |
| :--- | :--- | :--- | :--- |
| 0 | 18.124 | 2.148 | 551.819 |
| 1 | 12.131 | 13.713 | 8074.266 |
| 2 | 71.084 | 4.083 | 1802.829 |
| 3 | 182.496 | 1.318 | 343.450 |
I come out with 4 groups for the dataset:
* Cluster 1: Loyal client
* Cluster 0: New client
* Cluster 2: At risk client
* Cluster 3: Inactive client
