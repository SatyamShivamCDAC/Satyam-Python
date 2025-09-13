def create_acc(acc_list,acc_id,balance = 0):
    acc_list[acc_id] = balance

def withdraw(acc_list,acc_id,amount):
    if acc_id not in acc_list.keys():
        print("Account doesn't exist")
    else:
        if amount > acc_list[acc_id]:
            print("Insufficient Funds")
        else:
            acc_list[acc_id] = acc_list[acc_id] - amount
            print(f"{amount} deducted \n current balance - {acc_list[acc_id]}")

def deposit(acc_list,acc_id,amount):
    if amount<0:
        print("Enter valid amount")
    else:
        acc_list[acc_id] += amount
        print(f"{amount} deopsited \n current balance - {acc_list[acc_id]}")

def checkbalance(acc_list,acc_id):
    print(f"Balance - {acc_list[acc_id]}")

def transfer_money(acc_list,sender_id,reciver_id,amount):
    if amount<0:
        print('Enter valid amount')
    else:
        if(amount>acc_list[sender_id]):
            print("sender does't have that amount")
        else:
            acc_list[sender_id] = acc_list[sender_id] - amount
            acc_list[reciver_id] = acc_list[reciver_id] - amount
            print(f" {amount}amount transfer from {sender_id} to {reciver_id}")