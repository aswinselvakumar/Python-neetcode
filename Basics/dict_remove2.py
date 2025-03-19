def remove_keys(my_dict:dict[str,int],keys:list[str])->dict[str,int]:
    for k in keys:
        my_dict.pop(k)
    return my_dict

print(remove_keys({"a":1,"b":2,"c":3},["a","c"]))