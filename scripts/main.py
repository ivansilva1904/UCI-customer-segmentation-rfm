import os
import subprocess
import sys

directory = os.path.dirname(os.path.abspath(__file__))

data_cleaning_path = os.path.join(directory, 'data_cleaning.py')
rfm_table_path = os.path.join(directory, 'rfm_table.py')
rfm_heuristic_path = os.path.join(directory, 'rfm_heuristic_method.py')
rfm_kmeans_path = os.path.join(directory, 'rfm_kmeans_method.py')
group_segmentation = os.path.join(directory, 'group_segmentation.py')

print(f"----------Starting data_cleaning.py----------\n")
subprocess.run([sys.executable, data_cleaning_path], check=True)

print(f"\n----------Starting rfm_table.py----------\n")
subprocess.run([sys.executable, rfm_table_path], check=True)

print(f"\n----------Starting rfm_heuristic_method.py----------\n")
subprocess.run([sys.executable, rfm_heuristic_path], check=True)

print(f"\n----------Starting rfm_kmeans_method.py----------\n")
subprocess.run([sys.executable, rfm_kmeans_path], check=True)

print(f"\n----------Starting group_segmentation.py----------\n")
subprocess.run([sys.executable, group_segmentation], check=True)

print(f"\n----------RFM pipeline executed successfully----------\n")