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
        return (f'You have successfully Deposited {d_amount}')
    
    def check_balance(self):
        return self.amount
    
    def store_transaction(self, name,balance_before, balance_after, amount, transaction_type, account_number):
        self.transaction_history.append({"name":name, "balance_before": balance_before,"balance_after":balance_after,"amount":amount, "transaction type": transaction_type, "account number": account_number})


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
                






david_ac1 = BankAccount(22233456, 'David', 35000, 0000)
david_ac2 = BankAccount(23234567, 'David', 45000, 0000)

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

print(david_ac1.transfer(5000, david_ac2, 0000))

print("The transaction history for david_ac1:", david_ac1.transaction_history)
print("The transaction history for david_ac2:", david_ac2.transaction_history)

class Retirement_fund(BankAccount):
    def __init__(self, retirement_age, amount, name, Account_number, pension_type, pin=0):
        super().__init__(Account_number, name, amount, pin)
        self.retirement_age = retirement_age
        self.pension_type = pension_type

    def check_retirement_age(self):
        if self.retirement_age > 60:
            return("Unable to withdraw pension due to being above age limit")
        else:
            return(f'You have successfully withdrawn your pension due to being {self.retirement_age} and registerd under {self.pension_type} pension')

Ngozi_ci1 = Retirement_fund(59,56000, 'Ngozi', 22339867, 'Goverment', 0 )
Ngozi_ci2 = Retirement_fund(55,65000, 'Ngozi', 22334567, None, 0 )

print (Ngozi_ci1.check_retirement_age())
print (Ngozi_ci2.check_retirement_age())