from Assignments.class_asignments.day4.account import create_acc
from day4 import demo_string as ds
from day4 import account

accounts = {}

account.create_acc(accounts,101,50000)
account.create_acc(accounts,102)
account.create_acc(accounts,103,15000)

account.withdraw(accounts,101,50)
account.deposit(accounts,101,5000)
account.transfer_money(accounts,101,102,5000)
print(accounts)