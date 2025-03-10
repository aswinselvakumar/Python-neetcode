# ==,!=,<,>,<=,>=
def check_equal(x,y)-> bool:
    return x==y
def check_not_equal(x,y)->bool:
    return x!= y
def check_less_than(x,y)->bool:
    return x < y
def check_greater_than(x,y)->bool:
    return x > y
def check_lessthan_equal(x,y)->bool:
    return x <= y
def check_greaterthan_equal(x,y)->bool:
    return x >= y

print(check_equal(2,2))
print(check_not_equal(-2,2))
print(check_less_than(2,3))
print(check_greater_than(3,1))
print(check_lessthan_equal(2,3))
print(check_greaterthan_equal(3,3))