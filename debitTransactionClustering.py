import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

with open("transactions.json", "r") as json_file:
    data = json.load(json_file)

debit_transactions = [transaction for transaction in data["Transactions"] if transaction.get("CreditDebitIndicator") == "DBIT"]

X = np.array([[float(transaction["Amount"]), int(transaction["ValueDateTime"][:10].replace("-", ""))] for transaction in debit_transactions])

scaler = StandardScaler()
X = scaler.fit_transform(X)

n_clusters = 3

kmeans = KMeans(n_clusters=n_clusters, random_state=0)
kmeans.fit(X)

cluster_labels = kmeans.labels_

plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis')
plt.title("Debit Transaction Clusters")
plt.xlabel("Transaction Amount")
plt.ylabel("Transaction Date")
plt.show()
