# RFM Segmentation Project

This is a personal project based in a public dataset from The UCI Machine Learning Repository. My purpose with this project is to learn the basics of a Recency, Frequency and Monetary (RFM) analysis regarding the programming of the data pipeline, which you can run with ```py scripts/main.py``` from the root of the project, and its end result shown in a Power BI (PBI) dashboard.

## ETL
The first step was to download the raw dataset from [this repository](https://archive.ics.uci.edu/dataset/352/online+retail). Then I started with the process of cleaning the data, which, I must confess, didn't approach with the most scientific methodology. In excel, I transformed the range of data into a proper table, after that I checked each column through the autofilter menu looking for null or inconsistent values. Those were:
* CustomerID: null values
* Description: null values
* Quantity: negative values
* UnitPrice: null values
* InvoiceNo: alphanumeric values (which had a 'C' meaning "Cancelled")
Once I knew all the columns with problems, I counted and filtered them out of the dataset using the Pandas library and saved the new file in the data directoy.

## Creating the RFM columns
This was very simple, I used the "groupby()" method from pandas to group all the purchases from the same CustomerID and then calculate the three values of the analysis. This was also saved in a new file in the data directoty.

## Heuristic vs. KMeans
At this point I only knew about the rule-based method to rank customers, but while researching about this I found out about the KMeans approach to group datasets based in their behavior using the Scikit-learn library in python. I liked the idea of trying that library and, because this is a project to gain experience, I decided to apply the KMeans algorithm to the main page of the dashboard and dedicate a different page to compare how both methods rank the customers. Having said that, I ran into a lot of problems which I will explain in the "KMeans methodology problems" section if you are interested in that.  
Starting with the rule-based method, I split the dataset obtained in the previous stage into quintiles with pandas and assigned a score to each RFM category from 1 to 5 based on the quintile they fell on. I also wrote the score concatenated into the same table and saved that as an independent file in data.  
For the KMeans method, I first applied a logarithmic transformation to the data to ensure the values didn't present a big asymmetry between one another. Then I standarized the values with Scikit-learn and trained the KMeans model with a fixed number of cluster, for which I chose 4. All of this was saved in another file in data.

## Group segmentation
Once I had all the customers ranked, I used the groupby method again to check the average values for each RFM column in the 4 clusters previously created. Based on my analysis of the next table:
| Cluster | Recency mean | Frequency mean | Monetary mean |
| :--- | :--- | :--- | :--- |
| 0 | 18.124 | 2.148 | 551.819 |
| 1 | 12.131 | 13.713 | 8074.266 |
| 2 | 71.084 | 4.083 | 1802.829 |
| 3 | 182.496 | 1.318 | 343.450 |
I came out with 4 groups for the dataset:
* Cluster 1: Loyal client
* Cluster 0: New client
* Cluster 2: At risk client
* Cluster 3: Inactive client

## KMeans methodology problems
If you go back to my first commit, you'll see that the project was a bit all over the place because I implemented Git once I had already made a lot of progress. At first, like I said before, this project was supposed to apply the rule-based method only, but I started to employ the KMeans method without the logarithmic transformation. This resulted in clusters mainly grouped by their Monetary values before anything else, since there is such a huge gap between the range of those values and the Recency and Frequency ones.  
So then, I applied the logarithmic transformation to level those differences, but there was another problem. I was using the Kneed library to get the "optimal" number of clusters given the inertia obtained in the simulation of the KMeans model (which you can see as a comment in the code). For the method WITHOUT the logarithmic transformation it was 4 clusters, whereas for the method WITH the transformation it was 3. When these parameters were used, the clusters, again, didn't come out as well as intended in any case. This is where my simple project ended up being more of a clustering method comparison than a real RFM analysis.  
However, this taught me a valuable lesson about the difference between mathematical accuracy and business logic. The mathematical "elbow" suggested 3 clusters for the transformed data, but from a business perspective, 3 groups were not enough to correctly differentiate them. It merged highly distinct customer profiles, like new buyers and at-risk clients, into one giant cluster. To fix this, I made the decision to force the algorithm to use $k=4$ clusters on the log-transformed and standardized data. This approach sacrificed pure mathematical inertia to gain business interpretability, finally allowing the model to successfully categorize clients into clear, viable groups: Loyal, New, At Risk, and Inactive.  
Lastly, I'd like to mention the obvious, which is the great influence the use of AI had in this project. This entire learning process was supported by the information I got from an LLM whenever I got stuck at many points of its development.