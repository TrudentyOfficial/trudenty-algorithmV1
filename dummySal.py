import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from faker import Faker

# Create a Faker instance
fake = Faker()

# Define the number of transactions and salary amount
num_transactions = 100
salary_amount = 5000.00  # Assuming a fixed salary amount for this example

# Calculate the list of transaction dates for the 1st day of each month for six months
transaction_dates = [datetime(datetime.now().year, month, 1) for month in range(1, 7)]

# Create a list of transactions using list comprehension
transactions = [
    {
        "TransactionId": fake.random_int(min=1000000, max=9999999),
        "Amount": salary_amount,
        "Currency": "EUR",
        "CreditDebitIndicator": "CRDT",
        "Status": "BOOK",
        "BookingDateTime": date.isoformat(),
        "ValueDateTime": date.isoformat(),
        "RemittanceInformationUnstructured": "Salary Payment",
        "BankTransactionCode": {
            "Domain": {
                "DomainCode": "PMNT",
                "FamilyCode": "RCDT",
                "SubCode": "SALA"
            },
            "Proprietary": {
                "Code": "SalaryPayment",
                "Issuer": "BG"
            }
        },
        "CreditorAgent": {
            "Identification": "creditor_agent_identification"
        },
        "CreditorAccount": {
            "Identification": "DE78900900424711121212",
            "SchemeName": "IBAN",
            "Name": "Hansi Meier",
            "Currency": "EUR"
        },
        "DebtorAgent": {
            "Identification": "debtor_agent_identification"
        },
        "DebtorAccount": {
            "Identification": "DE87123456781234567891",
            "SchemeName": "IBAN",
            "Name": "Elias Book Store",
            "Currency": "EUR"
        },
        "PurposeCode": "SALA",
        "RemittanceInformationStructured": {
            "Reference": fake.uuid4(),
            "Type": "SCOR",
            "Issuer": "ISO"
        },
        "References": {
            "EndToEndId": fake.uuid4(),
            "MandateId": fake.uuid4(),
            "ChequeNumber": "check3",
            "TransactionReference": date.strftime('%Y%m%d-%H%M%S')
        },
        "RelatedParties": {
            "CreditorId": "creditor3",
            "UltimateCreditor": "Hansi Meier U",
            "UltimateDebtor": "Elias Book Store U"
        }
    }
    for date in transaction_dates for _ in range(num_transactions // 6)
]

# Save the list of transactions to a JSON file
with open('salary_transactions.json', 'w') as json_file:
    json.dump(transactions, json_file, indent=4)

print(f"Generated {num_transactions} salary transactions for 6 months and saved them to 'salary_transactions.json'.")
