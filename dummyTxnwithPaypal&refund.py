import json
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

paypal_debit_transactions = []
for _ in range(10):
    transaction = {
        "TransactionId": fake.random_int(min=1000000, max=9999999),
        "Amount": round(random.uniform(10, 500), 2),  
        "Currency": "EUR",
        "CreditDebitIndicator": "DBIT",
        "Status": "BOOK",
        "BookingDateTime": datetime.now().isoformat(),
        "ValueDateTime": datetime.now().isoformat(),
        "RemittanceInformationUnstructured": fake.sentence(),
        "BankTransactionCode": {
            "Domain": {
                "DomainCode": "PMNT",
                "FamilyCode": "RCDT",
                "SubCode": "SALA"
            },
            "Proprietary": {
                "Code": "PayPalPayment",
                "Issuer": "PayPal"
            }
        }
    }
    paypal_debit_transactions.append(transaction)


amazon_refund_transactions = []
for _ in range(10):
    transaction = {
        "TransactionId": fake.random_int(min=1000000, max=9999999),
        "Amount": round(random.uniform(10, 500), 2),  
        "Currency": "EUR",
        "CreditDebitIndicator": "CRDT",
        "Status": "BOOK",
        "BookingDateTime": datetime.now().isoformat(),
        "ValueDateTime": datetime.now().isoformat(),
        "RemittanceInformationUnstructured": fake.sentence(),
        "BankTransactionCode": {
            "Domain": {
                "DomainCode": "PMNT",
                "FamilyCode": "RCDT",
                "SubCode": "SALA"
            },
            "Proprietary": {
                "Code": "AmazonRefund",
                "Issuer": "Amazon"
            }
        }
    }
    amazon_refund_transactions.append(transaction)


monthly_salary = 2000.00


transactions = []

for i in range(6):
    salary_transaction = {
        "TransactionId": fake.random_int(min=1000000, max=9999999),
        "Amount": round(monthly_salary, 2),  # Consistent monthly salary
        "Currency": "EUR",
        "CreditDebitIndicator": "CRDT",
        "Status": "BOOK",
        "BookingDateTime": (datetime.now() - timedelta(days=i * 30)).isoformat(),
        "ValueDateTime": (datetime.now() - timedelta(days=i * 30)).isoformat(),
        "RemittanceInformationUnstructured": fake.sentence(),
        "BankTransactionCode": {
            "Domain": {
                "DomainCode": "PMNT",
                "FamilyCode": "RCDT",
                "SubCode": "SALA"
            },
            "Proprietary": {
                "Code": "SalaryPayment",
                "Issuer": "YourCompany"
            }
        }
    }
    transactions.append(salary_transaction)

transactions.extend(paypal_debit_transactions)
transactions.extend(amazon_refund_transactions)

transaction_data = {
    "AccountId": "178012",
    "Transactions": transactions
}

with open("transactions.json", "w") as json_file:
    json.dump(transaction_data, json_file, indent=2)

print("Transactions generated and saved to transactions.json")
