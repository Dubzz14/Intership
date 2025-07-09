class BankAccount:
    def __init__(self, Account_number, name, amount):
        self.Account_number = Account_number
        self.name = name
        self.amount = amount

    def withdraw(self, w_amount):
        if w_amount > self.amount:
            print("Insuffisient funds")
        else:
            self.amount = self.amount - w_amount
            return (f'You have successfully withdrawn {w_amount}')
        
    
    def deposit(self, d_amount):
        print("Your account does not support this transaction")
        self.amount = d_amount + self.amount
        return (f'You have successfully Deposited {d_amount}')
    
    def check_balance(self):
        return self.amount
    
david_ac1 = BankAccount(22233456, 'David', 35000)
david_ac2 = BankAccount(23234567, 'David', 45000)

print(david_ac1.check_balance())
print(david_ac2.check_balance())

print(david_ac1.withdraw(3000))
print(david_ac2.withdraw(4575))

print(david_ac1.check_balance())
print(david_ac2.check_balance())

print(david_ac1.deposit(20000))
print(david_ac2.deposit(500000))

print(david_ac1.check_balance())
print(david_ac2.check_balance())


class Retirement_fund(BankAccount):
    def __init__(self, retirement_age, amount, name, Account_number, pension_type):
        super().__init__(Account_number, name, amount)
        self.retirement_age = retirement_age
        self.pension_type = pension_type

    def check_retirement_age(self):
        if self.retirement_age > 60:
            return("Unable to withdraw pension due to being above age limit")
        else:
            return(f'You have successfully withdrawn your pension due to being {self.retirement_age} and registerd under {self.pension_type} pension')

Ngozi_ci1 = Retirement_fund(59,56000, 'Ngozi', 22339867, 'Goverment' )
Ngozi_ci2 = Retirement_fund(55,65000, 'Ngozi', 22334567, None  )

print (Ngozi_ci1.check_retirement_age())
print (Ngozi_ci2.check_retirement_age())

transaction_history = []

def store_transaction(name, amount, transaction_type, account_number):
    transaction_history.append({"name":name, "amount":amount, "transaction type": transaction_type, "account number": account_number})