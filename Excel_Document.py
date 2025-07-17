import pandas as pd

df = pd.read_csv(r"C:\Users\HP\OneDrive\Downloads\transactions.csv")

print(df.head())
print(df.to_string())

total_amount = df['amount'].sum()
most_frequent_status = df['pan'].mode()[0]
total_transactions = len(df)

print("Total Amount:", total_amount)
print("Most Frequent Status:", most_frequent_status)
print("Total Transactions:", total_transactions)