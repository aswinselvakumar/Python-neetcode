def first_char(name:str)->str:
    return name[:1]
def second_char(name:str)->str:
    return name[1:2]
def last_char(name:str)->str:
    return name[:len(name)-1]

print(first_char("Aswin"))
print(second_char("Lohith"))
print(last_char("Dharun"))