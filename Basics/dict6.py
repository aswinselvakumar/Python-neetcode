def get_dict_keys(age_dict:dict[str,int])->list[str]:
    result = []
    for n in age_dict:
        result.append(n)
    return result
def get_dict_values(age_dict:dict[str,int])->list[int]:
    values = []
    for v in age_dict:
        values.append(v)
    return values

print(get_dict_keys({"a":1,"b":2,"c":3}))
print(get_dict_values({"a":1,"b":2,"c":3}))