import json
from datetime import datetime
import matplotlib.pyplot as plt

with open("generated_transactions.json", "r") as json_file:
    data = json.load(json_file)


paypal_transactions = [transaction for transaction in data["Transactions"] if
                      transaction["BankTransactionCode"]["Proprietary"]["Code"] == "PayPal"]

paypal_transaction_dates = [datetime.strptime(transaction["ValueDateTime"], "%Y-%m-%dT%H:%M:%S.%f") for transaction in paypal_transactions]
paypal_transaction_amounts = [float(transaction["Amount"]) for transaction in paypal_transactions]


plt.figure(figsize=(10, 6))


size_factor = 100
sizes = [size_factor] * len(paypal_transaction_dates)

plt.scatter(paypal_transaction_dates, paypal_transaction_amounts, c='b', s=sizes, alpha=0.5)

plt.title("PayPal Transactions")
plt.xlabel("Transaction Date")
plt.ylabel("Amount (EUR)")
plt.grid(True)
plt.gca().invert_yaxis()  
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
