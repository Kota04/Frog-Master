import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_folder(folder_name):
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
    except OSError as e:
        logging.error(f"Error: Failed to create the directory {folder_name}. Exception: {e}")

# Create necessary folders
create_folder('./importance_plots/')

# List CSV files in the attacks folder
csv_files = [file for file in os.listdir('./attacks/') if file.endswith('.csv')]
main_labels=["Flow Duration","Total Fwd Packets",   "Total Backward Packets","Total Length of Fwd Packets","Total Length of Bwd Packets","Fwd Packet Length Max","Fwd Packet Length Min",
   "Fwd Packet Length Mean","Fwd Packet Length Std","Bwd Packet Length Max","Bwd Packet Length Min","Bwd Packet Length Mean","Bwd Packet Length Std",
   "Flow Bytes/s","Flow Packets/s","Flow IAT Mean","Flow IAT Std","Flow IAT Max","Flow IAT Min","Fwd IAT Total","Fwd IAT Mean","Fwd IAT Std","Fwd IAT Max",
   "Fwd IAT Min","Bwd IAT Total","Bwd IAT Mean","Bwd IAT Std","Bwd IAT Max","Bwd IAT Min","Fwd PSH Flags","Bwd PSH Flags","Fwd URG Flags","Bwd URG Flags",
   "Fwd Header Length","Bwd Header Length","Fwd Packets/s","Bwd Packets/s","Min Packet Length","Max Packet Length","Packet Length Mean","Packet Length Std",
   "Packet Length Variance","FIN Flag Count","SYN Flag Count","RST Flag Count","PSH Flag Count","ACK Flag Count","URG Flag Count","CWE Flag Count",
   "ECE Flag Count","Down/Up Ratio","Average Packet Size","Avg Fwd Segment Size","Avg Bwd Segment Size","Fwd Avg Bytes/Bulk",
   "Fwd Avg Packets/Bulk","Fwd Avg Bulk Rate","Bwd Avg Bytes/Bulk","Bwd Avg Packets/Bulk","Bwd Avg Bulk Rate","Subflow Fwd Packets","Subflow Fwd Bytes",
   "Subflow Bwd Packets","Subflow Bwd Bytes","Init_Win_bytes_forward","Init_Win_bytes_backward","act_data_pkt_fwd",
   "min_seg_size_forward","Active Mean","Active Std","Active Max","Active Min",
    "Idle Mean","Idle Std","Idle Max", "Idle Min","Label"]

with open("importance_list_for_attack_files.csv", "w") as importance_file:
    for j in csv_files:
        logging.info(f"Processing file: {j}")
        df = pd.read_csv(f'./attacks/{j}',usecols=main_labels)

        
        logging.info(f"Shape of {j}: {df.shape}")

        # Encode the label column as binary
        df["Label"] = df["Label"].apply(lambda x: 1 if x == "BENIGN" else 0)
        y = df["Label"].values
        x = df.drop(["Label"], axis=1)
        X=np.float32(x)
        # Ensuring proper data types
        X[np.isnan(X)] = 0
        X[np.isinf(X)] = 0
        
        # Training the model
        forest = RandomForestRegressor(n_estimators=250, random_state=0)
        forest.fit(X, y)

        # Calculating Feature Importance
        importances = forest.feature_importances_
        std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
        indices = np.argsort(importances)[::-1]

        # Top 20 features
        top_features = pd.DataFrame({
            'Features': x.columns[indices[:20]],
            'Importance': importances[indices[:20]]
        }).sort_values('Importance', ascending=False).set_index('Features')

        plt.figure(figsize=(10, 5))
        top_features.plot(kind='bar')
        plt.title(f"{j[:-4]} Attack - Feature Importance")
        plt.ylabel('Importance')
        plt.savefig(f"./importance_plots/{j[:-4]}.pdf", bbox_inches='tight', format='pdf')
        plt.close()

        top_5_features = top_features.head(5).index.tolist()
        importance_line = f"{j[:-4]}={top_5_features}\n"
        importance_file.write(importance_line)

        print(f"{j[:-4]} importance list:")
        print(top_features.head(20), "\n")
        logging.info(f"Feature importance plot saved for {j}")

logging.info("Processing completed.")
