def pay_bill(balance:int,bill:int)->None:
    if balance >= bill:
        balance -= bill
        return balance
    return balance

print(pay_bill(100,50))
print(pay_bill(100,100))
print(pay_bill(100,150))
     
    