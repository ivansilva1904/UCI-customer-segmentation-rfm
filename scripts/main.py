import os
import subprocess
import sys

directory = os.path.dirname(os.path.abspath(__file__))

data_cleaning_path = os.path.join(directory, 'data_cleaning.py')
rfm_heuristics_path = os.path.join(directory, 'rfm_heuristics.py')
rfm_kmeans_path = os.path.join(directory, 'rfm_kmeans.py')
group_segmentation = os.path.join(directory, 'group_segmentation.py')

print(f"----------Starting data_cleaning.py----------\n")
subprocess.run([sys.executable, data_cleaning_path], check=True)

print(f"\n----------Starting rfm_heuristics.py----------\n")
subprocess.run([sys.executable, rfm_heuristics_path], check=True)

print(f"\n----------Starting rfm_kmeans.py----------\n")
subprocess.run([sys.executable, rfm_kmeans_path], check=True)

print(f"\n----------Starting group_segmentation.py----------\n")
subprocess.run([sys.executable, group_segmentation], check=True)

print(f"\n----------RFM pipeline executed successfully----------\n")