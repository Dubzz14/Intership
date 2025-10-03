import json
import psycopg2

class BankAccount:
    def __init__(self, Account_number, name, amount, pin):
        self.Account_number = Account_number
        self.name = name
        self.amount = amount
        self.pin = pin
        self.transaction_history = []

    def withdraw(self, w_amount):
        if w_amount > self.amount:
            print("Insuffisient funds")
        else:
            balance_before = self.amount
            self.amount = self.amount - w_amount
            self.transaction_history.append(f"Withdrawal: {w_amount}")
            self.store_transaction(self.name, balance_before, self.amount, w_amount, "Withdrawal", self.Account_number)
            return (f'You have successfully withdrawn {w_amount}')
        
    
    def deposit(self, d_amount):
        balance_before = self.amount
        self.amount = d_amount + self.amount
        self.transaction_history.append(f"Deposit: {d_amount}")
        self.store_transaction(self.name,  balance_before, self.amount, d_amount, "Deposit", self.Account_number)
        return (f'You have successfully deposited {d_amount}')
    
    def check_balance(self):
        return self.amount
    
    def store_transaction(self, name,balance_before, balance_after, amount, transaction_type, account_number):
        self.transaction_history.append({"name":name, "balance_before": balance_before,"balance_after":balance_after,"amount":amount, "transaction type": transaction_type, "account number": account_number})
        
        pyth_data = self.transaction_history

        connection = psycopg2.connect(dbname = "showroom", user = "postgres", password = "ezeh", host ="localhost")

        cur = connection.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS transactions (name TEXT, balance_before INTEGER, balance_after INTEGER, amount INTEGER, transaction_type TEXT, account_number INTEGER);")
        
        for record in pyth_data:
            if not isinstance(record, dict):
                continue
        
        cur.execute("INSERT INTO transactions (name,balance_before, balance_after, amount, transaction_type, account_number) VALUES(%s,%s,%s,%s,%s,%s)", (record['name'], record['balance_before'], record['balance_after'], record['amount'], record['transaction type'], record['account number']))

        connection.commit()
        print("Data successfully moved")

        cur.execute("SELECT * FROM transactions")
        data_from_db = cur.fetchall()
        print (data_from_db)

        cur.close()
        connection.close()


    def transfer(self, t_amount, recepient_account,pin):
        if t_amount > self.amount:
            print("Insuffiient balance.")
        else:
            print(input("Your pin: "))
            if pin != self.pin:
                print("Incorrect pin")
            else:
                pin = self.pin
                self.amount -= t_amount
                recepient_account.amount += t_amount
                print(f"Transfer successful! Sent ₦{t_amount} to {recepient_account.name}.")
                print(f"Your new balance is ₦{self.amount}.")





david = BankAccount(22233456, 'David', 35000, 0000)
john = BankAccount(23234567, 'John', 45000, 0000)

print(david.check_balance())
print(john.check_balance())

print(david.withdraw(3000))
print(john.withdraw(4575))

print(david.check_balance())
print(john.check_balance())

print(david.deposit(20000))
print(john.deposit(500000))

print(david.check_balance())
print(john.check_balance())

print(david.transfer(5000, john, 0000))

print("The transaction history for david:", david.transaction_history)
print("The transaction history for john:", john.transaction_history)