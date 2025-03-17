def check_element_list(lists:list,element:int)->bool:
    if element in lists:
        return True
    return False

print(check_element_list([1,2,3],4))
print(check_element_list([2,3,4],3))