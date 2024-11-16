
#from encapsulation.bank_account import BankAccount
from encapsulation.saving_account import SavingAccount
from encapsulation.checking_account import CheckingAccount

savings=SavingAccount("S12345",500)
savings.deposit(250)
savings.withdraw(620)
savings.apply_interest()
print(savings.get_balance())

check_acc=CheckingAccount("S12345",500)
check_acc.deposit(380)
print(check_acc.get_balance())
check_acc.withdraw(780)