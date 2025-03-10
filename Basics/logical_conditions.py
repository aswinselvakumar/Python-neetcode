def discount_applies(age:int)->bool:
    if age<18 or age>=65:
        return True
    else:
        return False
    
print(discount_applies(17))
print(discount_applies(50))
print(discount_applies(70))