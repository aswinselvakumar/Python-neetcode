my_dict = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

my_dict.pop("a")
my_dict.pop("d",0) #,0 avoids the error
print(my_dict)