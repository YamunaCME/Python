class IsufficientBalanceError(Exception):
    pass

balance=5000
try:
    amount=float(input("enter withdrawal amount:"))
    if amount<=0:
        raise ValueError("amount must be greaterthan 0")
    if amount > balance:
        raise IsufficientBalanceError("insufficient amount")
    balance=balance-amount
    print("balance=",balance) 
except ValueError as e:
    print(e)   
except IsufficientBalanceError as i:
    print(i)         