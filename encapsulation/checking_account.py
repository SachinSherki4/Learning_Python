'''
Created on Oct 28, 2024

@author: ssherki
'''
from .bank_account import BankAccount

class CheckingAccount(BankAccount):
    
    def __init__(self,account_number,initial_balance=0,overdraft_limit=500):
        super().__init__(account_number,initial_balance=0)
        self.__overdraft_limit=overdraft_limit 
    
    def withdraw(self,amount):
        if 0 < amount <(self.get_balance()+self.__overdraft_limit):
            if amount < self.get_balance():
                print(f"Overdraft Used: ₹{amount - self.get_balance():.2f}")
            elif amount > self.get_balance():
                print(f"₹{amount} amount withdraw. Remaining Balance : ₹{self.get_balance()}")
        else:
            print(f"Invalid withdraw amount, exceeded Overdraft Limit.")
        
    def account_info(self):
        base_info=super().account_info()
        print(f"{base_info}, Overdraft Limit: ₹{self.overdraft_limit:.2f}")
        
        