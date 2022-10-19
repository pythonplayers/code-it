class Account():
    def __init__(self,accnum,holdername,balance):
        self.accnum=accnum
        self.holdername=holdername
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def withdrawal(self,amount):
        if (self.balance-amount)>=1000:
            self.balance-=amount
            return 1
        else:
            return 0

if __name__=='__main__':
    accnum=int(input())
    holdername=input()
    balance=input()
    ac1=Account(accnum,holdername,balance)
    damt=int(input())
    wamt=int(input())
    print(ac1.deposit(damt))
    res=ac1.withdrawal(wamt)
    if res==1:
        print("Avail",ac1.balance)
    else:
        print("Insufficient Balance")