import json
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Account details
account = {
    "AccountId": "178012",
    "Transactions": []
}

# Generate transactions for the past six months
today = datetime.now()
for _ in range(6):
    # Generate one salary transaction for this month
    salary_transaction = {
        "TransactionId": fake.uuid4(),
        "Amount": "{:.2f}".format(random.uniform(2000, 4000)),
        "Currency": "EUR",
        "CreditDebitIndicator": "CRDT",
        "Status": "BOOK",
        "BookingDateTime": today.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ValueDateTime": today.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "RemittanceInformationUnstructured": "Salary Payment",
        "BankTransactionCode": {
            "Domain": {"DomainCode": "PMNT", "FamilyCode": "RCDT", "SubCode": "SALA"},
            "Proprietary": {"Code": "SalaryPayment", "Issuer": "BG"},
        },
        "CreditorAgent": {"Identification": "creditor_agent_identification"},
        "CreditorAccount": {
            "Identification": "DE78900900424711121212",
            "SchemeName": "IBAN",
            "Name": "Hansi Meier",
            "Currency": "EUR",
        },
        "DebtorAgent": {"Identification": "debtor_agent_identification"},
        "DebtorAccount": {
            "Identification": "DE87123456781234567891",
            "SchemeName": "IBAN",
            "Name": "Elias Book Store",
            "Currency": "EUR",
        },
        "PurposeCode": "SALA",
        "RemittanceInformationStructured": {
            "Reference": "RF18539007547034",
            "Type": "SCOR",
            "Issuer": "ISO",
        },
        "References": {
            "EndToEndId": fake.uuid4(),
            "MandateId": fake.uuid4(),
            "ChequeNumber": fake.uuid4(),
            "TransactionReference": today.strftime("%Y%m%d"),
        },
        "RelatedParties": {
            "CreditorId": fake.uuid4(),
            "UltimateCreditor": "Hansi Meier U",
            "UltimateDebtor": "Elias Book Store U",
        },
    }

    account["Transactions"].append(salary_transaction)

    # Generate additional random transactions for this month
    for _ in range(19): 
        random_transaction = {
            "TransactionId": fake.uuid4(),
            "Amount": "{:.2f}".format(random.uniform(10, 500)),
            "Currency": "EUR",
            "CreditDebitIndicator": random.choice(["CRDT", "DBIT"]),
            "Status": "BOOK",
            "BookingDateTime": today.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "ValueDateTime": today.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "RemittanceInformationUnstructured": fake.sentence(),
            "BankTransactionCode": {
                "Domain": {
                    "DomainCode": fake.word(),
                    "FamilyCode": fake.word(),
                    "SubCode": fake.word(),
                },
                "Proprietary": {"Code": fake.word(), "Issuer": fake.word()},
            },
            "CreditorAgent": {"Identification": fake.uuid4()},
            "CreditorAccount": {
                "Identification": fake.uuid4(),
                "SchemeName": fake.word(),
                "Name": fake.name(),
                "Currency": "EUR",
            },
            "DebtorAgent": {"Identification": fake.uuid4()},
            "DebtorAccount": {
                "Identification": fake.uuid4(),
                "SchemeName": fake.word(),
                "Name": fake.name(),
                "Currency": "EUR",
            },
            "PurposeCode": fake.word(),
            "RemittanceInformationStructured": {
                "Reference": fake.uuid4(),
                "Type": fake.word(),
                "Issuer": fake.word(),
            },
            "References": {
                "EndToEndId": fake.uuid4(),
                "MandateId": fake.uuid4(),
                "ChequeNumber": fake.uuid4(),
                "TransactionReference": today.strftime("%Y%m%d"),
            },
            "RelatedParties": {
                "CreditorId": fake.uuid4(),
                "UltimateCreditor": fake.name(),
                "UltimateDebtor": fake.name(),
            },
        }

        account["Transactions"].append(random_transaction)

    # Move back one month for the next iteration
    today -= timedelta(days=30)

# Save the transactions to a JSON file
with open("transactions.json", "w") as json_file:
    json.dump(account, json_file, indent=4)

print("Transactions saved to 'transactions.json'")
