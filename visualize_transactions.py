import json
import matplotlib.pyplot as plt

with open('transactions.json', 'r') as json_file:
    transactions = json.load(json_file)

amounts = [transaction["Amount"] for transaction in transactions]

plt.bar(range(len(amounts)), amounts)
plt.xlabel("Transaction Index")
plt.ylabel("Transaction Amount")
plt.title("Transaction Amounts")
plt.xticks(range(len(amounts)), range(1, len(amounts) + 1)) 

plt.tight_layout()
plt.show()
plt.savefig('transaction_plot.png')

