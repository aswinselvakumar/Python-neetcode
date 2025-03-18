def pop_n(my_list:list[int],n:int)->list[int]:
    while n>0:
        my_list.pop()
        n-=1
    return my_list

print(pop_n([1,2,3,4],2))