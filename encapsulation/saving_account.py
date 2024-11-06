'''
Created on Oct 28, 2024

@author: ssherki
'''
from .bank_account import BankAccount

class SavingAccount(BankAccount):
    def __init__(self,account_number,initial_balance=0,interest_rate=0.02):
        super().__init__(account_number,initial_balance=0)
        self.__interest_rate=interest_rate
        
    def apply_interest(self):
        # as balance is private so we calling this method which return balance 
        interest=self.get_balance() * self.__interest_rate 
        # deposit method accept amount and add this into your bank balance
        self.deposit(interest)
        print(f"Interest added : {self.__interest_rate * 100:.2f} New Bank Balance : ₹{self.get_balance() +self.__interest_rate*100:.2f}")
    
    def account_info(self):
        base_info=super().account_info()
        print(f"{base_info}, Interest Rate : {self.interest_rate *100 :.2f}")
    