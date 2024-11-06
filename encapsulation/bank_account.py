'''
Created on Oct 28, 2024

@author: ssherki
'''

class BankAccount :
    def __init__(self,account_number,initial_balance=0):
        self.__account_number=account_number # private 
        self.__balance=initial_balance  # private
    
    def deposit(self,amount):
        if 0 < amount : 
            self.__balance += amount
            print(f"Deposited  ₹{amount:.2f} New Balance : ₹{self.__balance:.2f}")
        else:
            print("Deposited amount must be positive")
    
    def withdraw(self,amount):
        if 0 < amount and amount <=self.__balance:
            self.__balance -= amount 
            print(f"Amount withdraw : ₹{amount} Remaining Balance : ₹{self.__balance}")
        else:
            print("Invalid withdrawal amount.")
    
    def get_balance(self):
        return self.__balance
    
    def account_info(self):
        return f"Account Number : {self.__account_number} Balance : ₹{self.__balance}"
    
    
    
    
    
    
    
    
    
    
    