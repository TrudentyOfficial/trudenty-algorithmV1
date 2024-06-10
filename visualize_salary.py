import json
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import datetime, timedelta
import numpy as np


with open('salary_transactions.json', 'r') as json_file:
    transactions = json.load(json_file)

salary_amounts = [transaction["Amount"] for transaction in transactions]
average_salary = sum(salary_amounts) / len(salary_amounts)

print(f"The average salary is: {average_salary:.2f} EUR")
dates = [datetime.fromisoformat(transaction["BookingDateTime"]) for transaction in transactions]
amounts = [transaction["Amount"] for transaction in transactions]

#  the total salary for each month
month_totals = {}
for date, amount in zip(dates, amounts):
    key = date.strftime('%Y-%m')  # Group by year and month
    if key in month_totals:
        month_totals[key] += amount
    else:
        month_totals[key] = amount

# Extract months and corresponding total salary amounts
months = list(month_totals.keys())
total_salary = list(month_totals.values())

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(months, total_salary, color='blue')
plt.xlabel("Month")
plt.ylabel("Total Salary Amount (EUR)")
plt.title("Total Monthly Salary Credits")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
