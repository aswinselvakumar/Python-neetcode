def check_range(num:int)->str:
    if num < 0:
        return "Negative"
    elif num == 0:
        return "Zero"
    elif num >0 and num < 10:
        return "Positive single int"
    else:
        return "Positive multi digit"
    
print(check_range(100))