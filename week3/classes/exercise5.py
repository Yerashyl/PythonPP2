class bank_account():
    def __init__(self, owner, balance=0.0):
        self.owner=owner
        self.balance=balance
    def deposit(self, deposit_sum):
        self.balance += deposit_sum
        print(f"{deposit_sum} has been added to the account balance.")
    def withdraw(self, withdraw_sum):
        if (self.balance-withdraw_sum>=0):
            self.balance -= withdraw_sum
            print(f"{withdraw_sum} has been withdrawn from the account.")
        else:
            print("Insufficient balance")
    def balance(self):
        print(self.balance)
s = ""
print("Your Name")
o = input()
ex = bank_account(o)
while (s != "Exit"):
    print("deposit or withdraw or back or balance")
    next = input()
    if (next=='deposit'):
        print("Enter sum of deposit:")
        ds = int(input())
        ex.deposit(ds)
    elif (next=='withdraw'):
        print("Enter sum of withdraw:")
        ws = int(input())
        ex.withdraw(ws)
    elif (next=='back'):
        print('please enter Exit or Continue')
        s = input()
    elif (next=="balance"):
        ex.balance()