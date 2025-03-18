def remove_from_list(my_list:list[int],index:int)->list[int]:
    my_list.pop(index)
    return my_list

print(remove_from_list([1,2,3,4,5],2))