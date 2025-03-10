#falsey -> false,none,0,0.0," ",[]
#truethy ->true,any int,any float ,any list

def is_truthy(value) ->str:
    if value:
        return "truthy"
    else:
        return "Falsey"

print(is_truthy(0))
print(is_truthy(1))